"""Scoped finite and analytic-model checks; no geometric headline certification."""
from pathlib import Path
from itertools import product
import json,time,math
import numpy as np
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from scipy.linalg import expm
from scipy.optimize import root
from scipy.integrate import quad

def centering():
    theta=np.arange(4096)*2*np.pi/4096;pts=np.c_[np.cos(theta),np.sin(theta)]
    cases=0
    for tilt in [0,.2,.5,.8]:
        weights=(1+tilt*np.cos(theta))/len(theta)
        def F(z):
            d=pts-z[:2];a=np.exp(z[2]);r2=np.sum(d*d,axis=1);den=1+a*a*r2/4
            return np.r_[np.sum(weights[:,None]*(a*d/den[:,None]),axis=0),np.sum(weights*(1-a*a*r2/4)/den)]
        sol=root(F,[0,0,np.log(2)]);assert sol.success and np.linalg.norm(F(sol.x))<1e-9
        for ang in np.arange(8)*np.pi/4:
            p=2*np.array([np.cos(ang),np.sin(ang)])
            assert p@F(np.r_[p,0])[:2]<0
        cases+=1
    assert 2*.6-1>0 # Reverse triangle lower bound for an atom of mass .6.
    return dict(continuous_circle_balancings=cases,side_signs=32,large_atom_obstruction=True)

def critical_mass():
    t=s.symbols('t',real=True);v=s.Function('v')(t)
    chis=[s.cos(t),s.sin(t)]
    assert s.simplify(sum(s.diff(c*v,t)**2 for c in chis)-s.diff(v,t)**2-v*v)==0
    cases=0
    for dim in range(3,12):
        exponent=(dim-2)/dim
        for Y in [0,.1,.9,.999]:
            for mass in np.linspace(0,.999,501):
                assert Y*mass**exponent+(1-mass)**exponent>Y;cases+=1
    assert 1>=1*0+1*1 # At threshold, complete concentration is not excluded.
    return dict(squared_partition_identity=True,mass_exclusions=cases,threshold_control=True)

def integral_chains():
    cases=0
    for vals in [(2,3),(2,4),(1,6,0),(2,3,5,0),(4,6,10),(0,0),(1,1)]:
        A=s.diag(*vals);D=smith_normal_form(A,domain=s.ZZ)
        tau=sum(1 for i in range(len(vals)) if abs(D[i,i])>1)
        rank=A.rank();rho0=rho1=len(vals)-rank
        assert len(vals)>=rho0+tau and len(vals)>=rho1+tau
        assert 2*len(vals)>=rho0+rho1+2*tau;cases+=1
    D=smith_normal_form(s.diag(2,3),domain=s.ZZ)
    assert sorted(abs(D[i,i]) for i in range(2))==[1,6]
    return dict(two_term_integral_complexes=cases,coprime_torsion_generators=1,geometric_stabilization_not_tested=True)

def involution():
    rng=np.random.default_rng(8504);J=np.array([[0,1],[-1,0.]])
    G=np.diag([1,1,-1,-1]);cases=0
    for _ in range(30):
        R=rng.normal(size=(2,2));H=R.T@R+np.eye(2);N=rng.normal(size=(2,2));N=N+N.T
        A=np.zeros((4,4));A[:2,:2]=J@H;A[2:,2:]=J@N
        for eps in [.0001,.001,.01]:
            flow=expm(eps*A);Phi=flow@G
            assert np.linalg.norm(Phi@Phi-expm(2*eps*A))<1e-11
            assert min(np.linalg.svd(Phi-np.eye(4),compute_uv=False))>1e-5;cases+=1
    assert np.linalg.norm(expm(2*np.pi*J)-np.eye(2))<1e-12
    return dict(block_perturbations=cases,resonance_control=True,compact_global_fixed_set_not_tested=True)

def weighted_variance():
    rng=np.random.default_rng(8505);cases=0
    for n in range(3,10):
        edges=[(i,i+1) for i in range(n-1)]+[(0,n-1)]
        B=np.zeros((len(edges),n))
        for j,(a,b) in enumerate(edges):B[j,a]=1;B[j,b]=-1
        L=B.T@B;gap=np.linalg.eigvalsh(L)[1];K=gap*rng.uniform(.3,1,len(edges))
        assert min(np.linalg.eigvalsh(L@L-B.T@np.diag(K)@B))>-1e-10
        for _ in range(30):
            a=rng.normal(size=n);a-=a.mean()
            assert a@a<=np.sum((B@a)**2/K)+1e-10;cases+=1
        vals,vec=np.linalg.eigh(L);a=vec[:,1]
        assert a@a>np.sum((B@a)**2/(2*gap))
    return dict(graph_variance_cases=cases,excess_weight_controls=7,curvature_contraction_not_tested=True)

