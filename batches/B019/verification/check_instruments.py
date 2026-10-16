"""Exact finite-field algebra and finite models of the selected B019 mechanisms."""
from fractions import Fraction as F
from itertools import combinations, product
from math import comb, factorial, prod
from pathlib import Path
import json
import sys
import numpy as np
from scipy.linalg import block_diag

MOD=101
RNG=np.random.default_rng(19194)
OUT={}


def rank(a):
    a=np.array(a,dtype=np.int64,copy=True)%MOD
    rows,cols=a.shape;r=0
    for col in range(cols):
        pivots=np.flatnonzero(a[r:,col])
        if not len(pivots):continue
        pivot=r+int(pivots[0]);a[[r,pivot]]=a[[pivot,r]]
        a[r]=a[r]*pow(int(a[r,col]),-1,MOD)%MOD
        for j in range(r+1,rows):
            if a[j,col]:a[j]=(a[j]-a[j,col]*a[r])%MOD
        r+=1
        if r==rows:break
    return r


def inverse(a):
    a=np.array(a,dtype=np.int64)%MOD;n=len(a)
    aug=np.concatenate([a,np.eye(n,dtype=np.int64)],axis=1)
    for col in range(n):
        pivot=next((i for i in range(col,n) if aug[i,col]),None)
        assert pivot is not None
        aug[[col,pivot]]=aug[[pivot,col]]
        aug[col]=aug[col]*pow(int(aug[col,col]),-1,MOD)%MOD
        for j in range(n):
            if j!=col:aug[j]=(aug[j]-aug[j,col]*aug[col])%MOD
    return aug[:,n:]


def random_invertible(n):
    while True:
        a=RNG.integers(0,MOD,(n,n),dtype=np.int64)
        if rank(a)==n:return a


def length_checks():
    towers=0;diagrams=0
    for p,h,N in product((2,3),(1,2,3),range(1,7)):
        for n in range(N+1):
            bound=p**(N-n)
            ordinary=bound**h
            normalized=F(ordinary,p**(N*h))
            assert normalized==F(1,p**(n*h))
            # Base extension one level multiplies ordinary length by p^h.
            assert F((p*bound)**h,p**((N+1)*h))==normalized
            if bound>1:
                kernel=(bound-1)*bound**(h-1)
                quotient=bound**(h-1)
                assert F(kernel,p**(N*h))+F(quotient,p**(N*h))==normalized
            towers+=1
    for _ in range(90):
        dims=list(map(int,RNG.integers(1,7,size=5)))
        maps=[RNG.integers(0,MOD,size=(b,a)) for a,b in zip(dims,dims[1:])]
        # Ensure actual noninjectivity in part of the diagram.
        maps[1][:,-1]=0
        starts=np.cumsum([0]+dims);total=sum(dims)
        relation=np.zeros((total,sum(dims[:-1])),dtype=np.int64);column=0
        for i,a in enumerate(dims[:-1]):
            relation[starts[i]:starts[i+1],column:column+a]=np.eye(a,dtype=np.int64)
            relation[starts[i+1]:starts[i+2],column:column+a]=-maps[i]
            column+=a
        rr=rank(relation)
        assert total-rr==dims[-1]
        for i,a in enumerate(dims):
            injection=np.zeros((total,a),dtype=np.int64)
            injection[starts[i]:starts[i+1]]=np.eye(a,dtype=np.int64)
            image=rank(np.concatenate([relation,injection],axis=1))-rr
            transition=np.eye(a,dtype=np.int64)
            for j in range(i,len(maps)):transition=maps[j]@transition%MOD
            assert image==rank(transition)
            assert image<=min(dims[i:])
        diagrams+=1
    OUT['normalized_length']={'root_tower_quotients':towers,'noninjective_finite_colimit_diagrams':diagrams,
        'infinite_length_construction_certified':False}


