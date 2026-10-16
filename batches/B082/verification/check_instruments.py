"""Finite checks of selected mechanisms, with explicit negative controls."""
from itertools import combinations, permutations, product
from pathlib import Path
import json, math, time
import numpy as np
import sympy as sp
from scipy.linalg import eigh, expm
from scipy.integrate import quad
from scipy.special import ive, roots_hermitenorm
from scipy.stats import poisson

def annihilators(d):
    cs=[]
    for j in range(d):
        c=np.zeros((2**d,2**d))
        for m in range(2**d):
            if m>>j&1:c[m^(1<<j),m]=(-1)**((m&((1<<j)-1)).bit_count())
        cs.append(c)
    return cs
def normal_ordering():
    rng=np.random.default_rng(8201);cases=0
    for d in [4,5,6]:
        cs=annihilators(d);pairs=list(combinations(range(d),2));V=np.linalg.qr(rng.normal(size=(len(pairs),3))+1j*rng.normal(size=(len(pairs),3)))[0]
        B=[sum(np.conj(V[i,p])*cs[b]@cs[a] for i,(a,b) in enumerate(pairs)) for p in range(3)]
        H=sum(b.conj().T@b for b in B);sectors={k:[m for m in range(2**d) if m.bit_count()==k] for k in range(d+1)}
        W3=np.column_stack([(b.conj().T[:,1<<j])[sectors[3]] for b in B for j in range(d)])
        W4=np.column_stack([(b.conj().T@c.conj().T)[:,0][sectors[4]] for b in B for c in B])
        H3=H[np.ix_(sectors[3],sectors[3])];assert np.allclose(H3,W3@W3.conj().T)
        C3=W3@(W3.conj().T@W3-np.eye(3*d))@W3.conj().T;C4=W4@W4.conj().T
        def lift(C,k):
            ops=[]
            # Sector mask order matches the coefficient matrix order.
            for mask in sectors[k]:
                op=np.eye(2**d)
                for j in range(d):
                    if mask>>j&1:op=cs[j]@op
                ops.append(op)
            return sum(C[i,j]*ops[i].T@ops[j] for i,j in product(range(len(ops)),repeat=2))
        four=lift(C4,4);assert np.allclose(H@H,H+lift(C3,3)+four,atol=1e-10)
        assert np.linalg.norm(four)>1e-3 and not np.allclose(H@H,H+lift(C3,3)+2*four);cases+=1
    return dict(complex_pair_subspaces=cases,max_fock_dimension=64,ordered_pair_factor_control=True)

def pair_hamiltonian(Q,n):
    d=Q+1;states=list(combinations(range(d),n));outs=list(combinations(range(d),n-2));index={s:i for i,s in enumerate(outs)}
    H=np.zeros((len(states),len(states)))
    for p in range(2*Q-1):
        B=np.zeros((len(outs),len(states)))
        for col,s in enumerate(states):
            for a,b in combinations(range(n),2):
                i,j=s[a],s[b]
                if i+j!=p+1:continue
                falling=lambda q,k:math.factorial(q)/math.factorial(q-k)
                v=(i-j)*np.sqrt(falling(Q,i)*falling(Q,j)*math.factorial(p)/(Q*falling(2*Q-2,p)*math.factorial(i)*math.factorial(j)))
                remaining=tuple(x for x in s if x not in [i,j]);B[index[remaining],col]+=v*(-1)**(a+b-1)
        H+=B.T@B
    return H,states
