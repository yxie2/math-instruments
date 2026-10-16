"""Selected geometry identities and finite models; no global conjecture certification."""
from fractions import Fraction as F
from itertools import product, permutations
from math import comb, factorial, pi
from pathlib import Path
import json
import random
import sympy as S
from scipy.integrate import quad

rng=random.Random(26016)

def restriction_counts():
    counts=residue=0
    for d,k in product(range(1,5),range(1,4)):
        d0=k**d
        for degree in (d0,d0+1,2*d0+3):
            for q in range(d0,d0+12):
                # Hilbert function of a monic hypersurface in P^(d+1).
                hilbert=comb(q+d+1,d+1)-(comb(q-degree+d+1,d+1) if q>=degree else 0)
                lower=d0*comb(q-d0+d,d)
                assert hilbert>=lower
                assert factorial(d)*lower >= (k*(q-d0))**d
                counts+=1
        hr=[3*k+r for r in range(k)];bound=max(hr)+k**(d+1)
        for h in range(bound,bound+20):
            r=h%k;q=(h-hr[r])//k
            assert q>=d0
            lower=d0*comb(q-d0+d,d)
            assert factorial(d)*lower >= (h-bound)**d;residue+=1
    return dict(hypersurface_Hilbert_comparisons=counts,residue_class_bounds=residue,
                scope='Exact Hilbert functions and bound arithmetic; not uniform generic projection for every subvariety.')

def rational_faces():
    # Shared edge x+y=1,z=0; several containing polytopes, one excluded polytope.
    counts=0
    alpha=S.sqrt(2)/2;beta=S.sqrt(3)/5
    vertices=[(F(1),F(0),F(0)),(F(0),F(1),F(0)),(F(0),F(0),F(0)),(F(0),F(0),F(2))]
    for n in range(2,102):
        a=F(int(S.floor(alpha*10**n)),10**n)
        b3=F(int(S.floor(beta*10**n)),10**n)
        q=(a,1-a,F(0));b=(F(1),F(1),b3)
        dot=lambda x,y:sum(i*j for i,j in zip(x,y))
        assert 0<a<1 and b3>0 and dot(b,q)==1
        assert all(dot(b,v)<=1 for v in vertices)
        # The edge and both adjacent triangles contain q; x=0 does not.
        assert q[2]==0 and q[0]+q[1]==1 and q[0]>0 and q[1]>0
        assert sum(b)<F(5,2)  # an open budget survives rational approximation
        counts+=1
    # Independently rounding coordinates need not preserve a supporting equality.
    assert F(7,10)+F(2,10)!=1
    return dict(exact_rational_approximants=counts,
                scope='Shared-face incidence and strict-budget examples; not an algorithm for every rational polytope family.')

def cylinder_certificate():
    p,s,u,f,j,w,l,m,e=S.symbols('p s u f j w l m e')
    x=s*s+u**3+p*p*f;y=s+x*(x-u**3);z=s*x+p*p*j
    h=x*x*f-(1+2*s*x)*j-p*p*j*j-p*u
    assert S.expand(x*y-z*(z+1)-p*p*(h+p*u))==0
    ds=-3*p*p*x*u*u;du=-p*p;df=(6*s*x+3)*u*u;dj=3*x*x*u*u
    def deriv(g): return S.expand(S.diff(g,s)*ds+S.diff(g,u)*du+S.diff(g,f)*df+S.diff(g,j)*dj)
    for g in (x,y,z): assert deriv(g)==0
    assert deriv(h)==p**3
    nilpotence=[]
    for g in (p,s,u,f,j):
        for n in range(1,9):
            g=deriv(g)
            if g==0: nilpotence.append(n);break
        else: raise AssertionError('nilpotence bound')
    x0=s*s+u**3
    ff=4*s*s*l+(1+2*s*x0)*m;jj=-(1-2*s*x0)*l+x0*x0*m
    assert S.expand(x0*x0*ff-(1+2*s*x0)*jj-l)==0
    assert S.expand((1-2*s*x0)*ff+4*s*s*jj-m)==0
    q=S.expand(2*x0*ff**2-2*s*ff*jj-jj**2)
    hh=S.expand(l-p*u+p*p*q+p**4*ff**3)
    assert S.expand(h.subs({f:ff,j:jj},simultaneous=True)-hh)==0
    c=q.subs(l,0);q1=S.div(q-c,l,l)[0]
    assert S.expand(q-c-l*q1)==0
    ls=p*u-p*p*c
    root=S.expand(hh.subs(l,ls))
    assert S.rem(root,p**3,p)==0
    aux=u-p*q-p**3*ff**3-p*p*w
    e0=-w-p*ff**3-q1*aux
    assert S.expand(p**3*e0-(l-ls)-(p*p*q1-1)*(hh+p**3*w))==0
    # Exact polynomial inverse, including the special fiber p=0.
    substituted=S.Poly(S.expand(hh.subs(l,ls+p**3*e)),p)
    assert all(exp[0]>=3 for exp,coeff in substituted.terms())
    ww=S.expand(-substituted.as_expr()/p**3)
    assert S.expand(hh.subs(l,ls+p**3*e)+p**3*ww)==0
    # Certificate implies the remaining inverse after cancelling p^3 in the polynomial domain.
    assert S.expand(e0.subs({l:ls+p**3*e,w:ww},simultaneous=True)-e)==0
    assert not ww.has(S.Pow(p,-1))
    return dict(symbolic_certificate='passed',generator_nilpotence_orders=nilpotence,
                inverse_polynomial_terms=len(S.Poly(ww,p,s,u,m,e).terms()),
                scope='Exact source cylinder identities and inverse; no non-polynomiality or rigidity verification.')

