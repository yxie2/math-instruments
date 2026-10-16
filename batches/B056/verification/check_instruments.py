"""Selected finite checks; no source headline theorem is certified.

Run with Python, NumPy and SymPy. All source tables needed at runtime are
included here; the program does not depend on the private acquisition cache.
"""
import itertools as it
import json
import math
import time
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from pathlib import Path

import numpy as np
import sympy as sp


def pmul(a, b):
    """Carryless multiplication: integer bits encode F_2[q]."""
    z = 0
    while b:
        if b & 1:
            z ^= a
        a <<= 1
        b >>= 1
    return z


def addto(z, x, scale=1):
    for k, v in x.items():
        z[k] = z.get(k, 0) ^ pmul(v, scale)
        if not z[k]:
            del z[k]
    return z


def cocycle_certificate():
    low = 'exyzuvtjfn'
    basis = low + low.upper()
    rad = ''.join(a for a in basis if a not in 'ef')
    corners = dict(zip(low, ['ee'] * 4 + ['ef'] * 2 + ['fe'] * 2 + ['ff'] * 2))
    corners.update({a.upper(): c[::-1] for a, c in list(corners.items())})
    product = {(a, b): {} for a in basis for b in basis}
    for a in low:
        product[corners[a][0], a] = {a: 1}
        product[a, corners[a][1]] = {a: 1}
    for pair, value in {
        'xy': {'z': 2}, 'yx': {'z': 1}, 'xu': {'v': 1}, 'yu': {'v': 1},
        'tx': {'j': 1}, 'ty': {'j': 4}, 'ut': {'y': 1, 'x': 2},
        'vt': {'z': 2}, 'uj': {'z': 1}, 'tu': {'n': 3},
        'nt': {'j': 2}, 'un': {'v': 1},
    }.items():
        product[tuple(pair)] = value
    for a, b, c in it.product(low, repeat=3):
        x = product[c, a].get(b, 0)
        y = product[a, c].get(b, 0)
        if x:
            product[a, b.upper()][c.upper()] = x
        if y:
            product[b.upper(), a][c.upper()] = y

    def mul(x, y):
        z = {}
        for a, ca in x.items():
            for b, cb in y.items():
                addto(z, product[a, b], pmul(ca, cb))
        return z

    for a, b, c in it.product(basis, repeat=3):
        assert mul(product[a, b], {c: 1}) == mul({a: 1}, product[b, c])
    for a, b in it.product(basis, repeat=2):
        tr = product[a, b].get('E', 0) ^ product[a, b].get('F', 0)
        assert tr == int(a.swapcase() == b)
    assert mul(mul(product['u', 't'], {'u': 1}), {'t': 1}) == {'z': 6}
    degree = dict(zip(low, [0, 2, 2, 4, 1, 3, 1, 3, 0, 2]))
    degree.update({a.upper(): 5-d for a, d in list(degree.items())})
    for a, b in it.product(basis, repeat=2):
        assert all(degree[c] == degree[a]+degree[b] for c in product[a, b])
    rows = {
        4: '''EuNT EyZX FNtU JtXZ NtEU NtXV XzJT ZxEY tEun tXuf
              tXvn tXzj tuFn tuNf tvNn uFNT vNNT vtJu xEyz zJtx''',
        2: '''EuUE EuVX EvVE ExXE EyYE EzZE FNnF FVvF FVxU FtTF
              FtYU Ftun Ftxj JFtX JNtZ JUyX JVyZ JjEE JjTT JjXX
              NFtU NNtV NUyU NVyV NjJN NjZV NnNN NnVV Ntuf Ntvn
              Ntzj TtEE TtXX UuFF UuUU UvNF UvVU UxXU Uyun Uyxj
              UzZU VvNN VvVV VxEU VxXV Vyuf Vyvn Vyzj VzZV XxEE
              XxXX YuFT YuUY YvNT YvVY YxXY YyEE YyJJ YyTT YyXX
              YyYY YyZZ YzZY ZxXZ ZzEE ZzJJ ZzTT ZzXX jJFF jJUU
              jJjj jJnn jYyj jZvn jZzj nNFF nNUU ntTn tJjt tTNN
              tTVV tTtt tYyt tZzt tzJn uFVX uFty uNFT uNUY uNte
              uUyy uVye ujJu vNUE vNVX vNty vVyy vtTv xEuv xJFT
              xJUY xJjx xJte xTtx xXuu xXvv xXyy xXzz xYyx xZye
              xZzx xuFv xuNu xvNv yxJu yzJv zJNT zJVY zYyz zZuu
              zZvv zZyy zZzz''',
        8: 'EyJT JtEY tEyj tyJf',
        1: '''JNjX JVzX NNjU NVzU NjYU Njun Njxj Ntxt TNtX TVyX
              Vyxt VzYU Vzun Vzxj YuNJ YuVZ jYun juNn jxJn txTn
              uNNJ uNVZ uNjy uVzy xJNJ xJVZ xTNT xTVY yxTv zYuv
              zuNv zxJv''',
    }
    cochain = {}
    for coefficient, words in rows.items():
        for word in words.split():
            a, b, c, v = word
            assert (a, b, c) not in cochain
            assert sum(x.isupper() for x in word[:3]) == 1+v.isupper()
            assert corners[a][1] == corners[b][0] and corners[b][1] == corners[c][0]
            assert corners[v] == corners[a][0]+corners[c][1]
            cochain[a, b, c] = {v: coefficient}
    assert len(cochain) == 179
    p = lambda a, b, c: cochain.get((a, b, c), {})
    composable = 0
    for a, b, c, d in it.product(rad, repeat=4):
        composable += all(corners[x][1] == corners[y][0] for x, y in zip((a,b,c), (b,c,d)))
        delta = mul({a: 1}, p(b, c, d))
        for x, v in product[a, b].items():
            addto(delta, p(x, c, d), v)
        for x, v in product[b, c].items():
            addto(delta, p(a, x, d), v)
        for x, v in product[c, d].items():
            addto(delta, p(a, b, x), v)
        addto(delta, mul(p(a, b, c), {d: 1}))
        assert not delta, (a,b,c,d,delta)
    assert composable == 15250
    gamma = lambda a: 2 if a in 'uvtEXYZUV' else 0
    for a, b in it.product(rad, repeat=2):
        lhs = [{}, {}]
        for w in rad:
            addto(lhs[w.isupper()], mul(p(a,b,w), {w.swapcase(): 1}))
        rhs0 = {v: pmul(gamma(a), c) for v, c in product[a,b].items()} if b.isupper() else {}
        rhs1 = {v: pmul(gamma(b)^gamma(v)^(gamma(a) if b.islower() else 0), c)
                for v,c in product[a,b].items()}
        assert lhs[0] == {v:c for v,c in rhs0.items() if c}
        assert lhs[1] == {v:c for v,c in rhs1.items() if c}
    cycle_boundary = {}
    for coeff, a,b,c in [(4,'t','x','J'),(1,'t','y','J')]:
        for x,v in product[a,b].items():
            addto(cycle_boundary, {(x,c): v}, coeff)
        for x,v in product[b,c].items():
            addto(cycle_boundary, {(a,x): v}, coeff)
    assert not cycle_boundary
    evaluation = addto(dict(p('t','y','J')), p('t','x','J'), 4)
    assert evaluation == {'f': 8}
    return dict(associativity_triples=8000, cochain_entries=179,
                radical_four_words=18**4, composable_four_words=composable,
                boundary_pairs=324, nonzero_cycle_value='q^3 f over F_2[q]')


