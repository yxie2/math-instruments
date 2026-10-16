"""Selected finite algebra and geometry checks; no headline certification."""
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import product, permutations, combinations
from pathlib import Path
import json
import math
import random
import time
import numpy as np
from scipy.linalg import expm, block_diag


def mapping_torus():
    cases=relations=0
    for n in range(2,20):
        for a in range(n):
            image=set(range(n)); steps=0
            while True:
                nxt={a*x%n for x in image}
                if nxt==image: break
                image=nxt; steps+=1
            inverse={a*x%n:x for x in image}; assert len(inverse)==len(image)
            def iterate(x,k):
                for _ in range(abs(k)): x=(a*x%n) if k>=0 else inverse[x]
                return x
            def canonical(x,j): return iterate(a**steps*x%n,-j)
            for x,j in product(range(n),range(4)):
                assert canonical(x,j)==canonical(a*x%n,j+1)
                assert iterate(canonical(x,j),-1)==canonical(x,j+1)
                assert iterate(canonical(x,j),1)==canonical(a*x%n,j); relations+=1
            kernels=[{x for x in range(n) if pow(a,k,n)*x%n==0} for k in range(steps+2)]
            assert kernels[-1]==kernels[-2]
            assert len(image)*len(kernels[-1])==n; cases+=1
    return dict(cyclic_endomorphisms=cases,stage_and_stable_letter_relations=relations)


def action_monoid():
    group=list(permutations(range(3))); identity=(0,1,2)
    alphabet=[('g',g) for g in group]+[('s',i) for i in range(3)]+[('t',i) for i in range(3)]+[('zero',0)]
    def successors(word):
        out=[]
        for i,t in enumerate(word):
            if t[0]=='zero': return [(('zero',0),)] if len(word)>1 else []
            if t==('g',identity): out.append(word[:i]+word[i+1:])
        for i in range(len(word)-1):
            (k,a),(l,b)=word[i:i+2]; replacement=None
            if k==l=='g': replacement=(('g',tuple(a[b[j]] for j in range(3))),)
            elif k=='g' and l=='s': replacement=(('s',a[b]),)
            elif k=='t' and l=='g': replacement=(('t',b.index(a)),)
            elif k=='t' and l=='s': replacement=() if a==b else (('zero',0),)
            if replacement is not None: out.append(word[:i]+replacement+word[i+2:])
        return out
    @lru_cache(None)
    def normal_forms(word):
        nxt=successors(word)
        if not nxt: return frozenset([word])
        return frozenset().union(*(normal_forms(w) for w in nxt))
    cases=0
    for length in range(4):
        for word in product(alphabet,repeat=length): assert len(normal_forms(word))==1; cases+=1
    rng=random.Random(250)
    for _ in range(300):
        word=tuple(rng.choice(alphabet) for _ in range(rng.randrange(4,10)))
        assert len(normal_forms(word))==1; cases+=1
    assert len({next(iter(normal_forms((('g',g),)))) for g in group})==6
    return dict(words_with_all_reduction_orders=cases,embedded_group_size=6)


