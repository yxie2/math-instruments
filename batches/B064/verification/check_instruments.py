"""Selected finite analysis checks with explicit model and truncation boundaries."""
from itertools import product
from pathlib import Path
import json
import math
import time
import numpy as np
import sympy as s
from scipy.integrate import quad
from scipy.optimize import linprog
from scipy.linalg import fractional_matrix_power

RNG=np.random.default_rng(64016)

def zero_trace():
    cases=0
    for _ in range(80):
        length=RNG.uniform(.1,2,6); height=RNG.uniform(.1,2,6); signs=RNG.choice([-1,1],6)
        energy=np.sum(4*height**2/length)
        for delta in (.005,.05,.2,.8):
            x=np.linspace(0,1,501); w=signs[:,None]*height[:,None]*(1-abs(2*x-1))
            clipped=np.sign(w)*np.maximum(abs(w)-delta,0)
            assert np.max(abs(w-clipped))<=delta+1e-12
            e=np.sum(4*height**2/length*np.maximum(1-delta/height,0))
            assert e<=energy+1e-12
            assert np.all(clipped[:,[0,-1]]==0); cases+=1
    return dict(tent_truncations=cases,scope='Exact piecewise-linear energy in one-dimensional component models.')

def trace_cover():
    cases=0
    for n in range(3,30):
        parent=[-1]+[int(RNG.integers(0,j)) for j in range(1,n)]; costs=RNG.uniform(.01,1,n); values=np.zeros(n)
        for j in range(1,n):values[j]=values[parent[j]]+RNG.uniform(-1,1)*costs[j]
        retained=RNG.random(n)<.7; adjacency=[[] for _ in range(n)]
        for j in range(1,n):
            if retained[j]:adjacency[j].append(parent[j]);adjacency[parent[j]].append(j)
        unseen=set(range(n)); total_diam=0; total_mass=0
        while unseen:
            root=next(iter(unseen)); component={root}; stack=[root]; unseen.remove(root)
            while stack:
                for j in adjacency[stack.pop()]:
                    if j in unseen:unseen.remove(j);component.add(j);stack.append(j)
            mass=sum(costs[j] for j in component if j>0 and parent[j] in component and retained[j])
            diameter=max(values[list(component)])-min(values[list(component)])
            assert diameter<=mass+1e-12; total_diam+=diameter;total_mass+=mass
        assert total_diam<=total_mass+1e-12;cases+=1
    widths=[(2/3)**j for j in range(1,31)];assert widths[-1]<1e-5
    return dict(weighted_tree_covers=cases,cantor_cover_lengths=[widths[0],widths[9],widths[-1]],scope='Finite component-cover inequalities and nested interval examples, not arbitrary continuum topology.')

def pullback():
    rr,ww=np.polynomial.legendre.leggauss(96); r=(rr+1)/2; weights=ww/2*r
    angles=np.arange(384)*2*np.pi/384; z=r[:,None]*np.exp(1j*angles)[None,:]
    def integ(a):return float(np.sum(weights[:,None]*a)*2*np.pi/384)
    error=0.0;cases=0
    for a in (0.,.2,.6):
        phi=(z-a)/(1-a*z); deriv=(1-a*a)/abs(1-a*z)**2
        for p,exponent,j in product((2.3,4.,8.),(1.4,2.1,3.8),(1,2,3)):
            q=p*exponent/(p+exponent-2); assert 1<q<p
            assert abs((p-2)*q/(p-q)-exponent)<1e-12
            grad=j*abs(phi)**(j-1); exact=2*np.pi*j**p/(p*(j-1)+2)
            changed=integ(grad**p*deriv**2);error=max(error,abs(changed-exact)/max(1,exact))
            left=integ((grad*deriv)**q)**(1/q); right=exact**(1/p)*integ(deriv**exponent)**(1/q-1/p)
            assert left<=right*(1+1e-9);cases+=1
    assert error<1e-8
    return dict(automorphism_tests=cases,max_relative_change_of_variables_error=error)

