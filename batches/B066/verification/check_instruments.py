"""Finite models for selected field, probability and local linear-algebra arguments."""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, permutations, product
from pathlib import Path
import json
import math
import time
import numpy as np
import sympy as s

def ramification():
    def partitions(n,m=1):
        if n==0:yield ()
        for k in range(m,n+1):
            for rest in partitions(n-k,k):yield (k,)+rest
    cases=0
    for n in range(1,16):
        for parts in partitions(n):
            for ell in (2,3,5,7):
                N=sum(e%ell!=0 for e in parts)
                assert len(parts)<=N+F(n,ell)
                assert n-len(parts)>=(1-F(1,ell))*n-N;cases+=1
    assert 5*(1-F(1,2))-2>0 and 4*(1-F(1,2))-2==0
    return dict(fiber_partitions_checked=cases,scope='Partition bounds only; no cover realization claimed.')

def euler():
    from sympy.polys.fields import field
    cases=0
    for p in (2,3,5,7):
        K,x,y=field('x,y',s.GF(p))
        DX=lambda f:x*f.diff(x);DY=lambda f:y*f.diff(y)
        for n in range(1,p):
            r=pow(n,-1,p);U=(1+x**n)**r;V=(1+y**n)**r;Z=(x**n-y**n)**r
            Bx=U/DX(U);By=V/DY(V);Ax=Bx-1;Ay=By-1
            assert DX(Z)+DY(Z)==Z
            assert Bx*DX(Z)+By*DY(Z)==Z
            assert DX(Ax)/Ax==DY(Ay)/Ay==K(p-n)
            qx=DX(Z)/Z;qy=DY(Z)/Z
            assert qx+qy==1 and Ax*qx+Ay*qy==0
            valid=[]
            for e in range(1,p):
                exponents={powers[0]%p for powers,c in (U**e).numer.terms() if c}
                if exponents=={0,e}:valid.append(e)
            assert valid==[n];cases+=1
    return dict(rational_function_cases=cases,scope='Explicit p-independent rational-variable examples; no global reconstruction tested.')

def totients():
    cases=0
    for X,y,k in product((30,50,90),(3,5,7),(2,3)):
        primes=[p for p in s.primerange(2,X+1) if max(s.factorint(p-1),default=1)<=y]
        if len(primes)<k:continue
        image=Counter();products=set()
        for subset in combinations(primes,k):
            m=math.prod(subset);value=math.prod(p-1 for p in subset)
            assert m not in products;products.add(m)
            assert int(s.totient(m))==value;image[value]+=1
        count=math.comb(len(primes),k)
        assert count>=F(len(primes),k)**k
        assert max(image.values())>=math.ceil(F(count,len(image)))
        exponent_bound=math.floor(k*math.log(X,2))
        assert len(image)<=(exponent_bound+1)**len(list(s.primerange(2,y+1)))
        cases+=1
    return dict(subset_families=cases,scope='No asymptotic supply of smooth shifted primes tested.')

def size_bias():
    cases=0
    for raw in ((1,2,3),(1,1,2,4),(1,2,2,3,5)):
        masses=[F(v,sum(raw)) for v in raw];N=len(masses);ranked=sorted(masses,reverse=True)
        for d in range(1,N+1):
            total=F(0)
            for inds in permutations(range(N),d):
                prob=F(1);left=F(1)
                for i in inds:prob*=masses[i]/left;left-=masses[i]
                total+=prob
                selected=sorted([masses[i] for i in inds],reverse=True)+[F(0)]*(N-d)
                assert all(0<=v-w<=left for v,w in zip(ranked,selected));cases+=1
            assert total==1
    for d in range(1,6):
        a=s.symbols('a:'+str(d));t=[a[i]*s.prod(1-a[j] for j in range(i)) for i in range(d)]
        jac=s.Matrix(t).jacobian(a).det()
        assert s.factor(jac-s.prod(1-sum(t[:i]) for i in range(d)))==0
        assert s.prod(s.integrate(1-z,(z,0,1)) for z in a)==s.Rational(1,2)**d
    return dict(exact_sampling_tuples=cases,symbolic_jacobians=5)

def nonresonance():
    x,y=s.symbols('x y');V=s.Matrix([[s.Rational(1,2),1],[0,s.Rational(1,2)]]);R=s.Matrix([[s.Rational(1,4),1],[0,s.Rational(1,4)]])
    def sympower(n):
        basis=[x**i*y**(n-i) for i in range(n+1)]
        return s.Matrix([[s.expand(b.subs({x:x/2+y,y:y/2},simultaneous=True)).coeff(x,i).coeff(y,n-i) for b in basis] for i in range(n+1)])
    cases=0
    for n in range(2,6):
        for L in (s.kronecker_product(V.inv().T,sympower(n)),s.kronecker_product(R.inv().T,s.kronecker_product(R,sympower(n-1)))):
            assert (L-s.eye(L.rows)).det()!=0
            b=s.ones(L.rows,1);z=(L-s.eye(L.rows)).inv()*b
            assert (L-s.eye(L.rows))*z==b;cases+=1
        Q=s.kronecker_product(R.inv().T,sympower(n))
        assert ((Q-s.eye(Q.rows)).det()==0)==(n==2)
    f=x/2+x*x-2*x**3+x**4;h=x
    for n in range(2,9):
        c=s.symbols('c');trial=h+c*x**n
        coeff=s.series(trial.subs(x,f)-trial/2,x,0,n+1).removeO().coeff(x,n)
        h=trial.subs(c,s.solve(coeff,c)[0])
    assert s.series(h.subs(x,f)-h/2,x,0,9).removeO()==0
    return dict(jordan_operators=cases,formal_conjugacy_order=8,quadratic_resonance_retained=True)

