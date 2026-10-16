"""Selected finite models and identities; not certification of source headlines."""
import json
import time
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import math
import cmath
import numpy as np
import sympy as s


def spectral():
    x,z=s.symbols('x z');order=4
    M=s.Matrix([[1,x],[0,1]]);Mi=M.inv();A=s.diag(2,3)
    def trunc(v):return v.applyfunc(lambda a:sum(s.expand(a).coeff(z,k)*z**k for k in range(order+1)))
    def T(v):
        w=Mi*v
        shift=sum((w.diff(x,k)*z**k/s.factorial(k) for k in range(order+1)),s.zeros(2,1))
        return trunc(M*A*shift)
    P=M*s.diag(1,0)*Mi
    assert P*P==P and P+(s.eye(2)-P)==s.eye(2)
    cases=0
    for degree in range(5):
        v=s.Matrix([x**degree+x,2*x**degree+1])
        assert trunc(T(x*v)-x*T(v)-z*T(v))==s.zeros(2,1)
        assert trunc(T(P*v)-P*T(v))==s.zeros(2,1)
        powers=[v]
        xpowers=[x*v]
        for k in range(1,4):powers.append(T(powers[-1]));xpowers.append(T(xpowers[-1]))
        for coeff in [(1,2,3,4),(0,0,1,-2)]:
            fv=sum((coeff[k]*powers[k] for k in range(4)),s.zeros(2,1))
            fxv=sum((coeff[k]*xpowers[k] for k in range(4)),s.zeros(2,1))
            rhs=z*sum((k*coeff[k]*powers[k] for k in range(4)),s.zeros(2,1))
            assert trunc(fxv-x*fv-rhs)==s.zeros(2,1);cases+=1
    return dict(polynomial_commutators=cases,translation_order=order,gauge_and_projector=True)


