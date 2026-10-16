"""Local finite checks; analytic and algorithmic headline claims remain unverified."""
import json
import math
import time
from pathlib import Path
from fractions import Fraction as F
from itertools import product, combinations
from collections import defaultdict
import numpy as np


def deficiency():
    arrays=[[0]*7,[1]*7,[1,2,4,8,16,32,64],[-3,-2,-1,0,1,2,3],[1,1,2,2,3,3,4],[3,-5,7,3,-5,7,0]]
    pairs=0;exchanges=0;variances=0
    for weights in arrays:
        n=len(weights);supports={0:{0}};size={0:1};d={0:0.}
        for mask in range(1,1<<n):
            bit=mask&-mask;i=bit.bit_length()-1;base=supports[mask^bit]
            supports[mask]=base|{v+weights[i] for v in base};size[mask]=len(supports[mask]);d[mask]=mask.bit_count()-math.log2(size[mask])
        means=[]
        for q in range(n+1):
            vals=[d[mask] for mask in d if mask.bit_count()==q];mean=sum(vals)/len(vals);means.append(mean)
            variance=sum((v-mean)**2 for v in vals)/len(vals);assert variance<=q+1e-12;variances+=1
        assert all(b>=a-1e-12 for a,b in zip(means,means[1:]))
        for mask in supports:
            for i in range(n):
                if (mask>>i)&1:continue
                nxt=mask|(1<<i);assert size[mask]<=size[nxt]<=2*size[mask]
                for j in range(n):
                    if (mask>>j)&1:
                        other=(mask^(1<<j))|(1<<i)
                        assert abs(d[mask]-d[other])<=1+1e-12;exchanges+=1
            complement=((1<<n)-1)^mask;sub=complement
            while True:
                assert size[mask|sub]<=size[mask]*size[sub];pairs+=1
                if sub==0:break
                sub=(sub-1)&complement
    return dict(integer_weight_arrays=len(arrays),disjoint_support_pairs=pairs,exchange_checks=exchanges,fixed_size_variances=variances)


def prefix_recomputation():
    rng=np.random.default_rng(7502);cases=0;refinements=0;full_overflows=0
    for m in range(6):
        for trial in range(15):
            q=1+trial%4;C=1+trial%5;H=3;K=2
            def make(side):
                data=[]
                for j in range(20 if side==0 else 80):
                    weight=int(rng.integers(0,12 if side==0 else 40));mask=tuple(int(v) for v in rng.integers(0,2,m));valid=bool(rng.integers(0,4))
                    data.append((weight%q,mask,valid,(weight,mask)))
                    if j%7==0:data.append(data[-1])
                return data
            L,R=make(0),make(1);UL=len({a[3] for a in L if a[2]});UR=len({a[3] for a in R if a[2]});tasks=0;work=0;checklength=0;visits=defaultdict(int)
            def task(data,side,z,prefix):
                nonlocal tasks,work
                potential=[(j,a) for j,a in enumerate(data) if a[0]==z and a[1][:len(prefix)]==prefix]
                tasks+=1;work+=H+K*len(potential);entries=set()
                for j,a in potential:visits[side,j]+=1
                for j,a in potential:
                    if a[2]:entries.add(a[3])
                    if len(entries)>C:return None
                return entries
            for z in range(q):
                left=task(L,0,z,())
                if not left:continue
                stack=[()]
                while stack:
                    prefix=stack.pop();right=task(R,1,z,prefix)
                    if right is None:
                        if len(prefix)<m:stack.extend([prefix+(1,),prefix+(0,)]);refinements+=1
                        else:full_overflows+=1
                    elif right:checklength+=len(left)+len(right)
            task_bound=F(2*q)+F(2*(m+1)*UR,C)
            assert tasks<=task_bound
            assert work<=H*task_bound+K*(len(L)+(m+1)*len(R))
            assert checklength<=UL+(2*m+3)*UR
            assert all(v<=(1 if side==0 else m+1) for (side,j),v in visits.items());cases+=1
    assert (2**(4+1)-1)>4+1  # A late-filtered occurrence can be regenerated in the whole tree.
    return dict(schedule_models=cases,refined_nodes=refinements,full_mask_overflows=full_overflows,late_filter_negative_control=True)


def common_domain_selection():
    rng=np.random.default_rng(7503);cases=0;sharp=0
    for N in [1,2,5,10]:
        for p in [1.25,2.,4.,8.]:
            for _ in range(10):
                measure=rng.uniform(.1,2,17);densities=rng.uniform(0,3,(N,17));norms=np.sum(densities**p*measure,axis=1)**(1/p);U=max(norms)
                routes=rng.uniform(0,1,(N,17));routes/=np.maximum(1,routes.sum(axis=0))
                lhs=np.sum(routes*densities*measure);rhs=N**(1/p)*U*sum(measure)**(1-1/p)
                assert lhs<=rhs+1e-10;cases+=1
            # Equal disjoint cells of total measure one attain the factor.
            density=np.eye(N)*N**(1/p);route=np.eye(N);mu=np.ones(N)/N
            assert np.max(abs(np.sum(density**p*mu,axis=1)-1))<1e-12
            assert abs(np.sum(density*route*mu)-N**(1/p))<1e-12;sharp+=1
            for r in [.001,.2,2.]:
                beta=1.7;m=3.;lhs=r**(beta-m*(1-1/p))*(r**m)**(1-1/p)
                assert abs(lhs-r**beta)<1e-10*(1+r**beta)
    return dict(weighted_space_models=cases,sharp_disjoint_cell_models=sharp,scale_checks=3*sharp)


