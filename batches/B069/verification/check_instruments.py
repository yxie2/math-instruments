"""Exact identities and finite models for B069; global geometric claims are excluded."""
from pathlib import Path
from itertools import product
from fractions import Fraction as F
import json, math, time
import numpy as np
import sympy as s

def interpolation():
    x,y=s.symbols('x y');cases=0
    for ell in range(1,8):
        points=[(i,i*i+ell) for i in range(ell)]
        polys=[]
        for a,b in points:
            f=x*x+y*y+1
            for c,d in points:
                if (a,b)!=(c,d):f*=((a-c)*(x-c)+(b-d)*(y-d))
            assert s.Poly(f,x,y).total_degree()<=2+ell-1
            polys.append(f)
        M=s.Matrix([[f.subs({x:a,y:b}) for f in polys] for a,b in points])
        assert M.is_diagonal() and all(M[i,i]!=0 for i in range(ell));cases+=ell
    return dict(interpolated_points=cases,uniform_degree='m0+ell-1',fixed_ideal_generator='x^2+y^2+1')

def weighted():
    weights=[1,2];gain=2;cases=0
    def mul(a,b):
        out=set()
        for x,y in product(a,b):
            z=x+y
            if z in out:out.remove(z)
            else:out.add(z)
        return out
    images=[{(0,),(0,1)},{(1,),(1,1)}]
    for length in range(1,7):
        for word in product(range(2),repeat=length):
            value={()}
            for j in word:value=mul(value,images[j])
            value.symmetric_difference_update({word})
            assert all(sum(weights[i] for i in term)>=sum(weights[i] for i in word)+gain for term in value);cases+=1
    # Three-generator monomial algebra, only relation U_0^2=0.
    totals=[1];a,b=0,1
    for n in range(1,20):a,b=b,2*(a+b);totals.append(a+b)
    C=[0]+[sum(totals[:n]) for n in range(1,21)]
    for n in range(1,21):assert C[n]-3*C[max(0,n-1)]+C[max(0,n-2)]>=1
    t=F(1,2);budgets=[]
    for depth in range(4,13):
        value=1-3*t+t*t+t**depth/(1-t)
        assert value<0;budgets.append(str(value))
    return dict(substituted_words=cases,cumulative_degrees=20,convergent_tail_budgets=budgets)

def stabilization():
    p,a,u,F0,J,w=s.symbols('p a u F J w');vars=[p,a,u,F0,J]
    x=a*a-u*u+p*F0;H=x*x*F0-(1+2*a*x)*J-p*J*J-u
    M=s.Matrix([[F0,a-u],[a+u,-p]]);e=s.Matrix([x,-J]);n=s.Matrix([J,x]);N=n*e.T
    assert s.expand((e.T*n)[0])==0
    assert ((s.eye(2)-2*N)*(s.eye(2)+2*N)-s.eye(2)).applyfunc(s.expand)==s.zeros(2)
    Mp=(s.eye(2)-2*N)*M
    assert s.expand(Mp.det()-M.det())==0
    uprime=(Mp[1,0]-Mp[0,1])/2
    assert s.expand(H+J+uprime)==0
    delta=[0,2*p*x*u,-p,-4*a*x*u-2*u,-2*x*x*u]
    def D(f):return s.expand(sum(s.diff(f,v)*d for v,d in zip(vars,delta)))
    y=a+x*(x+u*u);z=a*x+p*J
    assert s.expand(x*y-z*(z+1)-p*(H+u))==0
    assert D(x)==D(y)==D(z)==D(p)==0 and D(H)==p
    nilpotence=[]
    for v in vars:
        derivatives=[v]
        while derivatives[-1]!=0:
            derivatives.append(D(derivatives[-1]));assert len(derivatives)<10
        nilpotence.append(len(derivatives)-1)
        # The +/- exponential composite cancels at each derivative order.
        for k in range(1,len(derivatives)):
            assert sum(F((-1)**j,math.factorial(j)*math.factorial(k-j)) for j in range(k+1))==0
    x0=a*a-u*u;L=x0*x0*F0-(1+2*a*x0)*J;N0=(1-2*a*x0)*F0+4*a*a*J
    assert s.expand(4*a*a*L+(1+2*a*x0)*N0-F0)==0
    assert s.expand(-(1-2*a*x0)*L+x0*x0*N0-J)==0
    Q0=2*x0*F0**2+p*F0**3-2*a*F0*J-J**2
    assert s.expand(H-L+u-p*Q0)==0
    return dict(matrix_change=True,quadric_identity=True,nilpotence_orders=nilpotence,unimodular_elimination=True)

