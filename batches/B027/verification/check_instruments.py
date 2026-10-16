"""Selected PDE/kernel/transport mechanisms, not global theorem certification."""
from fractions import Fraction as F
from itertools import product, permutations
from pathlib import Path
import json
import numpy as np
import sympy as S
from scipy.integrate import quad

rng=np.random.default_rng(27016)

def compact_projection():
    # e=(1,0) on the unit disk, zero outside; its potential is x/2
    # inside and x/(2|x|^2) outside. A is the unit circle.
    x,y=S.symbols('x y',real=True);r2=x*x+y*y
    phi=x/(2*r2);g=S.Matrix([S.diff(phi,x),S.diff(phi,y)])
    assert S.simplify(S.diff(g[0],x)+S.diff(g[1],y))==0
    assert S.simplify(g.dot(g)-1/(4*r2*r2))==0
    t=S.symbols('t',real=True)
    normal=S.Matrix([S.cos(t),S.sin(t)])
    outer=(-g).subs({x:S.cos(t),y:S.sin(t)}, simultaneous=True)
    assert S.trigsimp(outer.dot(normal)-S.cos(t)/2)==0
    # Exact inside/outside energies and orthogonality.
    ep=S.pi/4+S.integrate(S.pi/(2*S.Symbol('r',positive=True)**3),(S.Symbol('r',positive=True),1,S.oo))
    assert ep==S.pi/2 and S.pi-2*ep==0
    modes=0
    for n in range(1,13):
        for a,b,R in [(2,3,1),(1,-2,2),(-3,1,3)]:
            energy=S.pi*n*(a*a+b*b)*S.Rational(1,R)**(2*n)
            radial=S.integrate(2*S.pi*n*n*(a*a+b*b)*S.Symbol('r',positive=True)**(-2*n-1),(S.Symbol('r',positive=True),R,S.oo))
            assert S.simplify(energy-radial)==0;modes+=1
    return dict(exterior_modes=modes,unit_disk_projection='exact',scope='One discontinuous-field model and exterior harmonic modes; not the general projection existence proof.')

def harmonic_interaction():
    x,y=S.symbols('x y',real=True)
    # Interaction between disjoint unit-disk projected fields, centers (x,y),(4,1).
    potential=(x-4)/((x-4)**2+(y-1)**2)
    interaction=-S.pi*S.diff(potential,x)/2
    assert S.simplify(S.diff(interaction,x,2)+S.diff(interaction,y,2))==0
    assert S.diff(interaction,x).subs({x:0,y:0})!=0
    # Harmonicity alone does not give constancy: local minimality is essential.
    checks=0
    for c in range(1,21):
        for b in range(-10,11):
            if b:
                sigma=F(-b,c)
                assert 2*b*sigma+c*sigma*sigma<0
            else:
                assert all(c*F(s,7)**2>=0 for s in range(-5,6))
            checks+=1
    return dict(quadratic_minimum_checks=checks,nonminimal_harmonic_control='nonconstant',scope='Exact harmonic example and amplitude-polynomial implication; no absolute minimizer constructed.')

def green_regularization():
    count=0;worst=0.0;mixture=0
    for h in (.001,.01,.1,1.,10.,100.):
        L=1/np.log1p(1/h)
        val=quad(lambda a:h**(1-a)*(h+1)**a,0,1,epsabs=1e-11)[0]
        assert abs(L-val)<1e-10;mixture+=1
    for n in range(3,14):
        for repeat in range(5):
            z=.85*np.sqrt(rng.random(n))*np.exp(2j*np.pi*rng.random(n))
            h=np.abs(z[:,None]-z[None,:])**2/((1-abs(z)**2)[:,None]*(1-abs(z)**2)[None,:])
            L=np.zeros_like(h);mask=h>0;L[mask]=1/np.log1p(1/h[mask])
            f=h+.5-L
            ev=np.linalg.eigvalsh(f);worst=min(worst,float(ev[0]));assert ev[0]>-2e-11
            assert np.min(f)>-2e-11 and np.max(f)<.500000001
            previous=np.zeros_like(h)
            for eps in (1.,.3,.01,.0001):
                recip=4*np.pi*(L+eps*f);C=1/recip
                assert np.linalg.eigvalsh(recip)[-2]<2e-9
                assert np.all(C>=previous-1e-10)
                assert np.allclose(np.diag(C),1/(2*np.pi*eps));previous=C;count+=1
    return dict(regularized_matrices=count,logarithmic_mean_integrals=mixture,minimum_psd_eigenvalue=worst,scope='Numerical finite matrices; not all disk configurations or the continuum resolvent limit.')

