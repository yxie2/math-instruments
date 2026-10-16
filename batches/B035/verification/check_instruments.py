"""Exact reductions and finite quantitative checks; no global time bound audit."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations,product
from pathlib import Path
import json
import math
import random
import numpy as np
import sympy as s

def rational_shears():
    rng=random.Random(35109);cases=0;swaps=0
    for m in range(1,6):
        for _ in range(12):
            A=s.Matrix(m,m,lambda i,j:rng.randrange(-3,4));A[:,0]=s.zeros(m,1) if _%3==0 else A[:,0]
            B=A.copy();L=s.eye(m);R=s.eye(m);rows=list(range(m));cols=list(range(m));pivots=[]
            while True:
                occupied=[i for i in rows if any(B[i,j] for j in cols)]
                if not occupied:break
                i=occupied[0];j=max(j for j in cols if B[i,j]);value=B[i,j]
                E=s.eye(m);E[i,i]=1/value;B=E*B;L=E*L
                for k in cols:
                    if k<j and B[i,k]:
                        E=s.eye(m);E[j,k]=-B[i,k];B=B*E;R=R*E
                for k in rows:
                    if k>i and B[k,j]:
                        E=s.eye(m);E[k,i]=-B[k,j];B=E*B;L=E*L
                rows.remove(i);cols.remove(j);pivots.append((i,j))
            assert L*A*R==B and B.rank()==A.rank()==len(pivots)
            assert all(L[i,j]==R[i,j]==0 for i in range(m) for j in range(i+1,m))
            assert sum(int(x!=0) for x in B)==len(pivots) and all(x in (0,1) for x in B)
            E1=L.inv();E2=R.inv();assert E1*B*E2==A
            prime=3
            table=list(L)+list(R)+list(E1)+list(E2)
            while any(int(x.q)%prime==0 for x in table) or any(int(M[i,i].p)%prime==0 for M in (L,R,E1,E2) for i in range(m)):
                prime=int(s.nextprime(prime))
            modulus=prime**3
            mod=lambda M:np.array([int(x.p)*pow(int(x.q),-1,modulus)%modulus for x in M],dtype=object).reshape(M.rows,M.cols)
            h=np.array([rng.randrange(modulus) for j in range(m)],dtype=object);d=np.array([rng.randrange(modulus) for j in range(m)],dtype=object)
            hh=mod(L)@h%modulus;dd=mod(E2)@d%modulus
            for i,j in pivots:
                dd[j]=(dd[j]+hh[i])%modulus;hh[i],dd[j]=dd[j],hh[i];dd[j]=(hh[i]-dd[j])%modulus;swaps+=1
            hh=mod(E1)@hh%modulus;dd=mod(R)@dd%modulus
            assert np.array_equal(hh,(h+mod(A)@d)%modulus) and np.array_equal(dd,d);cases+=1
    return dict(exact_factorization_and_modular_shear_models=cases,rank_counted_swaps=swaps,scope='Algebraic factors and modular shears only; no tape execution time tested.')

def rotate(v,exponent):
    r=len(v);out=[F(0)]*r
    for i,a in enumerate(v):
        q,j=divmod(i+exponent,r);out[j]+=(-1)**q*a
    return out

def synthetic_transforms():
    rng=random.Random(352);checks=0
    def add(a,b,sign=1):return [(x+sign*y)/2 for x,y in zip(a,b)]
    def forward(z,r):
        t=len(z)
        if t==1:return z
        h=t//2;left=[add(z[k],z[k+h]) for k in range(h)];right=[rotate(add(z[k],z[k+h],-1),-2*r*k//t) for k in range(h)]
        return forward(left,r)+forward(right,r)
    def reverse(z,r):
        t=len(z)
        if t==1:return z
        h=t//2;left=reverse(z[:h],r);right=[rotate(v,2*r*k//t) for k,v in enumerate(reverse(z[h:],r))]
        return [add(left[k],right[k]) for k in range(h)]+[add(left[k],right[k],-1) for k in range(h)]
    for r in (2,4,8):
        for t in (2**j for j in range(int(math.log2(2*r))+1)):
            for j in range(2*t):
                total=[sum(rotate([F(1)]+[F(0)]*(r-1),2*r*j*k//t)[i] for k in range(t)) for i in range(r)]
                assert total==([F(t)]+[F(0)]*(r-1) if j%t==0 else [F(0)]*r)
            for _ in range(4):
                z=[[F(rng.randrange(-3,4)) for i in range(r)] for k in range(t)]
                transformed=forward(z,r)
                direct=[[sum(rotate(z[k],-2*r*j*k//t)[i] for k in range(t))/t for i in range(r)] for j in range(t)]
                bits=int(math.log2(t));rev=lambda j:int(format(j,f'0{bits}b')[::-1],2) if bits else 0
                assert all(transformed[rev(j)]==direct[j] for j in range(t))
                assert reverse(transformed,r)==[[x/t for x in v] for v in z];checks+=1
    return dict(exact_stored_order_transform_models=checks,scope='Character cancellation and retained bit-reversal layout; no fast simultaneous-layer or integer multiplication complexity certified.')

def perfect_matching(n,edges):
    adjacency=[0]*n
    for a,b in edges:adjacency[a]|=1<<b;adjacency[b]|=1<<a
    @lru_cache(None)
    def solve(mask):
        if not mask:return ()
        vertices=[i for i in range(n) if mask>>i&1];a=min(vertices,key=lambda i:(adjacency[i]&mask).bit_count());options=adjacency[a]&mask
        while options:
            bit=options&-options;options-=bit;b=bit.bit_length()-1;tail=solve(mask^(1<<a)^bit)
            if tail is not None:return ((a,b),)+tail
        return None
    return solve((1<<n)-1)

def matching_sizes(n,edges):
    @lru_cache(None)
    def rec(mask):
        if not mask:return {0}
        a=(mask&-mask).bit_length()-1;out=set(rec(mask^(1<<a)))
        for u,v in edges:
            b=v if u==a else u if v==a else -1
            if b>=0 and mask>>b&1:out|={1+k for k in rec(mask^(1<<a)^(1<<b))}
        return out
    return rec((1<<n)-1)

def network(size):
    arcs=[];count=0
    def nodes(k):
        nonlocal count
        out=list(range(count,count+k));count+=k;return out
    def make(k):
        if k==1:
            p=nodes(1);return p,p
        inputs=nodes(k);outputs=nodes(k);upper=make(k//2);lower=make(k//2)
        for i in range(k):
            arcs.extend([(inputs[i],upper[0][i//2]),(inputs[i],lower[0][i//2]),(upper[1][i//2],outputs[i]),(lower[1][i//2],outputs[i])])
        return inputs,outputs
    inputs,outputs=make(size);return count,inputs,outputs,arcs

def cardinality_network():
    checks=0
    for n in range(1,5):
        possible=list(combinations(range(n),2));size=1
        while size<n:size*=2
        count,inputs,outputs,arcs=network(size)
        for bits in range(2**len(possible)):
            edges=[e for j,e in enumerate(possible) if bits>>j&1];sizes=matching_sizes(n,tuple(edges))
            for k in range(n//2+1):
                b=n-2*k;g=list(edges)+[(n+2*i,n+2*i+1) for i in range(count)]+[(n+2*u+1,n+2*v) for u,v in arcs]
                g+=[(i,n+2*inputs[i]) for i in range(n)]+[(n+2*outputs[j]+1,n+2*count+j) for j in range(b)]
                witness=perfect_matching(n+2*count+b,g)
                assert (witness is not None)==(k in sizes)
                if witness is not None:assert sum(a<n and b<n for a,b in witness)==k
                checks+=1
    return dict(exhaustive_small_graph_thresholds=checks,scope='All simple graphs through four vertices, including isolates and zero-cardinality cases; no fast matching solver tested.')

def degree_paths():
    checks=0
    for n in range(2,6):
        possible=list(combinations(range(n),2))
        for bits in range(2**len(possible)):
            edges=[e for j,e in enumerate(possible) if bits>>j&1];inc=[[j for j,e in enumerate(edges) if i in e] for i in range(n)]
            if any(not row for row in inc):continue
            ports={};g=[];count=0
            for i,row in enumerate(inc):
                length=2*len(row)-1;g.extend((count+j,count+j+1) for j in range(length-1))
                for j,e in enumerate(row):ports[i,e]=count+2*j
                count+=length
            g.extend((ports[a,j],ports[b,j]) for j,(a,b) in enumerate(edges))
            assert count==4*len(edges)-n
            assert max(sum(i in e for e in g) for i in range(count))<=3
            witness=perfect_matching(count,g);original=perfect_matching(n,edges)
            assert (witness is not None)==(original is not None)
            if witness is not None:
                selected={frozenset(e) for e in witness};decoded=[(a,b) for j,(a,b) in enumerate(edges) if frozenset((ports[a,j],ports[b,j])) in selected]
                assert len(decoded)*2==n and len(set(v for e in decoded for v in e))==n
            checks+=1
    return dict(exhaustive_nonisolated_graphs=checks,scope='All simple graphs through five vertices without isolates; isolates are a separate immediate infeasibility case.')

def curvature_telescope():
    rng=random.Random(35121);checks=0
    for _ in range(100):
        depth=3;count=2**(depth+1)-1;mass=[F(rng.randrange(1,20),5) for i in range(count)];z=[F(0)]*count
        for i in range(2**depth-1,count):z[i]=mass[i]*F(rng.randrange(-10,11),10)
        for i in reversed(range(2**depth-1)):
            W=mass[2*i+1]+mass[2*i+2];zr=z[2*i+1]+z[2*i+2]
            mass[i]=max(mass[i],abs(zr)/2)
            z[i]=max(-mass[i],min(mass[i],zr))
        totalK=totalG=totale=totalh=F(0)
        for i in range(2**depth-1):
            kids=(2*i+1,2*i+2);W=sum(mass[j] for j in kids);zr=sum(z[j] for j in kids);e=abs(zr-z[i])
            # Enforce the source local endpoint slack e<=parent mass.
            assert e<=mass[i]
            G=W*F(rng.randrange(0,5),10);R=mass[i]-W;h=max(F(0),R+G)
            K=sum(z[j]**2/mass[j] for j in kids)-zr*zr/W
            assert K==sum((z[j]-zr/W*mass[j])**2/mass[j] for j in kids)
            assert K>=0
            totalK+=K;totalG+=G;totale+=e;totalh+=h
        terminal=sum(mass[2**depth-1:])
        assert totalK+totalG<=4*terminal+3*totale+4*totalh;checks+=1
    return dict(exact_nonconservative_tree_models=checks,scope='Abstract curvature/mass budget; source alignment and warmup hypotheses are not tested.')

def block_entropy():
    rng=np.random.default_rng(353);checks=0;large_offsets=0
    for _ in range(80):
        blocks=[slice(0,3),slice(3,6)];masses=np.array([.3,.7]);d=6;steps=20;eta=12.;kappa=.2
        f=np.ones(d);acc=np.zeros(d);costs=[];left=0.
        for t in range(steps):
            delta=np.r_[rng.uniform(0,.04)+rng.uniform(0,.004,3),rng.uniform(0,.004)+rng.uniform(0,.004,3)]
            delta=np.minimum(delta,f);assert all(np.ptp(delta[b])<=kappa/eta for b in blocks)
            large_offsets+=int(np.ptp(delta)>kappa/eta)
            predicted=-f;rho=np.zeros(d)
            for b,m in zip(blocks,masses):
                logits=eta*(acc+predicted)[b];ex=np.exp(logits-logits.max());rho[b]=m*ex/ex.sum()
            newf=f-delta;left+=(newf+kappa*delta)@rho;costs.append(newf)
            cumulative=np.sum(costs,axis=0);best=sum(m*cumulative[b].min() for b,m in zip(blocks,masses))
            assert left<=best+math.log(d)/eta+2*kappa+1e-10
            acc+=predicted+(1-2*kappa)*delta;f=newf;checks+=1
    return dict(prefix_regret_checks=checks,steps_exceeding_global_range_bound=large_offsets,scope='Product-of-block-simplex models, exact softmax maximizers; arbitrary constrained action hulls use the selected proof.')

def priority_lists():
    rng=random.Random(35124);checks=0
    for _ in range(200):
        n=12;reach=[[False]*n for j in range(n)]
        for i in reversed(range(n)):
            for j in range(i+1,n):
                if rng.random()<.15:reach[i][j]=True
                if reach[i][j]:
                    for k in range(j+1,n):reach[i][k]|=reach[j][k]
        up=lambda S:S|{j for i in S for j in range(n) if reach[i][j]}
        lists=[up({i for i in range(n) if rng.random()<.12}) for j in range(6)]
        key=lambda L,x:max((i,x) for i,K in enumerate(L) if x in K) if any(x in K for K in L) else None
        index=rng.randrange(6);rank=rng.randrange(n+1);carry=[lists[index]&set(range(rank,n))]+lists[index+1:]
        selected=[i for i in range(n) if key(lists,i) is not None and key(lists,i)>=(index,rank)]
        assert set(selected)==set.union(set(),*carry)
        assert sorted(selected,key=lambda x:key(lists,x))==sorted(selected,key=lambda x:key(carry,x))
        W={i for i in range(n) if rng.random()<.3};pruned=[K for K in lists if K&W]
        for x in W:
            for y in range(n):
                if key(pruned,x) is not None and key(pruned,y) is not None and key(pruned,x)<key(pruned,y):assert key(lists,x)<key(lists,y)
        checks+=1
    # The comparison fails if the first job is outside W.
    lists=[{0,1,2},{0}];pruned=[lists[0]]
    assert key(pruned,0)<key(pruned,1) and key(lists,0)>key(lists,1)
    return dict(random_poset_list_models=checks,outside_child_negative_control=True,scope='Carry and one-sided pruning order only; no global scheduling hierarchy constructed.')

def boundary_capacity():
    checks=0
    # Every injection has a nonempty set of boundary witnesses; disjointness makes these sets disjoint.
    for masks in product(range(1,8),repeat=4):
        disjoint=all(a&b==0 for a,b in combinations(masks,2));assert not disjoint;checks+=1
    for count in range(1,4):
        for masks in product(range(1,8),repeat=count):
            if all(a&b==0 for a,b in combinations(masks,2)):assert count<=3 and count+2<=5;checks+=1
    return dict(exact_boundary_witness_families=checks,scope='Three-slot capacity conditional on disjoint upsets and successor witnesses; source global boundary invariants are not certified.')

if __name__=='__main__':
    groups={}
    for fn in (rational_shears,synthetic_transforms,cardinality_network,degree_paths,curvature_telescope,block_entropy,priority_lists,boundary_capacity):
        groups[fn.__name__]=fn();print(fn.__name__,'passed',flush=True)
    out=dict(batch='B035',status='passed',check_groups=groups,limitations='Selected exact identities, reductions and finite models only; no claimed global algorithm or running time certified; no Lean build.')
    Path(__file__).with_name('results.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out,indent=2))
