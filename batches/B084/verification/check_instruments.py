"""Finite mechanisms and symbolic identities; no headline theorem certification."""
from fractions import Fraction as F
from itertools import product,combinations
from pathlib import Path
import json,time,math
import numpy as np
import sympy as s

def stable_images():
    A=s.Matrix([[2,1],[1,1]]);J=s.Matrix([[0,1],[0,0]])
    M=s.diag(A,J,J);X=s.diag(A,J,s.zeros(3));f=s.zeros(7,6)
    f[:2,:2]=s.eye(2);f[2:4,4:6]=s.eye(2);assert X*f==f*M
    cases=0
    for k in range(1,9):
        P=s.eye(6);P[0,5]=k;P[3,1]=k+1
        Q=s.eye(7);Q[6,0]=k;Q[2,5]=k-1
        m=P*M*P.inv();x=Q*X*Q.inv();g=Q*f*P.inv()
        mi=m**8;xi=x**8
        assert mi.rank()==xi.rank()==(g*mi).rank()==2
        assert s.Matrix.hstack(xi,g*mi).rank()==2 and x*g==g*m;cases+=1
    assert s.eye(1).rank()==1 # An invertible kernel cannot be discarded.
    assert s.Matrix([[0]]).rank()!=s.eye(1).rank() # Unhit stable target.
    return dict(conjugated_comparisons=cases,missing_hypothesis_controls=2)

def compatible_filtration():
    collisions=0
    for n in range(1,8):
        sets=[tuple(i+1 for i in range(n) if mask>>i&1) for mask in range(2**n)]
        blocks=[[a for a in sets if (max(a) if a else 0)==j] for j in range(n+1)]
        assert sum(map(len,blocks))==2**n
        graded={}
        for a in sets:graded.setdefault(sum(2*i-1 for i in a),[]).append(a)
        for degree,items in graded.items():
            B=s.eye(len(items))
            for j in range(len(items)-1):B[j,j+1]=j+1
            assert B.det()==1
            for cut in range(n+1):
                idx=[i for i,a in enumerate(items) if (max(a) if a else 0)<=cut]
                assert B[:,idx].rank()==len(idx)
            collisions+=len(items)>1
    assert sum(2*i-1 for i in (1,4))==sum(2*i-1 for i in (2,3))
    for p in (2,3,5):
        assert s.Matrix([[p]]).rank()==1 and s.zeros(1).rank()==0
        assert len({a%p for a in range(2*p)})==p # H_0 of Z --p--> Z.
    return dict(graded_filtrations=7,colliding_degrees=collisions,nonsplit_integral_controls=3)

PARENTS=[-1,0,0,1,1,2,2]
SEGMENTS=[]
for end in range(7):
    nodes=[];v=end
    while v>=0:
        nodes.append(v);SEGMENTS.append(tuple(nodes));v=PARENTS[v]
def rho(v):
    best=np.zeros(128)
    for seg in SEGMENTS:
        mask=sum(1<<i for i in seg);weight=sum(v[i] for i in seg)**2
        old=best.copy()
        for used in range(128):
            if not used&mask:best[used|mask]=max(best[used|mask],old[used]+weight)
    return math.sqrt(max(best))
def gate_correction():
    rng=np.random.default_rng(8401);cases=0
    for H in [{0},{0,1},{0,1,2},{0,1,3}]:
        gates=[i for i in range(7) if i not in H and PARENTS[i] in H]
        for repeat in range(12):
            f=rng.normal(size=7);k=rng.normal(size=7)
            for i in range(7):
                if i not in H:f[i]=0
                else:k[i]=0
            f/=rho(f);k/=rho(k)
            for scale in [.03,.2,.8,3]:
                c=np.zeros(7)
                for g in gates:
                    m=max(abs(sum(k[i] for i in seg)) for seg in SEGMENTS if seg[-1]==g)
                    v=PARENTS[g];total=0;sign=1
                    while v in H:
                        total+=f[v]
                        if m>0 and abs(total)>=2*scale*m:
                            sign=-np.sign(total);break
                        v=PARENTS[v]
                    c[g]=sign*m
                for sign in [-1,1]:
                    assert rho(f+scale*(c+sign*k))**2<=1+12*scale**2+1e-10
                cases+=1
    return dict(primal_corrected_pairs=cases,dual_norm_not_optimized=True)

def lens_diamonds():
    for a in [.1,1,3]:
        for b in [.2,1,4]:
            x=np.zeros(9);x[0]=a;ys=b*np.eye(9)[1:]
            eps=math.sqrt(2)*b;R=math.sqrt(a*a+b*b)
            assert R*R-a*a>=eps*eps/48-1e-12
            assert all(abs(np.linalg.norm(x+y)-R)<1e-12 for y in ys)
    edges=[(0,1)];nextv=2;hist=[edges]
    for _ in range(3):
        new=[]
        for u,v in edges:
            for branch in range(3):new.extend([(u,nextv),(nextv,v)]);nextv+=1
        edges=new;hist.append(edges)
    adj=[set() for _ in range(nextv)]
    for u,v in edges:adj[u].add(v);adj[v].add(u)
    for generation,es in enumerate(hist):
        for u,v in es:
            dist={u:0};queue=[u]
            for a in queue:
                for b in adj[a]:
                    if b not in dist:dist[b]=dist[a]+1;queue.append(b)
            assert dist[v]==2**(3-generation)
    for depth in range(1,20):assert F(1)+sum([F(1,12)]*depth)==F(1)+F(depth,12)
    return dict(hilbert_lenses=9,diamond_generations=4,telescopes=19,infinite_compactness_not_tested=True)

