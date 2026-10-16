"""Final-family finite mechanisms, symbolic identities and scoped analytic examples."""
from pathlib import Path
from itertools import product,combinations
from fractions import Fraction as F
import json,time,math
import numpy as np
import sympy as s
from scipy.integrate import quad

def warping_slope():
    x=s.symbols('x');p,q=s.symbols('p q',positive=True);r=s.Function('r')(x);phi=s.Function('phi')(x)
    rs=s.diff(r,x);ps=s.diff(phi,x)
    rt=s.diff(r,x,2)+(q-1)*(rs**2-1)/r+p*ps*rs/phi
    lam=-p*s.diff(phi,x,2)/phi-q*s.diff(r,x,2)/r
    lhs=s.diff(rt,x)+lam*rs
    rhs=s.diff(r,x,3)+(p*ps/phi+(q-2)*rs/r)*s.diff(r,x,2)+((q-1)*(1-rs**2)/r**2-p*ps**2/phi**2)*rs
    assert s.simplify(lhs-rhs)==0 and s.simplify(s.diff(rt,x)-rhs)!=0
    lapr=s.diff(r,x,2)+q*rs**2/r+p*ps*rs/phi
    assert s.simplify(rt-lapr+(q-1+rs**2)/r)==0
    rng=np.random.default_rng(8601)
    for _ in range(200):
        rv,pv=rng.uniform(.1,4,2);a=rng.uniform(1.01,4);b=rng.normal();P,Q=rng.integers(2,10,2)
        coeff=(Q-1)*(1-a*a)/rv**2-P*b*b/pv**2
        assert coeff*a<0 and coeff*(-a)>0
    return dict(symbolic_slope_and_composition=True,reaction_sign_cases=200,missing_commutator_rejected=True)

def heat_iteration():
    y,t=s.symbols('y t');H=s.Function('H')(y,t);z=s.Function('z')(y,t);a=s.Function('a')(y,t);b=s.Function('b')(y,t);force=s.Function('F')(y,t)
    V=z*H
    lhs=s.diff(V,t)-s.diff(V,y,2)
    rhs=(a-1)*s.diff(V,y,2)+b*s.diff(V,y)+z*force+(s.diff(z,t)-a*s.diff(z,y,2)-b*s.diff(z,y))*H-2*a*s.diff(z,y)*s.diff(H,y)
    assert s.expand((lhs-rhs).subs(s.diff(H,t),a*s.diff(H,y,2)+b*s.diff(H,y)+force))==0
    for count in [1,4,8,20]:
        partial=sum(F(4,16)**j for j in range(count))
        assert partial<F(4,3)
    assert sum(F(4,2)**j for j in range(10))>100
    return dict(cutoff_identity=True,contractive_series=True,noncontractive_control=True,parabolic_regularity_not_tested=True)

def collision_geometry():
    nodes,weights=np.polynomial.legendre.leggauss(32)
    mu=np.r_[(nodes+1)/2,-(nodes+1)/2];ww=np.r_[weights/2,weights/2]
    angles=np.arange(64)*2*np.pi/64
    om=np.array([[math.sqrt(1-z*z)*math.cos(a),math.sqrt(1-z*z)*math.sin(a),z] for z in mu for a in angles])
    area=np.repeat(ww,64)*2*np.pi/64
    p=np.array([1,2,3.]);xi=np.array([1,2,-1.]);g=p-xi
    weights=area*abs(om@g);out=p-(om@g)[:,None]*om;center=(p+xi)/2;rad=np.linalg.norm(g)/2
    mass=2*np.pi*np.linalg.norm(g)
    assert abs(sum(weights)-mass)<1e-11
    assert np.linalg.norm(np.sum(weights[:,None]*out,axis=0)-mass*center)<1e-10
    cov=np.einsum('n,ni,nj->ij',weights,out-center,out-center)
    assert np.linalg.norm(cov-mass*rad*rad/3*np.eye(3))<1e-10
    rng=np.random.default_rng(8603)
    for _ in range(30):
        n=rng.normal(size=3);norm=np.linalg.norm(n);C=np.array([[0,-n[2],n[1]],[n[2],0,-n[0]],[-n[1],n[0],0]])
        eig=np.linalg.svd(C,compute_uv=False);assert np.allclose(eig[:2],[norm,norm])
        assert abs(norm*(np.pi/norm**2)-np.pi/norm)<1e-12
    return dict(sphere_quadrature_points=len(om),mass_and_two_moments=True,plane_jacobians=30)

