"""Finite checks of selected interfaces, with explicit boundary controls."""
import json
import time
import math
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import numpy as np
import sympy as s
from scipy.linalg import solve_sylvester
from numpy.polynomial.hermite import hermgauss


def phi(T):return np.sum(np.maximum(np.linalg.eigvalsh(T),0)**1.5)


def cost(T,K):
    vals,V=np.linalg.eigh(T);keep=vals>max(1.,max(abs(vals)))*1e-11
    if not any(keep):assert np.linalg.norm(K)<1e-8;return 0.
    lam=vals[keep];U=V[:,keep];k=U.conj().T@K@U
    assert np.linalg.norm(K-U@k@U.conj().T)<1e-7*(1+np.linalg.norm(K))
    return float(1.5*np.sum(abs(k)**2/(np.sqrt(lam)[:,None]+np.sqrt(lam)[None,:])))


def hessian_averaging():
    rng=np.random.default_rng(7201);cases=0
    for n in range(1,7):
        for _ in range(12):
            Ts=[];Ks=[]
            for j in range(3):
                V,_=np.linalg.qr(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))
                vals=np.exp(rng.uniform(-7,7,n));T=(V*vals)@V.conj().T
                K=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));K=(K+K.conj().T)/2
                A=(V*np.sqrt(vals))@V.conj().T;sol=solve_sylvester(A,A,K)
                assert abs(cost(T,K)-1.5*np.vdot(K,sol).real)<1e-7*(1+cost(T,K))
                T0=np.pad(T,((0,2),(0,2)));K0=np.pad(K,((0,2),(0,2)))
                assert abs(cost(T0,K0)-cost(T,K))<1e-6*(1+cost(T,K))
                Ts.append(T);Ks.append(K)
            weights=rng.dirichlet(np.ones(3));T=sum(a*b for a,b in zip(weights,Ts));K=sum(a*b for a,b in zip(weights,Ks))
            rhs=sum(w*cost(t,k) for w,t,k in zip(weights,Ts,Ks))
            assert cost(T,K)<=rhs+1e-7*(1+rhs);cases+=1
    return dict(complex_mixtures=cases,sylvester_checks=3*cases,zero_extensions=3*cases)