def polynomial_kernel():
    cases=0
    for N in [2,3]:
        Q=3*(N-1);H,states=pair_hamiltonian(Q,N);e=eigh(H,eigvals_only=True);assert sum(abs(e)<1e-9)==1
        Hp,_=pair_hamiltonian(Q,N+1);assert min(eigh(Hp,eigvals_only=True))>1e-7
        z=sp.symbols('z:'+str(N));expr=sp.prod((z[j]-z[i])**3 for i,j in combinations(range(N),2));poly=sp.Poly(expr,*z)
        assert all(sp.degree(expr,x)==Q for x in z)
        swapped=expr.xreplace({z[0]:z[1],z[1]:z[0]});assert sp.expand(expr+swapped)==0
        v=np.array([float(poly.coeff_monomial(sp.prod(z[j]**s[j] for j in range(N))))/np.sqrt(math.prod(math.comb(Q,i) for i in s)) for s in states])
        assert np.linalg.norm(v)>0 and np.linalg.norm(H@v)<1e-9;cases+=1
    return dict(laughlin_flux_cases=cases,one_particle_above_has_no_zero_mode=True,independent_symbolic_zero_vectors=True)

def graph_domains():
    rng=np.random.default_rng(8203);sig=[np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.diag([1,-1])]
    for _ in range(40):
        v=rng.normal(size=3);S=sum(v[i]*sig[i] for i in range(3))/np.sqrt(2)
        assert np.allclose(S@S,np.dot(v,v)*np.eye(2)/2)
        assert abs(np.linalg.norm(-1j*S,2)-np.linalg.norm(v)/np.sqrt(2))<1e-12
    # D=-i sigma_x d/dx /sqrt(2)+x^2 sigma_z, psi=(exp(-x^2/2),0).
    # Piecewise smooth cosine cutoff is C1 and compactly supported; it has H1 regularity.
    errors=[]
    for R in [1.,2.,3.,4.]:
        def values(x):
            t=abs(x)/R
            if t<=1:return 1.,0.
            if t>=2:return 0.,0.
            return (1+np.cos(np.pi*(t-1)))/2,-np.sign(x)*np.pi*np.sin(np.pi*(t-1))/(2*R)
        def error(x):
            chi,dchi=values(x);f=np.exp(-x*x/2)
            # Orthogonal components of D((chi-1)psi).
            return ((chi-1)*f)**2+(x*x*(chi-1)*f)**2+((dchi-(chi-1)*x)*f)**2/2
        errors.append(quad(error,-12,12,points=[-2*R,-R,R,2*R],epsabs=1e-11)[0])
    assert all(errors[i+1]<errors[i] for i in range(3)) and errors[-1]<1e-4
    return dict(symbol_checks=40,cutoff_graph_errors=errors,unbounded_potential=True)

def collision_capacity():
    # A radial linear annular cutoff in k normal dimensions, Lipschitz and sufficient for H1 energy.
    k=9;sphere=2*np.pi**(k/2)/math.gamma(k/2);values=[]
    for eps in [.4,.2,.1,.05]:
        exact=sphere*(2**k-1)*eps**(k-2)/k
        numeric=quad(lambda r:sphere*r**(k-1)/eps**2,eps,2*eps)[0]
        assert abs(numeric-exact)<1e-10;values.append(exact)
    assert all(abs(values[i+1]/values[i]-2**-7)<1e-12 for i in range(3))
    rng=np.random.default_rng(8204)
    for _ in range(40):
        cut=rng.random(4);grad=rng.normal(size=(4,3));total=sum(np.prod(np.delete(cut,j))*grad[j] for j in range(4))
        assert np.linalg.norm(total)<=sum(np.linalg.norm(g) for g in grad)+1e-12
    # d/dx sign(x)=0 off {0}, but its distributional derivative pairs with phi as 2phi(0).
    jump=-quad(lambda x:np.sign(x)*(-2*x)*np.exp(-x*x),-10,10,points=[0])[0]
    assert abs(jump-2)<1e-10
    return dict(codimension_nine_energies=values,product_cutoffs=40,codimension_one_jump_control=True)

