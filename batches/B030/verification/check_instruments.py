"""Finite algebraic and analytic checks; not certificates of the source group claims."""
from fractions import Fraction as F
from itertools import product, permutations
from pathlib import Path
import json
import numpy as np
import sympy as S
from scipy.optimize import minimize, linprog

rng=np.random.default_rng(30016)

def rankmod(A,p):
    A=np.array(A,dtype=np.int64)%p;r=0
    for c in range(A.shape[1]):
        piv=next((i for i in range(r,len(A)) if A[i,c]),None)
        if piv is None:continue
        A[[r,piv]]=A[[piv,r]];A[r]=A[r]*pow(int(A[r,c]),-1,p)%p
        for i in range(len(A)):
            if i!=r:A[i]=(A[i]-A[i,c]*A[r])%p
        r+=1
        if r==len(A):break
    return r

def crossing_duality():
    count=0;worst=0.
    for h,w in ((2,2),(2,3),(3,3)):
        paths=set()
        def walk(v,seen):
            if v%w==w-1:
                paths.add(tuple(int(i in seen) for i in range(h*w)));return
            y,x=divmod(v,w)
            for yy,xx in ((y+1,x),(y-1,x),(y,x+1),(y,x-1)):
                z=yy*w+xx
                if 0<=yy<h and 0<=xx<w and z not in seen:walk(z,seen|{z})
        for y in range(h):walk(y*w,{y*w})
        V=np.array(sorted(paths),float)
        # Solve the density problem, then independently require its normalized
        # optimizer to have a convex decomposition in the crossing vectors.
        for k in range(12):
            keep=np.arange(len(V)) if k==0 else rng.choice(len(V),min(len(V),k+1),replace=False)
            A=V[keep];n=h*w
            sol=minimize(lambda x:x@x,np.ones(n),jac=lambda x:2*x,
                         constraints={'type':'ineq','fun':lambda x:A@x-1,'jac':lambda x:A},
                         bounds=[(0,None)]*n,method='SLSQP',options={'ftol':1e-12,'maxiter':500})
            assert sol.success
            active=A[np.abs(A@sol.x-1)<1e-5]
            rho=np.linalg.lstsq(active,np.ones(len(active)),rcond=None)[0]
            assert min(A@rho)>=1-1e-8 and min(rho)>=-1e-8
            E=rho@rho;P=rho/E
            fit=linprog(np.zeros(len(A)),A_eq=np.vstack((A.T,np.ones(len(A)))),
                        b_eq=np.r_[P,1],bounds=(0,None),method='highs',options={'primal_feasibility_tolerance':1e-6})
            assert fit.success
            err=max(abs(P@P-1/E),np.max(abs(A.T@fit.x-P)))
            worst=max(worst,float(err));assert err<1e-6
            for x in range(w):
                u=np.array([int(i%w==x) for i in range(n)])
                assert min(A@u)>=1 and u@P>=1-1e-8
            count+=1
    return dict(primal_and_convex_hull_models=count,maximum_residual=worst,scope='Finite crossing families and column blockers, not the planar limiting construction.')

def tree_energy():
    checks=0
    for trial in range(40):
        prob=np.ones(1);badcount=np.zeros(1);past=0.;a=1.08;D=2.;tau=.12;b=10*tau
        for n in range(1,10):
            bad=rng.integers(0,2,len(prob));past+=prob@bad
            split=rng.uniform(.1,.9,len(prob))
            badcount=np.repeat(badcount+bad,2)
            prob=np.column_stack((prob*split,prob*(1-split))).ravel()
            assert abs(prob.sum()-1)<1e-12 and abs(prob@badcount-past)<1e-12
            E=prob@(a**(D*((b+tau)*badcount-tau*n)))
            upper=tau/(b+tau)+np.log(E)/np.log(a)/(D*(b+tau)*n)
            assert past/n<=upper+1e-12;checks+=1
    return dict(finite_tree_levels=checks,scope='Conservation and Jensen bound; does not construct the source infinite probability flow.')

def localized_degree_algebra():
    roots=0;normal=0
    for m in (1,2,3):
        accepted=0
        while accepted<15:
            B=rng.integers(-2,3,(m,m));det=int(S.Matrix(B).det());d=abs(det)
            if not 0<d<=6:continue
            count=sum(not np.any(B@np.array(k)%d) for k in product(range(d),repeat=m))
            assert count==d;accepted+=1;roots+=1
        for _ in range(20):
            A=S.Matrix(rng.integers(-3,4,(m,m)));B=S.Matrix(rng.integers(-3,4,(m,m)))
            real=A.row_join(-B).col_join(B.row_join(A));z=(A+S.I*B).det()
            assert S.expand(real.det()-z*S.conjugate(z))==0;normal+=1
    return dict(torus_fiber_counts=roots,complex_normal_determinants=normal,
                scope='Checks algebraic inputs only; equivariant perturbations and local mapping degree are not computed.')

