"""Finite mechanism checks for B016; no global theorem or Lean certification."""
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, combinations_with_replacement, product
from math import ceil, log2, pi, prod, sin, sqrt
from pathlib import Path
import json
import random
import sys
import numpy as np

RNG = random.Random(1610278)
NP = np.random.default_rng(1610278)
OUT = {}


def close(a, b, tol=2e-9):
    assert np.max(np.abs(np.asarray(a)-np.asarray(b))) < tol, (a, b)


def unitary(n):
    a = NP.normal(size=(n,n))+1j*NP.normal(size=(n,n))
    q, r = np.linalg.qr(a)
    return q @ np.diag(np.diag(r)/np.abs(np.diag(r)))


def angle_checks():
    worst = 0.0
    for _ in range(500):
        a = RNG.uniform(.3, 3)
        da, dt = NP.normal(size=(2,3))
        la, theta, d = RNG.uniform(-3,3), RNG.uniform(-1.3,1.3), RNG.uniform(.1,3)
        c, s = np.cos(theta), np.sin(theta)
        lt = -2*np.dot(da,dt)/a-d*np.sin(2*theta)
        g, h = a*c, a*s
        dg, dh = c*da-a*s*dt, s*da+a*c*dt
        lg = c*la-2*s*np.dot(da,dt)-a*c*np.dot(dt,dt)-a*s*lt
        lh = s*la+2*c*np.dot(da,dt)-a*s*np.dot(dt,dt)+a*c*lt
        v = la/(2*a)-np.dot(dt,dt)/2+d*s*s
        residual = max(abs(-lg/2+v*g), abs(-lh/2+v*h-d*h))
        worst = max(worst, residual)
        close(np.dot(dg,dg)+np.dot(dh,dh), np.dot(da,da)+a*a*np.dot(dt,dt))
        assert residual < 2e-12
    # Reflection-paired samples with constant |theta| give the exact mass split.
    for size in range(1, 21):
        weights = NP.random(size)
        weights *= 1.5/weights.sum()
        theta = np.arcsin(1/sqrt(3))
        g = np.sqrt(np.tile(weights,2))*np.cos(theta)
        h = np.sqrt(np.tile(weights,2))*np.r_[np.full(size,np.sin(theta)),np.full(size,-np.sin(theta))]
        close([g@g,h@h,g@h],[2,1,0])
    OUT['angle_orbitals'] = {'local_derivative_models':500,'paired_normalizations':20,'max_equation_residual':worst}


def ensemble_checks():
    m, n = 6, 3
    basis = list(combinations(range(m),n))
    lower = list(combinations(range(m),n-1))
    index = {v:i for i,v in enumerate(lower)}
    annih = []
    for i in range(m):
        a = np.zeros((len(lower),len(basis)))
        for j,v in enumerate(basis):
            if i in v:
                a[index[tuple(x for x in v if x!=i)],j] = (-1)**v.index(i)
        annih.append(a)
    h = np.diag([0,0,1,1.5,2,4])
    cases = 0
    for rank in (1,2,7,20):
        for _ in range(20):
            x = NP.normal(size=(20,rank))+1j*NP.normal(size=(20,rank))
            rho = x@x.conj().T
            rho /= np.trace(rho)
            gamma = np.array([[np.trace(rho @ annih[j].T @ annih[i]) for j in range(m)] for i in range(m)])
            close(gamma,gamma.conj().T)
            close(np.trace(gamma),3)
            ev = np.linalg.eigvalsh(gamma)
            assert ev.min()>-1e-12 and ev.max()<1+1e-12
            assert np.trace(gamma@h).real >= 1-1e-12
            # Independent second-quantized energy calculation.
            many_h = sum(h[i,i]*(annih[i].T@annih[i]) for i in range(m))
            close(np.trace(rho@many_h), np.trace(gamma@h))
            cases += 1
    rho = np.zeros((20,20)); rho[basis.index((0,1,2)),basis.index((0,1,2))]=1
    close(np.trace(rho@many_h),1)
    graphcases = 0
    for m in range(3,9):
        for _ in range(10):
            g = NP.uniform(.3,2,m); g *= sqrt(2)/np.linalg.norm(g)
            weights = NP.uniform(.1,2,(m,m)); weights = (weights+weights.T)/2
            np.fill_diagonal(weights,0)
            lap = np.diag(weights.sum(axis=1))-weights
            h = np.diag(1/g)@lap@np.diag(1/g)
            f = NP.normal(size=m)+1j*NP.normal(size=m)
            xi = f/g
            form = sum(weights[i,j]*abs(xi[i]-xi[j])**2 for i in range(m) for j in range(i+1,m))
            close(np.vdot(f,h@f),form)
            gap = np.linalg.eigvalsh(h)[1]
            assert form+1e-9 >= gap*(np.vdot(f,f).real-abs(np.vdot(g,f))**2/2)
            graphcases += 1
    OUT['ensemble_certificate'] = {'arbitrary_wedge_density_matrices':cases,'wedge_dimension':20,
        'saturating_determinant':True,'weighted_graph_transforms':graphcases}


