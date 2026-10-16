"""Finite checks of selected operator mechanisms, not source headline theorems."""
from itertools import product
from pathlib import Path
import json
import time
import numpy as np
from scipy.linalg import expm, polar

RNG=np.random.default_rng(62016)

def rand(n): return RNG.normal(size=(n,n))+1j*RNG.normal(size=(n,n))
def norm(a): return np.linalg.norm(a,2)
def phi(a,r): return float(np.trace(r@a).real)
def sn(a,r): return np.sqrt(max(0,phi(a.conj().T@a,r)))
def clip(a,k):
    u,s,v=np.linalg.svd(a); return (u*np.minimum(s,k))@v

def absorption():
    cases=0; error=0.0
    for p in (2,3,5):
        w=np.exp(2j*np.pi/p); U=np.diag(w**np.arange(p)); V=np.roll(np.eye(p),1,axis=0)
        G=list(product(range(p),repeat=2)); mats={g:np.linalg.matrix_power(U,g[0])@np.linalg.matrix_power(V,g[1]) for g in G}
        for h,g in product(G,repeat=2):
            hg=((h[0]+g[0])%p,(h[1]+g[1])%p)
            nu=w**(-h[1]*g[0]); alpha=w**(h[0]*g[1])
            lhs=alpha*mats[hg].conj().T@mats[h]@mats[g]
            error=max(error,norm(lhs-alpha*nu*np.eye(p)))
            # Nontrivial ancillary operator commutes with each amplified v_g.
            b=np.kron(np.eye(p),np.array([[0,1],[1,0]])); t=np.kron(mats[g].conj().T,np.eye(2))
            assert norm(t@b@t.conj().T-b)<1e-12
            cases+=1
    assert error<1e-12
    return dict(block_intertwining_identities=cases,max_residual=error)

def red(w):
    s=[]
    for x in w:
        if s and s[-1]==-x: s.pop()
        else: s.append(x)
    return tuple(s)

def germs():
    words=[()]
    for _ in range(5): words += [w+(x,) for w in list(words) if len(w)==_ for x in (1,-1,2,-2) if not w or w[-1]!=-x]
    tests=0
    for w in words:
        if not w: continue
        inv=tuple(-x for x in reversed(w))
        for k in range(1,6):
            assert any(red(w+(a,)*k+inv)!=(a,)*k for a in (1,2)); tests+=1
    # In any finite group all germs agree after restricting to the trivial subgroup.
    # S3 has nontrivial inner automorphisms, so inner-germ injectivity fails there.
    from itertools import permutations
    S=list(permutations(range(3))); mul=lambda a,b:tuple(a[b[i]] for i in range(3))
    assert any(mul(a,b)!=mul(b,a) for a,b in product(S,repeat=2))
    return dict(free_word_power_tests=tests,finite_non_icc_control='S3 inner automorphisms collapse as germs',scope='Bounded word checks, not a test of all finite-index subgroups.')

def intertwiners():
    err=0.0; cases=0
    for d,k in ((2,2),(3,2),(2,3)):
        n=d*k
        for _ in range(15):
            h=rand(n); h=(h+h.conj().T)/2; u=expm(.01j*h/norm(h))
            b=rand(k); b=(b+b.conj().T)/2; p=np.eye(k)+.015*b/norm(b)
            t=u@np.kron(np.eye(d),p); up,pos=polar(t)
            assert norm(up-u)<1e-12
            assert norm(up-np.eye(n))<=2*norm(t-np.eye(n))+1e-12
            for _ in range(5):
                a=np.kron(rand(d),np.eye(k)); theta=u@a@u.conj().T
                err=max(err,norm(t@a-theta@t),norm(up@a-theta@up))
            cases+=1
    assert err<1e-11
    return dict(models=cases,max_intertwining_error=err,scope='Explicit intertwiner and polar step only; no cb norm computed.')

def index(u,v):
    w=u@v@u.conj().T@v.conj().T; ev=np.linalg.eigvals(w)
    return float(np.angle(ev).sum()/(2*np.pi)),float(np.min(abs(ev+1)))