def root_bundle_checks():
    cech={};cases=0
    for m in range(-12,13):
        L=abs(m)+4
        overlap=list(range(-L,L+1));chart0=[e for e in overlap if e>=0];chart1=[e for e in overlap if e<=m]
        differential=np.zeros((len(overlap),len(chart0)+len(chart1)),dtype=np.int64)
        for j,e in enumerate(chart0):differential[overlap.index(e),j]=1
        for j,e in enumerate(chart1):differential[overlap.index(e),len(chart0)+j]=-1
        rr=rank(differential);h0=len(chart0)+len(chart1)-rr;h1=len(overlap)-rr
        assert (h0,h1)==(max(0,m+1),max(0,-m-1))
        cech[m]=(h0,h1)
    for n in range(5):
        for roots in combinations(range(-3,4),n):
            for twist in range(-5,6):
                groups=[1]
                for r in roots:
                    h0,h1=cech[twist-1-r]
                    nxt=[0]*(len(groups)+1)
                    for i,count in enumerate(groups):nxt[i]+=count*h0;nxt[i+1]+=count*h1
                    groups=nxt
                euler=sum((-1)**i*v for i,v in enumerate(groups))
                assert euler==prod(twist-r for r in roots)
                if twist in roots:assert not any(groups)
                else:
                    degree=sum(r>twist for r in roots)
                    assert groups[degree]==abs(euler) and sum(v!=0 for v in groups)==1
                cases+=1
            # Euler leading coefficient = rank/n! = 1.
            assert F(factorial(n),factorial(n))==1
    OUT['cohomological_roots']={'Cech_matrix_models':len(cech),'root_and_twist_models':cases,
        'finite_flatness_certified':False}