def harmonic_barrier():
    x,y,eps=s.symbols('x y eps',positive=True); factor=s.cos(s.pi*x/2)*s.sinh(s.pi*(1-y)/2)/s.sinh(s.pi/2)
    assert s.simplify(s.diff(factor,x,2)+s.diff(factor,y,2))==0
    b=s.lambdify((x,y,eps),-s.log(4)+s.log(1/eps)*factor,'numpy');center=[]
    for e in (1e-1,1e-3,1e-6,1e-12):
        xx=np.linspace(-1,1,101); yy=np.linspace(e,1,101)
        assert np.max(b(xx,e,e)-(-np.log(4)-np.log(e)))<1e-10
        assert np.max(b(-np.ones(101),yy,e)-(-np.log(4)-np.log(yy)))<1e-10
        assert np.max(b(np.ones(101),yy,e)-(-np.log(4)-np.log(yy)))<1e-10
        assert np.max(b(xx,1,e)+np.log(4))<1e-10;center.append(float(b(0,.5,e)))
    assert all(a<b for a,b in zip(center,center[1:]))
    error=0.0
    for _ in range(100):
        z=RNG.uniform(-2,2)+1j*RNG.uniform(.1,3); k=.75
        for fp,fpp in [(1,0),(2*z,2),(1/z,-1/z**2),(1/z**2,-2/z**3)]:
            q=-1j*z.imag*fpp/fp; gx=fp-1j*z.imag*fpp/k; gy=1j*fp-1j*fp/k+z.imag*fpp/k
            jac=(gx.conjugate()*gy).imag/abs(fp)**2
            rhs=k*(k-1)+(2*k-1)*q.real+abs(q)**2
            error=max(error,abs(k*k*jac-rhs),abs(rhs-(abs(q+.25)**2-.25)))
    assert error<1e-11
    return dict(symbolic_harmonicity=True,center_values=center,jacobian_cases=400,max_residual=error)

def atoms():
    raw=np.array([v for v in product((0.,1.,2.),repeat=3) if any(v)]).T
    cost=(np.sum(raw**2,axis=0)*np.max(raw,axis=0))**(1/3); dictionary=raw/cost
    def atom_norm(c):
        result=linprog(np.ones(dictionary.shape[1]),A_ub=-dictionary,b_ub=-abs(c),bounds=(0,None),method='highs');assert result.success
        return result.fun
    cases=0
    for _ in range(60):
        c=RNG.normal(size=3)+1j*RNG.normal(size=3); d=RNG.normal(size=3)+1j*RNG.normal(size=3)
        A=atom_norm(c);assert A+1e-9>=np.linalg.norm(c,3)
        assert atom_norm(c+d)<=A+atom_norm(d)+1e-9
        mask=RNG.integers(0,2,3);assert atom_norm(c*mask)<=A+1e-9
        chunks=RNG.uniform(.01,2,(5,3)); total=chunks.sum(axis=0); target=RNG.uniform(0,1,3)*total*np.exp(2j*np.pi*RNG.random(3)); parts=chunks/total*target
        assert np.max(abs(parts)-chunks)<1e-12 and np.max(abs(parts.sum(axis=0)-target))<1e-12;cases+=1
    return dict(dictionary_atoms=raw.shape[1],norm_models=cases,scope='Mask-closed finite dictionary for the singleton-capacity toy G; an upper approximation, not the full ellipse atomic norm.')

def insertion():
    X,Y=s.symbols('X Y',real=True); rad=X*X+Y*Y; t=(rad-1)/3
    cut=1-10*t**3+15*t**4-6*t**5; cubic=X**3+X*Y**2
    mid=s.lambdify((X,Y),(cut*cubic,s.hessian(cut*cubic,(X,Y))),'numpy'); inner=s.lambdify((X,Y),(cubic,s.hessian(cubic,(X,Y))),'numpy')
    residual=0.0;cases=0;min_eig=10.;max_correction=0.
    for _ in range(40):
        h=RNG.normal(size=(2,2));h=h.T@h+np.eye(2);b=RNG.normal(size=(2,2));b=b.T@b+np.eye(2)
        A=fractional_matrix_power(h,-.5)@fractional_matrix_power(b,.5)
        residual=max(residual,float(np.linalg.norm(A.T@h@A-b)))
    for eps in (.001,.002,.004):
        for _ in range(160):
            v=RNG.uniform(-2,2,2);r2=v@v
            if r2>=4:R=0.;HR=np.zeros((2,2))
            else:R,HR=(inner if r2<=1 else mid)(*v)
            xi=np.array([.15,0])+eps*v; t2=xi@xi;D=-math.sqrt(1-t2)+1-t2/2
            Hq=.5*(np.eye(2)+np.eye(2)/math.sqrt(1-t2)+np.outer(xi,xi)/(1-t2)**1.5)
            actual=Hq+eps*HR;mine=float(np.linalg.eigvalsh(actual).min());min_eig=min(min_eig,mine);assert mine>.5
            corr=float(eps**3*R/D);max_correction=max(max_correction,abs(corr));assert abs(corr)<.25;cases+=1
    assert residual<1e-10
    return dict(matrix_normalizations=40,local_insertion_points=cases,min_hessian_eigenvalue=min_eig,max_cutoff_correction=max_correction,max_normalization_error=residual,scope='C2 piecewise-polynomial cutoff model checks second-derivative estimates; no claim to test all smooth derivatives.')