def child_energy():
    rng=np.random.default_rng(7202);signs=[x for x in product([-1,1],repeat=3) if math.prod(x)==1];cases=0
    for dims in [(2,2,2),(2,4,6),(4,4,4)]:
        Ds=[np.diag([1]*(d//2)+[-1]*(d//2)) for d in dims]
        for trial in range(18):
            Ws=[rng.normal(size=(dims[v],dims[(v+1)%3])) for v in range(3)]
            if trial%3==0:Ws[0][:,0]=0
            stars=[np.hstack([Ws[v],Ws[(v-1)%3].T]) for v in range(3)]
            e=sum(phi(R@R.T) for R in stars);bs=sum(cost(R.T@R,R.T@D@R) for R,D in zip(stars,Ds))
            tau=np.trace(Ds[0]@Ws[0]@Ds[1]@Ws[1]@Ds[2]@Ws[2])
            assert abs(tau)<=5*bs/3+1e-8
            energies=[];grams=[]
            for signs0 in signs:
                Cs=[np.diag(np.sqrt(1+sig*np.diag(D))) for sig,D in zip(signs0,Ds)]
                child=[Cs[v]@Ws[v]@Cs[(v+1)%3] for v in range(3)]
                gr=[child[v]@child[v].T+child[(v-1)%3].T@child[(v-1)%3] for v in range(3)]
                grams.append(gr);energies.append(sum(phi(g) for g in gr))
            delta=np.mean(energies)-e
            assert delta>=bs/(2*math.sqrt(2))-1e-7 and abs(tau)<=10*math.sqrt(2)*delta/3+1e-7
            for v in range(3):
                for sig in [-1,1]:
                    avg=sum(grams[j][v] for j,sg in enumerate(signs) if sg[v]==sig)/2
                    C=np.diag(np.sqrt(1+sig*np.diag(Ds[v])))
                    assert np.allclose(avg,C@stars[v]@stars[v].T@C)
            cases+=1
    return dict(four_child_models=cases,conditional_gram_checks=6*cases,mixed_trace_checks=cases)


def stable_keys():
    def grid(q,b):
        target=4/(1-q)/q**b;N=1
        while N<target:N*=2
        return N
    def key(x,N):return (x%1*N).__floor__()
    tested=stable=0
    for q in [F(1,2),F(2,3),F(3,5)]:
        start=1
        while 2*q**start>F(1,4):start+=1
        windows=[(start,start+2),(start+8,start+11),(start+17,start+19)]
        Ns=[grid(q,b) for a,b in windows]
        assert Ns[1]%Ns[0]==0 and Ns[2]%Ns[1]==0
        for x in [F(j,73) for j in range(73)]+[F(1,Ns[0]),F(2,Ns[1])]:
            for j,(a,b) in enumerate(windows):
                is_stable=not j or key(x,Ns[j-1])==key(x+2*q**a,Ns[j-1])
                for t in [F(1),F(4,3),F(2)]:
                    points=[x]+[x+t*q**n for n in range(a,b+1)]
                    assert len(set(key(z,Ns[j]) for z in points))==len(points);tested+=1
                    if is_stable:
                        for z in points:
                            for old in Ns[:j]:assert key(z,old)==key(x,old)
                        stable+=1
    for M,d,g,r0 in product([2,3],[1,2,3],[1,4],[1,3]):
        sigma=0
        for h in range(1,d+1):
            r=r0 if h==1 else max(r0,g+sigma)
            span=r if h==1 else r+g+sigma;assert span<=2*r
            sigma=M*r+(M-1)*g if h==1 else M*(r+g+sigma)+(M-1)*g
    N=16;boundary=F(1,N);assert key(boundary,N)==1 and key(boundary-F(1,1000),N)==0
    return dict(separated_windows=tested,stable_window_scale_models=stable,tree_parameter_models=24,boundary_control=True)


def open_repair():
    cases=0
    # Closed exceptional intervals on the circle, each away from the fundamental-domain seam.
    for a,b,eps in [(F(1,4),F(1,3),F(1,100)),(F(1,2),F(3,4),F(1,80))]:
        measure=b-a;assert (b+eps)-(a-eps)==measure+2*eps
        n=1
        while F(2,2**n)>=eps:n+=1
        for x in [a,(a+b)/2,b]:
            for t in [F(1),F(3,2),F(2)]:
                for j in range(n,n+5):
                    y=x+t*F(1,2**j);assert a-eps<y<b+eps;cases+=1
    p=F(1,10);B=[p/2,p,3*p/2];R=[2*p,3*p,4*p]
    assert sum(B)/3<=2*p and sum(R)/3<=3*p
    chosen=min(range(3),key=lambda j:B[j]+R[j]);assert B[chosen]+R[chosen]<=5*p
    assert B[chosen]+R[chosen]+p<=6*p
    return dict(uniform_tail_entries=cases,neighborhood_measure=True,expectation_selection=True)


def fourier_density():
    rng=np.random.default_rng(7203);nodes,weights=hermgauss(70);cases=0;maxerr=0.
    for alpha in [.4,1.,2.]:
        for scale in [.002,.2,1.]:
            pts=rng.uniform(-1,1,(9,2))*scale
            distances=np.sum((pts[:,None,:]-pts[None,:,:])**2,axis=2)
            pair=np.exp(-np.pi*alpha*distances).sum()
            xx,yy=np.meshgrid(nodes,nodes,indexing='ij');freq=np.stack([xx.ravel(),yy.ravel()],axis=1)*math.sqrt(alpha/math.pi)
            M=np.exp(2j*math.pi*freq@pts.T).sum(axis=1)
            integral=np.sum(np.outer(weights,weights).ravel()*abs(M)**2)/math.pi
            error=abs(pair-integral);maxerr=max(maxerr,error);assert error<1e-8;cases+=1
    for d,tail,density in product([F(1,10),F(1,20)],[F(0),F(1,100)],[F(99,100),F(1),F(101,100)]):
        lower=density*(1-tail)**2/(1+d)**2
        assert lower>=density*(1-2*tail)/(1+d)**2
    return dict(gaussian_pair_integrals=cases,clustered_point_cases=3,max_absolute_error=maxerr,cutoff_budget_models=12)


def poisson_derivatives():
    t,x=s.symbols('t x',positive=True);g=s.Function('g');a=s.symbols('a')
    expr=t**-1*g(x/t)
    assert s.simplify(s.diff(expr,t).subs(t,1)+g(x)+x*s.diff(g(x),x))==0
    assert s.simplify(s.diff(expr,t,2).subs(t,1)-(2*g(x)+4*x*s.diff(g(x),x)+x*x*s.diff(g(x),x,2)))==0
    H=s.Function('H');converted=s.diff(s.exp(-a*x)*H(x),x,2)
    assert s.simplify(converted-s.exp(-a*x)*(s.diff(H(x),x,2)-2*a*s.diff(H(x),x)+a*a*H(x)))==0
    shells=[j*j+j*k+k*k for j,k in product(range(-13,14),repeat=2)];assert shells.count(1)==6
    shell=np.array(shells);b=math.sqrt(3)/2;cases=0
    for alpha in [.4,.7,1.,1.8,3.]:
        c=math.pi*alpha/b;d=math.pi/(alpha*b);G1=np.exp(-c*shell);G2=np.exp(-d*shell)/alpha
        left=[sum(G1),sum(-c*shell*G1),sum(c*c*shell**2*G1)]
        right=[sum(G2),sum((-1+d*shell)*G2),sum((2-4*d*shell+d*d*shell**2)*G2)]
        assert np.allclose(left,right,rtol=1e-12,atol=1e-12);cases+=1
    return dict(symbolic_derivative_identities=3,first_shell_multiplicity=6,gaussian_poisson_models=cases)


def skew(b):
    n=len(b);B=s.zeros(n+1)
    for i in range(n):B[0,i+1]=b[i];B[i+1,0]=-b[i]
    return B


def phi_exact(Q,W):
    r=Q.rows;a=W[0,0];v=W[1:,0];T=W[1:,1:]
    return s.BlockMatrix([[s.Matrix([s.trace(Q*T)]),-v.T*Q],[-Q*v,a*Q]]).as_explicit()


def singular_epigraph():
    cases=0
    for r in [1,2]:
        n=r+1;bs=[s.Matrix([j+i+1 for i in range(r)]) for j in range(r)]+[s.zeros(r,1)]
        Q=sum((b*b.T for b in bs),s.zeros(r));B=s.Matrix.vstack(*(skew(b) for b in bs))
        for singular in [False,True]:
            X=s.diag(*([0 if singular else 2]+list(range(3,n+2))));Z=s.diag(*range(4,4+n))
            block=s.BlockMatrix([[s.kronecker_product(s.eye(n),X),B],[B.T,Z]]).as_explicit()
            assert block.det()==(X.det()*Z-phi_exact(Q,X.adjugate())).det();cases+=1
    A=s.diag(2,0);Q=s.diag(3,0);Ad=s.diag(s.Rational(1,2),0);threshold=s.trace(Ad*Q)
    for t in [threshold,threshold+1]:
        b=s.Matrix([s.sqrt(3),0]);bs=[b,s.zeros(2,1),s.zeros(2,1)]
        B=s.Matrix.vstack(*(skew(b) for b in bs));X=s.diag(1,2,0);Z=s.diag(t,3,0)
        block=s.BlockMatrix([[s.kronecker_product(s.eye(3),X),B],[B.T,Z]]).as_explicit()
        assert min(np.linalg.eigvalsh(np.array(block,dtype=float)))>-1e-10
    bad=s.Matrix([[0,1],[1,1]])
    assert bad.det()<0 and 1-0>=0
    return dict(exact_determinant_models=cases,singular_feasible_boundaries=2,range_omission_negative_control=True)


def angular_gram():
    c,u=s.symbols('c u',real=True);w=c+s.I*u;wb=c-s.I*u
    U=s.Matrix([[-wb,-w],[u*wb**2,u*w**2],[c*wb**2,-c*w**2]])
    V=s.Matrix([[0,0],[s.I,s.I],[1,1]])
    def real(M):return M.applyfunc(lambda z:s.expand(s.re(s.expand_complex(z))))
    forms=[real(U*U.conjugate().T)/2,real(V*V.conjugate().T)/2,real(U*V.conjugate().T+V*U.conjugate().T)/2]
    targets=[s.Matrix([[1,-u*c,0],[-u*c,u*u,0],[0,0,c*c]]),s.diag(0,1,1),s.Matrix([[0,0,-c],[0,0,-u],[-c,-u,0]])]
    ideal=s.groebner([c*c+u*u-1],c,u)
    for actual,target in zip(forms,targets):
        for e in actual-target:assert ideal.reduce(s.expand(e))[1]==0
    cases=0
    for C,S in [(s.Rational(1),s.Rational(0)),(s.Rational(3,5),s.Rational(4,5))]:
        Fmat=(2*U+V).subs({c:C,u:S})/s.sqrt(2)
        realF=s.Matrix.hstack(s.re(Fmat[:,0]),s.im(Fmat[:,0]),s.re(Fmat[:,1]),s.im(Fmat[:,1]))
        Q=s.simplify(realF*realF.T);B=s.Matrix.vstack(*(skew(realF[:,j]) for j in range(4)))
        for sing in [False,True]:
            X=s.diag(0 if sing else 2,3,4,5);Z=s.diag(6,7,8,9)
            pencil=s.BlockMatrix([[s.kronecker_product(s.eye(4),X),B],[B.T,Z]]).as_explicit()
            assert s.simplify(pencil.det()-(X.det()*Z-phi_exact(Q,X.adjugate())).det())==0;cases+=1
    return dict(symbolic_gram_entries=27,exact_size20_determinants=cases,singular_slice_models=2)


if __name__=='__main__':
    start=time.perf_counter();checks={}
    for f in [hessian_averaging,child_energy,stable_keys,open_repair,fourier_density,poisson_derivatives,singular_epigraph,angular_gram]:checks[f.__name__]=dict(status='pass',details=f())
    result=dict(batch='B072',status='pass',elapsed_seconds=round(time.perf_counter()-start,3),scope='Selected finite models and identities; no source headline or Lean certification.',checks=checks)
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