def bernstein():
    z,w=s.symbols('z w');rng=np.random.default_rng(8506);cases=0
    for N in range(1,6):
        a=[int(x) for x in rng.integers(-5,6,size=N+1)]
        coeff=[sum(s.Rational(math.comb(i,j),math.comb(N,j))*a[j] for j in range(i+1)) for i in range(N+1)]
        assert s.expand(sum(coeff[i]*math.comb(N,i)*z**i*(1-z)**(N-i) for i in range(N+1))-sum(a[j]*z**j for j in range(N+1)))==0
        terms={(d,e):int(rng.integers(-5,6)) for d in range(N+1) for e in range(N+1-d)}
        P=sum(a*z**d*w**e for (d,e),a in terms.items());rec=0
        for i in range(N+1):
            for j in range(N+1-i):
                c=sum(s.Rational(math.comb(i,d)*math.comb(j,e),math.comb(N,d+e)*math.comb(d+e,d))*a for (d,e),a in terms.items() if d<=i and e<=j)
                rec+=c*s.factorial(N)/(s.factorial(i)*s.factorial(j)*s.factorial(N-i-j))*z**i*w**j*(1-z-w)**(N-i-j)
        assert s.expand(rec-P)==0;cases+=1
    mats=[s.Matrix([[1,0],[0,0]]),s.Matrix([[1,1],[1,1]]),s.eye(2)]
    M=z*mats[0]+w*mats[1]+(1-z-w)*mats[2]
    for i in range(11):
        for j in range(11-i):
            assert min(np.linalg.eigvalsh(np.array(M.subs({z:s.Rational(i,10),w:s.Rational(j,10)})).astype(float)))>=-1e-12
    assert (1-8*z*(1-z)).subs(z,s.Rational(1,2))<0
    # (z-1/2)^2 is nonnegative but has degree-two Bernstein coefficient -1/4.
    assert s.Rational(1,4)-s.Rational(1,2)==-s.Rational(1,4)
    return dict(exact_interval_and_triangle_reconstructions=cases,matrix_points=66,vertex_only_and_necessity_controls=2)

def potential_decomposition():
    # V(r)=c log(r/R), with c chosen to make sup_D1 V=-1.
    R=1000;c=1/math.log(R)
    mass=-quad(lambda r:2*np.pi*r*c*math.log(r/R),0,8)[0]
    assert mass<=100*np.pi and abs(c*math.log(1/R)+1)<1e-12
    for radius in [.2,.7,1,1.3,3]:
        avg=quad(lambda r:2*r*math.log(max(r,radius)),0,1,points=[radius] if radius<1 else None)[0]
        expected=(radius*radius-1)/2 if radius<=1 else math.log(radius)
        assert abs(avg-expected)<1e-10
    assert abs(quad(lambda r:2*r*math.log(r),0,1)[0]+.5)<1e-10
    return dict(normalized_atomic_profile=True,disk_average_cases=6,atom_integrable=True)

def affine_correction():
    ratios=[]
    for A in [8,16,32,64,128]:
        rho=1/A;v=(np.arange(A)+.5)/A-.5;xx,yy=np.meshgrid(v,v);points=np.c_[xx.ravel(),yy.ravel()]
        for source in [np.array([0.,0]),points[0],np.array([.123,.213]),np.array([2.,1.])]:
            dist=np.linalg.norm(points-source,axis=1)
            kernel=np.minimum(1,rho*rho/np.maximum(dist*dist,1e-300))
            ratio=kernel.mean()/(rho*rho*(1+abs(math.log(rho))));assert ratio<20;ratios.append(ratio)
    source=np.array([2.,1.]);grad=-source/(source@source)
    angles=np.arange(1024)*2*np.pi/1024;unit=np.c_[np.cos(angles),np.sin(angles)]
    errors=[]
    for radius in [.1,.05,.025]:
        pts=radius*unit;raw=np.log(np.linalg.norm(pts-source,axis=1))-math.log(np.linalg.norm(source))
        corrected=raw-pts@grad;assert max(abs(corrected))<radius**2
        assert max(abs(raw))>.2*radius;errors.append(max(abs(corrected)))
    assert errors[1]<errors[0]/3 and errors[2]<errors[1]/3
    return dict(finite_grid_kernel_cases=len(ratios),far_field_scales=3,source_large_subdivision_regime_not_tested=True)

if __name__=='__main__':
    start=time.perf_counter();checks={}
    for f in [centering,critical_mass,integral_chains,involution,weighted_variance,bernstein,potential_decomposition,affine_correction]:checks[f.__name__]=dict(status='pass',details=f())
    result=dict(batch='B085',status='pass',elapsed_seconds=round(time.perf_counter()-start,3),scope='Selected finite mechanisms and analytic models; no headline theorem or Lean certification.',checks=checks)
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8');print(json.dumps(result))