def qmul(a,b):return np.r_[a[0]*b[0]-a[1:]@b[1:],a[0]*b[1:]+b[0]*a[1:]+np.cross(a[1:],b[1:])]
def qinv(a):return a*np.array([1,-1,-1,-1])
def quat(v):return np.r_[1-v@v,2*v]/(1+v@v)

def quadratic_relators():
    checks=0;largest=0.
    for _ in range(240):
        labels=[quat(rng.normal(size=3)*.002) for j in range(4)]
        terms=[(0,1)]+[(j,s) for j in range(1,4) for s in (1,-1)]
        rng.shuffle(terms);h=max(np.linalg.norm(a-np.array([1,0,0,0])) for a in labels)
        out=np.array([1.,0,0,0]);kappa=0.
        for j,s in terms:
            u=quat(rng.normal(size=3)*.003);kappa=max(kappa,np.linalg.norm(u-np.array([1,0,0,0])))
            a=labels[j] if s==1 else qinv(labels[j]);out=qmul(out,qmul(qmul(u,a),qinv(u)))
        n=len(terms);bound=2*n*kappa*h+n*(n-1)*h*h;error=np.linalg.norm(out-labels[0])
        assert error<=bound+1e-13;largest=max(largest,error/bound);checks+=1
    # An uncancelled near-identity factor has first-order, not quadratic, size.
    a=quat(np.array([1e-6,0,0]));h=np.linalg.norm(a-np.array([1,0,0,0]));assert h>1000*h*h
    return dict(quaternion_count_cancellation_models=checks,maximum_error_over_bound=largest,scope='Exact signed multiplicities imposed as inputs; no cellular boundary basis or finite quotient constructed.')

def rank_certificates():
    cases=0;losses=0;blocks=0
    for n in range(2,11):
        for _ in range(8):
            A=rng.integers(-1,2,(n,n));r=max(1,int(np.max(np.sum(A*A,axis=1))));q=int(S.nextprime(r))
            d=int(S.Matrix(A).rank());e=rankmod(A,q);assert 2*e>=d;cases+=1;losses+=int(e<d)
    for q in (7,11):
        A=2*np.eye(q,dtype=int)-np.roll(np.eye(q,dtype=int),1,axis=1)-np.roll(np.eye(q,dtype=int),-1,axis=1)
        d=int(S.Matrix(A).rank());e=rankmod(A,q);assert d==q-1 and e==q-2 and 2*e>=d;losses+=1;cases+=1
    for r,D in ((2,3),(2,5),(3,5),(3,7),(4,5),(4,7)):
        Y=np.block([[np.roll(np.eye(D,dtype=int),u*v,axis=1) for v in range(r)] for u in range(r)])
        C=Y@Y.T;assert np.trace(C)==r*r*D and np.trace(C@C)==(2*r**3-r*r)*D
        assert 4*rankmod(Y,D)>=r*D;blocks+=1
    return dict(integer_matrix_models=cases,observed_rank_drops=losses,regular_block_models=blocks,
                scope='Block tests deliberately use characteristic q=D dividing the finite group order.')

def line_certificates():
    count=0;bad_control=False
    for q,h in ((7,1),(7,2),(11,2)):
        marks=list(product((0,1),repeat=h));N=len(marks);points=list(product(range(q),repeat=h))
        def H(z):
            f=np.array([np.prod([z[k] if a[k] else 1-z[k] for k in range(h)],dtype=np.int64)%q for a in marks])
            return np.outer(f,f)%q
        for trial in range(20):
            Y=rng.integers(0,q,(N,2,2));Z={z:np.zeros((2,2),dtype=np.int64) for z in points};bad={z:A.copy() for z,A in Z.items()}
            for i,a in enumerate(marks):
                v=np.zeros(h,dtype=int);v[0]=1
                if h==2:v[1]=trial%q
                line=[tuple((np.array(a)+t*v)%q) for t in range(q)]
                assert np.all(sum((H(z) for z in line),np.zeros((N,N),dtype=np.int64))%q==0)
                for z in line:
                    if z!=a:Z[z]=(Z[z]+Y[i])%q
                    if z not in marks:bad[z]=(bad[z]+Y[i])%q
            direct=np.zeros((2*N,2*N),dtype=np.int64)
            for i in range(N):direct[2*i:2*i+2,2*i:2*i+2]=-Y[i]
            lhs=sum((np.kron(H(z),Z[z]) for z in points),np.zeros_like(direct))%q
            assert np.all((lhs-direct)%q==0)
            assert rankmod(direct,q)<=sum(rankmod(A,q) for A in Z.values())
            wrong=sum((np.kron(H(z),bad[z]) for z in points),np.zeros_like(direct))%q
            bad_control=bad_control or np.any((wrong-direct)%q);count+=1
    assert bad_control
    return dict(exact_finite_field_tensor_models=count,omit_all_marked_points_control='fails as expected',scope='Interpolation certificate only; no triangle-complex presentation verified.')

