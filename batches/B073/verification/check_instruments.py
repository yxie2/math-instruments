"""Finite diagnostics of selected interfaces; no source headline certification."""
import json
import math
import time
from pathlib import Path
from fractions import Fraction as F
from itertools import product, permutations
from collections import Counter, defaultdict
import numpy as np
from scipy.optimize import linprog
from scipy.spatial import ConvexHull


def words(n,h):
    return [w for t in range(h+1) for w in product(range(n),repeat=t)]


def insdel(x,y):
    row=list(range(len(y)+1))
    for i,a in enumerate(x,1):
        new=[i]
        for j,b in enumerate(y,1):
            new.append(row[j-1] if a==b else min(row[j],new[-1])+1)
        row=new
    return row[-1]


def hash_average():
    ws=words(3,2);q=16;hs=list(product(range(q),repeat=3));checks=0
    chosen=[((),(0,)),((0,1),(1,0)),((0,0),(1,2)),((0,2),(1,2)),((0,1),(2,))]
    for x,y in chosen:
        original=insdel(x,y);used=set(x+y);bad=0;mean=0
        for h in hs:
            hx=tuple(h[a] for a in x);hy=tuple(h[a] for a in y);dist=insdel(hx,hy)
            assert dist<=original
            injective=len({h[a] for a in used})==len(used)
            if injective: assert dist==original
            else:bad+=1
            mean+=dist;checks+=1
        assert F(bad,len(hs))<=F(len(used)*(len(used)-1),2*q)<F(1,2)
        assert F(mean,len(hs))>=F(original,2)
    # Sparse coordinates of a probability-weighted direct sum of one-hot maps.
    vectors=[]
    for x in ws[:5]:
        vector={}
        for j,h in enumerate(hs):
            key=(j,tuple(h[a] for a in x));vector[key]=F(1,len(hs))
        vectors.append(vector)
    for i in range(5):
        for j in range(i):
            distance=sum(abs(vectors[i].get(k,0)-vectors[j].get(k,0)) for k in vectors[i].keys()|vectors[j].keys())
            expected=sum(2*(tuple(h[a] for a in ws[i])!=tuple(h[a] for a in ws[j])) for h in hs)
            assert distance==F(expected,len(hs))
    return dict(exact_hash_pair_checks=checks,direct_sum_pairs=10,empty_strings=True)


def partition_histograms():
    cuts=[{0,1},{0,2},{0,3}];lists=list(product(range(4),repeat=2));cases=0
    for probs in [[F(1,3),F(1,2),F(2,5)],[F(7,8),F(8,9),F(15,16)]]:
        partitions=[]
        for bits in product([0,1],repeat=3):
            p=math.prod(probs[j] if bits[j] else 1-probs[j] for j in range(3))
            keys=[tuple(x in cuts[j] for j in range(3) if bits[j]) for x in range(4)]
            partitions.append((p,keys))
        collision={}
        for x,y in product(range(4),repeat=2):
            c=sum(p for p,k in partitions if k[x]==k[y]);target=math.prod(1-probs[j] for j in range(3) if (x in cuts[j])!=(y in cuts[j]))
            assert c==target;collision[x,y]=c
        for L,M in product(lists,repeat=2):
            dist=F(0)
            for p,k in partitions:
                a=Counter(k[x] for x in L);b=Counter(k[x] for x in M)
                dist+=p*sum(abs(a[c]-b[c]) for c in a.keys()|b.keys())
            assert dist>=4*(1-4*max(collision[x,y] for x in L for y in M))
            for order in permutations(M):
                for matched in range(3):
                    upper=2*(2-matched)+2*sum(1-collision[x,y] for x,y in zip(L[:matched],order[:matched]))
                    assert dist<=upper
                    linear=2*(2-matched)+2*sum(-math.log(float(collision[x,y])) for x,y in zip(L[:matched],order[:matched]))
                    assert float(dist)<=linear+1e-12
            cases+=1
    return dict(list_pairs=cases,partition_models=16,collision_equalities=32,repetitions=True)


def square_cover():
    def nearest(x):return math.floor(x+F(1,2))
    shears=[(F(0),F(10)),(F(10),F(0)),(F(10),F(1,100)),(F(-10),F(-1,100)),(F(9,10),F(9,10)),(F(2),F(2,5)),(F(-2),F(-2,5))]
    cases=0;iterations=0
    for a,b in shears:
        for x,y in product([F(i,7) for i in range(-12,13,3)],repeat=2):
            M=math.ceil((abs(x-a*y)+F(1,2)+abs(a)/2+2)/(1-a*b))
            fn=lambda i:nearest(x-a*nearest(y-b*i))
            assert fn(-M)>=-M and fn(M)<=M
            i=-M
            for _ in range(2*M+2):
                nxt=fn(i);assert i<=nxt<=M;iterations+=1
                if nxt==i:break
                i=nxt
            else:raise AssertionError('fixed-point iteration did not terminate')
            j=nearest(y-b*i)
            assert abs(x-i-a*j)<=F(1,2) and abs(y-b*i-j)<=F(1,2);cases+=1
    # Opposite signs fall outside the covering hypothesis.
    a,b=F(1,2),F(-1,2);x,y=F(3,5),F(3,10)
    # Any possible covering center has inverse-coordinate bounds |i|,|j|<2.
    invnorm=(1+abs(a))/(1-a*b)
    assert invnorm*max(abs(x)+F(1,2),abs(y)+F(1,2))<2
    assert all(max(abs(x-i-a*j),abs(y-b*i-j))>F(1,2) for i,j in product(range(-2,3),repeat=2))
    return dict(rational_targets=cases,integer_iterations=iterations,opposite_sign_hole=True)


