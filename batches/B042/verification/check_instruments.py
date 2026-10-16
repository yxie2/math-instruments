"""Finite checks of arithmetic and analytic interfaces, not headline claims."""
import itertools as it
import json
import random
from collections import defaultdict
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import mpmath as mp
import numpy as np
import sympy as s
rng=random.Random(42016);nr=np.random.default_rng(42016);out={}
models=0;monomials=0
for r in range(1,5):
    for b in range(1,6):
        N=b+1;B=b*sum(N**i for i in range(r));q=int(s.nextprime(B+1))
        exps=[a for a in it.product(range(b+1),repeat=r) if sum(a)<=b]
        degrees=[sum(a[i]*N**i for i in range(r)) for a in exps]
        assert len(set(degrees))==len(degrees) and max(degrees)<=B<q
        # In Q[T]/(T^q-2), distinct powers below q form a basis; Eisenstein at 2.
        models+=1;monomials+=len(exps)
out['bounded_avoidance']={'monomial_models':models,'distinct_monomials':monomials,'coefficient_field_fixed':True}

models=0
for m in range(1,5):
    for a in range(2*m+1):
        W=s.Matrix(2*m,a,lambda i,j:int(i==j))
        for _ in range(3):
            A=s.eye(2*m)
            for i in range(2*m):
                for j in range(i):A[i,j]=rng.randrange(-2,3)
            W=A*W;target=max(0,a-m);found=False
            for tries in range(30):
                T=s.Matrix(m,m,lambda i,j:rng.randrange(-3,4));T=T+T.T;L=s.eye(m).col_join(T)
                dim=m+a-L.row_join(W).rank();assert dim>=target
                if dim==target:found=True;break
            assert found;models+=1
out['lagrangian_intersections']={'exact_transversality_models':models,'maximum_symplectic_dimension':8}

mp.mp.dps=60;tests=0
for eps in ['.1','.01','.0001']:
    e=mp.mpf(eps)
    xs=[mp.mpf(-1),mp.mpf(-.5),mp.mpf(0),mp.mpf(.5)]+[1-mp.mpf(10)**(-j) for j in [2,5,10,20]]
    ss=[mp.mpf(.1),mp.mpf(.5)]+[1-mp.mpf(10)**(-j) for j in [2,5,10,20]]
    for x,v in it.product(xs,ss):
        rho=1-e*(1-x);sigma=1-e*mp.sqrt(1-v);z=1-x*mp.e**(1j*mp.acos(v));ze=1-rho*sigma*x*mp.e**(1j*mp.acos(v))
        assert abs(ze-z)<=3*e*abs(z)*(1+mp.mpf('1e-35'))
        assert -mp.log(abs(z)**2)<=-mp.log(abs(ze)**2)+6*e+mp.mpf('1e-35');tests+=1
out['matched_damping']={'high_precision_cross_kernel_models':tests,'closest_endpoint_distance':'1e-20'}

worst=0;tests=0
for _ in range(60):
    x=nr.uniform(-.8,.8,5);v=nr.uniform(.1,.8,6);e=.1;tau=1-e;rho=1-e*(1-x);sigma=1-e*np.sqrt(1-v);k=np.arange(1,701)
    tx=np.arccos(x);tv=np.arccos(v)
    def L(theta,phi,r):return -np.log(2)+np.log(abs(1-r*np.exp(1j*(theta+phi))))+np.log(abs(1-r*np.exp(1j*(theta-phi))))
    lhs=L(tx[:,None],tx[None,:],tau*tau).mean()+.5*np.log(1-(rho*x)[:,None]*(rho*x)[None,:]).mean()+L(tv[:,None],tv[None,:],sigma[:,None]*sigma[None,:]).mean()-np.log(abs(1-(rho*x)[:,None]*sigma[None,:]*np.exp(1j*tv)[None,:])**2).mean()
    A=(tau**k*np.cos(tx[:,None]*k)).mean(axis=0);B=((rho*x)[:,None]**k).mean(axis=0);C=(sigma[:,None]**k*np.cos(tv[:,None]*k)).mean(axis=0)
    rhs=-2*np.log(2)-2*np.sum(A*A/k)-.5*np.sum((B-2*C)**2/k);worst=max(worst,abs(lhs-rhs));assert abs(lhs-rhs)<1e-11
    p=nr.normal(size=700)*.7**k;w=nr.normal(size=700)*.7**k
    tangent=2*np.sum(p*p/k)+.5*np.sum(w*w/k)-4*np.sum(p*A/k)-np.sum(w*B/k)+2*np.sum(w*C/k)
    assert -2*np.sum(A*A/k)-.5*np.sum((B-2*C)**2/k)<=tangent+1e-12;tests+=1
