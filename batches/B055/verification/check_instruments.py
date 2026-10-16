"""Selected B055 finite checks; no source headline theorem certification."""
from fractions import Fraction as F
from itertools import product
from math import ceil, comb, log, sqrt, pi
from pathlib import Path
import json
import time

import numpy as np
import sympy as sp
from scipy.integrate import quad, quad_vec
from scipy.linalg import solve_sylvester
from scipy.special import beta as beta_function, roots_genlaguerre, gamma, roots_hermitenorm

RNG=np.random.default_rng(550)


def power(A,p):
    vals,U=np.linalg.eigh(A)
    assert min(vals)>0
    return (U*vals**p)@U.conj().T


def fixed_channels():
    cases=0
    for rows,cols,rank in [(3,4,2),(5,3,2),(4,5,3)]:
        U=np.linalg.qr(RNG.normal(size=(rows,rank)))[0]
        V=np.linalg.qr(RNG.normal(size=(cols,rank)))[0]
        rates=np.arange(1,rank+1)*.2
        for x in [-2.,-.5,0.,.7,2.]:
            E=U@np.diag(np.exp(rates*x))
            Ep=U@np.diag(rates*np.exp(rates*x))
            P=E@np.linalg.inv(E.T@E)@E.T
            Pd=(np.eye(rows)-P)@Ep@np.linalg.inv(E.T@E)@E.T
            Pd=Pd+Pd.T
            assert np.linalg.norm(P-U@U.T)<1e-12
            assert np.linalg.norm(Pd)<1e-12
            G=E@V.T
            assert np.linalg.norm(G@(np.eye(cols)-V@V.T))<1e-12
            cases+=1
    x=sp.symbols('x',real=True)
    for r in [sp.Rational(1),sp.Rational(2),sp.Rational(3,2)]:
        alpha=sp.Rational(3,2); shift=sp.Rational(1,3)
        b=-alpha*sp.tanh(r*alpha*(x-shift))
        D=alpha**(1/r)*sp.cosh(r*alpha*(x-shift))**(-1/r)
        assert sp.simplify(sp.diff(b,x)-r*(b*b-alpha*alpha))==0
        assert sp.simplify(sp.diff(D,x)/D-b)==0
        assert sp.simplify(sp.diff(D,x,2)/D-(alpha**2-(r+1)*(alpha**2-b*b)))==0
    # Constant rank is not sufficient for a fixed range.
    E=np.array([[1.],[0.]])
    Ep=np.array([[0.],[1.]])
    Pd=Ep@E.T+E@Ep.T
    assert np.linalg.norm(Pd)>1
    return dict(rectangular_curves=cases, symbolic_riccati_profiles=3, rotating_range_control=True)


