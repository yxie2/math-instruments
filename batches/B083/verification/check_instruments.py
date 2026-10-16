"""Finite and algebraic analogue checks; no spectrum or headline certification."""
from fractions import Fraction as F
from itertools import product, combinations, combinations_with_replacement
from pathlib import Path
import json, time, math
import numpy as np
import sympy as sp
from scipy.linalg import eigh

def compositions(total,length):
    if length==1:yield (total,);return
    for a in range(total+1):
        for rest in compositions(total-a,length-1):yield (a,)+rest
def slicing(x,ell):
    s=[F(0)]
    for a in x:s.append(s[-1]+a)
    return [[ell*max(F(0),min(s[a+1],F(r,ell))-max(s[a],F(r-1,ell))) for a in range(len(x))] for r in range(1,ell+1)]
def simplex_slices():
    cases=natural=0
    for j in range(4):
        for comp in compositions(4,j+1):
            x=list(map(lambda a:F(a,4),comp))
            for ell in range(1,7):
                rows=slicing(x,ell);assert all(sum(row)==1 and min(row)>=0 for row in rows)
                assert sum(sum(a>0 for a in row)>1 for row in rows)<=j;cases+=1
                for target in range(1,4):
                    for alpha in combinations_with_replacement(range(target),j+1):
                        push=lambda v:[sum(v[i] for i in range(j+1) if alpha[i]==k) for k in range(target)]
                        assert [push(row) for row in rows]==slicing(push(x),ell);natural+=1
    x=[F(3,10),F(7,10)];assert [r[::-1] for r in slicing(x,2)]!=slicing(x[::-1],2)
    return dict(rational_simplex_slices=cases,monotone_naturality_checks=natural,nonmonotone_permutation_control=True)

def boundary_restoration():
    rng=np.random.default_rng(8302);cases=0
    for t,n,s in [(1,4,1),(2,5,2),(3,4,3)]:
        f=rng.uniform(-1,1,(100,n,t));f[:,0,0]=1;f[::2,1,0]=-1
        g=f+rng.uniform(-.49,.49,f.shape);radii=np.max(abs(f),axis=2);chi=np.maximum(0,4*radii-3)
        gp=(1-chi[:,:,None])*g+chi[:,:,None]*f;rp=np.max(abs(gp),axis=2)
        delta=min(.5,np.min(np.sort(rp,axis=1)[:,-(s+1)])/2);assert delta>0
        G=gp/np.maximum(delta,rp)[:,:,None]
        assert np.max(abs(G))<=1+1e-12
        assert np.all(np.sum(np.max(abs(G),axis=2)>1-1e-12,axis=1)>=s+1)
        boundary=radii==1;assert np.allclose(G[boundary],f[boundary]);cases+=100
    delta=.2
    for x in [0,1e-9,-1e-9,.1,.2,.3]:
        val=x/max(delta,abs(x));assert abs(val)<=1 and (x!=0 or val==0)
    return dict(finite_compact_inputs=cases,whole_boundary_vectors_preserved=True,normalization_continuous_at_zero_control=True)

def complex_data(t):
    D=sp.zeros(6);D[2,1]=1;D[3,1]=1;D[4,2]=1;D[4,3]=-1
    h=sp.zeros(6);h[2,4]=1;h[2,5]=-t;r=sp.eye(6)-D*h-h*D
    Z=sp.diag(1,1,-1,-1,1,1);N=sp.eye(6)[:,[0,2]];K=sp.eye(6)[:,[0]]
    return D,h,r,Z,N,K
def chain_retraction():
    cases=0
    for t in [-3,-1,0,2,5]:
        D,h,r,Z,N,K=complex_data(t)
        assert D*D==sp.zeros(6) and r*r==r and D*r==r*D
        assert r*K==K and (r*N).rank()==K.rank() and (r*N).columnspace()==K.columnspace()
        assert r.rank()>K.rank()
        DD=sp.kronecker_product(D,sp.eye(6))+sp.kronecker_product(Z,D)
        HH=sp.kronecker_product(h,sp.eye(6))+sp.kronecker_product(r*Z,h)
        RR=sp.kronecker_product(r,r)
        assert DD*HH+HH*DD==sp.eye(36)-RR
        bad=sp.kronecker_product(h,sp.eye(6))+sp.kronecker_product(r,h)
        assert DD*bad+bad*DD!=sp.eye(36)-RR;cases+=1
    return dict(graded_complements=cases,signed_tensor_homotopies=cases,total_image_larger_than_K=True,missing_sign_control=True)

