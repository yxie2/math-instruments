"""Selected finite models; no global operator-algebra or topology claim."""
import itertools as it
import json
import random
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import numpy as np
import sympy as s
from sympy.polys.fields import field
from sympy.polys.domains import GF
rng=random.Random(41016);nr=np.random.default_rng(41016);out={}
def spectral(A,f):
    vals,U=np.linalg.eigh(A);return (U*f(vals))@U.T.conj()
worst=0
for _ in range(100):
    n=5;m=7;r=3
    U=np.linalg.qr(nr.normal(size=(n,n)))[0];V=np.linalg.qr(nr.normal(size=(m,m)))[0]
    d=U@np.diag([2,1,.7,.1,0])@U.T;eps=.2
    h=spectral(d,lambda t:np.maximum(t-eps,0));support=U[:,:r]@U[:,:r].T
    w=V[:,:r]@U[:,:r].T;Z=nr.normal(size=(r,r));l=U[:,:r]@(Z@Z.T)@U[:,:r].T
    mapped=w@l@w.T;cut=spectral(mapped,lambda t:np.maximum(t-.3,0));other=w@spectral(l,lambda t:np.maximum(t-.3,0))@w.T
    R=w@spectral(l,lambda t:np.sqrt(np.maximum(t,0)))
    err=max(np.linalg.norm(w.T@w-support),np.linalg.norm(cut-other),np.linalg.norm(R.T@R-l),abs(np.linalg.norm(mapped,2)-np.linalg.norm(l,2)))
    worst=max(worst,err);assert err<1e-10
out['cut_transport']={'rectangular_matrix_models':100,'max_error':worst,'general_bidual_membership_tested':False}

tests=0
for _ in range(100):
    z=np.array([rng.random() for _ in range(8)]);eps=.4
    ideal={i for i,t in enumerate(z) if t>=eps};b=np.array([t if i in ideal else 0 for i,t in enumerate(z)])
    assert max(abs(z-b))<eps
    cut=np.maximum(z-eps,0);assert all(cut[i]==0 for i in set(range(8))-ideal)
    f=z*z;g=np.sqrt(z);assert np.array_equal(f>0,g>0);tests+=1
out['ideal_cutoff']={'commutative_quotient_models':tests}

tests=0
for n in range(3,12):
    edges=list(it.combinations(range(n),2));tri=[(0,i,j) for i in range(1,n) for j in range(i+1,n)]
    d0=s.zeros(len(edges),n)
    for k,(i,j) in enumerate(edges):d0[k,i]=-1;d0[k,j]=1
    d1=s.zeros(len(tri),len(edges))
    for k,(a,b,c) in enumerate(tri):
        for e,sign in [((a,b),1),((b,c),1),((a,c),-1)]:d1[k,edges.index(e)]=sign
    assert d1*d0==s.zeros(len(tri),n);assert len(edges)-d1.rank()==d0.rank();tests+=1
# A three-cycle without a filling has a non-gradient cocycle.
assert 3-s.zeros(0,3).rank()>2
out['closed_gradients']={'filled_fan_models':tests,'missing_simple_connectivity_control':True,'infinite_range_closedness_tested':False}

tests=0
for _ in range(100):
    F=[Q(rng.randrange(21),20) for i in range(12)];lam=[Q(rng.randrange(1,10),10) for i in range(11)]
    near={i:[j for j in range(11) if abs(i-j)<=1] for i in range(11)}
    levels=sorted(set([Q(0),Q(1)]+F));integral=Q(0)
    for a,b in zip(levels,levels[1:]):
        t=(a+b)/2;integral+=(b-a)*sum(lam[j] for i in range(11) if min(F[i:i+2])<t<max(F[i:i+2]) for j in near[i])
    rhs=sum(abs(F[i+1]-F[i])*sum(lam[j] for j in near[i]) for i in range(11));assert integral==rhs;tests+=1
a={i:Q(i+1,10) for i in range(5)};b={i:Q(i+2,10) for i in range(-2,3)}
assert sum(v*b.get(i+20,0) for i,v in a.items())==0
out['translated_coarea']={'exact_integral_models':tests,'finite_support_translation_control':True}

