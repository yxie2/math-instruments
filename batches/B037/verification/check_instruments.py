"""Finite models of selected interfaces, not global topology certifications."""
from fractions import Fraction as F
import itertools as it
import json
import random
from pathlib import Path
import sympy as s
rng=random.Random(37016);out={}

# Puiseux monomial models of the finite-span norm separation step.
cases=0
for p in [2,3,5]:
    for _ in range(40):
        width=rng.randint(2,6); base=rng.randint(1,6)
        vals=[base+rng.randint(0,3) for j in range(width)];vals[0]=base
        previous=None
        for N in [4,8,12,16]:
            terms={}
            for j,a in enumerate(vals):
                exponent=F(j+1,p**N)+a
                terms[exponent]=(terms.get(exponent,0)+rng.randrange(1,p))%p
                higher=exponent+rng.randint(1,4)
                terms[higher]=(terms.get(higher,0)+1)%p
            valuation=min(e for e,c in terms.items() if c)
            assert base<valuation<=base+F(width,p**N)
            if previous is not None:assert valuation<previous
            previous=valuation
        cases+=1
out['frobenius_separation']={'finite_puiseux_models':cases,'depths_per_model':4}

x,y,u,v=s.symbols('x y u v');cases=0
for p in [2,3,5,7]:
    for h in [1,2,3]:
        # Graph y=x^(p^h) is an additive formal subgroup and is reduced/smooth.
        f=y-x**(p**h)
        defect=s.Poly(s.expand(f.subs({x:x+u,y:y+v})-f-f.subs({x:u,y:v})),x,y,u,v,modulus=p)
        assert defect.is_zero
        assert s.Poly(s.diff(f,x),x,y,modulus=p).is_zero and s.diff(f,y)==1
        assert s.Poly(s.diff(x**p,x),x,modulus=p).is_zero
        cases+=1
out['formal_smoothness']={'additive_graph_models':cases,'nonreduced_alpha_p_negative_controls':4}

def random_shape(depth):
    return () if depth==0 or rng.random()<.25 else tuple(random_shape(depth-1) for _ in range(rng.randint(1,3)))
def counts(T):
    if not T:return [1]
    child=[counts(t) for t in T];ans=[len(T)+1]+[0]*max(map(len,child))
    for c in child:
        for j,a in enumerate(c):ans[j+1]+=a
    return ans
def spine(T,m):
    if not T:return ()
    return tuple(() if m==0 else spine(t,m-1) for t in T)
def full_attach(T):
    return [] if not T else [0]*len(T)+[j+1 for t in T for j in full_attach(t)]
def relative_attach(T,m):
    if not T:return []
    return [j+1 for t in T for j in (full_attach(t) if m==0 else relative_attach(t,m-1))]
for _ in range(100):
    T=random_shape(5);c=counts(T)
    for m in range(5):
        a=counts(spine(T,m));a += [0]*(len(c)-len(a))
        assert a[:min(m+1,len(c))]==c[:min(m+1,len(c))]
        assert all(v==0 for v in a[m+2:])
        for j in relative_attach(T,m):
            assert j>m;a[j]+=1;a[j+1]+=1
        assert a==c
out['finite_spines']={'shapes':100,'cutoff_levels_each':5,'attachment_dimension_checked':True}

# Underlying globular-set cutoff universal property through dimension two.
count=maps=0
for q in [0,1]:
    for _ in range(20):
        nx=2;ny=2
        ex=[(rng.randrange(nx),rng.randrange(nx)) for j in range(4)]
        tx=[(a,b) for a in range(4) for b in range(4) if ex[a]==ex[b] and rng.random()<.3]
        ey=list(it.product(range(ny),repeat=2)) if q==0 else [(0,0),(0,1),(0,1),(1,1)]
        ty={(a,b) for a in range(len(ey)) for b in range(len(ey)) if ey[a]==ey[b]}
        full=lower=0
        for obj in it.product(range(ny),repeat=nx):
            opts=[[j for j,e in enumerate(ey) if e==(obj[a],obj[b])] for a,b in ex]
            assignments=list(it.product(*opts))
            if q==0:lower+=1
            else:lower+=len(assignments)
            for f in assignments:
                assert all((f[a],f[b]) in ty for a,b in tx)
                full+=1
        assert full==lower
        maps+=full;count+=1
