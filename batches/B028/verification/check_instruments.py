"""Finite tensor, differential and envelope checks; not PDE classification proofs."""
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path
import json
import numpy as np
import sympy as S
from scipy.optimize import linprog

rng=np.random.default_rng(28016)
perms=list(permutations(range(3)))

def sym3(a):return sum(a.transpose(p) for p in perms)
def J(v):
    eye=np.eye(len(v),dtype=v.dtype)
    return np.einsum('ij,k->ijk',eye,v)+np.einsum('ik,j->ijk',eye,v)+np.einsum('jk,i->ijk',eye,v)
def B(v):
    eye=np.eye(len(v),dtype=v.dtype)
    return 2*np.einsum('ij,k->ijk',eye,v)-np.einsum('ik,j->ijk',eye,v)-np.einsum('jk,i->ijk',eye,v)
def tensor_projections():
    n=5
    def s2(a):
        z=a+a.T;return 5*z-np.eye(n,dtype=int)*np.trace(z)
    def s3(a):
        z=sym3(a);return 7*z-J(np.einsum('iik->k',z))
    def hook(a):
        z=3*(a+a.transpose(1,0,2))-sym3(a)
        return 8*z-B(np.einsum('iik->k',z))
    def anti(a):return sum((-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))*a.transpose(p) for p in perms)
    result={}
    for name,r,scale,fn in [('symmetric_rank2',2,10,s2),('symmetric_rank3',3,42,s3),('hook_rank3',3,48,hook),('alternating_rank3',3,6,anti)]:
        size=n**r;basis=np.eye(size,dtype=np.int64)
        mat=np.column_stack([fn(row.reshape((n,)*r)).ravel() for row in basis])
        assert np.array_equal(mat,mat.T) and np.array_equal(mat@mat,scale*mat)
        rank=int(np.trace(mat)//scale);result[name]=dict(size=size,scale=scale,rank=rank)
        if name!='alternating_rank3':
            for col in mat.T:
                tensor=col.reshape((n,)*r)
                trace=np.trace(tensor) if r==2 else np.einsum('iik->k',tensor)
                assert np.all(trace==0)
    return dict(exact_projection_matrices=result,scope='Exact operators on the full five-dimensional tensor spaces; source certificate coefficient tables not verified.')

def tensor_bounds():
    checks=0
    for _ in range(200):
        raw=rng.normal(size=(5,5));A=(raw+raw.T)/2;A-=np.eye(5)*np.trace(A)/5;A/=np.linalg.norm(A)
        ev=np.linalg.eigvalsh(A)
        assert max(ev**2)<=.8+1e-12 and np.trace(A@A@A)**2<=.45+1e-12
        for k in range(1,9):assert np.linalg.norm(np.linalg.matrix_power(A,k))**2<=.8**(k-1)+1e-12
        raw=rng.normal(size=(5,5,5));X=sym3(raw)/6;X-=J(np.einsum('iik->k',X))/7
        contraction=np.einsum('ijk,jk->i',X,A)
        assert np.dot(contraction,contraction)<=5/7*np.sum(X*X)+1e-12
        z=rng.normal(size=5);Z=(np.einsum('i,jk->ijk',z,A)+np.einsum('j,ik->ijk',z,A)+np.einsum('k,ij->ijk',z,A))/3
        Z-=J(np.einsum('iik->k',Z))/7
        assert abs(np.sum(Z*Z)-np.dot(z,z)/3-10/21*np.dot(A@z,A@z))<1e-11;checks+=1
    # Sharp equality with A=diag(4,-1,-1,-1,-1)/sqrt(20), z=e1.
    vals=[S.Rational(4,1)/S.sqrt(20)]+[-1/S.sqrt(20)]*4
    assert S.simplify(sum(x**3 for x in vals)**2)==S.Rational(9,20)
    assert S.Rational(1,3)+S.Rational(10,21)*vals[0]**2==S.Rational(5,7)
    return dict(random_normalized_tensor_models=checks,sharp_cubic_and_contraction_constants='exact',scope='Finite models and equality constants; not the complete graph bounds or global algebraic certificate.')

def conic_bundle():
    z,w,c,d=S.symbols('z w c d');I=S.I
    th=S.Matrix([z*z-w*w,I*(z*z+w*w),2*z*w]);h1=S.Matrix([z,I*z,w]);h2=S.Matrix([-w,I*w,z])
    clean=lambda v:all(S.expand(q)==0 for q in v)
    assert S.expand(th.dot(th))==0 and S.expand(th.dot(h1))==0 and S.expand(th.dot(h2))==0
    assert clean(h1.cross(h2)-I*th) and clean(z*h1+w*h2-th)
    p=c*h1+d*h2;assert S.expand(p.dot(p)-(-w*c+z*d)**2)==0
    mat=S.Matrix.hstack(th.subs({z:1,w:0}),th.subs({z:0,w:1}),th.subs({z:1,w:1}));assert mat.det()!=0
    count=0
    for zz,ww in product(range(-3,4),repeat=2):
        if not(zz or ww):continue
        frame=S.Matrix.hstack(h1,h2).subs({z:zz,w:ww});assert frame.rank()==2
        row=S.Matrix([[-ww,zz]]);assert row.rank()==1 and row*S.Matrix([zz,ww])==S.zeros(1,1);count+=1
    return dict(symbolic_conic_and_quotient_identities='passed',projective_frame_samples=count,scope='Exact bundle-map formulas; no transport matching or global inverse-problem theorem.')

def finite_type():
    count=0
    for n in range(2,7):
        for rep in range(12):
            B0=rng.integers(-3,4,size=(n,n,n));B0=B0+B0.transpose(1,0,2)
            dB=rng.integers(-3,4,size=(n,n,n,n));dB=dB+dB.transpose(0,2,1,3)
            v=rng.integers(-3,4,size=n);q=int(rng.integers(-3,4))
            for s in range(n):
                i=(s+1)%n
                dv=lambda direction,a:sum(int(B0[a,direction,b])*int(v[b]) for b in range(n))+(q if a==direction else 0)
                raw=sum(int(dB[i,s,i,a]-dB[s,i,i,a])*int(v[a])+int(B0[s,i,a])*dv(i,a)-int(B0[i,i,a])*dv(s,a) for a in range(n))
                C=[int(dB[i,s,i,b]-dB[s,i,i,b])+sum(int(B0[s,i,a])*int(B0[a,i,b])-int(B0[i,i,a])*int(B0[a,s,b]) for a in range(n)) for b in range(n)]
                closed=sum(C[b]*int(v[b]) for b in range(n))+int(B0[s,i,i]-B0[i,i,s])*q
                assert raw==closed;count+=1
    x,y=S.symbols('x y',real=True);coords=[x,y];eta=x**3+2*x+y*y;v=S.Matrix([S.diff(eta,z) for z in coords]);q=x+y
    B0=[[[S.cancel((S.diff(eta,coords[i],coords[j])-(q if i==j else 0))/v[0]) if a==0 else S.S(0) for a in range(2)] for j in range(2)] for i in range(2)]
    for s in range(2):
        i=1-s
        C=[S.diff(B0[s][i][b],coords[i])-S.diff(B0[i][i][b],coords[s])+sum(B0[s][i][a]*B0[a][i][b]-B0[i][i][a]*B0[a][s][b] for a in range(2)) for b in range(2)]
        d=B0[s][i][i]-B0[i][i][s]
        assert S.cancel(sum(C[b]*v[b] for b in range(2))+d*q-S.diff(q,coords[s]))==0
    return dict(exact_coefficient_closures=count,variable_coefficient_solution='exact',scope='Checks the prolonged-system coefficients; pathwise ODE uniqueness remains the written argument.')

def profile_defect():
    v,z=S.symbols('v z',real=True);q=1-v*v;D=1-z
    gradv2=q*q*z/2;lapv=-v*q;lapq=-2*gradv2-2*v*lapv
    assert S.expand(-lapq+(3*v*v-1)*q+q*q*D)==0
    assert S.expand(q*q/4-gradv2/2-q*q*D/4)==0
    T2,pgradD=S.symbols('T2 pgradD')
    pgradlapU=-q*z*D-S.sqrt(2)*v*pgradD
    lapD=-2*T2-2*pgradlapU
    assert S.expand(-lapD+2*S.sqrt(2)*v*pgradD+2*q*z*D-2*T2)==0
    # Ground-state transform as a total divergence, for arbitrary one-dimensional q,eta.
    x=S.symbols('x');Q=S.Function('q')(x);e=S.Function('e')(x);V=S.Function('V')(x)
    original=S.diff(Q*e,x)**2+V*(Q*e)**2
    transformed=Q*Q*S.diff(e,x)**2+Q*e*e*(-S.diff(Q,x,2)+V*Q)
    assert S.expand(original-transformed-S.diff(Q*S.diff(Q,x)*e*e,x))==0
    return dict(defect_and_ground_state_identities='exact',scope='Symbolic identities conditional on the PDE and chain rule; no global stability classification.')

def overlap_variance():
    count=0
    for n,k in product(range(1,6),range(1,9)):
        for rep in range(4):
            vals=[F(int(v),3) for v in rng.integers(-4,5,size=k)]
            if not any(vals):vals[0]=F(1)
            grads=[[F(int(v),5) for v in row] for row in rng.integers(-5,6,size=(k,n))]
            norm=sum(v*v for v in vals);cross=[sum(vals[j]*grads[j][a] for j in range(k)) for a in range(n)]
            b=[v/norm for v in cross]
            variance=sum((grads[j][a]-vals[j]*b[a])**2 for j in range(k) for a in range(n))
            difference=sum(v*v for row in grads for v in row)-sum(v*v for v in cross)/norm
            assert variance==difference and variance>=0
            for V in (-3,0,4):assert V*norm==sum(V*v*v for v in vals)
            count+=1
    s=S.symbols('s');G=S.Function('G')(s);f=S.Function('f')(s);J0=S.Function('J')(s)
    original=J0*(S.diff(G*f,s)**2+S.diff(G,s,2)/G*(G*f)**2)
    desired=J0*G**2*S.diff(f,s)**2-S.diff(J0,s)*G*S.diff(G,s)*f**2
    assert S.expand(original-desired-S.diff(J0*G*S.diff(G,s)*f*f,s))==0
    return dict(exact_branch_variance_models=count,normal_jacobian_integration='exact',scope='Finite branch algebra and a symbolic integration-by-parts identity, not global immersed-tube compactness.')

def quadratic_envelopes():
    y,x,d,ell=S.symbols('y x d ell',real=True,nonzero=True)
    cost=(y-x-d*ell)**2/(2*ell);q=(y-x-d*ell)/ell
    Hess=S.hessian(cost,(y,ell));direction=S.Matrix([q,1])
    assert S.simplify((direction.T*Hess*direction)[0]-d*d/ell)==0
    assert S.diff(ell*S.log(ell),ell,2)==1/ell
    l,h=S.symbols('l h',positive=True);z=S.symbols('z');mid=(h*x+l*z)/(h+l)
    assert S.simplify((mid-x)**2/(2*l)+(z-mid)**2/(2*h)-(z-x)**2/(2*(h+l)))==0
    count=0
    for _ in range(100):
        a=[F(int(v),3) for v in rng.integers(-5,6,5)];b=[F(int(v),7) for v in rng.integers(-5,6,5)];c=[F(int(v),5) for v in rng.integers(-5,6,5)]
        xx=F(int(rng.integers(-5,6)),2);t=F(2,3);ll=F(3,7);hh=F(4,5)
        direct=max(a[i]*xx+b[i]+c[i]*(t+ll+hh)+(ll+hh)*a[i]*a[i]/2 for i in range(5))
        nested=max(a[i]*xx+(b[i]+c[i]*hh+hh*a[i]*a[i]/2)+c[i]*(t+ll)+ll*a[i]*a[i]/2 for i in range(5))
        assert direct==nested;count+=1
    return dict(exact_semigroup_models=count,moving_center_hessian='exact',scope='Cost composition and contact-Hessian algebra; not the full viscosity envelope theorem or Liouville theorem.')

def barycentric_envelope():
    count=0;maxgap=0.
    for m in range(1,5):
        for rep in range(15):
            points=rng.normal(size=(14,m));weights=rng.random(14);weights/=sum(weights);x=weights@points
            f=np.sin(points[:,0])+np.linalg.norm(points,axis=1)/3;s=float(rng.uniform(.3,2));g=f-np.sum(points*points,axis=1)/(2*s)
            primal=linprog(-g,A_eq=np.vstack([np.ones(14),points.T]),b_eq=np.r_[1,x],bounds=(0,None),method='highs')
            dual=linprog(np.r_[1,x],A_ub=-np.column_stack([np.ones(14),points]),b_ub=-g,bounds=[(None,None)]*(m+1),method='highs')
            assert primal.success and dual.success
            gap=abs(-primal.fun-dual.fun);maxgap=max(maxgap,float(gap));assert gap<1e-8
            assert sum(primal.x>1e-8)<=m+1
            variance=np.sum(primal.x*np.sum((points-x)**2,axis=1))
            assert abs(primal.x@f-variance/(2*s)-(-primal.fun+np.dot(x,x)/(2*s)))<1e-8;count+=1
    sharp=0
    for k,s in product((F(1,2),F(1),F(3,2)),(F(1,3),F(1),F(2))):
        for ratio in (F(-1),F(-1,2),F(0),F(1,2),F(1)):
            x=ratio*k*s;y1=-k*s;y2=k*s;w=(y2-x)/(y2-y1)
            value=w*k*abs(y1)+(1-w)*k*abs(y2)-(w*(y1-x)**2+(1-w)*(y2-x)**2)/(2*s)
            assert value==k*k*s/2+x*x/(2*s);sharp+=1
    return dict(finite_configuration_primal_dual_models=count,maximum_duality_gap=maxgap,exact_absolute_value_envelopes=sharp,scope='Finite-support LP duality plus an exact continuum example; not universal attainment or the source PDE subsolution construction.')

if __name__=='__main__':
    groups={}
    for fn in (tensor_projections,tensor_bounds,conic_bundle,finite_type,profile_defect,overlap_variance,quadratic_envelopes,barycentric_envelope):
        groups[fn.__name__]=fn();print(fn.__name__,'passed',flush=True)
    result=dict(batch='B028',status='passed',check_groups=groups,limitations='Selected finite algebra only; no Bernoulli dimension classification, elasticity uniqueness, Allen-Cahn rigidity or infinity-harmonic regularity certified; no Lean build.')
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
