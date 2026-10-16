"""Finite checks of selected combinatorial and constraint-preserving mechanisms."""
import itertools as it
import json
from collections import Counter,defaultdict
from fractions import Fraction as Q
from pathlib import Path
import numpy as np
rng=np.random.default_rng(44016);out={}

maximum=0.
for lam in [.1,.3,.6,.9]:
    P=lam*np.eye(3)+(1-lam)*np.ones((3,3))/3
    for _ in range(8):
        f=rng.uniform(-1,1,(6,3));f-=f.mean(axis=1,keepdims=True)
        variance=0.
        for path in it.product(range(3),repeat=6):
            prob=np.prod([P[path[j],path[j+1]] for j in range(5)])/3
            variance+=prob*(sum(f[j,path[j]] for j in range(6))/6)**2
        C=max(np.mean(v*v) for v in f)
        bound=C*(1+lam)/((1-lam)*6)
        assert variance<=bound+1e-12
        maximum=max(maximum,variance/bound)
out['averaged_walk']={'models':32,'paths_per_model':729,'maximum_bound_ratio':float(maximum),'stationary_initial_state':True}

for _ in range(300):
    X=rng.normal(size=(5,9));c=rng.normal(size=(5,1));kappa=rng.uniform(.05,.95)
    mean=X.mean(axis=1,keepdims=True);AX=(1-kappa)*X+kappa*mean
    F=np.clip(AX+c,-1,1);E=np.linalg.norm(X-F)
    assert np.linalg.norm(X-mean)<=E/kappa+1e-12
    assert 3*np.linalg.norm(mean-np.clip(mean+c,-1,1))<=E/kappa+1e-12
assert np.mean(np.clip([0,3],-1,1))!=np.clip(np.mean([0,3]),-1,1)
out['clipped_consensus']={'models':300,'averaging_clipping_noncommutation_control':True}

graphs=0;words=0;pairs=0
for n in range(1,6):
    for h in it.product(*[range(i,n) for i in range(n)]):
        if any(h[i]>h[i+1] for i in range(n-1)):continue
        edges={(i,j) for i in range(n) for j in range(i+1,h[i]+1)}
        edge=lambda i,j:(min(i,j),max(i,j)) in edges
        counts=Counter()
        for w in it.permutations(range(n)):
            if all(w[i]>w[i+1] or edge(w[i],w[i+1]) for i in range(n-1)):
                inv=sum(edge(w[i],w[j]) and w[i]>w[j] for i in range(n) for j in range(i+1,n))
                counts[inv]+=1;words+=1
        expected=Counter({0:1})
        for a in range(n):
            ell=sum(edge(i,a) for i in range(a));new=Counter()
            for degree,multiplicity in expected.items():
                for j in range(ell+1):new[degree+j]+=multiplicity
            expected=new
        assert counts==expected
        sets=[frozenset(i for i in range(n) if mask>>i&1) for mask in range(1<<n)]
        sets=[I for I in sets if all(not edge(i,j) for i,j in it.combinations(I,2))]
        product=defaultdict(Counter)
        for I,J in it.product(sets,repeat=2):
            omega=sum((1 if i>j else -1) for i in I for j in J if edge(i,j))
            exp=tuple(int(i in I)+int(i in J) for i in range(n))
            product[len(I),len(J)][exp,omega]+=1;pairs+=1
        for (j,k),poly in product.items():assert poly==product[k,j]
        graphs+=1
out['insertion_digits']={'graphs':graphs,'admissible_words':words,'scope':'all natural unit interval graphs through five vertices'}
out['quantum_commutation']={'graphs':graphs,'ordered_independent_set_pairs':pairs,'exact_laurent_coefficients':True}