def idempotent_differences():
    certificates=0; cycles=0
    for p in (2,3):
        vectors=[np.array(v,dtype=int) for v in product(range(p),repeat=3)]
        def key(a): return tuple((a%p).flat)
        def atom(u,l): return key(np.outer(u,l))
        # Signed dictionaries retain negative coefficients, unlike Counter subtraction.
        def add(*terms):
            result=Counter()
            for scalar,c in terms:
                for k,v in c.items(): result[k]+=scalar*v
            return {k:v for k,v in result.items() if v}
        def diff(u,v,l): return add((1,{atom((u+v)%p,l):1}),(-1,{atom(u,l):1}))
        for lam in vectors[1:]:
            affine=[u for u in vectors if int(lam@u)%p==1]
            kernel=[v for v in vectors[1:] if int(lam@v)%p==0]
            for v in kernel:
                for u in affine:
                    for up in affine:
                        if np.array_equal(u,up): continue
                        delta=(up-u)%p
                        dependent=any(np.array_equal(delta,(t*v)%p) for t in range(p))
                        if dependent:
                            w=next(w for w in kernel if not any(np.array_equal(w,(t*v)%p) for t in range(p)))
                            middle=(u+w)%p; comparisons=[(u,middle),(middle,up)]
                        else: comparisons=[(u,up)]
                        for left,right in comparisons:
                            mu=next(mu for mu in vectors if int(mu@left)%p==0 and int(mu@right)%p==0 and int(mu@v)%p==1)
                            for base in (left,right):
                                a=np.outer(base,lam)%p; b=np.outer(v,mu)%p
                                c=np.outer((base+v)%p,lam)%p; d=np.outer(v,(mu-lam)%p)%p
                                assert np.array_equal((a+b)%p,(c+d)%p)
                                for x in (a,b,c,d): assert np.array_equal(x@x%p,x)
                                assert not np.any(a@b%p) and not np.any(b@a%p)
                                assert not np.any(c@d%p) and not np.any(d@c%p)
                                relation=add((1,{key(a):1}),(1,{key(b):1}),(-1,{key(c):1}),(-1,{key(d):1}))
                                assert add((1,diff(base,v,lam)),(1,relation))==add((1,{key(b):1}),(-1,{key(d):1}))
                            certificates+=1
                    telescoped=add(*[(1,diff((u+j*v)%p,v,lam)) for j in range(p)])
                    assert not telescoped; cycles+=1
        # The cross-algebra split is tested as actual prefix-cylinder membership.
        for bits in product((0,1),repeat=5):
            A=bits[:2]==(0,0); A0=bits[:3]==(0,0,0); A1=bits[:3]==(0,0,1)
            B=bits[:2]==(0,1); C=bits[:1]==(1,)
            assert A==A0+A1 and not(A0 and A1) and A+B+C==1
    return dict(rank_one_comparison_certificates=certificates,exact_telescoping_cycles=cycles,
                scope='Checks the matrix identities and signed telescoping used in the proof, not arbitrary homological fillings.')


def cartan():
    rng=np.random.default_rng(254); cases=0; max_error=0.
    for n in (2,3,5,8):
        for _ in range(10):
            B=rng.uniform(.1,1,(n,n)); B=(B+B.T)/2; np.fill_diagonal(B,0)
            eigen,vec=np.linalg.eigh(B); v=abs(vec[:,-1]); B*=2/eigen[-1]
            for gap in (0.,.1,.8):
                BB=B*(1-gap); C=2*np.eye(n)-BB; Cv=C@v; x=rng.normal(size=n)
                rhs=sum(BB[i,j]*v[i]*v[j]*(x[i]/v[i]-x[j]/v[j])**2 for i in range(n) for j in range(i+1,n))+sum(Cv/v*x*x)
                err=abs(x@C@x-rhs); max_error=max(max_error,float(err)); assert err<1e-10
                if gap:
                    assert np.min(np.linalg.eigvalsh(C))>0 and np.min(np.linalg.inv(C))>0
                    boundary=rng.uniform(0,1,n); extension=np.linalg.solve(C,boundary)
                    assert min(extension)>0 and np.linalg.norm(C@extension-boundary)<1e-10
                else: assert np.linalg.norm(Cv)<1e-12
                cases+=1
    return dict(positive_and_null_cases=cases,max_scaled_form_error=max_error)


def centralizer():
    rng=random.Random(255); cases=noncommuting=0
    R=np.array([[0,-1],[1,0]],dtype=int); J=np.diag([1,-1])
    d4=[np.linalg.matrix_power(R,k)@np.linalg.matrix_power(J,j) for k in range(4) for j in range(2)]
    def mul(a,b): return a[0]@b[0],a[1]+a[0]@b[1]
    def length(a):
        Q,t=a; projection=sum(np.linalg.matrix_power(Q,j) for j in range(4))/4
        return float(np.linalg.norm(projection@t))
    def pairing(g,h): return (length(mul(g,h))**2-length(g)**2-length(h)**2)/2
    for _ in range(80):
        D=rng.randrange(1,7); g=(np.eye(3,dtype=int),np.array([D,0,0]))
        hs=[(block_diag(1,rng.choice(d4)),np.array([rng.randrange(-4,5) for _ in range(3)])) for j in range(2)]
        h,k=hs; hk=mul(h,k); kh=mul(k,h)
        noncommuting+=not(np.array_equal(hk[0],kh[0]) and np.array_equal(hk[1],kh[1]))
        assert abs(pairing(g,h)-D*h[1][0])<1e-10
        assert abs(pairing(g,hk)-pairing(g,h)-pairing(g,k))<1e-10; cases+=1
    return dict(crystallographic_models=cases,noncommuting_centralizer_pairs=noncommuting)