def floor_fraction(x):
    return x.numerator//x.denominator


def completion(s,z,w,t):
    delta = F(1,2**t)
    a = (1-delta)*s
    e = w+t+2
    c = F(floor_fraction(2**e*z/a),2**e)
    r = z-c*a
    guess = r*2**w/delta
    assert 0<=c<=1 and 0<=guess<=F(1,4)
    assert c*a+delta*F(1,2**w)*guess == z
    for x in (c,guess):
        assert x.denominator & (x.denominator-1) == 0
    return c,guess


def calibration_checks():
    cases = quarters = 0
    nondyadic = 0
    for w,t,k in product(range(1,8),range(1,6),range(2,8)):
        s = F(RNG.randrange(1,2**k+1),2**k)
        a = (1-F(1,2**t))*s
        scale = 2**(k+t+4)
        z = F(RNG.randrange(1,floor_fraction(a*scale)+1),scale)
        completion(s,z,w,t); completion(s,a,w,t)
        cases += 2
        for j in (1,3,7):
            p = F(RNG.randrange(2**(k-1)+1,2**k+1),2**k)
            c = F(floor_fraction(2**(j+2)/(2*p)),2**(j+2))
            e = F(1,4)-p*c/2
            b = 2**(j+1)*e
            assert 0<=c<=1 and 0<=b<=F(1,4)
            assert p*c/2+F(1,2**(j+1))*b == F(1,4)
            ratio = 1/(2*p)
            nondyadic += bool(ratio.denominator & (ratio.denominator-1))
            quarters += 1
    for _ in range(100):
        g = NP.normal(size=3)+1j*NP.normal(size=3); g /= 2*np.linalg.norm(g)
        b = NP.normal(size=5)+1j*NP.normal(size=5); b *= sqrt(3)/2/np.linalg.norm(b)
        psi = np.r_[g,b]
        reflected = (2*np.outer(psi,psi.conj())-np.eye(8))@np.r_[-g,b]
        close(reflected,np.r_[2*g,np.zeros(5)])
    OUT['dyadic_calibration'] = {'completion_cases':cases,'quarter_cases':quarters,
        'non_dyadic_reciprocals':nondyadic,'complex_reflection_models':100}


def deferred_checks():
    checked = leaves = 0
    for length in (1,2,3,4):
        for seed in range(6):
            z, delta, w, t = F(1,2),F(1,4),2,2
            def distribution(history,done):
                if done:
                    return [F(1),F(0),F(0),F(0)],{0}
                # Good probability depends on the full prefix.
                shift = (sum(history)+seed)%3
                weights = ([4,2,1,1],[3,4,1,0],[5,2,0,1])[shift]
                return [F(x,8) for x in weights],{0,1}
            records=[]
            def explore(history,done,good_so_far,prob,immediate,record):
                nonlocal leaves
                if len(history)==length:
                    # The verifier accepts this controller exactly on all-good paths.
                    deferred = prod(row[2] for row in record) if good_so_far else F(0)
                    assert deferred == immediate
                    records.append((prob,deferred))
                    leaves += 1
                    return
                law,goods = distribution(history,done)
                s = sum(law[y] for y in goods)
                c,b = completion(s,z,w,t)
                canonical=min(goods)
                for mode in (0,1):
                    for y in range(4):
                        p = (1-delta)*law[y] if mode==0 else delta/4
                        if not p: continue
                        keep = c if mode==0 and y in goods else b if mode==1 and y==canonical else F(0)
                        nowgood=y in goods
                        explore(history+(y,),done or y==1,good_so_far and nowgood,p*prob,
                                immediate*keep,record+[(mode,y,keep)])
            explore((),False,True,F(1),F(1),[])
            assert sum(p for p,_ in records)==1
            assert sum(p*a for p,a in records)==z**length
            checked += 1
    OUT['deferred_filters'] = {'adaptive_controllers':checked,'enumerated_branches':leaves,
        'dummy_padding_and_history_dependent_probabilities':True}