def clock_shift():
    err=0.0; points=0
    for n in (3,4,5,8,12,20,40,64):
        w=np.exp(2j*np.pi/n); u=np.diag(w**np.arange(n)); v=np.roll(np.eye(n),1,axis=0)
        assert abs(norm(u@v-v@u)-abs(w-1))<1e-12
        a=rand(n); a=(a+a.conj().T)/2; a=.01*a/norm(a)
        b=rand(n); b=(b+b.conj().T)/2; b=.01*b/norm(b)
        for s in np.linspace(0,1,7):
            z,gap=index(u@expm(1j*s*a),v@expm(1j*s*b)); err=max(err,abs(z-1)); assert gap>.9; points+=1
        z,_=index(u,np.diag(np.exp(1j*RNG.normal(size=n)))); assert abs(z)<1e-12
    assert err<1e-11
    return dict(path_points=points,max_index_error=err)

def free_prefix():
    cases=0
    for m in range(1,5):
        words=[()]; frontier=[()]
        for _ in range(3):
            frontier=[w+(x,) for w in frontier for x in range(-m,m+1) if x and (not w or w[-1]!=-x)]
            words+=frontier
        outputs=sorted(set(red((i,)+w) for i in range(1,m+1) for w in words)); oi={w:j for j,w in enumerate(outputs)}
        for _ in range(12):
            xi=RNG.normal(size=len(words))+1j*RNG.normal(size=len(words)); av=[]; bv=[]
            for i in range(1,m+1):
                a=np.zeros(len(outputs),complex); b=a.copy()
                for j,w in enumerate(words):
                    target=b if w and w[0]==-i else a
                    target[oi[red((i,)+w)]]+=xi[j]
                av.append(a); bv.append(b)
            for i in range(m):
                for j in range(i): assert abs(np.vdot(av[i],av[j]))<1e-10
            q=np.linalg.norm(xi)
            assert np.linalg.norm(sum(av))<=np.sqrt(m)*q+1e-10
            assert np.linalg.norm(sum(bv))<=np.sqrt(m)*q+1e-10
            assert np.linalg.norm(sum(av)+sum(bv))<=2*np.sqrt(m)*q+1e-10; cases+=1
    return dict(vectors=cases,scope='Full images of supported vectors; no truncation at the output boundary.')

def gns_products():
    err=0.0
    for d in range(2,10):
        f=np.exp(2j*np.pi*np.outer(np.arange(d),np.arange(d))/d)/np.sqrt(d)
        ps=[np.diag(np.eye(d)[i]) for i in range(d)]; qs=[f@p@f.conj().T for p in ps]
        r=np.column_stack([(d*p@q).reshape(-1)/np.sqrt(d) for p,q in product(ps,qs)])
        l=np.column_stack([(d*q@p).reshape(-1)/np.sqrt(d) for p,q in product(ps,qs)])
        err=max(err,norm(r.conj().T@r-np.eye(d*d)),norm(l.conj().T@l-np.eye(d*d)))
        assert norm(ps[0]@qs[0]-qs[0]@ps[0])>0.1
        for q in qs: assert norm(np.diag(np.diag(q))-np.eye(d)/d)<1e-12
        assert norm(l.conj().T@r)<=1+1e-12
    assert err<1e-11
    return dict(dimensions=list(range(2,10)),max_gram_error=err)