def factorial_marks():
    def cycles(p):
        seen=set();out=[]
        for i in range(len(p)):
            if i in seen:continue
            c=set();j=i
            while j not in c:c.add(j);seen.add(j);j=p[j]
            out.append(c)
        return out
    count=0
    for p in permutations(range(4)):
        for mask in range(16):
            pins={j for j in range(4) if mask>>j&1};old=sum(not(c&pins) for c in cycles(p))
            for a,b in combinations(range(4),2):
                pp=list(p);pp[a],pp[b]=pp[b],pp[a];new=sum(not(c&pins) for c in cycles(pp));assert new-old<=1;count+=1
    # Dependent weight W(n1,n2)=2 if total count is even, otherwise 1; every insertion ratio <=2.
    lam=[.4,.7];K=22;raw=np.array([[poisson.pmf(i,lam[0])*poisson.pmf(j,lam[1]) for j in range(K)] for i in range(K)])
    W=lambda i,j:2 if (i+j)%2==0 else 1
    Z=sum(raw[i,j]*W(i,j) for i,j in product(range(K),repeat=2));cases=0
    for a,b in [(1,0),(0,1),(2,0),(1,1),(2,1),(0,3)]:
        fall=lambda n,r:math.prod(range(n-r+1,n+1)) if n>=r else 0
        lhs=sum(raw[i,j]*W(i,j)*fall(i,a)*fall(j,b) for i,j in product(range(K),repeat=2))/Z
        rhs=lam[0]**a*lam[1]**b*sum(raw[i,j]*W(i+a,j+b) for i,j in product(range(K),repeat=2))/Z
        assert abs(lhs-rhs)<1e-11 and lhs<=2**(a+b)*lam[0]**a*lam[1]**b+1e-11;cases+=1
    return dict(cycle_pin_insertions=count,weighted_poisson_factorial_cases=cases,tail_mass_bound=float(poisson.sf(K-1,sum(lam))))

def ideal_returns():
    coeff=[]
    for rates in [[1,1,1],[.3,1.2,2.1]]:
        rates=np.array(rates);kappa=(4*np.pi)**-1.5/np.sqrt(np.prod(rates));errors=[]
        for t in [10,100,1000]:
            p=np.prod(ive(0,2*t*rates));errors.append(abs(t**1.5*p/kappa-1))
        assert errors[2]<errors[1]<errors[0] and errors[-1]<.001;coeff.append(errors)
    m=3;site=np.array([[.7,.3],[.3,.7]]);slot=np.ones((m,m))/m;step=np.kron(site,slot);words=0
    for n in range(1,5):
        for word in product([1,-1],repeat=n):
            W=np.eye(2*m)
            for d in word:W=(step if d==1 else step.T)@W
            assert abs(W[0,0]-np.linalg.matrix_power(site,n)[0,0]/m)<1e-12;words+=1
    perm=np.roll(np.eye(m),1,axis=0);assert np.allclose(perm.T@perm,np.eye(m)) and not np.allclose(slot@slot,np.eye(m))
    # Replacing nearest-neighbor jumps by doubled jumps preserves return probabilities but multiplies sqrt(det D) by 8.
    assert abs(np.sqrt(np.linalg.det(4*np.eye(3)))-8)<1e-12
    return dict(anisotropic_relative_errors=coeff,direction_words=words,fixed_inverse_seam_control=True,proper_sublattice_factor=8)