def field_checks():
    cases=0; worst=0.0
    for k,s in ((2,2),(3,2),(4,3)):
        for _ in range(8):
            v=unitary(k+s); a,b,c,d=v[:k,:k],v[:k,k:],v[k:,:k],v[k:,k:]
            r=np.linalg.norm(d,2); assert r<1
            zp=np.diag(np.exp(2j*pi*NP.random(s)))
            for length in (1,2,4,7):
                eg=np.zeros((k+s,k+s),complex); rg=eg.copy()
                for root in range(length+1):
                    z=np.exp(2j*pi*root/(length+1))*zp
                    x=np.linalg.solve(np.eye(s)-d@z,c)
                    f=a+b@z@x
                    e=np.vstack((np.eye(k),z@x))
                    y=np.linalg.solve(np.eye(s)-z.conj().T@d.conj().T,z.conj().T@b.conj().T)
                    rr=np.vstack((np.eye(k),y))
                    close(f@f.conj().T,np.eye(k),2e-8)
                    close(f@e.conj().T,rr.conj().T@v,2e-8)
                    elow=sum(z@np.linalg.matrix_power(d@z,j)@c for j in range(length))
                    rlow=sum(np.linalg.matrix_power(z.conj().T@d.conj().T,j)@z.conj().T@b.conj().T for j in range(length))
                    el=np.vstack((np.eye(k),elow)); rl=np.vstack((np.eye(k),rlow))
                    tau=r**length/(1-r)
                    assert np.linalg.norm(el-e,2)<=tau+1e-8
                    assert np.linalg.norm(rl-rr,2)<=tau+1e-8
                    error=np.linalg.norm(f@el.conj().T-rl.conj().T@v,2)
                    assert error<=2*tau+1e-8
                    worst=max(worst,error)
                    eg+=el@el.conj().T/(length+1); rg+=rl@rl.conj().T/(length+1)
                for gram in (eg,rg):
                    ev=np.linalg.eigvalsh(gram)
                    assert ev.min()>=1-r**(2*length)-1e-8 and ev.max()<=1+1e-8
                cases+=1
    multisets=paths=0
    for s,length in product(range(1,6),range(1,5)):
        n=ceil(log2(s+1)); bits=n*length+ceil(log2(length+1)); mod=2**bits
        vectors={i:tuple(i**j for j in range(length+1)) for i in range(1,s+1)}
        seen={}
        inputs=defaultdict(set)
        for size in range(1,length+1):
            for ms in combinations_with_replacement(range(1,s+1),size):
                freq=tuple(sum(vectors[i][j] for i in ms)%mod for j in range(length+1))
                assert freq not in seen
                seen[freq]=ms
                # Newton identities reconstruct a polynomial vanishing on exactly this multiset.
                e=[F(1)]
                for j in range(1,size+1):
                    e.append(sum((-1)**(t-1)*e[j-t]*freq[t] for t in range(1,j+1))/j)
                for x in ms:
                    assert sum((-1)**j*e[j]*x**(size-j) for j in range(size+1))==0
                multisets+=1
            for seq in product(range(1,s+1),repeat=size):
                freq=tuple(sum(vectors[i][j] for i in seq)%mod for j in range(length+1))
                inputs[freq].add(seq[-1]); paths+=1
        for freq,possible in inputs.items():
            assert possible==set(seen[freq]) and len(possible)<=length
    OUT['feedback_fields']={'unitary_block_truncations':cases,'exact_multiset_codes':multisets,
        'enumerated_internal_paths':paths,'max_observed_intertwining_error':worst}


