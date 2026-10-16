"""Finite algebra and numerical examples for B003; not a proof certification."""
from fractions import Fraction as Q
from itertools import product
from math import factorial, log
from pathlib import Path
import json
import random

import numpy as np

SEED = 20261016
random.seed(SEED)
rng = np.random.default_rng(SEED)


def tensor_checks():
    count = 0
    for n in range(1, 6):
        idx = list(product(range(n), repeat=3))
        for _ in range(12):
            s_values = {tuple(sorted(i)): random.randint(-5, 5) for i in idx}
            j_values = {(i, min(j, k), max(j, k)): random.randint(-5, 5) for i, j, k in idx}
            s = {i: Q(s_values[tuple(sorted(i))]) for i in idx}
            j = {(i, a, b): Q(j_values[i, min(a, b), max(a, b)]) for i, a, b in idx}
            left = sum(2*s[t]**2+4*s[t]*j[t]+j[t]**2+j[t]*j[t[1],t[0],t[2]] for t in idx)
            right = sum(2*(s[i,a,b]+(j[i,a,b]+j[a,i,b]+j[b,i,a])/3)**2
                        +(j[i,a,b]-j[a,i,b])**2/6 for i,a,b in idx)
            assert left == right and right >= 0
            count += 1
    # Dropping the last-two-index symmetry is not licensed by the identity.
    j = {(i,a,b): Q(1 if (i,a,b)==(0,0,1) else 0) for i,a,b in product(range(2), repeat=3)}
    left = sum(v*v+v*j[a,i,b] for (i,a,b),v in j.items())
    right = sum(2*((j[i,a,b]+j[a,i,b]+j[b,i,a])/3)**2+(j[i,a,b]-j[a,i,b])**2/6 for i,a,b in j)
    assert left != right
    return {'exact_tensor_examples': count, 'negative_control_without_symmetry': 'detected',
            'scope': 'The pointwise square identity only; not the integrated transport estimate.'}


def gaussian_operator_check():
    # Polynomials in ascending order, using exact integers. Probabilists' Hermite recurrence.
    def add(a,b,scale=1):
        out = [0]*max(len(a),len(b))
        for i,v in enumerate(a): out[i]+=v
        for i,v in enumerate(b): out[i]+=scale*v
        while len(out)>1 and out[-1]==0:out.pop()
        return out
    def op(a):
        first=[i*v for i,v in enumerate(a)]
        second=[(i+2)*(i+1)*a[i+2] for i in range(max(0,len(a)-2))]
        return add(first,second,-1)
    hs=[[1],[0,1]]
    for k in range(1,14):hs.append(add([0]+hs[-1],hs[-2],-k))
    for k,h in enumerate(hs):
        assert op(h)==[k*v for v in h]
        assert add(op(op(h)),op(h),-1)==[k*(k-1)*v for v in h] or k<=1
    return {'Hermite_degrees': [0,14], 'kernel_degrees': [0,1],
            'scope': 'Gaussian polynomial model only; no assertion of general range density.'}


def projection_checks():
    worst_error=0.0; worst_ratio=0.0; maximum_iterations=0
    for n in range(3,9):
        edges=[(i,j) for i in range(n) for j in range(i+1,n)]
        b=np.zeros((len(edges),n-1))
        points=rng.normal(size=(n,4))
        delta=np.array([np.linalg.norm(points[i]-points[j]) for i,j in edges])
        for e,(i,j) in enumerate(edges):
            if i<n-1:b[e,i]=1
            if j<n-1:b[e,j]=-1
        v=b/delta[:,None]
        for _ in range(5):
            lam=np.exp(rng.uniform(-7,0,len(edges)));lam/=lam.sum();sigma=lam.copy()
            ell=2*log(n)
            for iteration in range(2000):
                gram=v.T@(sigma[:,None]*v)
                p=v@np.linalg.solve(gram,v.T*sigma[None,:])
                rows=np.abs(p).sum(axis=1)
                u=sigma*rows**2/(2*ell**2)
                phi=u+(1-u.sum())*lam
                if np.max(np.abs(phi-sigma))<1e-13:break
                sigma=(sigma+phi)/2
            else:raise AssertionError('Numerical iteration did not converge on a test example')
            maximum_iterations=max(maximum_iterations,iteration)
            q=np.sqrt(sigma)[:,None]*p/np.sqrt(sigma)[None,:]
            avg=np.sum(sigma*rows**2)
            rhs=np.linalg.norm(np.abs(q)@np.sqrt(sigma))**2
            assert abs(avg-rhs)<1e-10
            assert np.linalg.norm(q-q.T)<1e-10 and np.linalg.norm(q@q-q)<1e-10
            assert avg<=ell**2+1e-10 and np.min(sigma-lam/2)>-1e-12
            assert rows.max()<=2**.5*ell+1e-9
            worst_error=max(worst_error,float(np.max(np.abs(phi-sigma))))
            worst_ratio=max(worst_ratio,float(rows.max()/(2**.5*ell)))
    return {'complete_graph_examples':30,'max_fixed_point_residual':worst_error,
            'max_row_bound_ratio':worst_ratio,'max_iterations':maximum_iterations,
            'scope':'Finite numerical examples, not a proof that this iteration always converges.'}


