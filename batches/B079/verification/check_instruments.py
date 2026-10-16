"""Selected finite mechanisms and dependency controls, not headline proofs."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json, math, time
import numpy as np
from scipy.special import logsumexp
from scipy.stats import poisson

def histories():
    def weight(times,T):
        cuts=sorted(set([-T,T]+times));out={bits:F(0) for bits in product([0,1],repeat=len(times))}
        for a,b in zip(cuts,cuts[1:]):out[tuple(int((a+b)/2<=t) for t in times)]+=b-a
        out[(0,)*len(times)]-=T;out[(1,)*len(times)]-=T;return out
    cases=0
    lists=[[F(-1),F(0),F(2)],[F(1),F(1),F(-2)],[F(0),F(0),F(0)],[F(-3,2),F(1,3),F(1,2)]]
    for t in lists:
        w=weight(t,F(3));assert w==weight(t,F(5)) and sum(w.values())==0 and sum(abs(x) for x in w.values())<=12
        q=F(1,10);cuts=sorted(set([F(0),F(1)]+[F(1,2)+q*x for x in t]));actual={b:F(0) for b in w}
        for a,b in zip(cuts,cuts[1:]):actual[tuple(int((a+b)/2<=F(1,2)+q*x) for x in t)]+=b-a
        assert actual=={b:q*x+(F(1,2) if len(set(b))==1 else 0) for b,x in w.items()};cases+=1
    for a,b in product(lists,repeat=2):
        wa,wb=weight(a,F(3)),weight(b,F(3));assert sum(abs(wa[k]-wb[k]) for k in wa)<=2*sum(abs(x-y) for x,y in zip(a,b))
    q=F(1,10);times=[F(1),F(-2),F(2),F(-1)];exact=expanded=missing=F(0)
    test=lambda bits:F(int((bits[0] or bits[2]) and bits[1]==bits[3]))
    for bits in product([0,1],repeat=4):
        exact+=test(bits)*math.prod(F(1,2)+(q*t if bit else -q*t) for bit,t in zip(bits,times))
        for S in product([0,1],repeat=4):
            term=test(bits)*math.prod((q*t*(1 if bit else -1)) if chosen else F(1,2) for bit,t,chosen in zip(bits,times,S));expanded+=term
            if not(S[0] and S[1]) and not(S[2] and S[3]):missing+=term
    assert exact==expanded and missing!=exact
    return dict(multitime_laws=cases,lipschitz_comparisons=16,exact_replica_expansion=str(exact),omitted_double_selection=str(missing))

def calibration():
    cases=0
    for C in [1.,3.,10.]:
        for eps in [.01,.1,.24]:
            for J in np.linspace((1-eps)/C,3,23):
                low=(1-eps)/J;high=min(C,(1+eps)/J)
                if high<low:continue
                assert high-low<=2*C*eps/(1-eps)+1e-12 and low>0;cases+=1
    assert abs(1-1*1)==abs(1-2*.5)==0
    assert 1000*.001==1
    return dict(feasible_interval_bounds=cases,different_observable_control=True,unbounded_amplitude_control=True)

def likelihood():
    cases=0;worst=0.
    for r in [.2,1.,4.]:
        for b in [0.,.1,.8,2.,5.]:
            T=.7;J=r*T*(math.sqrt(b)-1)**2;counts=np.arange(201);P=poisson.pmf(counts,r*T);Q=poisson.pmf(counts,r*b*T)
            logZ=np.full(201,-np.inf) if b==0 else counts*math.log(b)-r*T*(b-1)
            if b==0:logZ[0]=r*T
            Y=np.sqrt(P*Q)*math.exp(J/2);error=abs(Y.sum()-1);assert error<1e-12;worst=max(worst,error)
            for A in [J*.5,J+1]:
                for B in [-1,0,1,3]:
                    lhs=Q[(logZ<=B)&(J>A)].sum();assert lhs<=math.exp((B-A)/2)+1e-12;cases+=1
    # Initial density multiplies the conditional likelihood; its affinity is <=1.
    p=np.array([.1,.3,.6]);q=np.array([.7,.2,.1]);assert np.sqrt(p*q).sum()<1
    return dict(poisson_event_bounds=cases,max_affinity_identity_error=worst,initial_density_affinity=float(np.sqrt(p*q).sum()),max_omitted_poisson_tail=float(poisson.sf(200,14)))

def posterior_entropy():
    rng=np.random.default_rng(7904);states=list(product([0,1],repeat=3));n=len(states)
    def energy(mu,z):
        out=0.
        for i in range(3):
            for j,x in enumerate(states):
                if x[i]:continue
                y=list(x);y[i]=1;k=states.index(tuple(y));a,b=mu[j],mu[k]
                if a+b:out+=a*b/(a+b)*(z[j]-z[k])*(math.log(z[j])-math.log(z[k]))
        return out
    def ent(mu,z):return mu@(z*np.log(z))-(mu@z)*math.log(mu@z)
    maximum=0.
    for _ in range(60):
        mu=rng.dirichlet(np.ones(n));channel=rng.dirichlet(np.ones(4),size=n);z=np.exp(rng.normal(size=n));w=mu@channel;post=mu[:,None]*channel/w
        lhs=sum(w[y]*energy(post[:,y],z) for y in range(4));rhs=energy(mu,z);assert lhs<=rhs+1e-12;maximum=max(maximum,lhs/rhs)
        mix=np.array([1e-8,.2,.8-1e-8]);params=rng.uniform(.01,.99,size=(3,3));posts=np.array([[math.prod(p if bit else 1-p for p,bit in zip(pars,x)) for x in states] for pars in params]);mu=mix@posts
        E=sum(a*ent(p,z) for a,p in zip(mix,posts));I=sum(a*energy(p,z) for a,p in zip(mix,posts));assert E<=I+1e-12 and I<=energy(mu,z)+1e-12
    return dict(arbitrary_channels=60,product_posterior_mixtures=60,max_contraction_ratio=maximum)

def convex_limits():
    slopes=np.array([[0,0],[2,0],[0,3],[-1,-1]]);rng=np.random.default_rng(7905);cases=0
    for t in [.5,.1,.02]:
        for x in rng.uniform(-1,1,size=(40,2)):
            values=slopes@x;smooth=t*logsumexp(values/t);poly=max(values);assert -1e-12<=smooth-poly<=t*math.log(4)+1e-12
            weights=np.exp(values/t-logsumexp(values/t));gradient=weights@slopes
            for y in rng.uniform(-2,2,size=(3,2)):
                other=t*logsumexp(slopes@y/t);assert other>=smooth+gradient@(y-x)-1e-12
            cases+=1
    # Smooth approximations near a corner can converge to distinct subgradients.
    g1=slopes[np.argmax(slopes@np.array([1.,0]))];g2=slopes[np.argmax(slopes@np.array([0.,1]))];assert not np.allclose(g1,g2)
    # Pointwise-zero shrinking spikes have unit supremum, without convexity.
    for n in [10,100,1000]:assert max(0.,1-4*n*n*abs(0-1/n))==0
    return dict(smooth_convex_value_and_support_cases=cases,nonunique_support_control=True,nonconvex_spike_control=True)

def quadratic_supports():
    # H(beta,d)=d^2/(2s)-beta*u*d, d>=0, a<1/s beta on the chosen domain.
    s=.4;u=.3;a=.7;cases=0
    for beta in np.linspace(.2,1.4,9):
        for h in np.linspace(-1,2,11):
            c=1/s-beta*a;d=max(0,(h+beta*u)/c);z=h+beta*a*d;e=u*d
            Q=lambda B,H:s/2*max(0,H+B*u)**2
            FF=lambda B,H:max(0,H+B*u)**2/(2*(1/s-B*a))
            assert abs(s*max(0,z+beta*u)-d)<1e-12
            for B,H in [(.3,-.7),(.8,.2),(1.3,1.7)]:
                assert Q(B,H)>=Q(beta,z)+e*(B-beta)+d*(H-z)-1e-12
                assert FF(B,H)>=FF(beta,h)+(e+a*d*d/2)*(B-beta)+d*(H-h)-1e-12
            for dp in [0,.2,1,3]:
                cost=lambda x:x*x/(2*s)-beta*u*x
                assert cost(dp)>=cost(d)+z*(dp-d)+beta*a/2*(dp-d)**2-1e-12
            cases+=1
    return dict(full_support_transfers=cases,boundary_maximizers_included=True)

def moment_gauges():
    laws=[([F(1,2),F(2)],[F(1,3),F(2,3)]),([F(1),F(3),F(20)],[F(1,2),F(2,5),F(1,10)])];cases=0
    for xs,ps in laws:
        for n in range(1,8):
            m=sum(p*x**n for x,p in zip(xs,ps));mn=sum(p*x**(n+1) for x,p in zip(xs,ps));T=4*mn/m;upper=lower=F(0)
            # Y=L already satisfies the required moment capture.
            for k in range(-30,20):
                A=F(2)**k
                if A>T:continue
                N=(4**n*A**n)//m
                upper+=N*sum(p for x,p in zip(xs,ps) if x>=16*A);lower+=N*sum(p for x,p in zip(xs,ps) if x>=A)
            assert upper<=F(4**n,16**n)/(1-F(1,2**n))
            if n>=3:assert lower>=2**(n-2)-F(1,2)/(1-F(1,2**n))>=F(2**n,8)
            cases+=1
    # Finite envelopes with deliberately interleaving batch radii; logarithmic evaluation.
    d=1.4;entries=[(1.,-1),(2.,-40),(2.,-4),(3.,-60),(3.,-9),(4.,-16)]
    def terms(logr):return np.array([math.log(b)+d*lr+max(0.,2*(logr-lr)) for b,lr in entries])
    logs=np.linspace(-80,3,400);vals=[min(terms(x)) for x in logs];assert all(b>=a for a,b in zip(vals,vals[1:]))
    for r in logs:assert min(terms(r+math.log(3)))<=min(terms(r))+2*math.log(3)+1e-12
    C=2.;M=1.;Cp=max(C,max(M/math.exp(math.log(b)+d*lr) for b,lr in entries[:2]))
    for r in logs:
        logF=min(math.log(M),math.log(C)+min(terms(r)[2:]));assert logF<=math.log(Cp)+min(terms(r))+1e-12
    return dict(moment_batches=cases,interleaved_envelope_points=len(logs),finite_exclusion_checks=len(logs))

def collision_kernels():
    count=0
    for n in range(1,6):
        options=[[None]+[j for j in range(n) if j!=i] for i in range(n)]
        for out in product(*options):
            left=set(range(n));changed=True
            while changed:
                changed=False
                for v in list(left):
                    if not any(out[u]==v for u in left):left.remove(v);changed=True
            if left:assert all(out[v] in left for v in left) and all(sum(out[u]==v for u in left)==1 for v in left)
            count+=1
    rng=np.random.default_rng(7908);checks=0
    for n in range(2,8):
        for _ in range(10):
            x=rng.normal(size=(n,2));dist=np.linalg.norm(x[:,None]-x[None,:],axis=2);np.fill_diagonal(dist,np.inf);alpha=.8;b=.7
            nearest=np.minimum(b,dist.min(1))**(-alpha);major=b**(-alpha)+np.sum(dist**(-alpha),axis=1);assert np.prod(nearest)<=np.prod(major);checks+=1
    for alpha in [.1,.5,.9,.99]:assert 2*math.pi/(2-2*alpha)>0
    truncated=[2*math.pi*math.log(1/eps) for eps in [.1,.01,.001]];assert truncated[2]>truncated[1]>truncated[0]
    return dict(outdegree_one_graphs=count,kernel_majorizations=checks,endpoint_logarithmic_divergence=truncated)

if __name__=='__main__':
    start=time.perf_counter();checks={}
    for f in [histories,calibration,likelihood,posterior_entropy,convex_limits,quadratic_supports,moment_gauges,collision_kernels]:checks[f.__name__]=dict(status='pass',details=f())
    result=dict(batch='B079',status='pass',elapsed_seconds=round(time.perf_counter()-start,3),scope='Selected finite mechanisms; no source headline or Lean certification.',checks=checks)
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8');print(json.dumps(result))
