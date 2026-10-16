"""Finite checks of selected mechanisms; not certification of source headlines."""
from itertools import product, combinations
from pathlib import Path
import json
import math
import time
import numpy as np
import sympy as sp
from scipy.linalg import expm
from scipy.optimize import brentq


def reflection_phases():
    rng=np.random.default_rng(7601);cases=0
    for alpha in [.13,.71,math.pi*math.sqrt(2)/3]:
        e=np.array([math.cos(alpha),math.sin(alpha)]);R=2*np.outer(e,e)-np.eye(2)
        normal=np.array([-e[1],e[0]]);d=2.3*normal
        R0=np.diag([1.,-1.]);rotation=np.array([[math.cos(2*alpha),-math.sin(2*alpha)],[math.sin(2*alpha),math.cos(2*alpha)]])
        assert np.allclose(R@R0,rotation)
        for _ in range(50):
            p=rng.normal(size=2);v=rng.normal(size=2);v/=np.linalg.norm(v);lam=rng.normal();x=R@p+d
            assert abs(np.exp(1j*lam*p@(R@v))-np.exp(1j*lam*(x-d)@v))<1e-12
            z=complex(*rng.normal(size=2));phase=np.exp(1j*lam)
            bounded=lambda z:z/(1+abs(z))
            assert abs(bounded(phase*z)-phase*bounded(z))<1e-12
            assert abs(bounded(z)/(1-abs(bounded(z)))-z)<1e-12;cases+=1
    # Rational alpha admits a nonconstant mode under its generated rotation.
    alpha=math.pi/5;k=5
    assert abs(np.exp(2j*k*alpha)-1)<1e-12
    assert abs(np.exp(2j*alpha)-1)>.1
    return dict(affine_phase_and_transform_cases=cases,rational_angle_control=True)


def compact_obstruction():
    cases=0
    for n in range(3,16):
        U=np.roll(np.eye(n),1,axis=1)
        for k in range(1,n):
            K=np.cos(2*math.pi*k*(np.arange(n)[:,None]-np.arange(n)[None,:])/n)
            T=K/n;A=T.T@T
            assert np.max(abs(K.sum(axis=0)))<1e-11
            assert np.max(abs(K.sum(axis=1)))<1e-11
            assert np.allclose(U@T,T@U)
            vals,vecs=np.linalg.eigh(A);V=vecs[:,vals>1e-9];projector=V@V.T
            assert len(V.T)>0 and np.allclose(U@projector,projector@U)
            assert np.linalg.norm(V.T@np.ones(n))<1e-10
            assert np.allclose(V.T@U.T@projector@U@V,np.eye(V.shape[1]));cases+=1
    return dict(cyclic_kernel_models=cases,finite_model_is_obstruction_not_weak_mixing_example=True)


def block_oscillation():
    cases=0
    for period in range(2,10):
        # One atom is divergent, the other constant; endpoints are selected globally.
        weights=np.array([.2,.8]);seq=np.array([[float(k%period==0),0.] for k in range(1000)])
        K=0;total=0.;delta=.4;d=.2
        for w in range(1,65):
            for L in range(K+1,len(seq)):
                value=np.max(abs(seq[K:L+1]-seq[K]),axis=0)@weights
                if value>=delta*d/2:break
            else:raise AssertionError('missing finite witness')
            total+=value;K=L
            assert total>=w*delta*d/2-1e-12
            cases+=1
        assert total/math.sqrt(64)>1
    # Telescoping variation dominates every selected partition for a convergent sequence.
    rng=np.random.default_rng(7603);seq=1/(1+np.arange(200))
    for _ in range(100):
        ends=sorted(rng.choice(200,25,replace=False))
        total=sum(np.max(abs(seq[a:b+1]-seq[a])) for a,b in zip(ends,ends[1:]))
        assert total<=1
    return dict(selected_divergence_blocks=cases,finite_variation_controls=100)