def psd_sqrt(x):
    ev,u=np.linalg.eigh(x)
    assert ev.min()>-1e-10
    return (u*np.sqrt(np.maximum(ev,0)))@u.conj().T


def encoder_checks():
    cases=0; ratio=0.0
    for size in (2,3,4):
        for eps in (0,.0001,.01,.2,.7):
            for extra in (0,2):
                for _ in range(5):
                    m=size+extra
                    left=unitary(m)[:,:size]; right=unitary(size)
                    sig=np.sqrt(1-eps*NP.random(size))
                    t=(left*sig)@right.conj().T
                    length=size  # Each row has at most size entries.
                    theta=pi/(4*length+2); small=sin(theta)*t
                    b=np.block([[small,psd_sqrt(np.eye(m)-small@small.conj().T)],
                                [psd_sqrt(np.eye(size)-small.conj().T@small),-small.conj().T]])
                    close(b.conj().T@b,np.eye(m+size))
                    p=np.diag([1]*size+[0]*m); q=np.diag([1]*m+[0]*size)
                    rotate=(2*b@p@b.conj().T-np.eye(m+size))@(np.eye(m+size)-2*q)
                    out=np.linalg.matrix_power(rotate,length)@b[:,:size]
                    error=np.linalg.norm(out-np.vstack((t,np.zeros((size,size)))),2)
                    assert error<=5*eps+2e-9
                    if eps: ratio=max(ratio,error/eps)
                    cases+=1
    OUT['near_isometry_encoder']={'rectangular_dilation_models':cases,'max_error_over_epsilon':ratio,
        'scope':'Tests the block and singular-plane argument, not a compiled programmable-slot circuit.'}


