"""Finite checks of local interfaces, with explicit hypothesis controls."""
import json
import math
import re
import time
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from collections import defaultdict
import numpy as np


def coefficient_descent():
    rng=np.random.default_rng(7401);E=3;N=2;cases=0
    def scalar_mul(a,b,p):return np.convolve(a,b)[:E]%p
    def ring_matrix_mul(A,B,p):
        out=np.zeros_like(A)
        for i,j,k in product(range(N),repeat=3):out[i,j]=(out[i,j]+scalar_mul(A[i,k],B[k,j],p))%p
        return out
    def embed(A,p):
        out=np.zeros((N*E,N*E),dtype=np.int64)
        for i,j in product(range(N),repeat=2):
            for col in range(E):
                for r in range(E-col):out[i*E+col+r,j*E+col]=A[i,j,r]%p
        return out
    terms=[(3,()),(2,(0,)),(1,(0,1)),(-1,(1,0)),(2,(1,1))]
    identity=np.zeros((N,N,E),dtype=np.int64);identity[:,:,0]=np.eye(N,dtype=np.int64)
    for p in [2,3,5,7]:
        denominator=np.array([1,1,0]);inverse=np.array([1,-1,1])%p
        assert np.array_equal(scalar_mul(denominator,inverse,p),[1,0,0])
        for _ in range(20):
            P=[rng.integers(0,p,size=(N,N,E)) for j in range(2)]
            for A in P:A[:,:,2]=0
            V=[np.array([[scalar_mul(A[i,j],inverse,p) for j in range(N)] for i in range(N)]) for A in P]
            T=[embed(A,p) for A in V];fT=np.zeros_like(T[0]);numerator=np.zeros_like(identity)
            for coeff,word in terms:
                mat=np.eye(N*E,dtype=np.int64);num=identity.copy()
                for letter in word:mat=mat@T[letter]%p;num=ring_matrix_mul(num,P[letter],p)
                for _ in range(2-len(word)):
                    num=np.array([[scalar_mul(num[i,j],denominator,p) for j in range(N)] for i in range(N)])
                fT=(fT+coeff*mat)%p;numerator=(numerator+coeff*num)%p
            D=scalar_mul(denominator,denominator,p);Dmatrix=np.array([[D if i==j else np.zeros(E,dtype=np.int64) for j in range(N)] for i in range(N)])
            assert np.array_equal(embed(Dmatrix,p)@fT%p,embed(numerator,p))
            assert bool(np.any(fT))==bool(np.any(numerator))
            assert np.array_equal(embed(ring_matrix_mul(V[0],V[1],p),p),T[0]@T[1]%p);cases+=1
    # t^E is nonzero before truncation and zero after it; the strict degree bound is essential.
    monomial=[0]*E+[1];assert not any(monomial[:E]) and any(monomial)
    # t has zero constant term and cannot have a multiplicative inverse modulo t^E.
    assert all(np.convolve([0,1,0],a)[0]%2!=1 for a in product(range(2),repeat=E))
    return dict(exact_matrix_models=cases,prime_fields=[2,3,5,7],strict_degree_negative_control=True,nonregular_denominator_control=True)


def integration_jets():
    cases=0;commutators=0
    for d in [5,8]:
        matrices={i:np.array([[F((-1)**(r-q-1),r*i**(r-q)) if q<r else F(0) for q in range(d)] for r in range(d)],dtype=object) for i in [1,2,3]}
        e=np.array([F(1)]+[F(0)]*(d-1),dtype=object)
        # Formal division by z+i by coefficient recurrence, followed by integration.
        def integrate(a,i):
            quotient=[]
            for r in range(len(a)-1):quotient.append((a[r]-(quotient[-1] if quotient else 0))/i)
            return np.array([F(0)]+[b/(r+1) for r,b in enumerate(quotient)],dtype=object)
        for length in range(4):
            for word in product([1,2,3],repeat=length):
                vector=e.copy();mat=np.eye(d,dtype=object)
                for letter in word:mat=mat@matrices[letter]
                for letter in reversed(word):vector=integrate(vector,letter)
                assert all(mat@e==vector);cases+=1
        comm=matrices[1]@matrices[2]-matrices[2]@matrices[1]
        direct=integrate(integrate(e,2),1)-integrate(integrate(e,1),2)
        assert all(comm@e==direct) and any(direct);commutators+=1
        a=np.array([F((-1)**r,r+1) for r in range(d+4)],dtype=object)
        assert all(integrate(a,2)[:d]==matrices[2]@a[:d])
    return dict(exact_word_jets=cases,noncommuting_first_columns=commutators,truncation_checks=2)


