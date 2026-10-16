"""Finite matrix identities and conditional mechanisms for B018.

These checks do not certify infinite-dimensional operator-algebra claims.
"""
import itertools
import json
from math import log, pi, sqrt
from pathlib import Path
import sys
import numpy as np
import scipy
from scipy.integrate import quad
from scipy.linalg import block_diag, expm
from scipy.special import ndtr
from scipy.stats import chi2

RNG=np.random.default_rng(18288)
OUT={}


def matrix(m,n=None):
    n=m if n is None else n
    return RNG.normal(size=(m,n))+1j*RNG.normal(size=(m,n))


def hermitian(n):
    a=matrix(n)
    return (a+a.conj().T)/2


def positive_sqrt(a):
    values,vectors=np.linalg.eigh(a)
    return (vectors*np.sqrt(np.maximum(values,0)))@vectors.conj().T


def op(a):
    return np.linalg.norm(a,2)


def trace_norm(a):
    return np.linalg.svd(a,compute_uv=False).sum()


def close(a,b,tol=2e-9):
    assert np.linalg.norm(np.asarray(a)-np.asarray(b))<=tol*(1+np.linalg.norm(b))


def metric_checks():
    cases=0
    for n,f,k in itertools.product((2,3),(1,2,3),(1,2,3)):
        for _ in range(4):
            nf,nk=n*f,n*k
            v=matrix(nf,nk);d=.5+op(v)
            ti=np.block([[np.eye(nf),-v/d],[np.zeros((nk,nf)),np.eye(nk)]])
            cf=matrix(f);cf=cf.conj().T@cf+np.eye(f)
            ck=matrix(k);ck=ck.conj().T@ck+np.eye(k)
            c=block_diag(np.kron(np.eye(n),cf),np.kron(np.eye(n),ck))
            metric=ti.conj().T@c@ti
            recovered=-d*np.linalg.solve(metric[:nf,:nf],metric[:nf,nf:])
            close(recovered,v)
            def delta(a): return v@np.kron(a,np.eye(k))-np.kron(a,np.eye(f))@v
            def phi(a):
                return np.block([[np.kron(a,np.eye(f)),delta(a)/d],
                                 [np.zeros((nk,nf)),np.kron(a,np.eye(k))]])
            a,b=matrix(n),matrix(n)
            close(phi(a@b),phi(a)@phi(b))
            close(metric@phi(a),phi(a.conj().T).conj().T@metric)
            close(delta(a),recovered@np.kron(a,np.eye(k))-np.kron(a,np.eye(f))@recovered)
            assert op(recovered)<=d*op(metric)*op(np.linalg.inv(metric))+1e-8
            cases+=1
    OUT['triangular_metric']={'rectangular_models':cases,'cb_similarity_theorem_tested':False}


def cyclic_checks():
    cases=0;nonfaithful=0
    for n in range(2,7):
        for m in range(1,n+1):
            for h,singular in itertools.product((1,2,4),(False,True)):
                vectors=[matrix(n,m) for _ in range(h)]
                if singular and m>1:
                    for a in vectors: a[:,-1]=0
                scale=sqrt(sum(np.linalg.norm(a)**2 for a in vectors))
                vectors=[a/scale for a in vectors]
                rho=sum(a.conj().T@a for a in vectors)
                zeta=np.vstack([positive_sqrt(rho),np.zeros((n-m,m))])
                lifts=[a@np.linalg.pinv(zeta,rcond=1e-10) for a in vectors]
                close(np.linalg.norm(zeta),1)
                for a,v in zip(vectors,lifts): close(v@zeta,a,1e-7)
                assert op(np.vstack(lifts))<=1+1e-7
                cases+=1
    # A=M_n direct-sum M_n, sigma(a,b)=a, lambda(a,b)=b.
    for n,h in itertools.product((2,3,4),(1,2,4)):
        for _ in range(8):
            v=matrix(n);vdiag=np.kron(np.eye(h),v)
            xa,xb=matrix(n*h),matrix(n*h)
            wa,wb=matrix(n*h,n),matrix(n*h,n)
            dx=vdiag@xa-xb@vdiag
            dw=vdiag@wa-wb@v
            dxw=vdiag@xa@wa-xb@wb@v
            close(dx@wa,dxw-xb@dw)
            assert op(-v)>0  # Delta(0,I)=-V although sigma(0,I)=0.
            nonfaithful+=1
    # Scalar operators applied to one vector can never span this rank-two column pair.
    assert np.linalg.matrix_rank(np.eye(2)/sqrt(2))==2
    OUT['cyclic_columns']={'factorizations':cases,'nonfaithful_lift_identities':nonfaithful,
        'noncyclic_rank_control':True}