def density_speed():
    x=S.symbols('x');g=(1-x*x)**3;norm=S.integrate(g*g,(x,-1,1))
    A=S.integrate(S.diff(g,x)**2,(x,-1,1))/norm
    C=S.integrate(x*x*g*g,(x,-1,1))/norm
    B=S.integrate((x*S.diff(g,x)+g/2)**2,(x,-1,1))/norm
    af,bf,cf=map(float,(A,B,C));K=max(af,bf,af*cf+.25)
    nodes,weights=np.polynomial.legendre.leggauss(8);checks=0;worst=0.
    for d in (1,2,3,4):
        mesh=list(product(range(8),repeat=d));X=np.array([[nodes[j] for j in z] for z in mesh])
        W=np.array([np.prod([weights[j] for j in z]) for z in mesh])
        density=np.prod((1-X*X)**6,axis=1)/float(norm)**d;score=-6*X/(1-X*X)
        for _ in range(12):
            L=rng.normal(size=(d,d));v=rng.normal(size=d)
            value=np.sum((X@L.T+v)*score,axis=1)+np.trace(L)/2
            direct=np.sum(W*density*value**2)
            diag=np.diag(L);off=L-np.diag(diag)
            formula=af*(v@v)+bf*(diag@diag)+af*cf*np.sum(off*off)+.5*sum(L[i,j]*L[j,i] for i in range(d) for j in range(i+1,d))
            worst=max(worst,abs(direct-formula));assert abs(direct-formula)<1e-8
            assert formula<=K*(np.sum(L*L)+v@v)+1e-10;checks+=1
    return dict(product_quadrature_models=checks,maximum_identity_error=worst,moments={'A':str(A),'B':str(B),'C':str(C)},
                scope='Polynomial compact density has C2 square root, adequate for these integrals but not the source C-infinity assumption. Does not establish the partition coupling.')

def reiter_folner():
    G=list(permutations(range(3)));identity=(0,1,2);H=[identity,(1,0,2)]
    mul=lambda a,b:tuple(a[b[i]] for i in range(3));pi={}
    for t in G:
        if t not in pi:
            for h in H:pi[mul(h,t)]=h
    for h,x in product(H,G):assert pi[mul(h,x)]==mul(h,pi[x])
    tests=0
    for _ in range(60):
        nums=rng.integers(1,50,len(G));p={g:F(int(n),int(sum(nums))) for g,n in zip(G,nums)}
        for k in H:
            left=sum(abs(p[mul(k,g)]-p[g]) for g in G)
            ph={h:sum(p[g] for g in G if pi[g]==h) for h in H}
            assert sum(abs(ph[mul(k,h)]-ph[h]) for h in H)<=left
        tests+=1
    layers=0
    for n in range(3,33):
        nums=rng.integers(1,100,n);q={i:F(int(v),int(sum(nums))) for i,v in enumerate(nums)};K=(-2,-1,1,2)
        error=sum(sum(abs(q.get(x-k,0)-q.get(x,0)) for x in range(-2,n+2)) for k in K)
        mass=F(0);boundary=F(0);best=None;previous=F(0)
        for height in sorted(set(q.values())):
            A={x for x,v in q.items() if v>=height};b=sum(len({x+k for x in A}^A) for k in K)
            mass+=(height-previous)*len(A);boundary+=(height-previous)*b;previous=height
            ratio=F(b,len(A));best=ratio if best is None else min(best,ratio)
        assert mass==1 and boundary==error and best<=error;layers+=1
    return dict(non_normal_subgroup_pushforward_models=tests,exact_layer_cake_models=layers,
                scope='Finite equivariance and layer-cake identities, not an independent amenability proof.')

if __name__=='__main__':
    groups={}
    for fn in (crossing_duality,tree_energy,localized_degree_algebra,quadratic_relators,rank_certificates,line_certificates,density_speed,reiter_folner):
        groups[fn.__name__]=fn();print(fn.__name__,'passed',flush=True)
    result=dict(batch='B030',status='passed',check_groups=groups,limitations='Selected finite mechanisms only. No Cannon, Eilenberg-Ganea, non-residual-finiteness or simple amenability claim certified; no Lean build.')
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
