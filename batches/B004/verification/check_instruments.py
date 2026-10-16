"""Finite checks of selected B004 identities; no global theorem certification."""
from fractions import Fraction as Q
from itertools import product
from math import erf, exp, log, pi, sqrt
from pathlib import Path
import json
import random

import numpy as np

SEED=20261016
rng=np.random.default_rng(SEED)
random.seed(SEED)


def deficit_model():
    for n in range(1,13):
        a=[Q(random.randint(-5,5),3) for _ in range(n)]
        b=[Q(random.randint(-7,7),4) for _ in range(n)]
        # nu=N(0,I), eta=N(a,I), p=N(b,Sigma): covariance terms cancel in both differences.
        entropy_difference=sum(x*y-x*x/2 for x,y in zip(a,b))
        fisher_difference=sum(y*y-(y-x)**2 for x,y in zip(a,b))
        assert fisher_difference==2*entropy_difference
    return {'exact_gaussian_mean_models':12,'scope':'Deficit algebra only; not the strict optimizer-existence lemma.'}


def symmetric_tensor(n,d):
    values={tuple(sorted(i)):rng.normal() for i in product(range(n),repeat=d)}
    a=np.empty((n,)*d)
    for i in product(range(n),repeat=d):a[i]=values[tuple(sorted(i))]
    return a/np.linalg.norm(a)


def action(h,a,axis):
    return np.moveaxis(np.tensordot(h,a,axes=(1,axis)),0,axis)


def tensor_average():
    worst_slack=float('inf');worst_correlation=float('inf');cases=0;singular=0
    for n in [2,3]:
        for k in [2,3,4,5]:
            for mode in range(6):
                tensors=[symmetric_tensor(n,k),symmetric_tensor(n,k+1)]
                if mode==0:
                    tensors=[]
                    for d in [k,k+1]:
                        a=np.zeros((n,)*d);a[(0,)*d]=1;tensors.append(a)
                    singular+=1
                h=rng.normal(size=(n,n));h=(h+h.T)/2
                rho=np.zeros((n,n));lhs=0.;corr=0.;energy=0.
                for a in tensors:
                    f=a.reshape(n,-1);rho+=f@f.T
                    av=sum(action(h,a,j) for j in range(a.ndim))/a.ndim
                    lhs+=float(np.sum(av*av))
                    corr+=float(np.sum(a*action(h,action(h,a,1),0)))
                    energy+=float(np.sum(action(h,a,0)**2))
                eig,u=np.linalg.eigh(rho);assert eig.min()>-1e-12
                root=(u*np.sqrt(np.maximum(eig,0)))@u.T
                geometric=float(np.trace(root@h@root@h))
                assert geometric+2*energy/k>=lhs-1e-10
                assert geometric>=abs(corr)-1e-10
                assert abs(energy-np.trace(rho@h@h))<1e-10
                worst_slack=min(worst_slack,geometric+2*energy/k-lhs)
                worst_correlation=min(worst_correlation,geometric-abs(corr));cases+=1
    return {'direct_sum_examples':cases,'singular_reductions':singular,'minimum_averaging_slack':worst_slack,
            'minimum_correlation_slack':worst_correlation,'scope':'Finite symmetric tensors, not the asymptotic hierarchy.'}


def covariance_stability():
    nodes,weights=np.polynomial.legendre.leggauss(384)
    u=(nodes+1)/2;weights=weights/2;t=u/(1-u)
    integration_weight=weights/u**2
    worst_ratio=0.;cases=0;kvalues={}
    for cap in [1.,2.,10.,100.]:
        kval=float(np.sum(weights/(1-u)**2/((1+t/cap)**3*(1+(1+1/cap)*t))))
        assert 0<kval<=log(1+cap)+1e-10;kvalues[str(cap)]=kval
        for n in range(1,5):
            for mode in range(4):
                x=rng.normal(size=(n,n));a=x@x.T/n
                x=rng.normal(size=(n,n));b=x@x.T/n
                if mode==0:b=np.zeros((n,n))
                va,ua=np.linalg.eigh(a);vb,ub=np.linalg.eigh(b)
                va=np.maximum(va,0);vb=np.maximum(vb,0)
                aval=t[:,None]*va[None,:]**2;bval=t[:,None]*vb[None,:]**2
                ha=np.sqrt(1+aval/(1+aval/cap));hb=np.sqrt(1+bval/(1+bval/cap))
                ma=np.einsum('ij,tj,kj->tik',ua,ha,ua)
                mb=np.einsum('ij,tj,kj->tik',ub,hb,ub)
                lhs=float(integration_weight@np.sum((ma-mb)**2,axis=(1,2)))
                rhs=kval*float(np.sum((a-b)**2))
                assert lhs<=rhs+1e-7
                worst_ratio=max(worst_ratio,lhs/rhs if rhs else 0);cases+=1
    return {'matrix_examples':cases,'quadrature_nodes':384,'K_L_estimates':kvalues,
            'maximum_bound_ratio':worst_ratio,'scope':'Numerical quadrature including singular noncommuting inputs; no rigorous error enclosure.'}