def intersection_witness():
    rng=random.Random(256); cases=0; worst=0
    for n in range(1,10):
        for _ in range(20):
            sets=[rng.randrange(1<<n) for _ in range(12)]; q=(1<<n)-1; selected=[]
            for p in sets:
                if q&p!=q:
                    prev=q.bit_count(); q&=p; selected.append(p); assert q.bit_count()<prev
            direct=(1<<n)-1
            for p in sets: direct&=p
            assert q==direct and len(selected)<=n; cases+=1; worst=max(worst,len(selected))
    return dict(coordinate_subspace_models=cases,max_selected=worst,scope='Abstract finite-rank descent; no pairwise Artin intersection theorem tested.')


def unitary(rng,n):
    q,r=np.linalg.qr(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))
    return q@np.diag(np.diag(r)/abs(np.diag(r)))


def phase(U):
    angles=(np.angle(np.linalg.eigvals(U))/(2*np.pi))%1
    angles[np.minimum(angles,1-angles)<1e-8]=0
    return float(sum(angles))


def weighted_cycles():
    rng=np.random.default_rng(257); cases=0; error=0.
    for a in (1,2,3,5):
        for b in (1,2,4):
            for identity_control in (False,True):
                qs=[unitary(rng,b) for _ in range(a)]; C=np.eye(b,dtype=complex)
                for Q in qs[:-1]: C=Q@C
                if identity_control: qs[-1]=C.conj().T
                C=qs[-1]@C
                T=np.zeros((a*b,a*b),dtype=complex)
                for j,Q in enumerate(qs): T[((j+1)%a)*b:((j+1)%a+1)*b,j*b:(j+1)*b]=Q
                err=abs(phase(T)/b-((a-1)/2+phase(C)/b)); error=max(error,err); assert err<1e-7
                assert np.linalg.norm(T.conj().T@T-np.eye(a*b))<1e-12; cases+=1
    assert abs(phase(np.eye(3))-0)<1e-12
    assert abs(phase(np.exp(-2j*np.pi*.001)*np.eye(3))-2.997)<1e-12
    return dict(block_cycles=cases,max_phase_error=error,cut_at_one_controls=True)


def fixed_plane():
    rng=np.random.default_rng(258); cases=0; derivative_error=0.
    for k in (1,2,3):
        X=unitary(rng,k); eye=np.eye(k); start=block_diag(X,X.conj().T)
        for u in (0,.3,.7,1):
            c=math.cos(np.pi*u/2); s=math.sin(np.pi*u/2); R=np.block([[c*eye,-s*eye],[s*eye,c*eye]])
            hom=block_diag(X,eye)@R@block_diag(eye,X.conj().T)@R.T
            assert np.linalg.norm(hom.conj().T@hom-np.eye(2*k))<1e-12
            if u==0: assert np.linalg.norm(hom-start)<1e-12
            if u==1: assert np.linalg.norm(hom-np.eye(2*k))<1e-12
        for r in (0,2*k,4*k):
            for eps in (-1,1):
                m=k+r; H=rng.normal(size=(m,m))+1j*rng.normal(size=(m,m)); H=(H-H.conj().T)/2
                A=eps*H[:k,:k]; B=-H[k:,k:]; Z=-H[k:,:k]/2
                tangent=np.block([[eps*A,2*Z.conj().T],[-2*Z,-B]])
                assert np.linalg.norm(tangent-H)<1e-12
                K=np.block([[np.zeros((k,k)), -Z.conj().T],[Z,np.zeros((r,r))]])
                def G(t):
                    Ft=block_diag(expm(eps*t*A),-np.eye(r))
                    W=expm(t*K)@block_diag(np.eye(k),-expm(t*B))@expm(-t*K)
                    return Ft@W.conj().T
                numerical=(G(1e-5)-G(-1e-5))/(2e-5)
                err=np.linalg.norm(numerical-H); derivative_error=max(derivative_error,float(err)); assert err<3e-7
                assert k*k+2*k*r+r*r==m*m; cases+=1
    return dict(tangent_models=cases,max_derivative_error=derivative_error,
                scope='Homotopy and regular-fiber derivative only; mod-two degree is inspected analytically, not numerically certified.')


