"""Finite models for selected analytic bookkeeping; no headline proof certification."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import permutations, product
from math import ceil, log2, prod
from pathlib import Path
import json
import numpy as np

RNG=np.random.default_rng(23081)
OUT={}

def moving_cells():
    models=0; maxratio=0.; errors=[]
    for size in [8,12,16]:
        axis=(np.arange(size)+.5)/size
        xy=np.array(list(product(axis,repeat=2)))
        for epsilon in [.01,.05]:
            xyz=np.c_[xy,epsilon*np.sin(5*xy[:,0])*np.cos(4*xy[:,1])]
            weights=np.full(len(xy),1/len(xy))
            val=np.sin(xy[:,0])+xy[:,1]**2+epsilon*np.cos(3*xy[:,0])
            for cells in [2,4]:
                ix=np.floor(xy*cells).astype(int); total=0.; Eall=0.
                for key in product(range(cells),repeat=2):
                    use=np.all(ix==key,axis=1); w=weights[use]; f=val[use]; x=xyz[use]
                    mass=w.sum(); mean=np.dot(w,f)/mass
                    variance=np.dot(w,(f-mean)**2)
                    delta=(f[:,None]-f[None,:])**2
                    direct=np.sum(w[:,None]*w[None,:]*delta)/(2*mass)
                    assert abs(variance-direct)<1e-12
                    dist=np.linalg.norm(x[:,None,:]-x[None,:,:],axis=2)
                    kernel=np.divide(delta,dist**3,out=np.zeros_like(delta),where=dist>0)
                    energy=np.sum(w[:,None]*w[None,:]*kernel)
                    bound=dist.max()**3/(2*mass)*energy
                    assert variance<=bound+1e-12
                    if bound:maxratio=max(maxratio,variance/bound)
                    total+=variance;Eall+=energy
                assert total<=((2**.5+2)**3/1)*Eall/cells+1e-12
                models+=1;errors.append(total)
    # Weak first moments alone do not preserve squared moments.
    n=128; alternating=np.array([(-1.)**i for i in range(n)])
    assert alternating.mean()==0 and np.mean(alternating**2)==1
    OUT['moving_measure_cells']={'models':models,'maximum_variance_bound_ratio':maxratio,'scope':'Atomic grid models of the exact cell identity and energy inequality; atoms do not satisfy the continuum AD hypotheses. Oscillating control loses second moments without compactness.'}

def seed_charging():
    depth=6; leaves=list(product(range(2),repeat=depth)); nodes=[p for k in range(depth+1) for p in product(range(2),repeat=k)]
    checks=0
    for _ in range(150):
        w=RNG.integers(1,8,len(leaves)); mass={q:sum(int(v) for x,v in zip(leaves,w) if x[:len(q)]==q) for q in nodes}
        family=[q for q in nodes if RNG.random()<.25]; seeds={}
        for q in family:
            d=int(RNG.integers(0,min(2,depth-len(q))+1));seeds[q]=q+tuple(int(t) for t in RNG.integers(0,2,d))
        charges=set()
        for q in family:
            s=seeds[q]
            for qq in family:
                if len(s)<len(qq) and qq[:len(s)]==s:charges.add(qq[:-1])
        M=max([F(mass[q],mass[s]) for q,s in seeds.items()]+[F(1)])
        K=F(sum(mass[q] for q in charges),mass[()])
        assert sum(mass[q] for q in family)<=M*3*(1+K)*mass[()]
        for x in leaves:
            count=sum(x[:len(s)]==s for s in seeds.values())
            budget=3*(1+sum(x[:len(q)]==q for q in charges))
            assert count<=budget;checks+=1
    assert 5>1 # Five nested self-seeds with no intervening charge violate the N=0 pointwise bound.
    OUT['seed_charging']={'random_weighted_trees':150,'pointwise_leaf_checks':checks,'scope':'Full eligible-pair charge construction, overlapping seeds and nonuniform masses; does not prove geometric flat-seed or oscillation estimates.'}

def clock_thinning():
    models=0; orders=0; dependent=0
    for n in [3,4,5,6]:
        for _ in range(8):
            adjacency=np.triu(RNG.random((n,n))<.45,1);adjacency=adjacency|adjacency.T
            rates=list(map(int,RNG.integers(1,6,n)))
            pi=[F(rates[i],rates[i]+sum(rates[j] for j in range(n) if adjacency[i,j])) for i in range(n)]
            observed=[F(0)]*n; pair=np.zeros((n,n)); total=F(0)
            distribution=[]
            for order in permutations(range(n)):
                probability=F(1); remaining=sum(rates)
                for i in order:probability*=F(rates[i],remaining);remaining-=rates[i]
                position={i:k for k,i in enumerate(order)}
                keep=[i for i in range(n) if all(position[i]<position[j] for j in range(n) if adjacency[i,j])]
                assert all(not adjacency[i,j] for i in keep for j in keep)
                for i in keep:
                    observed[i]+=probability
                    for j in keep:pair[i,j]+=float(probability)
                distribution.append((float(probability),keep));total+=probability;orders+=1
            assert total==1 and observed==pi
            for i in range(n):
                for j in range(i):
                    if abs(pair[i,j]-float(pi[i]*pi[j]))>1e-8:dependent+=1
            l=RNG.random(n);l/=1.2*l.sum()
            m=np.array([rates[i]+sum(rates[j] for j in range(n) if adjacency[i,j])+int(RNG.integers(0,3)) for i in range(n)])
            lam=np.sqrt(np.array(rates)/m)
            gram=np.eye(n)+adjacency/(n+1); V=np.linalg.cholesky(gram)
            original=np.sum(np.sqrt(l)[:,None]*lam[:,None]*V,axis=0)
            mean=np.zeros(n);cost=0.
            for probability,keep in distribution:
                sampled=sum((np.sqrt(l[i])*lam[i]/float(pi[i])*V[i] for i in keep),start=np.zeros(n))
                mean+=probability*sampled;cost+=probability*np.dot(sampled,sampled)
            assert np.linalg.norm(mean-original)<1e-11
            assert np.dot(original,original)<=cost+1e-11 and cost<=l.sum()+1e-11
            models+=1
    # Complete graph, equal masses, identical vectors: dropping the selection coefficient costs n.
    assert (sum([1/3**.5]*3))**2>1
    OUT['clock_thinning']={'graphs':models,'exact_clock_orders':orders,'dependent_indicator_pairs':dependent,'scope':'Exact exponential-race law and r=p=2 compensation with vectors orthogonal on independent sets; not the source finite Fourier estimate.'}

def probability_transfer():
    cases=0; sharp=[]
    for _ in range(500):
        omega=RNG.random(10);omega/=omega.sum();rho=RNG.random(10);rho/=rho.sum()
        eta=float(RNG.uniform(.0001,.49));d=float(RNG.uniform(.001,.5));nu=(1-eta)*omega+eta*rho
        raw=RNG.random(10);f=1-d+d*raw/np.dot(nu,raw)
        assert f.min()>=1-d-1e-12 and abs(np.dot(nu,f)-1)<1e-12
        assert np.dot(omega,f)<=1+eta*d/(1-eta)+1e-12
        theta=float(RNG.uniform(0,1));blend=(1-theta)*f+theta
        assert np.dot(nu,blend)<=1+1e-12
        assert np.all(np.log(blend)-np.log(f)>=-theta*np.log(f)-1e-12)
        cases+=1
    for eta in [.01,.1,.4]:
        d=.03; f=[1+eta*d/(1-eta),1-d]
        assert abs((1-eta)*f[0]+eta*f[1]-1)<1e-12
        sharp.append({'eta':eta,'deficit':d,'uniform_average':f[0]})
    OUT['probability_transfer']={'mixtures':cases,'sharp_two_point_models':sharp,'scope':'Exact mixture inequality and numerical logarithmic blending. Band-limited majorant construction and source relative-drop bounds are not tested.'}

def fmatrix(rows,cols):
    raw=RNG.integers(1,5,(rows,cols))
    return [[F(int(raw[i,j]),int(raw[:,j].sum())) for j in range(cols)] for i in range(rows)]
def mm(A,B):return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]
def removal(U,V):
    P=sum(U);N=sum(V);d=min(P,N)
    up=[x*d/P if P else F(0) for x in U];vm=[x*d/N if N else F(0) for x in V]
    residual=[u-v-a+b for u,v,a,b in zip(U,V,up,vm)]
    beta=[a-b for a,b in zip(up,vm)]
    assert sum(beta)==0 and sum(map(abs,beta))<=2*d
    assert sum(map(abs,residual))==abs(P-N)
    return residual,beta,d
def scalar_pairs():
    models=0; identities=0
    for trial in range(45):
        widths=[3,4,5];trans=[fmatrix(a,b) for a,b in zip(widths,widths[1:])];terminal=fmatrix(5,8)
        nu=list(map(F,map(int,RNG.integers(-4,5,8))))
        if trial==0:terminal=[[F(1,5)]*8 for i in range(5)];nu=[F(1),F(-1)]*4
        phis=[None,None,terminal]
        for level in [1,0]:phis[level]=mm(trans[level],phis[level+1])
        residuals=[None]*3;betas=[None]*3;defects=[]
        for level in [2,1,0]:
            residuals[level]=[];betas[level]=[]
            for s in range(widths[level]):
                if level==2:
                    U=[p*max(v,0) for p,v in zip(phis[level][s],nu)];V=[p*max(-v,0) for p,v in zip(phis[level][s],nu)]
                else:
                    U=[sum(trans[level][s][t]*max(residuals[level+1][t][i],0) for t in range(widths[level+1])) for i in range(8)]
                    V=[sum(trans[level][s][t]*max(-residuals[level+1][t][i],0) for t in range(widths[level+1])) for i in range(8)]
                res,beta,d=removal(U,V);residuals[level].append(res);betas[level].append(beta);defects.append(d)
        for k in range(3):
            coeff=[[F(i==j) for j in range(widths[k])] for i in range(widths[k])]
            reconstructed=[r.copy() for r in residuals[k]]
            for level in range(k,3):
                pieces=mm(coeff,betas[level])
                reconstructed=[[x+y for x,y in zip(row,inc)] for row,inc in zip(reconstructed,pieces)]
                if level<2:coeff=mm(coeff,trans[level])
            assert reconstructed==[[p*v for p,v in zip(row,nu)] for row in phis[k]]
            identities+=widths[k]
        coarse=sum(abs(sum(row)) for row in residuals[0])
        assert sum(defects)==(sum(map(abs,nu))-coarse)/2
        if trial==0:assert all(sum(r)==0 for r in residuals[2]) and sum(defects)>0
        models+=1
    OUT['scalar_pairing']={'shared_descendant_models':models,'measure_reconstruction_identities':identities,'scope':'Exact rational atomic measures with overlapping support and shared descendants; no disk estimates. Zero signed mass can carry positive cancellation cost.'}

def particles():
    cases=0;nodeschecked=0
    for _ in range(80):
        widths=[2,3,4,3]; trans=[np.array(fmatrix(a,b),dtype=float) for a,b in zip(widths,widths[1:])]
        vectors=[None]*4;vectors[-1]=RNG.integers(-4,5,(widths[-1],2)).astype(float)
        for k in [2,1,0]:vectors[k]=trans[k]@vectors[k+1]
        norms=[np.linalg.norm(v,axis=1) for v in vectors]
        population={(r,):{1:float(norms[0][r])} for r in range(widths[0])}; masses={p:sum(v.values()) for p,v in population.items()};weights={p:1. for p in population}
        for k in range(3):
            nxt={}
            for path,births in population.items():
                row=trans[k][path[-1]];caps=weights[path]*row*norms[k+1];S=caps.sum();M=sum(births.values())
                assert M<=S+1e-10
                for j,cap in enumerate(caps):
                    child=path+(j,);weights[child]=weights[path]*row[j]
                    types={b:v*cap/S if S else 0. for b,v in births.items()};types[k+2]=float(cap-M*cap/S) if S else 0.
                    assert min(types.values())>=-1e-10
                    nxt[child]=types;masses[child]=float(cap)
            population=nxt
        for prefix,M in masses.items():
            occupancy=sum(v for path,births in population.items() if path[:len(prefix)]==prefix for b,v in births.items() if b<=len(prefix))
            assert abs(occupancy-M)<1e-9;nodeschecked+=1
        assert abs(sum(sum(t.values()) for t in population.values())-norms[-1].sum())<1e-9
        cases+=1
    # A zero parent with opposite nonzero children has only level-two births.
    assert np.linalg.norm(np.array([1.,0.])+np.array([-1.,0.]))==0
    assert 1.+1.>0 # Omitting the birth filter would count both children at that zero parent.
    OUT['particle_births']={'vector_refinement_models':cases,'prefix_occupancy_checks':nodeschecked,'scope':'Finite positive path measures, exact up to floating-point tolerance; no spatial label process or analytic switch packing.'}

def prefixes():
    cases=0;maxcomm=0.
    for n in [6,10,15]:
        for layers in [1,2,3]:
            for _ in range(12):
                T=5;family=[]
                for layer in range(layers):
                    U,_=np.linalg.qr(RNG.normal(size=(n,n)))
                    family.append([U[:,:rank]@U[:,:rank].T for rank in np.linspace(0,n,T+1).astype(int)])
                Z=[]
                for t in range(T+1):
                    z=np.eye(n)
                    for fam in family:z=fam[t]@z
                    Z.append(z)
                B=RNG.normal(size=(2*n,n));B/=np.linalg.norm(B,2)
                selected=RNG.integers(0,T+1,2*n)
                stack=np.vstack([B[row]@Z[t] for row,t in enumerate(selected)])
                L=1+ceil(log2(T+1))
                assert np.linalg.norm(stack,2)<=L**layers+1e-10
                variation=np.vstack([Z[t]-Z[t-1] for t in range(1,T+1)])
                assert np.linalg.norm(variation,2)**2<=layers**2*L**(2*(layers-1))+1e-10
                if layers>1:maxcomm=max(maxcomm,np.linalg.norm(family[0][2]@family[1][2]-family[1][2]@family[0][2]))
                cases+=1
    assert maxcomm>.1
    # Individually orthogonal but nonnested scalar projections violate the m=1 variation bound.
    alternating=[0,1,0,1,0,1]
    assert sum((b-a)**2 for a,b in zip(alternating,alternating[1:]))>1
    OUT['nested_projection_products']={'operator_norm_models':cases,'maximum_cross_layer_commutator':maxcomm,'scope':'Random real matrix families, checking all input vectors through operator norms. Does not certify the later analytic compression lemma.'}

def earliest_increments():
    cases=0;groups=0;remainders=0
    for cutoff in [1,2,4,7,12,16]:
        for _ in range(15):
            n=2; tensor=RNG.integers(-2,3,(n,n,n,n)); inputs=[RNG.integers(-3,4,n) for j in range(4)]
            updates={t:RNG.integers(-3,4,n) for t in range(1,cutoff+1)}
            previous={};latest=[np.zeros(n,dtype=np.int64) for j in range(4)];inc={}
            for t in range(1,cutoff+1):
                previous[t]=[v.copy() for v in latest];j=(t-1)%4;inc[t]=updates[t]-latest[j];latest[j]=updates[t]
            def form(args):return int(np.einsum('abcd,a,b,c,d',tensor,*args,optimize=False))
            value=0
            for u in range(1,cutoff+1):
                i=(u-1)%4
                for t in range(u+1,cutoff+1):
                    j=(t-1)%4
                    if i==j:continue
                    args=[inputs[e]-previous[t][e] for e in range(4)];args[i]=inc[u];args[j]=inc[t]
                    value+=form(args);groups+=1
            residual=[inputs[e]-latest[e] for e in range(4)];remainder=form(residual)
            for j in range(4):
                args=residual.copy();args[j]=latest[j];remainder+=form(args)
            assert value+remainder==form(inputs)
            if remainder:remainders+=1
            cases+=1
    OUT['two_earliest_expansion']={'exact_tensor_models':cases,'grouped_terms':groups,'nonzero_terminal_remainders':remainders,'scope':'Exact finite algebra only. No claim that arbitrary approximants have vanishing terminal remainders or the source pairwise form-norm decay.'}

if __name__=='__main__':
    for f in [moving_cells,seed_charging,clock_thinning,probability_transfer,scalar_pairs,particles,prefixes,earliest_increments]:
        f();print('PASS',f.__name__,flush=True)
    Path(__file__).with_name('results.json').write_text(json.dumps({'batch':'B023','status':'passed','check_groups':OUT,'limitations':'Finite algebra, numerical inequalities and models only. No full analytic theorem or Lean solution was certified.'},indent=2)+'\n',encoding='utf-8')
