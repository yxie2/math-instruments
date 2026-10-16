"""Finite checks for the extracted mechanisms and their dependencies."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product,combinations,permutations
from pathlib import Path
import json,math,time
import numpy as np
from scipy.stats import binom

def midpoint_arrays():
    edges=[(0,1),(1,2),(2,3),(3,0)];arrays=[(0,)+x for x in product(range(-2,3),repeat=3) if all(abs(((0,)+x)[i]-((0,)+x)[j])<=1 for i,j in edges)];cases=0
    E=lambda x:sum(abs(x[i]-x[j]) for i,j in edges);coeff=[.4,-.2,.7,-.1];A=sum(abs(x) for x in coeff)
    for s,t in product(arrays,repeat=2):
        lo=tuple((a+b)//2 for a,b in zip(s,t));hi=tuple(-(-(a+b)//2) for a,b in zip(s,t));assert lo in arrays and hi in arrays and E(lo)+E(hi)<=E(s)+E(t)
        for x in [lo,hi]:assert abs(np.dot(coeff,x)-(np.dot(coeff,s)+np.dot(coeff,t))/2)<=A/2+1e-12
        cases+=1
    rng=np.random.default_rng(8001);entropy_cases=0
    for _ in range(50):
        a=rng.integers(0,8,size=7).astype(float);b=rng.integers(0,8,size=7).astype(float);a/=sum(a);b/=sum(b)
        cuts=sorted(set([0.,1.]+list(np.cumsum(a))+list(np.cumsum(b))));lo=np.zeros(7);hi=np.zeros(7)
        for x,y in zip(cuts,cuts[1:]):
            if y-x<1e-14:continue
            i=min(6,np.searchsorted(np.cumsum(a),(x+y)/2));j=min(6,np.searchsorted(np.cumsum(b),(x+y)/2));lo[(i+j)//2]+=y-x;hi[(i+j+1)//2]+=y-x
        H=lambda p:sum(x*math.log(x) for x in p if x>0)
        assert H(lo)+H(hi)<=H(a)+H(b)+1e-12;entropy_cases+=1
    # Direct functional inequality on rounded midpoint images of height subsets.
    for _ in range(30):
        X=[x for x in arrays if rng.random()<.5];Y=[x for x in arrays if rng.random()<.5];U=set();V=set()
        for s,t in product(X,Y):U.add(tuple((a+b)//2 for a,b in zip(s,t)));V.add(tuple((a+b+1)//2 for a,b in zip(s,t)))
        weight=lambda x:F(2,3)**E(x)
        assert sum(map(weight,X))*sum(map(weight,Y))<=sum(map(weight,U))*sum(map(weight,V))
    # An explicit centered discrete log-concave law verifies the dyadic mass recursion.
    states=range(-300,301);weights={x:math.exp(-abs(x)/12) for x in states};Z=sum(weights.values());M=2;c=sum(w for x,w in weights.items() if abs(x)<=M)/Z
    p={j:sum(w for x,w in weights.items() if (2**j-4)*M<=x<=(2**(j+1)+4)*M)/Z for j in range(3,10)}
    assert all(p[j]<=p[j-1]**2/c+1e-12 for j in range(4,10))
    return dict(height_pairs=cases,quantile_entropy_cases=entropy_cases,weighted_midpoint_sum_checks=30,dyadic_recursions=6)

def scalar_spectra():
    rng=np.random.default_rng(8002);lam=np.array([0.,.1,.4,.9,1.]);theta=np.array([0.,.3,1.,2.,3.]);a=rng.normal(size=5)+1j*rng.normal(size=5);b=rng.normal(size=5)+1j*rng.normal(size=5);cross=a.conj()*b;cases=0
    assert sum(abs(cross))<=np.linalg.norm(a)*np.linalg.norm(b)+1e-12
    for N in [4,16,64,256]:
        probs=np.array([binom.pmf(np.arange(N+1),N,x) for x in lam]);assert np.max(abs(probs.sum(1)-1))<1e-12
        for j in [0,1,2,3]:
            moment=probs@((np.arange(N+1)/N)**j)
            expected=[np.ones(5),lam,lam**2+lam*(1-lam)/N,lam**3+3*lam**2*(1-lam)/N+lam*(1-lam)*(1-2*lam)/N**2][j]
            assert np.max(abs(moment-expected))<1e-12;cases+=1
        assert probs[0,0]==1 and probs[-1,-1]==1
    N=12;grid=np.arange(256)*2*np.pi/256;density=np.array([np.sum(abs(a)**2*abs(sum(np.exp(1j*k*(theta-t)) for k in range(N)))**2)/N for t in grid])
    for m in range(-4,5):assert abs(np.mean(np.exp(1j*m*grid)*density)-(1-abs(m)/N)*np.sum(abs(a)**2*np.exp(1j*m*theta)))<1e-12
    for w in [.2+2j,1+0j,3+1j]:
        powers=np.zeros(5,complex);powers[1:]=np.exp(w*np.log(lam[1:]));assert abs(cross@powers)<=np.linalg.norm(a)*np.linalg.norm(b)+1e-12
    limit=cross[1:].sum();assert abs(cross.sum()-limit)>1e-3
    return dict(bernstein_moments=cases,fejer_moments=9,zero_and_one_atoms=True,exponent_zero_jump=float(abs(cross[0])))

def omission_hazards():
    # Proper 2-clauses on two variables kill one of four assignments. The two extracted finite lemmas do not require k>=3.
    M=5;values=[];delays=np.zeros(M);rhs=np.zeros(M);cases=0
    for seq in product(range(4),repeat=M):
        def last(skip=None):
            mask=0;v=0
            for m,c in enumerate(seq,1):
                if m-1!=skip:mask|=1<<c
                if mask!=15:v=m
            return v
        v=last();values.append(v)
        for i in range(M):
            vi=last(i);indicators=[];localrhs=0.
            for m in range(i+1,M+1):
                G=set(seq[j] for j in range(m) if j!=i);A=len(G)<4 and len(G|{seq[i]})==4;indicators.append(A)
                q=.25 if len(G)==3 else 0.;localrhs+=2*min(M*q,1)
            assert vi-v==sum(indicators)
            delays[i]+=(vi-v)**2;rhs[i]+=localrhs
        cases+=1
    delays/=cases;rhs/=cases;assert np.all(delays<=rhs+1e-12) and np.var(values)<=sum(delays)+1e-12
    # Two individually harmless clauses may jointly kill the current solution set.
    solutions={0,1};assert solutions-{0} and solutions-{1} and not solutions-{0,1}
    return dict(exhaustive_clause_sequences=cases,variance=float(np.var(values)),sum_squared_omission_delays=float(sum(delays)),cooperative_killing_control=True)

def clause_replacement():
    cases=active=0
    for n in [4,8,20,50,120,1000]:
        for k in range(3,min(n-1,7)+1):
            v=n-1;eps=n**(-(k-1)/k);g=math.ceil(2*k*n**(1/k))
            for b in sorted(set([0,k-1,k,v//2,v-1,v])):
                if b<0 or b>v:continue
                q=lambda r:math.comb(b,r)/(2**r*math.comb(v,r)) if b>=r else 0.
                x=q(k-1);y=q(k);lower=-math.expm1(g*math.log1p(-y));assert lower>=x-eps-1e-12
                if x>eps:assert y>=x**(k/(k-1))/k-1e-12;active+=1
                cases+=1
    # All nonempty sets of Boolean assignments on three variables; direct killing-clause counts.
    assignments=list(product([0,1],repeat=3));counts=0
    for mask in range(1,256):
        sols=[a for i,a in enumerate(assignments) if mask>>i&1];forced=sum(len({a[j] for a in sols})==1 for j in range(3))
        for r in [1,2,3]:
            kills=0;total=0
            for coords in combinations(range(3),r):
                for pattern in product([0,1],repeat=r):kills+=all(tuple(a[j] for j in coords)==pattern for a in sols);total+=1
            assert F(kills,total)==(F(math.comb(forced,r),2**r*math.comb(3,r)) if forced>=r else 0);counts+=1
    rng=np.random.default_rng(8004)
    for M in [0,1,4,20]:
        P=np.r_[1.,np.sort(rng.random(100))[::-1],np.zeros(100)]
        for shift in [0,1,3,50]:assert sum(P[t]-P[t+shift] for t in range(M+1))<=shift+1e-12
    return dict(replacement_parameters=cases,active_power_comparisons=active,exact_solution_set_counts=counts,telescoping_checks=16)

def renewal_rewards():
    pieces=[(1,2,F(1,3)),(2,7,F(1,2)),(3,4,F(1,6))];Hmax=14;B=[F(0)]*(Hmax+1);R=[F(0)]*(Hmax+1);B[0]=1
    def visit(h,w,reward):
        for H,L,p in pieces:
            if h+H<=Hmax:B[h+H]+=w*p;R[h+H]+=w*p*(reward+L);visit(h+H,w*p,reward+L)
    visit(0,F(1),0);pf=[F(0)]*(Hmax+1)
    for H,L,p in pieces:pf[H]+=p*L
    for h in range(Hmax+1):assert R[h]==sum(B[i]*pf[j]*B[h-i-j] for i in range(h+1) for j in range(h-i+1))
    s=.4;joint=sum(float(p)*L*math.exp(-s*H) for H,L,p in pieces);split=sum(float(p)*L for H,L,p in pieces)*sum(float(p)*math.exp(-s*H) for H,L,p in pieces);assert abs(joint-split)>.01
    return dict(exact_height_coefficients=Hmax+1,joint_discounted_reward=joint,incorrect_independent_reward=split)

def joint_increment_transfer():
    pieces=[(1,2,1,F(1,3)),(2,7,10,F(1,2)),(3,4,2,F(1,6))];cases=0
    for s in [.1,.4,1.]:
        w=[float(p)*math.exp(-s*H) for H,L,D,p in pieces];d=1-sum(w)
        for x in [1,3,20]:
            q=sum(v for v,(_,_,D,_) in zip(w,pieces) if D>x);allmass=1/d;goodmass=1/(d+q);assert abs((allmass-goodmass)/allmass-q/(d+q))<1e-12;cases+=1
    Hmax=30;B=[F(0)]*(Hmax+1);R=[F(0)]*(Hmax+1);B[0]=1
    for h in range(1,Hmax+1):
        for H,L,D,p in pieces:
            if h>=H:B[h]+=p*B[h-H];R[h]+=p*(R[h-H]+L*B[h-H])
    for x in range(1,10):
        reward=sum(p*L for H,L,D,p in pieces if H<=x);assert sum(B[:x+1])**2*reward<=sum(R[:3*x+1])
    assert F(25,12)-F(3,2)==F(7,12)
    assert F(3,4)*F(3,4)==1-F(3,4)*F(7,12)==F(9,16)
    assert pieces[1][2]>5 and pieces[1][0]<5
    return dict(discounted_bad_piece_ratios=cases,truncated_reward_bounds=9,balanced_length_exponent='9/16',height_only_control=True)

def shuffle_energy():
    cases=identities=0;d=2;n=4;T=4;edges=[[(x,x^(1<<i)) for x in range(n) if not(x>>i&1)] for i in range(d)]
    for ell in [0,1,2,3]:
        records=[]
        for coins in product([0,1],repeat=2*T):
            pos=list(range(n));hist=[tuple(pos)];
            for s in range(T):
                mapping=list(range(n))
                for bit,(a,b) in zip(coins[2*s:2*s+2],edges[s%d]):
                    if bit:mapping[a],mapping[b]=b,a
                pos=[mapping[x] for x in pos];hist.append(tuple(pos))
            records.append(hist)
        groups=[];E=[];bvals=[]
        for s in range(T+1):
            G=defaultdict(list)
            for hist in records:G[tuple(row[:ell] for row in hist[:s+1])].append(hist)
            groups.append(G);energy=bad=0.
            for key,hists in G.items():
                free=set(range(n))-set(key[-1]);p=np.bincount([h[s][ell] for h in hists],minlength=n)/len(hists);w=p-np.array([1/(n-ell) if x in free else 0 for x in range(n)]);prob=len(hists)/len(records)
                energy+=prob*(w@w);bad+=prob*sum(w[x]**2 for x in free if x^(1<<(s%d)) not in free)
            E.append(energy);bvals.append(bad)
        for t in range(d,T+1):assert abs(E[t]-sum(2**(-j)*bvals[t-j] for j in range(1,d+1)))<1e-12;identities+=1
        for key,hists in groups[-1].items():
            for s in range(T+1):
                prefix=key[:s+1];past=groups[s][prefix];p=np.bincount([h[s][ell] for h in hists],minlength=n)/len(hists);q=np.bincount([h[s][ell] for h in past],minlength=n)/len(past);assert np.max(abs(p-q))<1e-12;cases+=1
    return dict(coin_arrays_per_exposure=256,exposure_counts=4,energy_identities=identities,full_path_prefix_comparisons=cases)

def sequential_tv():
    rng=np.random.default_rng(8008);states=list(permutations(range(5),3));cases=0
    for _ in range(35):
        p=rng.dirichlet(np.ones(len(states)));tv=abs(p-1/len(states)).sum()/2;total=refined=0.
        for j in range(3):
            G=defaultdict(list)
            for i,s in enumerate(states):G[s[:j]].append(i)
            for prefix,inds in G.items():
                mass=sum(p[i] for i in inds);q=np.zeros(5)
                for i in inds:q[states[i][j]]+=p[i]/mass
                u=np.array([0 if x in prefix else 1/(5-j) for x in range(5)]);total+=mass*abs(q-u).sum()/2
                # Reveal the final coordinate as auxiliary information (contains the prefix).
                for last in range(5):
                    selected=[i for i in inds if states[i][-1]==last];m=sum(p[i] for i in selected)
                    if not m:continue
                    qq=np.zeros(5)
                    for i in selected:qq[states[i][j]]+=p[i]/m
                    refined+=m*abs(qq-u).sum()/2
        assert tv<=total+1e-12 and total<=refined+1e-12;cases+=1
    pairs=[(i,(i+1)%4) for i in range(4)];assert all(sum(x[j]==i for x in pairs)==1 for i in range(4) for j in [0,1])
    assert len(pairs)<4*3
    return dict(injection_laws=cases,conditioning_refinement_checks=cases,uniform_individual_marginals_dependent_control=True)

if __name__=='__main__':
    start=time.perf_counter();checks={}
    for f in [midpoint_arrays,scalar_spectra,omission_hazards,clause_replacement,renewal_rewards,joint_increment_transfer,shuffle_energy,sequential_tv]:checks[f.__name__]=dict(status='pass',details=f())
    result=dict(batch='B080',status='pass',elapsed_seconds=round(time.perf_counter()-start,3),scope='Selected finite mechanisms; no headline or Lean certification.',checks=checks)
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8');print(json.dumps(result))
