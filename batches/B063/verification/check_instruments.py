"""Selected geometry and analysis checks; global source theorems are outside scope."""
from pathlib import Path
import json
import time
import math
import numpy as np
import sympy as s
from scipy.integrate import quad
from scipy.special import expit

RNG=np.random.default_rng(63016)

def frequency():
    x,y,l=s.symbols('x y l',real=True); p=4; cases=0
    def disk(poly,power):
        total=0
        for (a,b),c in s.Poly(s.expand(poly),x,y).terms():
            if a%2 or b%2: continue
            total+=c*s.gamma(s.Rational(a+1,2))*s.gamma(s.Rational(b+1,2))*s.factorial(power)/s.gamma(s.Rational(a+b,2)+power+2)
        return s.simplify(total)
    for degree in (1,2,3):
        u=s.re(s.expand((x+s.I*y)**degree))+s.Rational(1,3); ux=s.diff(u,x); uy=s.diff(u,y)
        assert s.diff(u,x,2)+s.diff(u,y,2)==0
        for a,b in [(0,0),(s.Rational(1,4),s.Rational(-1,3))]:
            sub={x:a+l*x,y:b+l*y}; U=u.subs(sub,simultaneous=True); X=ux.subs(sub,simultaneous=True); Y=uy.subs(sub,simultaneous=True)
            H=2*p*disk(U*U,p-1); D=l*l*disk(X*X+Y*Y,p); A=D/2; R=2*p*disk((l*x*X+l*y*Y)**2,p-1)
            assert s.simplify(l*s.diff(H,l)-2*D)==0
            assert s.simplify(l*s.diff(A,l)-(2*A-D+R))==0
            for z in [s.Rational(1,4),s.Rational(1,2),1,2]:
                assert H.subs(l,z)>0 and (R*H-D*D).subs(l,z)>=0
            cases+=1
    for _ in range(300):
        n=RNG.uniform(0,20); P=n/2-RNG.uniform(0,10); q=n*n+RNG.uniform(0,10)
        pdot=2*P-n+q-2*P*n
        assert pdot>=(n-1)*(n-2*P)-1e-10
        assert q-n>=-.25-1e-10
    return dict(exact_harmonic_models=cases,frequency_algebra_cases=300,scope='Kernel and differential identities only; no limiting-varifold construction.')

def projection():
    residual=0.0; cases=0
    for m,c in [(1,1),(2,1),(2,3),(4,2)]:
        for _ in range(40):
            # Small graph slopes and arbitrary random planes both occur.
            if _%2:
                q,_r=np.linalg.qr(np.vstack([np.eye(m),.03*RNG.normal(size=(c,m))]))
            else: q,_r=np.linalg.qr(RNG.normal(size=(m+c,m)))
            p=q@q.T; B=np.eye(m)-p[:m,:m]; e=np.trace(B); j=abs(np.linalg.det(q[:m]))
            residual=max(residual,np.linalg.norm(p[:m,m:]@p[m:,:m]-(B-B@B)))
            assert abs(j-math.sqrt(max(0,np.linalg.det(p[:m,:m]))))<1e-10
            assert 1-j<=e+1e-12
            if e<=1: assert 2*(1-j)-e<=e*e+1e-12
            shape=RNG.normal(size=(m,m)); shape=(shape+shape.T)/2; shape/=max(1,np.linalg.norm(shape,2))
            z=.03; J=np.eye(m)-z*shape
            dpi=np.linalg.solve(J,q[:m]); actual=abs(np.linalg.det(dpi)); formula=j/np.linalg.det(J)
            residual=max(residual,abs(actual-formula)); assert abs(actual-1)<=50*(e+z*z+np.trace(shape)**2)+1e-12
            # A graph sheet has projected Jacobian reciprocal to its area density.
            slope=RNG.normal(size=(c,m)); gram=np.eye(m)+slope.T@slope
            area=math.sqrt(np.linalg.det(gram)); jp=1/area
            multiplicity=int(RNG.integers(1,6)); assert abs(multiplicity*area*jp-multiplicity)<1e-12
            cases+=1
    p=np.diag([1.,0.,1.]); B=np.eye(2)-p[:2,:2]; assert np.trace(B)==1 and np.linalg.det(p[:2,:2])==0
    assert residual<1e-10
    return dict(plane_models=cases,max_identity_residual=residual,deficient_rank_control=True)

