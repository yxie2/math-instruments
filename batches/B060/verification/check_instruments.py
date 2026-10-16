"""Finite checks of selected arguments, not certification of source headlines."""
from fractions import Fraction as F
from itertools import combinations, product, permutations
from functools import lru_cache
from pathlib import Path
import json
import math
import random
import time
import numpy as np
from scipy.optimize import minimize, linprog


def partitions(n):
    def extend(a):
        if len(a)==n:
            yield tuple(a)
        else:
            for j in range(max(a)+2):
                yield from extend(a+[j])
    yield from extend([0])


def rank_edges(n, edges):
    parent=list(range(n))
    def root(x):
        while parent[x]!=x: x=parent[x]
        return x
    for u,v in edges: parent[root(u)]=root(v)
    return n-len({root(x) for x in range(n)})


def isotropic_trees():
    rng=random.Random(174); models=rank_checks=partition_checks=0; error=0.
    for n in (3,4):
        for q in (2,3):
            edges=[]
            for _ in range(q):
                order=rng.sample(range(n),n)
                edges.extend((order[j],order[rng.randrange(j)]) for j in range(1,n))
            inc=np.zeros((n,len(edges)))
            for i,(u,v) in enumerate(edges): inc[u,i]=1; inc[v,i]=-1
            basis=np.linalg.qr(np.column_stack([np.eye(n)[:,i]-np.eye(n)[:,-1] for i in range(n-1)]))[0]
            b=basis.T@inc
            for rho in (.2,.05):
                gamma=1e-5
                def objective(a):
                    w=np.exp(a); matrix=(b*w)@b.T
                    value=np.linalg.slogdet(matrix)[1]-sum(a)/q+gamma*(a@a)
                    leverage=w*np.sum(b*np.linalg.solve(matrix,b),axis=0)
                    return value, leverage-1/q+2*gamma*a
                opt=minimize(objective,np.zeros(len(edges)),jac=True,method='BFGS',options={'gtol':1e-10})
                a=opt.x; w=np.exp(a); matrix=(b*w)@b.T
                val,vec=np.linalg.eigh(matrix)
                z=((vec*val**-.5)@vec.T@b)*np.sqrt(w)
                err=np.linalg.norm(z@z.T-np.eye(n-1)); error=max(error,float(err))
                assert err<1e-10 and np.max(np.sum(z*z,axis=0))<=(1+rho)/q
                for mask in range(1<<len(edges)):
                    ids=[i for i in range(len(edges)) if mask>>i&1]
                    rr=np.linalg.matrix_rank(z[:,ids],tol=1e-9) if ids else 0
                    assert rr==rank_edges(n,[edges[i] for i in ids]); rank_checks+=1
                for ids in (list(range(len(edges))),list(range(q*(n-1)//2)),list(range(0,len(edges),2))):
                    c=max(0.,float(np.linalg.eigvalsh(z[:,ids]@z[:,ids].T)[0]))
                    for p in partitions(n):
                        d=max(p)+1; cross=sum(p[edges[i][0]]!=p[edges[i][1]] for i in ids)
                        assert cross+1e-9>=c*q*(d-1)/(1+rho); partition_checks+=1
                models+=1
    return dict(models=models,subset_ranks=rank_checks,partition_bounds=partition_checks,max_isotropy_error=error)


def mst_separation():
    rng=random.Random(175); cases=layers=0
    for n in (3,4):
        edges=list(combinations(range(n),2)); e=len(edges)
        trees=[t for t in combinations(range(e),n-1) if rank_edges(n,[edges[i] for i in t])==n-1]
        for _ in range(15):
            z=[F(rng.randrange(8),5) for _ in edges]; q=F(rng.randrange(1,9),4)
            deficits=[]
            for p in partitions(n):
                deficits.append(q*max(p)-sum(z[i] for i,(u,v) in enumerate(edges) if p[u]!=p[v]))
            c=np.array([float(x) for x in z]+[-float(q)])
            mat=[]
            for t in trees:
                row=np.zeros(e+1); row[list(t)]=-1; row[-1]=1; mat.append(row)
            opt=linprog(c,A_ub=mat,b_ub=np.zeros(len(mat)),bounds=[(0,1)]*e+[(0,n)],method='highs')
            assert opt.success and abs(-opt.fun-float(max(deficits)))<1e-8
            for _ in range(4):
                ell=[F(rng.randrange(5),4) for _ in edges]; vals=sorted(set([F(0),F(1)]+ell)); integral=F(0)
                for lo,hi in zip(vals,vals[1:]):
                    a=(lo+hi)/2
                    components=n-rank_edges(n,[edge for edge,l in zip(edges,ell) if l<a])
                    integral+=(hi-lo)*(components-1)
                assert integral==min(sum(ell[i] for i in t) for t in trees); layers+=1
            cases+=1
    return dict(linear_programs=cases,exact_kruskal_integrals=layers)


def compression():
    rng=random.Random(176); cases=conditional=0
    for n in (3,4,5):
        for r in (F(1,3),F(2,3)):
            for _ in range(6):
                family=rng.sample(list(range(1,1<<n)),rng.randrange(1,min(9,1<<n)))
                s=max(t.bit_count() for t in family); chosen=[]
                def probability(t):
                    return sum(r**z.bit_count()*(1-r)**(n-z.bit_count()) for z in range(1<<n)
                               if any((z|t)&a==a for a in chosen))
                while True:
                    bad=next((t for t in family if probability(t)<F(1,2)),None)
                    if bad is None: break
                    before=probability(0); chosen.append(bad)
                    assert probability(0)-before>r**s/2
                assert 1<=len(chosen)<=math.ceil(2*r**-s)
                for t in range(1<<n):
                    if any(t&a==a for a in family): assert probability(t)>=F(1,2); conditional+=1
                cases+=1
    return dict(families=cases,smoothed_superset_checks=conditional)


def cutoff():
    rng=random.Random(177); feasible=0; endpoints=set(); ties=0
    for n in range(1,8):
        for _ in range(60):
            w=[rng.randrange(5) for _ in range(n)]
            if not sum(w): w[0]=1
            lam=[F(x,sum(w)) for x in w]; A={i for i in range(n) if rng.randrange(2)}
            d=F(rng.randrange(1,5),5); m=F(rng.randrange(7),5)
            lower=max([lam[i] for i in range(n) if i not in A]+[F(0)])
            def f(u): return sum(min(x,u)*((i in A)-(1-d)) for i,x in enumerate(lam))-m*u
            cuts=sorted(set(lam+[F(0),F(1),lower])); candidates=set(cuts)
            for a,b in zip(cuts,cuts[1:]):
                if f(a)!=f(b):
                    root=a-f(a)*(b-a)/(f(b)-f(a))
                    if a<=root<=b: candidates.add(root)
            admissible=[u for u in candidates if u>=lower and f(u)>=0]
            if not admissible: continue
            eps=max(admissible); R={i for i,x in enumerate(lam) if x>eps}
            assert R<=A and len(R)*d<=m
            feasible+=1; endpoints.add(str(eps)); ties+=sum(x==eps for x in lam)>1
    assert '0' in endpoints and '1' in endpoints
    return dict(feasible_piecewise_linear_instances=feasible,tied_cutoffs=ties,zero_and_one_endpoints=True)


def pair_cover():
    edges=[3,5,10]; n=4; r=2; m=2; rho=F(1,2); pi=F(1,3); cases=0
    for T in (F(1,2),F(1),F(2)):
        degree={i:sum(e&i==i for e in edges)*rho**(r-i.bit_count()) for i in range(1<<n) if i.bit_count()<=r}
        c0={i for i in degree if degree[i]>T}; regular=[e for e in edges if not any(e&i==i for i in c0)]
        pairs=list(product(regular,repeat=2)); tuples=list(permutations(regular,m)); expected1=expected2=F(0)
        for mask in range(1<<len(pairs)):
            selected={pair for j,pair in enumerate(pairs) if mask>>j&1}
            c1={a|b for a,b in selected}
            c2={a|b for a,b in tuples if not any(pair in selected for pair in product((a,b),repeat=2))}
            for S in range(1<<n):
                if sum(S&e==e for e in edges)>=m: assert any(S&i==i for i in c0|c1|c2)
            prob=pi**mask.bit_count()*(1-pi)**(len(pairs)-mask.bit_count())
            expected1+=prob*sum(rho**i.bit_count() for i in c1)
            expected2+=prob*sum(rho**i.bit_count() for i in c2); cases+=1
        assert expected1<=pi*sum(rho**(a|b).bit_count() for a,b in pairs)
        assert expected2<=(1-pi)**(m*m)*sum(rho**(a|b).bit_count() for a,b in tuples)
        for B in range(1<<n):
            assert sum(rho**(e&~B).bit_count() for e in regular)<=T*sum(math.comb(B.bit_count(),i) for i in range(min(r,B.bit_count())+1))
    for h in range(64,513):
        assert 4*h+13*h*h+1<=18*h*h<=18*2**(2*h)<=2**(4*h)
    return dict(exhaustive_sampling_outcomes=cases,constant_regimes=449,scope='Small analogues test the exact mechanism; h>=64 instances are not enumerated.')


def read_k():
    rng=np.random.default_rng(184); cases=tail_checks=0
    states=np.array(list(product((0,1),repeat=5)))
    for _ in range(30):
        probs=rng.uniform(.15,.85,5); law=np.prod(np.where(states,probs,1-probs),axis=1)
        supports=[rng.choice(5,size=int(rng.integers(1,4)),replace=False).tolist() for _ in range(6)]
        values=[]; lengths=[]
        for ids in supports:
            table=rng.normal(size=2**len(ids)); indices=states[:,ids]@(2**np.arange(len(ids)))
            values.append(table[indices]); lengths.append(np.ptp(table))
        values=np.array(values); centered=np.sum(values,axis=0)-sum(values@law)
        p=max(sum(i in s for s in supports) for i in range(5))+.5
        for a in np.linspace(.05,max(abs(centered))+.1,15):
            bound=np.exp(-2*a*a/(p*sum(x*x for x in lengths)))
            assert sum(law[centered>=a])<=bound+1e-12
            assert sum(law[centered<=-a])<=bound+1e-12; tail_checks+=2
        cases+=1
    assert .5>math.exp(-2*5**2/10)
    return dict(models=cases,one_sided_tail_checks=tail_checks,incorrect_independence_control=True)


def rejection():
    rng=random.Random(185); cases=pairs_checked=0
    for trial in range(16):
        if trial==0: rows=[[F(1,2),F(1,2),F(0)],[F(1,2),F(0),F(1,2)],[F(0),F(1,2),F(1,2)]]
        else:
            rows=[]
            for _ in range(3):
                w=[rng.randrange(4) for _ in range(3)]
                if not sum(w): w[0]=1
                rows.append([F(x,sum(w)) for x in w])
        @lru_cache(None)
        def joint(state):
            if -1 not in state: return {state:F(1)}
            transitions={}
            for y in range(3):
                cuts=sorted(set([F(0),F(1)]+[rows[i][y] for i in range(3) if state[i]<0]))
                for a,b in zip(cuts,cuts[1:]):
                    out=tuple(y if state[i]<0 and (a+b)/2<=rows[i][y] else state[i] for i in range(3))
                    transitions[out]=transitions.get(out,F(0))+(b-a)/3
            stay=transitions.pop(state,F(0)); out={}
            for st,prob in transitions.items():
                for terminal,w in joint(st).items(): out[terminal]=out.get(terminal,F(0))+prob*w/(1-stay)
            return out
        law=joint((-1,-1,-1)); assert sum(law.values())==1
        for i,y in product(range(3),repeat=2): assert sum(w for s,w in law.items() if s[i]==y)==rows[i][y]
        for i,j in combinations(range(3),2):
            d=sum(abs(a-b) for a,b in zip(rows[i],rows[j]))/2
            disagreement=sum(w for s,w in law.items() if s[i]!=s[j])
            assert d<=disagreement<=2*d/(1+d)
            if trial==0: assert disagreement==F(2,3)>d
            pairs_checked+=1
        cases+=1
    return dict(exact_joint_laws=cases,pairwise_bounds=pairs_checked,simultaneous_optimality_counterexample=True)


def capture():
    rng=random.Random(186); cases=block_checks=0
    for r in (3,4):
        for s in (1,2,3,4):
            n=6*r*s+3; m=2; k=r*s**((r-1)/r); L=s
            assert r*L*(m-1)/(n-1)<=.5
            pool=list(combinations(range(r+3),r))
            for _ in range(5):
                support=rng.sample(pool,s); V=set().union(*map(set,support))
                u=min(V,key=lambda u:sum(u in e for e in support))
                assert 1<=sum(u in e for e in support)<=k+1e-10
                count=0
                for B in combinations(range(n),m):
                    degree=sum(bool(set(B)&set(e)) for e in support)
                    count+=1<=degree<=k+1e-10; block_checks+=1
                assert F(count,math.comb(n,m))>=F(m,2*n); cases+=1
    return dict(supports=cases,enumerated_blocks=block_checks,scope='Combinatorial capture only; no influence headline or large-m low-degree bound tested.')


def fourier_restriction():
    rng=np.random.default_rng(187); cases=0; error=0.
    for n in (3,4,5):
        bits=np.array(list(product((0,1),repeat=n))); masks=range(1<<n)
        for p in (.2,.5,.8):
            law=np.prod(np.where(bits,p,1-p),axis=1)
            chi=np.array([np.prod(((bits-p)/math.sqrt(p*(1-p)))[:,[i for i in range(n) if s>>i&1]],axis=1) for s in masks])
            for mode in range(3):
                f=(bits.sum(axis=1)%2) if mode==0 else (bits.sum(axis=1)>=n//2) if mode==1 else rng.integers(0,2,len(bits))
                hat=chi@(law*f)
                for free in (list(range(n//2)),list(range(n))):
                    ext=[i for i in range(n) if i not in free]; accumulated=np.zeros(1<<len(free)); infl=0.
                    for y in product((0,1),repeat=len(ext)):
                        fixed=np.all(bits[:,ext]==np.array(y),axis=1); x=bits[fixed][:,free]; vals=f[fixed]
                        mu=np.prod(np.where(x,p,1-p),axis=1); wy=np.prod([p if a else 1-p for a in y])
                        for A in range(1<<len(free)):
                            ca=np.prod(((x-p)/math.sqrt(p*(1-p)))[:,[j for j in range(len(free)) if A>>j&1]],axis=1)
                            accumulated[A]+=wy*(sum(mu*vals*ca))**2
                        for j in range(len(free)):
                            lookup={tuple(row):v for row,v in zip(x,vals)}
                            infl+=wy*sum(mu[t]*(v!=lookup[tuple(row[:j])+ (1-row[j],)+tuple(row[j+1:])]) for t,(row,v) in enumerate(zip(x,vals)))
                    for A in range(1<<len(free)):
                        selected=sum(1<<free[j] for j in range(len(free)) if A>>j&1); free_mask=sum(1<<i for i in free)
                        target=sum(hat[s]**2 for s in masks if s&free_mask==selected)
                        error=max(error,abs(accumulated[A]-target)); assert abs(accumulated[A]-target)<1e-11
                    full_lookup={tuple(row):v for row,v in zip(bits,f)}
                    original=sum(law[t]*(v!=full_lookup[tuple(row[:j])+(1-row[j],)+tuple(row[j+1:])]) for j in free for t,(row,v) in enumerate(zip(bits,f)))
                    assert abs(infl-original)<1e-11; cases+=1
    return dict(restrictions=cases,max_mass_error=error,nonmonotone_and_nonsymmetric_controls=True)


def main():
    start=time.perf_counter(); checks={}
    for fn in (isotropic_trees,mst_separation,compression,cutoff,pair_cover,read_k,rejection,capture,fourier_restriction):
        checks[fn.__name__]=fn(); print(fn.__name__,'passed',flush=True)
    report=dict(status='passed',elapsed_seconds=round(time.perf_counter()-start,3),checks=checks,
                scope='Selected finite mechanisms; no thin-tree, expectation-threshold, coloring or sharp-threshold headline theorem is certified.')
    Path(__file__).with_name('results.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='checks'}))


if __name__=='__main__': main()