derivative_error=0.
for _ in range(80):
    cross=rng.normal();negative=-rng.uniform(.1,4);C=np.array([[1.,cross],[cross,negative]])
    eps=rng.uniform(.001,.03);L=1+abs(negative)+cross**2/(1+eps)
    S=np.diag([eps,L]);assert np.linalg.eigvalsh(S+C).min()>0
    t=rng.uniform(.2,.8);x=rng.normal(size=2);cov=S+t*C;inv=np.linalg.inv(cov)
    density=lambda Q:np.exp(-x@np.linalg.solve(Q,x)/2)/(2*np.pi*np.sqrt(np.linalg.det(Q)))
    analytic=.5*(x@inv@C@inv@x-np.trace(inv@C))*density(cov)
    step=1e-5;numeric=(density(cov+step*C)-density(cov-step*C))/(2*step)
    derivative_error=max(derivative_error,abs(analytic-numeric))
    assert abs(analytic-numeric)<1e-7
    assert abs(S[0,0]-eps)<1e-12
out['indefinite_gaussian_path']={'models':80,'maximum_derivative_error':float(derivative_error),'scope':'covariance positivity and heat identity; no cutoff-limit test'}

nu={(-1,0):Q(1,2),(0,0):Q(-1),(1,0):Q(1,2)}
for _ in range(100):
    d={(i,j):Q(int(rng.integers(-8,9)),int(rng.integers(1,10))) for i in range(-2,3) for j in range(-2,3)}
    mu=defaultdict(Q)
    for a,v in nu.items():
        for b,w in d.items():mu[a[0]+b[0],a[1]+b[1]]+=v*w
    assert sum(mu.values())==0
    assert all(sum(v*a[k] for a,v in mu.items())==0 for k in range(2))
    for j in range(-2,3):assert sum(v for a,v in mu.items() if a[1]==j)==0
    for i,j in it.product(range(2),repeat=2):
        assert sum(v*a[i]*a[j] for a,v in mu.items())==(sum(d.values()) if i==j==0 else 0)
out['exact_convolution_constraints']={'rational_models':100,'scope':'moments and quotient cancellation; no asymptotic small-negative-part certification'}

intervals=0
for n in range(5,10):
    for _ in range(5):
        x=np.arange(n,dtype=float);y=rng.normal(size=n)
        slopes=sorted((y[j]-y[i])/(x[j]-x[i]) for i in range(n) for j in range(i+1,n))
        assert min(np.diff(slopes))>1e-10
        reps=[slopes[0]-1]+[(a+b)/2 for a,b in zip(slopes,slopes[1:])]+[slopes[-1]+1]
        orders=[np.argsort(y-s*x) for s in reps]
        for k in range(1,n):
            marks=[set(order[:k]) for order in orders]
            for _ in range(25):
                start=int(rng.integers(0,len(marks)-1));end=int(rng.integers(start+1,len(marks)))
                active=set().union(*(marks[j]^marks[j+1] for j in range(start,end)))
                if not active:continue
                b=len(active)
                if b<4:assert len(marks[start]-marks[end])>=1
                else:
                    c=b//4;unmarked=len(active-marks[start]);rank=k+c if 2*unmarked>=b else k-c
                    assert 0<=rank<=n
                    assert len(set(orders[start][:rank])-set(orders[end][:rank]))>=c
                intervals+=1
out['activity_to_endpoint']={'configurations':25,'intervals':intervals,'scope':'generic sampled sweeps, not uniform activity packing'}

models=0
for q in range(4,50):
    a=4/3;epsilon=np.log(2)/(2*np.log(q));beta=a-epsilon
    assert abs(q**a/2/q**beta-1/np.sqrt(2))<1e-12
    for N in range(4*q,8*q):
        b=N//q-1
        assert N/(2*q)<=b<N/q and b+1<=N/q
        assert q**a/4+1<=q**a/2
        models+=1
out['fixed_scale_power_gain']={'rounding_models':models,'fixed_scales':46,'scope':'conditional recurrence arithmetic; packing hypothesis not tested'}
result={'batch':'B044','status':'passed','scope':'Eight finite groups only. No PCP, elementary positivity, Ramsey classification or halving-line theorem certified.','checks':out}
Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