def trace_defects():
    squares=0; riccati=[]; scalar=[]
    for n in [2,3,5]:
        for _ in range(8):
            A=RNG.normal(size=(n,n))+1j*RNG.normal(size=(n,n))
            R=A.conj().T@A+np.eye(n)
            A=RNG.normal(size=(n,n))+1j*RNG.normal(size=(n,n))
            D=A.conj().T@A+np.eye(n)
            t=.7
            C=power(t*np.eye(n)+D,.5)
            M=power(R,-.5)-power(R,.5)@C
            square=np.linalg.norm(M,'fro')**2
            trace=np.trace(np.linalg.inv(R)+R@(t*np.eye(n)+D)-2*C).real
            assert abs(square-trace)<2e-10
            assert np.linalg.norm(R@D-D@R)>1e-3
            Req=power(t*np.eye(n)+D,-.5)
            assert np.linalg.norm(power(Req,-.5)-power(Req,.5)@C)<1e-12
            squares+=1
    for n in [2,3]:
        A=RNG.normal(size=(n,n)); B=(A+A.T)/2
        A=RNG.normal(size=(n,n)); V=A.T@A+.7*np.eye(n)
        for t in [.2,1.,4.]:
            def integrand(s):
                Y=s*np.eye(n)-B
                return np.linalg.inv(Y@Y+V+t*np.eye(n))/pi
            R,error=quad_vec(integrand,-np.inf,np.inf,epsabs=2e-11,epsrel=2e-11)
            L=np.linalg.inv(R)
            Z=solve_sylvester(L,L,-1j*(B@L-L@B))
            residual=np.linalg.norm(L@L+Z@Z+1j*(B@Z-Z@B)-V-t*np.eye(n))
            assert residual<1e-8 and np.linalg.norm(Z-Z.conj().T)<1e-10
            assert abs(np.trace(R@(V+t*np.eye(n)))-np.trace(L)+np.trace(R@Z@Z))<1e-9
            riccati.append(float(residual))
    for sigma in [.25,.5,.75]:
        beta=sigma-.5
        c=2*sigma/beta_function(sigma+.5,1-sigma)
        for d in [.3,1.,2.]:
            normal=quad(lambda t:t**beta*d/(sqrt(t)*sqrt(t+d)*(sqrt(t)+sqrt(t+d))),0,np.inf,epsabs=2e-9,epsrel=2e-9)[0]
            f0=quad(lambda t:t**beta*d*d/(sqrt(t)*(sqrt(t)+sqrt(t+d))**2),0,np.inf,epsabs=2e-9,epsrel=2e-9)[0]
            assert abs(c*normal-d**sigma)<2e-7
            assert abs(c*f0-d**(1+sigma)/(1+sigma))<2e-7
            scalar.append((sigma,d))
    return dict(noncommuting_squares=squares, resolvent_riccati_models=len(riccati), max_riccati_residual=max(riccati), scalar_normalization_and_duality=len(scalar))


def conjugation_kernel():
    comparisons=0; errors=[]
    nodes,weights=np.polynomial.legendre.leggauss(64)
    taus=(nodes+1)/2; weights=weights/2
    for sigma in [.2,.5,.8]:
        vs,vweights=roots_genlaguerre(96,-sigma)
        vweights=vweights/gamma(1-sigma)
        for a in [.7,2.]:
            z=np.array([-1.2,0.,0.,.8,1.4])
            diffs=z[:,None]-z[None,:]
            K=sum(w*(1+tau*(1-tau)*diffs**2/a)**(sigma-1) for tau,w in zip(taus,weights))
            mixed=sum(w*np.tensordot(vweights,np.exp(-vs[:,None,None]*tau*(1-tau)*diffs[None,:,:]**2/a),axes=1) for tau,w in zip(taus,weights))
            err=np.max(abs(K-mixed)); errors.append(float(err))
            assert err<2e-10 and min(np.linalg.eigvalsh(K))>-1e-12
            assert np.max(abs(np.diag(K)-1))<1e-12
            X=RNG.normal(size=(5,5))+1j*RNG.normal(size=(5,5)); X=X.conj().T@X
            Y=RNG.normal(size=(5,5))+1j*RNG.normal(size=(5,5)); Y=Y+Y.conj().T
            assert min(np.linalg.eigvalsh(K*X))>=-1e-11
            assert abs(np.trace(K*X)-np.trace(X))<1e-11
            assert abs(np.trace((K*X)@Y)-np.trace(X@(K*Y)))<1e-10
            comparisons+=1
    return dict(gamma_gaussian_mixture_models=comparisons,max_kernel_error=max(errors), repeated_eigenvalues=True)


