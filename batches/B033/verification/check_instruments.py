"""Selected exact identities and finite models; not the source global theorems."""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import json
import math
import numpy as np
import sympy as s
from scipy.integrate import quad

def endpoint_jets():
    z,q=s.symbols('z q'); cases=0
    for M in range(3,10):
        common=sum((j+1)*z**j for j in range(M+1))
        difference=z**(M+1)*(1+q+z)
        for j in range(M+1):assert s.diff(difference,z,j).subs(z,0)==0
        for delta in (.1,.03,.01):
            # Unit q and |z|<=delta: |difference|<=3 delta^(M+1).
            zz=delta*np.exp(.7j);qq=np.exp(.3j)
            assert abs(complex(difference.subs({z:zz,q:qq})))<=3*delta**(M+1)
            # A right-inverse loss delta^-1 leaves delta^M correction.
            assert 3*delta**M<1
            cases+=1
    return dict(jet_orders=7,complex_overlap_models=cases,scope='Polynomial endpoint jets and collar exponents only; no manifold-valued approximation theorem tested.')

def quadratic_gluing():
    e,v=s.symbols('e v');a=-e*v*v/2;b=e*v*v/2
    target=s.expand(v+a+e*(v+a)**2)
    # beta(v+d)=gamma(alpha(v)); solve coefficients to second order.
    d=-e**2*v**3
    residual=s.expand((v+d)+b.subs(v,v+d)-target)
    assert s.series(residual,e,0,3).removeO()==0
    n=0
    for p in (1,2,4,7):
        A=F(3);E=F(1,4);err=E/(A*2**p)
        for i in range(9):
            next_err=A*2**(p*i)*err**2
            next_E=A*2**(p*(i+2))*next_err
            assert next_E==E**2
            assert next_E<=F(1,4)**(2**(i+1))
            err,E=next_err,next_E;n+=1
    return dict(exact_second_order_cancellation=True,exact_recurrence_steps=n,scope='Quadratic improvement and rescaling; no dbar solution or moving-spray bound certified.')

def green_determinant():
    x=s.symbols('x');n=0
    for degree in range(1,7):
        for dimension in range(1,5):
            u=sum(s.Rational(j+1,5)*(1-x)**degree for j in range(dimension))
            curvature=-s.diff(x*s.diff(u,x),x)
            val=s.integrate(-s.log(x)*curvature,(x,0,1))
            assert s.simplify(val-u.subs(x,0))==0
            assert s.integrate(curvature,(x,0,1))==-s.diff(u,x).subs(x,1)
            n+=1
    return dict(exact_radial_logdet_green_models=n,scope='Curvature sign and normalization; existence of boundary-unitary holomorphic frames is not tested.')

def weak_trace_boundary():
    cases=0;worst=0.
    for dimension in range(1,5):
        coeff=np.arange(1,dimension+1)/7
        # N=diag(exp(a_i(1-x))), x=|z|^2. Hessian integrand (xT)' + x(xT)''.
        def integrand(x):
            N=np.exp(coeff*(1-x));T=N.sum();Tp=-(coeff*N).sum();Tpp=(coeff**2*N).sum()
            return T+3*x*Tp+x*x*Tpp
        value=quad(integrand,0,1,epsabs=1e-12)[0]
        expected=dimension-coeff.sum();worst=max(worst,abs(value-expected));assert abs(value-expected)<1e-11
        cases+=1
    # Boundary derivatives need not exist: alpha in (1/2,1) gives W^{1,2}.
    for alpha in (.55,.6,.75,.9):
        errors=[]
        for distance in (1e-2,1e-4,1e-6,1e-8):
            u=distance**alpha;du=alpha*distance**(alpha-1)
            err=abs(np.expm1(u)*du)
            assert err<=2*alpha*distance**(2*alpha-1)
            errors.append(err);cases+=1
        assert all(a>b for a,b in zip(errors,errors[1:]))
    return dict(radial_area_and_sobolev_models=cases,max_quadrature_error=worst,scope='Smooth area identities and nonsmooth W1,2 boundary examples; no global canonical ampleness claim tested.')

def alternating(A0,A1,A2,x,y):
    return s.expand(s.trace(A0*(A1.diff(x)*A2.diff(y)-A1.diff(y)*A2.diff(x)-A2.diff(x)*A1.diff(y)+A2.diff(y)*A1.diff(x))))

