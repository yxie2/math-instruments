"""Finite mechanism checks; not a proof of source scaling or percolation claims."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product, combinations
from pathlib import Path
import json
import math
import time
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.special import k0


def ray_calibration():
    cases=0
    points=[(a,h) for a in range(-4,8) for h in range(4)]
    def distance(x,y):return 0 if x==y else (abs(x[0]-y[0])+x[1]+y[1])
    potential=lambda x:x[1]-x[0]
    for x,y in product(points,repeat=2):
        B=potential(x)-potential(y)
        assert abs(B)<=distance(x,y)
        assert distance(x,(100,0))-distance(y,(100,0))==B
        seq=[distance(x,(j,0))-j for j in range(15)]
        assert all(a>=b for a,b in zip(seq,seq[1:])) and seq[-1]==potential(x)
        for j in range(15):assert distance(x,(j,0))-(potential(x)+j)==seq[j]-potential(x)>=0
        cases+=1
    for x,y,z in zip(points,points[1:],points[2:]):assert potential(x)-potential(z)==potential(x)-potential(y)+potential(y)-potential(z)
    euclidean=[]
    for j in [1,2,4,8,16,32,64]:euclidean.append(math.hypot(j,3)-j)
    assert all(a>b>0 for a,b in zip(euclidean,euclidean[1:]))
    a=[abs(3-j)-abs(j) for j in [0,2,1]];assert a[2]>a[1]
    return dict(tree_metric_pairs=cases,euclidean_positive_defects=euclidean,nongeodesic_control=True)


def support_regularities():
    rng=np.random.default_rng(7702);cases=0
    for p in [2.,3.,4.]:
        for _ in range(40):
            u=rng.normal(size=2);h=rng.normal(size=2);norm=lambda v:float(np.sum(abs(v)**p)**(1/p))
            g=np.sign(u)*abs(u)**(p-1)/norm(u)**(p-1)
            assert abs(g@u-norm(u))<1e-12
            for _ in range(10):
                v=rng.normal(size=2);assert g@v<=norm(v)+1e-12
            errors=[abs(norm(u+e*h)-norm(u)-e*g@h)/e for e in [1e-3,1e-4,1e-5]]
            assert errors[-1]<errors[0]+1e-10;cases+=1
    corner=np.ones(2)
    for a in np.linspace(0,1,21):
        g=np.array([a,1-a]);assert g@corner==1
        for v in product([-2,-1,0,1,2],repeat=2):assert g@v<=max(abs(t) for t in v)
    # Stadium = [-1,1] x {0} plus unit disk. Flat top and round caps have matching tangents.
    boundary=np.array([(x,1) for x in np.linspace(-1,1,21)]+[(1+math.cos(t),math.sin(t)) for t in np.linspace(-math.pi/2,math.pi/2,101)])
    assert np.all(boundary[:,1]<=1+1e-12)
    assert np.allclose(np.array([-.5,1])+np.array([.5,1]),2*np.array([0,1]))
    assert np.allclose([-math.sin(math.pi/2),math.cos(math.pi/2)],[-1,0])
    return dict(smooth_norm_models=cases,nonunique_corner_supports=21,c1_flat_segment_control=True)


def cluster(n,edges,bits,seeds,deleted=frozenset()):
    reached=set(seeds)-set(deleted)
    while True:
        old=len(reached)
        for edge,opened in zip(edges,bits):
            if opened and not (edge&deleted) and (edge&reached):reached.update(edge)
        if len(reached)==old:return frozenset(reached)


@lru_cache(None)
def models():
    rng=np.random.default_rng(7703);out=[]
    for rep in range(12):
        n=4;edges=[frozenset([0,1]),frozenset([1,2]),frozenset([2,3]),frozenset([0,2,3]),frozenset([0,1])]
        probs=[F(int(rng.integers(1,5)),5) for _ in edges]
        states=[]
        for bits in product([0,1],repeat=len(edges)):
            w=math.prod(p if b else 1-p for b,p in zip(bits,probs))
            states.append((bits,w,[cluster(n,edges,bits,[i]) for i in range(n)]))
        out.append((n,edges,probs,states))
    return out


def cluster_columns():
    cone_checks=0;resampling_checks=0
    for model,(n,edges,probs,states) in enumerate(models()):
        order=[2,0,3,1] if model%2 else list(range(n));mus=[];d=[]
        for k,s in enumerate(order):
            law={};den=F(0)
            for bits,w,cs in states:
                if not cs[s]&set(order[:k]):law[cs[s]]=law.get(cs[s],F(0))+w;den+=w
            mus.append({U:w/den for U,w in law.items()});d.append(den)
        H=sp.Matrix([[sum(w for U,w in mu.items() if s in U) for mu in mus] for s in order]);inv=H.inv()
        assert H*sp.Matrix(d)==sp.ones(n,1)
        Gamma=sp.eye(n)-inv;assert all(Gamma[i,j]>=0 for i in range(n) for j in range(n))
        functions=[lambda U:len(U),lambda U:len(U)**2]+[lambda U,A=A:int(bool(U&A)) for A in [frozenset([0]),frozenset([1,3]),frozenset([0,2,3])]]
        for k,mu in enumerate(mus):
            for fun in functions:
                v=sp.Matrix([sum(w*fun(U) for U,w in mu.items() if s in U) for s in order]);mean=sum(w*fun(U) for U,w in mu.items())
                coords=inv*v
                assert all(c>=0 for c in coords) and coords[k]==mean and all(coords[j]==0 for j in range(k));cone_checks+=1
        # Assemble alternating conditional resampling from deletion laws, including zero-mass states.
        k=1;s=order[k];S=frozenset(order[:k]);free=[v for v in range(n) if v not in S and v!=s]
        domain=[frozenset([s]+[v for v,b in zip(free,bits) if b]) for bits in product([0,1],repeat=len(free))]
        P=[]
        for U in domain:
            row={V:F(0) for V in domain}
            for bits,w,cs in states:
                W=cluster(n,edges,bits,S,U)
                for bits2,w2,cs2 in states:
                    V=cluster(n,edges,bits2,[s],W);row[V]+=w*w2
            P.append([row[V] for V in domain])
        P=sp.Matrix(P);mu=sp.Matrix([[mus[k].get(U,F(0)) for U in domain]])
        assert mu*P==mu
        a=math.prod(1-p for e,p in zip(edges,probs) if s in e);single=domain.index(frozenset([s]))
        assert all(P[i,single]>=a for i in range(len(domain)))
        f=sp.Matrix([len(U)**2 for U in domain]);pf=P*f
        assert max(pf)-min(pf)<=(1-a)*(max(f)-min(f));resampling_checks+=1
    return dict(exact_cone_functions=cone_checks,full_deletion_resampling_matrices=resampling_checks)


def relay_events():
    inequalities=0;site_maps=0
    for n,edges,probs,states in models():
        subsets=[frozenset(i for i,b in enumerate(bits) if b) for bits in product([0,1],repeat=n)]
        for o in range(n):
            for A in subsets[1:]:
                reach=sum(w for bits,w,cs in states if cs[o]&A)
                for T in subsets:
                    joint=sum(w for bits,w,cs in states if cs[o]&A and cs[o]&T)
                    least=min(sum(w for bits,w,cs in states if cs[a]&T) for a in A)
                    assert joint>=reach*least;inequalities+=1
    # Site-to-hypergraph incidence, with all configurations including closed self-sites.
    edges=[(0,1),(1,2),(2,3),(0,3)];n=4
    hypers=[frozenset([v]+[n+j for j,e in enumerate(edges) if v in e]) for v in range(n)]
    for bits in product([0,1],repeat=n):
        site_edges=[frozenset(e) for e in edges];edge_bits=[bits[a] and bits[b] for a,b in edges]
        for o in range(n):
            cs=cluster(n,site_edges,edge_bits,[o]) if bits[o] else frozenset()
            ch=cluster(n+len(edges),hypers,bits,[o])&set(range(n))
            if bits[o]:assert cs==ch
            else:assert o in ch and o not in cs
            site_maps+=1
    for probs in [[F(1,2)]*4,[F(0),F(1),F(1,3),F(2,3)]]:
        states=[]
        for bits in product([0,1],repeat=n):
            w=math.prod(p if b else 1-p for p,b in zip(probs,bits));edge_bits=[bits[a] and bits[b] for a,b in edges]
            cs=[cluster(n,[frozenset(e) for e in edges],edge_bits,[o]) if bits[o] else frozenset() for o in range(n)]
            states.append((w,cs))
        for A in [frozenset([0]),frozenset([1,2]),frozenset([0,1,3])]:
            for T in [frozenset([0]),frozenset([2,3])]:
                b=1-min(sum(w for w,cs in states if cs[a]&T) for a in A)
                for o in range(n):assert sum(w for w,cs in states if cs[o]&A and not cs[o]&T)<=b
    return dict(exact_joint_inequalities=inequalities,site_incidence_configurations=site_maps,deterministic_site_bits=True)


def spin_projection():
    rng=np.random.default_rng(7705);directions=np.vstack([np.eye(3),-np.eye(3)]);cases=0
    for n in [4,5,8]:
        for _ in range(8):
            v=rng.normal(size=(3,n-3));v=v/(2*np.maximum(1,np.linalg.norm(v,axis=1))[:,None]);rho=np.sqrt(1-np.sum(v*v,axis=1));b=rng.random(2)*3
            full=[];reduced=[]
            for ids in product(range(6),repeat=3):
                s=directions[list(ids)];sigma=np.concatenate([rho[:,None]*s,v],axis=1)
                full.append(sum(b[i]*(sigma[i]@sigma[i+1]) for i in range(2)))
                reduced.append(sum(b[i]*rho[i]*rho[i+1]*(s[i]@s[i+1]) for i in range(2)))
            full=np.exp(full);reduced=np.exp(reduced)
            assert np.allclose(full/full.sum(),reduced/reduced.sum(),atol=1e-14);cases+=1
    z=rng.normal(size=(100000,7));s=z[:,:3]/np.linalg.norm(z[:,:3],axis=1)[:,None];v=z[:,3:]/np.linalg.norm(z,axis=1)[:,None]
    moment=float(np.mean(s[:,0]**2));cross=float(np.mean((s[:,0]**2-1/3)*np.sum(v*v,axis=1)))
    assert abs(moment-1/3)<.01 and abs(cross)<.01
    return dict(exact_grid_density_models=cases,gaussian_moment_illustration=moment,gaussian_independence_illustration=cross)


def massive_kernels():
    max_error=0.;cases=0
    for mu,t in product([.5,1.,2.,3.],[.5,1.,2.,4.]):
        val=quad(lambda p:math.exp(-t*math.hypot(p,mu))/(2*math.pi*math.hypot(p,mu)),0,np.inf,epsabs=1e-11)[0]
        target=k0(mu*t)/(2*math.pi);max_error=max(max_error,abs(val-target));assert abs(val-target)<1e-9;cases+=1
    # rho(ds)=ds/3 on [1,4] is atomless, including at its lower edge.
    continuous=lambda r:quad(lambda s:k0(math.sqrt(s)*r)/(6*math.pi),1,4,epsabs=1e-12)[0]
    atomic=lambda r:sum(w*k0(mu*r)/(2*math.pi) for w,mu in [(1.,1.),(.3,2.),(.7,4.)])
    for C in [continuous,atomic]:
        bound=math.e*C(1)
        for r in np.linspace(1,12,45):assert 0<C(r)<=bound*math.exp(-r)+1e-12;cases+=1
    return dict(quadrature_and_decay_checks=cases,max_bessel_comparison_error=max_error,atomless_mass_measure_tested=True)


def tree_gluing():
    rng=np.random.default_rng(7707);cases=0
    for q in [2,3,5]:
        for count in range(2,6):
            edges=[(int(rng.integers(v)),v) for v in range(1,count)];weights=[rng.random(q)+.1 for _ in edges]
            seen=set();direct=0.
            for rest in product(range(q),repeat=count-1):
                heights=(0,)+rest;diffs=tuple((heights[v]-heights[u])%q for u,v in edges);seen.add(diffs)
                direct+=math.prod(w[d] for w,d in zip(weights,diffs))
            assert len(seen)==q**(count-1) and abs(direct-math.prod(sum(w) for w in weights))<1e-9;cases+=1
        cycle_differences={((b-a)%q,(c-b)%q,(a-c)%q) for a,b,c in product(range(q),repeat=3)}
        assert len(cycle_differences)==q*q<q**3 and all(sum(ds)%q==0 for ds in cycle_differences)
    # Both exterior boundaries share one latent variable; its joint kernel has covariance.
    joint=np.array([[.5,0],[0,.5]]);marginal=np.outer(joint.sum(axis=1),joint.sum(axis=0))
    assert not np.allclose(joint,marginal)
    return dict(tree_translation_bijections=cases,cycle_constraint_controls=3,joint_exterior_control=True)


def positive_core():
    rng=np.random.default_rng(7708);xi=.012;factor=3*math.sqrt(xi)/(1-2*xi);steps=0;cores=0
    for model in range(30):
        size=8;m=rng.random(size);m/=sum(m);g=np.geomspace(1e-90,1.,size);rng.shuffle(g)
        kernels=[]
        for _ in range(18):
            loss=rng.random((size,size))**8;loss*=min(.999/float(loss.max()),xi/float(m@loss@m));kernels.append(1-loss)
        delta=next(v for v in sorted(g,reverse=True) if sum(m[g<v])<.25)
        q=np.ones(size);f=g.copy();c=m@f;E=f-c*q
        for T in kernels:
            assert m@(1-T)@m<=xi+1e-12
            L=lambda z:(m*z)@T
            beta=m@L(q);qn=L(q)/beta;fn=L(f)/beta;cn=m@fn;En=fn-cn*qn
            recurrence=(L(E)-(m@L(E))*qn)/beta
            assert np.allclose(En,recurrence,atol=1e-15)
            norm=lambda z:math.sqrt(float(m@(z*z)))
            assert norm(En)<=factor*norm(E)+1e-14 and max(abs(En))<=3/(1-2*xi)*norm(E)+1e-14
            assert beta>=1-2*xi-1e-12 and max(qn)<=1/(1-2*xi)+1e-12
            assert cn>=delta/2-1e-14
            q,f,c,E=qn,fn,cn,En;steps+=1
        assert max(f/c)<=2;cores+=1
        backward=np.ones(size)
        for T in reversed(kernels):
            backward=T@(m*backward);backward/=m@backward;assert max(backward)<=2
        assert abs(m@(g*backward)-c)<1e-12
    # Without a small average loss, near-identity kernels retain a concentrated core for a long time.
    T=np.eye(8)*(1-1e-9)+np.ones((8,8))*1e-9;m=np.ones(8)/8;f=np.array([1.]+[1e-30]*7)
    for _ in range(18):f=(m*f)@T;f/=m@f
    assert max(f)>7 and m@(1-T)@m>.8
    return dict(centered_recurrence_steps=steps,uneven_positive_cores=cores,minimum_core_weight=1e-90,high_loss_negative_control=True)


if __name__=='__main__':
    start=time.perf_counter();checks={}
    for f in [ray_calibration,support_regularities,cluster_columns,relay_events,spin_projection,massive_kernels,tree_gluing,positive_core]:checks[f.__name__]=dict(status='pass',details=f())
    result=dict(batch='B077',status='pass',elapsed_seconds=round(time.perf_counter()-start,3),scope='Selected finite mechanisms and explicit dependency controls; no headline or Lean certification.',checks=checks)
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8');print(json.dumps(result))