def support_checks():
    cases=0
    for k in range(2,7):
        rows=np.array([[int(a==i) for a in range(k) for b in range(k)] for i in range(k)])
        cols=np.array([[int(b==j) for a in range(k) for b in range(k)] for j in range(k)])
        for p in [1.25,1.5,3.,4.,6.]:
            def defect(x,y):return float(np.sum(abs(x+y)**p+abs(x-y)**p-2*abs(x)**p-2*abs(y)**p))
            for i,j in product(range(k),repeat=2):
                assert abs(defect(rows[i],cols[j])-(2**p-4))<1e-9
                if i!=j:assert defect(rows[i],rows[j])==0 and defect(cols[i],cols[j])==0
            cases+=1
        assert all(np.sum((rows[i]!=0)&(cols[j]!=0))==1 for i,j in product(range(k),repeat=2))
        # At p=2, the defect cannot detect any incidence.
        assert all(np.sum((rows[i]+cols[j])**2+(rows[i]-cols[j])**2-2*rows[i]**2-2*cols[j]**2)==0 for i,j in product(range(k),repeat=2))
    return {'grid_and_exponent_examples':cases,'p_equals_two_negative_control':'detected',
            'scope':'Defect and incidence identities; the dimension conclusion uses the written strict-convexity argument.'}


def covering_constants():
    assert Q(2,64**2)/(1-Q(1,10**6))<Q(1,32**2)
    assert Q(33,32**2)<Q(1,4)
    assert Q(101,400)<Q(1,2)
    assert Q(1,2)-Q(3,200)==Q(97,200)
    assert Q(1600,97)<32
    return {'exact_rational_inequalities':5,'initial_doubling_bound':300*16**2,
            'scope':'Constants in covering estimates, not a sampling of the infinite metric space.'}


def jacobian_compatibility():
    count=0; noncommuting=0; worst_sos=0.0
    for n in range(2,6):
        for _ in range(15):
            vals={tuple(sorted(i)):random.randint(-3,3) for i in product(range(n),repeat=3)}
            xs=np.array([[[vals[tuple(sorted((r,i,j)))] for j in range(n)] for i in range(n)] for r in range(n)],dtype=np.int64)
            x=rng.integers(-3,4,size=n);a=np.einsum('r,rij->ij',x,xs)
            for r,s in product(range(n),repeat=2):
                assert np.array_equal(xs[r,:,s],xs[s,:,r])
                lhs=(xs[r]@a+a@xs[r])[:,s]-(xs[s]@a+a@xs[s])[:,r]
                rhs=(xs[r]@xs[s]-xs[s]@xs[r])@x
                assert np.array_equal(lhs,rhs)
                noncommuting+=int(np.any(xs[r]@xs[s]!=xs[s]@xs[r]))
            count+=1
        u,_=np.linalg.qr(rng.normal(size=(n,n))); signs=rng.choice([-1.,1.],size=n)
        xs=np.array([u@np.diag(signs*u[r])@u.T for r in range(n)])
        err=float(np.linalg.norm(sum(z@z for z in xs)-np.eye(n)))
        assert err<1e-12;worst_sos=max(worst_sos,err)
    assert noncommuting>0
    return {'exact_coefficient_examples':count,'noncommuting_pairs_detected':noncommuting,
            'signed_orthogonal_models':4,'max_sum_of_squares_error':worst_sos,
            'scope':'Coefficient identity and normal forms; not the global entropy inequality.'}


def determinant(a):
    a=[list(map(Q,row)) for row in a];result=Q(1)
    for k in range(len(a)):
        pivot=next(i for i in range(k,len(a)) if a[i][k])
        if pivot!=k:a[k],a[pivot]=a[pivot],a[k];result=-result
        v=a[k][k];result*=v
        for i in range(k+1,len(a)):
            factor=a[i][k]/v
            for j in range(k+1,len(a)):a[i][j]-=factor*a[k][j]
    return result


def cone_constants():
    for n in range(1,13):
        # Uniform standard simplex: E Xi=1/(n+1), E XiXj=(1+delta_ij)/((n+1)(n+2)).
        cov=[[Q(1+int(i==j),(n+1)*(n+2))-Q(1,(n+1)**2) for j in range(n)] for i in range(n)]
        det=determinant(cov)
        assert det==Q(1,(n+1)**(n+1)*(n+2)**n)
        volume=Q(1,factorial(n))
        assert det/volume**2==Q(factorial(n)**2,(n+1)**(n+1)*(n+2)**n)
        assert (n+1)**(n+1)*(n+2)**n*det==1
    return {'exact_simplex_dimensions':[1,12], 'interval_L_squared':'1/12',
            'scope':'Cone and simplex constants only; the entropy bound remains a separate input.'}


def main():
    checks={name:fn() for name,fn in [
        ('tensor_square',tensor_checks),('gaussian_operator',gaussian_operator_check),
        ('weighted_projection',projection_checks),('support_incidence',support_checks),
        ('covering_constants',covering_constants),('jacobian_compatibility',jacobian_compatibility),
        ('cone_constants',cone_constants)]}
    result={'status':'passed','seed':SEED,'numpy_version':np.__version__,'checks':checks,
            'limitation':'Finite checks and examples do not certify the source theorems or mathematical novelty.'}
    (Path(__file__).parent/'results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