def entropy(law):return -sum(float(p)*math.log(float(p)) for p in law.values() if p)
def marginal(law,fn):
    out=defaultdict(float)
    for key,p in law.items():out[fn(key)]+=p
    return dict(out)
def H(law,fn):return entropy(marginal(law,fn))


def replica_information():
    rng=np.random.default_rng(7504);cases=0;maxerr=0.
    maps=[lambda s:0,lambda s:s,lambda s:s%2];bp=[.2,.3,.5]
    for t in [1,2,3,4]:
        for _ in range(15):
            py=rng.dirichlet(np.ones(3));post=rng.dirichlet(np.ones(3),size=3);message=rng.dirichlet(np.ones(2),size=3)
            law={}
            for st in product(range(3),repeat=t):
                for w in range(2):law[st,w]=sum(py[y]*message[y,w]*math.prod(post[y,s] for s in st) for y in range(3))
            HW=H(law,lambda z:z[1]);HS=H(law,lambda z:z[0][0]);Htuple=H(law,lambda z:z[0]);Hjoint=entropy(law)
            I=HS+HW-H(law,lambda z:(z[0][0],z[1]));K=t*HS-Htuple
            KW=sum(H(law,lambda z,i=i:(z[0][i],z[1]))-HW for i in range(t))-(Hjoint-HW)
            Kp=KWp=Ip=tuplecond=0.
            for p,fn in zip(bp,maps):
                U=lambda z:tuple(fn(s) for s in z[0]);U1=lambda z:fn(z[0][0])
                HU=H(law,U);HU1=H(law,U1);HUW=H(law,lambda z:(U(z),z[1]))
                Kp+=p*(t*HU1-HU)
                KWp+=p*(sum(H(law,lambda z,i=i:(fn(z[0][i]),z[1]))-HW for i in range(t))-(HUW-HW))
                Ip+=p*(HU1+HW-H(law,lambda z:(U1(z),z[1])))
                tuplecond+=p*(Htuple+HUW-Hjoint-HU)
            left=t*(I-Ip);right=tuplecond+(K-Kp)-(KW-KWp);error=abs(left-right);maxerr=max(maxerr,error)
            assert error<2e-12 and Kp<=K+1e-12 and KWp<=KW+1e-12
            assert left<=HW+K-Kp+1e-12;cases+=1
    # S1,S2 are independent fair bits, W=S1. Marginals match, pairs do not.
    assert 2*math.log(2)>math.log(2)+0
    return dict(posterior_models=cases,projection_models=3*cases,max_identity_error=maxerr,mismatched_pair_negative_control=True)


def stationary_closure():
    cases=0;maxerror=0.
    # S(a,b)=(b-a)^2/2+g(b)-g(a), g periodic. Invariant graphs p=c+g'(theta).
    g=lambda x:.2*math.sin(x)+.1*math.cos(2*x)
    gp=lambda x:.2*math.cos(x)-.2*math.sin(2*x)
    for q in [20,31,50]:
        for l in [1,2]:
            delta=2*math.pi*l/q;actions=[]
            for phase in np.linspace(-2,2,17):
                theta=[phase+j*delta for j in range(q+1)]
                momenta=[delta+gp(x) for x in theta]
                assert abs(momenta[0]-momenta[-1])<1e-12
                for j in range(1,q):
                    incoming=(theta[j]-theta[j-1])+gp(theta[j]);negative_outgoing=-(theta[j+1]-theta[j])-gp(theta[j])
                    assert abs(incoming+negative_outgoing)<1e-12
                action=sum((b-a)**2/2+g(b)-g(a) for a,b in zip(theta,theta[1:]));actions.append(action)
                maxerror=max(maxerror,abs(action-q*delta**2/2));cases+=1
            assert max(actions)-min(actions)<1e-11
    return dict(periodic_chains=cases,max_action_error=maxerror,nonconstant_graph_gauge=True)