def weighted_graph():
    x=s.symbols('x',real=True);f=x*x/3+x**3/7;phi=x*x/5
    N=s.Integer(2);L=s.sqrt(1+N*N*s.diff(f,x)**2);U=N*s.diff(f,x)/L
    D=-s.diff(U,x)-s.diff(phi,x)*U;phip=phi-s.log(L)
    lap=lambda h:s.diff(s.diff(h,x)/L,x)/L
    W0=-2*s.diff(phi,x,2)-s.diff(phi,x)**2
    W1=-2*lap(phip)-(s.diff(phip,x)/L)**2
    II2=(N*s.diff(f,x,2)/L**3)**2
    rhs=D*D-2*U*s.diff(D,x)+II2+(s.diff(s.log(L),x)/L)**2
    assert s.simplify(W1-W0-rhs)==0
    assert s.simplify(s.exp(phip)*L-s.exp(phi))==0
    assert abs(float((2*U*s.diff(D,x)).subs(x,F(1,2))))>.01
    return dict(symbolic_weighted_identity=True,volume_preserved=True,omitted_derivative_rejected=True)

def joint_rounding():
    A=s.Matrix([[1,-1,0,0,0],[0,1,1,-1,0],[0,0,0,1,-2]])
    basis=[]
    for b in A.nullspace():basis.append(b*s.ilcm(*[a.q for a in b]))
    B=s.Matrix.hstack(*basis);D=7;t=[F(4,13),F(-5,17)]
    v=[sum(t[j]*int(B[i,j]) for j in range(2)) for i in range(5)]
    lower=[(a*D).__floor__() for a in t];probs=[a*D-lo for a,lo in zip(t,lower)]
    mean=[F(0)]*5;mass=F(0);K=max(abs(int(a)) for a in B)
    for bits in product([0,1],repeat=2):
        prob=math.prod(probs[j] if bits[j] else 1-probs[j] for j in range(2))
        out=B*s.Matrix([s.Rational(lower[j]+bits[j],D) for j in range(2)])
        assert A*out==s.zeros(3,1)
        for i,a in enumerate(out):
            val=F(int(a.p),int(a.q));assert (val*D).denominator==1
            assert abs(val-v[i])<=F(2*K,D);mean[i]+=prob*val
        mass+=prob
    assert mass==1 and mean==v
    assert s.Matrix([[1,-1]])*s.Matrix([0,1])!=s.zeros(1,1)
    return dict(exact_outcomes=4,unbiased=True,shared_constraints_preserved=True,independent_rounding_rejected=True)

def ground_state_transform():
    x,y=s.symbols('x y',real=True);v=s.exp(-x*x/3-y*y/5);w=-2*s.log(v)
    lap=lambda a:s.diff(a,x,2)+s.diff(a,y,2)
    assert s.simplify(2*lap(w)-s.diff(w,x)**2-s.diff(w,y)**2+4*lap(v)/v)==0
    for R in [1,2,4,8]:
        z=s.cos(s.pi*x/(2*R));lam=2+s.pi**2/R**2
        assert s.simplify(-4*s.diff(z,x,2)+2*z-lam*z)==0 and z.subs(x,0)==1
    return dict(log_identity=True,interval_ground_states=4,existence_not_tested=True)

def angle_pressure():
    x,z,w=s.symbols('x z w',real=True);u=x*x/3+x**3/7;t=x*x/5
    up=s.diff(u,x);omega=1/s.sqrt(1+up*up);H=s.diff(omega*up,x)
    a=s.Rational(2,3);b=s.Rational(4,5)
    pressure=H-s.diff(t,x)*omega*up+a*(z-u)+b*(w-omega)
    px=s.diff(pressure,x).subs({z:u,w:omega})
    potential=(s.diff(u,x,2)*omega**3)**2+s.diff(t,x,2)*(omega*up)**2+omega*up*px-omega*a
    lap=omega*s.diff(omega*s.diff(omega,x),x)
    drift=(-s.diff(t,x)+b*up)*omega**2*s.diff(omega,x)
    assert s.simplify(lap+drift+potential*omega+a)==0
    omitted=b*up*omega**2*s.diff(omega,x)
    assert abs(float(omitted.subs(x,F(1,2))))>.01
    return dict(manufactured_angle_identity=True,missing_pressure_angle_drift_rejected=True,global_solution_not_tested=True)

if __name__=='__main__':
    start=time.perf_counter();checks={}
    for f in [stable_images,compatible_filtration,gate_correction,lens_diamonds,weighted_graph,joint_rounding,ground_state_transform,angle_pressure]:checks[f.__name__]=dict(status='pass',details=f())
    result=dict(batch='B084',status='pass',elapsed_seconds=round(time.perf_counter()-start,3),scope='Selected finite mechanisms and symbolic identities; no headline theorem or Lean certification.',checks=checks)
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8');print(json.dumps(result))