def moving_basis_trace():
    x,y=s.symbols('x y');N=s.zeros(3);N[0,1]=1
    A1=s.diag(x,x,x+1)+N;A2=s.diag(y,y,y+2)+2*N
    A0=(x+1)*s.eye(3)-A1
    assert A0*A0!=A0 # Spectral selector need not be idempotent.
    base=alternating(A0,A1,A2,x,y);assert base==4
    checked=0
    for k in (1,2,3):
        G=s.Matrix([[1,x,0],[0,1,y],[0,0,1]])*s.Matrix([[1,0,0],[k*y,1,0],[x,0,1]])
        Gi=G.inv();B=[G*A*Gi for A in (A0,A1,A2)]
        assert s.expand(alternating(*B,x,y)-base)==0
        assert any(s.expand(t)!=0 for t in B[0]*B[1].diff(x)-B[1].diff(x)*B[0])
        checked+=1
    return dict(exact_variable_basis_models=checked,nonsemisimple=True,nonidempotent_selector=True,scope='Exact two-form identities; general proof is the source telescoping argument.')

def spectral_selection():
    x,y=s.symbols('x y');checks=0
    for multiplicity in (1,2,3):
        # Distinct polynomial joint tuples, with a repeated chosen tuple.
        tuples=[(x,y)]*multiplicity+[(x+1,y+2),(x+3,y-1)]
        A1=s.diag(*(t[0] for t in tuples));A2=s.diag(*(t[1] for t in tuples))
        I=s.eye(len(tuples));A0=(A1-(x+1)*I)*(A1-(x+3)*I)/3
        assert alternating(A0,A1,A2,x,y)==2*multiplicity
        checks+=1
    for n in range(1,8):
        for a in range(1,n+2):
            for b in range(1,n+2):
                L=lambda k:s.Matrix(n+1,n+1,lambda i,j:int(j-i==k))
                product=L(a)*L(b)
                assert (product!=s.zeros(n+1))==(a+b<=n)
                checks+=1
    return dict(spectral_and_grading_models=checks,scope='Selector multiplicity and grading obstruction; algebraic independence of source quantum eigenvalues is not certified.')

def rational_curve_involution():
    c,d,a,b,u,v,h,l=s.symbols('c d a b u v h l')
    reduce=lambda f:s.rem(s.Poly(s.expand(f),c),s.Poly(c*c-d,c)).as_expr()
    bar=lambda f:s.expand(f.subs(c,-c))
    delta=lambda f:2*s.Poly(reduce(f),c).coeff_monomial(c)
    alpha=a+c*b;gamma=u+c*v
    assert reduce(bar(alpha*gamma)-bar(alpha)*bar(gamma))==0
    assert reduce(delta(alpha*gamma)-delta(alpha)*gamma-bar(alpha)*delta(gamma))==0
    for exponent in range(1,16):
        assert s.expand((h**exponent-(l-h)**exponent)-(2*h-l)*sum(h**k*(l-h)**(exponent-1-k) for k in range(exponent)))==0
        assert reduce(delta(c**exponent)-(1-(-1)**exponent)*c**(exponent-1))==0
    return dict(exact_ring_product_rule=True,power_identities=30,scope='Rational cohomology algebra; geometric Leray-Hirsch and GRR inputs are read, not computationally proved.')

def modular_certificate():
    rng=np.random.default_rng(33067);checks=0
    for n in range(3,9):
        for rank in range(1,n):
            # Integral row-equivalent matrix with a known rational kernel.
            M=s.Matrix(rank,n,lambda i,j:int(i==j) if j<rank else int(rng.integers(-8,9)))
            Z=s.Matrix.vstack(-M[:,rank:],s.eye(n-rank))
            assert M*Z==s.zeros(rank,n-rank)
            assert Z.rank()==n-rank
            # Identity minor is a unit modulo any prime, completing both bounds.
            assert int(M[:,:rank].det())%10007==1
            ell=s.Matrix([[int(rng.integers(-4,5)) for _ in range(rank)]])*M
            assert ell*Z==s.zeros(1,n-rank);checks+=1
    # Modular annihilation alone is insufficient over Q.
    assert s.Matrix([[10007]])%10007==s.zeros(1,1)
    assert s.Matrix([[10007]]).rank()==1
    v=s.symbols('v');assert s.expand((v-4)*(3*v-8))==3*v*v-20*v+32
    return dict(exact_kernel_certificates=checks,modular_only_negative_control=True,scope='Certificate architecture only. The source 8280 by 6820 constraint matrix and its reported ranks have NOT been recomputed.')

if __name__=='__main__':
    groups={}
    for fn in (endpoint_jets,quadratic_gluing,green_determinant,weak_trace_boundary,moving_basis_trace,spectral_selection,rational_curve_involution,modular_certificate):
        groups[fn.__name__]=fn();print(fn.__name__,'passed',flush=True)
    out=dict(batch='B033',status='passed',check_groups=groups,limitations='Selected identities and finite models only; no K3 Oka, canonical ampleness, generalized Mukai or dimension-six classification theorem certified; no Lean build.')
    Path(__file__).with_name('results.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out,indent=2))