tests=0
for p in [3,5]:
    K,x=field('x',GF(p))
    def node(j):
        ans=K.zero;power=x
        while j:ans+=(j%p)*power;j//=p;power*=x
        return ans
    def val(f):
        if not f:return 10**9
        return min(k[0] for k in f.numer)-min(k[0] for k in f.denom)
    for m in range(7):
        nodes=[node(j) for j in range(m+1)];budget=sum(m//(p**l) for l in range(6))
        weights=[]
        for i in range(m+1):
            den=K.one
            for j in range(m+1):
                if i!=j:den*=nodes[i]-nodes[j]
            weights.append(x**budget/den);assert val(weights[-1])>=0
        for n in range(m+5):
            moment=sum((w*(u**n if n else K.one) for w,u in zip(weights,nodes)),K.zero)
            if n<m:assert moment==0
            elif n==m:assert not(moment-x**budget),(p,m,n,moment,x**budget)
            else:assert val(moment)>=budget+n-m
            tests+=1
out['integral_divided_differences']={'exact_moment_checks':tests,'node_model':'base-p digits in x F_p[[x]]'}

def rankmod(A,p):
    A=[list(row) for row in A];r=0
    for j in range(len(A[0])):
        piv=next((i for i in range(r,len(A)) if A[i][j]%p),None)
        if piv is None:continue
        A[r],A[piv]=A[piv],A[r];z=pow(A[r][j]%p,-1,p);A[r]=[v*z%p for v in A[r]]
        for i in range(len(A)):
            if i!=r:
                z=A[i][j]%p;A[i]=[(a-z*b)%p for a,b in zip(A[i],A[r])]
        r+=1
    return r
tests=0
for p in [3,5,7]:
    for degree in [1,2]:
        X=p;M=degree
        A=[[comb(z,m)%p for m in range((M+1)*X)] for z in range(p*X)]
        assert rankmod(A,p)==(M+1)*X
        for z in range(p*X):
            for m in range((M+1)*X):assert comb(z,m)%p==(comb(z%p,m%p)*comb(z//p,m//p))%p
        tests+=1
p=1000000000039;M=100001;kappa=Q(p,p-1);q=p+1
assert s.isprime(p) and M>=81 and M%2 and p>16*M*M and (2*(M//8))**3>p
assert Q(q,2*M)-kappa*(M+1)>1
out['digit_control']={'exact_lucas_basis_models':tests,'large_parameter_budget_checked':True,'full_group_operation_algebra_tested':False}

def cols(v,n):return s.Matrix.hstack(*v) if v else s.zeros(n,0)
def basis(A):return cols(A.columnspace(),A.rows)
def intersect(A,B):
    sol=A.row_join(-B).nullspace();return basis(cols([A*v[:A.cols,0] for v in sol],A.rows))
def extend(start,candidates):
    ans=start
    for v in candidates.columnspace():
        if ans.row_join(v).rank()>ans.cols:ans=ans.row_join(v)
    return ans
tests=0;noncomplex=0
for _ in range(50):
    n=6;I=s.eye(n);delta=s.zeros(n);delta[0,4]=delta[1,5]=1
    B=I[:,0:2];Z=I[:,0:4]
    # Degree 0: A_0,W; degree 1: B,A_1. Arbitrary graded K need not be stable.
    candidates=[]
    for positions in [[2,4,5],[0,1,3]]:
        for j in range(rng.randrange(4)):
            v=s.zeros(n,1)
            for i in positions:v[i]=rng.randrange(-2,3)
            candidates.append(v)
    K=basis(cols(candidates,n));KZ=intersect(K,Z);KB=intersect(K,B)
    temp=extend(KB,KZ);A0=temp[:,KB.cols:]
    BA=extend(B.row_join(A0),Z);A=BA[:,B.cols:]
    temp=extend(KZ,K);W0=temp[:,KZ.cols:];ZW=extend(Z.row_join(W0),I);W=ZW[:,Z.cols:]
    T=B.row_join(A).row_join(W);Ti=T.inv();P=T*s.diag(0,0,1,1,0,0)*Ti
    hom=s.zeros(n)
    # delta: W -> B has an invertible 2x2 coordinate matrix.
    C=(Ti*delta*W)[:2,:];hom=W*C.inv()*Ti[:2,:]
    assert P*P==P and delta*P==s.zeros(n) and P*delta==s.zeros(n)
    assert delta*hom+hom*delta==I-P
    assert K.row_join(P*K).rank()==K.cols
    if K.row_join(delta*K).rank()>K.cols:noncomplex+=1
    tests+=1
out['subspace_projection']={'exact_complex_models':tests,'non_subcomplex_inputs':noncomplex}

tests=0
for _ in range(60):
    # A commuting homotopy package gives an induced zero commutator.
    D=s.zeros(4);D[1,0]=1
    a=s.Matrix([0,rng.randrange(-3,4),rng.randrange(-3,4),rng.randrange(-3,4)])
    T=s.zeros(4);T[0,2]=rng.randrange(-3,4);T[0,3]=rng.randrange(-3,4)
    C=D*T-T*D;aprime=-T*a
    assert D*a==s.zeros(4,1) and D*aprime+C*a==s.zeros(4,1);tests+=1
out['square_zero_lift']={'exact_first_order_cycle_models':tests,'full_graph_form_context_tested':False}
result={'batch':'B041','status':'pass','scope':'Finite selected interfaces; no global theorem or Lean build certified.','checks':out}
Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