def density_checks():
    ps=0;purifications=0;gap=0
    for n in range(1,9):
        for rankx,ranky in itertools.product((1,n),(1,n)):
            for _ in range(6):
                a,b=matrix(n,rankx),matrix(n,ranky)
                x,y=a@a.conj().T,b@b.conj().T
                assert np.linalg.norm(x-y)**2<=trace_norm(x@x-y@y)+1e-8
                ps+=1
    paulis=[np.array([[0,1],[1,0]],complex),np.diag([1,-1])]
    for e in (2,3,5):
        for _ in range(40):
            xi=matrix(e,2);xi/=np.linalg.norm(xi)
            # Rows store K vectors, hence T=sum |row><row| = xi.T @ xi.conj().
            t=xi.T@xi.conj();root=positive_sqrt(t)
            deltas=[]
            for sigma in paulis:
                u=expm(1j*hermitian(e))
                changed=u@xi@sigma.T
                ts=changed.T@changed.conj()
                close(ts,sigma@t@sigma.conj().T)
                delta=np.linalg.norm(changed-xi);deltas.append(delta)
                assert trace_norm(ts-t)<=2*delta+1e-10
                assert np.linalg.norm(sigma@root@sigma.conj().T-root)**2<=trace_norm(ts-t)+1e-9
                purifications+=1
            dist2=np.linalg.norm(root-np.trace(root)*np.eye(2)/2)**2
            conjugation=sum(np.linalg.norm(s@root@s.conj().T-root)**2 for s in paulis)
            assert conjugation>=4*dist2-1e-9
            assert sum(d*d for d in deltas)>=16*dist2**2/8-1e-9
            gap+=1
    OUT['density_and_gap']={'powers_stormer_models':ps,'partial_trace_models':purifications,
        'invariant_component_subtracted_gap_models':gap,'full_weak_mixing_hypothesis_realized':False}


def varying_checks():
    spectral=0;perturbed=0
    for n in range(1,25):
        a=matrix(n);p=a.conj().T@a;p*=4/(1+op(p))
        close(np.linalg.eigvalsh(p)[0],4-op(4*np.eye(n)-p))
        spectral+=1
    omega=np.exp(2j*pi/3)
    for n,m,epsilon in itertools.product((1,2,4),(1,3,7,11),(.1,.01,.001)):
        # Actual representations of C3 in two different dimensions.
        u0=np.diag(omega**RNG.integers(0,3,size=n))
        representation=np.diag(omega**RNG.integers(0,3,size=m))
        h=hermitian(n);h/=max(1,op(h))
        u=expm(1j*epsilon*h)@u0
        z0=np.kron(u0,representation.conj());z=np.kron(u,representation.conj())
        identity=np.eye(n*m)
        p0=(z0-identity).conj().T@(z0-identity)
        p=(z-identity).conj().T@(z-identity)
        eig0=np.linalg.eigvalsh(p0)
        assert np.max(np.minimum(abs(eig0),abs(eig0-3)))<1e-9
        assert op(p-p0)<=2*op(z-z0)+1e-9
        close(op(z-z0),op(u-u0))
        minimum=np.linalg.eigvalsh(p)[0]
        assert min(abs(minimum),abs(minimum-3))<=2*op(u-u0)+1e-9
        perturbed+=1
    OUT['varying_dimensions']={'positive_spectral_minima':spectral,'perturbed_C3_models':perturbed,
        'largest_tensor_dimension':44,'ultrafilter_limit_tested':False}