def lifting():
    h,U,V,W=s.symbols('h U V W');x=U**3+h*V;y=-U**2+h*W
    S=2*U**3*V+3*U**4*W+h*(V*V-3*U*U*W*W)+h*h*W**3
    assert s.expand(x*x+y**3-h*S)==0
    alpha,beta,x,y,base_s,G,T=s.symbols('alpha beta x y base_s G T')
    r=alpha*(1+beta*y);q=beta**2;bez=alpha*h+beta*y-1
    a=y+U**2;b=base_s-h*G**2+2*U*y*G;W0=r*a+q*b
    assert s.expand(r*h+q*y*y-1-bez*(1+beta*y))==0
    assert s.expand(y*y*a-h*b-((h*G-y*U)**2+y**3-h*base_s))==0
    assert s.expand(h*W0-a-(r*h+q*y*y-1)*a-q*(h*b-y*y*a))==0
    assert s.expand(y*y*W0-b-(r*h+q*y*y-1)*b-r*(y*y*a-h*b))==0
    assert s.expand(alpha*(h*T-beta*x)+beta*(y*T+alpha*x)-T-bez*T)==0
    rel=h*G-y*U-x
    assert s.expand(h*(alpha*U+beta*G)-U-beta*x-bez*U-beta*rel)==0
    assert s.expand(y*(alpha*U+beta*G)-G+alpha*x-bez*G+alpha*rel)==0
    cases=0;nonunit=0
    for modulus in [2,4,6,8,9,10]:
        for h,y in product(range(modulus),repeat=2):
            if math.gcd(h,y,modulus)!=1:continue
            alpha,beta=next((a,b) for a,b in product(range(modulus),repeat=2) if (a*h+b*y)%modulus==1)
            r=alpha*(1+beta*y);q=beta*beta
            assert (r*h+q*y*y)%modulus==1
            for x,base_s in product(range(modulus),repeat=2):
                if (x*x+y**3-h*base_s)%modulus:continue
                for T in range(modulus):
                    U=(h*T-beta*x)%modulus;G=(y*T+alpha*x)%modulus
                    a=y+U*U;b=base_s-h*G*G+2*U*y*G
                    W=(r*a+q*b)%modulus;V=(G-U*W)%modulus
                    assert (h*W-a)%modulus==(y*y*W-b)%modulus==0
                    assert (U**3+h*V-x)%modulus==(-U*U+h*W-y)%modulus==0
                    val=2*U**3*V+3*U**4*W+h*(V*V-3*U*U*W*W)+h*h*W**3
                    assert (val-base_s)%modulus==0 and (alpha*U+beta*(V+U*W)-T)%modulus==0
                    cases+=1
                    if math.gcd(h,modulus)>1 and math.gcd(y,modulus)>1:nonunit+=1
    assert nonunit>0
    return dict(residue_ring_parameters=cases,both_coefficients_nonunits=nonunit,universal_cusp_identity=True)

def metric():
    rng=np.random.default_rng(69052);cases=0
    for dim in range(2,7):
        for _ in range(12):
            B=np.eye(dim)+.2*rng.normal(size=(dim,dim));Q=B@np.diag([1]+[0]*(dim-1))@np.linalg.inv(B);R=np.eye(dim)-Q
            G=rng.normal(size=(dim,dim));G=G.T@G+np.eye(dim);H=Q.T@G@Q+R.T@G@R
            assert np.linalg.norm(Q.T@H@R)<1e-8
            eig=np.linalg.eigvals(np.linalg.solve(G,H)).real;lo,hi=min(eig),max(eig);assert lo>0
            for _ in range(5):
                v=rng.normal(size=dim);a=v@G@v;b=v@H@v;assert lo*a-1e-8<=b<=hi*a+1e-8
            cases+=1
    f=[0,0,1,2,2];dist=[[abs(a-b) for b in f] for a in f]
    for i,j,k in product(range(5),repeat=3):
        assert dist[i][j]<=dist[i][k]+dist[k][j] and (dist[i][j]==0)==(f[i]==f[j])
    return dict(oblique_metric_models=cases,collapsed_pseudometric=True)