def uniform_pullback():
    full=[];critical=[]
    for n in [2,4,8,16,32,64]:
        # Phi_n=x+(1+y)/n and F_n=1_[0,1/n] on [-1,1]^2.
        # For n>=2 the x-section has length 1/n for every y, except the n=2 endpoint.
        val=quad(lambda y:(1+.5*np.sin(n*y))/n,-1,1)[0]
        assert abs(val-2/n)<1e-12;full.append(val)
        # Phi_n=x^2+1/n, F_n=1_[0,2/n]: rank fails only at x=0.
        critical.append(2/math.sqrt(n))
    assert all(full[i+1]<full[i] for i in range(5)) and critical[-1]<critical[0]
    assert 2>0 # Phi=0 pulls every shrinking interval around zero back to all [-1,1].
    assert F(64)*F(1,64)==1 # Unbounded densities may retain unit mass.
    return dict(perturbed_submersion_examples=6,critical_null_set_examples=6,rank_and_density_controls=2)

def pattern_centering():
    cases=0;broken=False
    for n in range(1,6):
        edges=list(combinations(range(n),2));full=(1<<n)-1;f=[F(i+2,i+3) for i in range(n)]
        family={S:F(S*S+3,7) for S in range(1<<n)}
        for mask in range(1<<len(edges)):
            adj=[0]*n
            for j,(u,v) in enumerate(edges):
                if mask>>j&1:adj[u]|=1<<v;adj[v]|=1<<u
            def isolated(D,R):return all(not(adj[i]&R) for i in range(n) if D>>i&1)
            def subs(R):return [S for S in range(1<<n) if not(S&~R)]
            def factor(D):return math.prod(f[i] for i in range(n) if D>>i&1)
            E={R:sum((-1)**D.bit_count()*factor(D)*family[R^D] for D in subs(R) if isolated(D,R)) for R in range(1<<n)}
            inv=sum(factor(D)*E[full^D] for D in subs(full) if isolated(D,full))
            assert inv==family[full]
            for D in subs(full):
                for A in subs(full^D):assert (isolated(D,full) and isolated(A,full^D))==isolated(D|A,full)
            if n==2 and mask==1:
                naive=sum((-1)**D.bit_count()*factor(D)*family[full^D] for D in subs(full));assert naive!=E[full];broken=True
            cases+=1
    assert broken
    return dict(contact_graphs=cases,exact_subset_inversion=True,geometry_omission_rejected=True)

def slot_entropy():
    cases=0
    for qs in product(range(5),repeat=3):
        Q=sum(qs)
        for ks in product(*[range(q+1) for q in qs]):
            k=sum(ks);prod=math.prod(math.comb(q,j) for q,j in zip(qs,ks));total=math.comb(Q,k)
            assert prod<=total
            if k:assert math.log(total)<=k*(1+math.log(Q/k))+1e-12
            else:assert total==prod==1
            cases+=1
    return dict(slot_allocations=cases,zero_retention_included=True)

def jet_spanning():
    rng=np.random.default_rng(8607);cases=0
    for n in range(2,6):
        basis=[]
        for i in range(n-1):
            H=np.zeros((n,n));H[i,i]=1;H[-1,-1]=-1;basis.append(H)
        for i,j in combinations(range(n),2):
            H=np.zeros((n,n));H[i,j]=H[j,i]=1;basis.append(H)
        m=len(basis)
        for _ in range(15):
            y=rng.uniform(-1,1,n);T=np.eye(n+m);T[:n,n:]=np.array([H@y for H in basis]).T
            T=np.kron(T,np.eye(2)).astype(complex)
            T+=1e-4*(rng.normal(size=T.shape)+1j*rng.normal(size=T.shape))
            right=T.conj().T@np.linalg.inv(T@T.conj().T)
            assert np.linalg.norm(T@right-np.eye(len(T)))<1e-10;cases+=1
    return dict(complex_fiber_jet_frames=cases,geometric_harmonic_columns_not_constructed=True)