def direct_product_checks():
    cases=0
    for width in (2,3):
        strings=list(product((0,1),repeat=width))
        functions=[lambda x:int(all(x)),lambda x:sum(x)%2,lambda x:int(sum(x)>len(x)//2)]
        for func in functions:
            for biased in (False,True):
                weights=[RNG.randrange(1,8) if biased else 1 for x in strings]
                denominator=sum(weights); mu=[F(x,denominator) for x in weights]
                @lru_cache(None)
                def posterior(partial):
                    valid=[i for i,x in enumerate(strings) if all(b<0 or b==x[j] for j,b in enumerate(partial))]
                    mass=sum(mu[i] for i in valid)
                    prob=sum(mu[i] for i in valid if func(strings[i]))/mass
                    transitions={}
                    for j,b in enumerate(partial):
                        if b<0:
                            transitions[j]=sum(mu[i] for i in valid if strings[i][j])/mass
                    return max(prob,1-prob),transitions
                for cap in range(width):
                    for copies in (1,2,3):
                        @lru_cache(None)
                        def value(states,remaining):
                            guess=prod(posterior(p)[0] for p in states)
                            best=guess
                            for inst,p in enumerate(states):
                                if remaining[inst]<=0: continue
                                for bit,one in posterior(p)[1].items():
                                    total=F(0)
                                    for answer,prob in ((0,1-one),(1,one)):
                                        nextp=list(p); nextp[bit]=answer
                                        ns=list(states); ns[inst]=tuple(nextp)
                                        nr=list(remaining); nr[inst]-=1
                                        total+=prob*value(tuple(ns),tuple(nr))
                                    best=max(best,total)
                            return best
                        empty=tuple([-1]*width)
                        beta=value((empty,),(cap,))
                        actual=value(tuple([empty]*copies),tuple([cap]*copies))
                        assert actual==beta**copies
                        cases+=1
    # Explicit total-budget control, enumerating every pair of two-bit AND inputs.
    success=0
    for x,y in product(product((0,1),repeat=2),repeat=2):
        if x[0]==0:
            guesses=(0,0)  # A one-bit query of y cannot beat guessing AND(y)=0 here.
        else:
            guesses=(x[1],0)
        success+=guesses==(int(all(x)),int(all(y)))
    assert F(success,16)==F(3,4)>F(9,16)
    assert F(1,2)>F(1,2)**2  # Identical hidden fair-bit inputs, no queries.
    OUT['adaptive_products']={'exact_optimal_interleaving_models':cases,
        'total_budget_control_success':'3/4 > 9/16','correlated_input_control':True}


def tournament_checks():
    drift=misscases=coherent=0
    for m in range(2,8):
        for _ in range(8):
            a=[[F(0) for _ in range(m)] for _ in range(m)]
            for i in range(m):
                for j in range(i+1,m):
                    a[i][j]=F(999,1000) if i==0 else F(RNG.randrange(0,17),16)
                    a[j][i]=1-a[i][j]
            w=[F(RNG.randrange(1,10),8) for _ in range(m)]
            total=sum(w)
            actual=sum(w[p]*sum(w[i]*a[i][p] for i in range(m)) for p in range(m))/total
            assert actual==(total*total-sum(x*x for x in w))/(2*total)
            drift+=1
            # Enumerate ideal paths; discard paths once the dominant candidate is found.
            states=[(F(1),tuple([F(1)]*m))]
            for steps in range(1,min(m,4)+1):
                nxt=[]
                for probability,weights in states:
                    total=sum(weights)
                    assert total>0
                    for p in range(1,m):
                        if weights[p]:
                            nxt.append((probability*weights[p]/total,tuple(weights[i]*a[i][p] for i in range(m))))
                states=nxt
                miss=sum(p for p,_ in states)
                assert miss<=F(2*m,2**steps)
                misscases+=1
            pivots=[RNG.randrange(m) for _ in range(3)]
            state=np.array([1/sqrt(m)]*m)[:,None]
            for p in pivots:
                state=np.concatenate([state*np.sqrt([float(1-a[i][p]) for i in range(m)])[:,None],
                                      state*np.sqrt([float(a[i][p]) for i in range(m)])[:,None]],axis=1)
            good=abs(state[:,-1])**2
            expected=np.array([float(prod(a[i][p] for p in pivots))/m for i in range(m)])
            close(good,expected)
            if sum(good)>0: close(good/sum(good),expected/sum(expected))
            coherent+=1
    amplifications=0; minimum=1.0
    for gamma in (.002,.01,.1,.4):
        lengths=ceil(10/sqrt(gamma))
        for p in np.linspace(gamma,1,400):
            theta=np.arcsin(sqrt(p))
            average=.5*p+.5*np.mean(np.sin((2*np.arange(lengths)+1)*theta)**2)
            assert average>=9/40-1e-12
            minimum=min(minimum,average)
        for p in (.02,.3,.9,1):
            g=NP.normal(size=3)+1j*NP.normal(size=3); g/=np.linalg.norm(g)
            bad=NP.normal(size=4)+1j*NP.normal(size=4); bad/=np.linalg.norm(bad)
            psi=np.r_[sqrt(p)*g,sqrt(1-p)*bad]
            q=(2*np.outer(psi,psi.conj())-np.eye(7))@np.diag([-1]*3+[1]*4)
            for ell in (0,1,2,7,11):
                out=np.linalg.matrix_power(q,ell)@psi
                factor=np.vdot(g,out[:3])
                close(out[:3],factor*g)
                close(abs(factor)**2,np.sin((2*ell+1)*np.arcsin(sqrt(p)))**2)
                amplifications+=1
    OUT['fractional_tournament']={'exact_drift_models':drift,'ideal_miss_checks':misscases,
        'coherent_product_states':coherent,'amplification_state_models':amplifications,
        'success_grid_points':1600,'minimum_observed_trial_success':minimum}


if __name__=='__main__':
    for check in (angle_checks,ensemble_checks,calibration_checks,deferred_checks,field_checks,
                  encoder_checks,direct_product_checks,tournament_checks):
        check()
        print(check.__name__,'passed',flush=True)
    result={'batch':'B016','python':sys.version.split()[0],'numpy':np.__version__,'checks':OUT,
            'scope':'Finite local identities and models; no global analytic, factoring, synthesis or query-separation proof certification.'}
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(OUT,indent=2))