def polynomial_filter():
    x=sp.symbols('x')
    cases=integer_checks=0
    for r,m,N in [(1,3,2),(1,6,3),(2,5,8),(2,8,4),(3,9,5),(3,12,16)]:
        ell=ceil(2*sqrt(m*r)*log(m))
        affine=(m+r-2*x)/sp.Integer(m-r)
        numerator=sp.Poly(sp.prod(1-x/sp.Integer(j) for j in range(1,r+1))*sp.chebyshevt(ell,affine),x)
        denom=sp.chebyshevt(ell,sp.Rational(m+r,m-r))
        p=sp.Poly(numerator.as_expr()/denom,x)
        assert p.eval(0)==1 and p.degree()<=r+ell
        for k in range(1,m+1):
            val=p.eval(k)
            if k<=r: assert val==0
            else: assert abs(val)<=sp.Rational(2,m**(3*r))
            integer_checks+=1
        W=sum(abs(c)*N**powers[0] for powers,c in p.terms())
        assert W<=(1+N)**r*(11*(1+N))**ell
        cases+=1
    return dict(exact_polynomial_models=cases,integer_evaluations=integer_checks,includes_interval_larger_than_count=True)


def kron_all(mats):
    out=np.ones((1,1),complex)
    for M in mats: out=np.kron(out,M)
    return out


def pruning():
    cases=deleted=retained=0
    for n in [3,4,5]:
        for model in range(8):
            zero=np.zeros(2**n,complex); zero[0]=1
            original=zero.copy(); pruned=zero.copy(); bound=0.
            for layer in range(4):
                # Product rotations supply a nontrivial evolving state.
                locals=[]
                for i in range(n):
                    theta=float(RNG.uniform(-.3,.3))
                    locals.append(np.array([[np.cos(theta),-np.sin(theta)],[np.sin(theta),np.cos(theta)]]))
                U=kron_all(locals); original=U@original; pruned=U@pruned
                Ps=[]
                for i in range(n):
                    theta=0. if (i+layer)%2 else float(RNG.uniform(-.3,.3))
                    v=np.array([-np.sin(theta),np.cos(theta)])
                    Ps.append(kron_all([np.outer(v,v) if k==i else np.eye(2) for k in range(n)]))
                before=pruned.copy(); keep=[]
                for P in Ps:
                    q=np.linalg.norm(P@before)**2
                    keep.append(q>=n**-6)
                    if q<n**-6:
                        bound+=2*sqrt(q); deleted+=1
                    else: retained+=1
                for P,k in zip(Ps,keep):
                    original=original-2*P@original
                    if k: pruned=pruned-2*P@pruned
                assert np.linalg.norm(original-pruned)<=bound+1e-12
            assert bound<=2*4*n**-2+1e-12
            cases+=1
    assert deleted and retained
    atoms=0
    for n in range(3,9):
        strings=list(product([0,1],repeat=n))
        # Correlated law concentrated near the common all-zero or all-one states.
        probs=np.array([.85 if not any(s) else .05 if all(s) else .1/(2**n-2) for s in strings])
        mean=sum(p*sum(s) for p,s in zip(probs,strings)); radius=2*mean
        ids=[i for i,s in enumerate(strings) if sum(s)<=radius]
        assert sum(probs[i] for i in ids)>=.5
        winner=max(ids,key=lambda i:probs[i]); z=strings[winner]
        count=sum(comb(n,j) for j in range(min(n,int(radius))+1))
        assert probs[winner]>=1/(2*count)
        for s in strings:
            hamming=sum(a!=b for a,b in zip(s,z))
            assert abs(sum(s)-hamming)<=sum(z)
        atoms+=1
    return dict(adaptive_circuits=cases,deleted_gates=deleted,retained_gates=retained,correlated_heavy_atom_models=atoms)


