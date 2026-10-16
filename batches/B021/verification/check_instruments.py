"""Exact finite models for selected logical mechanisms; no foundational theorem certification."""
from fractions import Fraction as F
from itertools import product, permutations
from math import comb, gcd
from pathlib import Path
import json
import random
import sys

R=random.Random(21245);OUT={}


def recovery_checks():
    runs=steps=0
    for denominator in (11,19,31):
        for numerator in range(1,denominator):
            t=F(numerator,denominator);delta=F(1,20);lo=F(-7,10);hi=F(3,5);s=F(0);ones=0
            for n in range(1,1001):
                bit=0 if s<=lo+delta else 1 if s>=hi-delta else R.randrange(2)
                s+=delta*(t-bit);ones+=bit
                assert lo<=s<=hi
                assert s==delta*(n*t-ones)
                assert abs(t-F(ones,n))<1/(n*delta)
                steps+=1
            runs+=1
    OUT['bounded_recovery']={'exact_rational_runs':runs,'arbitrary_interior_decisions':steps,'Borel_uniformization_tested':False,'irrational_cut_termination_tested':False}


def transcript_checks():
    queries=[F(-1),F(0),F(1),F(0)];accepted=0;rejected=0
    for bits in product((0,1),repeat=8):
        valid=True
        for coordinate in range(2):
            table=list(zip(queries,bits[4*coordinate:4*coordinate+4]))
            lower=max([F(-2)]+[q for q,b in table if b]);upper=min([F(2)]+[q for q,b in table if not b])
            if lower>=upper:valid=False;continue
            witness=(lower+upper)/2
            assert all((q<witness)==bool(b) for q,b in table)
        accepted+=valid;rejected+=not valid
    assert accepted==16
    OUT['cut_transcripts']={'two_coordinate_tables':accepted+rejected,'open_rectangle_transcripts':accepted,'category_cone_theorem_tested':False}


def branch_checks():
    cases=0;without_freezing=0
    for a,b in product(range(6),repeat=2):
        solutions=[];loose=0
        # max(a,b): case 0 a>=b with slack u; case 1 b>a with slack v.
        for e,h,u,v in product(range(2),range(6),range(7),range(7)):
            equations=[e*(a-b-u),e*(h-a),(1-e)*(b-a-1-v),(1-e)*(h-b)]
            if not any(equations):
                loose+=1
                if (1-e)*u==0 and e*v==0:solutions.append((e,h,u,v))
        assert len(solutions)==1 and solutions[0][1]==max(a,b)
        assert loose>1;without_freezing+=loose;cases+=1
    OUT['unique_branch_witnesses']={'exact_max_inputs':cases,'unfrozen_spurious_multiplicity':without_freezing,'ties_assigned_to_one_branch':True}


