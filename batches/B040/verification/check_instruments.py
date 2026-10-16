"""Finite tests of selected interfaces, not complexity lower-bound proofs."""
import itertools as it
import json
import random
from fractions import Fraction as Q
from functools import lru_cache
from math import factorial
from pathlib import Path
import numpy as np
import sympy as s
rng=random.Random(40016); out={}

count=0
for n in range(1,6):
    beta=Q(1,10);L=Q(3,2);bound=beta*L/(1-beta)
    joint={}
    for marks in it.product(range(2),repeat=n):
        for data in it.product(range(2),repeat=n):
            mass=Q(1)
            for b,x in zip(marks,data):
                mass*=beta if b else 1-beta
                mass*=([Q(1,4),Q(3,4)][x] if b else Q(1,2))
            joint[marks,data]=mass
    for data in it.product(range(2),repeat=n):
        den=sum(v for (m,x),v in joint.items() if x==data)
        posts=[sum(v for (m,x),v in joint.items() if x==data and m[i])/den for i in range(n)]
        assert max(posts)<=bound
        selected=sorted(range(n),key=lambda i:(-posts[i],i))[:2]
        bad=sum(v for (m,x),v in joint.items() if x==data and any(m[i] for i in selected))/den
        assert bad<=len(selected)*bound;count+=1
assert Q(1)>bound  # Revealing the marked event destroys the bound.
out['posterior']={'data_tuples':count,'success_conditioning_negative_control':True}

V=list(it.product(range(2),repeat=2));tests=0
for a,b in it.product(range(4),repeat=2):
    pa=[Q(1,8)+(Q(1,2) if j==a else 0) for j in range(4)]
    pb=[Q(1,8)+(Q(1,2) if j==b else 0) for j in range(4)]
    for bits in it.product(range(2),repeat=4):
        if not any(bits):continue
        M=np.array(bits).reshape(2,2)
        bias=sum(pa[i]*pb[j]*(-1)**int(np.array(x)@M@np.array(y)%2) for i,x in enumerate(V) for j,y in enumerate(V))
        assert abs(bias)<=Q(7,8)
        for R in [1,3,6]:assert abs(bias**R)<=Q(7,8)**R
        tests+=1
out['bilinear_bias']={'exact_bilinear_models':tests,'independent_product_counts':[1,3,6]}

tests=0
for n in range(2,7):
    for _ in range(15):
        f=np.array([rng.uniform(-1,1) for _ in range(2**n)]).reshape((2,)*n);f-=f.mean()
        S=sorted(rng.sample(range(n),rng.randint(1,n)))
        G=f.mean(axis=tuple(i for i in range(n) if i not in S),keepdims=True)
        infl=[np.mean((f-f.mean(axis=i,keepdims=True))**2) for i in range(n)]
        assert np.mean(G**2)<=sum(infl[i] for i in S)+1e-12
        err=np.mean((f-G)**2)
        for i in set(range(n))-set(S):assert infl[i]<=err+1e-12
        tests+=1
out['junta_influence']={'finite_product_projection_models':tests,'austin_theorem_proved_by_test':False}

tests=0
for _ in range(100):
    maps={(u,v):[rng.randrange(3) for a in range(3)] for u,v in it.product(range(2),repeat=2)}
    sigma=max(sum(maps[u,v][a[u]]==b[v] for u,v in maps) for a in it.product(range(3),repeat=2) for b in it.product(range(3),repeat=2))
    for d in [1,2]:
        left=[rng.sample(range(3),d) for _ in range(2)];right=[rng.sample(range(3),d) for _ in range(2)]
        events=sum(any(maps[u,v][a]==b for a in left[u] for b in right[v]) for u,v in maps)
        assert events<=d*d*sigma;tests+=1
out['local_lists']={'exact_projection_game_models':tests}

def per(A):
    A=[list(row) for row in A];n=len(A)
    if not n:return 1
    # Independent weighted matching enumeration, with memoized occupied columns.
    rows=sorted(range(n),key=lambda i:sum(x!=0 for x in A[i]))
    @lru_cache(None)
    def rec(k,mask):
        if k==n:return 1
        return sum(A[rows[k]][j]*rec(k+1,mask|1<<j) for j in range(n) if A[rows[k]][j] and not(mask>>j&1))
    return rec(0,0)
H=[[-1,-1,1],[-1,-1,1],[1,1,1]];tests=0
for w in [-3,0,2,7]:
    for I,O in it.product(range(4),repeat=2):
        rows=[i for i in range(3) if not(O>>i&1)];cols=[j for j in range(3) if not(I>>j&1)]
        val=0 if len(rows)!=len(cols) else (-2*w if I&1 else 1)*per([[H[i][j] for j in cols] for i in rows])
        assert val==(-2 if I==O==0 else -2*w if I==O==3 else 0);tests+=1
