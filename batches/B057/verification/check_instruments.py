"""Finite checks of selected arguments, not the source headline claims."""
import itertools as it
import json
import math
import time
from functools import lru_cache
from pathlib import Path

import numpy as np
import sympy as sp


PERMS = list(it.permutations(range(3)))
INDEX = {g:i for i,g in enumerate(PERMS)}
MUL = np.array([[INDEX[tuple(g[h[i]] for i in range(3))] for h in PERMS] for g in PERMS])
INV = np.array([next(j for j in range(6) if MUL[i,j]==0) for i in range(6)])


def compression():
    rng = np.random.default_rng(206)
    cases = pairs = 0
    for n in (7,8,11):
        for copies in (1,2):
            for _ in range(20):
                x = rng.integers(0,6,size=(n,copies))
                ref = x[1].copy()
                def move(v,cycle):
                    w = v.copy()
                    for a,b in zip(cycle,cycle[1:]+cycle[:1]):
                        w[b] = v[a]
                    return w
                for i in range(2,n):
                    k = next(j for j in range(n) if j not in (0,1,i))
                    z = MUL[INV[x],move(x,[1,i,k])]
                    assert np.array_equal(z[i],MUL[INV[x[i]],ref])
                    fresh = [j for j in range(n) if j not in (0,1,i,k)][:2]
                    zp = move(z,[i]+fresh)
                    pair = MUL[z,INV[zp]]
                    assert all(np.all(pair[j]==0) for j in range(n) if j not in (i,fresh[0]))
                    extra = next(j for j in range(n) if j not in (i,0,fresh[0]))
                    pair = move(pair,[fresh[0],0,extra])
                    assert np.array_equal(pair[i],MUL[INV[x[i]],ref])
                    assert np.array_equal(pair[0],INV[pair[i]])
                    x = MUL[x,pair]
                    assert np.array_equal(x[i],ref)
                    pairs += 1
                assert np.all(x[1:]==ref)
                cases += 1
    assert MUL[1,2]!=MUL[2,1]
    return dict(nonabelian_tuple_models=cases, pair_corrections=pairs,
                base_group='S3; one or two repeated natural copies; n=7,8,11')


def lattice_operations(le):
    n = len(le)
    meet,join = np.empty((n,n),int),np.empty((n,n),int)
    for i,j in it.product(range(n),repeat=2):
        lows = np.flatnonzero(le[:,i]&le[:,j])
        highs = np.flatnonzero(le[i]&le[j])
        greatest = [x for x in lows if np.all(le[lows,x])]
        least = [x for x in highs if np.all(le[x,highs])]
        assert len(greatest)==len(least)==1
        meet[i,j],join[i,j] = greatest[0],least[0]
    return meet,join


def insert(le,a,b,inner):
    n,m = len(le),len(inner)-2
    result = np.eye(n+m,dtype=bool)
    result[:n,:n] = le
    result[n:,n:] = inner[1:-1,1:-1]
    for j in range(n,n+m):
        result[:n,j] = le[:,a]
        result[j,:n] = le[b,:]
    return result


def covers(le):
    return {(i,j) for i,j in it.product(range(len(le)),repeat=2)
            if i!=j and le[i,j] and not any(le[i,k] and le[k,j] for k in range(len(le)) if k not in (i,j))}


def private_insertions():
    rng = np.random.default_rng(57)
    chain = lambda n: np.fromfunction(lambda i,j:i<=j,(n,n),dtype=int)
    diamond = np.eye(5,dtype=bool)
    diamond[0,:] = True
    diamond[:,-1] = True
    boolean = np.array([[a&b==a for b in range(4)] for a in range(4)],dtype=bool)
    checked = preserved = 0
    for initial in (chain(4),diamond,boolean):
        for a,b in it.product(range(len(initial)),repeat=2):
            if a==b or not initial[a,b]:
                continue
            for q in (chain(3),chain(4),diamond):
                oldmeet,oldjoin = lattice_operations(initial)
                result = insert(initial,a,b,q)
                meet,join = lattice_operations(result)
                assert np.array_equal(meet[:len(initial),:len(initial)],oldmeet)
                assert np.array_equal(join[:len(initial),:len(initial)],oldjoin)
                lost = covers(initial)-covers(result)
                assert lost == ({(a,b)} if (a,b) in covers(initial) else set())
                checked += 1
    # Two private chains fence the original bottom-top interval permanently.
    for _ in range(5):
        le = chain(2)
        le = insert(insert(le,0,1,chain(4)),0,1,chain(4))
        for step in range(7):
            meet,join = lattice_operations(le)
            interior = [c for c in range(len(le)) if c not in (0,1) and le[0,c] and le[c,1]]
            for c in interior:
                assert any(u!=v and le[u,v] and meet[c,u]==meet[c,v]==0 and join[c,u]==join[c,v]==1
                           for u,v in it.product(interior,repeat=2))
            preserved += 1
            candidates = [(a,b) for a,b in it.product(range(len(le)),repeat=2) if a!=b and le[a,b]]
            a,b = candidates[int(rng.integers(len(candidates)))]
            le = insert(le,a,b,chain(3))
    return dict(private_insertions=checked, persistent_fence_stages=preserved)


