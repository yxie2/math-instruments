"""Finite models and exact identities; source global and geometric inputs are not certified."""
from pathlib import Path
from itertools import product, combinations
from fractions import Fraction as F
import json, math, time
import numpy as np
import sympy as s

def cycle_rank():
    cases=[]
    for exceptional in range(1,8):
        # Cellular model of a surviving 2-sphere and exceptional 2-spheres,
        # with one acyclic 3-cell/2-cell pair to test passage to homology.
        n=exceptional+2;boundary=s.zeros(n,1);boundary[n-1,0]=1
        restriction=s.zeros(1,n);restriction[0,0]=1
        assert restriction*boundary==s.zeros(1)
        source_h2=n-boundary.rank();target_h2=1
        assert restriction.rank()==target_h2 and source_h2-target_h2==exceptional
        intersection=s.diag(1,*([-1]*exceptional));classes=s.eye(exceptional+1)
        assert intersection.det()!=0 and classes.rank()==exceptional+1
        # Positivity detector on the effective listed classes is nonzero.
        detector=s.Matrix([[exceptional+2]+[1]*exceptional])
        assert all((detector*classes)[0,j]>0 for j in range(exceptional+1))
        cases.append([exceptional,source_h2,target_h2])
    # A nonzero cellular cycle can be a boundary; positivity is an extra input.
    assert s.Matrix([[1]]).rank()==1
    return dict(cellular_models=cases,scope='Localization rank models and blowup-type intersection forms; no realization of a flip sequence.')

def rounding():
    rng=np.random.default_rng(70056);cases=0;higher=0
    def w(x,N):return math.ceil(N*max(x,F(0)))
    def default(b,N):return sum(w(1-j*(1-b),N) for j in range(1,math.ceil(1/(1-b))+1))
    for _ in range(20000):
        N=int(rng.integers(1,10));count=int(rng.integers(1,5))
        fixed=[bool(rng.integers(0,2)) for _ in range(count)]
        bs=[F(int(rng.integers(0,N)),N) if flag else F(int(rng.integers(1,90)),100) for flag in fixed]
        ms=[int(rng.integers(1,4)) for _ in bs];rs=[int(rng.integers(1,m+1)) for m in ms]
        total=sum(m*b for m,b in zip(ms,bs))
        if total>=1:continue
        variable=sum(r for r,flag in zip(rs,fixed) if not flag)
        paid=w(total,N)
        for b,m,r in zip(bs,ms,rs):
            if b>F(1,2):
                assert m==r==1;higher+=1
                paid+=default(b,N)-w(b,N)
        debt=paid-sum(r*default(b,N) for r,b in zip(rs,bs))
        assert debt>=-max(variable-1,0);cases+=1
    for r in range(1,9):
        b=F(1,2*r);assert w(r*b,1)-r*default(b,1)==1-r
    assert higher>0
    return dict(rational_profiles=cases,higher_default_cases=higher,sharp_ceiling_examples=8)