def joint_kernels():
    nil=sp.Matrix([[0,1],[0,0]]);rot=sp.Matrix([[1,1],[-1,-1]]);zero=sp.zeros(2);eye=sp.eye(2);cases=0
    for Slist in [[nil]*3,[nil,rot,nil,rot],[nil,zero,rot,eye],[eye]*4]:
        d=len(Slist);kernels=[];comps=[]
        for S in Slist:
            N=S.nullspace();basis=list(N);M=[]
            for e in sp.eye(2).columnspace():
                if not basis or sp.Matrix.hstack(*basis,e).rank()>len(basis):basis.append(e);M.append(e)
            kernels.append(N);comps.append(M)
        operators=[]
        for I in combinations(range(d),3):
            factors=[Slist[j] if j in I else eye for j in range(d)]
            factors.insert(1,eye) # Passive factor interspersed in the tensor order.
            operators.append(sp.kronecker_product(*factors))
        stack=sp.Matrix.vstack(*operators);cols=[]
        for size in range(3):
            for active in combinations(range(d),size):
                options=[comps[j] if j in active else kernels[j] for j in range(d)];options.insert(1,eye.columnspace())
                for chosen in product(*options):cols.append(sp.kronecker_product(*chosen))
        pred=sp.Matrix.hstack(*cols) if cols else sp.zeros(2**(d+1),0)
        assert stack*pred==sp.zeros(stack.rows,pred.cols)
        assert pred.rank()==stack.cols-stack.rank();cases+=1
    return dict(tensor_operator_lists=cases,nilpotent_zero_invertible_factors=True,interspersed_passive_factor=True)

def matching_parts(T,n,b):
    edges=[(i,j) for i,j in product(range(n),repeat=2) if np.linalg.norm(T[i*b:(i+1)*b,j*b:(j+1)*b])>0]
    N=max([sum(i==x for i,j in edges) for x in range(n)]+[sum(j==x for i,j in edges) for x in range(n)])
    colors=[]
    for edge in edges:
        for group in colors:
            if all(edge[0]!=e[0] and edge[1]!=e[1] for e in group):group.append(edge);break
        else:colors.append([edge])
    assert len(colors)<=2*N-1
    parts=[]
    for group in colors:
        A=np.zeros_like(T)
        for i,j in group:A[i*b:(i+1)*b,j*b:(j+1)*b]=T[i*b:(i+1)*b,j*b:(j+1)*b]
        parts.append(A)
    return parts,N
def matching_norms():
    rng=np.random.default_rng(8305);cases=0
    for n in [4,7,10]:
        for radius in [0,1,2]:
            b=2;T=np.zeros((n*b,n*b),dtype=complex)
            for i,j in product(range(n),repeat=2):
                if abs(i-j)<=radius:T[i*b:(i+1)*b,j*b:(j+1)*b]=rng.normal(size=(b,b))+1j*rng.normal(size=(b,b))
            parts,N=matching_parts(T,n,b);assert np.allclose(sum(parts),T)
            for A in parts:
                assert np.linalg.norm(A,2)<=np.linalg.norm(T,2)+1e-10
                sq=A.conj().T@A
                for i,j in product(range(n),repeat=2):
                    if i!=j:assert np.max(abs(sq[i*b:(i+1)*b,j*b:(j+1)*b]))<1e-12
            assert sum(np.linalg.norm(A,2) for A in parts)<=(2*N-1)*np.linalg.norm(T,2)+1e-10;cases+=1
    return dict(block_supports=cases,matching_counts_and_diagonal_squares=True,infinite_universal_norm_not_computed=True)