def tensor_detection():
    rng=np.random.default_rng(7101);cases=0;negative=0
    # Use the inverse-pairing kernel in the source's ordered slots.
    for n,Q,C in [(0,np.eye(2),np.eye(2)),(1,np.array([[0.,1.],[-1.,0.]]),np.array([[0.,1.],[-1.,0.]]))]:
        sign=(-1)**(n*(n-1)//2);B=sign*C.T@Q;delta=np.linalg.inv(Q);K=sign*C@delta
        assert np.allclose(B,np.eye(2)) and np.allclose(K,np.eye(2))
        for r in range(5):
            if n*r%2:continue
            e=rng.normal(size=2**r)+1j*rng.normal(size=2**r)
            kernel=np.array([[1.]])
            for _ in range(r):kernel=np.kron(kernel,K)
            norm=np.vdot(e,e).real;interleave=(-1)**(n*r*(r-1)//2)
            block_contraction=interleave*(e@kernel@e.conjugate()).real
            assert abs(interleave*block_contraction-norm)<1e-10
            if interleave==-1:assert block_contraction<0;negative+=1
            cases+=1
    assert negative>0
    return dict(polarized_tensor_models=cases,odd_sign_negative_controls=negative)


def thresholds():
    cases=0
    for a in [(-2,3,1),(1,5,0),(4,2,7)]:
        m=(2,3,0);minimum=min(F(a[i],m[i]) for i in [0,1])
        for w in product(range(5),repeat=3):
            den=sum(m[i]*w[i] for i in range(3))
            if not den:continue
            val=F(sum(a[i]*w[i] for i in range(3)),den)
            assert val>=minimum
            for d in [-3,0,2]:assert F(sum((a[i]+d*m[i])*w[i] for i in range(3)),den)==val+d
            cases+=1
        assert any(F(a[i],m[i])==minimum for i in [0,1])
    # Three finite sets of divisors over an intermediate divisor; all ramification factors positive.
    for c in range(-3,5):
        groups=[[(F(c),2),(F(c+3),5)],[(F(7-c),3),(F(-c),4)]];base=[2,5]
        iterated=min(min(a/m for a,m in group)/base[j] for j,group in enumerate(groups))
        direct=min(a/(m*base[j]) for j,group in enumerate(groups) for a,m in group)
        assert iterated==direct
    return dict(monomial_valuations=cases,negative_thresholds=True,tower_models=8)


def neutral_generators():
    # Weights (2,3,5) lie on the old line; new coordinates e2,e3 are independent modulo it.
    W=s.Matrix([[2,3,5,0,0],[0,0,0,1,0],[0,0,0,0,1]])
    cases=0
    for e1,e2 in product(range(-6,7),repeat=2):
        numerator=-3*e1-5*e2
        if numerator%2:continue
        e=s.Matrix([numerator//2,e1,e2,0,0]);assert W*e==s.zeros(3,1)
        assert 2*e==e1*s.Matrix([-3,2,0,0,0])+e2*s.Matrix([-5,0,2,0,0]);cases+=1
    t=s.symbols('t');polynomials=0
    for k in range(-3,4):
        for a in [1,s.sqrt(2),1+s.sqrt(2)]:
            f=s.expand(a*t**k+(2-a)*t**k+3*t**(k+2))
            coeff=s.expand(f*t**(-k)).coeff(t,0);assert coeff==2;polynomials+=1
            cancelled=s.expand(a*t**k-a*t**k+t**(k+1));assert s.expand(cancelled*t**(-k)).coeff(t,0)==0
    # All nonzero coefficients in an algebraic equation have value zero.
    for degree in range(1,9):
        for v in list(range(-5,0))+list(range(1,6)):
            values=[j*v for j in range(degree+1)];assert values.count(min(values))==1
    return dict(weight_kernel_vectors=cases,least_initial_examples=polynomials,cancellation_controls=polynomials,algebraic_unique_minimum_cases=80)


def section_interpolation():
    cases=0;obstructions=0
    for m1 in range(1,5):
        for m2 in range(m1+1,m1+5):
            k=m2-m1
            for mi in range(m2+1,m2+10):
                assert k+(mi-m2)==mi-m1
                assert k*mi+(mi-m2)*m1==(mi-m1)*m2
                for slope in range(4):
                    a1=3;a2=a1+k*slope;ai=a1+(mi-m1)*slope
                    assert k*(ai-a1)==(mi-m1)*(a2-a1);cases+=1
            for neg in range(1,5):
                mi=m1+k*(3+neg+1);ai=F(3)-F((mi-m1)*neg,k)
                assert ai<0;obstructions+=1
    u,v=s.symbols('u v');rho=v**2
    for j in range(5):
        e1=(u+1)*rho**j;e2=(u**2+2)*rho**j
        assert s.simplify(e1/e2)==(u+1)/(u**2+2)
    return dict(order_interpolations=cases,negative_slope_obstructions=obstructions,base_ratio_models=5)


def lattice_counts():
    m=s.symbols('m');checks=0
    # Rational translated interval [1/2,3/2], with m=2n.
    def interval(n):return sum(3+x*x+2*n*x+4*n*n for x in range(n,3*n+1))
    p=s.interpolate([(n,interval(n)) for n in range(1,6)],m)
    assert p.subs(m,0)==3
    for n in range(6,11):assert p.subs(m,n)==interval(n);checks+=1
    def simplex(n):return sum(5+x*y+n*x for x in range(n+1) for y in range(n+1-x))
    p=s.interpolate([(n,simplex(n)) for n in range(1,7)],m);assert p.subs(m,0)==5
    for n in range(7,12):assert p.subs(m,n)==simplex(n);checks+=1
    rng=np.random.default_rng(7102);retracts=0
    for dim in range(3,8):
        for count in range(1,(dim-1)//2+1):
            u=np.ones(dim);u[:count]=-1;total=u.sum()
            for _ in range(30):
                x=rng.dirichlet(np.ones(dim))*total;t=max(1/(1+x[:count]));r=u+t*(x-u)
                assert min(r)>-1e-12 and abs(sum(r)-total)<1e-10 and min(abs(r[:count]))<1e-10
                assert abs(max(1/(1+r[:count]))-1)<1e-10
                for h in [0,.25,.5,1]:assert min((1-h)*x+h*r)>-1e-12
                retracts+=1
    return dict(unused_dilation_checks=checks,weighted_zero_values=[3,5],retraction_points=retracts)


def quadratic_waves():
    cases=0;maxscaled=0.
    # Gaussian g(y)=exp(-pi y^2), ghat=g, a Schwartz test of the exact Fourier identity.
    for beta,T,y0 in product([-2.,-.5,.5,2.],[2.,5.,20.,80.],[-3.,-.4,0.,.7,4.]):
        u=T*beta*y0;a=1-1j*T*beta
        integral=a**(-.5)*cmath.exp(-math.pi*u*u/a)
        factor=cmath.exp(2j*math.pi*(np.sign(beta)/8-u*u/(2*T*beta)))/math.sqrt(T*abs(beta))
        b=1+1j/(T*beta)
        bracket=b**(-.5)*cmath.exp(-math.pi*y0*y0/b)
        assert abs(integral-factor*bracket)<2e-12
        error=abs(bracket-math.exp(-math.pi*y0*y0));bound=1/(2*T*abs(beta))
        assert error<=bound+1e-12;cases+=1;maxscaled=max(maxscaled,error/bound)
    return dict(exact_gaussian_models=cases,max_error_bound_ratio=maxscaled)


def defect_rounding():
    rng=np.random.default_rng(7103);cases=0;stages=0
    for N in range(1,10):
        for trial in range(5):
            X=rng.integers(-16,17,N)/16 if trial else np.ones(N)
            sigma=np.where(X>=0,1,-1);p=(1-np.abs(X))/2;mu=sum(p)
            M=20*N;theta=2*np.pi*np.outer(np.arange(M)/M,np.arange(N));E=np.exp(1j*theta)
            A=np.vstack([(E*sigma).real,(E*sigma).imag]);q=p.copy()
            for j in range(5,0,-1):
                idx=np.where(np.rint(q*2**j).astype(int)%2)[0];old=sum(q)
                assert len(idx)<=min(N,2**j*mu)+1e-12
                if not len(idx):continue
                options=np.array(list(product([-1,1],repeat=len(idx))))
                errors=np.max(np.abs(A[:,idx]@options.T),axis=0);xi=options[np.argmin(errors)]
                if sum(xi)>0:xi=-xi
                q[idx]+=xi*2.**(-j)
                assert min(q)>=0 and max(q)<=1 and sum(q)<=old+1e-12
                assert np.allclose(q*2**(j-1),np.rint(q*2**(j-1)));stages+=1
            eps=sigma*(1-2*q);assert set(eps)<=set([-1,1])
            coeff=eps-X;assert np.allclose(coeff,-2*sigma*(q-p))
            grid=max(abs(E@coeff));dense=max(abs(np.exp(2j*np.pi*np.outer(np.arange(4000)/4000,np.arange(N)))@coeff))
            assert dense<=grid/(1-math.pi*math.e/20)+1e-10
            if mu==0:assert np.all(coeff==0)
            cases+=1
    return dict(rounding_examples=cases,dyadic_stages=stages,zero_defect=True,grid_to_circle=True)


if __name__=='__main__':
    start=time.perf_counter();checks={}
    for f in [spectral,tensor_detection,thresholds,neutral_generators,section_interpolation,lattice_counts,quadratic_waves,defect_rounding]:checks[f.__name__]=dict(status='pass',details=f())
    result=dict(batch='B071',status='pass',elapsed_seconds=round(time.perf_counter()-start,3),scope='Selected finite models and identities; no source headline or Lean certification.',checks=checks)
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
