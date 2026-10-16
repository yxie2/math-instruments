"""Finite mechanism checks; no continuum or source headline certification."""
from collections import defaultdict
from itertools import product, permutations
from pathlib import Path
import json, time, math
import numpy as np
from scipy.linalg import expm, eigh
from scipy.integrate import quad

def conformal_constraints():
    rng=np.random.default_rng(8101)
    for _ in range(60):
        u=rng.uniform(1,2);f=rng.normal(size=3);lap=rng.normal();R=rng.normal()
        K=rng.normal(size=(3,3));K=(K+K.T)/2
        dK=rng.normal(size=(3,3,3));dK=(dK+dK.transpose(0,2,1))/2
        G=np.zeros((3,3,3))
        for l,i,j in product(range(3),repeat=3):G[l,i,j]=2*((l==j)*f[i]+(l==i)*f[j]-(i==j)*f[l])
        Kp=u*u*K;dKp=u*u*(dK+2*f[:,None,None]*K)
        J=np.array([sum(dK[j,i,j] for j in range(3))-np.trace(dK[i]) for i in range(3)])
        Jp=np.array([u**-4*sum(dKp[j,i,j]-sum(G[l,j,i]*Kp[l,j]+G[l,j,j]*Kp[i,l] for l in range(3)) for j in range(3))-u**-2*(np.trace(dK[i])-2*f[i]*np.trace(K)) for i in range(3)])
        assert np.allclose(u*u*Jp,J+4*K@f)
        mu=(R+np.trace(K)**2-np.sum(K*K))/2
        Rp=u**-5*(-8*lap+R*u);mup=(Rp+u**-4*(np.trace(K)**2-np.sum(K*K)))/2
        assert abs(u**4*mup-mu+4*lap/u)<1e-10
        X=rng.normal(size=(2,3));Y=rng.normal(size=3);Y/=max(1,np.linalg.norm(Y))
        def I(X):return np.sum(X*X)+2*np.dot(np.cross(*X),Y)
        i0=I(X);assert i0>=-1e-12
        theta=rng.normal();rot=np.array([[np.cos(theta),-np.sin(theta)],[np.sin(theta),np.cos(theta)]])
        assert abs(I(rot@X)-i0)<1e-10
        ip=u**-8*i0;Dp=mup+Jp@(u**-2*Y)-ip;D=mu+J@Y-i0
        rhs=4/u*(-lap+K@(u*f)@Y)+(1-u**-4)*i0
        assert abs(u**4*Dp-D-rhs)<1e-10
    # A conformally radial sphere, computed from its warped area and radial arclength.
    for r in [.4,1,3]:
        u=1+.2/r;du=-.2/r**2;area=4*np.pi*r*r*u**4
        darea=4*np.pi*(2*r*u**4+4*r*r*u**3*du)
        assert abs(darea/(area*u*u)-u**-2*(2/r+4*du/u))<1e-12
    return dict(pointwise_tensor_cases=60,radial_spheres=3,constant_flux_rotation=True)

def area_envelope():
    rng=np.random.default_rng(8102);cases=0
    for _ in range(25):
        h=rng.normal(size=(3,3));h=(h+h.T)/2
        planes=[np.linalg.qr(rng.normal(size=(3,2)))[0] for j in range(3)]
        L=np.array([np.trace(T.T@h@T)/2 for T in planes]);step=1e-6
        def area(T,s):return np.sqrt(np.linalg.det(T.T@(np.eye(3)+s*h)@T))
        vals=np.array([area(T,step) for T in planes]);assert np.max(abs((vals-1)/step-L))<1e-4
        assert abs((min(vals)-1)/step-min(L))<1e-4
        assert abs((min(area(T,-step) for T in planes)-1)/(-step)-max(L))<1e-4
        # A nonactive candidate with a large slope cannot change the derivative at zero.
        assert abs((min([*vals,2-100*step])-1)/step-min(L))<1e-4;cases+=1
    return dict(tied_active_plane_sets=cases,right_minimum_left_maximum=True)