def predecessor_checks():
    cyclic_models=0;admissible=0;representations=0
    for n in range(1,12):
        for a in range(n):
            pull=[a*j%n for j in range(n)]
            for mask in range(1,1<<n):
                selected={j for j in range(n) if mask>>j&1}
                cyclic_models+=1
                if not selected.issubset({pull[k] for k in selected}): continue
                admissible+=1
                for j in selected:
                    x=j
                    for p in range(1,len(selected)+1):
                        x=pull[x]
                        if x==j: break
                    else: raise AssertionError('Nonperiodic cyclic character')
                    representations+=1
    group=list(itertools.permutations(range(3)));identity=(0,1,2)
    def multiply(g,h): return tuple(g[h[i]] for i in range(3))
    index={g:i for i,g in enumerate(group)};e=index[identity]
    multiplication=[[index[multiply(g,h)] for h in group] for g in group]
    def power(g,k):
        out=e
        for _ in range(k): out=multiplication[out][g]
        return out
    r=index[(1,2,0)];s=index[(1,0,2)]
    words={(power(r,k),b):multiplication[power(r,k)][power(s,b)] for k in range(3) for b in range(2)}
    chars=[]
    for kind in range(3):
        values=[]
        for g in group:
            fixed=sum(i==g[i] for i in range(3))
            values.append(1 if kind==0 else (-1 if fixed==1 else 1) if kind==1 else fixed-1)
        chars.append(np.array(values,dtype=int))
    endomorphisms=0;s3_admissible=0;reducible=0
    for image_r,image_s in itertools.product(range(6),repeat=2):
        if power(image_r,3)!=e or power(image_s,2)!=e: continue
        if multiplication[multiplication[image_s][image_r]][image_s]!=power(image_r,2): continue
        theta=[None]*6
        for k,b in itertools.product(range(3),range(2)):
            theta[words[(power(r,k),b)]]=multiplication[power(image_r,k)][power(image_s,b)]
        assert all(theta[multiplication[g][h]]==multiplication[theta[g]][theta[h]] for g,h in itertools.product(range(6),repeat=2))
        coefficients=np.array([[int(np.dot(chars[i],chars[j][theta]))//6 for j in range(3)] for i in range(3)])
        for j in range(3):
            close(sum(coefficients[i,j]*chars[i] for i in range(3)),chars[j][theta])
            reducible+=int(coefficients[:,j].sum()>1)
        for mask in range(1,8):
            selected=[j for j in range(3) if mask>>j&1]
            if not all(any(coefficients[i,j]>0 for j in selected) for i in selected):continue
            s3_admissible+=1
            for i in selected:
                iterate=list(range(6))
                for p in range(1,len(selected)+1):
                    iterate=[theta[g] for g in iterate]
                    if np.array_equal(chars[i][iterate],chars[i]):break
                else:raise AssertionError('Nonperiodic S3 irreducible')
        endomorphisms+=1
    OUT['finite_predecessors']={'cyclic_subset_models':cyclic_models,'admissible_cyclic_sets':admissible,
        'periodic_character_checks':representations,'S3_endomorphisms':endomorphisms,
        'S3_admissible_sets':s3_admissible,'reducible_pullbacks':reducible}


def baire_checks():
    cases=0
    # A continuous column family with a discontinuous projection at a rank drop.
    for n in (2,3,5,8):
        q,_=np.linalg.qr(matrix(n));xi=q[:,-1]
        zero=q[:,:-1]@q[:,:-1].conj().T
        close(zero@xi,np.zeros(n))
        for t in (.5,.1,.01,.001):
            columns=q@np.diag([1]*(n-1)+[t])
            projection=columns@np.linalg.pinv(columns)
            close(projection@xi,xi)
            # Persistent correlation one forces discontinuity at t=0.
            close(abs(np.vdot(xi,xi)),1)
            for _ in range(10):
                a,b=matrix(n,1)[:,0],matrix(n,1)[:,0]
                assert abs(np.linalg.norm(projection@a)-np.linalg.norm(projection@b))<=np.linalg.norm(a-b)+1e-9
            cases+=1
    margins=0
    for s,fraction in itertools.product(np.geomspace(.001,2,30),(.1,.5,.9)):
        alpha=fraction*min(.25,s/32)
        ell=int(np.ceil(8/(alpha*s*s)))+1
        error=4*s*alpha*alpha/(1-2*alpha)+1/ell
        assert alpha*s*s/2-error>=alpha*s*s/8
        margins+=1
    OUT['conditional_generation']={'rank_drop_examples':cases,'fixed_amplitude_margins':margins,
        'Baire_or_factor_perturbation_theorem_tested':False}


def encoding_checks():
    cases=0
    for n in range(1,9):
        for degenerate in (False,True):
            for _ in range(8):
                a=[hermitian(n) for _ in range(4)]
                if degenerate:a[0]=2*np.eye(n);a[1]=-np.eye(n)
                c=op(a[0])+op(a[1])+1
                A=block_diag(a[0],a[1]+c*np.eye(n))
                B=np.block([[a[2],np.eye(n)],[np.eye(n),a[3]]])
                threshold=(op(a[0])+c-op(a[1]))/2
                values,vectors=np.linalg.eigh(A)
                e11=(vectors*(values<threshold))@vectors.conj().T
                close(e11,block_diag(np.eye(n),np.zeros((n,n))))
                e22=np.eye(2*n)-e11;e12=e11@B@e22;e21=e12.conj().T
                close(e12@e21,e11);close(e21@e12,e22)
                decoded=[e11@A@e11,e12@A@e21-c*e11,e11@B@e11,e12@B@e21]
                for actual,expected in zip(decoded,a):close(actual,block_diag(expected,np.zeros((n,n))))
                cases+=1
    OUT['matrix_encoding']={'random_and_degenerate_models':cases}


def hermitian_basis(n):
    result=[]
    for i in range(n):
        a=np.zeros((n,n),complex);a[i,i]=1;result.append(a)
    for i in range(n):
        for j in range(i+1,n):
            a=np.zeros((n,n),complex);a[i,j]=a[j,i]=1/sqrt(2);result.append(a)
            a=np.zeros((n,n),complex);a[i,j]=1j/sqrt(2);a[j,i]=-1j/sqrt(2);result.append(a)
    return result


def flow_checks():
    basis_cases=0;words=0;gaussian=0
    for n in range(1,7):
        basis=hermitian_basis(n)
        for _ in range(8):
            a=matrix(n);close(sum(e@a@e for e in basis),np.trace(a)*np.eye(n));basis_cases+=1
            tuple_=[hermitian(n) for _ in range(3)]
            for length in (1,2,4,6):
                word=RNG.integers(0,3,size=length)
                coordinate=int(RNG.integers(0,3))
                total=0j;expected=0j
                for position,x in enumerate(word):
                    if x!=coordinate:continue
                    left=np.eye(n,dtype=complex);right=np.eye(n,dtype=complex)
                    for k in word[:position]:left=left@tuple_[k]
                    for k in word[position+1:]:right=right@tuple_[k]
                    total+=sum(np.trace(e@left@e@right) for e in basis)/n**2
                    expected+=np.trace(left)*np.trace(right)/n**2
                close(total,expected);words+=1
    for n,d,v,t in itertools.product((1,3,7),(1,2,9),(.2,1,3),(.1,2)):
        # nd^2 real coordinates with covariance v/d.
        h0=n*d*d/2*log(2*pi*np.e*v/d)
        h1=n*d*d/2*log(2*pi*np.e*(v+t)/d)
        gain=(h1-h0)/d**2
        close(gain,.5*n*log((v+t)/v));gaussian+=1
    # A uniform bounded input, convolved with the same Gaussian along the flow.
    a=1.0
    def density_score(x,s):
        z1=(x+a)/sqrt(s);z0=(x-a)/sqrt(s)
        # Complementary-tail form avoids cancellation on the positive tail.
        density=(ndtr(-z0)-ndtr(-z1) if x>=0 else ndtr(z1)-ndtr(z0))/(2*a)
        derivative=(np.exp(-z1*z1/2)-np.exp(-z0*z0/2))/(2*a*sqrt(2*pi*s))
        return density,derivative
    def entropy(s):
        limit=a+11*sqrt(s)
        return quad(lambda x: -density_score(x,s)[0]*log(density_score(x,s)[0]),-limit,limit,epsabs=2e-10)[0]
    def fisher(s):
        limit=a+11*sqrt(s)
        return quad(lambda x: density_score(x,s)[1]**2/density_score(x,s)[0],-limit,limit,epsabs=2e-10)[0]
    epsilon,t=.2,1.3
    gain=entropy(t)-entropy(epsilon)
    integrated=quad(lambda s:.5*fisher(s),epsilon,t,epsabs=2e-9)[0]
    close(gain,integrated,2e-8)
    OUT['retained_ensemble_flow']={'basis_contractions':basis_cases,'noncommutative_word_derivatives':words,
        'exact_Gaussian_normalizations':gaussian,'uniform_input_entropy_gain':gain,
        'integrated_Fisher_gain':integrated,'free_limit_tested':False}


def event_checks():
    tails=0;blocks=0;lipschitz=0;binary=0
    for d,p in itertools.product((4,8,12),(2,3,4)):
        ranks=[d//p+(j<d%p) for j in range(p)]
        assert max(ranks)<=2*d/p
        dimension=sum(r*r for r in ranks)
        q=p*dimension
        assert q<=2*d*d
        mask=block_diag(*(np.ones((r,r)) for r in ranks))
        basis=hermitian_basis(d)
        projected_dimension=sum(np.linalg.norm(e*mask)**2 for e in basis)
        close(projected_dimension,dimension)
        for t in (.1,1,4):
            expected=t*p*projected_dimension/d**2
            assert expected<=2*t+1e-10
            blocks+=1
        for multiplier in (1,2,4,8):
            threshold=multiplier*q
            log_bound=q/2*log(2)-threshold/4
            probability=chi2.sf(threshold,q)
            assert probability<=min(1,np.exp(log_bound))+1e-14
            tails+=1
        D=[hermitian(d) for _ in range(p)]
        u=expm(1j*hermitian(d));v=expm(.01j*hermitian(d))@u
        delta=op(u-v)
        lhs=sqrt(sum(np.linalg.norm(u.conj().T@a@u-v.conj().T@a@v)**2/d for a in D))
        rhs=2*delta*sqrt(sum(np.linalg.norm(a)**2/d for a in D))
        assert lhs<=rhs+1e-9;lipschitz+=1
    for size in (3,6,10):
        for _ in range(80):
            mu=RNG.dirichlet(np.ones(size));gamma=RNG.dirichlet(np.ones(size))
            subset=RNG.choice(size,size//2,replace=False)
            alpha=mu[subset].sum();beta=gamma[subset].sum()
            kl=sum(mu*np.log(mu/gamma))
            binary_kl=alpha*log(alpha/beta)+(1-alpha)*log((1-alpha)/(1-beta))
            assert kl>=binary_kl-1e-12
            assert binary_kl>=alpha*log(1/beta)-log(2)-1e-12
            binary+=1
    for alpha in (.1,.5,.9,1):
        for logbeta in (-2,-10,-100,-230):
            beta=np.exp(logbeta)
            binary_kl=alpha*(log(alpha)-logbeta)
            if alpha<1:binary_kl+=(1-alpha)*(log(1-alpha)-np.log1p(-beta))
            assert binary_kl>=-alpha*logbeta-log(2)-1e-12
            binary+=1
    parameter_models=[]
    for v in (1,2,10):
        p=100000*int(v);d=10*p
        bracket=2*log(1+128*sqrt(v))+log(2)-p/(256*v)
        assert bracket<-8
        exponent=p*log(d+1)+d*d*bracket
        assert exponent<=-4*d*d
        parameter_models.append({'v':v,'p':p,'d':d,'bracket':bracket})
    OUT['structural_event']={'projected_noise_normalizations':blocks,'chi_squared_tail_bounds':tails,
        'unitary_conjugation_bounds':lipschitz,'binary_entropy_models':binary,
        'explicit_asymptotic_margins':parameter_models,'source_tuple_existence_tested':False}


if __name__=='__main__':
    for check in (metric_checks,cyclic_checks,density_checks,varying_checks,predecessor_checks,
                  baire_checks,encoding_checks,flow_checks,event_checks):
        check();print(check.__name__,'passed',flush=True)
    result={'batch':'B018','python':sys.version.split()[0],'numpy':np.__version__,'scipy':scipy.__version__,
        'checks':OUT,'scope':'Finite identities, conditional interfaces and numerical checks; no infinite-dimensional or Lean proof certification.'}
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(OUT,indent=2))