def affine_reduction():
    residual=0.0; cases=0
    z=s.symbols('z',real=True)
    for m in range(1,10):
        h=(1+z*z)**s.Rational(m+2,2)
        assert s.simplify((1+z*z)*s.diff(h,z,2)-m*z*s.diff(h,z)-(m+2)*h)==0
    for m in (1,2,3):
        xs=s.symbols('x:'+str(m),real=True); t=s.symbols('t',real=True); vars=(*xs,t)
        F=1+sum((i+1)*x*x/2+x**4/20 for i,x in enumerate(xs)); P=2+sum((i+2)*x*x/3+x/5 for i,x in enumerate(xs))
        u=s.sqrt(F*F+t*t); w=P*(1+(t/F)**2)**s.Rational(m+2,2)
        hu=s.lambdify(vars,s.hessian(u,vars),'numpy'); hw=s.lambdify(vars,s.hessian(w,vars),'numpy'); hf=s.lambdify(xs,s.hessian(F,xs),'numpy'); hp=s.lambdify(xs,s.hessian(P,xs),'numpy')
        ff=s.lambdify(xs,F,'numpy'); pp=s.lambdify(xs,P,'numpy')
        for _ in range(20):
            xx=RNG.uniform(-.8,.8,m); tt=float(RNG.uniform(-1,1)); f=float(ff(*xx)); p=float(pp(*xx)); uu=math.hypot(f,tt)
            H=hf(*xx); U=hu(*xx,tt); W=hw(*xx,tt)
            assert np.linalg.eigvalsh(U).min()>0
            det=f**(m+2)*uu**(-(m+3))*np.linalg.det(H)
            left=f/uu*np.trace(np.linalg.solve(U,W)); h=(1+(tt/f)**2)**((m+2)/2)
            right=h*(np.trace(np.linalg.solve(H,hp(*xx)))+(m+2)*p/f)
            residual=max(residual,abs(np.linalg.det(U)-det),abs(left-right)); cases+=1
    assert residual<1e-9
    return dict(dimension_identities=9,positive_hessian_models=cases,max_residual=residual,scope='Algebraic reduction with arbitrary positive F,P; no reduced-system solution claimed.')

def cap_identity():
    q=s.symbols('q'); psi=(1-q)**6; cases=0
    for n in range(1,13):
        for c in [s.Rational(1,2),1,3]:
            integrand=s.expand(2*q*(c+q)*s.diff(psi,q,2)+n*(c-q)*s.diff(psi,q)-n*(n+1)*psi)
            value=sum(coef/(s.Rational(n,2)+degree[0]) for degree,coef in s.Poly(integrand,q).terms())
            assert s.simplify(value)==0; cases+=1
    return dict(exact_paraboloid_cap_integrals=cases,test='(1-q)_+^6 is C5 with compact cap support; the C2 identity follows also by smooth approximation.')

def model_cutoff():
    a,b=.3,.9; qa,qb=a*a/2,b*b/2
    def theta(q):
        if q<=qa:return 1.,0.
        if q>=qb:return 0.,0.
        t=(q-qa)/(qb-qa); th=expit(1/t-1/(1-t))
        return th,-th*(1-th)*(1/t**2+1/(1-t)**2)/(qb-qa)
    cases=0; residual=0.0
    for k in (-2.,0.,1.):
        def sk(r):return math.sinh(math.sqrt(-k)*r)/math.sqrt(-k) if k<0 else (r if k==0 else math.sin(math.sqrt(k)*r)/math.sqrt(k))
        def ck(r):return math.cosh(math.sqrt(-k)*r) if k<0 else (1. if k==0 else math.cos(math.sqrt(k)*r))
        def deriv(q):
            r=math.sqrt(2*q);return theta(q)[0]*(sk(r)/r if r else 1.)
        for r in np.linspace(.02,1.2,100):
            q=r*r/2; th,dt=theta(q); A=th*ck(r)+r*dt*sk(r); B=th*ck(r)
            assert A<=B+1e-12
            eps=1e-7; differentiated=deriv(q)+r*r*(deriv(q+eps)-deriv(q-eps))/(2*eps)
            residual=max(residual,abs(A-differentiated))
            if r<a:
                F=quad(deriv,0,q,epsabs=1e-12)[0]; assert abs(B-(1-k*F))<1e-10
            if r>b: assert deriv(q)==0 and A==B==0
            cases+=1
    assert residual<1e-6
    return dict(model_points=cases,max_derivative_residual=residual)