def retained_freshness():
    groups=defaultdict(list)
    for bits in product([0,1],repeat=4):
        for order in permutations(range(4)):
            history=[]
            # Stop at first one, or after the third query. Numerical retries retain all answers.
            for k in range(3):
                history.append((order[k],bits[order[k]]));groups[tuple(history)].append((bits,order))
                if bits[order[k]]:break
    for hist,states in groups.items():
        seen={i for i,b in hist};unused=sorted(set(range(4))-seen);count=defaultdict(int)
        for bits,order in states:count[(tuple(bits[i] for i in unused),tuple(i for i in order if i in unused))]+=1
        expected=2**len(unused)*math.factorial(len(unused))
        assert len(count)==expected and len(set(count.values()))==1
    # Conditional on a failed observed zero, a reused coordinate is zero with probability one.
    failed=[b for b in product([0,1],repeat=2) if b[0]==0];assert sum(b[0] for b in failed)==0
    return dict(adaptive_histories=len(groups),joint_remaining_bits_and_orders=True,forgotten_failure_control=True)

def spectral_averaging():
    Hc=np.array([[.3,.7],[.7,-.4]]);b=np.array([.6,-.2]);checks=0
    for s in [-2,-.1,1.4]:
        H=np.block([[np.array([[s]]),b[None,:]],[b[:,None],Hc]])
        for z in [-1+.2j,.7+.8j]:
            M=z+b@np.linalg.solve(Hc-z*np.eye(2),b)
            assert M.imag>0 and abs(np.linalg.inv(H-z*np.eye(3))[0,0]-1/(s-M))<1e-12
            val=quad(lambda x:(1/(x-M)).imag,-np.inf,np.inf,epsabs=1e-10)[0]
            assert abs(val-np.pi)<1e-9;checks+=1
    # Uniform density 1/4 on [-2,2]; smooth Poisson spectral tests avoid jump quadrature.
    for E,eta in [(-.5,.3),(.2,.1),(1.5,.4)]:
        def local(s):
            H=np.block([[np.array([[s]]),b[None,:]],[b[:,None],Hc]])
            ev,v=eigh(H)
            return np.sum(v[0]**2*eta/((ev-E)**2+eta**2))/4
        value=quad(local,-2,2,epsabs=1e-10)[0]
        assert value<=np.pi/4+1e-10
    return dict(schur_poisson_pairs=checks,averaged_poisson_bounds=3,scalar_atomic_family_has_continuous_average=True)

def lorentz_frames():
    rng=np.random.default_rng(8105);eta=np.diag([-1.,1,1,1]);Uc=np.array([1.,0,0,0])
    for _ in range(40):
        M=np.eye(4)+.2*rng.normal(size=(4,4));G=M.T@eta@M;U=np.linalg.solve(M,Uc)
        K=G+2*np.outer(G@U,G@U);assert min(np.linalg.eigvalsh(K))>0
        assert abs(np.linalg.det(K)+np.linalg.det(G))<1e-9
        assert np.allclose(K,M.T@M)
        lo,hi=np.linalg.eigvalsh(K)[[0,-1]];sv=np.linalg.svd(M,compute_uv=False)
        assert abs(sv[0]**2-hi)<1e-9 and abs(sv[-1]**2-lo)<1e-9
    r=8;M=np.eye(4);M[:2,:2]=[[np.cosh(r),np.sinh(r)],[np.sinh(r),np.cosh(r)]]
    assert np.allclose(M.T@eta@M,eta,atol=1e-8) and np.linalg.norm(M,2)>2900
    assert np.linalg.norm(M@Uc)>2000
    return dict(congruence_cases=40,fixed_gram_unbounded_boost_control=True)

def box_selection():
    # Cubical version of the source boxes: exact 3D center-volume bound (2Kl)^3.
    for L in [0,.3,2]:
        for ell in [.2,.1,.05]:
            K=1.7;z=np.array([.2,-.1,.3]);f=lambda y:L*y[0]
            for delta in product([-1,0,1],repeat=3):
                y=z+.99*K*ell*np.array(delta)
                for side in [-1,1]:
                    s=f(z)+side*.99*K*ell
                    assert abs(s-f(y))<=K*(1+L)*ell+1e-12
            # Over unit-volume centers the normalized average for Gamma=1 is 16K^4 ell.
            assert abs((2*K*ell)**4/ell**3-16*K**4*ell)<1e-12
    p=1.5;ell=np.array([.25,.125,.0625]);radial=2*np.pi**2*ell**(4-p)/(4-p)/ell**3
    assert np.all(np.diff(radial)>0) and 4-2*p>0
    return dict(affine_graph_scales=9,layer_bound=True,locally_L2_fixed_center_divergence=True)