def damped_products():
    rng=np.random.default_rng(7403);c=(1-math.exp(-2))/9;cases=0;minratio=1e100
    def cayley(T,psi):
        return -math.expm1(-2*T)/(math.expm1(-T)**2+4*math.exp(-T)*math.sin(psi/2)**2)
    for N in [1,2,4,10,30]:
        for gamma in [1.,.1,.001]:
            for trial in range(40):
                size=int(rng.integers(1,N+1));angles=rng.normal(size=size)*10**rng.uniform(-7,1)
                a=gamma*np.minimum(abs(angles),N*angles**2)+10**rng.uniform(-12,-2,size=size)
                T=float(sum(a));psi=float(sum(angles));value=cayley(T,psi)
                assert T+1e-12>=gamma*min(1,psi*psi)/2
                assert value>=c*gamma*(1-1e-12);minratio=min(minratio,value/gamma);cases+=1
    m=1000;bad=cayley(1/m,1)
    assert bad<c
    return dict(products=cases,explicit_constant=c,minimum_observed_ratio=minratio,missing_factor_count_negative_control=bad)


def hypergeometric_smoothing():
    def choose(n,k):return math.comb(n,k) if 0<=k<=n else 0
    cases=0
    for g in [10,20,40]:
        for M in [1,2,g//4,g//2,g-1]:
            for m in range(g):
                p=[F(choose(g-M,v)*choose(M,m-v),choose(g,m)) for v in range(g-M+1)]
                q=[F(choose(g-M,v)*choose(M,m+1-v),choose(g,m+1)) for v in range(g-M+1)]
                flux=[F(g-M-v,g-m)*p[v] for v in range(len(p))]
                assert sum(p)==sum(q)==1
                for v in range(len(p)):assert q[v]-p[v]==(flux[v-1] if v else 0)-flux[v]
                tv=sum(abs(x-y) for x,y in zip(p,q))/2
                assert tv==max(flux)<=max(p);cases+=1
    # Common sublaw flag: the report on a hidden label has the same law in both hypotheses.
    P=[F(1,2),F(1,3),F(1,6)];Q=[F(1,4),F(1,4),F(1,2)];common=[min(a,b) for a,b in zip(P,Q)];omega=sum(common)
    U=[a/omega for a in common]
    for law in [P,Q]:
        residual=[(a-b)/(1-omega) for a,b in zip(law,common)]
        assert all(omega*u+(1-omega)*r==a for u,r,a in zip(U,residual,law))
    assert all(F(1,2)*omega*u/(omega*u)==F(1,2) for u in U)
    return dict(adjacent_hypergeometric_pairs=cases,common_component_mass=str(omega),hidden_label_posterior='1/2')


def binary_rank(rows,n):
    pivots={}
    for row in rows:
        while row:
            b=row.bit_length()-1
            if b in pivots:row^=pivots[b]
            else:pivots[b]=row;break
    return len(pivots)


def parity_lifts():
    types=[0,0,1,2];base_edges={(i,j) for i in range(4) for j in range(i+1,4) if types[i]!=types[j]}
    neighbors={a:[b for b in range(3) if b!=a] for a in range(3)}
    def edge(u,v):return tuple(sorted((u,v))) in base_edges
    def lifted(b):
        vs=[]
        for u in range(4):
            for bit in range(2):vs.append((u,dict(zip(neighbors[types[u]],[bit,bit^b[types[u]]]))))
        return vs
    lifts=[lifted([0,0,0]),lifted([1,0,0])]
    graphs=[(1,[]),(2,[]),(2,[(0,1)]),(3,[(0,1),(1,2)]),(3,[(0,1),(1,2),(0,2)]),(4,[(0,1),(1,2),(2,3),(0,3)]),(4,[(0,1),(0,2),(0,3)]),(4,[(0,1),(1,2),(0,2)]),(4,[])]
    projections=0;dual_witnesses=0;repeated=0
    for n,edges in graphs:
        totals=[0,0]
        for phi in product(range(4),repeat=n):
            if not all(edge(phi[x],phi[y]) for x,y in edges):continue
            a=[types[u] for u in phi];indices={(x,b):2*x+j for x in range(n) for j,b in enumerate(neighbors[a[x]])}
            rows=[(1<<(2*x))|(1<<(2*x+1)) for x in range(n)]
            rows +=[(1<<indices[x,a[y]])|(1<<indices[y,a[x]]) for x,y in edges]
            rhs=[int(t==0) for t in a]+[0]*len(edges)
            rank=binary_rank(rows,2*n);aug=binary_rank([r|(b<<(2*n)) for r,b in zip(rows,rhs)],2*n+1)
            homogeneous=2**(2*n-rank);inhomogeneous=0 if aug>rank else homogeneous
            totals[0]+=homogeneous;totals[1]+=inhomogeneous;found=False
            for dual in range(1<<len(rows)):
                lhs=0;right=0
                for j,row in enumerate(rows):
                    if (dual>>j)&1:lhs^=row;right^=rhs[j]
                if lhs==0 and right:
                    found=True;dual_witnesses+=1
                    assert all(sum((dual>>x)&1 for x in range(n) if a[x]==t)%2==1 for t in range(3))
            assert found==(inhomogeneous==0)
            projections+=1;repeated+=len(set(phi))<n
        direct=[]
        for vertices in lifts:
            count=0
            for assignment in product(range(len(vertices)),repeat=n):
                ok=True
                for x,y in edges:
                    u,z=vertices[assignment[x]];v,w=vertices[assignment[y]]
                    if not edge(u,v) or z[types[v]]!=w[types[u]]:ok=False;break
                count+=ok
            direct.append(count)
        assert direct==totals and totals[0]>=totals[1]
    return dict(source_graphs=len(graphs),projected_systems=projections,dual_witnesses=dual_witnesses,repeated_projection_cases=repeated)


def cycle_potentials():
    valid=0
    for bits in product(range(2),repeat=12):
        g=[np.array(bits[4*i:4*i+4]).reshape(2,2) for i in range(3)]
        if any(sum(g[i][a[i],a[(i+1)%3]] for i in range(3))%2 for a in product(range(2),repeat=3)):continue
        c=[int(x[0,0]) for x in g];alpha=[[int(x[u,0])^int(x[0,0]) for u in range(2)] for x in g]
        C=[0,c[0],c[0]^c[1]];Y=[[v^C[i] for v in alpha[i]] for i in range(3)]
        assert C[2]^C[0]==c[2]
        assert all(g[i][u,v]==Y[i][u]^Y[(i+1)%3][v] for i,u,v in product(range(3),range(2),range(2)));valid+=1
    rng=np.random.default_rng(7406);models=0
    for dims in [(1,2,3),(2,1,2,3),(1,1,1,1)]:
        for _ in range(20):
            Y=[rng.integers(0,2,size=d) for d in dims]
            for a in product(*(range(d) for d in dims)):assert sum(int(Y[i][a[i]])^int(Y[(i+1)%len(dims)][a[(i+1)%len(dims)]]) for i in range(len(dims)))%2==0
            models+=1
    g=np.array([[0,0],[0,1]])
    assert all((g[u,v]^g[v,u])==0 for u,v in product(range(2),repeat=2)) and (g[0,0]^g[0,1]^g[1,0]^g[1,1])==1
    return dict(exhaustive_three_cycle_tables=4096,zero_sum_tables=valid,singleton_models=models,two_cycle_counterexample=True)


def split_and_affine():
    W='(?:111)*';P=['0','01'];Q=['0','10'];expressions={}
    for x,y in product(range(2),repeat=2):
        middle='(?:'+Q[0]+W+P[0]+'|'+Q[1]+W+P[1]+')*'
        body=W+P[x]+middle+Q[y]+W
        if x==y:body='(?:'+W+'|'+body+')'
        expressions[x,y]=re.compile('^(?:'+body+')$')
    checks=0
    for length in range(13):
        for letters in product('01',repeat=length):
            word=''.join(letters);parts=[word[i:i+3] for i in range(0,length,3)]
            domain=length%3==0 and all(e in ['010','111'] for e in parts)
            flips=sum(e=='010' for e in parts)%2
            for x,y in product(range(2),repeat=2):
                actual=domain and (x^flips)==y;expression=domain and bool(expressions[x,y].fullmatch(word))
                assert actual==expression;checks+=1
    assert expressions[0,0].fullmatch('00')
    rng=np.random.default_rng(7407);singular=0
    for _ in range(100):
        maps=[(rng.integers(0,2,(2,2)),rng.integers(0,2,2)) for j in range(5)]
        linear=np.eye(2,dtype=np.int64)
        for A,b in maps:linear=linear@A%2;singular+=round(np.linalg.det(A))%2==0
        def run(v):
            for A,b in maps:v=(v@A+b)%2
            return v
        zero=run(np.zeros(2,dtype=np.int64))
        for v in product(range(2),repeat=2):
            v=np.array(v);assert np.array_equal((run(v)-zero)%2,v@linear%2)
    return dict(expression_word_state_cases=checks,missing_domain_negative_control=True,affine_composites=100,singular_component_maps=singular)


def affine_line_correction():
    exact=0
    for l in range(1,7):
        for v in [0,1]:
            failures=0
            for values in product(range(2),repeat=l+1):
                # Center is the all-one tuple in the multiplicative monoid {0,1}.
                center=values[0]^v
                failures+=all(values[j+1]!=center for j in range(l))
            assert F(failures,2**(l+1))==F(1,2**l);exact+=1
    l=1
    while F(1,2**l)>F(1,4*2*(1+2*l+4*l*l)):l+=1
    D=2*(1+2*l+4*l*l);u=F(1,2*D)
    assert F(1,2**l)<=F(1,4*D) and (1-u)**D>=F(1,2)
    rng=np.random.default_rng(7408);indices=np.arange(2**l)
    for attempt in range(1,1001):
        beta=rng.integers(0,2,size=2**l,dtype=np.int8);ok=True
        for v in [0,1]:
            values=beta.copy();values[-1]^=v;success=np.zeros(2**l,dtype=bool)
            for j in range(l):success|=values==values[indices^(1<<j)]
            if not all(success):ok=False;break
        if ok:break
    else:raise AssertionError('finite random search did not find a correction')
    assert 1+l+math.comb(l,2)<=1+2*l+4*l*l
    return dict(exact_local_probability_models=exact,chosen_length=l,dependency_bound=D,search_attempts=attempt,all_tuple_state_checks=2**(l+1),monoid='multiplicative {0,1}',same_correction_for_all_states=True)


if __name__=='__main__':
    start=time.perf_counter();checks={}
    for f in [coefficient_descent,integration_jets,damped_products,hypergeometric_smoothing,parity_lifts,cycle_potentials,split_and_affine,affine_line_correction]:checks[f.__name__]=dict(status='pass',details=f())
    result=dict(batch='B074',status='pass',elapsed_seconds=round(time.perf_counter()-start,3),scope='Selected finite interfaces and hypothesis controls; no source headline or Lean certification.',checks=checks)
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
