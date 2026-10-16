"""Exact finite checks of selected algebraic devices; no global topology certification."""
from collections import defaultdict
from fractions import Fraction
from itertools import product, combinations
from math import comb, prod
from pathlib import Path
import json
import random

rng=random.Random(25016)

def rank(a, p=None):
    if not a: return 0
    a=[[int(x)%p if p else Fraction(x) for x in row] for row in a]
    r=0
    for j in range(len(a[0])):
        i=next((i for i in range(r,len(a)) if a[i][j]),None)
        if i is None: continue
        a[r],a[i]=a[i],a[r]
        inv=pow(a[r][j],-1,p) if p else 1/a[r][j]
        a[r]=[(x*inv)%p if p else x*inv for x in a[r]]
        for i in range(len(a)):
            if i!=r and a[i][j]:
                c=a[i][j];a[i]=[(x-c*y)%p if p else x-c*y for x,y in zip(a[i],a[r])]
        r+=1
        if r==len(a): break
    return r

def ident(n): return [[int(i==j) for j in range(n)] for i in range(n)]
def mul(a,b,mod=None):
    out=[[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
    return [[x%mod for x in row] for row in out] if mod else out
def power(a,n,mod=None):
    out=ident(len(a))
    while n:
        if n&1: out=mul(out,a,mod)
        a=mul(a,a,mod);n//=2
    return out

def nilpotent_lift():
    models=0
    for labels in range(1,4):
        # C1 --t1--> C0 over Q[t_i]/t_i^2. H0 and H1 are not free over this ring.
        size=1<<labels
        for n in range(1,5):
            a=ident(n)
            for _ in range(8):
                i,j=rng.randrange(n),rng.randrange(n)
                if i!=j:
                    c=rng.randint(-2,2);a[i]=[x+c*y for x,y in zip(a[i],a[j])]
            if rank(a)!=n: a=ident(n)
            f=[[0]*(n*size) for _ in range(n*size)]
            d=[[0]*(n*size) for _ in range(n*size)]
            for i,j in product(range(n),repeat=2):
                for mask in range(size): f[i*size+mask][j*size+mask]=a[i][j]
                for bit in range(labels):
                    c=rng.randint(-2,2)
                    for mask in range(size):
                        if not mask&(1<<bit): f[i*size+mask+(1<<bit)][j*size+mask]+=c
            for i in range(n):
                for mask in range(size):
                    if not mask&1: d[i*size+mask+1][i*size+mask]=1
            assert mul(f,d)==mul(d,f)
            assert rank(d)==n*size//2 and rank(f)==n*size
            inds=[i*size+mask for i in range(n) for mask in range(size) if not mask&1]
            h0=[[f[i][j] for j in inds] for i in inds]
            assert rank(h0)==len(inds)
            inds=[i*size+mask for i in range(n) for mask in range(size) if mask&1]
            assert rank([[f[i][j] for j in inds] for i in inds])==len(inds)
            models+=1
    # A pairing nonzero at time zero can first recur at the full dimension.
    recurrences=0
    for n in range(1,13):
        f=[[int(i==(j+1)%n) for j in range(n)] for i in range(n)]
        first=next(k for k in range(1,n+1) if power(f,k)[0][0])
        assert first==n;recurrences+=1
    assert power([[0]],1)[0][0]==0  # invertibility is essential
    return dict(nonfree_homology_models=models,sharp_positive_recurrences=recurrences,
                scope='Finite nilpotent ring complexes and recurrence; no labelled Floer construction.')

def lattice_units():
    matrices=0
    for n in range(1,4):
        q=2**n;order=6*2**(4*(n-1))
        for a,b,c,d in product(range(q),repeat=4):
            if (a*d-b*c)%2:
                f=[[a,b],[c,d]]
                assert power(f,order,q)==ident(2)
                # Any pairing with q0=1 survives each multiple of the group order.
                assert power(f,2*order,q)[0][0]==1
                matrices+=1
    # The two-term complex diag(2,3,0) has even torsion, odd torsion and free homology.
    d=[[2,0,0],[0,3,0],[0,0,0]];f=[[3,0,0],[0,2,0],[0,0,3]]
    cone2=[[f[i][j] for j in range(3)]+[d[i][j] for j in range(3)] for i in range(3)]
    cone1=[[-d[i][j] for j in range(3)] for i in range(3)]+[[f[i][j] for j in range(3)] for i in range(3)]
    assert rank(cone2,2)==3 and rank(cone1,2)==3 and rank(d,2)==1
    for n in range(1,10): assert (3*pow(3,-1,2**n))%(2**n)==1
    assert 3 not in (-1,1)  # localization does not give an integral unit
    return dict(all_GL2_matrices=matrices,torsion_complexes=1,
                scope='Finite congruence recurrence and a torsion-containing chain example; no instanton maps.')

def clean(c): return {k:v for k,v in c.items() if v}
def boundary(c):
    out=defaultdict(int)
    for chain,v in c.items():
        for i in range(len(chain)): out[chain[:i]+chain[i+1:]]+=(-1)**i*v
    return clean(out)
def plus(a,b,sign=1):
    out=defaultdict(int,a)
    for k,v in b.items(): out[k]+=sign*v
    return clean(out)
def residue(c,flag):
    out=defaultdict(int)
    for chain,v in c.items():
        if all(x in chain for x in flag): out[chain[chain.index(flag[-1])+1:]]+=v
    return clean(out)
def subspaces(k):
    seen={frozenset({0})};todo=list(seen)
    while todo:
        a=todo.pop()
        for x in range(1<<k):
            b=a|frozenset(y^x for y in a)
            if b not in seen: seen.add(b);todo.append(b)
    return sorted((s for s in seen if len(s)>1),key=lambda s:(len(s),tuple(sorted(s))))
def chains(poset):
    out=[()]
    def extend(c):
        for x in poset:
            if not c or c[-1]<x:
                out.append(c+(x,));extend(c+(x,))
    extend(())
    return out

def saturated_residue():
    poset=subspaces(3);allchains=chains(poset);checks=0
    flags=[c for c in allchains if c and all(len(s)==2**(i+1) for i,s in enumerate(c))]
    for flag in flags:
        for c in allchains:
            lhs=residue(boundary({c:1}),flag)
            rhs={q:(-1)**len(flag)*v for q,v in boundary(residue({c:1},flag)).items()}
            assert lhs==rhs;checks+=1
    line=frozenset({0,1});plane=frozenset({0,1,2,3});whole=frozenset(range(8))
    c={(line,plane,whole):1};flag=(plane,)
    assert residue(boundary(c),flag)!= {q:-v for q,v in boundary(residue(c,flag)).items()}
    return dict(subspaces=len(poset),flags=len(flags),chain_identities=checks,
                scope='Augmented finite subspace-poset identities, with an unsaturated failure control.')

def shuffle_one(u,v):
    r,t=len(u),len(v);out=defaultdict(int)
    for hp in combinations(range(r+t),r):
        hp=set(hp);i=j=inv=0;chain=[]
        for k in range(r+t):
            if k in hp: i+=1;inv+=j
            else: j+=1
            chain.append((u[i-1] if i else 0,v[j-1] if j else 0))
        out[tuple(chain)]+=(-1)**inv
    return clean(out)
def shuffle(a,b):
    out=defaultdict(int)
    for u,x in a.items():
        for v,y in b.items():
            for c,s in shuffle_one(u,v).items(): out[c]+=x*y*s
    return clean(out)
def shuffle_checks():
    flags=[c for r in range(5) for c in combinations(range(1,5),r)];count=0
    for u,v in product(flags,repeat=2):
        lhs=boundary(shuffle({u:1},{v:1}))
        rhs=plus(shuffle(boundary({u:1}),{v:1}),shuffle({u:1},boundary({v:1})),(-1)**len(u))
        assert lhs==rhs;count+=1
    return dict(flag_pairs=count,scope='Exact signed staircase shuffles, including empty flags and augmented boundaries.')

def groupoid_weights():
    models=nonfaithful=0
    for m,n in product(range(1,13),repeat=2):
        for a in range(n):
            if m*a%n: continue
            image={a*x%n for x in range(m)}
            unseen=set(range(n));mass=Fraction(0)
            while unseen:
                x=min(unseen);orbit={(x+y)%n for y in image};unseen-=orbit
                stabilizer=sum(a*h%n==0 for h in range(m));mass+=Fraction(1,stabilizer)
            assert mass==Fraction(n,m)
            models+=1;nonfaithful+=stabilizer>1
    compositions=0
    for _ in range(100):
        aa=[rng.randrange(1,10) for _ in range(5)];bb=[rng.randrange(1,10) for _ in range(3)];cc=[2,7]
        f=[rng.randrange(3) for _ in aa];g=[rng.randrange(2) for _ in bb];x=[rng.randrange(-5,6) for _ in aa]
        fx=[sum(Fraction(bb[j],aa[i])*x[i] for i in range(5) if f[i]==j) for j in range(3)]
        gfx=[sum(Fraction(cc[k],bb[j])*fx[j] for j in range(3) if g[j]==k) for k in range(2)]
        direct=[sum(Fraction(cc[k],aa[i])*x[i] for i in range(5) if g[f[i]]==k) for k in range(2)]
        assert gfx==direct
        assert sum(Fraction(fx[j],bb[j]) for j in range(3))==sum(Fraction(x[i],aa[i]) for i in range(5))
        compositions+=1
    return dict(cyclic_functors=models,nonfaithful_functors=nonfaithful,composition_checks=compositions,
                scope='Finite groupoid homotopy masses and pushforward composition; no spectral character splitting.')

def compositions(n,d):
    if d==1: yield (n,);return
    for a in range(n+1):
        for tail in compositions(n-a,d-1): yield (a,)+tail
def lattice_counts():
    comparisons=limits=explicit=0
    for p in (2,3,5):
        prev=[1]*15
        for d in range(1,6):
            vals=[1]*15 if d==1 else [sum(p**b*prev[b] for b in range(j+1)) for j in range(15)]
            for j in range(10):
                direct=sum(p**sum(i*e for i,e in enumerate(es)) for es in compositions(j,d))
                assert vals[j]==direct;comparisons+=1
            den=prod(1-p**u for u in range(1,d))
            for j in range(14):
                mod=p**(j+1)
                assert (vals[j]-pow(den,-1,mod))%mod==0;limits+=1
            prev=vals
    # Enumerate the free entries of triangular subgroup bases, not only their counts.
    for d in (2,3):
        for j in range(4):
            bases=set()
            for es in compositions(j,d):
                positions=[(i,k) for i in range(d) for k in range(i+1,d)]
                for off in product(*(range(2**es[k]) for i,k in positions)):
                    mat=[[0]*d for _ in range(d)]
                    for i in range(d): mat[i][i]=2**es[i]
                    for (i,k),v in zip(positions,off): mat[i][k]=v
                    bases.add(tuple(map(tuple,mat)))
            assert len(bases)==sum(2**sum(i*e for i,e in enumerate(es)) for es in compositions(j,d))
            explicit+=len(bases)
    return dict(coefficient_comparisons=comparisons,p_adic_congruences=limits,triangular_bases=explicit,
                scope='Finite subgroup-basis enumeration and exact p-adic precision checks; no profinite kernel theorem.')

# Sparse polynomials over F_2 are sets of exponent tuples.
def padd(*polys):
    out=set()
    for p in polys: out.symmetric_difference_update(p)
    return out
def pmul(a,b):
    out=set()
    for x in a:
        for y in b:
            z=tuple(i+j for i,j in zip(x,y))
            if z in out: out.remove(z)
            else: out.add(z)
    return out
def ppow(a,n,k):
    out={(0,)*k}
    while n:
        if n&1: out=pmul(out,a)
        a={tuple(2*x for x in e) for e in a};n//=2
    return out
def substitute(f,ys,k):
    out=set()
    for e in f:
        term={(0,)*k}
        for y,n in zip(ys,e): term=pmul(term,ppow(y,n,k))
        out.symmetric_difference_update(term)
    return out
def cartier(f): return {tuple((x-1)//2 for x in e) for e in f if all(x%2 for x in e)}
def sq(f,n):
    out=set()
    for e in f:
        for es in compositions(n,len(e)):
            if all((i&~a)==0 for a,i in zip(e,es)):
                z=tuple(a+i for a,i in zip(e,es))
                if z in out: out.remove(z)
                else: out.add(z)
    return out
def dickson(k):
    out={(0,)*k+(1,)}
    for bits in product((0,1),repeat=k):
        if not any(bits): continue
        terms={(0,)*k+(1,)}
        for i,b in enumerate(bits):
            if b: terms.add(tuple(int(j==i) for j in range(k))+(0,))
        out=pmul(out,terms)
    return [{e[:-1] for e in out if e[-1]==2**j} for j in range(k)]

def cartier_checks():
    identities=naturality=dickson_models=floors=0
    for k in range(1,4):
        for _ in range(25):
            f={tuple(rng.randrange(6) for _ in range(k)) for _ in range(10)}
            for i in range(4):
                assert cartier(sq(f,2*i))==sq(cartier(f),i)
                assert not cartier(sq(f,2*i+1));identities+=2
            while True:
                a=[[rng.randrange(2) for _ in range(k)] for _ in range(k)]
                if rank(a,2)==k: break
            ys=[{tuple(int(j==i) for j in range(k)) for i in range(k) if row[i]} for row in a]
            assert cartier(substitute(f,ys,k))==substitute(cartier(f),ys,k);naturality+=1
        ds=dickson(k)
        for c in range(5):
            for bs in product(range(3),repeat=k-1):
                f=substitute({(c,)+bs},ds,k)
                expected=set()
                if c%2==k%2 and all(b%2 for b in bs):
                    expected=substitute({((c+k-2)//2,)+tuple((b-1)//2 for b in bs)},ds,k)
                assert cartier(f)==expected;dickson_models+=1
        for floor in range(6):
            c0=next(c for c in range(floor+1,floor+3) if c%2==k%2)
            target=(c0+k-2)//2
            for e in range(target,target+5):
                c=2*e-k+2
                assert c>floor and c%2==k%2
                assert (c+k-2)//2==e;floors+=1
    return dict(Steenrod_identities=identities,GL_naturality=naturality,
                Dickson_monomials=dickson_models,exponent_floor_checks=floors,
                scope='Exact polynomial Cartier identities and threshold arithmetic; no full Steenrod tensor obstruction.')

def primitive_roots():
    # Non-primitively generated, connected polynomial Hopf algebra:
    # Delta(x)=xL+xR; Delta(y)=yL+yR+xL*xR, deg(x)=1, deg(y)=2.
    dx={(1,0,0,0),(0,0,1,0)}
    dy={(0,1,0,0),(0,0,0,1),(1,0,1,0)}
    def delta(f): return substitute(f,[dx,dy],4)
    def reduced(f): return padd(delta(f),{e+(0,0) for e in f},{(0,0)+e for e in f})
    checked=roots=0
    for degree in range(2,25):
        monoms=[(a,b) for b in range(degree//2+1) for a in [degree-2*b] if a+b>=2]
        vectors={};relations=[]
        for i,e in enumerate(monoms):
            v=reduced({e});mask=1<<i
            while v:
                pivot=max(v)
                if pivot not in vectors: vectors[pivot]=(set(v),mask);break
                w,m=vectors[pivot];v.symmetric_difference_update(w);mask^=m
            if not v: relations.append(mask)
        for mask in relations:
            f={e for i,e in enumerate(monoms) if mask>>i&1}
            assert not reduced(f)
            assert all(all(x%2==0 for x in e) for e in f)
            root={tuple(x//2 for x in e) for e in f}
            assert not reduced(root) and pmul(root,root)==f
            roots+=1
        checked+=len(monoms)
    # Reducedness is essential for the root step: truncate x^2=y^2=0.
    assert reduced({(0,1)})=={(1,0,1,0)}
    # y is then a nonprimitive square root of the zero primitive.
    assert all(any(x>=2 for x in e[:2]) or any(x>=2 for x in e[2:])
               for e in pmul(reduced({(0,1)}),reduced({(0,1)})))
    return dict(decomposable_monomials=checked,primitive_kernel_basis_vectors=roots,
                scope='Exact coproduct kernels in a non-primitively generated polynomial Hopf algebra; no spherical-class classification.')

if __name__=='__main__':
    groups={name:fn() for name,fn in [
        ('nilpotent_lift',nilpotent_lift),('lattice_units',lattice_units),
        ('saturated_residue',saturated_residue),('product_shuffle',shuffle_checks),
        ('groupoid_weights',groupoid_weights),('lattice_counts',lattice_counts),
        ('Cartier_halving',cartier_checks),('primitive_roots',primitive_roots)]}
    result=dict(batch='B025',status='passed',check_groups=groups,
                limitations='Finite algebra does not certify cosmetic surgery, Quillen rational homology, chromatic fixed-point loss or Curtis claims.')
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