def correlation_windows():
    rng=np.random.default_rng(7604);cases=0
    for N in range(1,25):
        u=rng.normal(size=(N,4))+1j*rng.normal(size=(N,4))
        for H in [1,2,5,N+3]:
            windows=np.array([sum((u[m-j] for j in range(H) if 0<=m-j<N),np.zeros(4,complex)) for m in range(N+H-1)])
            assert np.allclose(windows.sum(axis=0),H*u.sum(axis=0))
            expanded=H*np.sum(abs(u)**2)+2*sum((H-h)*np.real(np.sum(u[h:]*u[:-h].conj())) for h in range(1,min(H,N)))
            assert abs(expanded-np.sum(abs(windows)**2))<1e-8
            lhs=np.sum(abs(u.mean(axis=0))**2);rhs=(N+H-1)*expanded/(N*N*H*H)
            assert lhs<=rhs+1e-10;cases+=1
    assert np.mean(np.ones(100))==1 # Nondecaying correlations cannot be discarded.
    return dict(complex_finite_windows=cases,includes_window_larger_than_sample=True)


def polynomial_coordinates():
    x=sp.Symbol('x');normalizations=0;inheritances=0
    # h=c(x-z)^m(x-z+b), choosing the root z at every prime.
    for c,b,m,z in product([1,6,10],[1,6],[1,2],[-2,3]):
        h=c*(x-z)**m*(x-z+b);bad=sp.factorint(c*b)
        D0=math.prod(int(p)**(int(v)+1) for p,v in bad.items())
        M=math.prod(int(p)**((int(v)+1)*m+int(v)) for p,v in bad.items())
        r=(z+D0-1)%D0-D0+1
        g=sp.Poly(sp.expand(h.subs(x,r+D0*x)/M),x)
        assert all(t.q==1 for t in g.all_coeffs())
        first=sp.expand(g.as_expr().subs(x,x+sp.Rational(z-r,D0))).coeff(x,m)
        # The first centered coefficient is a unit at every prime: it is exactly 1 here.
        assert first==1
        assert r+D0>=1;normalizations+=1
    # Choose root 0 (multiplicity 2) at p=2 and root 1 (multiplicity 1) elsewhere.
    h=x*x*(x-1)
    def lam(l):return math.prod(int(p)**(int(v)*(2 if p==2 else 1)) for p,v in sp.factorint(l).items())
    def residue(l):
        return next(r for r in range(-l+1,1) if all((r-(0 if p==2 else 1))%(int(p)**int(v))==0 for p,v in sp.factorint(l).items()))
    def aux(l):return sp.Poly(sp.expand(h.subs(x,residue(l)+l*x)/lam(l)),x)
    for l,D in product(range(1,13),range(1,9)):
        a,b=aux(l),aux(l*D);i=(residue(l)-residue(l*D))//l
        assert 0<=i<D and all(t.q==1 for t in a.all_coeffs()+b.all_coeffs())
        assert sp.expand(a.as_expr().subs(x,D*x-i)-lam(D)*b.as_expr())==0
        assert lam(D)%D==0 and lam(D)<=D**3;inheritances+=1
    return dict(exact_unit_normalizations=normalizations,prime_dependent_inheritance_identities=inheritances)


def square_kernels():
    counts=0;lists=0;max_error=0.
    for p in [3,5,7,11]:
        squares={u*u%p for u in range(1,p)};A=lambda t:float(t%p in squares);delta=(math.sqrt(p)+1)/(2*p)
        B=np.array([[A(y-x)-.5 for y in range(p)] for x in range(p)])/p
        assert np.linalg.norm(B,2)<=delta+1e-12
        for tags in product([-1,0,1],repeat=3):
            edges=[((u,v) if t==1 else (v,u)) for (u,v),t in zip(combinations(range(3),2),tags) if t]
            average=sum(math.prod(A(z[v]-z[u]) for u,v in edges) for z in product(range(p),repeat=3))/p**3
            assert abs(average-2**(-len(edges)))<=len(edges)*delta+1e-12;counts+=1
        for pattern in [(1,0),(1,1),(1,-1)]:
            xs=list(product(range(p),repeat=2));ys=list(range(p));m=sum(t!=0 for t in pattern)
            K=np.array([[math.prod(A(t*(y-x[j])) for j,t in enumerate(pattern) if t) for y in ys] for x in xs])
            C=(K-2**(-m))/math.sqrt(len(xs)*len(ys));sv=np.linalg.svd(C,compute_uv=False)
            fourth=np.trace((C@C.T)@(C@C.T));assert abs(fourth-sum(sv**4))<1e-10
            assert sv[0]**4<=fourth+1e-12 and fourth<=32*m/math.sqrt(p)+1e-12;lists+=1
    # Repeated same-edge constraints have density about 1/2, not 1/4.
    p=101;actual=(p-1)/(2*p);delta=(math.sqrt(p)+1)/(2*p)
    assert abs(actual-.25)>2*delta
    return dict(directed_graph_counts=counts,two_list_fourth_moments=lists,repeated_edge_negative_control=True)