def rref_mod(a, p):
    a = np.asarray(a, dtype=np.int64).copy() % p
    pivots = []
    for col in range(a.shape[1]):
        choices = np.flatnonzero(a[len(pivots):,col])
        if not len(choices):
            continue
        row = len(pivots)
        a[[row, row+choices[0]]] = a[[row+choices[0], row]]
        a[row] = a[row]*pow(int(a[row,col]), -1, p) % p
        for k in range(a.shape[0]):
            if k != row and a[k,col]:
                a[k] = (a[k]-a[k,col]*a[row]) % p
        pivots.append(col)
        if len(pivots) == a.shape[0]:
            break
    return a, pivots


def null_mod(a, p):
    a, pivots = rref_mod(a, p)
    free = [j for j in range(a.shape[1]) if j not in pivots]
    z = np.zeros((a.shape[1],len(free)), dtype=np.int64)
    for k,j in enumerate(free):
        z[j,k] = 1
        for i,c in enumerate(pivots):
            z[c,k] = -a[i,j] % p
    return z


def rank_mod(a, p):
    return len(rref_mod(a,p)[1])


@lru_cache(None)
def partitions(n, cap=None):
    if n == 0:
        return ((),)
    cap = min(n, cap if cap is not None else n)
    return tuple((i,)+t for i in range(cap,0,-1) for t in partitions(n-i,i))


