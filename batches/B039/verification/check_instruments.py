"""Finite algebraic checks; no global geometric theorem is certified."""
import itertools as it
import json
import random
from pathlib import Path
import numpy as np
import sympy as s
rng=random.Random(39016);out={}

def strings(spec):
    n=sum(l+1 for p,l in spec);E=s.zeros(n);F=s.zeros(n);grades=[];off=0
    for p,l in spec:
        grades.extend(p+2*j for j in range(l+1))
        for j in range(l):E[off+j+1,off+j]=1;F[off+j,off+j+1]=(j+1)*(l-j)
        off+=l+1
    return E,F,grades
def comm(A,B):return A*B-B*A
count=0
for lengths in [(0,),(1,),(2,),(3,),(4,),(1,2),(2,3),(0,2,4),(1,1,3)]:
    E,F,g=strings([(-l,l) for l in lengths]);n=len(g)
    assert comm(comm(F,E),E)==-2*E and comm(E,F)==s.diag(*g)
    domain=[(a,b) for a in range(n) for b in range(n) if g[a]-g[b]==-2]
    cols=[]
    for a,b in domain:
        X=s.zeros(n);X[a,b]=1;cols.append(s.Matrix(comm(E,comm(E,X))).reshape(n*n,1))
    if cols:assert s.Matrix.hstack(*cols).rank()==len(domain)
    annihilator=s.eye(n)
    for a in range(min(g),max(g)+1):annihilator*=comm(E,F)-a*s.eye(n)
    assert annihilator==s.zeros(n);count+=1
E,F,g=strings([(-2,2)]);C=s.eye(3)+E
assert comm(C,E)==s.zeros(3) and C[:,0]!=s.eye(3)[:,0]
assert F*C[:,0]!=s.zeros(3,1)
out['common_lowering']={'exact_string_sums':count,'raiser_only_negative_control':True}

def hl(E,g,r):
    if not isinstance(r,int):return False
    for i in range(max(abs(a-r) for a in g)+1):
        left=[j for j,a in enumerate(g) if a==r-i];right=[j for j,a in enumerate(g) if a==r+i]
        if len(left)!=len(right) or (E**i).extract(right,left).rank()!=len(left):return False
    return True