def thermal_affinity():
    m=3;L=np.array([[1.,-1,0],[-1,2,-1],[0,-1,1]])
    H=np.kron(L,np.eye(m))+np.kron(np.eye(m),L)+np.diag([.7 if i==j else 0 for i,j in product(range(m),repeat=2)])
    S=np.zeros((m*m,m*m))
    for i,j in product(range(m),repeat=2):S[i*m+j,j*m+i]=1
    P=(np.eye(m*m)+S)/2;B=lambda t:expm(-t*H)@P
    beta=.8;Z=np.trace(B(beta));Phi=B(beta/2)/np.sqrt(Z);Gamma=B(beta)/Z
    assert Phi.min()>0 and abs(np.sum(Phi**2)-1)<1e-12 and np.allclose(Phi@Phi.T,Gamma)
    joint=Phi**2;assert np.allclose(joint.sum(axis=1),np.diag(Gamma))
    assert abs(np.trace(B(.3)@B(.5))/Z-1)<1e-12
    T=Phi.reshape(m,m,m*m);occupation=np.sum(T.sum(axis=0)**2)/m
    rho=np.einsum('ij,kj->ik',T.reshape(m,-1),T.reshape(m,-1));assert abs(occupation-rho.sum()/m)<1e-12
    affinitysum=sum(np.sum(m*T[x]*T[y]) for x,y in product(range(m),repeat=2))/m**2
    assert abs(affinitysum-occupation)<1e-12
    rng=np.random.default_rng(8107)
    for _ in range(40):
        p=rng.random(8);q=rng.random(8);nu=np.minimum(p,q)*rng.random(8);mass=nu.sum()
        cp=np.sum(nu*nu/p);cq=np.sum(nu*nu/q)
        assert np.sqrt(p*q).sum()+1e-12>=mass**2/np.sqrt(cp*cq)
    plus=np.array([[.5,.5],[.5,.5]]);minus=np.array([[.5,-.5],[-.5,.5]])
    assert np.array_equal(np.diag(plus),np.diag(minus)) and plus.sum()/2==1 and minus.sum()/2==0
    return dict(two_particle_kernel_dimension=9,common_measure_cases=40,cell_affinity_identity=True,diagonal_density_loses_coherence=True)

def all_q_sandwich():
    rng=np.random.default_rng(8108);cases=0
    for _ in range(30):
        n=5;w=rng.random((n,n));w=(w+w.T)/2;np.fill_diagonal(w,0)
        H=np.diag(w.sum(axis=1))-w+np.diag(rng.random(n));a=rng.normal(size=n)*.4;delta=rng.uniform(.2,1)
        correction=np.sum(w*(np.cosh(a[:,None]-a[None,:])-1),axis=1)
        Ht=H-np.diag(2*a/delta+correction);E=eigh(Ht,eigvals_only=True)
        for u in np.linspace(-1,1,7):
            conjugate=np.exp(u*a[:,None])*H*np.exp(-u*a[None,:])
            # Real form product correction, bounded by the exact graph cosh correction.
            sym=(conjugate+conjugate.T)/2
            assert min(eigh(sym-H+np.diag(correction),eigvals_only=True))>-1e-10
        X=np.exp(a[:,None])*expm(-delta*H)*np.exp(a[None,:]);logx=np.log(eigh(X,eigvals_only=True)[::-1])
        assert np.all(np.cumsum(logx)<=np.cumsum(-delta*E)+1e-10)
        for q in [.1,.3,.7,1,1.5,2,3.2]:assert np.exp(q*logx).sum()<=np.exp(-q*delta*E).sum()+1e-9
        cases+=1
    return dict(graph_analogues=cases,powers=[.1,.3,.7,1,1.5,2,3.2],continuum_gradient_square_not_imported=True)

if __name__=='__main__':
    start=time.perf_counter();checks={}
    for f in [conformal_constraints,area_envelope,retained_freshness,spectral_averaging,lorentz_frames,box_selection,thermal_affinity,all_q_sandwich]:checks[f.__name__]=dict(status='pass',details=f())
    result=dict(batch='B081',status='pass',elapsed_seconds=round(time.perf_counter()-start,3),scope='Selected finite mechanisms and one discrete analogue; no headline or Lean certification.',checks=checks)
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8');print(json.dumps(result))