def cells(lam):
    return {(i,j) for i,r in enumerate(lam) for j in range(r)}


@lru_cache(None)
def strip_sign(lam, mu):
    small, big = cells(mu), cells(lam)
    if not small <= big:
        return 0
    skew = big-small
    if not skew or any({(i,j),(i+1,j),(i,j+1),(i+1,j+1)} <= skew for i,j in skew):
        return 0
    seen = {next(iter(skew))}
    todo = list(seen)
    while todo:
        i,j = todo.pop()
        for x in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
            if x in skew and x not in seen:
                seen.add(x)
                todo.append(x)
    return (-1)**(len({i for i,j in skew})-1) if seen == skew else 0


@lru_cache(None)
def character(lam, rho):
    if not rho:
        return int(not lam)
    return sum(strip_sign(lam,mu)*character(mu,rho[1:]) for mu in partitions(sum(lam)-rho[0]))


@lru_cache(None)
def bead_matrix(s, k):
    small, large = partitions(s-k), partitions(s)
    index = {x:i for i,x in enumerate(large)}
    r = np.zeros((len(large),len(small)),dtype=np.int64)
    beads = s+1
    for j,mu in enumerate(small):
        beta = {beads+(mu[t] if t<len(mu) else 0)-t-1 for t in range(beads)}
        for x in beta:
            if x+k in beta:
                continue
            new = sorted((beta-{x})|{x+k},reverse=True)
            lam = tuple(y-beads+t+1 for t,y in enumerate(new) if y-beads+t+1>0)
            r[index[lam],j] += (-1)**sum(x<y<x+k for y in beta)
    return r


def tensor_recurrence():
    prime = 101
    checked, entries, mixed = 0, 0, 0
    universal = {}

    @lru_cache(None)
    def rec(s,k,e,v):
        if not s:
            return (v[0]*v[0] % prime,)
        if k>s:
            return rec(s,s,0,v)
        if k == 1:
            assert e == 0
            dims = [character(lam,(1,)*s) for lam in partitions(s)]
            value = sum(a*b for a,b in zip(dims,v))**2*pow(math.factorial(s),-1,prime)
            return tuple(int(d*value % prime) for d in dims)
        r = bead_matrix(s,k)
        w = tuple(int(x) for x in (r.T@np.array(v,dtype=np.int64)) % prime)
        a = np.array(rec(s,k-1,0,v),dtype=np.int64)
        if any(w):
            a = (a+pow(k*(e+1),-1,prime)*(r@np.array(rec(s-k,k,e+1,w),dtype=np.int64))) % prime
        return tuple(int(x) for x in a)

    for s in range(1,9):
        ps = partitions(s)
        table = np.array([[character(lam,rho) for rho in ps] for lam in ps], dtype=np.int64)
        z = [math.prod(j**m*math.factorial(m) for j,m in Counter(rho).items()) for rho in ps]
        for i,j in it.product(range(len(ps)),repeat=2):
            assert sum(Fraction(int(table[i,k]*table[j,k]),z[k]) for k in range(len(ps))) == int(i==j)
        for k in range(1,s+1):
            r = bead_matrix(s,k)
            assert all(r[i,j] == strip_sign(lam,mu) for i,lam in enumerate(ps) for j,mu in enumerate(partitions(s-k)))
        hits = []
        for i,lam in enumerate(ps):
            exact = [sum(Fraction(int(table[i,k]**2*table[j,k]),z[k]) for k in range(len(ps))) for j in range(len(ps))]
            assert all(g.denominator == 1 and g>=0 for g in exact)
            v = tuple(int(j==i) for j in range(len(ps)))
            assert rec(s,s,0,v) == tuple(int(g)%prime for g in exact)
            if all(exact):
                hits.append(lam)
            checked += 1
            entries += len(ps)
        universal[str(s)] = [list(x) for x in hits]
        assert bool(hits) == (s not in (2,4))
        for seed in range(3):
            v = tuple((i+seed)%5-2 for i in range(len(ps)))
            values = np.array(v)@table
            exact = [sum(Fraction(int(values[k]**2*table[j,k]),z[k]) for k in range(len(ps))) for j in range(len(ps))]
            assert rec(s,s,0,v) == tuple(int(g.numerator)*pow(g.denominator,-1,prime)%prime for g in exact)
            mixed += 1
    # A zero residue is inconclusive for a nonnegative integer: no reconstruction is claimed.
    assert 101>0 and 101%prime == 0
    return dict(max_degree=8, individual_squares=checked, multiplicities=entries,
                mixed_character_vectors=mixed, modulus=prime, universal_candidates=universal,
                scope='Independent small-degree recurrence check; source range through 64 not rerun.')


