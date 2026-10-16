"""Finite checks of eight extracted mechanisms, not the source headline theorems."""
from collections import defaultdict, deque
from fractions import Fraction as F
from itertools import combinations, permutations, product
from math import exp, log, prod
from pathlib import Path
import json
import numpy as np
from scipy.integrate import quad

RNG=np.random.default_rng(22026)
OUT={}

def density():
    positive=0
    for _ in range(500):
        w=RNG.lognormal(0,1,80); w/=w.mean()
        x=RNG.integers(0,5,80).astype(float)
        y=RNG.choice([0.,1.,2.],80,p=[.94,.04,.02])
        a=np.mean(w*x); b=np.mean(w*x*x); e=np.mean(w*y)
        delta=a*a/b-e
        if delta>0:
            positive+=1
            good=(x>0)&(y==0)
            assert np.mean(w*good)+1e-12>=delta
            assert good.mean()+1e-12>=delta**2/np.mean(w*w)
    instances=0; starts=0
    for mask in range(1<<10):
        points=[i+1 for i in range(10) if mask>>i&1]+[20]
        for h in [1,2,3]:
            chosen=[]
            for m in range(0,11):
                left=[p for p in points if m<p<=m+h]
                right=[p for p in points if m+h<p<=m+2*h]
                if left and not right:
                    p=max(left); nxt=min(q for q in points if q>p)
                    assert nxt-p>h
                    chosen.append(p)
            assert len(chosen)<=h*len(set(chosen))
            starts+=len(chosen); instances+=1
    # Without a second weight moment, weighted mass need not imply fixed ordinary density.
    for n in [10,100,1000]:
        w=np.zeros(n); w[0]=n
        assert np.mean(w)==1 and np.mean(w*w)==n
    OUT['weighted_density']={'weighted_models':500,'positive_bounds':positive,'point_set_block_models':instances,'good_starts':starts,'scope':'Moment inequalities and finite charging, not prime-weight construction or asymptotics.'}

def profiles():
    def step(t):
        if t<=0:return 0.
        if t>=1:return 1.
        a=exp(-1/t); b=exp(-1/(1-t))
        return a/(a+b)
    rows=[]; edge=log(2)
    for length in [4.,10.,30.,100.]:
        def chi(z):return step((z+edge)/edge)*step((length+edge-z)/edge)
        cuts=[-edge,0.,length,length+edge]
        def integ(f):return sum(quad(f,a,b,epsabs=1e-11,epsrel=1e-11)[0] for a,b in zip(cuts,cuts[1:]))
        A=integ(chi); B=integ(lambda z:chi(z)**2); N2=integ(lambda z:chi(z)**2*exp(-z))
        assert A>=length-1e-10 and B<=length+log(4)+1e-10 and .5<N2<2
        for lam in [.1,1.,3.]:
            c=lam*N2/A**2
            mass=integ(lambda z:(chi(z)*exp(-z)/(N2*c)**.5)**2*c*exp(z))
            l1=integ(lambda z:chi(z)*exp(-z)/(N2*c)**.5*c*exp(z))
            mu=integ(lambda z:c*exp(z)*(chi(z)*exp(-z)/(N2*c)**.5)**2*c*exp(z))
            assert abs(mass-1)<1e-10 and abs(l1-lam**.5)<1e-10
            assert abs(mu-lam*B/A**2)<1e-10
            assert mu<=lam*(length+log(4))/length**2+1e-10
            rows.append({'log_R':length,'lambda':lam,'first_moment':mu})
    OUT['smooth_profiles']={'models':rows,'scope':'Numerical quadrature of explicit smooth compact profiles; no sieve estimates.'}

def trim(a):
    a=list(map(F,a))
    while len(a)>1 and a[-1]==0:a.pop()
    return a
def add(a,b):return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def scale(a,c):return trim([x*c for x in a])
def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return trim(c)
def div(a,b):
    a=trim(a); b=trim(b); q=[F(0)]*max(1,len(a)-len(b)+1)
    while a!=[0] and len(a)>=len(b):
        d=len(a)-len(b); t=a[-1]/b[-1]; q[d]+=t
        a=add(a,[F(0)]*d+scale(b,-t))
    return trim(q),a
def xp(n):return [-1]+[0]*(n-1)+[1]
def inverse_mod(a,m):
    r0,r1=m,a; s0,s1=[F(0)],[F(1)]
    while r1!=[0]:
        q,r=div(r0,r1); r0,r1=r1,r; s0,s1=s1,add(s0,scale(mul(q,s1),-1))
    assert len(r0)==1
    return div(scale(s0,1/r0[0]),m)[1]
