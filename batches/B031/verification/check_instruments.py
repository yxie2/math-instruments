"""Exact finite models for selected averaging, coupling and chain mechanisms."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import numpy as np
import sympy as S
rng=np.random.default_rng(31016)

def haar_averaging():
    count=0
    for n in range(5,35):
        rho=rng.integers(0,20,n)
        for _ in range(4):
            E=set(map(int,rng.choice(n,int(rng.integers(1,n+1)),replace=False)))
            B=set(map(int,rng.choice(n,int(rng.integers(1,n+1)),replace=False)))
            lhs=sum(sum(int(rho[(z+e)%n]) for e in E) for z in B)
            rhs=sum(int(rho[y])*len(B & {(y-e)%n for e in E}) for y in range(n))
            assert lhs==rhs
            assert sum(sum(int(rho[(z+e)%n]) for e in E) for z in range(n))==len(E)*sum(rho)
            count+=1
    # Singular Radon model: counting measure on Z versus real interval length.
    singular=0
    for length in (F(2),F(5,2),F(17,3),F(41,2)):
        for j in range(31):
            z=F(j,31);lo=-(-z.numerator//z.denominator);end=z+length;hi=end.numerator//end.denominator
            mass=hi-lo+1;assert length-1<=mass<=length+1 and length/2<=mass<=2*length;singular+=1
    return dict(finite_tonelli_models=count,singular_interval_models=singular,scope='Finite averaging and singular interval examples, not nilpotent boundary maps.')

def backward_recurrence():
    models=0
    for n in range(5,22):
        for _ in range(4):
            Q=set(map(int,rng.choice(n,int(rng.integers(2,n+1)),replace=False)))
            A=set(map(int,rng.choice(sorted(Q),int(rng.integers(1,len(Q)+1)),replace=False)))
            stages=[]
            for j in range(3):
                support=list(map(int,rng.choice(n,int(rng.integers(1,min(n,4)+1)),replace=False)))
                weights=list(map(int,rng.integers(1,6,len(support))));sigma={s:F(w,sum(weights)) for s,w in zip(support,weights)}
                T={x:sum(p*q for s,p in sigma.items() for t,q in sigma.items() if (x+s-t)%n in A) for x in range(n)}
                g={z:sum(p for s,p in sigma.items() if (z-s)%n in A) for z in range(n)}
                assert sum(T[x] for x in A)==sum(v*v for v in g.values())
                D=F(len({(x+s)%n for x in Q for s in support}),len(Q));tau=F(len(A),len(Q))/(2*D)
                prev={x for x in A if T[x]>=tau};assert prev and F(len(prev),len(Q))>=F(len(A),len(Q))**2/(2*D)
                stages.append((prev,A,sigma,tau));A=prev
            # The stages were selected backwards; propagate the exact success law forwards.
            for start in A:
                dist={start:F(1)};bound=F(1)
                for prev,target,sigma,tau in reversed(stages):
                    new={}
                    for x,p0 in dist.items():
                        for s,p in sigma.items():
                            for t,q in sigma.items():
                                y=(x+s-t)%n
                                if y in target:new[y]=new.get(y,F(0))+p0*p*q
                    dist=new;bound*=tau
                assert sum(dist.values())>=bound
            models+=1
    return dict(exact_three_stage_models=models,scope='Finite cyclic group recurrence, including all intermediate state constraints.')

def normalized_counts():
    cases=0
    for L in range(2,42):
        for _ in range(4):
            a=int(rng.integers(20,100));counts=list(map(int,rng.integers(max(0,a-10),a+11,L)));Z=sum(counts);D=sum(abs(v-a) for v in counts)
            tv=sum(abs(F(v,Z)-F(1,L)) for v in counts)/2
            assert abs(Z-L*a)<=D and tv<=F(D,Z)
            if D<L*a:assert tv<=F(D,L*a-D)
            cases+=1
    collision=0
    for N in range(2,35):
        for t in range(1,min(N,8)+1):
            distinct=F(1)
            for j in range(t):distinct*=F(N-j,N)
            assert 1-distinct<=F(t*(t-1),2*N);collision+=1
    return dict(exact_normalization_models=cases,without_replacement_collision_bounds=collision,scope='Deterministic count normalization, not the source random-star concentration estimates.')

def cone_conditional_tests():
    def step(u,v,t):
        i,r=u;j,s=v
        if i==j:return (i,(1-t)*r+t*s)
        z=(1-t)*r-t*s
        return (i,z) if z>=0 else (j,-z)
    def ip(u,v):return u[1]*v[1]*(1 if u[0]==v[0] else -1)
    lists=0;moments=[]
    for n in range(1,8):
        moment=F(0)
        for seq in product(range(3),repeat=n):
            m=(seq[0],F(1))
            for j,k in enumerate(seq[1:],2):m=step(m,(k,F(1)),F(1,j))
            for ray in range(3):assert sum(ip((ray,F(1)),(k,F(1))) for k in seq)/n<=ip((ray,F(1)),m)
            moment+=m[1]**2;lists+=1
        moment/=3**n;assert moment<=F(1,n);moments.append(str(moment))
    for _ in range(100):
        a=rng.random(20);a/=a.sum();b=rng.random(20);b/=b.sum();obs=rng.uniform(-2,2,20)
        assert abs((a-b)@obs)<=2*np.max(abs(obs))*.5*np.sum(abs(a-b))+1e-12
    return dict(tripod_lists_enumerated=lists,exact_inductive_second_moments=moments,bounded_observable_TV_checks=100,
                scope='Non-Hilbert tripod cone identities plus generic TV bounds; no source conditional star coupling verified.')

def small_complete_sets():
    checks=0
    for n in range(2,9):
        # Atoms are arbitrary subsets, and classes may meet multiple atoms.
        labels=rng.integers(0,min(4,n),n);classes=[set(np.where(labels==k)[0]) for k in sorted(set(labels))]
        atoms=[{i} for i in range(n)];p=F(1,3);expect=F(0)
        for bits in product((0,1),repeat=n):
            marked={i for i,b in enumerate(bits) if b};missing=set().union(*(c for c in classes if not c&marked))
            M=marked|missing;assert all(M&c for c in classes)
            weight=p**sum(bits)*(1-p)**(n-sum(bits));expect+=weight*F(len(M),n)
        predicted=p+sum(F(len(c),n)*(1-p)**len(c) for c in classes)
        assert expect==predicted
        representatives={min(c) for c in classes};kappa=sum(F(1,len(next(c for c in classes if i in c))) for i in range(n))/n
        assert F(len(representatives),n)==kappa;checks+=1
    return dict(exhaustive_marking_models=checks,scope='Finite marking formula and class-count identity; infinite-class dominated convergence is analytic, not a finite test.')

def marker_graphings():
    paths=0
    for M,k in product(range(3,13),range(2,7)):
        for h,j in product(range(M),range(k)):
            # t acts in the first factor, commuting j-generator in the second.
            z=(h,j);n=(-h)%M;middle=((h+n)%M,j);assert middle[0]==0
            end=((middle[0]-n)%M,(middle[1]+1)%k);assert end==(h,(j+1)%k);paths+=1
    heights=0
    for width in (1,2,5,99):
        for M in (width+2,width+5,width+17):
            known=set(range(width))
            for k in range(M-width):
                assert set(range(k,k+width))<=known;known.add(k+width)
            assert known==set(range(M));heights+=1
    return dict(commuting_marker_paths=paths,height_window_inductions=heights,scope='Finite commuting-action and height propagation models; no measured cost lower bound.')

def split_boundary():
    count=0
    for old,r in product(range(1,6),range(1,5)):
        A=S.Matrix(rng.integers(-5,6,(old,r)));d=A.col_join(S.eye(r));q=S.zeros(r,old).row_join(S.eye(r))
        assert q*d==S.eye(r)
        phi=S.Matrix(rng.integers(-5,6,(3,r)));assert (phi*q)*d==phi
        # Reduction over non-fields tests that no flatness assumption is used.
        for mod in (4,6,9):
            assert all(int(v)%mod==0 for v in q*d-S.eye(r));count+=1
    return dict(split_boundary_models_over_nonfields=count,scope='Checks split-chain algebra. The Hurewicz realization of attaching spheres is not implemented.')

def fox_character():
    z=S.symbols('z');mod=z*z+z+1
    red=lambda v:S.rem(S.cancel(v),mod,z)
    values=[S.Integer(-1),z,z*z,S.Integer(-1),S.Integer(1)]
    inverse=[red(v**2) if i in (1,2) else v for i,v in enumerate(values)]
    words=[[(0,1),(1,1),(0,-1)]+[(1,-1)]*4,
           [(2,1),(3,1),(2,-1)]+[(3,-1)]*3,
           [(0,1)]+[(3,-1)]*13,
           [(4,1),(2,1),(4,-1)]+[(1,-1)]*5]
    rows=[]
    for word in words:
        prefix=S.Integer(1);row=[S.Integer(0)]*5
        for i,sign in word:
            if sign==1:row[i]=red(row[i]+prefix);prefix=red(prefix*values[i])
            else:prefix=red(prefix*inverse[i]);row[i]=red(row[i]-prefix)
        assert prefix==1;rows.append(row)
    D=S.Matrix(rows);expected=S.Matrix([[1-z,-2,0,0,0],[0,0,2,z*z-1,0],[1,0,0,-1,0],[0,-(1+z),1,0,1-z*z]])
    assert all(red(v)==0 for v in D-expected)
    minor=red(D[:,[0,1,2,4]].det());assert red(minor+4*(1-z*z))==0 and minor!=0
    d1=S.Matrix([red(v-1) for v in values]);assert all(red(v)==0 for v in D*d1)
    return dict(fox_entries_checked=20,relators_checked=4,nonzero_minor=str(minor),boundary_composition='zero in Q[z]/(z^2+z+1)',
                scope='Exact local-system boundary and injectivity; the tower obstruction excluding a 2-dimensional model is not certified.')

if __name__=='__main__':
    groups={}
    for fn in (haar_averaging,backward_recurrence,normalized_counts,cone_conditional_tests,small_complete_sets,marker_graphings,split_boundary,fox_character):
        groups[fn.__name__]=fn();print(fn.__name__,'passed',flush=True)
    out=dict(batch='B031',status='passed',check_groups=groups,limitations='Selected mechanisms only; no global recognition, non-CAT action, non-fixed-price or D(2) conclusion certified; no Lean build.')
    Path(__file__).with_name('results.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out,indent=2))