def contact_layout(size, signs):
    points=[]; originals={}; gadgets=[]; contacts={}
    for y in range(size):
        for x in range(size):
            originals[(x,y)]=len(points); points.append(np.array([2*x,2*y,0.]))
    def edge(i,j): return tuple(sorted((i,j)))
    for axis in [0,1]:
        sigma=1 if axis==0 else -1
        for fixed in range(size):
            line=[]
            for pos in range(size-1):
                xy=(pos,fixed) if axis==0 else (fixed,pos)
                end=(pos+1,fixed) if axis==0 else (fixed,pos+1)
                sign=signs[(axis,fixed,pos)]
                L,R=originals[xy],originals[end]
                if sign==0: line.append(None); continue
                h=sqrt(3)/2
                A=len(points); B=A+1
                for along,height in ([(1,0),(1,1)] if sign<0 else [(.5,h),(1.5,h)]):
                    v=points[L].copy(); v[axis]+=along; v[2]=sigma*height; points.append(v)
                g=dict(axis=axis,sigma=sigma,L=L,R=R,A=A,B=B,sign=sign)
                gadgets.append(g); line.append(g)
                pairs=[(L,A),(A,R),(A,B)] if sign<0 else [(L,A),(A,B),(B,R)]
                for i,j in pairs: contacts[edge(i,j)]=0.
                if pos and sign>0 and line[-2] is not None and line[-2]['sign']>0:
                    contacts[edge(line[-2]['B'],A)]=0.
    return np.array(points),originals,gadgets,contacts


def contact_inverse():
    cases=pair_checks=constraint_checks=0
    for size in [2,3,4]:
        for mode in range(5):
            signs={(axis,fixed,pos):(-1 if mode==0 else 1 if mode==1 else int(RNG.integers(-1,2))) for axis in [0,1] for fixed in range(size) for pos in range(size-1)}
            points,originals,gadgets,contacts=contact_layout(size,signs)
            m=len(points); displacement=np.zeros_like(points)
            for key in contacts: contacts[key]=float(RNG.integers(-5,6))/7
            def d(i,j): return contacts[tuple(sorted((i,j)))]
            for i in range(m):
                for j in range(i):
                    dsq=np.sum((points[i]-points[j])**2)
                    if (j,i) in contacts: assert abs(dsq-1)<1e-12
                    else: assert dsq>=2-1e-12
                    pair_checks+=1
            for axis in [0,1]:
                for fixed in range(size):
                    gs=[g for g in gadgets if g['axis']==axis and int(round(points[g['L']][1-axis]/2))==fixed]
                    gs.sort(key=lambda g:points[g['L']][axis])
                    for g in gs:
                        L,R,A,B=[g[k] for k in ['L','R','A','B']]
                        if g['sign']<0:
                            displacement[R,axis]=displacement[L,axis]+d(L,A)+d(A,R)
                            displacement[A,axis]=displacement[L,axis]+d(L,A)
                            displacement[B,axis]=displacement[A,axis]
                            displacement[B,2]=g['sigma']*d(A,B)
                    previous=None
                    for g in gs:
                        L,R,A,B=[g[k] for k in ['L','R','A','B']]
                        if g['sign']<0: previous=None; continue
                        if previous is not None and tuple(sorted((previous['B'],A))) in contacts:
                            displacement[A,axis]=displacement[previous['B'],axis]+d(previous['B'],A)
                        displacement[B,axis]=displacement[A,axis]+d(A,B)
                        displacement[A,2]=(d(L,A)-(displacement[A,axis]-displacement[L,axis])/2)/(g['sigma']*sqrt(3)/2)
                        displacement[B,2]=(d(B,R)-(displacement[R,axis]-displacement[B,axis])/2)/(g['sigma']*sqrt(3)/2)
                        previous=g
            S=max(np.linalg.norm(s) for s in displacement)
            dmax=max([abs(v) for v in contacts.values()]+[0.])
            assert S<=6*m*dmax+1e-12
            scale=max(20*S,10.)
            for (i,j),desired in contacts.items():
                u=points[j]-points[i]; v=displacement[j]-displacement[i]
                assert abs(u@v-desired)<1e-11
                length=np.linalg.norm(scale*u+v)
                remainder=length-scale-desired
                assert -1e-11<=remainder<=4*S*S/scale+1e-10
                constraint_checks+=1
            cases+=1
    return dict(signed_grid_models=cases,all_pair_distance_checks=pair_checks,independent_contact_constraints=constraint_checks,includes_square_cycles_and_extra_contacts=True)