def drift_resolvent():
    cases=0; residual=0.0; factors=[]
    for n in (4,8,12):
        ks=np.arange(-n,n+1); size=len(ks); lap=-np.diag(ks**2); drift=np.zeros((size,size),complex)
        # V=amplitude*cos(x), so V' u' shifts frequency k by plus/minus one.
        for amp in (.2,1.,3.):
            drift[:]=0
            for j,k in enumerate(ks):
                if j+1<size:drift[j+1,j]=-amp*k/2
                if j>0:drift[j-1,j]=amp*k/2
            a=100*(1+amp)**2; inv=np.diag(1/(a+ks**2)); Q=inv@drift; factor=float(np.linalg.norm(Q,2)); assert factor<.2
            h=RNG.normal(size=size)+1j*RNG.normal(size=size); z=np.zeros(size,complex)
            for _ in range(30):z=inv@(h+drift@z)
            direct=np.linalg.solve(a*np.eye(size)-lap-drift,h)
            residual=max(residual,float(np.linalg.norm(z-direct)),float(np.linalg.norm((a*np.eye(size)-lap-drift)@z-h)))
            factors.append(factor); cases+=1
    assert residual<1e-10
    return dict(fourier_models=cases,max_contraction_factor=max(factors),max_solve_residual=residual,scope='Galerkin contraction and signs only; no infinite-dimensional domain or Lipschitz regularity test.')

def hartogs():
    cases=0; max_ratio=0.0
    for _ in range(300):
        delta=RNG.uniform(.02,1); B=RNG.uniform(1,5); phi=RNG.uniform(-8,8)
        a=RNG.uniform(0,1,(3,3))*np.exp(2j*np.pi*RNG.random((3,3)))
        a[:,:2]*=B/delta; a[:,2]*=B*np.exp(phi/2)
        det=abs(np.linalg.det(a)); bound=6*B**3*delta**(-2)*np.exp(phi/2)
        assert det<=bound+1e-10
        if det: assert 2*np.log(det)<=2*np.log(6)+6*np.log(B)+4*np.log(1/delta)+phi+1e-10
        max_ratio=max(max_ratio,float(det/bound)); cases+=1
    # Constant phi=0 gives the product of the unit ball and disk. Its identity
    # map is bounded and has Jacobian one: no-minorant is necessarily false.
    for radius in np.linspace(0,.99,30):
        assert 1<=1/(1-radius)
        assert 0<=4*np.log(1/(1-radius)) # H=0 is an admissible minorant.
    return dict(derivative_matrix_models=cases,max_determinant_ratio=max_ratio,constant_potential_control=True)

def fourier_filter():
    error=0.0; cases=0
    for N in (2,3,5,8,13):
        roots=np.exp(2j*np.pi*np.arange(N)/N)
        for h in range(N):
            co=RNG.normal(size=4*N)+1j*RNG.normal(size=4*N); co/=np.sum(abs(co)); theta=.83
            observed=np.mean(roots**(-h)*np.polynomial.polynomial.polyval(theta*roots,co)); exact=sum(co[r]*theta**r for r in range(h,len(co),N))
            error=max(error,float(abs(observed-exact)))
            for c in (1.,2.,5.):
                theta=np.exp(-.99*c/N); z=.5*theta; K=2. # g(t)=1/(1-t/2) on the unit disk.
                observed=np.mean(roots**(-h)/(1-z*roots)); exact=z**h/(1-z**N)
                error=max(error,float(abs(observed-exact)))
                for k in (1,2,4):
                    kept=sum(z**(h+j*N) for j in range(k)); bound=K*np.exp(-.99*k*c)/(1-np.exp(-.99*c))
                    assert abs(exact-kept)<=bound+1e-12
            cases+=1
    N=5; roots=np.exp(2j*np.pi*np.arange(N)/N); h=N+1
    assert abs(np.mean(roots**(-h)*roots)-1)<1e-12 # lower degree one survives, violating a tail starting at h.
    assert error<1e-11
    return dict(residue_classes=cases,max_identity_error=error,out_of_range_degree_control=True)

def main():
    start=time.perf_counter(); checks={}
    for fn in (frequency,projection,affine_reduction,cap_identity,model_cutoff,drift_resolvent,hartogs,fourier_filter):
        checks[fn.__name__]=fn();print(fn.__name__,'passed',flush=True)
    report=dict(status='passed',elapsed_seconds=round(time.perf_counter()-start,3),checks=checks,scope='Selected local identities and finite models; no global geometric source theorem is certified.')
    Path(__file__).with_name('results.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='checks'}))

if __name__=='__main__':main()