def finite_covers():
    checks=0
    for m in range(2,11):
        def mul(x,y):return (x[0]+y[0],x[1]+y[1],(x[2]+y[2]+x[0]*y[1])%m)
        def power(x,n):return (n*x[0],n*x[1],(n*x[2]+n*(n-1)//2*x[0]*x[1])%m)
        for a,b,c,d in product(range(-2,3),repeat=4):
            x=power((a,b,1),m);y=power((c,d,0),m)
            assert mul(x,y)==mul(y,x);checks+=1
        for n in range(1,6):
            # G0=(mn Z,n Z,0); N=(0,Z,Z/m), N0=(0,n Z,0).
            x=(m*n,2*n,0);y=(-2*m*n,n,0)
            assert mul(x,y)[2]==0
            assert (m*n)*(n)%m==0
        # Finite reduction in the two infinite coordinates retains the kernel.
        assert len({(0,0,c%m) for c in range(m)})==m
    return dict(power_commutator_models=checks,finite_kernel_separation=True,fiber_subgroup_extensions=45)

def exterior():
    cases=0
    for n in range(2,7):
        Q=s.eye(n)
        for i in range(n-1):Q[i,i+1]=i+1
        for p in range(1,n+1):
            source=list(combinations(range(n),p));target=list(combinations(range(n),p+1))
            for r in range(1,n+1):
                rows=[]
                for cov in range(r):
                    for out in target:
                        row=[]
                        for mon in source:
                            val=0
                            for j in range(n):
                                if j not in mon and tuple(sorted((j,)+mon))==out:
                                    val+=Q[cov,j]*(-1)**sum(i<j for i in mon)
                            row.append(val)
                        rows.append(row)
                rank=s.Matrix(rows).rank() if rows else 0
                kernel=len(source)-rank;expected=math.comb(n-r,p-r) if r<=p else 0
                assert kernel==expected;cases+=1
                if r==p:assert kernel==1
    x,y=s.symbols('x y');f=x*x+y
    for m in range(1,8):
        assert s.expand(s.diff(f**m,x)-m*f**(m-1)*s.diff(f,x))==0
    return dict(exterior_kernel_dimensions=cases,root_ratio_differentiations=7)

def character_energy():
    cases=0
    for q,v0,v1 in product([F(1,3),F(1,2),F(1),F(2),F(3)],range(1,8),range(1,8)):
        ratios=[F(v1,v0),q*F(v0,v1)];weights=[2,3]
        energy=sum(c*(r+1/r-2) for c,r in zip(weights,ratios))
        divergences=[F(0),F(0)]
        for (a,b),c,r in zip([(0,1),(1,0)],weights,ratios):
            divergences[a]+=c*(r-1);divergences[b]+=c*(1/r-1)
        assert sum(divergences)==energy and energy>=0
        assert (energy==0)==(q==1 and v0==v1);cases+=1
    return dict(periodic_graph_character_models=cases,scope='Discrete reversible analogue of the logarithmic energy argument.')

def distance():
    rng=np.random.default_rng(70058);cases=0
    def rho(z,w):return np.arctanh(abs((z-w)/(1-np.conj(w)*z)))
    for _ in range(200):
        z,w,a=.8*np.sqrt(rng.random(3))*np.exp(2j*np.pi*rng.random(3))
        phi=lambda x:(x-a)/(1-np.conj(a)*x)
        assert abs(rho(phi(z),phi(w))-rho(z,w))<1e-10;cases+=1
    for R in np.linspace(.1,8,40):assert 0<np.tanh(R)<1
    # Cutting a path at R, then moving to a net center costs < r/2+r/4.
    for r,R in product([F(1,3),F(1),F(3)],range(1,8)):
        total=R+r/4+r/8;tail=total-R
        assert tail<r/2 and tail+r/4<r
    assert all(0<F(1,n)<1 and abs(F(1,n)-F(1,2))<F(1,2) for n in range(3,40))
    return dict(disc_isometries=cases,compact_disc_ball_radii=40,path_budget_models=21,local_compactness_control='In (0,1) with Euclidean distance, 1/n stays in the closed radius-1/2 ball about 1/2 but converges to an omitted endpoint.')

def hensel():
    rng=np.random.default_rng(70059);roots=0;representations=0
    for p in [3,5,7]:
        modulus=p**4
        def mul(x,y):return ((x[0]*y[0])%modulus,(x[0]*y[1]+x[1]*y[0])%modulus)
        def inv(x):
            a=pow(x[0],-1,modulus);return (a,(-x[1]*a*a)%modulus)
        def add(x,y):return tuple((a+b)%modulus for a,b in zip(x,y))
        def neg(x):return tuple(-a%modulus for a in x)
        def sqrt_unit(u,v):
            for _ in range(5):
                error=add(mul(v,v),neg(u));v=add(v,neg(mul(error,inv(add(v,v)))))
            assert mul(v,v)==u;return v
        for _ in range(80):
            a=int(rng.integers(1,modulus))
            if a%p==0:a+=1
            u=(a,int(rng.integers(0,modulus)))
            residue_root=next((v for v in range(1,p) if v*v%p==a%p),None)
            if residue_root is not None:sqrt_unit(u,(residue_root,0));roots+=1
            a0,b0=next((x,y) for x,y in product(range(p),repeat=2) if (x*x+y*y)%p==a%p)
            c=((a0*a0+b0*b0)%modulus,0);ratio=mul(u,inv(c));v=sqrt_unit(ratio,(1,0))
            aa=mul(v,(a0,0));bb=mul(v,(b0,0));assert add(mul(aa,aa),mul(bb,bb))==u;representations+=1
    assert 3 not in {(a*a+b*b)%8 for a,b in product(range(8),repeat=2)}
    return dict(dual_number_square_roots=roots,two_square_representations=representations,dyadic_negative_control=True)

def lattice():
    k=4;cases=0;fractional=0
    for p,t in [(s.Matrix([[1,1]]),s.Matrix([1,3])),(s.Matrix([[2,0]]),s.Matrix([2,1]))]:
        assert p*t==s.Matrix([[k]])
        pr=s.eye(2)-t*p/k;assert p*pr==s.zeros(1,2) and pr*t==s.zeros(2,1)
        for l1,l2,z in product(range(-5,6),range(-5,6),range(-5,6)):
            l=s.Matrix([l1,l2]);b=(p*l)[0]
            if (b-z)%k:continue
            u=k*pr*l;assert all((u[j]+t[j]*z)%k==0 for j in range(2))
            lift=(u+t*z)/k;assert all(a.q==1 for a in lift) and p*lift==s.Matrix([z]) and pr*lift==pr*l
            for h in [-2,1,3]:assert pr*(lift+t*h)==pr*lift
            cases+=1;fractional+=any(a.q!=1 for a in pr*l)
        for v1,v2 in product(range(-8,9),repeat=2):
            v=s.Matrix([v1,v2]);assert ((p*(k*v))[0]==0)==((p*v)[0]==0)
    p=s.Matrix([[1,1]]);t=s.Matrix([1,3]);u=s.Matrix([-1,1]);z=1
    assert all((u[j]+t[j]*z)%k==0 for j in range(2))
    assert any((u[j]-t[j]*z)%k!=0 for j in range(2))
    assert fractional>0
    return dict(integral_gluing_pairs=cases,fractional_inner_coordinates=fractional,lift_independence=True,sign_sensitive_control=True)

if __name__=='__main__':
    start=time.perf_counter();checks={}
    for f in [cycle_rank,rounding,finite_covers,exterior,character_energy,distance,hensel,lattice]:checks[f.__name__]=dict(status='pass',details=f())
    result=dict(batch='B070',status='pass',elapsed_seconds=round(time.perf_counter()-start,3),scope='Finite models and selected identities; no source headline or Lean certification.',checks=checks)
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