def reciprocal_updates():
    updates=bordered=0;maxerror=0.
    for n in range(3,13):
        for rep in range(5):
            V=rng.normal(size=(n,3));V[-1]=0;V*=.45/max(np.linalg.norm(V,axis=1))
            U=V@V.T;a=1.;H=a-U;b=.5+rng.random(n);b[-1]=a;M=b[:,None]*b[None,:]/H
            for j in range(3):
                z=int(rng.integers(n));c=float(rng.uniform(0,2));col=M[:,z];aa=M[z,z]
                HH=col[:,None]*col[None,:]/M;UU=aa-HH
                assert np.linalg.eigvalsh(UU)[0]>-1e-10
                exact=aa/(1+c*aa)-HH/(1+c*HH)
                partial=np.zeros_like(UU)
                for k in range(45):partial+=c**k*UU**(k+1)/(1+c*aa)**(k+2)
                error=np.max(abs(exact-partial));maxerror=max(maxerror,float(error));assert error<1e-10
                M=M+c*col[:,None]*col[None,:]
                assert np.linalg.eigvalsh(1/M)[-2]<1e-9;updates+=1
            pts=rng.normal(size=(n,4));D=np.sum((pts[:,None,:]-pts[None,:,:])**2,axis=2)
            K=.2+rng.random(n);B=D/(K[:,None]*K[None,:]);ell=1/K
            block=np.block([[B,ell[:,None]],[ell[None,:],np.zeros((1,1))]])
            assert np.linalg.eigvalsh(block)[-2]<1e-9
            gram=(D[:,0,None]+D[None,0,:]-D)/2
            assert np.linalg.eigvalsh(gram)[0]>-1e-9;bordered+=1
    return dict(column_updates=updates,bordered_distance_matrices=bordered,maximum_series_error=maxerror,scope='Finite inertia, Schur series and Hilbert-distance models; no boundary Green-kernel limit.')

def localized_virial():
    r,A,n,N=S.symbols('r A n N',positive=True)
    eta=(1-(r-1)**3)**N;w=-r*S.diff(eta,r)
    assert S.simplify(S.diff(r**(n+A)*eta,r)-r**(n+A-1)*((n+A)*eta-w))==0
    checks=0
    for n0 in range(3,10):
        for rep in range(20):
            xs=rng.normal(size=(5,n0));ys=rng.normal(size=(6,n0))+3
            X=lambda z:z*np.maximum(0,1-np.maximum(0,np.linalg.norm(z,axis=1)-1)**3)[:,None]**8
            xx=X(xs);yy=X(ys);d=xs[:,None,:]-ys[None,:,:];r2=np.sum(d*d,axis=2)
            kernel=r2**((2-n0)/2);grad=-(n0-2)*d*kernel[:,:,None]/r2[:,:,None]
            fg=rng.random((5,1))*rng.random((1,6))
            separate=np.sum(fg*(-np.sum(xx[:,None,:]*grad,axis=2)+np.sum(yy[None,:,:]*grad,axis=2)))
            joined=(n0-2)*np.sum(fg*kernel*np.sum((xx[:,None,:]-yy[None,:,:])*d,axis=2)/r2)
            assert abs(separate-joined)<1e-10;checks+=1
    return dict(weighted_divergence_identity='exact',paired_kernel_sums=checks,scope='Algebra and finite nonsingular kernel sums; not integrability, existence or nonexistence of PDE solutions.')

