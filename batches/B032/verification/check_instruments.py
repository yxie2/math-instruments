"""Selected positive-measure, entropy, thermal and transport checks."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import math
import numpy as np
import sympy as S
from scipy.optimize import minimize, minimize_scalar
from scipy.special import logsumexp
rng=np.random.default_rng(32016)

def density_pruning():
    tests=0
    for trial in range(100):
        nums=list(map(int,rng.integers(1,15,64)));mass=[F(n,sum(nums)) for n in nums]
        good={i for i in range(64) if rng.random()<.35};original=set(good);eta=F(1,8);depths=(0,2,4,6)
        if trial%2==0:
            mass=[F(1,64)]*64;good=set(range(64));original=set(good);eta=F(9,10)
        def cells(depth):return [set(range(k,k+2**(6-depth))) for k in range(0,64,2**(6-depth))]
        total=lambda A:sum(mass[i] for i in A)
        for depth in depths:
            for cell in cells(depth):
                if total(cell&original)<eta*total(cell):good-=cell
        assert total(original-good)<=len(depths)*eta
        target={int(rng.integers(0,64))} if trial%2==0 else {i for i in good if rng.random()<.5}
        factors=[]
        for j in range(3):
            children=cells(depths[j+1]);ratios=[]
            for parent in cells(depths[j]):
                hit=[c for c in children if c<=parent and c&target]
                ratios.append(sum(total(c&original) for c in hit)/total(parent))
                assert sum(total(c) for c in hit)<=ratios[-1]*total(parent)/eta
            factors.append(max(ratios))
        assert total(target)<=math.prod(factors)/eta**3;tests+=1
    return dict(exact_tree_pruning_models=tests,scope='Abstract hit-cube multiplication; geometric angular containment is an input.')

def collision_bins():
    tests=0;fourier=0
    for _ in range(80):
        x=rng.integers(-40,41,20)/10;y=rng.integers(-40,41,16)/10
        a=rng.random(20);b=rng.random(16);a/=a.sum();b/=b.sum()
        bins=lambda z,w:np.array([sum(w[np.floor(z)==k]) for k in range(-4,5)])
        aa=bins(x,a);bb=bins(y,b);Ba=aa@aa;Bb=bb@bb
        delta=x[:,None]-x[None,:];weights=np.outer(a,a)
        assert Ba<=np.sum(weights*(abs(delta)<=1))+1e-12
        for C in (1,2):
            for shift in (-3.1,-.2,0,1.3):assert np.sum(weights*(abs(delta-shift)<=C))<=(2*C+3)*Ba+1e-12
            # Fourier convention exp(-i r x); integrate on [-1,1] exactly for atoms.
            integral=np.sum(weights*2*np.sinc(delta/np.pi))
            c=(np.sin(.5)/.5)**2
            assert np.sum(weights*(abs(delta)<=C))<=C*integral/c+1e-11;fourier+=1
        kernel=np.sum(np.outer(a,b)/(1+abs(x[:,None]-y[None,:]))**2)
        assert kernel<=10*np.sqrt(Ba*Bb)+1e-12;tests+=1
    return dict(atomic_collision_models=tests,finite_band_fourier_bounds=fourier,scope='Atomic measures, including coincident atoms; constants chosen conservatively.')

def thermal_forms():
    y=np.arange(4096)/4096;freq=np.arange(1,5);cos=np.cos(2*np.pi*freq[:,None]*y);chars=np.cos(2*np.pi*np.arange(13)[:,None]*y)
    def calc(lam):
        f=np.exp(-lam@(1-cos));q=chars@f/len(y);return -np.log(q[0]),q,q/q[0],f
    tests=0;minimum=1.
    for _ in range(60):
        A=rng.random(4)*2;D=rng.random(4);E=rng.random(4)
        fa,qa,ca,wa=calc(A);fad,qad,cad,_=calc(A+D);fe,qe,ce,_=calc(A+E);fed,_,ced,_=calc(A+D+E)
        assert min(qa)>=-1e-13 and min(cad-ca)>=-1e-12 and fad>=fa-1e-12
        assert fed-fe<=fad-fa+1e-11
        K=wa/wa.sum();cov=(chars*K)@chars.T-np.outer(ca,ca);minimum=min(minimum,float(cov.min()));assert cov.min()>-1e-12
        delta=np.sqrt(np.maximum(0,2*(1-ca)))
        for u,v in product(range(7),repeat=2):assert delta[u+v]<=delta[u]+delta[v]+1e-10
        shift=rng.random();shifted=np.exp(-A@(1-np.cos(2*np.pi*freq[:,None]*(shift-y))))*np.exp(-D@(1-cos))
        for u in range(8):assert abs(np.mean(np.exp(2j*np.pi*u*y)*shifted))<=qad[u]+1e-12
        tests+=1
    return dict(circle_quadrature_models=tests,minimum_covariance=minimum,scope='Finite spectral windows and periodic quadrature, not all coefficients or the Fourier-convergence procedure.')

def prescribed_marginal_variation():
    tests=0;worst=0.
    for T,alpha in product((2,3),(.1,.5,2.)):
        tuples=np.array(list(product((0,1),repeat=T)));sums=tuples.sum(axis=1);Z=np.arange(T+1);cost=alpha*(Z[None,:]-sums[:,None])**2
        shape=cost.shape;N=cost.size
        constraint=np.vstack((np.ones(N),*[np.repeat(tuples[:,i],len(Z)) for i in range(T)]));target=np.r_[1,np.full(T,.5)]
        def objective(flat):
            p=flat.reshape(shape);pz=p.sum(axis=0);return T*np.log(2)+np.sum(p*(np.log(p/pz)+cost))
        def jac(flat):
            p=flat.reshape(shape);return (np.log(p/p.sum(axis=0))+cost).ravel()
        sol=minimize(objective,np.full(N,1/N),jac=jac,bounds=[(1e-12,1)]*N,
            constraints={'type':'eq','fun':lambda x:constraint@x-target,'jac':lambda x:constraint},
            method='SLSQP',options={'ftol':1e-12,'maxiter':1000})
        assert sol.success
        def dual(a):return T*np.log(2)+T*a/2-max(logsumexp(a*sums[:,None]-cost,axis=0))
        optimum=minimize_scalar(lambda a:-dual(a),bounds=(-10,10),method='bounded',options={'xatol':1e-11})
        gap=sol.fun-dual(optimum.x);worst=max(worst,abs(gap));assert -1e-8<=gap<1e-7 and np.max(abs(constraint@sol.x-target))<1e-9
        p=sol.x.reshape(shape);px=p.sum(axis=1);pz=p.sum(axis=0)
        divergence=np.sum(px*np.log(px*2**T));info=np.sum(p*np.log(p/(px[:,None]*pz[None,:])))
        assert abs(divergence+info+np.sum(p*cost)-sol.fun)<1e-10;tests+=1
    return dict(primal_dual_prescribed_marginal_models=tests,maximum_duality_gap=worst,scope='Finite binary models; no verification of the source all-distribution moment hypothesis or later entropy compression.')

def likelihood_domination():
    tests=0
    for _ in range(200):
        p=rng.random(24);p/=p.sum();q=rng.random(24);q/=q.sum();logL=np.log(p/q);D=p@logL
        assert p@np.maximum(-logL,0)<=1/np.e+1e-12
        for v in (.1,.5,1,2,4):
            assert p[logL>v].sum()<=(D+1/np.e)/v+1e-12
            kept=p*(logL<=v);assert np.all(kept<=np.exp(v)*q+1e-12)
        rho=p.reshape(4,6);mu=rng.random(4);mu/=mu.sum();nu=rng.random(6);nu/=nu.sum();reference=np.outer(mu,nu)
        actual=np.outer(rho.sum(axis=1),rho.sum(axis=0));K=np.max(rho/reference)
        assert np.sum(rho*np.log(rho/actual))<=np.log(K)+1e-12;tests+=1
    return dict(likelihood_and_actual_product_models=tests,scope='Finite likelihood truncations and entropy decomposition.')

def marginal_core():
    tests=0;deletions=0
    for trial in range(100):
        points=list(product(range(4),range(3),range(2)));weights=[F(int(x),10000) for x in rng.integers(1,100,len(points))]
        weights=[w/1000 if x[0]==0 or (trial%2==0 and x[1]==0) else w for x,w in zip(points,weights)];m=sum(weights)
        observations=[lambda x:x[0],lambda x:x[1],lambda x:x[0],lambda x:x[2]]
        comparators=[]
        for sizes in (4,3,4,2):
            nums=list(map(int,rng.integers(1,15,sizes)));comparators.append({i:F(v,sum(nums)) for i,v in enumerate(nums)})
        eta=m/8;current=weights.copy()
        def marg(w,f):
            out={}
            for x,a in zip(points,w):out[f(x)]=out.get(f(x),F(0))+a
            return out
        oldbounds=[]
        for i,j in ((0,1),(2,3)):
            joint=marg(weights,lambda x:(observations[i](x),observations[j](x)))
            oldbounds.append(max(a/(comparators[i][u]*comparators[j][v]) for (u,v),a in joint.items()))
        while True:
            removed=False
            for f,mu in zip(observations,comparators):
                now=marg(current,f)
                for value,a in now.items():
                    if 0<a<eta*mu[value]:
                        for k,x in enumerate(points):
                            if f(x)==value:current[k]=F(0)
                        removed=True;deletions+=1;break
                if removed:break
            if not removed:break
        M=sum(current);assert M>=m-4*eta and M>0;rho=[a/M for a in current]
        for (i,j),A in zip(((0,1),(2,3)),oldbounds):
            joint=marg(rho,lambda x:(observations[i](x),observations[j](x)));mi=marg(rho,observations[i]);mj=marg(rho,observations[j])
            assert all(a<=A*M/eta**2*mi[u]*mj[v] for (u,v),a in joint.items())
        tests+=1
    assert deletions>=100
    return dict(exact_simultaneous_core_models=tests,removed_factor_values=deletions,scope='Repeated observations with different comparison marginals are counted separately.')

def conformal_chart():
    t,b1,b2,y,k=S.symbols('t b1 b2 y k');x=S.Matrix([t,b1,b2,y]);q=t*y-b1*b1-b2*b2
    G=S.Matrix([[0,0,0,S.Rational(1,2)],[0,-1,0,0],[0,0,-1,0],[S.Rational(1,2),0,0,0]])
    v=S.Matrix([0,0,k,0]);D=1-2*k*b2-k*k*q;phi=(x+v*q)/D;w=1/D
    simp=lambda z:S.factor(z)
    assert simp((phi.T*G*phi)[0]-q/D)==0
    invD=1+2*k*phi[2]-k*k*(phi.T*G*phi)[0]
    for z in (phi-v*(phi.T*G*phi)[0])/invD-x:assert simp(z)==0
    J=phi.jacobian(x)
    for z in J.T*G*J-G/D**2:assert simp(z)==0
    box=lambda f:4*S.diff(f,t,y)-S.diff(f,b1,2)-S.diff(f,b2,2)
    assert simp(box(w))==0
    for u in phi:assert simp(box(w*u))==0
    # The second-order chain coefficients give the full wave covariance.
    for z in J*G.inv()*J.T-G.inv()/D**2:assert simp(z)==0
    c,d,a1,a2,beta,h=S.symbols('c d a1 a2 beta h')
    before=a1*a1+a2*a2-4*beta*d+4*h*c
    after=a1*a1+(a2+2*c*k)**2-4*beta*d+4*(h-a2*k-c*k*k)*c
    assert S.expand(after-before)==0
    return dict(metric_entries=16,inverse_coordinates=4,wave_zero_and_first_order_identities=5,wave_second_order_entries=16,discriminant='preserved',scope='Exact rational chart identities away from D=0; no packet localization, band projection or transport estimate certified.')

def capacity_allocation():
    models=0;zero=0
    for _ in range(120):
        n,m,L=7,9,4;inc=rng.integers(0,2,(n,m));y=[F(int(z),10) for z in rng.integers(0,10,m)]
        A=F(3,2);D=max(1,int(inc.sum(axis=0).max()));eps=[F(int(z),100) for z in rng.integers(0,8,n)]
        old=[[F(0) for i in range(n)] for l in range(L)];new=[[F(0) for j in range(m)] for l in range(L)];retained=[F(0)]*L;removed=F(0)
        for i in range(n):
            Y=sum(y[j] for j in range(m) if inc[i,j]);cap=A*Y+eps[i];parts=list(map(int,rng.integers(1,10,L)))
            values=[cap*F(p,sum(parts)) for p in parts];factor=min(F(1),A*Y/cap) if cap else F(0)
            kept=[z*factor for z in values];removed+=sum(values)-sum(kept)
            for l in range(L):
                retained[l]+=kept[l]
                if Y:
                    for j in range(m):
                        if inc[i,j]:new[l][j]+=kept[l]*y[j]/(A*D*Y)
                else:zero+=1;assert kept[l]==0
        assert removed<=sum(eps)
        for j in range(m):assert sum(new[l][j] for l in range(L))<=y[j]
        for l in range(L):assert sum(new[l])==retained[l]/(A*D)
        models+=1
    return dict(exact_fractional_allocation_models=models,zero_capacity_label_cases=zero,scope='Cell-capacity transfer conditional on the predecessor and overlap bounds.')

if __name__=='__main__':
    groups={}
    for fn in (density_pruning,collision_bins,thermal_forms,prescribed_marginal_variation,likelihood_domination,marginal_core,conformal_chart,capacity_allocation):
        groups[fn.__name__]=fn();print(fn.__name__,'passed',flush=True)
    out=dict(batch='B032',status='passed',check_groups=groups,limitations='Selected local and finite mechanisms only; no Falconer, L log L, Bochner-Riesz or local-smoothing theorem certified; no Lean build.')
    Path(__file__).with_name('results.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out,indent=2))
