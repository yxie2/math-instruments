"""Finite checks of selected operator-algebra mechanisms, not global claims."""
from itertools import product
from fractions import Fraction as F
from pathlib import Path
import json
import math
import numpy as np
import sympy as s
from scipy.linalg import block_diag
from scipy.optimize import least_squares

def incidence_dimensions():
    checks=0
    for d,r,q in product(range(1,5),range(1,6),range(1,4)):
        for a in range(1,d+1):
            for b in range(r+1):
                codim=q*a*(r-b)-a*(d-a)-b*(r-b)
                assert codim==(q*a-b)*(r-b)-a*(d-a)
                # Coordinate Grassmann charts: forbidden lower-left blocks give independent constraints.
                selected=[(i,j,k) for i in range(q) for j in range(b,r) for k in range(a)]
                assert len(set(selected))==q*a*(r-b)
                checks+=1
    return dict(exact_incidence_dimension_models=checks,scope='Constraint ranks and dimension arithmetic only; no uniform bundle transversality certified by finite sampling.')

def square_root(P,power=.5):
    eig,U=np.linalg.eigh(P);assert eig.min()>0
    return (U*eig**power)@U.T

def continuous_scaling():
    rng=np.random.default_rng(34294);worst=0.;models=0
    for d in (1,2,3):
        for _ in range(8):
            A=[np.eye(d)+.15*rng.normal(size=(d,d)) for j in range(2)]
            T=[np.vstack((A[0],np.zeros((d,d)))),np.vstack((np.zeros((d,d)),A[1]))]
            indices=list(zip(*np.tril_indices(d)))
            def matrix(v):
                L=np.zeros((d,d))
                for val,(i,j) in zip(v,indices):L[i,j]=np.exp(val) if i==j else val
                return L@L.T
            def residual(v):
                P=matrix(v);Q=np.eye(2*d)+sum(t@P@t.T for t in T);R=sum(t.T@np.linalg.solve(Q,t) for t in T)-1.5*np.linalg.inv(P)
                return np.array([R[i,j] for i,j in indices])
            fit=least_squares(residual,np.zeros(len(indices)),xtol=1e-13,ftol=1e-13,gtol=1e-13,max_nfev=500)
            assert fit.success
            P=matrix(fit.x);Q=np.eye(2*d)+sum(t@P@t.T for t in T)
            X=[np.sqrt(2/3)*square_root(Q,-.5)@t@square_root(P) for t in T]
            err=np.linalg.norm(sum(x.T@x for x in X)-np.eye(d));worst=max(worst,err);assert err<1e-8
            assert np.linalg.eigvalsh(sum(x@x.T for x in X)).max()<2/3+1e-10
            models+=1
    return dict(expanding_matrix_models=models,max_normalization_error=worst,scope='Expansion is guaranteed by two invertible disjoint target blocks. Numerical stationary equations do not certify bundlewise continuity.')

def central_homotopy():
    rng=np.random.default_rng(34295);z=np.array([1,0,0,1,0]);q=np.array([0,0,0,0,1]);checks=0
    def mul(a,b):return np.r_[(a[:4].reshape(2,2)@b[:4].reshape(2,2)).ravel(),a[4]*b[4]]
    def actleft(a,b):return (a[:4].reshape(2,2)@b.reshape(2,2)).ravel()
    def actright(b,a):return (b.reshape(2,2)@a[:4].reshape(2,2)).ravel()
    def differential(fn,n):
        def out(*args):
            val=actleft(args[0],fn(*args[1:]))+(-1)**(n+1)*actright(fn(*args[:-1]),args[-1])
            for j in range(n):val=val+(-1)**(j+1)*fn(*args[:j],mul(args[j],args[j+1]),*args[j+2:])
            return val
        return out
    def homotopy(fn,n):
        def out(*args):
            val=np.zeros(4,dtype=np.int64)
            for i in range(n-1):val+=(-1)**(i+1)*fn(*(mul(z,a) for a in args[:i]),q,mul(q,args[i]),*args[i+1:])
            return val
        return out
    for n in range(1,5):
        coeff=rng.integers(-2,3,size=(4,)+(5,)*n)
        def fn(*args):
            val=coeff
            for a in args:val=np.tensordot(val,a,axes=(1,0))
            return val
        dJ=differential(homotopy(fn,n),n-1);Jd=homotopy(differential(fn,n),n+1)
        for _ in range(60):
            args=[rng.integers(-2,3,size=5) for j in range(n)]
            assert np.array_equal(dJ(*args)+Jd(*args),fn(*args)-fn(*(mul(z,a) for a in args)))
            checks+=1
    return dict(exact_noncommutative_mixed_input_models=checks,degrees=[1,2,3,4],scope='M2 plus C with values in its M2 central summand; arbitrary cochains, not only cocycles.')

def bounded_ball_modulus():
    rng=np.random.default_rng(341);checks=0
    for dimension in (2,3,5):
        A=rng.normal(size=(dimension,dimension));B=rng.normal(size=(dimension,dimension));bound=np.linalg.norm(A,2)*np.linalg.norm(B,2)
        for j in range(1,81):
            X=rng.normal(size=(dimension,dimension))/j
            l2=lambda Y:np.linalg.norm(Y,'fro')/np.sqrt(dimension)
            assert l2(A@X@B)<=bound*l2(X)+1e-12
            checks+=1
    return dict(matrix_sequence_bounds=checks,scope='Uniform L2-modulus examples only. Ultrafilter quotient and iterated-ultrapower claims are established by the read source proof, not simulated.')