def transport():
    x,y,z,t,b,t0=s.symbols('x y z t b t0');coords=[x,y,z]
    P=s.Matrix([[1,0,0],[0,1,0],[y,0,0]]);Q=s.eye(3)-P
    A=s.Matrix([1,0,y]);B=s.Matrix([0,1,0]);e=s.Matrix([0,0,1])
    def bracket(a,b):return b.jacobian(coords)*a-a.jacobian(coords)*b
    assert Q*bracket(A,B)!=s.zeros(3,1)
    xi=z*A+z*z*B;f=x*y+z*z;g=x+z
    def connection(xi,e):return Q*bracket(xi,e)
    assert (connection(f*xi,e)-f*connection(xi,e)).applyfunc(s.expand)==s.zeros(3,1)
    assert (connection(xi,g*e)-(s.Matrix([s.diff(g,c) for c in coords]).dot(xi))*e-g*connection(xi,e)).applyfunc(s.expand)==s.zeros(3,1)
    S=s.Matrix([[1,t,b*t*t],[0,1,b*t],[0,0,1]])
    coeff=-s.diff(S,t)*S.inv();T=S*S.subs(t,t0).inv()
    assert (s.diff(T,t)+coeff*T).applyfunc(s.simplify)==s.zeros(3)
    assert T.subs(t,t0)==s.eye(3)
    assert (2*t*coeff.subs(t,t*t)).subs(t,0)==s.zeros(3)
    mid=s.symbols('mid')
    assert (T.subs(t0,mid)*T.subs({t:mid})-T).applyfunc(s.simplify)==s.zeros(3)
    return dict(nonintegrable_splitting_connection_rules=True,normalized_gauge_transport=True,critical_pullback=True)

def eigencharge():
    z=s.symbols('z');M=s.Matrix([[-4,-s.Rational(20,3),-5,-5],[1,1,0,0],[s.Rational(1,2),1,1,0],[s.Rational(1,6),s.Rational(1,2),1,1]])
    J=s.Matrix([[0,s.Rational(25,6),0,5],[-s.Rational(25,6),0,-5,0],[0,5,0,0],[-5,0,0,0]])
    cyclo=sum(z**j for j in range(5))
    assert M.charpoly(z).as_expr()==cyclo and M**5==s.eye(4) and J.det()==625 and M.T*J*M==J
    lines=s.Matrix([[1,k,s.Rational(k*k,2),s.Rational(k**3,6)] for k in range(4)])
    assert lines.det()==1
    # Toda's polynomial coefficients in the source normalization Z/5.
    q=s.Matrix([[(z-1)/5,(-3*z**3+9*z-16)/30,(z**3+2*z*z+3*z-1)/5,-1]])
    assert all(s.rem(s.together(a).as_numer_denom()[0],cyclo,z)==0 for a in q*M-z*q)
    lam=np.exp(2j*np.pi/5);t=.5/np.tan(np.pi/5)
    charge=np.array([lam-1,5*(t*t-5/6+1j*t/2),5*(-.5+1j*t),-5])
    matrix=np.vstack([np.eye(4)[0],np.eye(4)[1],charge.real,charge.imag])
    invnorm=np.linalg.norm(np.linalg.inv(matrix),2);rng=np.random.default_rng(69055)
    for _ in range(100):
        v=rng.normal(size=4);Z=charge@v
        assert np.linalg.norm(v)<=invnorm*(abs(v[0])+abs(v[1])+abs(Z))+1e-10
    return dict(cyclotomic_eigenvector=True,action_order=5,euler_determinant=625,inverse_norm=float(invnorm),norm_models=100)

def numerical_embedding():
    a,b=s.symbols('a b');out=[]
    for dims in [(3,0),(1,2)]:
        monomials=[a**i*b**j for i in range(dims[0]+1) for j in range(dims[1]+1)]
        def coeffs(f):
            p=s.Poly(s.expand(f),a,b);return s.Matrix([p.coeff_monomial(m) for m in monomials])
        def exptr(f):return sum(f**j/s.factorial(j) for j in range(4))
        linears=[a] if dims==(3,0) else [a+b,a+2*b]
        chars=[coeffs(exptr(sum(k*L for k,L in zip(ks,linears)))) for ks in product(range(4),repeat=len(linears))]
        test=s.Matrix.hstack(*chars);assert test.rank()==len(monomials)
        td=1+2*a+s.Rational(11,6)*a*a+a**3 if dims==(3,0) else (1+a)*(1+s.Rational(3,2)*b+b*b)
        top=a**dims[0]*b**dims[1]
        pair=s.Matrix([[s.Poly(s.expand(f.subs({a:-a,b:-b},simultaneous=True)*g*td),a,b).coeff_monomial(top) for g in monomials] for f in monomials])
        assert pair.det()!=0 and (test.T*pair).rank()==len(monomials)
        if dims==(1,2):assert s.Matrix.hstack(*[coeffs(exptr(k*(a+b))) for k in range(4)]).rank()==4<6
        out.append(dict(dimensions=dims,numerical_rank=len(monomials),euler_determinant=str(pair.det())))
    return out

if __name__=='__main__':
    start=time.perf_counter();checks={}
    for f in [interpolation,weighted,stabilization,lifting,metric,transport,eigencharge,numerical_embedding]:checks[f.__name__]=dict(status='pass',details=f())
    result=dict(batch='B069',status='pass',elapsed_seconds=round(time.perf_counter()-start,3),scope='Selected identities and finite models, not source headline or Lean certification.',checks=checks)
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