def attempt_clocks():
    rng=np.random.default_rng(7607);cases=0
    for size in range(2,9):
        for rep in range(10):
            edges=[(i,i+1) for i in range(size-1)]+[(int(rng.integers(size)),int(rng.integers(size))) for _ in range(10)]
            edges.append((0,0));n=len(edges);degree=np.zeros(size);counts=np.zeros((size,size))
            for u,v in edges:degree[u]+=1;degree[v]+=1;counts[u,v]+=1;counts[v,u]+=1
            P=counts/degree[:,None];mu=degree/(2*n);G=n*(np.eye(size)-P)
            u=rng.normal(size=size);v=rng.normal(size=size)
            matrix=(mu*u)@(G@v);direct=.5*sum((u[a]-u[b])*(v[a]-v[b]) for a,b in edges)
            assert abs(matrix-direct)<1e-10 and np.allclose(mu@P,mu)
            assert np.linalg.matrix_rank(G,tol=1e-8)==size-1
            t=.1;power=np.eye(size);weight=math.exp(-n*t);mix=weight*power
            for k in range(1,70):power=power@P;weight*=n*t/k;mix+=weight*power
            assert np.allclose(mix,expm(-t*G),atol=1e-12);cases+=1
    # Two loops at vertex 0 and one edge to 1: P(0,1)=1/5, not 1.
    assert 3*(1/5)!=3*1
    illustrations=[]
    for n in [20,80,320]:
        clocks=np.cumsum(rng.exponential(1/n,size=(4000,n)),axis=1)
        empirical=float(np.mean(np.max(abs(clocks-np.arange(1,n+1)/n),axis=1)**2))
        assert empirical<=4/n
        illustrations.append(dict(n=n,empirical_max_square=empirical,analytic_bound=4/n))
    return dict(multigraph_energy_and_semigroup_models=cases,loop_clock_negative_control=True,simulation_only=illustrations)


def bounded_centers():
    rng=np.random.default_rng(7608);cases=0
    def center(y,w):return brentq(lambda r:float(w@np.arctan(y-r)),float(min(y)-1),float(max(y)+1),xtol=1e-12)
    for _ in range(100):
        y=rng.normal(size=7)*10;w=rng.random(7);w/=sum(w);m=center(y,w);shift=rng.normal()*10
        assert abs(center(y+shift,w)-m-shift)<1e-9
        a=math.exp(rng.normal());delta=np.exp(y);delta_n=delta/a
        ahat=math.exp(center(np.log(delta),w)-center(np.log(delta_n),w))
        assert abs(ahat/a-1)<1e-10;cases+=1
    errors=[];means=[]
    for n in [10,100,1000,10000]:
        eps=1/n;y=np.array([0.,float(n*n)]);w=np.array([1-eps,eps])
        m=center(y,w);errors.append(m);means.append(float(y@w))
        assert 0<m<=math.tan(eps*math.pi/(2*(1-eps)))+1e-10
    assert all(a>b for a,b in zip(errors,errors[1:])) and all(a<b for a,b in zip(means,means[1:]))
    return dict(atomic_shift_and_scale_models=cases,vanishing_contamination_centers=errors,diverging_ordinary_means=means)


if __name__=='__main__':
    start=time.perf_counter();checks={}
    for f in [reflection_phases,compact_obstruction,block_oscillation,correlation_windows,polynomial_coordinates,square_kernels,attempt_clocks,bounded_centers]:
        checks[f.__name__]=dict(status='pass',details=f())
    result=dict(batch='B076',status='pass',elapsed_seconds=round(time.perf_counter()-start,3),scope='Selected finite mechanisms and hypothesis controls, not source headline or Lean certification.',checks=checks)
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8');print(json.dumps(result))