def form_elimination():
    cases=0
    for low,high in [(1,2),(2,3),(4,5)]:
        for _ in range(20):
            A=RNG.normal(size=(low,low)); A=A.T@A
            E=min(np.linalg.eigvalsh(A))
            M=RNG.normal(size=(high,high)); M=M.T@M+np.eye(high)
            alpha=float(RNG.uniform(.2,2.))
            C=E*np.eye(high)+alpha*M
            B=RNG.normal(size=(high,low))*.1
            beta=np.linalg.norm(power(M,-.5)@B,2)
            H=np.block([[A,B.T],[B,C]])
            value=min(np.linalg.eigvalsh(H))
            assert E-beta*beta/alpha-1e-12<=value<=E+1e-12
            cases+=1
    for b in [.01,.03,.1]:
        val=(1-sqrt(1+4*b*b))/2
        assert -b*b<=val<=0
        assert .98<=(-val)/(b*b)<=1.00001
    # Without a complement lower bound the compression can miss an arbitrarily low state.
    assert min(np.linalg.eigvalsh(np.diag([0.,-10.])))<0
    return dict(weighted_block_forms=cases,quadratic_scale_controls=3,missing_gap_control=True)


def odd_approximation():
    nodes,weights=roots_hermitenorm(160); weights=weights/sqrt(2*pi)
    target=np.tanh(nodes+.1*nodes**3)
    kappa=.02
    angle=.5*np.arcsin((1-kappa)*target)
    assert np.max(abs(np.sin(2*angle)-(1-kappa)*target))<1e-14
    nonsymmetric=angle+.1+.03*nodes**2
    sym=(nonsymmetric-nonsymmetric[::-1])/2
    assert np.sum(weights*(sym-angle)**2)<=np.sum(weights*(nonsymmetric-angle)**2)
    # Smooth odd periodic cutoff, sampled and evaluated on the whole period.
    L=7.; M=2048
    grid=np.linspace(-L,L,M,endpoint=False)
    def cutoff(x):
        y=np.abs(x)/L
        result=np.zeros_like(y)
        mask=y<1
        result[mask]=np.exp(-y[mask]**8/(1-y[mask]**8))
        return result
    f=.5*np.arcsin((1-kappa)*np.tanh(grid+.1*grid**3))*cutoff(grid)
    coefficients=[]
    for n in range(1,81):
        coefficients.append(2*np.mean(f*np.sin(n*pi*grid/L)))
    def approx(x):
        return sum(a*np.sin((n+1)*pi*x/L) for n,a in enumerate(coefficients))
    theta=approx(nodes)
    error=np.sqrt(np.sum(weights*(np.sin(2*theta)-target)**2))
    angle_error=np.sqrt(np.sum(weights*(theta-angle)**2))
    assert error<=2*angle_error+kappa+1e-12 and error<.04
    dense=np.linspace(-L,L,4096)
    assert max(abs(approx(dense)))<.9
    for eps in [.001,.01,.1]:
        inner=nodes; changed=nodes+eps*np.sin(nodes)
        outer=lambda x:np.tanh(3*x)
        assert np.sqrt(np.sum(weights*(outer(changed)-outer(inner))**2))<=3*np.sqrt(np.sum(weights*(changed-inner)**2))+1e-12
    return dict(gaussian_quadrature_nodes=160,sine_modes=80,final_L2_error=float(error),angle_error_bound=float(2*angle_error+kappa),outer_first_lipschitz_checks=3)