def algebra_mul(a,b):
    result = np.zeros_like(a)
    for g,h in it.product(range(6),repeat=2):
        result[MUL[g,h]] += a[g]@b[h]
    return result


def idempotent_repair():
    rng = np.random.default_rng(207)
    unit = np.zeros((6,2,2))
    unit[0] = np.eye(2)
    d = np.zeros_like(unit)
    d[0,0,0] = 1
    upper,lower = np.zeros_like(unit),np.zeros_like(unit)
    upper[1,0,1],lower[2,1,0] = .2,.3
    u = algebra_mul(unit+upper,unit+lower)
    ui = algebra_mul(unit-lower,unit-upper)
    e = algebra_mul(algebra_mul(u,d),ui)
    assert np.max(abs(algebra_mul(e,e)-e))<1e-14
    lengths = [0 if g==PERMS[0] else (1 if sum(g[i]!=i for i in range(3))==2 else 2) for g in PERMS]
    weight = np.exp(.1*np.array(lengths))
    norm = lambda a: float(np.sum(abs(a)*weight[:,None,None]))
    classes = [[0],[i for i in range(6) if lengths[i]==1],[i for i in range(6) if lengths[i]==2]]
    residual = trace_error = tail_max = 0.0
    for _ in range(16):
        a = e+rng.normal(size=e.shape)*.0004
        b = 4*(a-algebra_mul(a,a))
        r = norm(b)
        assert r<.1
        q,power = unit.copy(),unit.copy()
        terms = 15
        for j in range(1,terms+1):
            power = algebra_mul(power,b)
            q += math.comb(2*j,j)/4**j*power
        p = unit/2+algebra_mul(a-unit/2,q)
        tail = norm(a-unit/2)*r**(terms+1)/(1-r)
        residual = max(residual,norm(algebra_mul(p,p)-p))
        tail_max = max(tail_max,tail)
        for cls in classes:
            error = abs(sum(np.trace(p[g]-e[g]) for g in cls))
            assert error<=tail+2e-13
            trace_error = max(trace_error,float(error))
        intertwiner = algebra_mul(p,e)+algebra_mul(unit-p,unit-e)
        assert norm(intertwiner-unit)<1
        assert norm(algebra_mul(intertwiner,e)-algebra_mul(p,intertwiner))<2e-13
        assert norm(algebra_mul(p,p)-p)<2e-13
    return dict(models=16,maximum_idempotence_residual=residual,
                maximum_class_trace_error=trace_error,maximum_series_tail_bound=tail_max,
                scope='Finite S3 group algebra with exponential weights; infinite-group convergence uses the analytic argument.')


def pfaffian(a):
    n = len(a)
    if not n:
        return 1
    result = 0
    for j in range(1,n):
        keep = [k for k in range(n) if k not in (0,j)]
        result += (-1)**(j+1)*int(a[0,j])*pfaffian(a[np.ix_(keep,keep)])
    return result


def deletion_pfaffian(a):
    return sum((-1)**i*pfaffian(np.delete(np.delete(a,i,0),i,1)) for i in range(len(a)))


def pfaffian_descent():
    rng = np.random.default_rng(208)
    cases = 0
    for m in range(1,5):
        for _ in range(8):
            size = 2*m+1
            raw = rng.integers(-3,4,size=(size,size))
            a = raw-raw.T
            shifts = rng.integers(-5,6,size=size)
            changed = a+shifts[None,:]-shifts[:,None]
            assert deletion_pfaffian(a)==deletion_pfaffian(changed)
            raw = rng.integers(-3,4,size=(size+1,size+1))
            b = raw-raw.T
            assert sum((-1)**i*deletion_pfaffian(np.delete(np.delete(b,i,0),i,1)) for i in range(size+1))==0
            even = a[:-1,:-1]
            rotated = even[np.ix_(list(range(1,size-1))+[0],list(range(1,size-1))+[0])].copy()
            rotated[:-1,-1] += 1
            rotated[-1,:-1] -= 1
            rhs = -pfaffian(even)
            for i in range(1,size-1):
                keep = [j for j in range(1,size-1) if j!=i]
                rhs += (-1)**(i+1)*pfaffian(even[np.ix_(keep,keep)])
            assert pfaffian(rotated)==rhs
            duplicate = a.copy()
            duplicate[-1,:] = duplicate[0,:]
            duplicate[:,-1] = duplicate[:,0]
            assert deletion_pfaffian(duplicate)==0
            cases += 1
    return dict(skew_matrix_models=cases,maximum_pfaffian_size=8,
                checks=['lift shifts','cocycle deletion','twisted cyclic rotation','repeated projected vertices'],
                scope='Algebraic identities only; no sparse-cycle vanishing theorem is tested.')


