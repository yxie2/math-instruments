"""Finite models and a complete reconstruction of the pinned Snaky certificate."""
from fractions import Fraction as F
from itertools import product, combinations
from math import comb, prod
from pathlib import Path
import hashlib
import json
import re
import sys
import numpy as np
from scipy.optimize import linprog, brentq

OUT={}
RNG=np.random.default_rng(20187)


def arrangement_checks():
    cases=patterns=zeros=0
    for e in (1,2,3):
        for s in (2,3,4,5):
            for trial in range(3):
                a=RNG.integers(-2,3,(s,e)).astype(float)
                for row in a:
                    if not np.any(row):row[0]=1
                b=RNG.integers(-2,3,s).astype(float)
                if trial==0 and s>2:a[-1]=a[0];b[-1]=b[0]
                count=strict=0
                for signs in product((-1,0,1),repeat=s):
                    ub=[];rhs=[];eq=[];erhs=[]
                    for j,sign in enumerate(signs):
                        if sign:ub.append([*(-sign*a[j]),1]);rhs.append(sign*b[j])
                        else:eq.append([*a[j],0]);erhs.append(-b[j])
                    opt=linprog([0]*e+[-1],A_ub=ub or None,b_ub=rhs or None,
                        A_eq=eq or None,b_eq=erhs or None,bounds=[(None,None)]*e+[(0,1)],method='highs')
                    if opt.success and opt.x[-1]>1e-8:
                        count+=1;strict+=0 not in signs;zeros+=0 in signs
                bound=sum(comb(s,d)*sum(comb(s,j) for j in range(min(s,e-d)+1)) for d in range(min(s,e)+1))
                assert count<=bound<=(e+1)**2*(s+1)**e
                assert strict<=sum(comb(s,j) for j in range(min(s,e)+1))
                cases+=1;patterns+=count
    OUT['affine_signs']={'arrangements':cases,'realized_patterns':patterns,'patterns_with_zeros':zeros,'method':'floating-point strict-feasibility linear programs, including duplicates'}


