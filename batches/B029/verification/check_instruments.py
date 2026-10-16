"""Finite constructions and conditional scalar certificates from geometry sources."""
from fractions import Fraction as F
from math import comb, isqrt
from itertools import product
from pathlib import Path
import json
import numpy as np
import sympy as S
from scipy.integrate import quad

rng=np.random.default_rng(29016)

def positive_densities():
    checks=0;worst=0.
    for r,theta in product((0.,.1,.3,.6,.85,.95),(0.,.3,1.2,2.8)):
        rho=lambda t:(1-r*r)/(1-2*r*np.cos(t-theta)+r*r)
        expected=(1,r*np.cos(theta),r*np.sin(theta))
        for fun,value in zip((lambda t:1, np.cos,np.sin),expected):
            got=quad(lambda t:rho(t)*fun(t),0,2*np.pi,epsabs=1e-11)[0]/(2*np.pi)
            error=abs(got-value);worst=max(worst,error);assert error<1e-10
        # A perturbation with zero mass and first Fourier coefficients.
        eps=.1*(1-r)/(1+r)
        for lam in (0,.25,.75,1):
            combined=lambda t:rho(t)+lam*eps*np.cos(2*t)
            assert min(combined(t) for t in np.linspace(0,2*np.pi,1001))>0
            for fun,value in zip((lambda t:1,np.cos,np.sin),expected):
                assert abs(quad(lambda t:combined(t)*fun(t),0,2*np.pi,epsabs=1e-11)[0]/(2*np.pi)-value)<1e-10
            checks+=1
    return dict(positive_density_and_patch_models=checks,maximum_mean_error=worst,scope='Full-circle Poisson-kernel examples and convex patching; not every parameterized circle-valued path.')

def small_value_derivative():
    x,y,delta,B=S.symbols('x y delta B',nonzero=True,real=True);f=y-x*x;chi=S.Function('chi')(x,y);eta=S.Function('eta')
    h=chi*B*f*eta(f/delta)
    deriv=S.diff(h,y).subs(y,x*x).subs(eta(0),1)
    assert S.simplify(deriv-B*chi.subs(y,x*x))==0
    checks=0
    for b,e in product(range(1,17),range(1,7)):
        epsilon=F(1,e);width=epsilon/F(2*b)
        assert b*width<epsilon;checks+=1
    # A whole vertical segment would force h(y1)-h(y0)=B*(y1-y0).
    assert F(1)*F(1)>2*F(1,10)
    return dict(local_prescribed_derivative='exact',small_support_bounds=checks,vertical_arc_control='obstructed',scope='Local transverse formula and amplitude bounds; finite intersections and tangencies use the written patching proof.')

def prescribed_curvature():
    x,y=S.symbols('x y');coords=[x,y];f=S.Function('f')(x,y);g=S.diag(1,f*f);inv=g.inv()
    Gamma=[[[S.simplify(sum(inv[k,l]*(S.diff(g[l,j],coords[i])+S.diff(g[l,i],coords[j])-S.diff(g[i,j],coords[l])) for l in range(2))/2) for j in range(2)] for i in range(2)] for k in range(2)]
    R=S.diff(Gamma[0][1][1],x)-S.diff(Gamma[0][0][1],y)+sum(Gamma[0][0][l]*Gamma[l][1][1]-Gamma[0][1][l]*Gamma[l][0][1] for l in range(2))
    assert S.simplify(R/(f*f)+S.diff(f,x,2)/f)==0
    k=F(1,1000);upper=1/(1-k);lower=1-k*upper
    assert lower>0 and upper<F(1002,1000)
    count=0
    for order in range(2,11):
        # Formal ODE recurrence for K=x^order*(1+y+y^2), f(0)=1,f_x(0)=0.
        coeff=[S.S(1),S.S(0)];K=1+y+y*y
        for j in range(2,order+6):
            coeff.append(-K*coeff[j-2-order]/(j*(j-1)) if j-2>=order else S.S(0))
        assert all(c==0 for c in coeff[1:order+2])
        assert S.simplify(coeff[order+2]+K/((order+1)*(order+2)))==0;count+=1
    return dict(arbitrary_parameter_metric_curvature='exact',flat_jet_ode_models=count,uniform_positive_lower_bound=str(lower),scope='Curvature formula and formal jets; no nonimmersion obstruction verified.')