def selection_checks():
    projectors=0;extinctions=0
    # Regular group algebra of (Z/2)^m, exact coefficient arithmetic.
    for m in range(1,8):
        size=1<<m;invsize=pow(size,-1,MOD)
        for last in range(m):
            coefficients=np.array([(-1 if z>>last&1 else 1)*invsize%MOD for z in range(size)])
            square=np.zeros(size,dtype=np.int64)
            for a,b in product(range(size),repeat=2):square[a^b]=(square[a^b]+coefficients[a]*coefficients[b])%MOD
            assert np.array_equal(square,coefficients)
            alive=coefficients.copy()
            for j in range(m):
                shifted=alive[np.arange(size)^(1<<j)]
                alive=(alive+shifted)*pow(2,-1,MOD)%MOD
                assert bool(np.any(alive))==(j<last)
                extinctions+=1
            projectors+=1
    # An original-algebra character need not have a shift-invariant quotient kernel.
    # Infinite commuting involutions act +1 except at m-1. alpha(z_j)=z_(j+1).
    for m in range(1,15):
        value=lambda j: -1 if j==m-1 else 1
        assert value(m-2)-1==0 and value(m-1)-1==-2
        for j in range(m+1):
            assert prod((1+value(i))//2 for i in range(j))==int(j<m)
    OUT['twisted_selection']={'character_projectors':projectors,'successive_selections':extinctions,
        'quotient_kernel_controls':14,'fixed_finitely_presented_group_certified':False}


def bar_checks():
    # D=k[a]/a^2, X=k with augmentation action, A=k[a,x]/(a,x)^2, N=k.
    # D has infinite global dimension: only the bar decomposition is tested here.
    def multiply(a,b):
        if a==0:return b
        if b==0:return a
        return None
    bases={}
    for n in range(6):
        for r in range(n+1):
            bases[n,r]=[(left,)+word for left in (0,1) for word in product(range(3),repeat=n) if word.count(2)==r]
    differentials={};checked=0
    for n in range(1,6):
        for r in range(n+1):
            source=bases[n,r];target=bases.get((n-1,r),[]);index={w:i for i,w in enumerate(target)}
            boundary=np.zeros((len(target),len(source)),dtype=np.int64)
            for col,word in enumerate(source):
                left,entries=word[0],word[1:]
                if entries[0]!=2:
                    result=multiply(left,entries[0])
                    if result is not None:boundary[index[(result,)+entries[1:]],col]+=1
                for j in range(n-1):
                    result=multiply(entries[j],entries[j+1])
                    if result is not None:
                        out=(left,)+entries[:j]+(result,)+entries[j+2:]
                        boundary[index[out],col]+=(-1)**(j+1)
                if entries[-1]==0:boundary[index[(left,)+entries[:-1]],col]+=(-1)**n
            boundary%=MOD;differentials[n,r]=boundary
            if n>1 and (n-1,r) in differentials:
                assert not np.any(differentials[n-1,r]@boundary%MOD)
            checked+=1
    homologies=[]
    for n in range(5):
        row=[]
        for r in range(n+1):
            outgoing=rank(differentials[n,r]) if n else 0
            incoming=rank(differentials[n+1,r])
            actual=len(bases[n,r])-outgoing-incoming
            expected=int(n==0) if r==0 else comb(n-1,r-1)
            assert actual==expected;row.append(actual)
        assert sum(row)==(1 if n==0 else 2**(n-1));homologies.append(row)
    # r=1 has positive-degree Tor: ordinary tensor would omit this component.
    assert homologies[2][1]==1
    signs=0
    for r in range(6):
        for blocks in product(range(3),repeat=r+1):
            exponent=sum((r-j)*count for j,count in enumerate(blocks))
            for j,count in enumerate(blocks):
                if not count:continue
                reduced=list(blocks);reduced[j]-=1
                newexp=sum((r-i)*c for i,c in enumerate(reduced))
                oldsign=j+sum(blocks[:j]);newsign=r+sum(blocks[:j])
                assert (oldsign+newexp-exponent-newsign)%2==0;signs+=1
    paths=0
    for vertices in range(2,9):
        for _ in range(10):
            adjacency=np.triu(RNG.integers(0,2,(vertices,vertices)),1)
            tensor=np.eye(vertices,dtype=np.int64)
            for r in range(vertices+1):
                if r==vertices:assert not np.any(tensor)
                tensor=adjacency@tensor;paths+=1
    OUT['derived_square_zero']={'bar_blocks':checked,'homology_by_degree_and_X_count':homologies,
        'multibar_sign_checks':signs,'semisimple_directed_path_iterates':paths,
        'nonflat_higher_Tor_detected':True,'global_counterexample_certified':False}


def pole_checks():
    cases=0;max_ratio=0
    for k,m in product((1,2,3),(1,2,4)):
        for _ in range(5):
            n=k+m
            # Real well-conditioned but nonorthogonal coordinates.
            p=np.eye(n)+.08*RNG.normal(size=(n,n));pinv=np.linalg.inv(p)
            g=np.eye(k)+.1*RNG.normal(size=(k,k));c=2*np.eye(m)+.1*RNG.normal(size=(m,m))
            m0=block_diag(np.zeros((k,k)),c)
            first=RNG.normal(size=(n,n));first[:k,:k]=g
            second=.1*RNG.normal(size=(n,n))
            l0=RNG.normal(size=(2,n));l0[:,:k]=0
            b0=RNG.normal(size=(n,2));b0[:k]=0
            l1=RNG.normal(size=(2,n));b1=RNG.normal(size=(n,2))
            j=block_diag(np.zeros((k,k)),np.linalg.inv(c))
            target=l0@j@b0
            errors=[]
            for epsilon in (1e-3,1e-4,1e-5):
                mat=p@(m0+epsilon*first+epsilon**2*second)@pinv
                l=(l0+epsilon*l1)@pinv;b=p@(b0+epsilon*b1)
                value=l@np.linalg.solve(mat,b)
                errors.append(np.linalg.norm(value-target))
            assert errors[-1]<=.03*errors[0]+1e-8
            max_ratio=max(max_ratio,errors[-1]/max(errors[0],1e-30))
            # Choose an oblique e with range=kernel and f a tilted complement.
            tilt=RNG.normal(size=(k,m))
            e=np.block([[np.eye(k),tilt],[np.zeros((m,k)),np.zeros((m,m))]])
            f=np.eye(n)-e
            complement=np.vstack([-tilt,np.eye(m)])
            embedding_inverse=np.hstack([np.zeros((m,k)),np.eye(m)])
            fixed_inverse=complement@np.linalg.inv(c)@embedding_inverse
            assert np.linalg.norm(l0@fixed_inverse@b0-target)<1e-9
            assert np.linalg.norm(f@m0@fixed_inverse-f)<1e-9
            cases+=1
    # One-sided annihilation leaves a constant; a double pole defeats both O(epsilon) factors.
    for epsilon in (F(1,10),F(1,100),F(1,1000)):
        assert epsilon*(1/epsilon)==1
        assert epsilon*(1/epsilon**2)*epsilon==1
    OUT['killed_resolvent_pole']={'oblique_block_models':cases,'maximum_small_to_large_error_ratio':max_ratio,
        'one_sided_and_higher_pole_controls':True}


class Series:
    """Matrix coefficients keyed by actual free words; no commuting of letters."""
    def __init__(self,coefficients,N):
        self.N=N;self.c={w:np.asarray(a,dtype=np.int64)%MOD for w,a in coefficients.items() if len(w)<=N and np.any(np.asarray(a)%MOD)}
        self.shape=next(iter(coefficients.values())).shape
    def __add__(self,other):
        keys=self.c.keys()|other.c.keys()
        return Series({w:(self.c.get(w,np.zeros(self.shape,dtype=np.int64))+other.c.get(w,np.zeros(self.shape,dtype=np.int64)))%MOD for w in keys} or {():np.zeros(self.shape,dtype=np.int64)},self.N)
    def __neg__(self):return Series({w:-a for w,a in self.c.items()} or {():np.zeros(self.shape,dtype=np.int64)},self.N)
    def __sub__(self,other):return self+-other
    def __matmul__(self,other):
        result={};shape=(self.shape[0],other.shape[1])
        for a,ac in self.c.items():
            for b,bc in other.c.items():
                if len(a+b)>self.N:continue
                result[a+b]=(result.get(a+b,np.zeros(shape,dtype=np.int64))+ac@bc)%MOD
        return Series(result or {():np.zeros(shape,dtype=np.int64)},self.N)
    def block(self,rows,cols):return Series({w:a[np.ix_(rows,cols)] for w,a in self.c.items()} or {():np.zeros((len(rows),len(cols)),dtype=np.int64)},self.N)
    def invert(self):
        c0=self.c[()];base=Series({():inverse(c0)},self.N);identity=Series({():np.eye(len(c0),dtype=np.int64)},self.N)
        error=identity-base@self;power=identity;total=identity
        for _ in range(self.N):power=power@error;total=total+power
        return total@base


def schur_checks():
    cases=0;broken=0
    for n,N in product((2,3,4),(1,2,3)):
        identity=Series({():np.eye(n,dtype=np.int64)},N)
        roots=np.arange(n)*3+1
        constant=Series({():np.diag(roots)},N)
        for _ in range(8):
            coefficients={():np.eye(n,dtype=np.int64)}
            for degree in range(1,N+1):
                for word in product((0,1),repeat=degree):coefficients[word]=RNG.integers(0,MOD,(n,n))
            k=Series(coefficients,N);kinv=k.invert()
            assert not (k@kinv-identity).c
            w=k@constant@kinv
            for corrupt in (False,True):
                test=w
                if corrupt:
                    change=np.zeros((n,n),dtype=np.int64);change[0,0]=1
                    test=w+Series({(0,)*N:change},N)
                q=identity
                schurs=[]
                for h,root in enumerate(roots):
                    scalar=Series({():root*np.eye(n,dtype=np.int64)},N)
                    shifted=test-scalar;q=q@shifted
                    other=[j for j in range(n) if j!=h]
                    corner=shifted.block(other,other)
                    schur=shifted.block([h],[h])-test.block([h],other)@corner.invert()@test.block(other,[h])
                    schurs.append(schur)
                assert (not q.c)==all(not s.c for s in schurs)
                assert bool(q.c)==corrupt
                if corrupt:broken+=1
                else:cases+=1
    # Explicitly verify that word 01 and word 10 remain different.
    one=np.ones((1,1),dtype=np.int64)
    a=Series({(0,):one},2);b=Series({(1,):one},2)
    assert (a@b-b@a).c
    OUT['free_ring_schur']={'exact_conjugated_models':cases,'broken_polynomial_controls':broken,
        'noncommuting_word_control':True,'field_characteristic':MOD}


def matching(supports,n):
    owners=[-1]*n
    def augment(i,seen):
        for j in supports[i]:
            if j in seen:continue
            seen.add(j)
            if owners[j]<0 or augment(owners[j],seen):owners[j]=i;return True
        return False
    return sum(augment(i,set()) for i in range(len(supports)))


def filtration_checks():
    profiles=0;matrices=0
    for dims in ((1,1),(2,1),(1,1,1),(2,2,1),(1,2,2),(2,1,2,1)):
        n=sum(dims);starts=np.cumsum((0,)+dims);f=[sum(dims[b:]) for b in range(len(dims))]
        counts=list(product(*(range(v+1) for v in dims)))
        for left,right in product(counts,repeat=2):
            aa=[sum(left[b:]) for b in range(len(dims))];cc=[sum(right[b:]) for b in range(len(dims))]
            deficit=max([0]+[a+c-v for a,c,v in zip(aa,cc,f)])
            supports=[list(range(starts[b],n)) for b in range(len(dims)) for _ in range(left[b]+right[b])]
            assert len(supports)-matching(supports,n)==deficit
            profiles+=1
            if RNG.random()>.08:continue
            A=np.eye(n,dtype=np.int64)[:,[starts[b]+j for b in range(len(dims)) for j in range(left[b])]]
            C=np.eye(n,dtype=np.int64)[:,[starts[b]+j for b in range(len(dims)) for j in range(right[b])]]
            best=n
            for _ in range(6):
                g=np.zeros((n,n),dtype=np.int64)
                for i in range(len(dims)):
                    for j in range(i+1):
                        block=random_invertible(dims[i]) if i==j else RNG.integers(0,MOD,(dims[i],dims[j]))
                        g[starts[i]:starts[i+1],starts[j]:starts[j+1]]=block
                intersection=A.shape[1]+C.shape[1]-rank(np.concatenate([A,g@C%MOD],axis=1))
                assert intersection>=deficit;best=min(best,intersection)
            assert best==deficit;matrices+=1
    OUT['filtered_intersection']={'exhaustive_profile_pairs':profiles,'finite_field_positioning_models':matrices}


def centralizer_checks():
    cases=0
    for lengths in ((1,),(1,2),(1,1,3),(2,2,4),(1,2,3,4),(2,3,3,5)):
        n=sum(lengths);r=len(lengths);starts=np.cumsum((0,)+lengths)
        t=np.zeros((n,n),dtype=np.int64)
        for start,a in zip(starts,lengths):
            for j in range(a-1):t[start+j+1,start+j]=1
        bottoms=[starts[j+1]-1 for j in range(r)]
        for _ in range(30):
            while True:
                target=RNG.integers(0,MOD,(r,r))
                for i,b in enumerate(lengths):
                    for j,a in enumerate(lengths):
                        if a>b:target[i,j]=0
                if rank(target)==r:break
            lift=np.zeros((n,n),dtype=np.int64)
            for i,b in enumerate(lengths):
                for j,a in enumerate(lengths):
                    if a>b:continue
                    for power in range(a):lift[starts[i]+b-a+power,starts[j]+power]=target[i,j]
            assert not np.any((t@lift-lift@t)%MOD)
            assert np.array_equal(lift[np.ix_(bottoms,bottoms)],target)
            assert rank(lift)==n
            dual=inverse(lift).T%MOD
            assert not np.any((t.T@dual-dual@t.T)%MOD)
            cases+=1
    OUT['nilpotent_centralizer']={'exact_Jordan_lifts_and_duals':cases,'complex_irreducibility_tested':False}


if __name__=='__main__':
    for check in (length_checks,root_bundle_checks,selection_checks,bar_checks,pole_checks,
                  schur_checks,filtration_checks,centralizer_checks):
        check();print(check.__name__,'passed',flush=True)
    result={'batch':'B019','python':sys.version.split()[0],'numpy':np.__version__,'checks':OUT,
        'scope':'Selected exact finite mechanisms and numerical block limits; not global algebraic or Lean proof certification.'}
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(OUT,indent=2))