def gaussian():
    errors=[]
    # h(x,y)=2+cos(x) is nonnegative with infinite total integral, but uniform local mass.
    for a in (1.,.2,.02,.002):
        x=.37;value=quad(lambda z:math.exp(-z*z/4)/(math.sqrt(4*math.pi))*(2+math.cos(x-math.sqrt(a)*z)),-14,14,epsabs=1e-12)[0]
        exact=2+math.exp(-a)*math.cos(x);assert abs(value-exact)<1e-11;errors.append(abs(value-(2+math.cos(x))))
    assert all(a>b for a,b in zip(errors,errors[1:]))
    # h=|x|^(-1/2) on |x|<1 times the y-constant function: locally integrable,
    # uniformly locally bounded mass. At x=2 it vanishes near the evaluation point.
    tails=[]
    for a in (.1,.03,.01):
        val=quad(lambda u:2*(math.exp(-(2-u*u)**2/(4*a))+math.exp(-(2+u*u)**2/(4*a)))/math.sqrt(4*math.pi*a),0,1,epsabs=1e-12)[0]
        bound=4/math.sqrt(4*math.pi*a)*math.exp(-1/(4*a));assert val<=bound+1e-12;tails.append(val)
    assert tails[-1]<tails[0]*1e-8
    return dict(periodic_limit_errors=errors,singular_distant_tails=tails,scope='Explicit uniformly local L1 models; no maximal estimate tested.')

def envelope():
    k=1;P=10.;L=3.;centers=np.array(list(product(range(-70,71),repeat=2)),float)
    def dist_cells(point):return np.linalg.norm(np.maximum(abs(point)-.5,0),axis=-1)
    ratios=[];tails=[];cases=0
    for r,shear in product((1.,.5,.25,.125),(-.6,0.,.7)):
        M=np.array([[r,shear*r],[0,r*r]]);assert abs(np.linalg.det(M)-r**3)<1e-12
        child_centers=centers@M.T
        for z in [np.array([.2,.1]),np.array([8.,-5.]),np.array([-20.,12.])]:
            parent_dist=dist_cells(z-centers); child_distance=float(dist_cells(M@z)); wc=(1+child_distance)**(-P)
            terms=(1+parent_dist)**(-P)*(1+dist_cells(child_centers))**(-P)
            ratios.append(float(terms.sum()/wc));tails.append(float(terms[parent_dist>L].sum()/wc));cases+=1
            assert np.all(terms>=0)
    assert max(ratios)<100 and max(tails)<100
    return dict(finite_windows=cases,parent_cells=len(centers),max_normalized_partial_sum=max(ratios),max_normalized_partial_tail=max(tails),scope='Positive sums truncated to [-70,70]^2. Observed bounds are finite-model checks, not infinite-lattice certificates.')

def main():
    start=time.perf_counter();checks={}
    for fn in (zero_trace,trace_cover,pullback,harmonic_barrier,atoms,insertion,gaussian,envelope):
        checks[fn.__name__]=fn();print(fn.__name__,'passed',flush=True)
    report=dict(status='passed',elapsed_seconds=round(time.perf_counter()-start,3),checks=checks,scope='Selected finite analytic mechanisms; no uniformization, Brennan, restriction or Schrodinger endpoint headline certified.')
    Path(__file__).with_name('results.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='checks'}))

if __name__=='__main__':main()