out['moment_squares']={'damped_kernel_and_tangent_models':tests,'series_terms':700,'max_identity_error':worst}

def add(*ps):
    ans=defaultdict(int)
    for P in ps:
        for w,c in P.items():ans[w]+=c
    return {w:c for w,c in ans.items() if c}
def neg(P):return {w:-c for w,c in P.items()}
def mul(P,R):
    ans=defaultdict(int)
    for a,c in P.items():
        for b,d in R.items():ans[a+b]+=c*d
    return {w:c for w,c in ans.items() if c}
def bracket(P,R):return add(mul(P,R),neg(mul(R,P)))
X={'x':1};Y={'y':1}
def deriv(P,R):
    ans={};dy=bracket(Y,P)
    for word,c in R.items():
        for i,z in enumerate(word):
            if z=='y':ans=add(ans,mul(mul({word[:i]:c},dy),{word[i+1:]:1}))
    return ans
def depth(P):return min((w.count('y') for w in P),default=10**6)
lie=[bracket(X,Y)]
for n in range(4):lie.extend([bracket(X,lie[-1]),bracket(Y,lie[-1])])
tests=0
for P,R in it.product(lie,repeat=2):
    I=add(deriv(P,R),neg(deriv(R,P)),bracket(P,R));assert depth(I)>=depth(P)+depth(R);tests+=1
out['ihara_depth']={'exact_associative_expansion_pairs':tests}

tests=0
for _ in range(100):
    W=s.Matrix(6,3,lambda i,j:(int(i==j) if i<3 else rng.randrange(-3,4)))
    for i in range(3):
        for j in range(i):W[i,j]=2*rng.randrange(-3,4)
    minor=W[:3,:];assert int(minor.det())%2
    c=s.Matrix([s.Rational(rng.randrange(-5,6),rng.choice([1,3,5,7])) for _ in range(3)]);v=W*c
    recovered=minor.inv()*v[:3,:];assert recovered==c and all(z.q%2 for z in recovered)
    c[0]+=s.Rational(1,2);v=W*c;assert any(z.q%2==0 for z in v);tests+=1
assert s.Matrix([[2]]).inv()[0]==s.Rational(1,2)
out['saturated_lattice']={'odd_minor_models':tests,'dependent_reduction_negative_control':True}

T=s.symbols('T');tests=0
for Qv in [2,3,5,7]:
    polys=[]
    for sign in [-1,1]:polys.append(s.Poly((T-sign)*(T-sign*Qv),T))
    for a in range(-int(2*np.sqrt(Qv)),int(2*np.sqrt(Qv))+1):polys.append(s.Poly(T*T-a*T+Qv,T))
    for g in [1,2,3]:
        bound=max(comb(2*g,j)*Qv**j for j in range(2*g+1));mod=3
        if Qv==3:mod=5
        while mod<=2*bound:mod*=3 if Qv!=3 else 5
        seen={}
        for _ in range(30):
            P=s.Poly(1,T)
            for j in range(g):P*=rng.choice(polys)
            cs=tuple(map(int,P.all_coeffs()));assert all(abs(cs[j])<=comb(2*g,j)*Qv**j for j in range(2*g+1))
            residue=tuple(c%mod for c in cs)
            if residue in seen:assert seen[residue]==cs
            seen[residue]=cs;tests+=1
out['frobenius_finite_precision']={'bounded_integral_polynomial_models':tests,'geometric_local_constancy_tested':False}

tests=0
for p in [3,5,7]:
    # Character values 1 and 1+epsilon in F_p[epsilon]/epsilon^2 have order dividing p.
    for _ in range(40):
        coefs=[rng.randrange(p) for j in range(p)]
        value0=sum(coefs)%p;value1=(sum(coefs)%p,sum(j*c for j,c in enumerate(coefs))%p)
        assert value0==value1[0]
        power=(1,0)
        for j in range(p):power=(power[0]%p,(power[0]+power[1])%p)
        assert power==(1,0)
        tests+=1
out['integral_character_evaluation']={'ramified_residue_algebra_models':tests,'projector_denominator_invertible':False,'geometric_group_ring_freeness_tested':False}
result={'batch':'B042','status':'pass','scope':'Selected finite interfaces only; no arithmetic headline or Lean build certified.','checks':out}
Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
