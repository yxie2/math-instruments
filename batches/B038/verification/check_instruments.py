"""Selected finite algebraic interfaces; no geometric headline certification."""
import itertools as it
import json
import math
import random
from fractions import Fraction as F
from pathlib import Path
import numpy as np
import sympy as s
from scipy.optimize import minimize
rng=random.Random(38016);nr=np.random.default_rng(38016);checks={}

# Independent finite contact-constrained log-determinant optimization.
worst=0
for n in [2,3]:
    for _ in range(8):
        vectors=[]
        for j in range(3):
            U=np.linalg.qr(nr.normal(size=(n,n))+1j*nr.normal(size=(n,n)))[0]
            vectors.extend(U.T)
        contacts=sum(np.outer(v,v.conj())/3 for v in vectors)
        assert np.linalg.norm(contacts-np.eye(n))<1e-12
        basis=[np.diag(np.eye(n)[j]) for j in range(n)]
        for a,b in it.combinations(range(n),2):
            M=np.zeros((n,n),complex);M[a,b]=M[b,a]=1;basis.append(M)
            M=np.zeros((n,n),complex);M[a,b]=1j;M[b,a]=-1j;basis.append(M)
        C=np.array([[np.vdot(v,M@v).real for M in basis] for v in vectors])
        def matrix(z):return sum((a*M for a,M in zip(z,basis)),np.zeros((n,n),complex))
        def fun(z):
            e=np.linalg.eigvalsh(matrix(z));return -sum(np.log(e)) if min(e)>0 else 1e10
        z=np.r_[np.full(n,.5),np.zeros(n*n-n)]
        result=minimize(fun,z,method='SLSQP',constraints=[{'type':'ineq','fun':lambda z:1-C@z},{'type':'ineq','fun':lambda z:np.linalg.eigvalsh(matrix(z))-1e-7}],options={'ftol':1e-12,'maxiter':300})
        assert result.success
        error=np.linalg.norm(matrix(result.x)-np.eye(n));worst=max(worst,error);assert error<2e-5
checks['ellipsoid_contacts']={'finite_optimizations':16,'max_matrix_error':worst}

def monomials(n,m):return [a for a in it.product(range(m+1),repeat=n) if sum(a)==m]
spanchecks=0;shears=0
for n,m in [(2,k) for k in range(2,7)]+[(3,2),(3,3)]:
    z=s.symbols('z:'+str(n));mons=monomials(n,m);columns=[]
    covectors=[(1,k) for k in range(m+1)]+[(0,1)] if n==2 else [a for a in it.product(range(3),repeat=n) if any(a)]
    for ell in covectors:
        l=sum(a*b for a,b in zip(ell,z))
        for v in s.Matrix([ell]).nullspace():
            field=[s.Poly(l**m*vj,*z) for vj in v]
            columns.append(s.Matrix([f.coeff_monomial(a) for f in field for a in mons]))
            if shears<40:
                phi=s.Matrix(z)+l**m*v
                assert s.expand(phi.jacobian(z).det())==1
                assert all(s.expand(a-b)==0 for a,b in zip(phi.xreplace(dict(zip(z,s.Matrix(z)-l**m*v))),z))
                shears+=1
    rank=s.Matrix.hstack(*columns).rank()
    assert rank==n*math.comb(n+m-1,m)-math.comb(n+m-2,m-1)
    spanchecks+=1
checks['volume_shears']={'exact_spanning_dimensions':spanchecks,'exact_shear_inverses_and_jacobians':shears}

pairs=list(it.combinations(range(4),2))
def wedge(a,b):
    result=0
    for i,I in enumerate(pairs):
        for j,J in enumerate(pairs):
            if len(set(I+J))==4:
                inversions=sum(I[k]>J[l] for k in range(2) for l in range(2))
                result+=(-1)**inversions*a[i]*b[j]
    return result
def form(terms):return s.Matrix([terms.get(pair,0) for pair in pairs])
A=form({(0,2):1,(1,3):-1});T=form({(0,3):1,(1,2):1})
count=0
for _ in range(120):
    h=rng.randint(-4,4);y=rng.randint(1,5);C=h*A+y*T
    a,b,c,d=[rng.randint(-5,5) for j in range(4)]
    Hdet=a*b-c*c-d*d
    B=form({(0,1):a,(2,3):b,(0,2):c,(1,3):c,(0,3):d,(1,2):-d})+rng.randint(-4,4)*A+rng.randint(-4,4)*T
    G=s.Matrix([[wedge(u,v) for v in [A,C,B]] for u in [A,C,B]])
    assert (G.det()>0)==(Hdet>0)
    Omega=A+s.I*(C-h*A)/y
    assert s.expand(wedge(Omega,Omega))==0
    assert wedge(Omega,s.conjugate(Omega))==2*wedge(A,A)
    count+=1
checks['definite_pairs']={'exact_wedge_models':count}