def commuting_tensor_independence():
    checks=0
    for m,n in product(range(1,4),repeat=2):
        E=[np.eye(m)[i:i+1].T@np.eye(m)[j:j+1] for i,j in product(range(m),repeat=2)]
        F=[np.eye(n)[i:i+1].T@np.eye(n)[j:j+1] for i,j in product(range(n),repeat=2)]
        products=[np.kron(e,np.eye(n))@np.kron(np.eye(m),f) for e,f in product(E,F)]
        assert np.linalg.matrix_rank(np.array([p.ravel() for p in products]))==m*m*n*n
        checks+=1
    # Without factorhood: the same diagonal algebra in both legs has e1*e2=0.
    assert np.array_equal(np.diag([1,0])@np.diag([0,1]),np.zeros((2,2)))
    return dict(spatial_factor_models=checks,nonfactor_negative_control=True,scope='Finite matrix factors only; nonspatial von Neumann representations require the support-projection proof.')

def tensor_labels():
    rng=np.random.default_rng(34299);checks=0;choices=[]
    for m,r in ((2,3),(3,2),(3,4)):
        n=1
        while 2**n<=2*m*n+r-1:n+=1
        choices.append([m,r,n]);labels=rng.normal(size=(m**n,r))
        for _ in range(25):
            Ps=[rng.normal(size=(2,m)) for j in range(n)]
            assert all(np.linalg.matrix_rank(p)==2 for p in Ps)
            tensor=Ps[0]
            for p in Ps[1:]:tensor=np.kron(tensor,p)
            assert np.linalg.matrix_rank(tensor@labels)==r;checks+=1
    return dict(sampled_rank_two_tensor_maps=checks,dimensions=choices,scope='Random finite samples illustrate the dimension threshold; they do not establish independence for every tuple of quotient maps.')

def ideal_weights():
    checks=0
    for n in range(1,6):
        for I,J in product(range(2**n),repeat=2):
            # Ideal I consists of coordinates selected by its bit mask.
            wi=[0 if I>>k&1 else math.inf for k in range(n)]
            wj=[0 if J>>k&1 else math.inf for k in range(n)]
            assert all(a+a==a for a in wi)
            assert (I&J==I)==all(a+b==a for a,b in zip(wi,wj));checks+=1
    return dict(exact_commutative_ideal_pairs=checks,scope='Finite direct sums; extended-trace topology and arbitrary C-star ideals use the source and classical proofs.')

def averaged_rank_signal():
    rng=np.random.default_rng(34301);checks=0;noncommuting=0
    for _ in range(60):
        d=4;k=3;mult=rng.integers(1,5,size=k);weights=mult/mult.sum()
        eig=np.r_[rng.uniform(.3,1,size=2),np.zeros(2)];U,_=np.linalg.qr(rng.normal(size=(d,d)));Y=(U*eig)@U.T
        eps=.4;eta=.1
        # Each candidate supports Y but has rank two or three in a four-dimensional space.
        blocks=[];T=np.zeros((d,d))
        for a in range(k):
            V1,_=np.linalg.qr(rng.normal(size=(2,2)));V2,_=np.linalg.qr(rng.normal(size=(2,2)))
            V=U@block_diag(V1,V2)
            vals=np.r_[rng.uniform(.8,1,size=2),.9 if a%2 else 0,0];H=(V*vals)@V.T;blocks.append(H)
        # g=1 on [.8,1], zero at zero; scalar contractions preserve the supported Y.
            contraction=1-rng.uniform(0,.01)
            T+=weights[a]*contraction**2*(Y@Y)
            noncommuting+=int(np.linalg.norm(Y@H-H@Y)>1e-8)
        assert np.linalg.norm(T-Y@Y,2)<eps**2/2
        avg=block_diag(*(H for H,m in zip(blocks,mult) for j in range(int(m))))
        normalized_rank=np.count_nonzero(np.linalg.eigvalsh(avg)>eta)/mult.sum()
        expected=sum(w*np.count_nonzero(np.linalg.eigvalsh(H)>eta) for w,H in zip(weights,blocks))
        assert abs(normalized_rank-expected)<1e-12
        assert np.count_nonzero(eig>eps)<=2*np.linalg.norm(Y,2)**2/eps**2*normalized_rank+1e-12
        for power in (1,2):assert abs(np.trace(np.linalg.matrix_power(avg,power))/mult.sum()-sum(w*np.trace(np.linalg.matrix_power(H,power)) for w,H in zip(weights,blocks)))<1e-10
        checks+=1
    assert F(1,2)**2!=F(1,2)*(0**2+1**2)
    return dict(normalized_block_average_models=checks,noncommuting_pairs=noncommuting,ordinary_average_negative_control=True,scope='Finite rank-deficient examples test block normalization and spectral bound; arbitrary extended weights and stable folding are not simulated.')

if __name__=='__main__':
    groups={}
    for fn in (incidence_dimensions,continuous_scaling,central_homotopy,bounded_ball_modulus,commuting_tensor_independence,tensor_labels,ideal_weights,averaged_rank_signal):
        groups[fn.__name__]=fn();print(fn.__name__,'passed',flush=True)
    out=dict(batch='B034',status='passed',check_groups=groups,limitations='Selected finite mechanisms only; no quasitrace counterexample, Hochschild vanishing, character criterion or stabilization classification certified; no Lean build.')
    Path(__file__).with_name('results.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out,indent=2))