def rational_checks():
    seen={};valid=0
    for p,n in product(range(21),repeat=2):
        if p*n:continue
        for d in range(1,21):
            for t in range(d):
                numerator=(p+n)*t+d-1
                if numerator%d:continue
                q=numerator//d;s=d-1-t;code=(p,n,d,t,s,q);value=F(p-n,d)
                assert value not in seen or seen[value]==code
                seen[value]=code;valid+=1
    for z,code in seen.items():
        p,n,d,t,s,q=code
        assert gcd(p+n,d)==1 and d==1+t+s and (p+n)*t+d==1+q*d
        assert (p-n,d)==(z.numerator,z.denominator)
    assert seen[F(0)]==(0,0,1,0,0,0)
    values=list(seen);arithmetic=0
    def code(z):
        a=abs(z.numerator);d=z.denominator;t=0 if d==1 else pow(a,-1,d)
        return (max(z.numerator,0),max(-z.numerator,0),d,t,d-1-t,(a*t+d-1)//d)
    for _ in range(400):
        x,y=R.sample(values,2)
        for z in (x+y,x-y,x*y)+(() if y==0 else (x/y,)):
            p,n,d,t,s,q=code(z);assert F(p-n,d)==z and p*n==0 and (p+n)*t+d==1+q*d
            arithmetic+=1
    OUT['rational_codes']={'enumerated_valid_codes':valid,'distinct_values':len(seen),'rational_arithmetic_outputs':arithmetic,'zero_and_denominator_one':True}


def binary_checks():
    cases=members=0
    for y in range(101):
        b=2**(y+1);n=(b+1)**y
        for x in range(y+1):
            h=b**x;q,r=divmod(n,h);s,d=divmod(q,b)
            assert n==s*b*h+d*h+r and r<h and d<b
            assert d==comb(y,x)
            assert (d%2==1)==(x&y==x)
            if d%2:assert d==2*((d-1)//2)+1;members+=1
            cases+=1
    OUT['binary_masking']={'exact_digit_extractions':cases,'true_memberships':members,'single_fold_power_graph_verified':False}


def slicing_checks():
    cases=nonsections=0
    for _ in range(500):
        nx=R.randrange(2,15);ny=R.randrange(1,nx+1);na=nx;eta=R.randrange(1,6)
        f=list(range(ny))+[R.randrange(ny) for _ in range(nx-ny)];R.shuffle(f)
        flat=list(range(nx))+[R.randrange(nx) for _ in range(na*eta-nx)];R.shuffle(flat)
        blocks=[set(flat[i*na:(i+1)*na]) for i in range(eta)];visited=set();source_used=set();assembled={}
        for block in blocks:
            yi={f[x] for x in block}-visited;visited|=yi
            si={x for x in block if f[x] in yi}
            assert not source_used&si;source_used|=si
            candidates=list(si);R.shuffle(candidates)
            injection=dict(zip(sorted(yi),candidates));assert len(injection)==len(yi)
            nonsections+=any(f[x]!=y for y,x in injection.items())
            assembled.update(injection)
        assert set(assembled)==set(range(ny)) and len(set(assembled.values()))==ny
        cases+=1
    assert nonsections
    OUT['ordinal_slices_finite_model']={'presentations':cases,'local_injections_not_sections':nonsections,'nonwellorderable_sets_modeled':False,'choice_preservation_tested':False}


def selector_checks():
    group=list(permutations(range(3)));identity=(0,1,2)
    def mul(a,b):return tuple(a[b[i]] for i in range(3))
    def inv(a):return tuple(a.index(i) for i in range(3))
    def action(s,f):return {g:f[mul(inv(s),g)] for g in group}
    def choose(f):
        for alpha in range(4):
            pattern={g:f[g]%(2**alpha) for g in group}
            if len(set(pattern.values()))==len(group):return min(group,key=pattern.get),alpha
        raise AssertionError('No separating level')
    def preliminary(f):return group[sum((i+1)*f[g] for i,g in enumerate(group))%6]
    def output(f):
        g,_=choose(f);return mul(g,preliminary(action(inv(g),f)))
    cases=bad=0
    for labels in list(permutations(range(6)))[:120]:
        f=dict(zip(group,labels));g,alpha=choose(f)
        for s in group:
            sf=action(s,f);sg,sa=choose(sf)
            assert sa==alpha and sg==mul(s,g)
            assert output(sf)==mul(s,output(f))
            bad+=mul(sg,preliminary(sf))!=mul(s,mul(g,preliminary(f)))
            cases+=1
    assert bad
    OUT['covariant_selection']={'nonabelian_covariance_checks':cases,'unmoved_generic_formula_failures':bad,'infinite_detector_separation_tested':False}


def syntax_checks():
    # de Bruijn syntax, with annotations present in lam and pi.
    def rename(t,r):
        if t[0]=='v':return ('v',r(t[1]))
        if t[0]=='s':return t
        rr=(lambda j:0 if j==0 else r(j-1)+1) if t[0] in ('l','p') else r
        return (t[0],rename(t[1],r),rename(t[2],rr))
    def subst(t,sigma):
        if t[0]=='v':return sigma(t[1])
        if t[0]=='s':return t
        lift=(lambda j:('v',0) if j==0 else rename(sigma(j-1),lambda k:k+1)) if t[0] in ('l','p') else sigma
        return (t[0],subst(t[1],sigma),subst(t[2],lift))
    def sorts(t):return {t[1]} if t[0]=='s' else set() if t[0]=='v' else sorts(t[1])|sorts(t[2])
    def steps(t):
        result=[]
        if t[0] in ('v','s'):return result
        if t[0]=='a' and t[1][0]=='l':result.append(subst(t[1][2],lambda j:t[2] if j==0 else ('v',j-1)))
        result += [(t[0],u,t[2]) for u in steps(t[1])]
        result += [(t[0],t[1],u) for u in steps(t[2])]
        return result
    def gen(depth):
        if depth==0:return ('s',R.randrange(5)) if R.randrange(2) else ('v',R.randrange(4))
        tag=R.choice(('a','l','p'));return (tag,gen(depth-1),gen(depth-1))
    count=0
    for _ in range(600):
        term=gen(3)
        for reduct in steps(term):assert sorts(reduct)<=sorts(term);count+=1
    s=('s',0);t=('s',1);body=('a',('v',0),('v',0));omega=('a',('l',s,body),('l',s,body))
    assert omega in steps(omega)
    erasing=('a',('l',s,t),omega);assert t in steps(erasing) and erasing in steps(erasing)
    annotation=('l',omega,('v',0));assert annotation in steps(annotation)
    extra=('a',('l',('s',99),t),s);assert t in steps(extra) and 99 not in sorts(t)
    OUT['finite_syntax_support']={'random_full_beta_steps':count,'annotation_reduction_control':True,'raw_weak_not_strong_control':True,'conversion_expansion_can_add_sorts':True,'typing_metatheory_verified':False}


def signed_fixed_checks():
    cases=0;comparisons=0
    for n in range(1,7):
        vectors=list(product((0,1),repeat=n))
        for _ in range(30):
            signs=[R.randrange(2) for i in range(n)]
            parents=[R.sample(range(n),R.randrange(1,n+1)) for i in range(n)]
            modes=[R.randrange(2) for i in range(n)]
            def flip(v):return tuple(v[i]^signs[i] for i in range(n))
            def f(v):
                y=flip(v);z=tuple((max if modes[i] else min)(y[j] for j in parents[i]) for i in range(n))
                return flip(z)
            def le(v,w):return all(a<=b for a,b in zip(flip(v),flip(w)))
            for v in vectors:
                for w in vectors:
                    if le(v,w):assert le(f(v),f(w));comparisons+=1
            post=[v for v in vectors if le(v,f(v))]
            join=flip(tuple(max(flip(v)[i] for v in post) for i in range(n)))
            assert f(join)==join
            # Search the doubled signed graph for an odd closed walk.
            for start in range(n):
                reached={(start,0)};pending=[(start,0)]
                while pending:
                    i,parity=pending.pop()
                    for j in parents[i]:
                        state=(j,parity^signs[i]^signs[j])
                        if state not in reached:reached.add(state);pending.append(state)
                assert (start,1) not in reached
            cases+=1
    assert all(1-x!=x for x in (0,1))
    OUT['mixed_order_fixed_points']={'finite_lattice_models':cases,'comparable_pairs':comparisons,'odd_negative_loop_no_fixed_point_control':True,'general_candidate_interface_verified':False}


if __name__=='__main__':
    if not __debug__:raise SystemExit('Assertions must be enabled.')
    for check in (recovery_checks,transcript_checks,branch_checks,rational_checks,binary_checks,slicing_checks,selector_checks,syntax_checks,signed_fixed_checks):
        check();print(check.__name__,'passed',flush=True)
    result={'batch':'B021','python':sys.version.split()[0],'checks':OUT,'scope':'Exact finite models of selected arithmetic, combinatorial and syntactic mechanisms; not global computability, set-theoretic or type-theoretic certification.'}
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(OUT,indent=2))
