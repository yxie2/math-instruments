"""Exact and finite models for the selected arithmetic and covering reductions."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import math
import time
import sympy as s

def squareclass():
    def sf(n):
        return (1 if n>0 else -1)*math.prod(p for p,e in s.factorint(abs(n)).items() if e%2)
    N=3000; kernels={n:sf(n) for n in range(-N,N+1) if n}; cases=0
    for pred in (lambda d:d>0,lambda d:abs(d)%2==0,lambda d:d%5 in (1,2),lambda d:(abs(d)*17+3)%11<4):
        A=[0];S=[0]
        for x in range(1,N+1):
            A.append(A[-1]+sum(pred(kernels[n]) for n in (-x,x)))
            S.append(S[-1]+sum(pred(n) for n in (-x,x) if abs(kernels[n])==x))
        for X in (1,7,31,100,999,N):
            assert A[X]==sum(S[X//(m*m)] for m in range(1,math.isqrt(X)+1))
            assert S[X]==sum(int(s.mobius(m))*A[X//(m*m)] for m in range(1,math.isqrt(X)+1));cases+=1
    assert sum(n%4==0 for n in range(1,101))!=sum(sum(d%4==0 for d in range(1,100//(m*m)+1) if abs(kernels[d])==d) for m in range(1,11))
    return dict(convolution_cases=cases,noninvariant_negative_control=True)

def rank_tail():
    cases=0
    for size in (30,100,300):
        a=[size//j for j in range(1,size+1)]+[0]*size;B=max(a)
        T=lambda k:sum(v>k for v in a)
        for R,K in ((1,3),(2,7),(5,12)):
            exact=sum(v for v in a if v>R)
            assert exact==R*T(R)+sum(T(k) for k in range(R,B))
            assert exact<=R*T(R)+sum(T(k) for k in range(R,K))+B*T(K)
            C=max(F(T(k)*k*k,size) for k in range(R,K+1))
            bound=C*size*(F(1,R)+sum(F(1,k*k) for k in range(R,K))+F(B,K*K))
            assert exact<=bound;cases+=1
    for n in (10,100,1000):
        a=[0]*n+[1]*(n-1)+[n]
        assert F(sum(a),len(a))==1-F(1,2*n)
        assert F(sum(v>=2 for v in a),len(a))==F(1,2*n)
    return dict(layer_cake_cases=cases,rare_outlier_mean_limit=1,rare_outlier_distribution_mean=0.5,scope='No analytic rank-count estimate tested.')

def sign_extension():
    cases=0
    for a in range(-3,5):
        def mul(x,y):
            n,e,c=x;m,f,d=y
            if c:m,f=-m-a*f,f
            return (n+m+a*((e+f)//2),(e+f)%2,(c+d)%2)
        def inv(x):
            n,e,c=x
            y=(-n-a*e,e,0)
            return mul((0,0,c),y)
        z=(0,0,1); ident=(0,0,0); G=list(product(range(2),repeat=2))
        lift=lambda g:(0,g[0],g[1])
        add=lambda g,h:((g[0]+h[0])%2,(g[1]+h[1])%2)
        action=lambda g:1-2*g[1]
        f=lambda g,h:mul(mul(lift(g),lift(h)),inv(lift(add(g,h))))[0]
        d=lambda g:mul(mul(mul(z,lift(g)),z),inv(lift(g)))[0]
        assert mul(z,z)==ident
        for g,h,k in product(G,repeat=3):
            assert mul(mul(lift(g),lift(h)),lift(k))==mul(lift(g),mul(lift(h),lift(k)))
            assert f(g,h)+f(add(g,h),k)==action(g)*f(h,k)+f(g,add(h,k))
            assert d(add(g,h))==d(g)+action(g)*d(h)+2*f(g,h);cases+=1
        assert d((1,0))==-a
        split=(a%2==0)
        assert any(mul((n,1,0),(n,1,0))==ident for n in range(-5,6))==split
        for shift in range(-2,3):
            shifted=(shift,1,0)
            ds=mul(mul(mul(z,shifted),z),inv(shifted))[0]
            assert ds==d((1,0))-2*shift
        if split:
            t=(-a//2,1,0)
            assert mul(t,t)==ident and mul(t,z)==mul(z,t)
    return dict(cocycle_triples=cases,split_iff_even_parameter=True)

def denominators():
    cases=0
    for p,j,q in product((2,3,5,7),range(1,6),range(2,16)):
        if math.gcd(p,q)>1:continue
        x=[F(v,p**j) for v in (2,-3,7)]
        a=[v+F(w,q) for v,w in zip(x,(5,-4,9))]
        m=q*pow(q,-1,p**j)
        b=[m*(v-w) for v,w in zip(a,x)];c=[(m-1)*v for v in x]
        assert m%p**j==1 and all(v.denominator==1 for v in b+c)
        assert [m*v-u-w for v,u,w in zip(a,b,c)]==x;cases+=1
    return dict(exact_vector_certificates=cases)

def graph_cover():
    def components(n,edges):
        adj=[[] for _ in range(n)]
        for u,v in edges:adj[u].append(v);adj[v].append(u)
        unseen=set(range(n));count=0
        while unseen:
            stack=[unseen.pop()];count+=1
            while stack:
                for v in adj[stack.pop()]:
                    if v in unseen:unseen.remove(v);stack.append(v)
        return count
    cases=0
    for n,p in product(range(3,9),(2,3,5,7)):
        base=[(j,(j+1)%n) for j in range(n)]+[(0,n),(n,n+1)];N=n+2
        for chosen,expected in ((0,1),(n,p)):
            edges=[(N*a+u,N*((a+(i==chosen))%p)+v) for i,(u,v) in enumerate(base) for a in range(p)]
            assert components(N*p,edges)==expected
            deg=[0]*(N*p);bd=[0]*N
            for u,v in edges:deg[u]+=1;deg[v]+=1
            for u,v in base:bd[u]+=1;bd[v]+=1
            assert deg==bd*p
            if chosen==0:
                cut=[(N*a+u,N*a+v) for i,(u,v) in enumerate(base) if i!=chosen for a in range(p)]
                assert components(N*p,cut)==p
                assert len({j%p for j in range(p)})==p
            cases+=1
    return dict(voltage_covers=cases,bridge_negative_control=True)

def vp(x,p):
    x=F(x)
    if not x:return math.inf
    n,d=abs(x.numerator),x.denominator;v=0
    while n%p==0:n//=p;v+=1
    while d%p==0:d//=p;v-=1
    return v

def annular_roots():
    cases=0
    for p,ell in product((2,3,5,7),(2,3,5,7)):
        if p==ell:continue
        c=F(1);partial=F(1)
        for n in range(1,21):
            c*=F(1,ell)-(n-1);c/=n
            assert vp(c,p)>=0
            assert vp(c*p**n,p)>=n
            partial+=c*p**n
            assert vp(partial**ell-(1+p),p)>=n+1;cases+=1
    c=F(1);wild=[]
    for n in range(1,15):
        c*=F(1,3)-(n-1);c/=n
        wild.append(vp(c*3**n,3));assert wild[-1]==-vp(math.factorial(n),3)
    assert wild[-1]<0
    for d,t in product(range(-4,5),(F(-2,5),F(-1,5),F(0),F(2,5))):
        assert 1+(d+1)*t>d*t and 1+(d-1)*t>d*t
    return dict(tame_coefficient_checks=cases,wild_term_valuations=wild,scope='Finite exact series and Laurent-valuation models; no global analytic theorem certified.')

def kummer():
    cases=0
    for p,q,a in product(list(s.primerange(2,120)),(2,3,5,7),range(-6,7)):
        if not a or a%p==0 or p==q:continue
        condition=(p-1)%q==0 and pow(a,(p-1)//q,p)==1
        roots=sum(pow(t,q,p)==a%p for t in range(p))
        order=int(s.n_order(a%p,p))
        assert condition==(roots==q)==(((p-1)//order)%q==0);cases+=1
    return dict(finite_field_cases=cases)

def reservoir():
    cases=0
    for bases in ((2,3,5),(3,7,11),(2,5,13)):
        odd=[q for q in bases if q!=2];mod=math.prod(odd)
        residues=[next(a for a in range(2,q) if int(s.legendre_symbol(a,q))==-1) for q in odd]
        from sympy.ntheory.modular import crt
        a=int(crt(odd,residues)[0]);assert math.gcd(a*(a-1),mod)==1
        for p in s.primerange(13,30000):
            if p%mod!=a or p%8!=5:continue
            for q in bases:
                assert int(s.legendre_symbol(q,p))==-1
                assert ((p-1)//int(s.n_order(q,p)))%2==1;cases+=1
    for q,J,x in product((2,3,5),(4,7,10),(10,30,100)):
        P=math.prod(q**j-1 for j in range(1,J+1))
        factors=[p for p in s.factorint(P) if p>x]
        assert x**len(factors)<=P
        assert math.log(P)<=math.log(q)*J*(J+1)/2
    ratios=[]
    for L in (1e20,1e30,1e40):
        logs=(math.log(L)-L**.1,2*math.log(L)+L**.3-1e-6*L)
        assert max(logs)<0;ratios.append(logs)
    assert all(ratios[j+1][i]<ratios[j][i] for j in range(2) for i in range(2))
    return dict(quadratic_character_checks=cases,asymptotic_log_ratios=ratios,scope='Conditional reduction only; no reservoir or exceptional-prime counting theorem tested.')

def main():
    start=time.perf_counter();checks={}
    for fn in (squareclass,rank_tail,sign_extension,denominators,graph_cover,annular_roots,kummer,reservoir):
        checks[fn.__name__]=fn();print(fn.__name__,'passed',flush=True)
    report=dict(status='passed',elapsed_seconds=round(time.perf_counter()-start,3),checks=checks,scope='Selected reductions only; no Goldfeld, Margulis-Platonov, section-conjecture or unconditional primitive-root headline certified.')
    Path(__file__).with_name('results.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='checks'}))

if __name__=='__main__':main()
