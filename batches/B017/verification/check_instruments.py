"""Exact finite bookkeeping and numerical kernel checks for B017."""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import combinations, product
from math import ceil, comb, exp, gcd, log, log2, prod
from pathlib import Path
import json
import random
import sys
import numpy as np

RNG=random.Random(17022)
NP=np.random.default_rng(17022)
OUT={}


def subsets(values):
    values=tuple(values)
    for size in range(len(values)+1):
        yield from combinations(values,size)


def coordinate_checks():
    cases=0; max_scaled_excess=0.0
    for n,u,a,q in product((3,7,12),(.6,.75,.85),(1,2),(.03,.07,.15)):
        indices=np.arange(n)
        kernel=q**abs(indices[:,None]-indices[None,:])
        kernel*=np.where(indices[:,None]==indices[None,:],1,a)
        for concentration in (False,True):
            alpha=NP.random(n); alpha/=alpha.sum()
            beta=NP.random(n); beta/=beta.sum()
            k=RNG.randrange(n)
            if concentration:
                eps=q**(1/(1-u))
                alpha*=eps; beta*=eps
                alpha[k]+=1-eps; beta[k]+=1-eps
            term=kernel*(alpha[:,None]*beta[None,:])**u
            total=term.sum()
            da,db=1-alpha[k],1-beta[k]
            others=indices!=k
            central=(alpha[k]*beta[k])**u
            single=term[k,others].sum()+term[others,k].sum()
            double=term[np.ix_(others,others)].sum()
            geometric=(2*q**(1/(1-u))/(1-q**(1/(1-u))))**(1-u)
            single_bound=a*geometric*(alpha[k]**u*db**u+beta[k]**u*da**u)
            double_bound=(1+2*a*q/(1-q))*(da*db)**u
            assert single<=single_bound+2e-12 and double<=double_bound+2e-12
            assert abs(total-central-single-double)<1e-12
            max_scaled_excess=max(max_scaled_excess,(total-1)/q**(1/(1-u)))
            for distance in (1,2,3):
                far=abs(indices-k)>=distance
                mass=term[k,far].sum()+term[far,k].sum()
                factor=(2*q**(distance/(1-u))/(1-q**(1/(1-u))))**(1-u)
                assert mass<=a*factor*(alpha[k]**u*db**u+beta[k]**u*da**u)+2e-12
            cases+=1
    tensor=0
    for dims in ((2,2),(3,2),(2,2,2)):
        tuples=list(product(*(range(n) for n in dims)))
        primes=(2,3,5)[:len(dims)]
        integers=[prod(p**e for p,e in zip(primes,v)) for v in tuples]
        for u,s in ((.6,.7),(.75,.6),(.85,.3)):
            kernels=[np.array([[p**(-s*abs(i-j)) for j in range(n)] for i in range(n)]) for p,n in zip(primes,dims)]
            big=kernels[0]
            for k in kernels[1:]: big=np.kron(big,k)
            arithmetic=np.array([[(x*y/gcd(x,y)**2)**(-s) for y in integers] for x in integers])
            assert np.max(abs(big-arithmetic))<1e-12
            for _ in range(20):
                x=NP.random(len(tuples)); y=NP.random(len(tuples)); x/=x.sum(); y/=y.sum()
                # These distributions need not factor into prime-coordinate laws.
                lhs=x**u@big@y**u
                bound=prod(max(k.sum(axis=1)) for k in kernels)
                assert lhs<=bound+1e-12
                # Check an actual first-coordinate slicing identity.
                xx=x.reshape(dims[0],-1); yy=y.reshape(dims[0],-1)
                rest=kernels[1]
                for k in kernels[2:]: rest=np.kron(rest,k)
                sliced=sum(kernels[0][i,j]*(xx[i]**u@rest@yy[j]**u) for i in range(dims[0]) for j in range(dims[0]))
                assert abs(lhs-sliced)<1e-12
                tensor+=1
    # Inflation on the diagonal already changes a point-mass kernel total.
    assert 2*1**.75>1
    OUT['coordinate_kernel']={'explicit_three_part_bounds':cases,'dependent_tensor_models':tensor,
        'max_observed_scaled_excess':max_scaled_excess,
        'scope':'Explicit finite bounds and slicing; not a determination of the asymptotic universal constant.'}