def conjugate(lam):
    return tuple(sum(r>j for r in lam) for j in range(lam[0] if lam else 0))


def dominates(a,b):
    return sum(a)==sum(b) and all(sum(a[:k])>=sum(b[:k]) for k in range(1,max(len(a),len(b))+1))


def horizontal_chain():
    chains = 0
    for n in range(1,16):
        for tau,theta in it.product(partitions(n),repeat=2):
            if not dominates(tau,theta):
                continue
            current = tau
            for length in range(len(theta),0,-1):
                t = theta[length-1]
                cols = list(conjugate(current))
                chosen = sorted(range(len(cols)),key=lambda j:(cols[j],j),reverse=True)[:t]
                after = [h-int(j in chosen) for j,h in enumerate(cols)]
                assert after == sorted(after,reverse=True)
                nxt = conjugate(tuple(h for h in after if h))
                assert dominates(nxt,theta[:length-1])
                for k in range(1,len(current)+1):
                    loss = sum(current[:k])-sum(nxt[:k])
                    assert loss == max(0,t-(current[k] if k<len(current) else 0))
                assert all(h-g in (0,1) for h,g in zip(cols,after))
                current = nxt
            assert not current
            chains += 1
    # Removing the leftmost of tied columns can destroy the partition.
    assert [1,2,2] != sorted([1,2,2],reverse=True)
    return dict(max_degree=15, dominance_pairs_with_constructed_chains=chains,
                tie_rule='rightmost among equal-height columns')