def rational_certificate():
    R,K,v,b,j,z,L,B=sp.symbols('R K v b j z L B')
    rat=sp.Rational
    A,C,k,T0,g,h=rat(1,13),rat(53,24),rat(19,16),rat(73,48),rat(2331,10000),rat(87,2500)
    x,y,m,n=rat(4663,5000),rat(6853,10000),rat(-1051,400),rat(-1073,500)
    Q=A*v*b+C*v*v+k*K*v-2*k*R*b+T0*R*v
    T=g*R*v+h*j*v; S=z+b*v-2*R*b
    F2=(A*v-2*k*R)*b*b+b*(2*C*v*v+2*k*K*v+(g+2*T0)*R*v+h*j*v)+x*v*v*j+y*v**3+m*K*v*v+n*R*v*v
    rules=[2*R*v,2*v*K+R*j,-R*b,-z-b*v,-j*v+K*b-L]
    W=sum(sp.diff(F2,var)*rule for var,rule in zip([R,K,v,b,j],rules))+(v+R-K)*F2
    assert sp.expand(sp.diff(F2,b)-2*Q-T)==0
    ps=[R*j*(b-7*v)**2,R*B*(b-rat(7,3)*v)**2,K*v*(b-rat(9,2)*v)**2,v*B*(K+R/4-v/7)**2,(v*b-rat(14,5)*v*v-rat(13,4)*K*v+rat(4,3)*R*v)**2]
    coeff=[rat(337,10000),rat(183,2500),rat(411,10000),rat(11461,5000),rat(647,10000)]
    raw=z*z-12*R*v*b*b+6*v**4
    residual=sp.Poly(sp.expand((raw-(z+Q)**2-S*T-W-L*(x*v*v+h*b*v)-sum(c*p for c,p in zip(coeff,ps))).subs(b,B+2*v)),R,K,v,B,j)
    expected={R**2*v**2:rat(223,160000),R**2*v*B:rat(4007,240000),R**2*B**2:rat(1097,120000),R*K*v**2:rat(83,80000),R*K*v*B:rat(3343,24000),R*v**3:rat(16259,23400000),R*v**2*B:rat(30179,5460000),R*v**2*j:rat(26,625),R*v*B**2:rat(107,15000),R*v*B*j:rat(3,2500),R*B**3:rat(121,32500),R*B**2*j:rat(11,10000),K**2*v**2:rat(579,20000),K**2*v*B:rat(207,2500),K*v**3:rat(911,975000),K*v**2*B:rat(349,420000),K*v**2*j:rat(5011,5000),K*v*B**2:rat(133,130000),K*v*B*j:rat(87,2500),v**4:rat(1661507,1521000000),v**3*B:rat(633799,621075000),v**2*B**2:rat(10657,1690000)}
    assert residual==sp.Poly(sum(mon*c for mon,c in expected.items()),R,K,v,B,j)
    assert len(residual.terms())==22 and all(c>0 for c in residual.coeffs())
    coercive=expected[v**4]
    assert coercive-rat(1,1000)==rat(140507,1521000000)>0
    # Sign constraints hold, but the uncorrected expression is negative.
    point={R:1,K:1,v:1,b:2,j:1,z:2,L:1}
    assert (b-2*v).subs(point)==0 and S.subs(point)==0
    assert raw.subs(point)==-38
    return dict(exact_remainder_coefficients=22,weighted_squares=5,coercive_coefficient=str(coercive),margin_over_one_thousandth=str(coercive-rat(1,1000)),negative_pointwise_control=-38,scope='Algebra verified; PDE signs, integrability and boundary conditions remain hypotheses.')


def main():
    start=time.perf_counter(); checks={}
    for fn in [fixed_channels,trace_defects,conjugation_kernel,polynomial_filter,pruning,contact_inverse,form_elimination,odd_approximation,rational_certificate]:
        checks[fn.__name__]=fn()
        print(fn.__name__,'passed',flush=True)
    report=dict(batch='B055',status='passed',elapsed_seconds=round(time.perf_counter()-start,3),checks=checks,scope='Finite algebraic and numerical checks of selected mechanisms, not certification of source headline claims or Lean solutions.')
    Path(__file__).with_name('results.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