A=form({(0,2):1,(1,3):1});basic=form({(0,1):1});count=0
for _ in range(100):
    cones=[]
    for j in range(2):
        u,r,h=[rng.randint(-4,4) for k in range(3)];q=abs(u)+abs(r)+rng.randint(1,4)
        M=s.Matrix([[h+u,r+q],[r-q,h-u]])
        C=form({(0,2):M[0,0],(0,3):M[0,1],(1,2):M[1,0],(1,3):M[1,1],(0,1):rng.randint(-4,4)})
        assert wedge(A,C)==s.trace(M)*wedge(A,A)/2
        assert wedge(C,C)==M.det()*wedge(A,A);cones.append(C)
    for j in range(11):
        C=(s.Rational(j,10)*cones[0]+s.Rational(10-j,10)*cones[1])
        assert wedge(C,C)*wedge(A,A)-wedge(A,C)**2>0
        AA=A+3*basic;CC=C-7*basic
        assert [wedge(AA,AA),wedge(AA,CC),wedge(CC,CC)]==[wedge(A,A),wedge(A,C),wedge(C,C)]
    count+=1
checks['mixed_cones']={'pairs':count,'convex_points':1100,'basic_additions':1100}

# Fourier symbol on the flat Hermitian four-torus, including the harmonic mode.
anti=s.Matrix.hstack(form({(0,2):1,(1,3):-1}),form({(0,3):1,(1,2):1}))
R=anti*(anti.T*anti).inv()*anti.T
def skew(a):
    M=s.zeros(4)
    for v,(i,j) in zip(a,pairs):M[i,j]=v;M[j,i]=-v
    return M
for _ in range(100):
    xi=s.Matrix([rng.randint(-5,5) for j in range(4)])
    if xi==s.zeros(4,1):xi[0]=1
    a=anti*s.Matrix([rng.randint(-5,5),rng.randint(-5,5)])
    one=skew(a).T*xi
    b=s.Matrix([2*(xi[i]*one[j]-xi[j]*one[i])/(xi.dot(xi)) for i,j in pairs])
    assert R*b==a
    assert all(s.expand(xi[i]*b[pairs.index((j,k))]-xi[j]*b[pairs.index((i,k))]+xi[k]*b[pairs.index((i,j))])==0 for i,j,k in it.combinations(range(4),3))
assert R*anti==anti # H restores the harmonic mode.
checks['closed_lift']={'exact_nonzero_fourier_symbols':100,'harmonic_mode':True}

# Linear correction of a positive separator, and the affine-class distinction.
for _ in range(100):
    L=s.Matrix(4,2,[rng.randint(-3,3) for j in range(8)])
    B=L.col_join(s.eye(2));RR=s.zeros(2,4).row_join(s.eye(2));P=s.Matrix([[1,0,0,0,0,0]])
    W=s.eye(6)[:,1:4];Z=B.row_join(W)
    TT=P*(s.eye(6)-B*RR);Q=TT-P
    assert TT*Z==s.zeros(1,5)
    assert Q*(s.eye(6)-s.diag(0,0,0,0,1,1))==s.zeros(1,6)
    alpha=-s.eye(6)[:,0]+B*s.Matrix([2,-1])
    assert (TT*alpha)[0]==-1
    assert (P*s.eye(6)[:,0])[0]==1 # Affine separation need not annihilate every closed direction.
checks['separator_correction']={'exact_linear_and_affine_models':100}

worst=0
for _ in range(30):
    Q=np.eye(3);H=np.eye(3);total=np.zeros((3,3));eps=.06
    for j in range(20):
        X=nr.normal(size=(3,3));E=X@X.T;E*=eps/(2*np.linalg.norm(E,2))
        ev,V=np.linalg.eigh(Q);root=(V*np.sqrt(ev))@V.T
        delta=root@E@root;newQ=Q-delta;newH=np.linalg.inv(newQ);B=newH-H;D=H@delta@H
        assert np.linalg.eigvalsh(B-D).min()>-1e-10
        assert np.linalg.eigvalsh(D/(1-eps)-B).min()>-1e-10
        total+=D;Q,H=newQ,newH
    assert np.linalg.eigvalsh(H-np.eye(3)-total).min()>-1e-9
    assert np.linalg.eigvalsh(total/(1-eps)-(H-np.eye(3))).min()>-1e-9
checks['inverse_increments']={'noncommuting_matrix_steps':600,'telescoped_sums':30}

def L(m,sigma):return 1 if m==0 else (m+1)*math.factorial(m+1)**sigma
decays={};models=0
for sigma in [1,2]:
    decays[str(sigma)]={str(m):float(sum(F(L(j,sigma)*L(m-j,sigma),L(m,sigma)) for j in range(1,m))) for m in [20,50,100,200]}
    assert decays[str(sigma)]['200']<decays[str(sigma)]['100']<decays[str(sigma)]['50']<decays[str(sigma)]['20']
    for _ in range(3):
        Js=[s.eye(2)]+[s.Matrix(2,2,[rng.randint(-2,2)*L(j,sigma)/s.Integer(10) for i in range(4)]) for j in range(1,13)]
        Ks=[s.eye(2)]
        for j in range(1,13):Ks.append(-sum((Js[l]*Ks[j-l] for l in range(1,j+1)),s.zeros(2)))
        for base in [1,2,4]:
            for j in range(1,13):
                assert sum((base**l*Js[l]*base**(j-l)*Ks[j-l] for l in range(j+1)),s.zeros(2))==s.zeros(2)
            models+=1
checks['factorial_inverse']={'convolution_ratios':decays,'exact_matrix_series_models':models,'orders_each':12}
result={'batch':'B038','status':'pass','scope':'Finite interfaces only; no global geometric theorem or Lean build certified.','checks':checks}
Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
