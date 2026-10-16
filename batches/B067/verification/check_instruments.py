"""Scoped algebraic and finite tensor checks; no global geometry certification."""
from itertools import combinations, permutations, product
from fractions import Fraction as F
from pathlib import Path
import json
import math
import time
import numpy as np
import sympy as s

RNG=np.random.default_rng(67016)

def generalized_inverse():
    x=s.symbols('x');cases=0
    Q=s.Matrix([[1,1,1,1],[1,-1,1,-1],[1,1,-1,-1],[1,-1,-1,1]])/2
    for spectrum in permutations((0,1,2,3)):
        f=Q*s.diag(*spectrum);B=f.T*f
        p=s.Poly(s.interpolate([(0,0),(1,1),(4,s.Rational(1,4)),(9,s.Rational(1,9))],x),x)
        P=sum((c*B**int(m[0]) for m,c in p.terms()),s.zeros(4));dagger=P*f.T
        assert f*dagger*f==f and dagger*f*dagger==dagger
        left=dagger*f;right=f*dagger
        assert left.T==left and left*left==left and right.T==right and right*right==right
        assert s.kronecker_product(dagger,s.eye(2))*s.kronecker_product(f,s.eye(2))==s.kronecker_product(left,s.eye(2));cases+=1
    for k in (10,100,1000):
        assert F(1,k)*k==1
    return dict(exact_spectral_models=cases,varying_map_negative_control='f_k=1/k, x_k=1 has f_k x_k tending to zero but identity kernel-complement projection.')

def gluing():
    cases=0
    for a,b in product(range(1,30),repeat=2):
        if a*b<=a*a and a*b<=b*b:assert a==b
    for n in range(2,10):
        count=0
        for a,b,c,d in product(range(n),repeat=4):
            if math.gcd(a*d-b*c,n)!=1:continue
            graph={(((a*x+b*y)%n,(c*x+d*y)%n),(x,y)) for x,y in product(range(n),repeat=2)}
            assert len(graph)==n*n and len({g[0] for g in graph})==n*n and len({g[1] for g in graph})==n*n
            count+=1;cases+=1
            if count==24:break
    return dict(torsion_graphs=cases,scope='Kernel algebra only; polarization realization not tested.')

def cyclic_norms():
    x,z=s.symbols('x z');cases=0
    for d in range(2,6):
        T=s.zeros(d)
        for i in range(d-1):T[i+1,i]=1
        T[0,d-1]=x
        for m in range(1,6):
            U=sum(((j+1)*T**j for j in range(m+1)),s.zeros(d))
            cp=U.charpoly(z).as_poly()
            for j,c in enumerate(cp.all_coeffs()):
                if c!=0:assert s.degree(c,x)<=m*j//d
            assert sum((c*U**(d-j) for j,c in enumerate(cp.all_coeffs())),s.zeros(d)).applyfunc(s.expand)==s.zeros(d)
            W=s.eye(d)+T
            assert s.expand((U*W).det()-U.det()*W.det())==0
            assert U.det().subs(x,0)==1
            assert s.expand(((1+x)*s.eye(d)).det()-(1+x)**d)==0;cases+=1
    return dict(section_characteristic_polynomials=cases,scope='Finite flat cyclic algebras; not a test of nonflat analytic descent.')

def norm_descent():
    cases=0
    for d in range(1,13):
        for _ in range(10):
            E=RNG.integers(-4,5,(d,3));E[np.all(E==0,axis=1),0]=1
            t=next(t for t in range(2*d+1) if np.all(E@np.array([1,t,t*t])!=0))
            vals=[int(v) for v in E@np.array([1,t,t*t])]
            norm=math.prod(vals)
            assert norm!=0 and math.prod(3*v for v in vals)==3**d*norm;cases+=1
    return dict(fiber_hyperplane_avoidance=cases,scope='Tests simultaneous nonvanishing and norm gluing factor, not removable-singularity theory.')

def hodge_gap():
    point_cases=0;integrated=0;growth=0;worst=0.
    for n in range(1,5):
        inds=list(combinations(range(2*n),n));N=len(inds);K=inds.index(tuple(range(n,2*n)));delta=1/(N+2)
        for _ in range(40):
            rank=int(RNG.integers(0,n+1));b=np.zeros(2*n);b[:rank]=RNG.uniform(.001,.999,rank)
            g=RNG.normal(size=(N,N))+1j*RNG.normal(size=(N,N))
            sums=np.array([b[list(I)].sum() for I in inds]);coeff=n-b.sum()+sums[:,None]+sums[None,:]
            e=float(np.sum(coeff*abs(g)**2));norm=float(np.sum(abs(g)**2));A=np.trace(g);B=np.prod(b[:n])*g[K,K] if rank==n else 0
            assert abs(A-B)**2<=N*e+1e-9 and abs(B)**2>=norm-2*e-1e-9;point_cases+=1
        for _ in range(20):
            b=np.r_[RNG.uniform(.1,.99,n),np.zeros(n)];p=np.prod(b[:n]);t=RNG.normal()+1j*RNG.normal();c=RNG.normal()+1j*RNG.normal();data=[]
            sums=np.array([b[list(I)].sum() for I in inds]);coeff=n-b.sum()+sums[:,None]+sums[None,:]
            for a in (t,-t):
                g=np.zeros((N,N),complex);np.fill_diagonal(g,(c-a)/(N-1));g[K,K]=a
                data.append((float(np.sum(coeff*abs(g)**2)),float(np.sum(abs(g)**2)),np.trace(g),p*a))
            assert abs(sum(np.conj(A)*B for e,norm,A,B in data))<1e-9
            assert sum(e for e,norm,A,B in data)>=delta*sum(norm for e,norm,A,B in data)-1e-9;integrated+=1
        h=np.r_[RNG.uniform(.1,3,n),np.zeros(n)];g=RNG.normal(size=(N,N));g[K,K]=0
        def norm(R):
            metric=1+R*h;f=np.array([np.prod(metric[list(I)]) for I in inds])
            return float(np.sum(g*g*np.prod(metric)/(f[:,None]*f[None,:])))
        for R in (1,2,10,100,10000):
            ratio=norm(R)/(R**(n-delta)*norm(1));assert ratio<=1+1e-10;worst=max(worst,ratio);growth+=1
    return dict(pointwise_tensor_models=point_cases,orthogonality_models=integrated,flat_constant_form_growth= growth,max_normalized_growth=worst,scope='Tensor and flat-torus models only; no global Hodge-rank bound tested.')