def reduce_word(word):
    stack=[]
    for x in word:
        if stack and stack[-1]==-x: stack.pop()
        else: stack.append(x)
    return tuple(stack)


def capping():
    rng=random.Random(259); cases=0; max_difference=0
    # Injections: identity, a Nielsen automorphism, and a conjugated basis.
    maps=[{1:(1,),2:(2,)},{1:(1,2),2:(2,)},{1:(3,1,-3),2:(3,2,-3)}]
    def inverse(w): return tuple(-x for x in w[::-1])
    def image(w,mp): return reduce_word(tuple(y for x in w for y in (mp[x] if x>0 else inverse(mp[-x]))))
    def cyclic(w):
        i=0
        while 2*i<len(w) and w[i]==-w[-1-i]: i+=1
        return w[i:len(w)-i] if i else w
    for _ in range(140):
        W=reduce_word([rng.choice((1,-1,2,-2)) for _ in range(rng.randrange(1,100))])
        if not W: continue
        b=next(x for x in (1,-1,2,-2) if x!=-W[-1] and x!=-W[0])
        assert cyclic(W+(b,))==W+(b,)
        for mp in maps:
            old=image(W,mp); z=cyclic(image(W+(b,),mp)); assert z
            assert abs(len(z)-len(old))<=6
            for u in ((1,),(2,),(1,2),(1,2,1), (3,1,-3)):
                linear=sum(old[i:i+len(v)]==v for v in (u,inverse(u)) for i in range(len(old)-len(v)+1))
                count=sum(tuple(z[(i+j)%len(z)] for j in range(len(v)))==v for v in (u,inverse(u)) for i in range(len(z)))
                diff=abs(count-linear); max_difference=max(max_difference,diff); assert diff<=20
            cases+=1
    return dict(capped_injection_instances=cases,max_pattern_difference=max_difference,
                scope='Fixed explicit injections only; uniform constants for arbitrary injections use the source Morse argument.')


def stable_virtual_free():
    cases=0
    # C_d x Z is virtually free. The invariant free subgroup is {0} x dZ.
    for d in range(2,10):
        for u in range(d):
            for v,w in ((1,0),(1,2),(2,3)):
                def phi(x): return ((u*x[0]+v*x[1])%d,w*x[1])
                sample=[(a,z) for a in range(d) for z in range(-12,13)]
                kernels=[]
                for j in range(d+3):
                    current=[]
                    for x in sample:
                        y=x
                        for _ in range(j): y=phi(y)
                        if y==(0,0): current.append(x)
                    kernels.append(set(current))
                assert all(kernels[j]<=kernels[j+1] for j in range(len(kernels)-1))
                assert kernels[-1]==kernels[-2]
                if math.gcd(u,d)==1 and w:
                    quotient=list(product(range(d),repeat=2)); pre={(0,0)}
                    def qphi(x):
                        a,z=phi(x); return a,z%d
                    while True:
                        nxt={x for x in quotient if qphi(x) in pre}
                        if nxt==pre: break
                        assert pre<nxt; pre=nxt
                    assert {x for x in quotient if qphi(x) in pre}==pre
                    assert not any((a,0) in pre for a in range(1,d))
                cases+=1
    return dict(virtually_cyclic_endomorphisms=cases,
                scope='Finite windows and finite quotients; no general Hopficity or ascending-torus finiteness theorem tested.')


def main():
    start=time.perf_counter(); checks={}
    for fn in (mapping_torus,action_monoid,idempotent_differences,cartan,centralizer,intersection_witness,weighted_cycles,fixed_plane,capping,stable_virtual_free):
        checks[fn.__name__]=fn(); print(fn.__name__,'passed',flush=True)
    report=dict(status='passed',elapsed_seconds=round(time.perf_counter()-start,3),checks=checks,
                scope='Selected finite mechanisms; no embedding, Artin, group-equation or one-relator headline theorem is certified.')
    Path(__file__).with_name('results.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='checks'}))


if __name__=='__main__': main()
