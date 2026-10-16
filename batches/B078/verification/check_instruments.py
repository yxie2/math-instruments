"""Finite checks of selected mechanisms; no source headline certification."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import math
import time
import numpy as np
from scipy.optimize import linprog
from numpy.polynomial.hermite import hermgauss


def conditional_coupling():
    rng=np.random.default_rng(7801);states=list(product([0,1],repeat=3));n=len(states)
    bad=np.array([not all(a<=b for a,b in zip(x,y)) for x in states for y in states],float)
    A=[]
    for i in range(n):
        row=np.zeros((n,n));row[i,:]=1;A.append(row.ravel())
    for j in range(n):
        row=np.zeros((n,n));row[:,j]=1;A.append(row.ravel())
    lower=np.zeros((n,n));upper=np.zeros((n,n))
    for i,x in enumerate(states):
        lo=[j for j,y in enumerate(states) if all(b<=a for a,b in zip(x,y))]
        hi=[j for j,y in enumerate(states) if all(b>=a for a,b in zip(x,y))]
        lower[i,lo]=1/len(lo);upper[i,hi]=1/len(hi)
    cases=0;maximum=0.
    for _ in range(12):
        p=rng.dirichlet(np.ones(2*n)).reshape(2,n);c=p[1].sum();lam=p[1]/c@lower
        failures=[];distances=[]
        for mix in [0,.01,.1,.5,1]:
            q=(1-mix)*p+mix*rng.dirichlet(np.ones(2*n)).reshape(2,n)
            if mix==1:q[0]+=q[1];q[1]=0
            mu=q[1]/q[1].sum()@upper if q[1].sum()>0 else rng.dirichlet(np.ones(n))
            sol=linprog(bad,A_eq=A,b_eq=np.r_[lam,mu],bounds=(0,None),method='highs');assert sol.success
            coupling=sol.x.reshape(n,n)
            assert np.max(abs(coupling.sum(1)-lam))<1e-9 and np.max(abs(coupling.sum(0)-mu))<1e-9
            d=abs(p-q).sum()/2;failure=sol.fun
            if d<=c/2:
                cond=abs(p[1]/c-q[1]/q[1].sum()).sum()/2
                assert cond<=4*d/c+1e-10 and failure<=cond+1e-10
            failures.append(failure);distances.append(d);cases+=1;maximum=max(maximum,failure)
        assert np.mean(failures)<=6/c*np.mean(distances)+1e-10
    return dict(environment_couplings=cases,maximum_order_failure=maximum,zero_conditioning_event_included=True)


def scale_errors():
    L=2.;c=.7;cases=0;values=[]
    for K in [32,64,128,256,512,1024]:
        j=np.arange(K);X=1/np.log(j+2);weights=L**(c*(j+1-K));S=X@weights+1/math.log(K+2);values.append(S)
        for N in [1,3,9,20]:
            bound=X[:N]@weights[:N]+X[N:].max()/(1-L**(-c))+1/math.log(K+2)
            assert S<=bound+1e-12;cases+=1
    assert all(a>b for a,b in zip(values,values[1:]))
    constant=sum(2**(.7*(j+1-100)) for j in range(100))+1;assert constant>3
    pure=np.array([.5,.5]);laws=np.eye(2)
    averaged=abs(laws.mean(0)-pure).sum()/2;quenched=abs(laws-pure).sum(1).mean()/2
    assert averaged==0 and quenched==.5
    return dict(early_tail_bounds=cases,nonsummable_sequence_values=values,constant_error_control=constant,averaged_tv=averaged,expected_quenched_tv=quenched)


def departure_rows():
    types=[F(1,5),F(4,5)];cases=0
    def weight(word,env):
        value=F(1)
        for x,y in zip(word,word[1:]):value*=env[x] if y==x+1 else 1-env[x]
        return value
    for first,second in [([0,1,0,1],[2,1]),([0,1],[1,2,1,2]),([-2,-1,-2,-1],[0,-1])]:
        dep1=set(first[:-1]);dep2=set(second[:-1]);assert dep1.isdisjoint(dep2)
        sites=sorted(dep1|dep2);joint=a=b=F(0)
        for rows in product(types,repeat=len(sites)):
            env=dict(zip(sites,rows));w1=weight(first,env);w2=weight(second,env);prob=F(1,2**len(sites));joint+=prob*w1*w2;a+=prob*w1;b+=prob*w2;cases+=1
        assert joint==a*b
    repeat=sum(t*t for t in types)/2;fresh=(sum(types)/2)**2;assert repeat!=fresh
    # First arrival at 1: the event's likelihood uses only row 0.
    for t in types:
        conditional=sum(s*F(1,4) for s in types)/sum(F(1,4) for s in types)
        assert conditional==sum(types)/2
    return dict(exact_environment_assignments=cases,repeated_row_second_moment=str(repeat),incorrect_fresh_row_product=str(fresh))


def positive_trials():
    cases=0
    for m in range(1,8):
        choices=[F(1,100),F(1,3),F(9,10)];exact=F(0)
        for row in product(choices,repeat=m):exact+=math.prod(row)*F(1,3**m)
        assert exact==(sum(choices)/3)**m;cases+=1
    for q in [1e-2,1e-5,1e-12]:
        r=math.ceil(20/q);failure=math.exp(r*math.log1p(-q));assert failure<=math.exp(-20)*(1+1e-12)
    assert (1-0.)**100000==1
    return dict(fresh_column_lengths=cases,smallest_positive_probability=1e-12,zero_probability_control=True)


def bounded_reweighting():
    p=np.array([.2,.3,.5]);fields=np.array([[.5,1.1,1.8],[1.8,.7,.5]]);env=np.array([.4,.6]);cases=0
    for j in range(5):
        explicit=0.
        for w,A in zip(env,fields):
            for word in product(range(3),repeat=j):explicit+=w*math.prod(p[i]*A[i] for i in word)
        same=sum(w*(p@A)**j for w,A in zip(env,fields));assert abs(explicit-same)<1e-12;cases+=1
    shared=sum(w*(p@A)**2 for w,A in zip(env,fields));refreshed=(env@(fields@p))**2;assert abs(shared-refreshed)>.001
    # Geometric expansion around C: uniform approximation of 1/z and its square.
    z=np.linspace(.5,1.8,301);C=1.8;u=1-z/C
    for N in [10,40,100]:
        inv=sum(u**j for j in range(N+1))/C;bound=(1-.5/C)**(N+1)/.5
        assert np.max(abs(inv-1/z))<=bound+2e-14
        assert np.max(abs(inv**2-1/z**2))<=4*bound+2e-14
    nodes,weights=hermgauss(24);nodes*=math.sqrt(2);weights/=math.sqrt(math.pi)
    values=[]
    for eps in [1,.1,.01,.001,0]:
        val=sum(a*b*math.tanh(x)*math.tanh(math.sqrt(1-eps)*x+math.sqrt(eps)*y) for x,a in zip(nodes,weights) for y,b in zip(nodes,weights));values.append(val)
    assert abs(values[-2]-values[-1])<abs(values[1]-values[-1])
    return dict(extra_replica_expansions=cases,same_field_second_moment=shared,refreshed_field_second_moment=refreshed,singular_covariance_values=values)


def gaussian_calculus():
    rng=np.random.default_rng(7806);n=3;checks=0;worst=0.
    for r in [1,2]:
        Ftest=rng.normal(size=(n,)*r);h=rng.normal(size=n);base=rng.dirichlet(np.ones(n));Delta=rng.normal(size=(n,n));Delta=(Delta+Delta.T)/2
        def observable(x):
            p=base*np.exp(x);p/=p.sum()
            return sum(Ftest[word]*math.prod(p[i] for i in word) for word in product(range(n),repeat=r))
        p=base*np.exp(h);p/=p.sum();rhs=0.
        for word in product(range(n),repeat=r+2):
            bracket=sum(Delta[word[a],word[b]] for a in range(r) for b in range(r))-2*r*sum(Delta[word[a],word[r]] for a in range(r))+r*(r+1)*Delta[word[r],word[r+1]]-r*Delta[word[r],word[r]]
            rhs+=.5*math.prod(p[i] for i in word)*Ftest[word[:r]]*bracket
        step=2e-4;H=np.zeros((n,n));value=observable(h)
        for i in range(n):
            ei=np.eye(n)[i]*step;H[i,i]=(observable(h+ei)-2*value+observable(h-ei))/step**2
            for j in range(i):
                ej=np.eye(n)[j]*step;H[i,j]=H[j,i]=(observable(h+ei+ej)-observable(h+ei-ej)-observable(h-ei+ej)+observable(h-ei-ej))/(4*step**2)
        error=abs(.5*np.sum(Delta*H)-rhs);worst=max(worst,error);assert error<2e-7
        assert abs(rhs)<=(2*r*r+r)*abs(Ftest).max()*abs(Delta).max()+1e-12;checks+=1
    nodes,weights=hermgauss(40);nodes*=math.sqrt(2);weights/=math.sqrt(math.pi);p0=np.array([.3,.7]);C0=np.array([[.3,.05],[.05,.5]]);C1=np.array([[.8,.15],[.15,.4]]);D=C1-C0
    def integrate(t):
        C=(1-t)*C0+t*C1;L=np.linalg.cholesky(C);value=derivative=0.;mom=np.zeros(4)
        for x,a in zip(nodes,weights):
            for y,b in zip(nodes,weights):
                h=L@np.array([x,y]);z=p0@np.exp(h);p=p0*np.exp(h)/z;w=a*b
                value+=w*math.log(z);derivative+=w*.5*(p@np.diag(D)-p@D@p)
                mom+=w*np.array([z,z*z,1/z,1/z**2])
        return value,derivative,mom
    t=.43;val,rhs,mom=integrate(t);diff=(integrate(t+1e-4)[0]-integrate(t-1e-4)[0])/2e-4;assert abs(diff-rhs)<1e-8
    K=max(np.diag((1-t)*C0+t*C1));assert np.all(mom<=np.exp(np.array([1,4,1,4])*K/2)+1e-10)
    return dict(replica_hessian_cases=checks,max_hessian_error=worst,quadrature_derivative_error=abs(diff-rhs),partition_moments=mom.tolist())


def components(n,edges,opened):
    parent=list(range(n))
    def root(i):
        while i!=parent[i]:i=parent[i]
        return i
    for k in opened:
        a,b=edges[k];parent[root(a)]=root(b)
    return [root(i) for i in range(n)]


def rc_conditioning():
    edges=[(0,1),(0,1),(1,2),(2,2),(2,3),(3,0)];odds=[F(1,2),F(2),F(3,2),F(2,3),F(3),F(4,5)];cases=0
    def law(n,es,vs,q):
        d={}
        for bits in product([0,1],repeat=len(es)):
            opened=[i for i,b in enumerate(bits) if b];d[bits]=q**len(set(components(n,es,opened)))*math.prod(vs[i] for i in opened)
        Z=sum(d.values());return {b:w/Z for b,w in d.items()}
    for q in [F(1,4),F(1),F(2),F(4)]:
        full=law(4,edges,odds,q)
        for fixed in [{0:1,2:0},{0:0,3:1},{0:1,1:1,4:0}]:
            rem=[i for i in range(len(edges)) if i not in fixed];roots=components(4,edges,[i for i,b in fixed.items() if b]);unique=sorted(set(roots));mapped=[unique.index(r) for r in roots]
            quotient=law(len(unique),[(mapped[edges[i][0]],mapped[edges[i][1]]) for i in rem],[odds[i] for i in rem],q)
            keep={tuple(bits[i] for i in rem):w for bits,w in full.items() if all(bits[i]==b for i,b in fixed.items())};Z=sum(keep.values())
            assert all(w/Z==quotient[b] for b,w in keep.items());cases+=1
        # Decision leaf: inspect edge 0, then edge 2 only if 0 is open.
        leaf={bits:w for bits,w in full.items() if bits[0] and not bits[2]};Z=sum(leaf.values());p4=sum(w for bits,w in leaf.items() if bits[4])/Z
        assert 0<p4<1
        hidden={bits:w for bits,w in leaf.items() if bits[4]};assert sum(hidden.values())>0
        assert sum(w for bits,w in hidden.items() if bits[4])/sum(hidden.values())==1!=p4
    # A wire between 1 and 2 connects 0 to 3 in the quotient but not physically.
    es=[(0,1),(2,3)];roots=components(4,es,[0,1]);assert roots[0]!=roots[3]
    wired=components(4,es+[(1,2)],[0,1,2]);assert wired[0]==wired[3]
    return dict(exact_quotient_laws=cases,adaptive_leaf_hidden_event_controls=4,wiring_shortcut_control=True)


def planar_loops():
    coords=[(0,0),(1,0),(1,1),(0,1),(-1,0)];edges=[(0,1),(1,2),(2,3),(3,0),(0,2),(0,4)];dual=[(0,2),(0,2),(1,2),(1,2),(0,1),(2,2)];cases=0
    def loops(opened):
        rotation={};isolated=0
        for v in range(5):
            darts=[2*i+(edges[i][1]==v) for i in opened if v in edges[i]]
            if not darts:isolated+=1;continue
            def angle(d):
                a,b=edges[d//2];u=b if d%2==0 else a;return math.atan2(coords[u][1]-coords[v][1],coords[u][0]-coords[v][0])
            darts.sort(key=angle)
            for a,b in zip(darts,darts[1:]+darts[:1]):rotation[a]=b
        unseen=set(rotation);count=isolated
        while unseen:
            d=next(iter(unseen));count+=1
            while d in unseen:unseen.remove(d);d=rotation[d^1]
        return count
    odds=[F(1,2),F(2),F(3),F(2,5),F(4,3),F(7,4)]
    for bits in product([0,1],repeat=6):
        A=[i for i,b in enumerate(bits) if b];Ac=[i for i,b in enumerate(bits) if not b];k=len(set(components(5,edges,A)));kd=len(set(components(3,dual,Ac)))
        assert loops(A)==2*k+len(A)-5 and kd==len(A)-5+k+1
        for q in [F(1,4),F(1),F(2),F(4)]:
            w=q**k*math.prod(odds[i] for i in A);wd=q**kd*math.prod(q/odds[i] for i in Ac)
            assert wd/w==q**(6-5+1)/math.prod(odds);cases+=1
    return dict(loop_configurations=64,heterogeneous_duality_checks=cases,bridge_dual_loop_included=True)


if __name__=='__main__':
    start=time.perf_counter();checks={}
    for f in [conditional_coupling,scale_errors,departure_rows,positive_trials,bounded_reweighting,gaussian_calculus,rc_conditioning,planar_loops]:checks[f.__name__]=dict(status='pass',details=f())
    result=dict(batch='B078',status='pass',elapsed_seconds=round(time.perf_counter()-start,3),scope='Finite selected mechanisms and dependency controls; no headline or Lean certification.',checks=checks)
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8');print(json.dumps(result))