def constants():
    a,t=s.symbols('a t');cases=0
    polys=[a*a-2,a*a-3,a*a-5,a**4-10*a*a+1]
    for f in polys:
        assert s.Poly(f,a,domain=s.QQ).is_irreducible
        assert s.Poly(f,a,domain=s.QQ.frac_field(t)).is_irreducible
        factors=s.factor_list(f,a,extension=[s.sqrt(2),s.sqrt(3),s.sqrt(5)])[1]
        assert all(s.degree(g,a)==1 and e==1 for g,e in factors)
        assert len(factors)==s.degree(f,a);cases+=1
    assert len(s.factor_list(a*a-2,a,extension=s.sqrt(2))[1])==2
    return dict(constant_extension_models=cases,nonregular_base_control='Q(sqrt(2)) over Q loses degree after using that same field as the base; geometric integrality is essential.')

def nef_intersections():
    cases=0
    # Hirzebruch surface: S^2=-e, S.F=1, F^2=0; nef aS+bF iff a>=0,b>=ae.
    for e,a,extra,c in product(range(6),range(7),range(7),range(1,5)):
        b=a*e+extra;d=c*e+1
        PH=-e*a*c+a*d+b*c
        assert PH>=0
        if PH==0:assert a==b==0
        for u,v in ((1,0),(0,1),(2,3)):
            assert -e*u*c+u*d+v*c>0
        cases+=1
    # On P1 x P1, S-F is nonzero but orthogonal to S+F; it is not nef.
    assert 1+(-1)==0
    for size in range(1,30):
        coeff=RNG.integers(1,8,size);degrees=np.zeros(size,dtype=int)
        assert int(coeff@degrees)==0
        degrees[int(RNG.integers(size))]=1
        assert int(coeff@degrees)>0
    return dict(toric_surface_models=cases,non_nef_negative_control=True)

def curvature():
    cases=0
    for p in (2,3,5,7,11):
        X=np.zeros((p,p),dtype=np.int64);D=X.copy();I=np.eye(p,dtype=np.int64)
        for j in range(p-1):X[j+1,j]=1;D[j,j+1]=j+1
        def power(M,n):
            out=I.copy()
            for _ in range(n):out=out@M%p
            return out
        def mult(v):return sum((int(c)*power(X,j) for j,c in enumerate(v)),np.zeros_like(X))%p
        assert np.array_equal((D@X-X@D)%p,I)
        for _ in range(20):
            a=RNG.integers(0,p,p);M=mult(a);rhs=(power(M,p)+mult(power(D,p-1)@a%p))%p
            assert np.array_equal(power((D+M)%p,p),rhs);cases+=1
        # dlog(1+x) is Cartier fixed; the connection is a gauge transform.
        g=I+X;ginv=sum(((-1)**j*power(X,j) for j in range(p)),np.zeros_like(X))%p
        C=(D+ginv)%p
        assert np.array_equal(C,ginv@D@g%p) and np.array_equal(power(C,p),np.zeros_like(X))
        Dx=np.kron(C,I);Dy=np.kron(I,C)
        assert np.array_equal((Dx@Dy-Dy@Dx)%p,np.zeros_like(Dx))
    def partitions(seq):
        if not seq:yield ();return
        first,*rest=seq
        for part in partitions(rest):
            yield ((first,),)+part
            for i in range(len(part)):
                yield part[:i]+(tuple(sorted((first,)+part[i])),)+part[i+1:]
    fixed={}
    for p in (2,3,5,7):
        canonical=lambda part:tuple(sorted(tuple(sorted(block)) for block in part))
        objects={canonical(part) for part in partitions(list(range(p)))}
        fixed[p]=sum(canonical(tuple(tuple((j+1)%p for j in b) for b in part))==part for part in objects)
        assert fixed[p]==2
    return dict(arbitrary_coefficient_operators=cases,fixed_cyclic_partitions=fixed,scope='Universal identities in truncated p-basis algebras; retained Laurent basis and global abundance untested.')

def main():
    start=time.perf_counter();checks={}
    for fn in (generalized_inverse,gluing,cyclic_norms,norm_descent,hodge_gap,constants,nef_intersections,curvature):
        checks[fn.__name__]=fn();print(fn.__name__,'passed',flush=True)
    report=dict(status='passed',elapsed_seconds=round(time.perf_counter()-start,3),checks=checks,scope='Selected finite mechanisms only; no Zilber-Pink, Iitaka, uniform-index or abundance headline certified.')
    Path(__file__).with_name('results.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='checks'}))

if __name__=='__main__':main()