def mixed_naturality():
    g = sp.symbols('g')
    differential = sp.diag(g,1)
    matrices = [sp.Matrix(x) for x in [[[1,1],[0,1]],[[1-g,1],[0,1]],[[1,0],[1,1]],[[1,0],[1,1-g]]]]
    def actual(m):
        a,b,c,d = list(m)
        return sp.Matrix([[a,b],[g*c,d]]),sp.Matrix([[a,g*b],[c,d]])
    for m in matrices:
        m1,m0 = actual(m)
        assert differential*m1==m0*differential
        assert m1.det().subs(g,0)==m0.det().subs(g,0)==1
    u,up,l,lp = [actual(m) for m in matrices]
    for degree in (0,1):
        assert lp[degree]*u[degree]==up[degree]*l[degree]
        assert (lp[degree]*u[degree]).det()==1-g
    projected_left = matrices[3][0,0]*matrices[0][0,0]
    projected_right = matrices[1][0,0]*matrices[2][0,0]
    assert sp.expand(projected_left-projected_right)==g
    # A homotopy on Typ(g) can kill this difference, but not strict equality.
    assert g*1==projected_left-projected_right
    return dict(actual_commuting_squares=2, projected_commutator='g != 0',
                local_model='Q[g] localized at (g); all four maps are isomorphisms',
                scope='Failure of the specified strict functor assignment, not a disproof of its intended K-theory conclusion.')


def residue_norm_detector():
    t,x,y,pi,u,eta,zeta = sp.symbols('t x y pi u eta zeta')
    f = sp.Poly(t**5-t+1,t,modulus=5)
    orbit = sp.Poly(t,t,modulus=5)
    for r in range(1,11):
        orbit = (orbit**5).rem(f)
        expected = sp.Poly(t-r,t,modulus=5)
        assert orbit==expected
        assert sp.gcd(f,orbit-sp.Poly(t,t,modulus=5)).degree()==(5 if r%5==0 else 0)
    assert f.is_irreducible
    cyclotomic = sp.expand(sp.cyclotomic_poly(5,1-t))
    assert cyclotomic==t**4-5*t**3+10*t**2-10*t+5
    poly = t**5-5*t**4+10*t**3-10*t**2+5*t-pi
    companion = sp.zeros(5)
    for j in range(4):
        companion[j+1,j] = 1
    companion[:,4] = sp.Matrix([pi,-5,10,-10,5])
    assert companion.det()==pi
    assert sp.expand(((t-1)**5+zeta).subs(t,1-eta))==-eta**5+zeta
    local = x**5-u*pi**4*x**4+2*u*pi**4*x**3-2*u*pi**4*x**2+u*pi**4*x-x*y**4+y**5-pi
    linear = sum(c*x**a*y**b*pi**cpi for (a,b,cpi),c in sp.Poly(local,x,y,pi).terms() if a+b+cpi<=1)
    assert linear==-pi
    assert sp.Poly(poly,t).all_coeffs()[-1]==-pi
    return dict(frobenius_extension_degrees=10, special_fiber_polynomial='t^5-t+1 over F5',
                uniformizer_norm='pi', ambient_linear_term='-pi',
                scope='Polynomial, residue-degree and norm data; no algebraic K-theory class is computed.')


@lru_cache(None)
def compositions(total,slots):
    if slots==1:
        return ((total,),)
    return tuple((a,)+rest for a in range(total+1) for rest in compositions(total-a,slots-1))