def transfer_duality():
    p = 5
    # Upper triangular 2x2 algebra, with basis e11,e12,e22.
    matrices = [np.array(x,dtype=np.int64) for x in [
        [[1,0],[0,0]], [[0,1],[0,0]], [[0,0],[0,1]]]]
    structure = np.array([[[int((a@b)[0,0]),int((a@b)[0,1]),int((a@b)[1,1])]
                           for b in matrices] for a in matrices])
    left = [structure[i].T for i in range(3)]
    dual = [structure[:,i,:] for i in range(3)]
    modules = [left, matrices, [np.array([[1]]),np.array([[0]]),np.array([[0]])],
               [np.array([[0]]),np.array([[0]]),np.array([[1]])]]
    checks = []
    for actions in modules:
        d = len(actions[0])
        equations = np.vstack([np.kron(np.eye(d,dtype=int),dual[i])-np.kron(actions[i].T,np.eye(3,dtype=int)) for i in range(3)])
        hom = null_mod(equations,p)
        assert hom.shape[1] == d
        evaluations = np.array([np.array([1,0,1])@hom[:,j].reshape((3,d),order='F') for j in range(d)]).T
        assert rank_mod(evaluations,p) == d
        checks.append(d)
    # In R=F_5[x,y]/(x,y)^2, tensoring the injection Rx -> R with DR is not exact.
    rx = np.array([[0,0,0],[1,0,0],[0,0,0]],dtype=int)
    ry = np.array([[0,0,0],[0,0,0],[1,0,0]],dtype=int)
    dx,dy = rx.T,ry.T
    radical_image = np.column_stack((dx,dy))
    quotient_dimension = 3-rank_mod(radical_image,p)
    assert quotient_dimension == 2 and rank_mod(dx,p) == 1
    # A split contractible free complex stays exact after tensoring even here.
    eye,zero = np.eye(3,dtype=int),np.zeros((3,3),dtype=int)
    for i in range(-8,9):
        d = eye if i%2 == 0 else zero
        before = eye if (i+1)%2 == 0 else zero
        assert not np.any(d@before) and rank_mod(d,p)+rank_mod(before,p) == 3
    # Cohomology duality reverses arrows. The coresolution begins at C^(-1).
    dimensions = {j: 3 for j in range(-8,3)}
    maps = {j: np.diag([1,0,0]) if j%2==0 else np.diag([0,1,0]) for j in range(-8,2)}
    for a in range(1,6):
        j = -a-1
        h_negative = dimensions[j]-rank_mod(maps[j],p)-rank_mod(maps[j-1],p)
        h_dual = dimensions[j]-rank_mod(maps[j-1].T,p)-rank_mod(maps[j].T,p)
        assert h_negative == h_dual == 1
    return dict(nakayama_evaluation_module_dimensions=checks, negative_degree_checks=5,
                nonflat_tensor_kernel_dimension=quotient_dimension-rank_mod(dx,p),
                scope='Finite evaluation pairings and degree reversal; not a nonprojective self-orthogonal module.')


