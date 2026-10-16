"""Finite algebraic models of selected lemmas; no headline-theorem certification."""
from pathlib import Path
from itertools import product
from fractions import Fraction as F
import json, math, time
import numpy as np
import sympy as s

def mass():
    rng=np.random.default_rng(68036);cases=0
    for n in range(2,6):
        for _ in range(25):
            a=rng.normal(size=(n,n));c=a.T@a+np.eye(n)
            b=rng.normal(size=(n,n));g=b.T@b
            mixed=np.linalg.det(c)*np.trace(np.linalg.solve(c,g))
            assert mixed>=np.trace(g)-1e-8
            assert mixed>0;cases+=1
    # n=2 mixed determinant of diag(1,0) with itself vanishes.
    t=s.symbols('t');c=s.diag(1,0)
    assert s.expand((c+t*c).det()).coeff(t)==0 and c!=s.zeros(2)
    return dict(positive_models=cases,singular_test_class_negative_control=True)

def picard_descent_model():
    cases=0
    # Pic/Pic^0 torsion and an abstract connected-fiber evaluation pullback.
    for modulus in range(2,16):
        for torsion in range(modulus):
            order=modulus//math.gcd(modulus,torsion)
            assert (order*torsion)%modulus==0
            cases+=1
    evaluations=s.Matrix([[1,0,1],[0,1,1],[1,1,0]])
    fiber=[0,0,1,2,2,2]
    pulled=s.Matrix([list(evaluations.row(i)) for i in fiber])
    assert all(any(v!=0 for v in pulled.row(i)) for i in range(len(fiber)))
    bad=evaluations.copy();bad[1,:]=s.zeros(1,3)
    assert all(v==0 for v in s.Matrix([list(bad.row(i)) for i in fiber]).row(2))
    return dict(torsion_classes=cases,evaluation_fiber_model=True,scope='Abstract Picard quotient model, not verification of a geometric Picard isomorphism.')