def orbit_checks():
    matching=variance=clipping=0
    for p in (2,3,5,7):
        for _ in range(30):
            plus=[F(RNG.randrange(1,8),32) for _ in range(3)]
            minus=[F(RNG.randrange(1,8),32) for _ in range(3)]
            ps,ms=sum(plus),sum(minus); matched=min(ps,ms)
            coupling=[[matched*x*y/(ps*ms) for y in minus] for x in plus]
            left=[plus[i]-sum(coupling[i]) for i in range(3)]
            right=[minus[j]-sum(coupling[i][j] for i in range(3)) for j in range(3)]
            colors=[RNG.randrange(p) for _ in plus]
            totals=[]; retained_plus=[F(0)]*3; retained_minus=[F(0)]*3
            for g in range(p):
                success=[int(g==c) for c in colors]
                pout=[plus[i]*success[i] for i in range(3)]
                mout=[sum(coupling[i][j]*(1-success[i]) for i in range(3))+right[j]*F(p-1,p) for j in range(3)]
                assert sum(pout)+sum(mout)<=max(ps,ms)
                for i in range(3):
                    retained_plus[i]+=pout[i]/p; retained_minus[i]+=mout[i]/p
                totals.append(sum(pout)+sum(mout))
            assert retained_plus==[x/p for x in plus]
            assert retained_minus==[x*F(p-1,p) for x in minus]
            matching+=1
            old=F(1,2*p)
            coeff=[F(RNG.randrange(1,5),100*p) for _ in range(3)]
            colors=[RNG.randrange(p) for _ in coeff]
            post=[[old+sum(c*(int((k+g)%p==color)-F(1,p)) for c,color in zip(coeff,colors)) for k in range(p)] for g in range(p)]
            assert min(min(row) for row in post)>=0
            for k in range(p): assert sum(row[k] for row in post)/p==old
            actual=sum(y*y for y in post[0])-p*old*old
            variances=sum(sum((row[k]-old)**2 for row in post)/p for k in range(p))
            assert actual==variances>=0
            for row in post: assert sum(y*y for y in row)==sum(y*y for y in post[0])
            merged=sum(post[0]); assert merged<=1
            assert merged**2>=sum(y*y for y in post[0])
            deletion=merged*F(RNG.randrange(0,9),8)
            assert merged**2-(merged-deletion)**2<=2*deletion
            variance+=1
            children=[F(RNG.randrange(0,9),8) for _ in range(RNG.randrange(0,6))]
            newborn=F(RNG.randrange(0,9),8)
            x=sum(children)+newborn
            assert sum(c*c for c in children)<=x
            if x>1: assert x-1<=x*x-sum(c*c for c in children)
            clipping+=1
    assert F(1,2)**2+F(1,2)**2<1  # Splitting costs energy without losing mass.
    OUT['orbit_accounting']={'correlated_matching_models':matching,'cyclic_variance_models':variance,
        'clipping_models':clipping,'uncharged_class_split_control':True}


def partitions(n,minimum=1):
    if n==0:
        yield ()
    for first in range(minimum,n+1):
        for tail in partitions(n-first,first):
            yield (first,)+tail


def grouping_checks():
    cases=exceptional=0
    for denominator in range(2,33):
        for parts in partitions(denominator):
            if 3*max(parts)>=2*denominator: continue
            sums=1
            for p in parts: sums |= sums<<p
            interior=any((sums>>value)&1 for value in range(1,denominator) if denominator<3*value<2*denominator)
            triple=len(parts)==3 and 3*parts[0]==denominator and len(set(parts))==1
            assert interior or triple
            if triple: assert not interior
            cases+=1; exceptional+=triple
    assert not any(F(1,3)<sum(s)<F(2,3) for s in subsets((F(1,3),F(2,3))))
    OUT['factor_grouping']={'exhaustive_rational_partitions':cases,'exceptional_three_thirds':exceptional,
        'two_thirds_boundary_control':True}


def stopping_checks():
    # Each distinct formal prime has one bin, surrogate size, and multiplicative weight.
    bins=[0,0,1,1,1,2]
    lower=[7,4,2]
    factors=list(range(len(bins)))
    weights=[F(2,3),F(-1,2),F(3,4),F(-2,5),F(5,7),F(1,3)]
    models=terms=0
    for start,threshold in product((1,3),(8,25,60,150,500)):
        if start>=threshold: continue
        original=F(0)
        # Formal squarefree kernel: count each full m with a nonconstant weight.
        def kernel(ms):
            if len(set(ms))!=len(ms): return F(0)
            return F(1+sum(i+1 for i in ms),1+len(ms))
        for full in subsets(factors):
            running=start; stopped=False
            for i in sorted(full,key=lambda i:bins[i]):
                running*=lower[bins[i]]
                if running>=threshold:
                    stopped=True; break
            if stopped: original+=prod(weights[i] for i in full)*kernel(full)
        separated=F(0)
        for finalbin in range(3):
            for selected in subsets(factors):
                if any(bins[i]>finalbin for i in selected): continue
                k=sum(bins[i]==finalbin for i in selected)
                if not k: continue
                running=start*prod(lower[bins[i]] for i in selected)
                if not F(running,lower[finalbin])<threshold<=running: continue
                # This side has no information about the remaining factors.
                beta=prod(weights[i] for i in selected)
                for remaining in subsets(factors):
                    if any(bins[i]<finalbin for i in remaining): continue
                    ell=sum(bins[i]==finalbin for i in remaining)
                    alpha=prod(weights[i] for i in remaining)
                    separated+=beta*alpha*kernel(selected+remaining)/comb(k+ell,k)
                    terms+=1
        assert separated==original
        models+=1
    # Actual sizes within a bin can make only one of two selections cross.
    assert sum(int(x>=5) for x in (4,6))*F(1,2)==F(1,2)!=1
    OUT['stopping_bin']={'exact_independent_coefficient_models':models,'collected_terms_including_overlaps':terms,
        'unequal_exact_size_control':True}