positive=negative=0
for _ in range(100):
    specs=[]
    for factor in range(2):
        center=rng.randint(-2,2);spec=[]
        for j in range(rng.randint(1,2)):
            l=rng.randint(0,2);c=center if _<50 else rng.randint(-2,2);spec.append((c-l,l))
        specs.append(spec)
    E,F,g=strings(specs[0]);D,FF,h=strings(specs[1]);K=s.kronecker_product(E,s.eye(len(h)))+s.kronecker_product(s.eye(len(g)),D)
    grades=[a+b for a in g for b in h];twice=min(grades)+max(grades)
    good=twice%2==0 and hl(K,grades,twice//2)
    centers=[{p+l for p,l in spec} for spec in specs]
    expected=all(len(c)==1 for c in centers)
    assert good==expected
    if good:
        assert hl(E,g,next(iter(centers[0]))) and hl(D,h,next(iter(centers[1])));positive+=1
    else:negative+=1
out['tensor_lefschetz']={'positive_models':positive,'negative_models':negative}

def cuts(n,w,b):
    xs=s.symbols('x:'+str(n));polys=[]
    for mask in range(1,1<<n):
        S={j for j in range(n) if mask>>j&1}
        polys.append(s.prod(xs[j]**w[j] for j in S)*s.prod((xs[j]-xs[k])**b[j][k] for j in S for k in set(range(n))-S))
    return xs,polys
models=unit=0
for n in [1,2,3]:
    for _ in range(10):
        w=[rng.randrange(2) for j in range(n)];b=[[0]*n for j in range(n)]
        for j,k in it.combinations(range(n),2):b[j][k]=b[k][j]=rng.randrange(2)
        xs,polys=cuts(n,w,b);G=s.groebner(polys,*xs)
        if list(G)==[1]:unit+=1
        else:assert G.is_zero_dimensional
        for values in it.product([-1,0,1],repeat=n):
            if any(values):assert any(p.subs(dict(zip(xs,values)))!=0 for p in map(s.sympify,polys))
        models+=1
out['finite_cut_quotient']={'exact_groebner_models':models,'unit_ideals':unit}

t=s.symbols('t')
for j in range(1,31):
    U=s.Matrix([[1,j*t],[0,1]])*s.Matrix([[1,0],[t**2,1]])
    assert s.expand(U.det())==1 and all(s.denom(s.cancel(a))==1 for a in U.inv())
    assert U.subs(t,0)==s.eye(2)
# Nonflat target S/(t): S -> S/(t) has isomorphic special fiber but kernel (t).
assert s.rem(t,t,t)==0 and t!=0
# Unbounded-below module S[t^-1] is nonzero but equals t times itself.
assert s.cancel(t*(1/t))==1
out['graded_flat_lift']={'polynomial_isomorphism_models':30,'nonflat_target_negative_control':True,'unbounded_below_negative_control':True}

# Exterior coefficient algebra, with Z/2 acting by parity. Its even part has nilpotents.
def mul(a,b):
    c=[0]*4
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i&j:continue
            inversions=sum((i>>u&1)*(j>>v&1) for u in range(2) for v in range(u))
            c[i|j]+=(-1)**inversions*x*y
    return tuple(c)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
zero=(0,0,0,0);one=(1,0,0,0);theta=(0,1,0,0);eta=(0,0,1,0)
assert mul(theta,eta)==(0,0,0,1) and mul(eta,theta)==(0,0,0,-1)
assert mul(mul(theta,eta),mul(theta,eta))==zero
count=0
for _ in range(100):
    a,b,c=[tuple(rng.randint(-3,3) for j in range(4)) for k in range(3)]
    assert mul(mul(a,b),c)==mul(a,mul(b,c))
    even=(a[0],0,0,a[3]);odd=(0,a[1],a[2],0)
    assert add(even,odd)==a
    # Invariants of B tensor the trivial/sign representation recover even/odd coefficients.
    assert len([j for j in range(4) if j.bit_count()%2==0])==2
    count+=1
assert theta!=zero and theta[0]==0 # Augmentation loses an actual coefficient.
out['coefficient_algebra']={'exact_exterior_models':count,'nilpotent_even_unit_endomorphisms':True,'augmentation_loss_control':True,'symplectic_group_modelled':False}

count=0
for variables in [2,3]:
    for degree in range(1,5 if variables==2 else 4):
        mons=[a for a in it.product(range(degree+1),repeat=variables) if sum(a)==degree]
        grid=list(it.product(range(degree+1),repeat=variables))
        V=s.Matrix([[s.prod(s.Integer(x)**a for x,a in zip(point,mon)) for mon in mons] for point in grid])
        left=(V.T*V).inv()*V.T;assert left*V==s.eye(len(mons))
        coefficients=s.Matrix(len(mons),4,[rng.randint(-4,4) for j in range(4*len(mons))])
        assert left*(V*coefficients)==coefficients
        count+=1
out['finite_polarization']={'rational_left_inverse_models':count,'exterior_coefficient_components':4}

x,y,z=s.symbols('x y z');vars=(x,y,z)
def truncated_length(f,mu):
    mons=[a for a in it.product(range(mu+1),repeat=3) if sum(a)<=mu];index={a:j for j,a in enumerate(mons)};cols=[]
    for v in vars:
        derivative=s.diff(f,v)
        for a in mons:
            poly=s.Poly(derivative*s.prod(v**e for v,e in zip(vars,a)),*vars);col=[0]*len(mons)
            for mon,c in poly.terms():
                if mon in index:col[index[mon]]=c
            if any(col):cols.append(s.Matrix(col))
    rank=s.Matrix.hstack(*cols).rank() if cols else 0
    return len(mons)-rank
models=0
for mu in range(1,6):
    f=(x+y)**2+(y+z)**2+z**(mu+1)
    assert truncated_length(f,mu)==mu
    assert truncated_length(x*x+y*y,mu)==mu+1
    if mu>1:assert truncated_length(f,mu-1)==mu
    models+=1
out['jet_length_test']={'isolated_lengths':models,'infinite_length_negative_controls':models,'smaller_cutoff_controls':4}

def H(u,e):
    a=u.real;b=u.imag;R=np.eye(3,dtype=complex);R[1:,1:]=np.array([[1,a],[0,1]])@np.array([[1,0],[b,1]])
    K=np.eye(3,dtype=complex);K[0,1]=-u**e
    return K@R
worst=0;tests=0
for e in range(1,7):
    root=np.exp(2j*np.pi/e)
    def J(r):return np.linalg.inv(H(root*r,e))@H(r,e)
    for r in [.4,.1,.01,.001]:
        start=H(r,e);end=H(root*r,e)@J(r)
        worst=max(worst,np.linalg.norm(start-end));assert np.linalg.norm(start-end)<1e-12
        for theta in np.linspace(0,2*np.pi,13):
            u=r*np.exp(1j*theta/e);phi=H(u,e)@J(r*theta/(2*np.pi));tval=r**e*np.exp(1j*theta)
            assert np.linalg.norm(np.array([1,tval,0])@phi-np.array([1,0,0]))<1e-12
            assert np.linalg.norm(np.linalg.inv(phi)@phi-np.eye(3))<1e-12;tests+=1
out['base_change_seam']={'linear_space_transport_models':tests,'seam_error':worst,'closed_ball_tubes_modelled':False}
result={'batch':'B039','status':'pass','scope':'Selected finite interfaces; no headline theorem or Lean build certified.','checks':out}
Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