out['signed_equality']={'exact_boundary_states':tests}

def selector(X,theta,q):
    k=len(X);h=k-q;n=11*k-2*q;A=[[0]*n for _ in range(n)]
    for i in range(k):
        for j in range(k):A[i][j]=X[i][j]
    offsets=[k,k+(k+h)];off=k+2*(k+h)
    for c,g in enumerate(offsets):
        for i in range(k):
            for j in range(h):A[g+i][g+k+j]=A[g+k+j][g+i]=1
            w=1 if c==0 else theta[i]
            for a in range(3):
                for b in range(3):A[off+a][off+b]=H[a][b]
            A[i][off]=-2*w;A[g+i][off+1]=1
            A[off][i]=A[off+1][g+i]=1;off+=3
    return A
tests=0
for k in [1,2]:
    for q in range(k//2+1):
        for _ in range(4):
            X=[[rng.randrange(-2,3) for _ in range(k)] for _ in range(k)];theta=[rng.randrange(-2,3) for _ in range(k)]
            total=0
            for S in it.combinations(range(k),q):
                for T in it.combinations(set(range(k))-set(S),q):
                    C=sorted(set(range(k))-set(S)-set(T));total+=np.prod([theta[i] for i in T],dtype=object)*per([[X[i][j] for j in C] for i in C])
            A=selector(X,theta,q);assert per(A)==(-2)**(2*k)*factorial(k-q)**4*total;tests+=1
out['coefficient_selector']={'full_matching_models':tests,'maximum_matrix_order':22,'characteristic_two_scalar_vanishes':True}

x=s.symbols('x');tests=0;splits=0
for p in [5,7,11,13]:
    roots=list(range(min(p,5)));F=s.Poly(s.prod(x-a for a in roots),x,modulus=p)
    for _ in range(25):
        a=s.Poly(sum(rng.randrange(p)*x**j for j in range(len(roots))),x,modulus=p)
        g=s.gcd(F,a).monic();zeros=[r for r in roots if int(a.eval(r))%p==0]
        expected=s.Poly(s.prod(x-r for r in zeros),x,modulus=p)
        assert g==expected
        if not zeros:
            inv=s.invert(a,F);assert (a*inv).rem(F)==s.Poly(1,x,modulus=p)
        if 0<len(zeros)<len(roots):splits+=1
        tests+=1
out['dynamic_evaluation']={'exact_gcd_models':tests,'proper_splits':splits}

p=7;q=3;Y=np.array([[0,0,2],[1,0,0],[0,1,0]],dtype=np.int64);R=np.diag([1,2,4]);I=np.eye(3,dtype=np.int64)
def mul(a):return (int(a[0])*I+int(a[1])*Y+int(a[2])*(Y@Y))%p
def solve(A,b):
    M=np.column_stack([A,b]).astype(np.int64)%p
    for j in range(q):
        z=next(i for i in range(j,q) if M[i,j]);M[[j,z]]=M[[z,j]];M[j]=M[j]*pow(int(M[j,j]),-1,p)%p
        for i in range(q):
            if i!=j:M[i]=(M[i]-M[i,j]*M[j])%p
    return M[:,-1]
tests=0
for _ in range(60):
    h0=np.array([rng.randrange(p) for _ in range(q)])
    if not any(h0):h0[0]=1
    Vmat=mul(h0)@R%p;G=np.linalg.matrix_power(Vmat,3)%p;assert np.array_equal(G,int(G[0,0])*I%p)
    w=np.array([rng.randrange(p) for _ in range(q)])
    if not any(w):w[0]=1
    j=next(i for i in range(q) if w[i]);lam=np.zeros(q,dtype=np.int64);lam[j]=pow(int(w[j]),-1,p)
    E=np.outer(w,lam)%p;assert np.array_equal(E@E%p,E)
    basis=np.column_stack([w,Y@w%p,Y@Y@w%p]);h=solve(basis,Vmat@w%p)
    assert np.array_equal(mul(h)@E%p,Vmat@E%p)
    norm=mul(h)@mul(R@h%p)@mul(R@R@h%p)%p;assert np.array_equal(norm,G);tests+=1
out['idempotent_norm']={'exact_cyclic_field_models':tests,'field':'F_7[y]/(y^3-2)','idempotent_construction_audited':False}
result={'batch':'B040','status':'pass','scope':'Finite selected interfaces only; no complexity headline or Lean build certified.','checks':out}
Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