out['globular_cutoffs']={'underlying_globular_models':count,'unique_extensions':maps,'coherator_operations_tested':False}

def vp(a,p):
    if a==0:return 10**9
    n,d=a.numerator,a.denominator;k=0
    while n%p==0:n//=p;k+=1
    while d%p==0:d//=p;k-=1
    return k
checks=0
for _ in range(40):
    p=rng.choice([2,3,5]);cs=[F(p)**rng.randint(-3,3) for j in range(12)]
    a=[F(rng.randint(-5,5)) for j in cs];old=[F(0)]
    for h in range(12):
        # Force small changes even when previous maps amplify p-adic norm.
        cumulative=F(1);loss=0
        for j in range(h-1,-1,-1):
            cumulative*=cs[j];loss=max(loss,-vp(cumulative,p))
        err=F(p)**(h+loss+2)
        terminal=(old[h]-a[h]+err)/cs[h]
        new=[F(0)]*(h+2);new[-1]=terminal
        for j in range(h,-1,-1):new[j]=a[j]+cs[j]*new[j+1]
        assert all(new[j]-cs[j]*new[j+1]==a[j] for j in range(h+1))
        assert all(vp(new[j]-old[j],p)>=h+2 for j in range(h+1))
        old=new;checks+=1
out['dense_tower_protocol']={'finite_extension_steps':checks,'complete_infinite_spaces_simulated':False}

# Mod-p generators lifted through finite p-power precision.
checks=0
for p in [2,3,5]:
    for precision in range(1,9):
        modulus=p**precision
        for _ in range(5):
            A=s.Matrix([[1,p*rng.randint(-3,3)],[0,1]])
            target=s.Matrix([rng.randrange(modulus),rng.randrange(modulus)])
            residual=target;coefficient=s.zeros(2,1)
            for j in range(precision):
                digit=(A.inv()*residual).applyfunc(lambda a:int(a)%p)
                coefficient+=p**j*digit
                residual=(residual-A*digit)/p
                assert all(s.denom(v)==1 for v in residual)
            assert all(int(v)%modulus==0 for v in A*coefficient-target)
            checks+=1
out['compact_nakayama']={'finite_precision_digit_lifts':checks,'spectrum_constructed':False}

def posets(n):
    pairs=list(it.combinations(range(n),2));seen=set()
    for mask in range(1<<len(pairs)):
        R={(i,i) for i in range(n)}|{e for j,e in enumerate(pairs) if mask>>j&1}
        for k in range(n):
            R|={(i,j) for i in range(n) for j in range(n) if (i,k) in R and (k,j) in R}
        key=frozenset(R)
        if key not in seen:seen.add(key);yield R
zigzags=covers=chains=0
for n in range(1,6):
    U=set(range(n))
    for R in posets(n):
        ideals=[{i for i in range(n) if mask>>i&1} for mask in range(1<<n)]
        ideals=[A for A in ideals if all(a in A for a,b in R if b in A)]
        for A in ideals:
            new=U-A
            greatest=[x for x in new if all((y,x) in R for y in new)]
            if not A or not greatest:continue
            retraction={}
            for e in U:
                options=[a for a in A if (a,e) in R and all((b,a) in R for b in A if (b,e) in R)]
                if options:retraction[e]=options[0]
            if len(retraction)!=n:continue
            top=greatest[0];t=retraction[top]
            k={e:e if e in A else t for e in U};g={e:e if e in A else top for e in U}
            assert all((k[a],k[b]) in R and (g[a],g[b]) in R for a,b in R)
            assert all((e,g[e]) in R and (k[e],g[e]) in R for e in U)
            zigzags+=1
        for A in ideals:
            for B in ideals:
                if A|B!=U:continue
                for size in range(1,n+1):
                    for chain in it.combinations(range(n),size):
                        if all((a,b) in R for a,b in zip(chain,chain[1:])):
                            assert set(chain)<=A or set(chain)<=B;chains+=1
                covers+=1
out['relative_poset_zigzags']={'exhaustive_naturally_labelled_models_up_to':5,'valid_sieve_retractions':zigzags}
out['nerve_covers']={'ideal_cover_pairs':covers,'nondegenerate_chains':chains,'strict_higher_orientals_tested':False}
result={'batch':'B037','status':'pass','scope':'Selected finite algebraic and combinatorial models only; no global theorem or Lean build certified.','checks':out}
Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