def filtered_derivations():
    x,y=S.symbols('x y');checks=orders=0
    def degree(f,weights):
        return max((sum(a*b for a,b in zip(es,weights)) for es,c in S.Poly(f,x,y).terms() if c),default=None)
    def initial(f,d,weights):
        return S.expand(sum(c*x**es[0]*y**es[1] for es,c in S.Poly(f,x,y).terms() if sum(a*b for a,b in zip(es,weights))==d))
    for weights in ((1,1),(-1,2),(2,-3),(-2,-1)):
        for r in range(4):
            shift=r*weights[0]-weights[1]
            deriv=lambda f:S.expand(x**r*S.diff(f,y))
            for _ in range(12):
                f=S.expand(sum(rng.randrange(-3,4)*x**rng.randrange(4)*y**rng.randrange(5) for _ in range(8)))
                if not f: continue
                d=degree(f,weights);left=initial(f,d,weights);right=f
                for m in range(6):
                    assert S.expand(left-initial(right,d+m*shift,weights))==0
                    left=deriv(left);right=deriv(right);checks+=1
                g=1+x+y**3
                nu=lambda z:S.Poly(z,y).degree()
                assert nu(S.expand(f*g))==nu(f)+nu(g);orders+=1
    # Generator bounds can fail without degree-exact representatives.
    h1=x;h2=x*x+y
    bad_shift=degree(S.diff(h2,y),(1,1))-degree(h2,(1,1))
    h=h2-h1*h1
    assert degree(S.diff(h,y),(1,1))>degree(h,(1,1))+bad_shift
    # Characteristic zero matters for factorial closure: d/dx kills x^2 over F_2.
    assert S.Poly(S.diff(x*x,x),x,modulus=2).is_zero and not S.Poly(S.diff(x,x),x,modulus=2).is_zero
    return dict(graded_iterate_identities=checks,LND_order_products=orders,
                scope='Weighted polynomial models with positive and negative degrees; no source associated-graded presentation.')

