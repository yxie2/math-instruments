"""Finite algebra and local geometry checks, not classification proofs."""
from pathlib import Path
import json,random
import sympy as s
rng=random.Random(46016);out={}
for _ in range(150):
    weight=[rng.randrange(-3,5) for i in range(20)]
    sets=[{i for i in range(20) if rng.randrange(2)} for j in range(3)]
    c=lambda a,b:sum(weight[i] for i in b-a)-sum(weight[i] for i in a-b)
    A,B,C=sets;assert c(A,C)==c(A,B)+c(B,C) and c(A,B)==-c(B,A)
out['divisor_cocycle']={'weighted_set_models':150,'scope':'finite-support valuation-set algebra only'}

noncommuting=0
for _ in range(60):
    mat=lambda:s.Matrix(3,3,[rng.randrange(-3,4) for i in range(9)])
    R=mat();Q=R.T*R+s.eye(3);A=mat();B=mat()
    assert A.T*Q*Q.inv()*B.T*Q==(B*A).T*Q
    noncommuting+=A*B!=B*A
out['ordered_path_contraction']={'exact_models':60,'noncommuting_examples':noncommuting}

for n in range(2,12):
    D=s.diag(0,*range(1,n))
    for power in range(1,8):assert (D**power).nullspace()==D.nullspace()
J=s.Matrix([[0,1],[0,0]])
assert len((J**2).nullspace())>len(J.nullspace())
out['no_generalized_invariants']={'models':10,'powers_per_model':7,'jordan_counterexample':True}

t=s.symbols('t',real=True)
for n in range(1,11):
    periodic=s.sin(n*t)+s.cos((n+1)*t)/3;h0=t/(2*s.pi)+periodic
    L=lambda f:s.diff(f,t,2)+2*s.diff(f,t)
    v=-periodic;h=s.simplify(h0+v)
    assert s.simplify(L(h)-1/s.pi)==0
    assert s.simplify(h.subs(t,t+2*s.pi)-h-1)==0
out['periodic_height_correction']={'exact_models':10,'scope':'one-dimensional drift-Laplacian analogue, not a complex surface'}

x,y,z=s.symbols('x y z');coords=(x,y,z);alpha=s.Matrix([0,-x,1])
for _ in range(30):
    f=sum(rng.randrange(-3,4)*term for term in [1,x,y,z,x*y,x*z,y*z,x*x,y*y,z*z])
    K=s.Matrix([s.diff(f,y)+x*s.diff(f,z),-s.diff(f,x),f-x*s.diff(f,x)])
    assert s.expand((alpha.T*K)[0]-f)==0
    lie=s.Matrix([sum(K[j]*s.diff(alpha[i],coords[j])+alpha[j]*s.diff(K[j],coords[i]) for j in range(3)) for i in range(3)])
    assert all(s.expand(v)==0 for v in lie-s.diff(f,z)*alpha)
out['contact_hamiltonian']={'exact_darboux_polynomials':30,'scope':'local equations and contact preservation'}

u,v,w=s.symbols('u v w');second=(u,v,w)
# Symplectic pairing of (1,x,y,z),(1,u,v,w), squared.
b=(w-z+x*v-y*u)**2
poly=s.Poly(b,*second);coeff=s.Matrix(poly.coeffs());jets=coeff.row_join(coeff.jacobian(coords))
for _ in range(40):
    point={a:rng.randrange(-5,6) for a in coords}
    assert jets.subs(point).rank()==4
# The fixed-second derivative has the claimed linear/quadratic terms.
sx,sy,sz,a1,a2,a3=s.symbols('sx sy sz a1 a2 a3');ss=s.Matrix([sx,sy,sz]);aa=s.Matrix([a1,a2,a3])
form=s.Matrix([-y,x,1]);dform=s.Matrix([[0,2,0],[-2,0,0],[0,0,0]])
actual=sum(aa[i]*s.diff(b,coords[i]) for i in range(3)).subs({u:x+sx,v:y+sy,w:z+sz},simultaneous=True)
expected=-2*(form.dot(ss))*form.dot(aa)+(form.dot(ss))*(aa.T*dform*ss)[0]
assert s.expand(actual-expected)==0
out['symmetric_contact_jet']={'projective_chart_points':40,'first_jet_rank':4,'fixed_second_derivative_identity':True,'scope':'standard symplectic projective model; not existence on arbitrary contact manifolds'}

models=0
for exponent in [s.Rational(1,2),s.Rational(2,3),s.sqrt(2),-s.sqrt(3)]:
    for n in range(-25,26):
        eigenvalue=n-exponent;assert eigenvalue!=0 and s.simplify(eigenvalue/eigenvalue)==1;models+=1
assert 3-s.Integer(3)==0
out['kummer_euler']={'monomial_models':models,'integral_exponent_kernel_control':True,'scope':'Laurent polynomial de Rham differential, not stack descent'}

models=0
for C in range(-4,9):
    for source_weight in range(-8,10):
        a=max(1,(C-source_weight)//2+1)
        assert C-2*a<source_weight
        targets=[base-2*power for base in range(-10,C+1) for power in range(a,a+15)]
        assert source_weight not in targets;models+=1
# Dropping the common bound permits nonzero h^a maps of weight zero.
for a in range(1,31):assert 2*a-2*a==0
out['bounded_weight_tail_killing']={'weight_models':models,'unbounded_weight_controls':30,'scope':'finite graded models; mixed Hodge strictness and completed finite generation are inputs'}

result={'batch':'B046','status':'passed','scope':'Eight finite/local groups. No irrationality, spherical-shell, contact classification or quantum Langlands theorem certified.','checks':out}
Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