def finite_map_checks():
    cases=0
    for nt in range(0,5):
        for nw in range(1,4):
            for mapping in product(range(nw),repeat=nt):
                covered=set(mapping)
                for good in subsets(range(nt)):
                    good=set(good); discarded=set(range(nt))-good
                    r=Counter(mapping[i] for i in good)
                    collisions=sum(v*(v-1) for v in r.values())
                    for ex in subsets(range(nw)):
                        ex=set(ex)
                        if set(range(nw))-ex-covered: continue
                        star=ex|{mapping[i] for i in discarded}|{w for w,v in r.items() if v>=2}
                        preimage={i for i,w in enumerate(mapping) if w in star}
                        assert -len(ex)<=nt-nw<=len(discarded)+F(collisions,2)
                        assert len(star)<=len(ex)+len(discarded)+F(collisions,2)
                        assert len(preimage)<=len(ex)+2*len(discarded)+collisions
                        outside=[mapping[i] for i in range(nt) if i not in preimage]
                        assert len(outside)==len(set(outside)) and set(outside)==set(range(nw))-star
                        cases+=1
    crowded=[0]*100
    assert len(set(crowded))==1 and len(crowded)==100
    OUT['finite_maps']={'exhaustive_map_partition_exception_models':cases,'single_exceptional_value_control_fiber_size':100}


def phase_checks():
    cases=0
    phases=[F(i,32) for i in range(32)]
    # Discontinuous phase function, plus bounded approximant perturbations.
    limit=lambda s: F(1)+int(s>=F(1,2))+F(1,3)*int(s==F(1,4))
    approx=lambda h,s: limit(s)+F((-1)**h,h)*(2*int(s<F(1,3))-1)
    for h,k,s in product(range(1,24),range(1,24),phases):
        assert abs(approx(h,s)-approx(k,s))<=F(1,h)+F(1,k)
        assert abs(approx(h,s)-limit(s))<=F(1,h)
        cases+=1
    # Exact phases for theta(x)=frac(x): x=N+s, unbounded N.
    for s in phases:
        for n in (10,100,1000):
            x=n+s; assert x-int(x)==s
    # H-dependent C_H(x)=H gives zero comparison error but non-Cauchy coefficients.
    dependent=lambda h,s: h
    assert all(dependent(h,s)-h==0 for h in range(1,20) for s in phases)
    assert abs(dependent(20,F(0))-dependent(1,F(0)))==19
    # A rational phase schedule misses an irrational point; arbitrary values there are invisible.
    # Use a symbolic distinct point to avoid mistaking a float for an irrational proof.
    missed='irrational point not in the rational schedule'
    invisible=lambda h,s: h if s==missed else 0
    assert all(invisible(h,s)==0 for h in range(1,20) for s in phases)
    assert abs(invisible(20,missed)-invisible(1,missed))==19
    OUT['common_phase_comparison']={'discontinuous_exact_inequality_models':cases,
        'exact_phase_samples':96,'dependent_comparison_and_unvisited_phase_controls':True}


def marked_prefix(m,threshold):
    r,q=m-1,m; ns=[]; skipped=0; records=[]
    while r>0 and (threshold is None or q<threshold):
        a=(q+r-1)//r; n=a if a!=m else m+1
        skipped+=a==m
        assert n<=q+1
        old=F(r,q)
        r,q=n*r-q,n*q
        assert 0<=r<2*m and F(r,q)==old-F(1,n)
        assert F(r,q)<F(1,n)
        records.append((n,r,q)); ns.append(n)
    assert skipped<=1 and ns==sorted(set(ns)) and m not in ns
    assert F(1,m)+sum(F(1,n) for n in ns)+F(r,q)==1
    return ns,r,q,skipped


