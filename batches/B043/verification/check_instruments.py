"""Finite models of selected operator and evolution arguments; no global theorem check."""
import json
from pathlib import Path
import numpy as np
import sympy as s
rng=np.random.default_rng(43016); out={}

# Factorization checks do not test infinite-dimensional density.
err=0.
for n in range(2,12):
    U,_=np.linalg.qr(rng.normal(size=(n,n)))
    A=np.diag(.8**np.arange(n))@U
    H=np.diag(.5**np.arange(n)); B=np.linalg.solve(A,H)
    x=rng.normal(size=n)
    err=max(err,np.linalg.norm(A@B-H),np.linalg.norm(B@np.linalg.solve(H,A@x)-x))
assert err<1e-9
out['annulus_factorization']={'models':10,'maximum_error':float(err),'scope':'finite factorization and preimage identity only'}

# Exact atom-isolating polynomials detect negative and nonreal masses.
tests=0
for n in range(2,10):
    nodes=list(range(n)); masses=[s.Rational(i+1,n) for i in nodes]
    for j in nodes:
        values=[s.prod(s.Rational(x-k,j-k) for k in nodes if k!=j) for x in nodes]
        assert values==[s.Integer(i==j) for i in nodes]
        assert sum(v*v*c for v,c in zip(values,masses))==masses[j]
        bad=masses.copy();bad[j]=-1
        assert sum(v*v*c for v,c in zip(values,bad))==-1
        bad[j]=s.I
        assert sum(v*v*c for v,c in zip(values,bad))==s.I
        tests+=1
out['positive_moments']={'atom_tests':tests,'negative_and_complex_controls':True,'scope':'finite support; no polynomial-density test'}

err=0.
for _ in range(120):
    y=rng.normal(size=(20,2));z=rng.normal(size=(20,2));h=rng.uniform(0,2,20)
    g=lambda a:np.sin(a[:,0])+np.cos(a[:,1])
    grad=np.column_stack([np.cos(z[:,0]),-np.sin(z[:,1])])
    delta=y-z; bound=.5*np.sum(delta**2,axis=1)
    assert np.all(abs(g(y)-g(z)-np.sum(grad*delta,axis=1))<=bound+1e-12)
    hg=g(y)+rng.uniform(-.5,.5,20)*h
    assert np.all(hg<=g(z)+np.sum(grad*delta,axis=1)+bound+.5*h+1e-12)
    v=rng.normal(size=20)
    assert np.linalg.norm((hg-g(y))*v)<=.5*np.linalg.norm(h*v)+1e-12
out['commuting_taylor']={'models':120,'scope':'diagonal common-spectral models; global envelope assumed'}

nonreducing=0
for _ in range(100):
    a=rng.uniform(.1,1.4);b=rng.uniform(.1,1.4)
    J=np.array([[np.cos(a),0],[np.sin(a),0],[0,np.cos(b)],[0,np.sin(b)]])
    A=np.array([1.,2.,3.,4.]);B=np.array([2.,4.])
    for t in np.arange(0,4.6,.25):
        assert np.linalg.norm((A>t)[:,None]*J*(B<=t)[None,:])<1e-12
    P=J@J.T
    nonreducing+=np.linalg.norm(np.diag(A)@P-P@np.diag(A))>1e-8
    for power in [.1,.3,.5,.9,1,1.5,2,3,5,8]:
        v=rng.normal(size=2)
        assert np.linalg.norm(A**power*(J@v))<=np.linalg.norm(B**power*v)+1e-8
# Ordinary positive matrix order is weaker than the needed band condition.
A=np.array([[1.,0],[0,0]]);B=A+np.array([[1.,1],[1,1]])
assert np.linalg.eigvalsh(B-A).min()>-1e-12
assert np.linalg.eigvalsh(B@B-A@A).min()<-.1
out['spectral_tail_powers']={'models':100,'powers_per_model':10,'nonreducing_ranges':int(nonreducing),'ordinary_order_counterexample':True}