def gauss_volume():
    cases=0;ratios=[]
    def counts(weights,k):
        dp=[0]*k;dp[0]=1
        for w in weights:
            for j in range(w,k):dp[j]+=dp[j-w]
        return sum(dp)
    for weights in [(1,),(1,2),(2,3),(1,2,3)]:
        for a in [1,2,4]:
            for k in [8,17,31]:
                assert counts(weights+(a,),k)==sum(counts(weights,k-i*a) for i in range((k-1)//a+1));cases+=1
            k=300;dim=len(weights)+1
            ratios.append(counts(weights+(a,),k)*math.factorial(dim)*math.prod(weights)*a/k**dim)
    A,a=s.symbols('A a',positive=True)
    for n in range(1,7):
        f=(A+a)**(n+1)/a
        assert s.simplify(s.diff(f,a)-(A+a)**n*(n*a-A)/a**2)==0
        assert s.simplify(f.subs(a,A/n)/(n+1)**(n+1)-A**n/n**n)==0
    assert max(abs(r-1) for r in ratios)<.08
    return dict(exact_colength_convolutions=cases,asymptotic_ratios=ratios,optimized_dimensions=6)

def hilbert():
    k,z,t=s.symbols('k z t');cases=0
    for n in range(1,6):
        q=s.sympify(s.prod(k+j for j in range(1,n)))/math.factorial(n-1)
        for j in range(-20,21):
            expected=math.comb(j+n-1,n-1) if j>=0 else ((-1)**(n-1)*math.comb(-j-1,n-1) if -j>=n else 0)
            assert q.subs(k,j)==expected;cases+=1
        H=1/(1-z)**n;canonical=z**n/(1-z)**n
        assert s.simplify(canonical-(-1)**n*H.subs(z,1/z))==0
    # weights 1,2: exact polynomial plus alternating wave, canonical shift 3.
    for j in range(-30,31):
        q=F(j,2)+F(3,4)+F((-1)**j if j>=0 else (-1)**(-j),4)
        expected=j//2+1 if j>=0 else -((-j-3)//2+1) if j<=-3 else 0
        assert q==expected;cases+=1
    lam=s.Rational(1,5)
    polar=s.series(1/((1-s.exp(-lam*t))*(1-s.exp(-2*lam*t))),t,0,1).removeO()
    assert s.expand(polar).coeff(t,-2)==1/(2*lam**2)
    assert s.expand(polar).coeff(t,-1)==3/(4*lam)
    assert 1/(lam*2)>1 and 1/lam>1
    return dict(exact_signed_coefficients=cases,canonical_duality_dimensions=5,weighted_polar_density='y/(2 lambda^2)+3/(4 lambda)',frequency_exclusion=True)

def profiles():
    x,y=s.symbols('x y');basis=[1,x,y]
    def mat(points):return s.Matrix([[s.sympify(f).subs({x:a,y:b}) for f in basis] for a,b in points])
    assert mat([(0,0),(1,0),(2,0)]).rank()==2
    assert mat([(0,0),(1,0),(0,1)]).rank()==3
    cases=0
    for r in range(2,7):
        for profile in product(range(3),repeat=r):
            assert all(sum(profile[(i+j)%r] for j in range(r))==sum(profile) for i in range(r));cases+=1
    # Three collinear points: individual factors give a direct product profile.
    points=[0,1,2];profile=[1,2,3]
    polynomials=[s.prod((x-points[i])**profile[(i+j)%3] for i in range(3)) for j in range(3)]
    f=s.prod(polynomials)
    assert s.degree(f,x)==18
    for a in points:
        assert all(s.diff(f,x,j).subs(x,a)==0 for j in range(6))
        assert s.diff(f,x,6).subs(x,a)!=0
    return dict(cyclic_profiles=cases,rank_drop_example=True,product_multiplicities=[6,6,6])

def weighted_jets():
    x,u,t=s.symbols('x u t');points=[(1,1),(2,3)]
    basis=[x**a*u**g for a in range(4) for g in range(2)]
    deform=[(x**a+t*x**(a+1)+t**2*x**(a+2))*u**g for a in range(4) for g in range(2)]
    def jets(fs):return s.Matrix([[s.diff(f,x,dx,u,du).subs({x:a,u:b}) for f in fs] for a,b in points for dx,du in [(0,0),(1,0),(0,1)]])
    M=jets(basis);N=jets(deform)
    assert M.rank()==6 and N.subs(t,0)==M
    pivot=M.rref()[1];minor=N[:,list(pivot)].det();assert minor.subs(t,0)!=0
    for scale in [s.Rational(1,2),s.Rational(1,10),s.Rational(1,100)]:assert minor.subs(t,scale)!=0
    for a,b in product(range(4),repeat=2):
        f=s.Poly((x**a+x**(a+1))*(x**b+2*x**(b+2)),x)
        assert min(m[0] for m,c in f.terms())==a+b
    return dict(jet_rows=6,jet_columns=8,nonzero_minor_at_zero=str(minor.subs(t,0)),small_scales=3,least_term_products=16)

def prolongation():
    results=[]
    for u,w in [(1,1),(2,1),(3,1),(1,2),(2,2),(3,2),(2,3)]:
        dim=u*w;unknown=dim*u*u;rows=[]
        def ix(x,a,b):return (x*u+a)*u+b
        for x,y,z in product(range(dim),repeat=3):
            # B_x(y) = A_x(v_y) tensor w_y.
            vx,wx=divmod(x,w);vy,wy=divmod(y,w);vz,wz=divmod(z,w)
            row=[0]*unknown
            if wz==wy:row[ix(x,vz,vy)]+=1
            if wz==wx:row[ix(y,vz,vx)]-=1
            if any(row):rows.append(row)
        rank=s.Matrix(rows).rank() if rows else 0
        nullity=unknown-rank
        assert nullity==(u*u*(u+1)//2 if w==1 else 0)
        results.append(dict(U=u,W=w,nullity=nullity))
    return results

def rotation():
    I=s.Matrix([[0,-1,0,0],[1,0,0,0],[0,0,0,-1],[0,0,1,0]])
    J=s.Matrix([[0,0,-1,0],[0,0,0,1],[1,0,0,0],[0,-1,0,0]])
    K=I*J;assert I*J==-J*I and K*K==-s.eye(4)
    e=s.eye(4)[:,0];cases=[]
    for c,d in [(s.Integer(1),0),(s.Rational(3,5),s.Rational(4,5)),(0,s.Integer(1)),(-1,0)]:
        B=s.Matrix.hstack(e,c*J*e+d*K*e)
        assert B.T*B==s.eye(2) and B.T*I*B==s.zeros(2)
        assert (B.T*J.T*B)[0,1]==c and (B.T*K.T*B)[0,1]==d
        assert c*c+d*d==1 and abs(c)<=1
        invariant=(s.eye(4)-B*B.T)*J*B==s.zeros(4,2)
        assert invariant==(d==0);cases.append([str(c),str(d),bool(invariant)])
    # Opposite angles: special phase zero, but neither plane is J-invariant.
    c=s.Rational(3,5);d=s.Rational(4,5)
    assert s.expand((c+s.I*d)*(c-s.I*d))==1 and c*c<1
    return dict(quaternionic_planes=cases,opposite_angle_negative_control=True,scope='Linear calibration algebra; compact existence and Albanese geometry are not tested.')

if __name__=='__main__':
    start=time.perf_counter();checks={}
    for f in [mass,picard_descent_model,gauss_volume,hilbert,profiles,weighted_jets,prolongation,rotation]:checks[f.__name__]=dict(status='pass',details=f())
    result=dict(batch='B068',status='pass',elapsed_seconds=round(time.perf_counter()-start,3),scope='Selected finite models only; no certification of source headline theorems or formal solutions.',checks=checks)
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))