def expansions(target,k,minimum=2):
    if k==1:
        if target.numerator==1 and target.denominator>=minimum:
            yield (target.denominator,)
        return
    lo=max(minimum,(target.denominator+target.numerator-1)//target.numerator)
    hi=(k*target.denominator)//target.numerator
    for n in range(lo,hi+1):
        remainder=target-F(1,n)
        if remainder>0:
            for tail in expansions(remainder,k-1,n+1): yield (n,)+tail


def pad(ns,marker):
    ns=list(ns)
    b=ns[-1] if marker!=ns[-1] else ns[-2]
    new=(b+1,b*(b+1))
    if marker in new:
        factor=next((a for a in range(2,int(b**.5)+1) if b%a==0),None)
        assert factor is not None,(ns,marker,b)
        new=(b+factor,(b//factor)*(b+factor))
    ns.remove(b); ns.extend(new)
    assert len(ns)==len(set(ns)) and marker in ns and sum(F(1,n) for n in ns)==1
    return tuple(sorted(ns))


def marked_checks():
    cases=skips=complete=padding=0
    for m in range(4,501):
        for factor in (2,5,50):
            threshold=factor*m*m
            ns,r,q,skipped=marked_prefix(m,threshold)
            assert q<threshold*threshold
            assert len(ns)<3+log2(log2(threshold))
            if r:
                assert q>=threshold and F(r,q)<F(2*m,threshold)<=F(1,m)
                assert all(F(r,q)<F(1,n) for n in ns)
            cases+=1; skips+=skipped
        if m<=45:
            ns,r,q,_=marked_prefix(m,None)
            assert r==0
            complete+=1
    counts={}
    for length in (3,4,5):
        samples=list(expansions(F(1),length))
        counts[length]=len(samples)
        for ns in samples:
            for marker in ns:
                out=pad(ns,marker)
                assert len(out)==length+1
                padding+=1
    OUT['marked_prefix']={'bounded_prefix_models':cases,'skipped_marker_events':skips,
        'complete_unbounded_runs':complete,'enumerated_expansions_by_length':counts,'all_marker_padding_models':padding}


def descent_checks():
    cases=identities=0
    for x,y in ((20,10),(30,10),(40,20),(60,15)):
        rho=F(y,x)
        for _ in range(25):
            # Duplicated shifts remain separately indexed.
            shifts=[RNG.randrange(1,200) for _ in range(5)]; shifts += shifts[:2]
            good={h for h in range(1,y+1) if RNG.randrange(3)==0}
            bad=set(range(1,y+1))-good
            bigbad=[]; exceptional=[]
            for u in range(y+1,x+1):
                residues=[(-n)%u for n in shifts]
                if any(h in good or h==0 for h in residues): continue
                bigbad.append(u)
                if sum(h<=y for h in residues)<rho*len(shifts)/2: exceptional.append(u)
            hset=bad|set(bigbad)
            d=[[sum((n+h)%v==0 for v in range(1,x+1)) for h in range(1,y+1)] for n in shifts]
            right=len(exceptional)+len(bad)+F(2,1)/(rho*len(shifts))*sum(row[h-1] for row in d for h in bad)
            assert len(hset)<=right
            for order in (2,3,5):
                moment=max(sum(value**order for value in row)/y for row in d)**(1/order)
                delta=len(bad)/y
                bound=len(exceptional)/x+float(rho)*delta+2*moment*delta**(1-1/order)
                assert len(hset)/x<=bound+1e-10
            cases+=1
    for m in (12,24,36,60):
        divisors=[i for i in range(1,m+1) if m%i==0]
        for c,cn,t,u in product((1,6),(1,),divisors,range(1,m)):
            z=(c*t+u-1)//u; h=u*z-c*t
            assert F(u,m*c)==F(1,(m//t)*z)+F(1,z*c//cn)*F(h,m*cn)
            identities+=1
    recurrence=0
    for alpha,loga,logeps,depth in product((.5,.75,.9,.99),(0,1,10),(-3,-50,-500),(1,3,10,40)):
        current=-np.inf
        for _ in range(depth): current=np.logaddexp(logeps,loga+alpha*current)
        terms=[(1-alpha**i)/(1-alpha)*loga+alpha**i*logeps for i in range(depth)]
        bound=np.logaddexp.reduce(terms)
        assert current<=bound+1e-9
        recurrence+=1
    OUT['indexed_descent']={'residue_predecessor_models':cases,'exact_scale_transfer_identities':identities,
        'log_domain_recurrence_models':recurrence,'duplicate_list_indices_retained':True}


if __name__=='__main__':
    for check in (coordinate_checks,orbit_checks,grouping_checks,stopping_checks,finite_map_checks,
                  phase_checks,marked_checks,descent_checks):
        check(); print(check.__name__,'passed',flush=True)
    result={'batch':'B017','python':sys.version.split()[0],'numpy':np.__version__,'checks':OUT,
        'scope':'Selected finite mechanisms and explicit numerical bounds; not global number-theory or Lean proof certification.'}
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(OUT,indent=2))