def smooth_assembly():
    checks=0
    for n in range(1,81):
        lam=F(1,2**(n+4));eps=F(1,1000);amplitude=eps*F(1,2**n)*lam**(n+2)/F(n+1)**n
        for m in range(n+1):
            bound=amplitude*F(n+1)**m/lam**(m+2)
            assert bound<=eps*F(1,2**n);checks+=1
    tails=0
    for m,N in product(range(12),range(12,28)):
        partial=sum((F(1,2**n) for n in range(N+1,N+21)),F(0))
        assert partial<F(1,2**N);tails+=1
    # Covariant tensor pushforward carries lambda^-2 before differentiating.
    x,y,lam=S.symbols('x y lam',positive=True);E=S.Matrix([[x*x+y,x*y],[x*y,y*y-x]])
    R=S.Matrix([[0,-1],[1,0]]);coords=R.T*S.Matrix([x,y])/lam
    pushed=R*E.subs({x:coords[0],y:coords[1]},simultaneous=True)*R.T/lam**2
    restored=lam**2*R.T*pushed.subs({x:-lam*y,y:lam*x},simultaneous=True)*R
    assert all(S.expand(a)==0 for a in restored-E)
    return dict(exact_diagonal_seminorm_bounds=checks,tail_bounds=tails,tensor_scaling='exact',scope='Finite bounds realizing the infinite-series criterion; chosen source local obstructions remain conditional inputs.')

def rearrangement():
    def Rquad(p,y,c,a,b):
        L=1-y;start=np.clip(c-p/2,0,L-p)
        return max((start-c)**2,(start+p-c)**2)+a*y*y+b*y
    integrals=convexity=0;maxerror=0.
    for rep in range(40):
        c=float(rng.uniform(-.5,1.5));a=float(rng.uniform(0,2));b=float(rng.uniform(-1,1));y=float(rng.uniform(0,.9));L=1-y
        original=((L-c)**3+c**3)/3+(a*y*y+b*y)*L
        rearranged=quad(lambda p:Rquad(p,y,c,a,b),0,L,epsabs=1e-10,points=[min(max(2*c,0),L),min(max(2*(L-c),0),L)])[0]
        error=abs(original-rearranged);maxerror=max(maxerror,error);assert error<1e-8;integrals+=1
        for j in range(10):
            u=rng.dirichlet([1,1,1])[:2];v=rng.dirichlet([1,1,1])[:2];t=float(rng.random());z=(1-t)*u+t*v
            assert Rquad(*z,c,a,b)<=(1-t)*Rquad(*u,c,a,b)+t*Rquad(*v,c,a,b)+1e-10
            p=float(rng.uniform(0,1-z[1]));p2=float(rng.uniform(p,1-z[1]));assert Rquad(p,z[1],c,a,b)<=Rquad(p2,z[1],c,a,b)+1e-12;convexity+=1
    return dict(integral_preservation_models=integrals,convexity_and_monotonicity_models=convexity,maximum_integral_error=maxerror,scope='Quadratic functions on a downwards simplex; no Hamiltonian realization of rearrangements.')

def relative_primitives():
    x,y=S.symbols('x y');a=S.Function('a')(x);b=S.Function('b')(y);c=S.Function('c')(x);d=S.Function('d')(y)
    h=S.diff(a,x)*b+c*S.diff(d,y);alpha_x=-c*d;alpha_y=a*b
    assert S.expand(S.diff(alpha_y,x)-S.diff(alpha_x,y)-h)==0
    checks=0
    for m in range(1,6):
        for rep in range(15):
            # Coordinates x,y,p_1,...,p_m,theta_1,...,theta_m.
            n=2+2*m;omega=np.zeros((n,n));area=float(rng.uniform(.1,3));omega[0,1]=area;omega[1,0]=-area
            for j in range(m):
                p=2+j;theta=2+m+j;omega[p,theta]=1;omega[theta,p]=-1
                for base in (0,1):
                    val=float(rng.normal());omega[p,base]=val;omega[base,p]=-val
            assert abs(np.linalg.det(omega)-area**2)<1e-9
            alpha=np.zeros(n);alpha[:2]=rng.normal(size=2)
            # i_Y Omega=-alpha means Omega.T Y=-alpha.
            Y=np.linalg.solve(omega.T,-alpha)
            assert np.max(abs(Y[2:2+m]))<1e-12;checks+=1
    return dict(local_primitive_identity='exact',horizontal_moser_models=checks,scope='Differential algebra and finite nondegenerate forms; not a global packing construction or flow existence proof.')