def sumsets_and_powers():
    rng = np.random.default_rng(210)
    count = 0
    for ambient in range(1,5):
        for _ in range(10):
            d0 = 3
            pool = compositions(d0,ambient)
            indices = rng.choice(len(pool),size=min(7,len(pool)),replace=False)
            d = {pool[int(i)] for i in indices}
            origin = next(iter(d))
            h = sp.Matrix([[x-y for x,y in zip(v,origin)] for v in d]).rank()
            c = len(d)
            assert c<=math.comb(d0+h,h)
            z = next(j for j in range(c) if math.comb(d0+j,j)>=c)
            sums = {tuple(0 for _ in range(ambient))}
            for k in range(1,5):
                sums = {tuple(a+b for a,b in zip(v,w)) for v in sums for w in d}
                bound = lambda j:math.comb(k+j,j)+(c-1-j)*math.comb(k+j-1,j)
                assert len(sums)>=bound(h)>=bound(z)
                for j in range(h):
                    assert (bound(j+1)-bound(j))*(j+1)==math.comb(k+j-1,j)*(k-1)*(c-j-1)
                count += 1
    variables = sp.symbols('x y z')
    exponents = sorted(compositions(2,3),reverse=True)
    monomials = [math.prod(v**e for v,e in zip(variables,a)) for a in exponents]
    basis = [monomials[i]+sum((j+1)*monomials[j] for j in range(i+1,len(monomials))) for i in range(4)]
    products = 0
    for k in range(1,5):
        representatives = {}
        for indices in it.combinations_with_replacement(range(len(basis)),k):
            value = tuple(sum(exponents[i][j] for i in indices) for j in range(3))
            representatives.setdefault(value,indices)
        for value,indices in representatives.items():
            polynomial = sp.Poly(sp.expand(math.prod(basis[i] for i in indices)),*variables)
            assert polynomial.monoms()[0]==value
            products += 1
    return dict(sumset_bounds=count, polynomial_products_with_distinct_leading_values=products)


def rank_mod(a,p=101):
    a = np.array(a,dtype=np.int64).copy()%p
    row = 0
    for col in range(a.shape[1]):
        choices = np.flatnonzero(a[row:,col])
        if not len(choices):
            continue
        a[[row,row+choices[0]]] = a[[row+choices[0],row]]
        a[row] = a[row]*pow(int(a[row,col]),-1,p)%p
        for i in range(row+1,len(a)):
            a[i] = (a[i]-a[i,col]*a[row])%p
        row += 1
        if row==len(a):
            break
    return row


def differential_injectivity():
    def basis(n,p,q):
        if min(p,q)<0:
            return []
        return [a+b for a in compositions(p,n) for b in compositions(q,n)]
    def operator(n,p,q,reverse=False):
        src = basis(n,p,q)
        dst = basis(n,p+1,q-1) if reverse else basis(n,p-1,q+1)
        ix = {a:i for i,a in enumerate(dst)}
        matrix = np.zeros((len(dst),len(src)),dtype=np.int64)
        for j,a in enumerate(src):
            for i in range(n):
                f,t = (n+i,i) if reverse else (i,n+i)
                if a[f]:
                    b = list(a)
                    b[f] -= 1
                    b[t] += 1
                    matrix[ix[tuple(b)],j] += a[f]
        weights = np.array([math.prod(math.factorial(x) for x in a) for a in dst],dtype=np.int64)
        return matrix,weights
    spaces = injective = 0
    for n in (1,2,3):
        for p,q in it.product(range(5),repeat=2):
            if p+q>5:
                continue
            src = basis(n,p,q)
            d,wd = operator(n,p,q)
            e,we = operator(n,p,q,True)
            weights = np.array([math.prod(math.factorial(x) for x in a) for a in src],dtype=np.int64)
            assert np.array_equal(d.T@(wd[:,None]*d)-e.T@(we[:,None]*e),(p-q)*np.diag(weights))
            if p>q:
                assert rank_mod(d)==len(src)
                injective += 1
            spaces += 1
    u1,u2,y1,y2 = sp.symbols('u1 u2 y1 y2')
    h = u1*y2-u2*y1
    assert y1*sp.diff(h,u1)+y2*sp.diff(h,u2)==0 and h!=0
    assert sp.Poly(sp.diff(u1**5,u1),u1,modulus=5).is_zero
    return dict(bihomogeneous_spaces=spaces, injective_positive_weight_spaces=injective,
                controls=['nonzero kernel at equal degrees','characteristic-five derivative failure'])


def main():
    started = time.perf_counter()
    results = {}
    for name,fn in [('compression',compression),('private_insertions',private_insertions),
                    ('idempotent_repair',idempotent_repair),('pfaffian_descent',pfaffian_descent),
                    ('mixed_naturality',mixed_naturality),('residue_norm_detector',residue_norm_detector),
                    ('sumsets_and_powers',sumsets_and_powers),('differential_injectivity',differential_injectivity)]:
        results[name] = fn()
        print(name,'passed',flush=True)
    report = dict(status='passed',elapsed_seconds=round(time.perf_counter()-started,3),checks=results,
                  scope='Selected finite arguments only; no headline theorem or infinite K-theory computation is certified.')
    Path(__file__).with_name('results.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='checks'}))


if __name__=='__main__':
    main()