def simplex_projection():
    rng=np.random.default_rng(7304);cases=0;maxerr=0.
    for d in [2,3]:
        for model in range(5):
            while True:
                vertices=rng.normal(size=(d+1,d))
                determinant=np.linalg.det((vertices[1:]-vertices[0]).T)
                if abs(determinant)>.1:break
            volume=abs(determinant)/math.factorial(d)
            for _ in range(12):
                u=rng.normal(size=d);u/=np.linalg.norm(u)
                _,_,vh=np.linalg.svd(u[None,:]);projection=vertices@vh[1:].T
                area=float(np.ptp(projection)) if d==2 else ConvexHull(projection).volume
                n=d+1;A=np.zeros((d+2,2*n+1));A[:d,:n]=-vertices.T;A[:d,n:2*n]=vertices.T;A[:d,-1]=-u
                A[d,:n]=1;A[d+1,n:2*n]=1;rhs=np.r_[np.zeros(d),1,1];objective=np.zeros(2*n+1);objective[-1]=-1
                sol=linprog(objective,A_eq=A,b_eq=rhs,bounds=(0,None),method='highs');assert sol.success
                L=sol.x[-1];error=abs(area*L-d*volume);maxerr=max(maxerr,error)
                assert error<1e-8*(1+d*volume);cases+=1
    return dict(projected_hull_and_chord_lp_pairs=cases,max_absolute_error=maxerr)


def finite_martingales():
    G=[F(0),F(1),F(2)];psi=[F(2),F(-1),F(3)]
    transitions={0:[(0,F(1))],1:[(0,F(1,4)),(1,F(1,2)),(2,F(1,4))],2:[(2,F(1))]}
    # Rewards chosen so the chance bias equality holds; path residual is a martingale difference.
    reward={(i,j):G[j]+psi[i]-psi[j] for i in transitions for j,p in transitions[i]}
    paths=[(F(1),[1],F(0),F(0),F(0))]
    for horizon in range(1,9):
        new=[]
        for prob,states,weight,jumps,residual in paths:
            i=states[-1]
            for j,p in transitions[i]:
                w=reward[i,j];R=w+psi[j]-psi[i]-G[i]
                new.append((prob*p,states+[j],weight+w,jumps+(G[j]-G[i])**2,residual+R))
        paths=new
        assert sum(p for p,*_ in paths)==1
        expected_jumps=sum(p*j for p,st,w,j,r in paths)
        assert expected_jumps==sum(p*(G[st[-1]]**2-G[st[0]]**2) for p,st,w,j,r in paths)
        assert expected_jumps<=4
        for p,st,w,j,r in paths:
            assert w==sum(G[v] for v in st[:-1])+r+psi[st[0]]-psi[st[-1]]
        assert sum(p*r for p,st,w,j,r in paths)==0
    for t in range(1,11):
        totals=[sum(v) for v in product([-1,1],repeat=t)]
        assert sum(totals)==0 and sum(x*x for x in totals)==t*2**t
    return dict(markov_paths_at_horizon8=len(paths),horizons=8,exact_coin_variances=10)


def restart_budgets():
    potential=[-2,0,3];W=5;B=2*W;paths=0
    for st in product(range(3),repeat=6):
        weight=sum(potential[a]-potential[b] for a,b in zip(st,st[1:]))
        assert weight>=-B;paths+=1
    # j zero-cost mean-payoff steps, then one negative-cost attractor step.
    costs=[];rounds=[]
    for j in range(1,81):costs.extend([0]*j+[-1]);rounds.extend([j]*(j+1))
    weight=0;prefixes=0
    for t,(cost,q) in enumerate(zip(costs,rounds),1):
        weight+=cost;assert q<=1+math.sqrt(2*t)
        assert weight>=-(1+math.sqrt(2*t))
        for eps in [F(1,2),F(1,5),F(1,20)]:
            K=F(3,2);delta=eps/2;C=K+K*K/eps
            assert float(K*math.sqrt(2*t))<=float(eps*t/2+K*K/eps)+1e-12
            assert weight>=-eps*t-C
        prefixes+=1
    assert F(sum([0,-1]*100),200)==F(-1,2)
    return dict(potential_paths=paths,interrupted_prefixes=prefixes,constant_round_negative_control=True)