def units():
    checks=0
    for p,q in [(3,5),(5,7),(5,11)]:
        poly,rem=div(mul(xp(p*q),xp(1)),mul(xp(p),xp(q)))
        assert rem==[0] and sum(poly)==1 and all(x.denominator==1 for x in poly)
        for k in range(1,p):
            inv=inverse_mod(xp(k),poly)
            assert all(x.denominator==1 for x in inv)
            assert div(mul(inv,xp(k)),poly)[1]==[1]
            checks+=1
    OUT['cyclotomic_units']={'exact_integral_inverse_checks':checks,'scope':'Unit differences in three cyclotomic rings. Finite generation of all number-field units and the uniform root field are proved symbolically, not computed here.'}

def flags():
    labels=list(product(range(2),range(3))); n=len(labels)
    orders=[o for o in permutations(range(n)) if all(o.index(i)<o.index(j) for i in range(n) for j in range(n) if i!=j and all(a<=b for a,b in zip(labels[i],labels[j])))]
    checks=0
    for _ in range(100):
        M=np.eye(n,dtype=np.int64)
        for a,(i,j) in enumerate(labels):
            for b,(k,l) in enumerate(labels):
                if a!=b and i<=k and j<=l:M[a,b]=RNG.integers(-4,5)
        N=M-np.eye(n,dtype=np.int64); inv=np.eye(n,dtype=np.int64); power=inv.copy()
        for k in range(1,n):power=power@(-N); inv+=power
        assert np.array_equal(M@inv,np.eye(n,dtype=np.int64))
        for o in orders:
            B=M[np.ix_(o,o)]
            assert np.all(np.tril(B,-1)==0)
            for k in range(1,n):assert np.all(B[k:,:k]==0)
            checks+=1
        # Altering strictly lower-both blocks leaves row and column graded maps unchanged.
        M2=M.copy()
        for a,(i,j) in enumerate(labels):
            for b,(k,l) in enumerate(labels):
                if i<k and j<l:M2[a,b]+=7
        for coord in [0,1]:
            for value in set(x[coord] for x in labels):
                ix=[i for i,x in enumerate(labels) if x[coord]==value]
                assert np.array_equal(M[np.ix_(ix,ix)],M2[np.ix_(ix,ix)])
    OUT['two_flags']={'integer_matrix_models':100,'coordinate_order_extensions':len(orders),'gallery_order_checks':checks,'scope':'Split rank-one blocks with compatible graded maps; not reconstruction of arbitrary flag families or seam equations.'}

def entropy(vals,weights):
    d=defaultdict(float)
    for v,w in zip(vals,weights):d[v]+=float(w)
    return -sum(p*log(p) for p in d.values() if p>0)
def shared_entropy():
    k=3; p=3; states=list(product(range(p),repeat=2*k)); labels=list(product(range(3),repeat=1))
    cases=0; maxgain=0.
    for _ in range(30):
        weights=RNG.random((len(states),3)); weights/=weights.sum()
        flat=weights.ravel(); Y=[y for y in states for h in range(3)]; H=[h for y in states for h in range(3)]
        hh=entropy(H,flat)
        cond=[entropy([(y[c],h) for y,h in zip(Y,H)],flat)-hh for c in range(2*k)]
        deficit=log(p)-sum(cond)/(2*k)
        for s in [1,2,3]:
            sample=[tuple(2*j+sign for j,sign in zip(js,signs)) for js in combinations(range(k),s) for signs in product(range(2),repeat=s)]
            hj=sum(entropy([tuple(y[c] for c in ix) for y in Y],flat) for ix in sample)/len(sample)
            bound=log(p)-hj/s+hh/s
            assert deficit<=bound+1e-11
            maxgain=max(maxgain,hh-hh/s); cases+=1
    OUT['shared_conditioning']={'joint_distributions':30,'subset_size_models':cases,'maximum_saved_nats_vs_repeating_conditioning':maxgain,'scope':'Independent uniformly sampled coordinate sets; finite entropies do not verify the source coverage schedule.'}