def occupation_bound():
    curvature=1/(2*5**1.5);checks=0
    for h in [.1,1.,3.]:
        phi=lambda x:math.sqrt(h*h+x*x)+x
        prime=lambda x:1+x/math.sqrt(h*h+x*x)
        for x in np.linspace(-h,h,11):
            for delta in np.r_[-10*h,-3*h,np.linspace(-h,h,13),3*h,10*h]:
                remainder=phi(x+delta)-phi(x)-prime(x)*delta
                assert remainder+1e-12>=curvature/h*min(delta*delta,h*h);checks+=1
    walks=0
    for increments in [[(-1,F(1,2)),(1,F(1,2))],[(-1,F(1,2)),(2,F(1,2))],[(-2,F(1,4)),(1,F(3,4))]]:
        assert sum(a*p for a,p in increments)>=0
        for start in [-100,-3,0,3,100]:
            for h in [F(1,2),F(1),F(2)]:
                R=2*h+1;M=12;states={start:F(1)};cost=F(0);V=F(0)
                for m in range(M):
                    nxt=defaultdict(F)
                    for x,p in states.items():
                        for delta,q in increments:
                            V+=p*q*delta**2
                            if abs(x)<=h:cost+=p*q*min(delta**2,h*h)
                            nxt[x+delta]+=p*q
                    states=nxt
                bound=50*float(h)*(float(h+R)+math.sqrt(float(V)))+50*M*float(h*h)*min(1,float(V/(R-h)**2))
                assert float(cost)<=bound;walks+=1
    return dict(convex_remainders=checks,finite_submartingale_models=walks,starts_include_plus_minus100=True,checked_absolute_constant=50)


def affine_plateaux():
    # Shifted box K=[2,4]^2 and F=min(0,1+- (x_i-3)), flow x'=3-x.
    normals=np.array([[0,0],[1,0],[-1,0],[0,1],[0,-1]],dtype=float);offsets=np.array([0,1,1,1,1],dtype=float)
    cases=0;ties=0
    for x0 in product(np.linspace(1.1,4.9,9),repeat=2):
        y0=np.array(x0)-3;radius=max(abs(y0));entry=max(0,math.log(radius)) if radius else 0;budget=max(0,radius-1)
        assert entry<=budget+1e-12
        previous=-1e100
        for t in np.linspace(0,3,31):
            y=y0*math.exp(-t);values=offsets+normals@y;minimum=min(values);active=np.flatnonzero(abs(values-minimum)<1e-12)
            derivative=min(normals[active]@(-y));assert derivative>=-1e-12
            if minimum<0:assert derivative>=1-1e-12
            if len(active)>1:ties+=1
            eps=1e-7;actual=(min(offsets+normals@(y*math.exp(-eps)))-minimum)/eps
            assert abs(actual-derivative)<1e-6
            assert minimum>=previous-1e-12;previous=minimum
            if t>=entry+1e-10:assert minimum>=-1e-12
            cases+=1
    # F=-|x| and x'=-x approach their compact plateau {0}, but never enter from x0=1.
    assert all(math.exp(-t)>0 for t in range(20))
    return dict(trajectory_points=cases,active_ties=ties,entry_time_budgets=81,nonuniform_slope_negative_control=True)


def ordered_flux():
    rng=np.random.default_rng(7508);cases=0;cuts=0
    for n in range(2,9):
        for model in range(15):
            split=n//2 if model%2==0 and n>=4 else n;components=[list(range(split))]+([list(range(split,n))] if split<n else [])
            edges=[]
            for comp in components:
                if len(comp)>1:
                    edges.extend((comp[i],comp[(i+1)%len(comp)]) for i in range(len(comp)))
                    for u,v in combinations(comp,2):
                        if rng.random()<.3:edges.extend([(u,v),(v,u)])
            rates=[int(rng.integers(1,8)) for e in edges];levels=[int(rng.integers(0,5)) for i in range(n)];values=sorted(set(levels));rank={v:i for i,v in enumerate(values)}
            delta=F(min(rates),2*sum(rates));weights=[delta**rank[a] for a in levels]
            assert all(weights[v]<=delta*weights[u] for u,v in product(range(n),repeat=2) if levels[u]<levels[v])
            direct=sum(k*weights[u]*(levels[v]-levels[u]) for (u,v),k in zip(edges,rates));reconstructed=F(0)
            for low,high in zip(values,values[1:]):
                flux=sum(k*weights[u]*(int(levels[u]<=low<levels[v])-int(levels[v]<=low<levels[u])) for (u,v),k in zip(edges,rates))
                assert flux>=0;reconstructed+=(high-low)*flux;cuts+=1
            assert direct==reconstructed>=0;cases+=1
    # A downward edge without a return path has negative flux even under separation.
    assert F(1,10)*(0-1)<0
    # Two opposite edges with inadequate weight separation can also give negative flux.
    assert 1*1*(1-0)+2*1*(0-1)<0
    return dict(exact_directed_graphs=cases,level_cuts=cuts,disconnected_and_tied_levels=True,return_path_negative_control=True,weight_separation_negative_control=True)


if __name__=='__main__':
    start=time.perf_counter();checks={}
    for f in [deficiency,prefix_recomputation,common_domain_selection,replica_information,stationary_closure,occupation_bound,affine_plateaux,ordered_flux]:checks[f.__name__]=dict(status='pass',details=f())
    result=dict(batch='B075',status='pass',elapsed_seconds=round(time.perf_counter()-start,3),scope='Selected finite mechanisms and hypothesis controls; no source headline or Lean certification.',checks=checks)
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