def vp(x,p):
    x=F(x)
    if x==0:return math.inf
    a,b=abs(x.numerator),x.denominator;v=0
    while a%p==0:a//=p;v+=1
    while b%p==0:b//=p;v-=1
    return v

def conjugator():
    cases=0
    for n,ell,k in product((2,3,4),(2,3,5),(2,3)):
        q=3 if ell==2 else 2;e=ell**k-1
        N=s.zeros(n)
        for i in range(n-1):N[i+1,i]=1
        A=s.diag(*[q**i for i in range(n)]);P=s.diag(*[s.Rational(-1,e)**i for i in range(n)])
        T=s.eye(n)
        for i in range(n-1):T[i,i+1]=i+1
        N,A,P=[T*M*T.inv() for M in (N,A,P)]
        assert A*N==q*N*A and P*A==A*P and P*N*P.inv()==-N/e
        exp=lambda a:sum((a**j*N**j/s.factorial(j) for j in range(n)),s.zeros(n))
        assert P*exp(-e*s.Rational(2,3))*P.inv()==exp(s.Rational(2,3))
        assert all(vp(F(z),ell)>=k for z in P-s.eye(n));cases+=1
    return dict(exact_matrix_models=cases)

def entropy_components():
    cases=0
    def H(p):return -sum(x*math.log(x) for x in (p,1-p) if x)
    weights=[.1,.2,.3,.4]
    for ps in ((0,.2,.5,.8),(.1,.2,.3,.4),(0,0,.5,.5)):
        ent=[H(p) for p in ps];total=sum(w*h for w,h in zip(weights,ent))
        label_entropy=-sum(w*math.log(w) for w in weights)
        for length in (1,2,4,8):
            probabilities=[w*prob**sum(bits)*(1-prob)**(length-sum(bits)) for w,prob in zip(weights,ps) for bits in product((0,1),repeat=length)]
            block_entropy=-sum(z*math.log(z) for z in probabilities if z)
            assert abs((block_entropy-label_entropy)/length-total)<1e-12
        for mask in range(1,16):
            inds=[i for i in range(4) if mask>>i&1];mass=sum(weights[i] for i in inds)
            restricted=sum(weights[i]*ent[i] for i in inds)/mass
            restricted_weights=[weights[i]/mass if i in inds else 0 for i in range(4)]
            assert abs(sum(restricted_weights)-1)<1e-14
            assert all(a<=b/mass+1e-15 for a,b in zip(restricted_weights,weights))
            assert min(ent[i] for i in inds)-1e-15<=restricted<=max(ent[i] for i in inds)+1e-15;cases+=1
        if 0 in ent:assert total>0 and sum(weights[i]*ent[i] for i in range(4) if ent[i]==0)==0
    for n in range(3,11):assert n-(n-1)==1
    return dict(restricted_mixtures=cases,positive_average_with_zero_components=True,scope='Exact mixture bookkeeping; geometric and entropy-criterion inputs not tested.')

def quadratic_fourier():
    def integral(c,p):
        c=F(c,2);m=max(0,-int(vp(c,p)));mod=p**m
        other=c.denominator//mod
        a=c.numerator*pow(other,-1,mod) if mod>1 else 0
        x=np.arange(mod,dtype=np.int64);res=(a%mod)*(x*x%mod)%mod if mod>1 else np.zeros(1)
        return np.exp(2j*np.pi*res/mod).mean()
    cases=0;max_error=0.;phases={}
    for p,v,u in product((2,3,5),range(-2,3),(1,7)):
        if u%p==0:continue
        P=F(u)*F(p)**v;scale=p**(v/2);N=3
        cN=p**N*integral(P/F(p)**(2*N),p)
        cprev=p**(N-1)*integral(P/F(p)**(2*(N-1)),p)
        omega=cN/scale
        error=max(abs(cN-cprev),abs(abs(omega)-1),abs(integral(P,p)-omega*scale*integral(-1/P,p)))
        assert error<2e-9;max_error=max(max_error,error);cases+=1
        T=2 if p!=2 else 3
        transformed=p**N*integral(P*T*T/F(p)**(2*N),p)/(scale*p**vp(T,p))
        assert abs(transformed-omega)<2e-9
        phases[p,v,u]=(omega,scale,integral(P,p),integral(-1/P,p))
    for p in (2,3,5):
        left=phases[p,-1,1];right=phases[p,1,1]
        assert abs(left[2]*right[2]-left[0]*right[0]*left[1]*right[1]*left[3]*right[3])<2e-9
    return dict(scalar_models=cases,diagonal_models=3,max_error=max_error,scope='Finite residue models including p=2; no global packet theorem tested.')

def main():
    start=time.perf_counter();checks={}
    for fn in (ramification,euler,totients,size_bias,nonresonance,conjugator,entropy_components,quadratic_fourier):
        checks[fn.__name__]=fn();print(fn.__name__,'passed',flush=True)
    report=dict(status='passed',elapsed_seconds=round(time.perf_counter()-start,3),checks=checks,scope='Selected finite reductions only; no field reconstruction, prime statistics, Langlands or packet equidistribution headline certified.')
    Path(__file__).with_name('results.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='checks'}))

if __name__=='__main__':main()