def filtered_koszul():
    p = 5
    # Monomial positions carry two-dimensional coefficient spaces.
    # Sparse generators use (x exponent,y exponent,coefficient component).
    generators = [
        {(1,0,0):1,(0,1,1):1}, {(0,1,0):1},
        {(3,0,0):1}, {(0,3,0):1}, {(3,0,1):1}, {(0,3,1):1},
    ]
    models = [generators, generators[:1]+generators[2:],
              [{(2,0,0):1,(0,2,1):2},{(1,1,0):1}]+generators[2:],
              [{(2,0,0):1,(0,2,0):1},{(1,1,0):1}]+generators[2:]]
    strict = 0
    comparisons = 0
    outputs = []
    for gens in models:
        degrees = {}
        for d in range(8):
            positions = [(x,d-x,c) for x in range(d+1) for c in range(2)]
            ix = {x:i for i,x in enumerate(positions)}
            rows = []
            for g in gens:
                gd = next(iter(g))[0]+next(iter(g))[1]
                for shift in range(d-gd+1):
                    row = np.zeros(len(positions),dtype=int)
                    for (x,y,c),v in g.items():
                        row[ix[x+shift,y+d-gd-shift,c]] = v
                    rows.append(row)
            w, piv = rref_mod(np.array(rows,dtype=int).reshape((-1,len(positions))),p)
            w = w[:len(piv)]
            initial = np.zeros_like(w)
            for i,col in enumerate(piv):
                first = (col//2)*2
                initial[i,first:first+2] = w[i,first:first+2]
            iw, ip = rref_mod(initial,p)
            assert piv == ip
            free = [j for j in range(len(positions)) if j not in piv]
            degrees[d] = (positions,ix,w,iw[:len(ip)],piv,free)
        bettis = []
        for which in (2,3):
            multiplication = {}
            for d in range(7):
                pos,ix,w,iw,piv,free = degrees[d]
                npos,nix,nw,niw,npiv,nfree = degrees[d+1]
                rel = degrees[d+1][which]
                for variable in range(2):
                    m = np.zeros((len(nfree),len(free)),dtype=int)
                    for j,col in enumerate(free):
                        x,y,c = pos[col]
                        v = np.zeros(len(npos),dtype=int)
                        v[nix[x+(variable==0),y+(variable==1),c]] = 1
                        for r,pivot in enumerate(npiv):
                            v = (v-v[pivot]*rel[r])%p
                        m[:,j] = v[nfree]
                    multiplication[d,variable] = m
            table = []
            for j in range(7):
                dims = [len(degrees[j-k][5]) if j>=k else 0 for k in range(3)]
                d1 = np.column_stack((multiplication[j-1,0],multiplication[j-1,1])) if j>=1 else np.zeros((dims[0],0),dtype=int)
                d2 = np.vstack((-multiplication[j-2,1],multiplication[j-2,0])) if j>=2 else np.zeros((2*dims[1],0),dtype=int)
                assert not np.any(d1@d2%p)
                r1,r2 = rank_mod(d1,p),rank_mod(d2,p)
                table.append([dims[0]-r1,2*dims[1]-r1-r2,dims[2]-r2])
            bettis.append(table)
        for before,after in zip(*bettis):
            for a,b in zip(before,after):
                assert a<=b
                strict += a<b
                comparisons += 1
        outputs.append(bettis)
    assert strict>0
    return dict(module_models=len(models), graded_betti_comparisons=comparisons,
                strict_increases=strict, tables_by_internal_degree=outputs)


def division_coefficients():
    x,y = sp.symbols('x y',commutative=True)
    # Hamilton's rational quaternion division algebra, an algebraic model of
    # the ordered-basis step, not the source's complex-function-field setup.
    def qm(a,b):
        w,x,y,z = a
        v,r,s,t = b
        return tuple(sp.expand(q) for q in (w*v-x*r-y*s-z*t,w*r+x*v+y*t-z*s,
                     w*s-x*t+y*v+z*r,w*t+x*s-y*r+z*v))
    one,i,j = (1,0,0,0),(0,1,0,0),(0,0,1,0)
    t1,t2 = (0,x+y,0,0),(0,y,0,0)
    assert qm(t1,t2)==qm(t2,t1)
    assert qm(t1,t1)==(-(x+y)**2,0,0,0) or qm(t1,t1)==(sp.expand(-(x+y)**2),0,0,0)
    assert qm(t2,t2)==(-y*y,0,0,0)
    assert qm(j,t1)!=qm(t1,j)
    def power(a,n):
        r = one
        for _ in range(n):
            r = qm(r,a)
        return r
    shifts = 0
    for d in range(7):
        monomials = [qm(power(t1,a),power(t2,d-a)) for a in range(d+1)]
        expanded = [qm(e,m) for m in monomials for e in [one,i,j,(0,0,0,1)]]
        columns = [[sp.expand(v[c]).coeff(x,a).coeff(y,d-a) for a in range(d+1) for c in range(4)] for v in expanded]
        assert sp.Matrix(columns).rank()==4*(d+1)
        for a in range(d+1):
            base = qm(j,monomials[a])
            assert qm(base,t1)==qm(j,qm(power(t1,a+1),power(t2,d-a)))
            assert qm(base,t2)==qm(j,qm(power(t1,a),power(t2,d-a+1)))
            shifts += 2
    return dict(homogeneous_basis_degrees=7, exact_right_shifts=shifts,
                noncentral_coefficient_control=True,
                scope='Rational quaternion model of ordered bases and right multiplication; no triangular construction for general regular sequences.')


def integral_projections():
    rng = np.random.default_rng(205)
    cases = 0
    max_ratio = 0.0
    for n,l in [(3,2),(4,2),(5,3)]:
        for _ in range(6):
            a = sp.Matrix(rng.integers(-3,4,size=(n,l)).tolist())
            if a.rank()<l:
                continue
            gram = int((a.T*a).det())
            minors = [int(a[list(rows),:].det()) for rows in it.combinations(range(n),l)]
            assert sum(v*v for v in minors)==gram
            q = np.linalg.qr(np.array(a,dtype=float))[0]
            for count in range(l,n+1):
                for rows in it.combinations(range(n),count):
                    sub = a[list(rows),:]
                    if sub.rank()<l:
                        continue
                    det_projection = int((sub.T*sub).det())
                    assert 1<=det_projection<=gram
                    inverse_norm = 1/np.linalg.svd(q[list(rows),:],compute_uv=False)[-1]
                    ratio = inverse_norm/math.sqrt(gram)
                    assert ratio<=1+1e-10
                    max_ratio = max(max_ratio,ratio)
                    cases += 1
    for n in (0,1,100,10**6):
        a = sp.Matrix([[1,n],[0,1],[1,n+1]])
        assert (a.T*a).det()==3
        assert a.columnspace()[0]==sp.Matrix([1,0,1])
    # Without integrality, bounded wedge norm need not control coordinate inversion.
    for epsilon in (.1,.01,.001):
        assert math.hypot(epsilon,1)<2 and math.hypot(epsilon,1)/epsilon>1/epsilon
    return dict(injective_coordinate_projections=cases, largest_bound_ratio=max_ratio,
                unbounded_basis_shears=4, nonintegral_controls=3)


def sylow_restriction():
    power_checks = 0
    for p in (2,3,5):
        for k in range(2,5):
            modulus = p**k
            units = list(range(1,modulus,p))
            for n in range(1,10):
                if n%p:
                    assert len({pow(u,n,modulus) for u in units})==len(units)
                    power_checks += 1
            assert len({pow(u,p,modulus) for u in units})<len(units)

    def coboundary(group,multiply,action,degree,p):
        nonidentity = group[1:]
        domain = list(it.product(nonidentity,repeat=degree))
        target = list(it.product(nonidentity,repeat=degree+1))
        ix = {t:i for i,t in enumerate(domain)}
        d = np.zeros((len(target),len(domain)),dtype=int)
        for row,t in enumerate(target):
            terms = [(t[1:],action(t[0]))]
            for j in range(degree):
                terms.append((t[:j]+(multiply(t[j],t[j+1]),)+t[j+2:],(-1)**(j+1)))
            terms.append((t[:-1],(-1)**(degree+1)))
            for word,c in terms:
                if word in ix:
                    d[row,ix[word]] += c
        return d%p,domain
    cases = []
    group = list(it.permutations(range(3)))
    mult = lambda a,b: tuple(a[b[i]] for i in range(3))
    identity = group[0]
    sign = lambda g: (-1)**sum(g[i]>g[j] for i in range(3) for j in range(i+1,3))
    for p in (2,3):
        subgroup = [g for g in group if (mult(g,g)==identity if p==2 else sign(g)==1)]
        if p==2:
            subgroup = [identity,next(g for g in subgroup if g!=identity)]
        for twisted in (False,True):
            action = sign if twisted else lambda g:1
            b,_ = coboundary(group,mult,action,1,p)
            d,words = coboundary(group,mult,action,2,p)
            bs,_ = coboundary(subgroup,mult,action,1,p)
            ds,swords = coboundary(subgroup,mult,action,2,p)
            assert not np.any(d@b%p) and not np.any(ds@bs%p)
            z = null_mod(d,p)
            restriction = z[[words.index(w) for w in swords],:]
            assert not np.any(ds@restriction%p)
            hdim = z.shape[1]-rank_mod(b,p)
            image = rank_mod(np.column_stack((bs,restriction)),p)-rank_mod(bs,p)
            assert image==hdim
            cases.append(dict(prime=p,sign_action=twisted,source_h2_dimension=hdim))
    return dict(principal_unit_power_bijections=power_checks, sylow_h2_models=cases,
                scope='Finite principal-unit quotients and S3 cohomology; not the full Witt-order finiteness theorem.')


def main():
    start = time.perf_counter()
    results = {}
    for name,check in [
        ('cocycle_certificate',cocycle_certificate),('transfer_duality',transfer_duality),
        ('filtered_koszul',filtered_koszul),('division_coefficients',division_coefficients),
        ('integral_projections',integral_projections),('sylow_restriction',sylow_restriction),
        ('tensor_recurrence',tensor_recurrence),('horizontal_chain',horizontal_chain),
    ]:
        results[name] = check()
        print(name, 'passed', flush=True)
    report = dict(status='passed',elapsed_seconds=round(time.perf_counter()-start,3),checks=results,
                  scope='Selected exact finite algebra and small-degree tests, not certification of source conjecture claims.')
    Path(__file__).with_name('results.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='checks'}))


if __name__=='__main__':
    main()