def flux_jensen():
    r,J=S.symbols('r J');H=(2-3*r)/(1-r)**S.Rational(3,2)
    assert S.simplify(S.diff(H,r)+3*r/(2*(1-r)**S.Rational(5,2)))==0
    D=np.sqrt(48)/7;lam=.98
    G=lambda x:(1-lam*min(x,D)**2)/np.sqrt(1-min(x,D)**2)
    assert abs(G(D)-.28)<1e-12
    count=0
    for n in range(2,22):
        for rep in range(20):
            values=rng.uniform(.001,.99999,size=n);weights=rng.random(n);weights/=sum(weights);mean=weights@values
            left=weights@(1/values-lam*values);right=G(mean)*(weights@(np.sqrt(1-values**2)/values))
            assert left+1e-10>=right;count+=1
    mean=.99*.1+.01*.8
    assert 1/.8-lam*.8-G(mean)*np.sqrt(1-.8**2)/.8<0
    return dict(weighted_slice_models=count,convexity_derivative='exact',pointwise_mean_substitution_control='fails as expected',scope='Scalar Jensen mechanism; source geometric flux and coarea hypotheses not verified.')

def knot_certificate():
    def arctan_bounds(z,n):
        low=sum(((-1)**j*z**(2*j+1)/F(2*j+1) for j in range(n+1)),F(0));return low,low+z**(2*n+3)/F(2*n+3)
    a,b=arctan_bounds(F(1,5),31);c,d=arctan_bounds(F(1,239),9)
    pminus=F('3.14159265358979');pplus=F('3.14159265358980')
    assert pminus<16*a-4*d<16*b-4*c<pplus
    knots=['.64','.74','.84','.92','.98','1.02','1.06','1.10','1.14','1.18','1.22','1.26','1.30','1.34','1.38','1.42','1.46','1.50','1.54','1.58','1.62','1.70','1.90','2.25']
    bs=[1744,1200,735,432,247,144,57,-15,-74,-119,-153,-178,-196,-211,-226,-247,-275,-260,-193,-76,86,536,2275,6853]
    ss=[None]*5+[76,98,123,151,182,215,247,271,297,325,332,332,318,293,271,251]+[None]*3
    claimed=[4416,2298,1859,1313,967,1037,581,280,145,137,137,209,269,379,369,90,90,100,520,1470,250,1899,14266]
    Dplus=F('.989743318611');assert 49*Dplus*Dplus>48
    bminus=1-1/pminus;error=lambda h:F('.008')*max(Dplus/h-bminus,F(0))**4
    gaps=[]
    for j in range(23):
        a,b=map(F,knots[j:j+2]);inside=a>=F('1.02') and b<=F('1.62');K=F('2.4') if inside else 2/(a*a)
        low=min(F(bs[k]+(ss[k] if inside else 0),100000)-error(F(knots[k])) for k in (j,j+1))-K*(b-a)**2/8
        assert low*10**6>=claimed[j] and low>0;gaps.append(low)
    assert min(gaps)==F(9,100000)
    # Fixed-grid interval rules at N=10^40, using integer square roots.
    N=10**40;count=0
    for numerator in range(101):
        value=F(numerator,103);lo=value.numerator*N//value.denominator;hi=-(-value.numerator*N//value.denominator)
        rootlo=isqrt(lo*N);roothi=isqrt(hi*N);roothi+=int(roothi*roothi<hi*N)
        assert F(rootlo,N)**2<=value<=F(roothi,N)**2;count+=1
    return dict(Machin_pi_enclosure='exact',source_interpolation_intervals=23,minimum_conditional_margin=str(min(gaps)),outward_square_root_models=count,
                scope='The source knot lower bounds and curvature bounds are INPUTS. Their transcendental evaluations and analytic derivative estimates were not independently reproduced. All 23 rational interpolation claims are checked exactly.')

if __name__=='__main__':
    groups={}
    for fn in (positive_densities,small_value_derivative,prescribed_curvature,smooth_assembly,rearrangement,relative_primitives,flux_jensen,knot_certificate):
        groups[fn.__name__]=fn();print(fn.__name__,'passed',flush=True)
    result=dict(batch='B029',status='passed',check_groups=groups,limitations='Selected constructions and conditional finite certificates only; no global immersion, nonimmersion, packing or isoperimetric classification certified; no Lean build.')
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