for n in range(2,16):
    c=rng.normal(size=n)
    for m in range(1,n+1):
        # X=l1^n, functionals the coordinate vectors in linfinity^n.
        assert np.max(abs(c[:m]))<=np.max(abs(c))+1e-12
    T=rng.normal(size=(n,n+3)); inv=T.T@np.linalg.inv(T@T.T)
    z=rng.normal(size=n);res=z.copy();x=np.zeros(n+3)
    for _ in range(45):
        step=.5*inv@res;x+=step;res-=T@step
    assert np.linalg.norm(T@x-z)<1e-10
out['evaluation_surjection']={'finite_models':14,'scope':'coordinate normers and residual-halving surjection; not the infinite-dimensional criterion'}

for epsilon in [.1,.01,.001]:
    start=int(np.ceil(2/epsilon)); indices=np.arange(start,start+100)
    assert max(np.max(1/indices),np.max(2/indices))<=epsilon+1e-15
    # A finite window of the compact diagonal operators diag(1/n),diag(2/n).
out['small_restriction']={'tail_models':3,'simultaneous_operators':2,'scope':'compact diagonal examples, not a finite test for strict singularity'}

for j in range(1,81):
    M=s.Integer(5+j%7);t=s.Rational(j%17,3)+s.I*s.Rational(j%5,2)
    if t==M:t+=s.Rational(1,2)
    z=s.I*s.Rational(1+j%13,3)
    B=s.Rational(j%11-5,3)+s.I*s.Rational(j%7-3,2)
    C=s.Rational(j%5-2,2)+s.I*s.Rational(j%9-4,3)
    B1=(t*B+z*C)/(t-M);C1=C-B1;g=B-B1
    flux=lambda b,c:M*s.expand_complex(b*s.conjugate(b))/2+s.re(z*s.conjugate(b)*c)
    difference=flux(B1,C1)-flux(B,C)-(s.re(t)-M/2)*g*s.conjugate(g)
    assert s.simplify(s.expand_complex(difference))==0
    R=-z/M+(z/M)*s.Rational(j%9,10)
    assert s.simplify(flux(R,s.Integer(1)))<0
out['laguerre_flux']={'exact_recurrence_models':80,'disk_models':80,'scope':'quadratic identity and disk algebra, not rapid tail decay'}

# Backward summation includes a neutral D eigenvalue 1.
N=90;D=np.array([1.,2.,4.]);forcing=np.array([.01,.02,-.01]);checks=[]
for w0 in [.01,.03,.05]:
    w=np.zeros(N+1);w[0]=w0;u=np.zeros((N+1,3))
    for iteration in range(100):
        f=np.array([forcing*.3**n+.01*(w[n]**2+np.dot(u[n],u[n])) for n in range(N)])
        un=np.zeros_like(u)
        for n in range(N-1,-1,-1):un[n]=(un[n+1]-f[n])/D
        wn=np.zeros_like(w);wn[0]=w0
        for n in range(N):wn[n+1]=.125*w[n]+.01*np.sum(u[n])
        change=max(np.max(abs(wn-w)),np.max(abs(un-u)));w,u=wn,un
        if change<1e-15:break
    for n in range(N):
        f=forcing*.3**n+.01*(w[n]**2+np.dot(u[n],u[n]))
        assert np.linalg.norm(u[n+1]-D*u[n]-f)<1e-13
        assert abs(w[n+1]-.125*w[n]-.01*np.sum(u[n]))<1e-13
    assert max(2.**n*(abs(w[n])+np.linalg.norm(u[n])) for n in range(N+1))<.2
    checks.append(iteration+1)
out['neutral_stable_graph']={'finite_horizon':N,'models':3,'iterations':checks,'scope':'finite backward boundary model, no PDE or infinite-horizon proof'}

result={'batch':'B043','status':'passed','scope':'Eight finite model groups. No source headline theorem, infinite-dimensional limit or Lean proof certified.','checks':out}
Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