def multiplier_squares():
    rng=np.random.default_rng(8306)
    for _ in range(30):
        n=5;b=2;D=np.zeros((n*b,n*b),complex);perm=rng.permutation(n)
        for i,j in enumerate(perm):
            block=rng.normal(size=(b,b))+1j*rng.normal(size=(b,b));block/=max(1,np.linalg.norm(block,2));D[i*b:(i+1)*b,j*b:(j+1)*b]=block
        T=rng.normal(size=D.shape)+1j*rng.normal(size=D.shape);e,V=eigh(np.eye(n*b)-D.conj().T@D);W=(V*np.sqrt(np.maximum(e,0)))@V.conj().T
        assert np.allclose(T.conj().T@T-(D@T).conj().T@(D@T),(W@T).conj().T@(W@T))
        assert np.linalg.norm(D@T,2)<=np.linalg.norm(T,2)+1e-10 and np.linalg.norm(T@D,2)<=np.linalg.norm(T,2)+1e-10
        A=rng.normal(size=D.shape);assert np.allclose(D@(A@T),(D@A)@T) and np.allclose((D@T).conj().T,T.conj().T@D.conj().T)
    return dict(matching_contractions=30,positive_square_and_both_actions=True,finite_analogue_only=True)

def cofiber_quotients():
    cases=0
    # R/J = Q[x,y,z]/(x^2), all generators in degree two; multiplication by y is regular.
    for k in range(1,8):
        basis=lambda degree:[(a,b,c) for a in [0,1] for b in range(degree+1) for c in range(degree+1) if a+b+c==degree]
        src=basis(k-1);dst=basis(k);M=sp.zeros(len(dst),len(src))
        for j,(a,b,c) in enumerate(src):M[dst.index((a,b+1,c)),j]=1
        assert M.rank()==len(src) and len(dst)-M.rank()==sum(b==0 for a,b,c in dst)
        for unit in [sp.Rational(2,3),-4]:assert (unit*M).columnspace()==M.columnspace() or (unit*M).rank()==M.rank()
        cases+=1
    # Multiplication by x on Q[x]/(x^2) has both a kernel and a cokernel in its cone.
    zero_divisor=sp.Matrix([[0,0],[1,0]])
    assert 2-zero_divisor.rank()==1 and len(zero_divisor.nullspace())==1
    return dict(regular_graded_pieces=cases,zero_divisor_extra_cone_kernel=True,actual_spectrum_maps_not_tested=True)

def finite_descent():
    D,_,_,_,_,_=complex_data(2);cases=0
    for p in [2,3,5,7]:
        for s in [2,3,5,11]:
            if s%p==0:continue
            for a in [1,2,6]:
                source=(D.row_join(sp.Rational(a,s)*sp.eye(6))).col_join(sp.zeros(6).row_join(-D))
                target=(D.row_join(a*sp.eye(6))).col_join(sp.zeros(6).row_join(-D))
                T=sp.diag(*([1]*6+[sp.Rational(1,s)]*6))
                assert source*source==sp.zeros(12) and target*T==T*source
                def mod(x):num,den=sp.fraction(x);return int(num)*pow(int(den),-1,p)%p
                assert all(mod(x)==0 for x in target*T-T*source)
                assert mod(T.det())!=0;cases+=1
        try:pow(p,-1,p)
        except ValueError:pass
        else:raise AssertionError('nonunit denominator unexpectedly invertible')
    return dict(localized_chain_cone_isomorphisms=cases,nonunit_denominator_controls=4,finite_spectra_compactness_not_tested=True)

if __name__=='__main__':
    start=time.perf_counter();checks={}
    for f in [simplex_slices,boundary_restoration,chain_retraction,joint_kernels,matching_norms,multiplier_squares,cofiber_quotients,finite_descent]:checks[f.__name__]=dict(status='pass',details=f())
    result=dict(batch='B083',status='pass',elapsed_seconds=round(time.perf_counter()-start,3),scope='Selected finite mechanisms and chain-complex analogues; no topological headline or Lean certification.',checks=checks)
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8');print(json.dumps(result))