def covariance_normalization():
    rng=np.random.default_rng(8207);cases=0
    sqrt=lambda A:(lambda e,V:(V*np.sqrt(np.maximum(e,0)))@V.T)(*eigh(A))
    for d in [2,4,8]:
        for _ in range(10):
            A=rng.normal(size=(d,d));B=rng.normal(size=(d,d));S=A@A.T;T=B@B.T
            assert np.sum((sqrt(S)-sqrt(T))**2)<=sum(abs(eigh(S-T,eigvals_only=True)))+1e-9;cases+=1
    v=rng.normal(size=(7,4));v/=np.linalg.norm(v,axis=1)[:,None];E=[0,1,2,3,4];F=[1,2,3,4,5];n=len(E)
    P=lambda E:sum(np.outer(v[g],v[g]) for g in E)/n
    PE,PF=P(E),P(F);assert abs(np.sum(sqrt(PE)**2)-1)<1e-12
    assert np.sum((sqrt(PE)-sqrt(PF))**2)<=len(set(E)^set(F))/n+1e-12
    R=v@v.T;W=rng.normal(size=4);xi=v@W;co=[.7,-.2,.3];BP=sum(c*np.linalg.matrix_power(PE,j+1) for j,c in enumerate(co));words=0.
    for r,c in enumerate(co,1):
        for g in product(E,repeat=r):words+=c/n**r*math.prod(R[g[j],g[j+1]] for j in range(r-1))*(xi[g[0]]*xi[g[-1]]-R[g[-1],g[0]])
    assert abs(words-(W@BP@W-np.trace(BP)))<1e-12
    nodes,weights=roots_hermitenorm(100);weights/=np.sqrt(2*np.pi)
    ev=np.array([.4,-.2,.1])
    for s in [.2,.5,1.]:
        numeric=np.prod([np.sum(weights*np.exp(1j*s*l*(nodes**2-1))) for l in ev]);exact=np.prod((1+4*s*s*ev**2)**-.25)
        assert abs(abs(numeric)-exact)<1e-10 and exact<=(1+4*s*s*np.sum(ev*ev))**-.25+1e-12
    return dict(noncommuting_trace_inequalities=cases,overlapping_frame_bound=True,covariance_word_identity=True,gaussian_characteristic_tests=3,variance_for_identity_over_n=[2/n for n in [1,4,100]])

def tracial_transfer():
    rng=np.random.default_rng(8208)
    for _ in range(30):
        X=rng.normal(size=(4,4))+1j*rng.normal(size=(4,4));X=(X+X.conj().T)/2
        Y=rng.normal(size=(4,4))+1j*rng.normal(size=(4,4));Y=(Y+Y.conj().T)/2;t=rng.uniform(-2,2)
        assert np.linalg.norm(expm(1j*t*X)-expm(1j*t*Y),'fro')<=abs(t)*np.linalg.norm(X-Y,'fro')+1e-10
    # Growing-norm diagonal matrices with a vanishing weighted atom; all fixed moments converge to q_0=0.
    for j in [3,5,8,12]:
        mass=np.exp(-j*j);xs=np.array([0.,float(j)]);weights=np.array([1-mass,mass])
        for d in range(5):
            r=4;K=j/2;lhs=sum(w*abs(x)**d for x,w in zip(xs,weights) if abs(x)>K);rhs=np.dot(weights,xs**(2*r))*K**(d-2*r)
            assert lhs<=rhs+1e-12
        for t in [.2,1.]:assert abs(np.dot(weights,np.exp(1j*t*xs))-1)<=2*mass+1e-15
    # Convex extension uses the affine squared error and convex absolute Fourier value.
    for _ in range(30):
        w=rng.dirichlet(np.ones(6));z=rng.normal(size=6)+1j*rng.normal(size=6);error=rng.random(6)
        assert abs(w@z)<=max(abs(z))+1e-12 and w@error<=max(error)+1e-12
    return dict(noncommuting_duhamel_cases=30,growing_norm_spectral_laws=4,convex_mixtures=30,sequential_compactness_not_numerically_proved=True)

if __name__=='__main__':
    start=time.perf_counter();checks={}
    for f in [normal_ordering,polynomial_kernel,graph_domains,collision_capacity,factorial_marks,ideal_returns,covariance_normalization,tracial_transfer]:checks[f.__name__]=dict(status='pass',details=f())
    result=dict(batch='B082',status='pass',elapsed_seconds=round(time.perf_counter()-start,3),scope='Selected finite mechanisms and analytic toy examples; no source headline or Lean certification.',checks=checks)
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8');print(json.dumps(result))