def legal(config,r):return [config.index(r)] if r in config else list(range(len(config)))
def move(config,r,j):return config[:j]+(r,)+config[j+1:]
def dist(x,y):return abs(x-y)
def policy(w,c,r):
    labels=legal(c,r)
    if len(labels)==1:return {labels[0]:F(1)}
    p=F(1+(sum(w)+sum(c)+r)%4,5)
    return {labels[0]:p,labels[1]:1-p}


def compact_policy_models():
    cases=0;leaves=0
    for w in words(3,4):
        paths=[(F(1),F(0),F(1),(0,1),0)]
        for t,r in enumerate(w):
            new=[]
            for prob,lo,hi,c,cost in paths:
                cursor=lo
                for j,p in policy(w[:t],c,r).items():
                    endpoint=cursor+(hi-lo)*p
                    new.append((prob*p,cursor,endpoint,move(c,r,j),cost+dist(c[j],r)))
                    cursor=endpoint
                assert cursor==hi
            paths=new
        assert sum(p for p,*_ in paths)==1
        assert all(p==hi-lo for p,lo,hi,c,cost in paths)
        intervals=sorted((lo,hi) for p,lo,hi,c,cost in paths)
        assert intervals[0][0]==0 and intervals[-1][1]==1
        assert all(b==c for (a,b),(c,d) in zip(intervals,intervals[1:]))
        def recurse(t,c):
            if t==len(w):return F(0)
            return sum(p*(dist(c[j],w[t])+recurse(t+1,move(c,w[t],j))) for j,p in policy(w[:t],c,w[t]).items())
        assert sum(p*cost for p,lo,hi,c,cost in paths)==recurse(0,(0,1))
        cases+=1;leaves+=len(paths)
    return dict(input_words=cases,seed_intervals=leaves,exact_expected_costs=True)


def rational_flow_rounding():
    H=4;k=2;D=2;b=math.ceil(math.log2(k*H*H));denom=2**b
    distributions={():{(0,1):F(1)}};flows={};costs={():F(0)};checks=0
    for w in words(3,H-1):
        for r in range(3):
            nxt=defaultdict(F);row={};increment=F(0)
            for c in permutations(range(3),2):
                mass=distributions[w].get(c,F(0))
                for j,q in policy(w,c,r).items():
                    row[c,j]=mass*q;nxt[move(c,r,j)]+=mass*q;increment+=mass*q*dist(c[j],r)
                assert sum(v for (cc,j),v in row.items() if cc==c)==mass
            distributions[w+(r,)]=dict(nxt);flows[w,r]=row;costs[w+(r,)]=costs[w]+increment
            assert sum(nxt.values())==1;checks+=1
    zero_rows=0;max_increase=F(0)
    for word in words(3,H):
        current={(0,1):F(1)};cost=F(0)
        for t,r in enumerate(word):
            w=word[:t];nxt=defaultdict(F)
            for c,mass in current.items():
                original_mass=distributions[w].get(c,F(0));labels=legal(c,r);reserved=min(labels)
                if original_mass:
                    row={j:flows[w,r].get((c,j),F(0))/original_mass for j in labels}
                    assert row==policy(w,c,r)
                else:
                    row={j:F(j==reserved) for j in labels};zero_rows+=1
                rounded={j:F(math.floor(row[j]*denom),denom) for j in labels if j!=reserved};rounded[reserved]=1-sum(rounded.values())
                tv=sum(abs(row[j]-rounded[j]) for j in labels)/2
                assert tv<=F(k,denom) and sum(rounded.values())==1
                for j,q in rounded.items():nxt[move(c,r,j)]+=mass*q;cost+=mass*q*dist(c[j],r)
            current=dict(nxt)
        increase=cost-costs[word];max_increase=max(max_increase,increase)
        assert increase<=F(k*len(word)**2*D,denom)<=D
    # Explicit zero-mass row remains legal, regardless of whether rounding reaches it.
    for c in permutations(range(3),2):
        for r in range(3):
            j=min(legal(c,r));assert r in move(c,r,j)
    return dict(causal_flow_edges=checks,words=121,bits_per_request=b,max_exact_cost_increase=str(max_increase),reached_zero_mass_rows=zero_rows,legal_default_rows=18,lp_optimality_tested=False)


if __name__=='__main__':
    start=time.perf_counter();checks={}
    for f in [hash_average,partition_histograms,square_cover,simplex_projection,finite_martingales,restart_budgets,compact_policy_models,rational_flow_rounding]:checks[f.__name__]=dict(status='pass',details=f())
    result=dict(batch='B073',status='pass',elapsed_seconds=round(time.perf_counter()-start,3),scope='Selected finite models and identities; no source headline, LP optimum or Lean certification.',checks=checks)
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