def digit_checks():
    colorings=aps=0;composite=0
    for n in range(2,9):
        for k in (3,4,5):
            for c in product((0,1),repeat=n):
                if any(len({c[(a+j*d)%n] for j in range(k)})==1 for a in range(n) for d in range(1,n)):continue
                # All valid cyclic colorings at these sizes are tested, with two digits.
                lifted=[(c[x%n],c[(x//n)%n]) for x in range(n*n)]
                for d in range(1,(n*n-1)//(k-1)+1):
                    i=0;e=d
                    while e%n==0:i+=1;e//=n
                    for a in range(n*n-(k-1)*d):
                        assert len({lifted[a+j*d] for j in range(k)})>1
                        assert all(((a+j*d)//(n**i))%n==((a//(n**i))+j*e)%n for j in range(k))
                        aps+=1
                colorings+=1;composite+=n in (4,6,8)
    assert colorings and composite
    OUT['cyclic_digits']={'valid_cyclic_colorings':colorings,'composite_base_colorings':composite,'integer_progressions':aps}


def density(w,edges,v):
    n=len(w)
    return sum(prod(w[x[a]][x[b]] for a,b in edges) for x in product(range(n),repeat=v))/n**v


def finite_host_checks():
    kernels=[[[F(1,4),F(3,4)],[F(3,4),F(1,2)]],[[F(0),F(1)],[F(1),F(0)]]]
    patterns=[(3,[(0,1),(1,2)]),(3,[(0,1),(1,2),(0,2)]),(4,[(0,1),(1,2),(2,3),(3,0)])]
    models=0
    for w in kernels:
        mu=density(w,[(0,1)],2)
        for n in (2,3,4):
            hostpairs=list(combinations(range(n),2));et=[F(0)]*len(patterns);ep=F(0);epow=[F(0)]*len(patterns)
            for labels in product(range(2),repeat=n):
                for bits in product((0,1),repeat=len(hostpairs)):
                    probability=F(1,2**n)
                    a=[[F(0) for _ in range(n)] for _ in range(n)]
                    for (x,y),bit in zip(hostpairs,bits):
                        z=w[labels[x]][labels[y]];probability*=z if bit else 1-z
                        a[x][y]=a[y][x]=F(bit)
                    if not probability:continue
                    p=density(a,[(0,1)],2);ep+=probability*p
                    for j,(v,edges) in enumerate(patterns):
                        et[j]+=probability*density(a,edges,v);epow[j]+=probability*p**len(edges)
            assert ep==(1-F(1,n))*mu
            for j,(v,edges) in enumerate(patterns):
                tau=density(w,edges,v);m=len(edges)
                assert abs(et[j]-tau)<=F(comb(v,2),n)
                assert epow[j]>=ep**m>=mu**m*(1-F(m,n))
                models+=1
    # A collapsed pair of leaves reuses one Bernoulli edge, rather than two independent ones.
    assert F(1,3)!=F(1,3)**2
    mu=F(1,2);delta=mu**3;n=28
    assert n>(3+3*mu**3)/delta
    OUT['finite_host_transfer']={'exact_expected_density_models':models,'strict_triangle_witness_threshold':n,'bipartite_counterexample_constructed':False}


def forcing_checks():
    cycle=[(0,1),(1,2),(2,3),(3,0)];triangle=[(0,1),(1,2),(0,2)]
    cases=0
    for p in (F(1,4),F(1,2),F(3,4)):
        d=min(p,1-p)/2;w=[[p+d,p-d],[p-d,p+d]]
        for v,edges in ((3,triangle),(4,cycle),(3,[(0,1),(1,2)])):
            expansion=F(0)
            for bits in product((0,1),repeat=len(edges)):
                degrees=[0]*v
                for bit,(a,b) in zip(bits,edges):degrees[a]+=bit;degrees[b]+=bit
                if all(x%2==0 for x in degrees):expansion+=p**(len(edges)-sum(bits))*d**sum(bits)
            assert density(w,edges,v)==expansion
            cases+=1
    # Triangle is a small model of the transfer argument, not the source's bipartite H.
    w0=np.array([[0.,1.],[1.,0.]]);p=.5;d=.25
    signs=[-1,1];states=list(product(range(2),signs))
    def kernel(s):return [[(1-s)*w0[x,y]+s*(p+d*a*b) for y,b in states] for x,a in states]
    root=brentq(lambda s:density(kernel(s),triangle,3)-p**3,0,1,xtol=1e-14)
    w=kernel(root);variance=np.mean((np.array(w)-p)**2)
    assert abs(density(w,triangle,3)-p**3)<1e-12
    assert abs(variance-((1-root)**2*p*(1-p)+root**2*d*d))<1e-12
    assert density(w,cycle,4)>p**4+1e-5
    OUT['constant_density_interpolation']={'exact_even_subgraph_expansions':cases,'triangle_model_root':root,'nonconstant_variance':variance,'C4_excess':density(w,cycle,4)-p**4,'source_H_deficit_verified':False}


def unit_checks():
    cases=0
    for p in (2,3,5,7):
        for k in (1,2,3):
            t=p**k;mod=p**(k+2)
            for a,b in product(range(p*2),repeat=2):
                u=(1+t*a)%mod;v=(1+t*b)%mod
                assert (((u*v)%mod-1)//t)%p==(a+b)%p
                assert ((pow(u,-1,mod)-1)//t)%p==(-a)%p
                cases+=1
            # Principal units of the finite quotient have p-power order.
            for a in range(p**2):assert pow(1+t*a,p**(k+2),mod)==1
    OUT['principal_units']={'product_and_inverse_models':cases,'domain_theorem_proved_by_finite_models':False,'prime_to_residue_torsion_hypothesis_retained':True}


def binary_checks():
    cases=0
    for h0,h1,h2,h3 in product((-1,1),repeat=4):
        c=(h0+h1+h2+h3)//2;d=(h0-h1+h2-h3)//2
        g=complex((h0-h2)//2,(h1-h3)//2);b=(h1+h3)//2
        u=complex((h2-1)//2,(h3-1)//2)
        assert h2+1j*h3==(1+1j)+2*u
        assert d-c==-2*b
        assert g-c==(1j-1)*b-(h2+1j*h3)
        if abs(c)==1:
            lr=complex(-b/c);lw=(g/c-1)/(1+1j)
            assert abs(lw.real-round(lw.real))<1e-10 and abs(lw.imag-round(lw.imag))<1e-10
            assert round(lr.real+lr.imag+lw.real+lw.imag)%2==1
            cases+=1
    # At order four, W=i is residue one at (1+i), but is not odd-order torsion.
    assert (1j-1)/(1+1j)==1j and 1j!=1
    # F4=F2[z]/(z^2+z+1): the nontrivial C3 character sums to zero.
    assert 1^2^3==0 and (1^1^1)==1
    OUT['binary_first_order_obstruction']={'all_sign_quadruples':16,'unit_denominator_cases':cases,'order_four_even_torsion_control':True,'alternating_product_input_verified':False}


def snaky_checks():
    data=Path(__file__).with_name('data').joinpath('snaky21.txt').read_bytes()
    digest=hashlib.sha256(data).hexdigest()
    assert digest=='3fa12d36a6d4dbb185e3f2808c8dfde13d85ee309afbca030d6ad17ae9fe3d04'
    shape=frozenset(((0,0),(1,0),(2,0),(3,0),(3,1),(4,1)))
    order=((0,0),(1,0),(2,0),(3,0),(3,1),(4,1))
    cards=[(shape-{q},shape,1) for q in order]
    stats={'nodes':0,'references':0,'inline_nodes':0,'local_reply_classes':0,'normalizations':0}
    symbols='0123456789ABCDEFG'
    def point(token):
        assert len(token)==2 and all(c in symbols for c in token)
        return tuple(symbols.index(c) for c in token)
    def placed(token):
        match=re.fullmatch(r'(\d+)(?::([0-7])([0-9A-G]{2}))?',token)
        assert match is not None
        index=int(match[1]);assert 0<=index<len(cards)
        s=int(match[2] or 0);dx,dy=point(match[3]) if match[3] else (0,0)
        matrix=np.array([[0,1],[1,0]],dtype=int) if s&1 else np.eye(2,dtype=int)
        matrix=matrix@np.diag([-1 if s&2 else 1,-1 if s&4 else 1])
        def transform(cells):return frozenset(tuple(int(t) for t in matrix@np.array(q)+[dx,dy]) for q in cells)
        a,t,h=cards[index];stats['references']+=1
        return transform(a),transform(t),h
    def combine(p,children):
        assert children
        owned=set().union(*(c[0] for c in children))
        common=set.intersection(*(set(c[1]) for c in children))
        a=(owned|common)-{p};t=set().union({p},*(c[1] for c in children));h=1+max(c[2] for c in children)
        assert a<=t and p not in a
        after=a|{p}
        for reply in list(t-after)+[None]:
            survivors=[c for c in children if reply not in c[1]]
            assert survivors and all(c[0]<=after and c[1]<=t and c[2]<h for c in survivors)
            stats['local_reply_classes']+=1
        # Reduced envelopes, normalized back to full envelopes, give the same card.
        reduced=[(set(c[0]),set(c[1])-c[0]) for c in children]
        u=set().union(*(c[0] for c in reduced));v=set().union(*(c[1] for c in reduced))
        intersection=set.intersection(*(c[1] for c in reduced));required=u|intersection
        pp=required-{p};ee=(v-required)|{p}
        assert pp==a and pp|ee==t
        stats['normalizations']+=1;stats['nodes']+=1
        return frozenset(a),frozenset(t),h
    for line in data.decode('ascii').splitlines():
        tokens=re.findall(r'\(|\)|[^\s()]+',line)
        assert int(tokens[0])==len(cards)
        stack=[(point(tokens[1]),[])];pos=2
        while pos<len(tokens):
            token=tokens[pos];pos+=1
            if token=='(':
                stack.append((point(tokens[pos]),[]));pos+=1;stats['inline_nodes']+=1
            elif token==')':
                assert len(stack)>1
                p,children=stack.pop();stack[-1][1].append(combine(p,children))
            else:stack[-1][1].append(placed(token))
        assert len(stack)==1
        p,children=stack.pop();cards.append(combine(p,children))
    a,t,h=cards[-1]
    assert len(cards)==728 and not a and len(t)==251 and h==21
    assert all(0<=x<=16 and 0<=y<=16 for x,y in t)
    assert max(c[2] for c in cards)==21
    assert stats['nodes']==1620 and stats['inline_nodes']==898 and stats['references']==4089
    OUT['snaky21_reconstruction']={**stats,'sha256':digest,'numbered_cards':len(cards),'final_required_cells':len(a),'final_support_cells':len(t),'final_height':h,'formal_proof_build':False,'executable_playing_policy_tested':False}


def reduced_checks():
    cases=0;universe=set(range(6))
    for _ in range(1000):
        children=[(set(RNG.choice(6,size=int(RNG.integers(0,7)),replace=False)),set(RNG.choice(6,size=int(RNG.integers(0,7)),replace=False))) for _ in range(int(RNG.integers(1,5)))]
        p=int(RNG.integers(0,6));u=set().union(*(a for a,e in children));v=set().union(*(e for a,e in children));i=set.intersection(*(e for a,e in children));hh=u|i
        pp=hh-{p};ee=(v-hh)|{p}
        full=[(a,a|e) for a,e in children]
        a=(u|set.intersection(*(t for _,t in full)))-{p};t=set().union({p},*(t for _,t in full))
        assert a==pp and t==pp|ee
        for _ in range(4):
            m=set(RNG.choice(6,size=int(RNG.integers(0,7)),replace=False));b=universe-m
            assert (pp<=m and not b&ee)==(pp<=m and not b&(pp|ee))
        cases+=1
    OUT['reduced_envelopes']={'overlapping_required_and_envelope_models':cases,'route25_table_reconstructed':False}


if __name__=='__main__':
    if not __debug__:raise SystemExit('Assertions must be enabled.')
    for check in (arrangement_checks,digit_checks,finite_host_checks,forcing_checks,unit_checks,binary_checks,snaky_checks,reduced_checks):
        check();print(check.__name__,'passed',flush=True)
    result={'batch':'B020','python':sys.version.split()[0],'numpy':np.__version__,'checks':OUT,'scope':'Finite mechanism models and full Snaky 21 certificate reconstruction; no Lean build or certification of the other headline claims.'}
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(OUT,indent=2))