def trace_pairing():
    w=S.symbols('w');models=quotients=0
    for degree in range(1,9):
        for _ in range(8):
            aa=[rng.choice((-3,-2,-1,1,2,3))]+[rng.randrange(-3,4) for _ in range(degree-1)]
            a=sum(c*w**i for i,c in enumerate(aa))
            gram=S.Matrix(degree,degree,lambda i,j:S.expand(a*w**(i+j)).coeff(w,degree-1))
            assert gram.det()==(-1)**(degree*(degree-1)//2)*aa[0]**degree;models+=1
    for _ in range(50):
        a,b,c=[S.Integer(rng.randrange(-5,6)) for _ in range(3)]
        block=S.Matrix([[a,b],[b,c]])
        if block.det()==0: continue
        gram=S.Matrix([[0,0,0,1],[0,a,b,0],[0,b,c,0],[1,0,0,0]])
        ell=S.Matrix([[0,rng.randrange(-5,6),rng.randrange(-5,6),rng.randrange(-5,6)]])
        small=ell[:,1:3]
        assert (ell*gram.inv()*ell.T)[0]==(small*block.inv()*small.T)[0];quotients+=1
    # Rank-four self-dual splitting determined by two section counts.
    solutions=[]
    for ds in product(range(-5,6),repeat=4):
        if tuple(sorted(ds))!=ds or tuple(sorted(-d for d in ds))!=ds: continue
        if sum(max(d,0) for d in ds)==3 and sum(max(d-1,0) for d in ds)==2: solutions.append(ds)
    assert solutions==[(-3,0,0,3)]
    return dict(ramified_residue_Gram_models=models,orthogonal_quotient_norms=quotients,
                splitting_solutions=solutions,scope='Local perfect-pairing algebra; no source curve or principal-parts construction.')

def jet_brackets():
    t,z=S.symbols('t z');models=preserving=0
    for k,ell in product(range(1,7),range(4)):
        for _ in range(2):
            poly=lambda:sum(rng.randrange(-2,3)*z**i for i in range(4))
            b,h,a,c=[poly() for _ in range(4)]
            dv=[t**(k+1)*b,t**k*h];vv=[t**(ell+2)*a,t**(ell+1)*c]
            bracket=[S.expand(sum(dv[j]*S.diff(vv[i],coord)-vv[j]*S.diff(dv[i],coord) for j,coord in enumerate((t,z)))) for i in range(2)]
            expected=[t**(k+ell+2)*((ell+1-k)*b*a+h*S.diff(a,z)-c*S.diff(b,z)),
                      t**(k+ell+1)*((ell+1)*b*c+h*S.diff(c,z)-k*h*a-c*S.diff(h,z))]
            assert all(S.expand(x-y)==0 for x,y in zip(bracket,expected))
            div=S.expand(t**5*(S.diff(t**-5*dv[0],t)+S.diff(t**-5*dv[1],z)))
            assert S.expand(div-t**k*((k-4)*b+S.diff(h,z)))==0
            if k!=4:
                assert S.expand((k-4)*S.diff(h,z)/(4-k)+S.diff(h,z))==0;preserving+=1
            models+=1
    assert S.diff(z,z)!=0  # at k=4, no b can cancel this h'
    return dict(polynomial_brackets=models,nonresonant_volume_corrections=preserving,
                scope='Exact local vector-field algebra; no convergence or global obstruction vanishing.')

def logarithmic_curvature():
    t=S.symbols('t',positive=True);models=0;errors=[]
    for b in range(1,9):
        for r in range(b+1):
            u=t**r*(1+t)**(b-r)
            lhs=S.expand(u*(S.diff(u,t)+t*S.diff(u,t,2))-t*S.diff(u,t)**2)
            assert S.cancel(lhs/u**2-(b-r)/(1+t)**2)==0
            mass,err=quad(lambda x:4*pi*(b-r)*x/(1+x*x)**2,0,float('inf'))
            assert abs(mass+2*pi*r-2*pi*b)<1e-9
            errors.append(abs(mass+2*pi*r-2*pi*b));models+=1
    return dict(radial_singular_metrics=models,maximum_mass_error=max(errors),
                scope='Polynomial Levi identities and diffuse-plus-atomic mass models; no nonsmooth compactness theorem.')

def invariant_measure_obstruction():
    a=(1+S.I*S.sqrt(3))/2;s=S.Rational(1,2)-S.I*(1+2*S.sqrt(2))/(2*S.sqrt(3))
    aa=S.diag(a,1/a);bb=S.Matrix([[s,1],[S.sqrt(2)/3,1-s]])
    simplify=lambda m:m.applyfunc(S.simplify)
    eye=S.eye(2)
    assert S.simplify(aa.det()-1)==0 and S.simplify(bb.det()-1)==0
    assert simplify(aa**3)==-eye and simplify(bb**3)==-eye
    cc=simplify(aa.inv()*bb)
    assert simplify(cc**4)==-eye and simplify(cc**8)==eye
    assert S.simplify(S.trace(aa*bb)-(1+S.sqrt(2)))==0
    assert bb[0,1]!=0 and bb[1,0]!=0
    perms=0
    for n in (1,2):
        for p in permutations(range(n)):
            if all(p[p[p[i]]]==i for i in range(n)):
                assert tuple(p)==tuple(range(n));perms+=1
    annuli=0
    for n in range(-12,13):
        for theta in (F(1),F(3,2),F(7,4)):
            radius=F(2)**n*theta
            assert F(2)**n<=radius<F(2)**(n+1)
            assert F(2)**(n+1)<=2*radius<F(2)**(n+2);annuli+=1
    return dict(exact_matrix_data='passed',small_support_permutations=perms,half_open_annulus_checks=annuli,
                scope='Exact matrix and finite partition data; infinite-measure exclusion is the written countable-additivity argument.')

if __name__=='__main__':
    groups={}
    for name,fn in [('restriction_counts',restriction_counts),('rational_faces',rational_faces),
                    ('cylinder_certificate',cylinder_certificate),('filtered_derivations',filtered_derivations),
                    ('trace_pairing',trace_pairing),('jet_brackets',jet_brackets),
                    ('logarithmic_curvature',logarithmic_curvature),('invariant_measure_obstruction',invariant_measure_obstruction)]:
        groups[name]=fn();print(name,'passed',flush=True)
    result=dict(batch='B026',status='passed',check_groups=groups,
                limitations='Checks concern selected finite mechanisms, not Fujita freeness, cancellation failure, Lipman-Zariski or Griffiths counterexamples.')
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