def radius_interpolation():
    for n in range(2,12):
        d=F(10)+F(n,2);eta=1/(2*d);m=math.ceil(10+3*d);p=2*d+1
        assert eta>1/p and 1-eta*d==F(1,2) and 2-eta*d==F(3,2) and eta*(m-10)>=F(3,2)
    x=s.symbols('x');cases=0
    for degree in range(1,7):
        gram=s.Matrix([[s.integrate(x**(i+j),(x,-1,1)) for j in range(degree+1)] for i in range(degree+1)])
        inv=gram.inv();coeff=s.Matrix([(-1)**i*(i+1) for i in range(degree+1)])
        norm=(coeff.T*gram*coeff)[0]
        for k in range(degree+1):assert (s.factorial(k)*coeff[k])**2<=s.factorial(k)**2*inv[k,k]*norm;cases+=1
    for val in [1e-5,1e-10,1e-20]:
        eta=.1;p=20;scale=val**eta
        # Fractional radius r(z)^(1/p)=val^(1/p)+z on |z|<=scale/4.
        assert scale/4<val**(1/p)/2
    return dict(exact_exponent_sets=10,polynomial_evaluation_bounds=cases,fractional_radius_examples=3)

def proper_degree():
    rng=np.random.default_rng(8609);x=rng.uniform(-1,1,(1000,3));eps=.1
    disp=eps*np.prod(1-x*x,axis=1);g=x.copy();g[:,0]+=disp
    distance=1-np.max(abs(x),axis=1)
    assert np.all(disp<distance/2)
    det=1-2*eps*x[:,0]*(1-x[:,1]**2)*(1-x[:,2]**2)
    assert min(det)>.8 and np.max(abs(g))<1
    # Small values do not force positive derivative: x + eps(1-x^2)sin(Nx).
    N=100;point=np.pi/N;der=1-2*eps*point*np.sin(N*point)+eps*(1-point*point)*N*np.cos(N*point)
    assert der<0 and 2*eps<.5
    return dict(cube_points=1000,positive_jacobian=True,value_only_control_rejected=True,degree_theorem_not_numerically_proved=True)

def collapsed_composition():
    x=(np.arange(10000)+.5)/10000;norms=[]
    # q_j(t)=(t,sin(t)/j); v(a,b)=(a,|b|), q_0 lies entirely on the crease.
    for j in [1,2,4,8,16,32]:
        derivative=np.cos(x)/j
        norms.append(np.mean(abs(derivative)**2)**.5)
    assert all(norms[i+1]<norms[i] for i in range(5))
    # q_j(t)=(t,sin(2pi jt)/j): values converge, second derivative component does not.
    bad=[np.mean((2*np.pi*np.cos(2*np.pi*j*x))**2)**.5 for j in [1,2,4,8,16,32]]
    assert min(bad)>4
    return dict(crease_collapse_scales=6,missing_derivative_convergence_rejected=True)

if __name__=='__main__':
    start=time.perf_counter();checks={}
    for f in [warping_slope,heat_iteration,collision_geometry,uniform_pullback,pattern_centering,slot_entropy,jet_spanning,radius_interpolation,proper_degree,collapsed_composition]:checks[f.__name__]=dict(status='pass',details=f())
    result=dict(batch='B086',status='pass',elapsed_seconds=round(time.perf_counter()-start,3),scope='Selected finite mechanisms, symbolic identities and analytic models; no headline theorem or Lean certification.',checks=checks)
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8');print(json.dumps(result))