STEPS=[(1,0),(-1,0),(0,1),(0,-1)]
def periodic():
    finite=0; exceptional=0; maxcomponent=0
    for Q in [2,3]:
        residues=list(product(range(Q),repeat=2))
        for mask in range(1<<len(residues)):
            A={r for i,r in enumerate(residues) if mask>>i&1}
            seen=set(); sizes=[]; infinite=False
            for root in A:
                if root in seen:continue
                lifts={root:root}; queue=deque([root])
                while queue:
                    r=queue.popleft(); v=lifts[r]
                    for dx,dy in STEPS:
                        w=(v[0]+dx,v[1]+dy); z=(w[0]%Q,w[1]%Q)
                        if z not in A:continue
                        if z in lifts:
                            if lifts[z]!=w:infinite=True
                        else:lifts[z]=w;queue.append(z)
                seen.update(lifts); sizes.append(len(lifts))
            if infinite:continue
            finite+=1; maxcomponent=max(maxcomponent,max(sizes,default=0))
            assert max(sizes,default=0)<=Q*Q
            outside=[r for r in residues if r not in A]
            E=set(outside[:min(2,len(outside))]); bound=len(E)+4*len(E)*Q*Q
            reached=set()
            for root in E:
                if root in reached:continue
                comp={root}; queue=deque([root])
                while queue:
                    v=queue.popleft()
                    for dx,dy in STEPS:
                        w=(v[0]+dx,v[1]+dy)
                        if w in comp or (w not in E and (w[0]%Q,w[1]%Q) not in A):continue
                        comp.add(w);queue.append(w)
                        assert len(comp)<=bound
                reached.update(comp); exceptional+=1
    OUT['periodic_components']={'finite_periodic_patterns':finite,'exceptional_components':exceptional,'largest_component_before_exceptions':maxcomponent,'scope':'All period-2 and period-3 nearest-neighbor patterns, with exact lift-cycle detection. Does not construct Gaussian-prime obstructions.'}

def normalizers():
    S=list(permutations(range(3))); identity=(0,1,2)
    def smul(a,b):return tuple(a[b[i]] for i in range(3))
    def sinv(a):return tuple(a.index(i) for i in range(3))
    G=list(product(S,S,[0,1])); U=[g for g in G if g[2]==0]
    def gm(a,b):
        x,y,e=a; z,w,f=b
        if e:z,w=w,z
        return smul(x,z),smul(y,w),e^f
    def gi(a):
        x,y,e=a; x,y=sinv(x),sinv(y)
        return (y,x,e) if e else (x,y,e)
    N={(identity,s,0) for s in S}
    conjugates={frozenset(gm(gm(g,n),gi(g)) for n in N) for g in G}
    T=[g for g in G if {gm(gm(g,n),gi(g)) for n in N}==N]
    assert set(T)==set(U) and len(conjugates)==2
    checks=0
    for t in T:
        possible=[b for b in S if all(smul(smul(b,u[0]),sinv(b))==gm(gm(t,u),gi(t))[0] for u in U)]
        assert possible==[t[0]]
        for v in T:assert gm(t,v)[0]==smul(t[0],v[0]);checks+=1
    other=next(c for c in conjugates if c!=frozenset(N))
    assert {g[0] for g in other}==set(S)
    # Nontrivial centralizer destroys uniqueness of extension in an abelian model.
    assert all(a==(a^b) for a,b in product(range(2),[0]))
    assert any(a!=(a^b) for a,b in product(range(2),[1]))
    OUT['normalizer_extension']={'ambient_group_order':len(G),'normalizer_order':len(T),'homomorphism_pairs':checks,'kernel_conjugates':len(conjugates),'scope':'Finite wreath-product model verifies unique implementation and nontrivial other-kernel image; no profinite reconstruction theorem checked.'}

def power_separation():
    limit=2_000_000; sieve=np.ones(limit+1,dtype=bool);sieve[:2]=False
    for p in range(2,int(limit**.5)+1):
        if sieve[p]:sieve[p*p::p]=False
    records=[]
    q=[2,3]; ps=[[3,5],[2,5]]; aux=[7,11]; d=2; m=2; modulus=m*prod(aux)
    for ell in range(1+modulus,limit,modulus):
        if not sieve[ell]:continue
        if not all(pow(qj,(ell-1)//s,ell)==1 and all(pow(p,(ell-1)//s,ell)!=1 for p in P) for qj,P,s in zip(q,ps,aux)):continue
        for qj,P,s in zip(q,ps,aux):
            subgroup=set(); x=1
            while x not in subgroup:subgroup.add(x);x=x*qj%ell
            for p in P:
                for f in range(1,d+1):assert pow(p,f,ell) not in subgroup
        records.append(ell)
        if len(records)==5:break
    assert len(records)==5
    OUT['simultaneous_power_separation']={'m':m,'d':d,'q':q,'P':ps,'auxiliary_primes':aux,'witness_primes':records,'scope':'Five exact residue-field examples with overlapping prime sets; not infinitude, Kummer independence or Chebotarev.'}

if __name__=='__main__':
    for f in [density,profiles,units,flags,shared_entropy,periodic,normalizers,power_separation]:
        f(); print('PASS',f.__name__,flush=True)
    result={'batch':'B022','status':'passed','check_groups':OUT,'limitations':'Finite identities and models support selected mechanisms only. No full headline theorem or Lean proof build is certified.'}
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