def interval_comparison():
    nodes,weights=np.polynomial.legendre.leggauss(100);checks=0;worst=0.
    for n in range(3,10):
        for rep in range(25):
            L,M=rng.uniform(.2,3,2);d0=rng.uniform(-3,3);lam=rng.uniform(.7,3)
            s=d0+L*nodes/2;ss=M*nodes/2;h=s[:,None]-ss[None,:];w=L*M*weights[:,None]*weights[None,:]/4
            K=lambda h:(lam*lam+h*h)**((2-n)/2)
            kval=K(h);ki=(K(d0-L/2-ss)+K(d0+L/2-ss))/2
            kj=(K(s+M/2)+K(s-M/2))/2
            lhs=np.sum(w*(2*kval-ki[None,:]-kj[:,None]))
            rhs=(n-2)*np.sum(w*(h*h-d0*h)/(lam*lam+h*h)*kval)
            err=abs(lhs-rhs);worst=max(worst,float(err));assert err<1e-9
            assert d0*np.sum(w*h/(lam*lam+h*h)*kval)>-1e-10
            ci,cj=rng.uniform(0,3,2)
            bound=ci*ki[None,:]+cj*kj[:,None]+((n-2)*min(ci,cj)*h*h/(lam*lam+h*h)+abs(ci-cj))*kval
            assert np.sum(w*((ci+cj)*kval-bound))<1e-9;checks+=1
    return dict(interval_pairs=checks,maximum_midpoint_identity_error=worst,scope='Bounded separated intervals by quadrature; unbounded zero-weight cases follow the written nonnegative argument.')

def splitting_obstruction():
    count=0
    for n in range(1,7):
        weights=[F(i+1,n*(n+1)//2) for i in range(n)]
        for choice in product(range(4),repeat=n):
            for j in range(4):
                selected=sum((weights[i] for i in range(n) if choice[i]==j),F(0))
                if selected:
                    assert selected/3>selected/6
                    break
            else:raise AssertionError('No selected branch')
            count+=1
    # Component totals can fit while selected subsets cannot.
    assert 2*F(1,4)/3==F(1,6)
    assert 2*F(1,4)/6<F(1,6)
    return dict(deterministic_branch_assignments=count,component_total_control='insufficient',scope='Exact finite copies of the mass obstruction; no Coulomb dual support certificate checked.')

def cell_mass_approximation():
    count=osc=0
    for rep in range(40):
        n=5;q={t:0 for t in permutations(range(n),3)}
        for triple in list(q):
            if tuple(sorted(triple))!=triple:continue
            w=int(rng.integers(1,20))
            for t in permutations(triple):q[t]=w
        total=sum(q.values());q={t:F(v,total) for t,v in q.items()}
        marginal=[[sum((v for t,v in q.items() if t[a]==i),F(0)) for i in range(n)] for a in range(3)]
        assert marginal[0]==marginal[1]==marginal[2]
        # Source density m_i on an interval of length one, piece length q/m_i;
        # map affinely to whole target interval. Its pushed mass is q.
        for i in range(n):
            assert sum((v/marginal[0][i] for t,v in q.items() if t[0]==i),F(0))==1
        for a in (1,2):
            for j in range(n):
                density=sum((v for t,v in q.items() if t[a]==j),F(0))
                assert density==marginal[0][j]
        count+=1
        delta=.4;eta=9.6
        for t in q:
            points1=np.array(t)*10+delta*rng.random(3);points2=np.array(t)*10+delta*rng.random(3)
            cost=lambda x:sum(1/abs(x[i]-x[j]) for i in range(3) for j in range(i+1,3))
            assert abs(cost(points1)-cost(points2))<=6*delta/eta**2;osc+=1
    return dict(exact_cell_mass_models=count,coulomb_oscillation_checks=osc,scope='Exact block marginals and separated-cost samples; interval models are not three-dimensional density constructions or an attainment proof.')

if __name__=='__main__':
    groups={}
    for fn in (compact_projection,harmonic_interaction,green_regularization,reciprocal_updates,localized_virial,interval_comparison,splitting_obstruction,cell_mass_approximation):
        groups[fn.__name__]=fn();print(fn.__name__,'passed',flush=True)
    result=dict(batch='B027',status='passed',check_groups=groups,limitations='Selected finite mechanisms only. No global regularity, hot-spots, nonexistence or Coulomb counterexample proof is certified; no Lean build.')
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