def deletion_and_triangle():
    count=0
    for m in range(3,11):
        z=[[Q(random.randint(-5,5)) for _ in range(4)] for _ in range(m-1)]
        z.append([-sum(row[j] for row in z) for j in range(4)])
        c=sum(v*v for row in z for v in row)
        for i in range(m):
            remaining=sum((z[j][a]+z[i][a]/(m-1))**2 for j in range(m) if j!=i for a in range(4))
            assert remaining==c-Q(m,m-1)*sum(v*v for v in z[i]);count+=1
    for i in range(1,25):
        s=Q(i,7);b=3*s
        # Integrate (b-a)^2/2 from 0 to b, after integrating the positive affine function in the second variable.
        coefficients=[b*b/2,-b,Q(1,2)]
        integral=sum(c*b**(j+1)/(j+1) for j,c in enumerate(coefficients))
        assert integral==(3*s)**3/6
    nodes,w=np.polynomial.legendre.leggauss(192);u=(nodes+1)/2;w=w/2;t=u/(1-u)
    maxerror=0.
    for q in [-3.,-2.,-1.,-.5,0.]:
        val=float(sum(ww*(.5*erf((q-tt)/sqrt(2))+.5)/(1-uu)**2 for uu,tt,ww in zip(u,t,w)))
        target=q*(.5+.5*erf(q/sqrt(2)))+exp(-q*q/2)/sqrt(2*pi)
        maxerror=max(maxerror,abs(val-target));assert abs(val-target)<1e-10
    return {'exact_recentered_lists':count,'exact_triangle_integrals':24,'tail_integral_max_error':maxerror,
            'scope':'Algebra and tail integrals only; arbitrary lists in this check are not claimed to be extremal partitions.'}


def shift_constants():
    ell=Q(5,2);kappa=Q(1,100);delta=Q(1,4)
    assert ell*(1-2*ell*kappa)/2==Q(19,16)>1
    assert ell-1+delta==Q(7,4)<2
    count=0
    for i in range(-149,150):
        c=Q(i,100)
        for j in range(-25,26):
            q=Q(j,100);signed=q+(1 if q<=c else -1)
            assert c-1<=signed<=c+1;count+=1
    return {'exact_height_margin':'19/16','exact_interval_examples':count,
            'scope':'Margins in the section argument; not its analytic spectral hypothesis.'}


def predictor_checks():
    worst_column=0.;worst_cancel=0.;worst_identity=0.;cases=0
    for d in [1,2,4,7]:
        for n in [1,5,20,50]:
            sigma=.2
            vectors=rng.normal(size=(n,d));vectors/=np.maximum(np.linalg.norm(vectors,axis=1),1)[:,None]
            vectors[0]=0 # Include the zero-vector convention.
            b=sigma*vectors
            r=np.zeros((d,d+n));r[:,:d]=np.eye(d)
            rows=[];states=[r.copy()];filters=[]
            for i in range(n):
                eta=1/(1+sqrt(1-float(b[i]@b[i])))
                c=np.eye(d)-eta*np.outer(b[i],b[i])
                error=float(np.linalg.norm(c@c+np.outer(b[i],b[i])-np.eye(d)))
                worst_identity=max(worst_identity,error)
                row=eta*b[i]@r;row[:d]=0
                assert np.linalg.norm(row[d+i:])<1e-12
                rows.append(row);filters.append((eta,c))
                r=c@r;r[:,d+i]+=b[i];states.append(r.copy())
            m=np.array(rows);column_squares=np.sum(m*m,axis=0)
            assert column_squares.max()<=sigma**2+1e-12
            worst_column=max(worst_column,float(column_squares.max()/sigma**2))
            x=np.zeros(d+n);signs=rng.choice([-1.,1.],size=n);prefix=np.zeros(d)
            for i in range(n):
                x[d+i]=m[i]@x+signs[i];prefix+=signs[i]*b[i]
                error=float(np.linalg.norm(states[i+1]@x-prefix))
                worst_cancel=max(worst_cancel,error);assert error<1e-11
            q=rng.uniform(.1,2,d+n)
            assert np.sum(column_squares*q)<=sigma**2*q.sum()+1e-12
            cases+=1
    return {'finite_filter_examples':cases,'max_column_budget_ratio':worst_column,
            'max_filter_identity_error':worst_identity,'max_prefix_cancellation_error':worst_cancel,
            'scope':'Predictor algebra with arbitrary signs; does not assert these coefficients lie in the required path body.'}


def main():
    checks={name:fn() for name,fn in [('deficit_model',deficit_model),('symmetric_slots',tensor_average),
        ('covariance_stability',covariance_stability),('deletion_and_triangle',deletion_and_triangle),
        ('shift_constants',shift_constants),('predictor_columns',predictor_checks)]}
    report={'status':'passed','seed':SEED,'numpy_version':np.__version__,'checks':checks,
            'limitation':'Finite calculations do not certify the global source theorems, formalizations or novelty.'}
    (Path(__file__).parent/'results.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()