def moments():
    error=0.0; cases=0; rade=False; truncated=0
    for _ in range(12):
        d=4; rho=np.diag(np.exp(-np.arange(d))); rho/=np.trace(rho)
        mask=np.abs(np.arange(d)[:,None]-np.arange(d)[None,:])<=1
        outmask=np.abs(np.arange(d)[:,None]-np.arange(d)[None,:])<=2
        zs=[rand(d)*mask for _ in range(3)]; p=RNG.random(3); p/=sum(p)
        a=sum(t*z.conj().T@z for t,z in zip(p,zs)); b=sum(t*z@z.conj().T for t,z in zip(p,zs))
        rhs=a@a+sum(t*z.conj().T@b@z for t,z in zip(p,zs))-sum(t*t*(z.conj().T@z)@(z.conj().T@z) for t,z in zip(p,zs))
        c=phi(a@a,rho)+sum(t*phi(z.conj().T@b@z,rho) for t,z in zip(p,zs))
        h=rand(d); h/=norm(h); gamma=sum(t*sn(h@z,rho)**2 for t,z in zip(p,zs)); k=2*np.sqrt(c/gamma)
        fourth=np.zeros((d,d),complex); small_errors={.5:[],1.:[],2.:[]}; filtered=[]
        for phases in product((1,1j,-1,-1j),repeat=3):
            z=sum(np.sqrt(t)*e*x for t,e,x in zip(p,phases,zs)); zz=z.conj().T@z; fourth+=zz@zz/64
            for cutoff in small_errors:
                zc=clip(z,cutoff); small_errors[cutoff].append(sn(z-zc,rho)**2)
                assert norm(zc)<=cutoff+1e-12
                if norm(z)>cutoff: truncated+=1
            v=clip(z,k)*outmask
            assert norm(v)<=d*k+1e-12
            assert sn(v-z,rho)<=sn(clip(z,k)-z,rho)+1e-12
            filtered.append(sn(h@v,rho)**2)
        error=max(error,norm(fourth-rhs))
        for cutoff,errs in small_errors.items(): assert np.mean(errs)<=c/cutoff**2+1e-10
        assert max(filtered)>=gamma/4-1e-10
        rademacher=np.zeros((d,d),complex)
        for es in product((1,-1),repeat=3):
            z=sum(np.sqrt(t)*e*x for t,e,x in zip(p,es,zs)); zz=z.conj().T@z
            rademacher+=zz@zz/8
        rade=rade or norm(rademacher-rhs)>1e-3; cases+=1
    assert error<1e-9 and rade and truncated>0
    return dict(nontracial_models=cases,phase_realizations=cases*64,max_fourth_moment_error=error,active_clippings=truncated,rademacher_extra_terms_detected=bool(rade))

def pinching():
    err=0.0; cases=0
    for d in (4,8,16):
        for _ in range(12):
            w=RNG.random(d)+.01; w/=sum(w); r=np.diag(w); x=rand(d); prev=x
            for size in (d,d//2,1):
                mask=(np.arange(d)[:,None]//size)==(np.arange(d)[None,:]//size); y=x*mask
                err=max(err,abs(phi(y,r)-phi(x,r)))
                assert sn(y,r)<=sn(prev,r)+1e-11
                assert abs(sn(x,r)**2-sn(y,r)**2-sn(x-y,r)**2)<1e-9
                assert np.linalg.norm((prev*mask)-y)<1e-12; prev=y
            assert norm(prev-np.diag(np.diag(x)))<1e-12; cases+=1
    r=np.diag([.8,.2]); q=np.ones((2,2))/2; z=np.diag([1.,0.]); y=q@z@q+(np.eye(2)-q)@z@(np.eye(2)-q)
    assert abs(phi(y,r)-phi(z,r))>.2
    return dict(models=cases,max_state_preservation_error=err,noncentralizer_control=True)

def multipliers():
    bad=[]; good=[]; cutoff=[]
    for n in (2,4,8,16,32):
        d=n+1; w=2.**(-np.arange(d)-1) # Compression of one fixed infinite-dimensional state; no renormalization.
        rho=np.diag(w); dn=np.zeros((d,d)); dn[n,n]=1; rn=np.zeros((d,d)); rn[n,0]=1
        bad.append(sn(dn@rn,rho)); good.append(sn(dn,rho))
        b=np.diag(RNG.uniform(-1,1,d)); assert sn(dn@b,rho)<=norm(b)*sn(dn,rho)+1e-12
        # Diagonal operators are in the centralizer; clipping preserves the tail support.
        u=np.diag(np.linspace(-2,2,d)); v=u+dn
        fu=np.diag(np.maximum(np.diag(u),0)); fv=np.diag(np.maximum(np.diag(v),0))
        cutoff.append(sn(fu-fv,rho)); assert sn(fu-fv,rho)<=sn(u-v,rho)+1e-12
    assert max(bad)-min(bad)<1e-12 and good[-1]<1e-4 and cutoff[-1]<1e-4
    return dict(corners=[3,5,9,17,33],state_null_norms=good,bad_product_norms=bad,cutoff_error_norms=cutoff,scope='Finite compressions of a fixed diagonal state; restricted to explicit models.')

def main():
    start=time.perf_counter(); checks={}
    for fn in (absorption,germs,intertwiners,clock_shift,free_prefix,gns_products,moments,pinching,multipliers):
        checks[fn.__name__]=fn(); print(fn.__name__,'passed',flush=True)
    result=dict(status='passed',elapsed_seconds=round(time.perf_counter()-start,3),checks=checks,scope='Selected finite mechanisms only; no arithmetic, universal stability, bicentralizer, modular recovery or paving headline certified.')
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='checks'}))

if __name__=='__main__': main()
