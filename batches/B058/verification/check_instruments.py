"""Reproducible checks for the selected B058 mechanisms, not the headline claims."""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import combinations, product
import json
import math
from pathlib import Path
import random
import time

import numpy as np
import sympy as sp


def affine_lines(q):
    points = list(product(range(q), repeat=2))
    lines = [{(x, (a*x+b) % q) for x in range(q)}
             for a in range(q) for b in range(q)]
    lines += [{(b, y) for y in range(q)} for b in range(q)]
    return points, lines


def affine_moments():
    rng = random.Random(5801)
    cases = 0
    for q in (2, 3, 5, 7, 11):
        points, lines = affine_lines(q)
        sets = [set(), set(points), set(points[:q]), set(points[::2])]
        sets += [set(rng.sample(points, rng.randrange(q*q+1))) for _ in range(20)]
        for selected in sets:
            n = len(selected)
            counts = [len(selected & line) for line in lines]
            assert sum(counts) == (q+1)*n
            assert sum(x*x for x in counts) == n*n+q*n
            variance = sum((F(x)-F(n,q))**2 for x in counts)
            assert variance == q*n-F(n*n,q) <= F(q**3,4)
            directional = [sum((F(x)-F(n,q))**2 for x in counts[i:i+q])/q
                           for i in range(0, len(counts), q)]
            assert sum(directional) == n-F(n*n,q*q)
            cases += 1
    return dict(point_sets=cases, prime_fields=[2,3,5,7,11], arithmetic='exact rational')


def cubic_coordinates():
    shapes = pairs = 0
    for q in (5, 11, 17):
        points, lines = affine_lines(q)
        assert len({x**3 % q for x in range(q)}) == q
        for d in range(1,q):
            for z in range(q):
                shape = {(x**3 % q, (d*x+z) % q) for x in range(q)}
                assert len(shape) == q
                for line in lines:
                    assert len(shape & line) <= 3
                    pairs += 1
                shapes += 1
        for d in range(1,q):
            for x,y in points:
                assert sum((y-d*x-z) % q == 0 for z in range(q)) == 1
    # Exhaust all four deletion offsets at q=5: survival probability is constant.
    q = 5
    points, _ = affine_lines(q)
    survivors = Counter()
    for zs in product(range(q), repeat=q-1):
        for x,y in points:
            if all((y-d*x-zs[d-1]) % q for d in range(1,q)):
                survivors[x**3 % q, y] += 1
    assert set(survivors.values()) == {(q-1)**(q-1)}
    # Every mixed cover of the entire plane of cost a+b/2 <= q is classified.
    # This is a small conditional-cover model, not the source sparse gadget.
    q = 3
    points, lines = affine_lines(q)
    plane = set(points)
    tested = valid = 0
    for a in range(q+1):
        for chosen in combinations(range(len(lines)), a):
            covered = set().union(*(lines[i] for i in chosen))
            for b in range(2*(q-a)+1):
                for singles in combinations(points,b):
                    tested += 1
                    if covered | set(singles) == plane:
                        assert a == q and b == 0
                        assert all(not (lines[i] & lines[j]) for i,j in combinations(chosen,2))
                        valid += 1
    assert valid == q+1
    return dict(cubic_shapes=shapes, shape_line_pairs=pairs, deletion_outcomes=625,
                mixed_covers_examined=tested, equality_parallel_classes=valid,
                scope='Cubic map and conditional-cover mechanism; no asymptotic gadget existence test.')


def interpolation():
    rng = random.Random(5803)
    cases = 0
    for s in (2,3,4):
        for _ in range(8):
            nodes = rng.sample(range(-12,17),2*s)
            g = [math.prod(x-y for j,y in enumerate(nodes) if j != i)
                 for i,x in enumerate(nodes)]
            pairs = [(p,q) for p in range(2*s) for q in range(2*s)]
            pattern = [(p,q) for p,q in pairs if q<p<s or s<=p<q]
            basis_a = list(product(range(s),range(s-1)))
            basis_b = list(product(range(s-1),range(s)))
            def evaluation(exponents, locations):
                return sp.Matrix([[nodes[p]**i*nodes[q]**j for i,j in exponents]
                                  for p,q in locations])
            va, vb = evaluation(basis_a,pattern), evaluation(basis_b,pattern)
            assert va.det() != 0 and vb.det() != 0
            ea, eb = evaluation(basis_a,pairs), evaluation(basis_b,pairs)
            full_weights = [sp.Rational((1 if p<q else -1 if p>q else 0)*(nodes[p]-nodes[q]),2*g[p]*g[q])
                            for p,q in pairs]
            reduced_weights = [sp.Rational((-1 if p<s else 1)*(nodes[p]-nodes[q]),g[p]*g[q])
                               for p,q in pattern]
            full = ea.T*sp.diag(*full_weights)*eb
            reduced = va.T*sp.diag(*reduced_weights)*vb
            assert full == reduced and full.det() != 0
            for degree in range(2*s-1):
                assert sum(sp.Rational(nodes[i]**degree,g[i]) for i in range(2*s)) == 0
            cases += 1
    return dict(arbitrary_order_rational_models=cases, maximum_pairing_dimension=12,
                checks=['both interpolation rectangles','row-shift factorization','nonzero determinant'])


def column_basis(matrix):
    cols = matrix.columnspace()
    return sp.Matrix.hstack(*cols) if cols else sp.zeros(matrix.rows,0)


def polynomial_space(us,z,h):
    n, width = z.shape
    if width == 0:
        return sp.zeros(0,0)
    equations = []
    for t,u in enumerate(us,1):
        annihilators = u.T.nullspace()
        for vector in annihilators:
            row = vector.T*z
            equations.append([t**e*row[j] for e in range(h+1) for j in range(width)])
    mat = sp.Matrix(equations) if equations else sp.zeros(0,width*(h+1))
    kernel = mat.nullspace()
    return sp.Matrix.hstack(*kernel) if kernel else sp.zeros(width*(h+1),0)


def evaluate_space(z,coeff,h,t):
    evaluation = sp.Matrix.hstack(*[t**e*z for e in range(h+1)])
    return evaluation*coeff


def subspace_budget():
    rng = random.Random(5804)
    cases = stages = equality = 0
    for n,m in [(2,3),(3,3),(3,4),(4,4),(4,5)]:
        for kind in range(3):
            us,vs = [],[]
            for i in range(m):
                transform = sp.eye(n)
                for _ in range(5):
                    a,b = rng.sample(range(n),2)
                    transform[a,:] += rng.choice([-2,-1,1,2])*transform[b,:]
                if kind == 0:
                    transform = sp.eye(n)
                    cut = n//2
                    indices = list(range(n)) if i<m//2 else list(range(cut,n))+list(range(cut))
                    ucols = indices[:cut] if i<m//2 else indices[:n-cut]
                    vcols = indices[len(ucols):]
                else:
                    indices = rng.sample(range(n),n)
                    a = rng.randrange(n+1)
                    b = rng.randrange(n-a+1)
                    ucols,vcols = indices[:a],indices[a:a+b]
                us.append(transform[:,ucols] if ucols else sp.zeros(n,0))
                vs.append(transform[:,vcols] if vcols else sp.zeros(n,0))
            def intersection(u,v):
                return u.cols+v.cols-u.row_join(v).rank()
            assert all(intersection(u,v)==0 for u,v in zip(us,vs))
            total = sum(intersection(u,v) for u in us for v in vs)
            assert total <= (m*m//4)*n
            if kind == 0:
                assert total == (m*m//4)*n
                equality += 1
            zs = [sp.eye(n)]+vs
            previous = [0]*len(zs)
            ks = []
            for h in range(m):
                coeffs = [polynomial_space(us,z,h) for z in zs]
                current = [c.cols for c in coeffs]
                kh = [a-b for a,b in zip(current,previous)]
                for z,c,k in zip(zs,coeffs,kh):
                    assert evaluate_space(z,c,h,m+1).rank() == k
                ell = kh[0]-(ks[-1][0] if ks else 0)
                assert ell >= 0
                ks.append(kh)
                budget = sum(e*(ks[e][0]-(ks[e-1][0] if e else 0)) for e in range(h+1))
                assert sum(kh[1:]) <= budget
                for j in range(m):
                    assert evaluate_space(zs[0],coeffs[0],h,j+1).rank() <= kh[0]-kh[j+1]
                previous = current
                stages += 1
            for j,z in enumerate(zs):
                assert sum(k[j] for k in ks) == sum(intersection(u,z) for u in us)
            cases += 1
    # Graph-of-matrix corollary, including the sharp two-block construction.
    rank_cases = 0
    for m in range(2,8):
        for d in (1,2,3):
            xs = [sp.zeros(d) if i<m//2 else sp.eye(d) for i in range(m)]
            ys = [sp.eye(d)-x for x in xs]
            total = sum((xs[i]-ys[j]).rank() for i in range(m) for j in range(m) if i!=j)
            assert total == 2*(m//2)*((m-1)//2)*d
            rank_cases += 1
    assert 1 > (1*1//4)*1  # U_1=V_1=R violates the conclusion without disjointness.
    return dict(subspace_models=cases, filtration_stages=stages, equality_models=equality,
                sharp_rank_sum_models=rank_cases, arithmetic='exact rational linear algebra')


def off_diagonal():
    rng = random.Random(5805)
    models = cells = 0
    for n in range(2,10):
        for k in range(2,n+1):
            chosen = set(rng.sample(range(n),k))
            pb,rb,pi = {},{},{}
            for x,y in product(range(n),repeat=2):
                if x==y:
                    continue
                pb[x,y] = F(1,k*(k-1)) if x in chosen and y in chosen else F(0)
                rb[x,y] = (F(1,n*(k-1)) if y in chosen else F(1,k*n)) if x in chosen else F(0)
                pi[x,y] = F(1,n*(n-1))
            assert sum(pb.values())==sum(rb.values())==sum(pi.values())==1
            for x in range(n):
                assert sum(v for (a,b),v in rb.items() if a==x)==(F(1,k) if x in chosen else 0)
                assert sum(v for (a,b),v in rb.items() if b==x)==F(1,n)
            signed = {xy:pb[xy]-2*rb[xy]+pi[xy] for xy in pi}
            # An additive symmetric overlap kernel cancels exactly.
            heights = [F(rng.randrange(1,10)) for _ in range(n)]
            assert sum(v*(heights[x]+heights[y]) for (x,y),v in signed.items())==0
            for mask in range(1<<n):
                cell = {x for x in range(n) if mask>>x&1}
                m,b = len(cell),len(cell&chosen)
                p,a = F(b,k),F(m,n)
                actual = sum(v for (x,y),v in signed.items() if x in cell and y in cell)
                expected = (p-a)**2+(F(2*k,n)-1)*p*(1-p)/(k-1)-a*(1-a)/(n-1)
                assert actual==expected
                if m<=1:
                    assert actual==0
                if b>=2:
                    assert F(b*(b-1),k*(k-1)) >= p*p/2
                cells += 1
            models += 1
    return dict(pair_laws=models, cell_identities=cells, singleton_and_full_support_cases=True)


def kl(p,q):
    return sum(float(a)*math.log(float(a/b)) for a,b in zip(np.ravel(p),np.ravel(q)) if a>0)


def prediction():
    rng = np.random.default_rng(5806)
    models = sequences = steps = 0
    max_chain_error = max_square_error = 0.0
    for n,nq in [(3,2),(4,3),(5,2)]:
        for repeat in range(3):
            raw = rng.integers(1,10,size=(n,nq)).astype(float)
            if repeat==0:
                raw = np.outer(np.arange(1,n+1),np.arange(1,nq+1))
            omega = raw/raw.sum()
            mu,kappa = omega.sum(axis=1),omega.sum(axis=0)
            conditional = omega/kappa[None,:]
            pair = (conditional*kappa[None,:])@conditional.T
            reference = np.outer(mu,mu)
            info = max(0.0,kl(pair,reference))
            tests = [rng.integers(0,2,size=n) for _ in range(3)]
            fs = [rng.normal(size=(2,2)) for _ in tests]
            gs = [rng.normal(size=(nq,2)) for _ in tests]
            for a in fs+gs:
                a /= max(1.,np.max(np.linalg.norm(a,axis=1)))
            K = 3
            discrepancies = []
            for seq in product(range(3),repeat=K):
                history = [() for _ in range(n)]
                previous_kl = 0.
                chain = 0.
                for test in seq:
                    groups = defaultdict(list)
                    for p,h in enumerate(history):
                        groups[h].append(p)
                    residual = fs[test][tests[test]].copy()
                    for group in groups.values():
                        residual[group] -= np.average(residual[group],axis=0,weights=mu[group])
                    conditional_kl = tv = 0.
                    for group in groups.values():
                        for other in groups.values():
                            actual = np.zeros((2,2)); ref = np.zeros((2,2))
                            for p,r in product(group,other):
                                actual[tests[test][p],tests[test][r]] += pair[p,r]
                                ref[tests[test][p],tests[test][r]] += reference[p,r]
                            mass = actual.sum()
                            actual /= mass
                            ref /= ref.sum()
                            conditional_kl += mass*kl(actual,ref)
                            tv += mass*np.abs(actual-ref).sum()/2
                    chain += conditional_kl
                    new_history = [h+(int(tests[test][p]),) for p,h in enumerate(history)]
                    values = list(dict.fromkeys(new_history))
                    a = np.zeros((len(values),len(values))); b = a.copy()
                    index = {h:i for i,h in enumerate(values)}
                    for p,r in product(range(n),repeat=2):
                        a[index[new_history[p]],index[new_history[r]]] += pair[p,r]
                        b[index[new_history[p]],index[new_history[r]]] += reference[p,r]
                    current_kl = kl(a,b)
                    max_chain_error = max(max_chain_error,abs(current_kl-previous_kl-conditional_kl))
                    assert abs(current_kl-previous_kl-conditional_kl)<2e-12
                    assert 2*tv*tv <= conditional_kl+2e-12
                    square = sum(pair[p,r]*np.dot(residual[p],residual[r]) for p,r in product(range(n),repeat=2))
                    center_means = conditional.T@residual
                    alternative = np.sum(kappa*np.sum(center_means**2,axis=1))
                    max_square_error = max(max_square_error,abs(square-alternative))
                    assert square>=-2e-12 and abs(square-alternative)<2e-12
                    discrepancy = abs(sum(omega[p,q]*np.dot(residual[p],gs[test][q]) for p,q in product(range(n),range(nq))))
                    discrepancies.append(discrepancy)
                    history,previous_kl = new_history,current_kl
                    steps += 1
                assert chain<=info+2e-12
                sequences += 1
            assert np.mean(discrepancies) <= 4*(info/K)**.25+2e-12
            models += 1
    return dict(wedge_models=models, complete_test_sequences=sequences, prefix_steps=steps,
                max_chain_rule_error=max_chain_error,max_wedge_square_error=max_square_error,
                independent_zero_information_controls=3)


def occupancy():
    rng = random.Random(5807)
    graphs = conditionings = 0
    for n in range(1,9):
        for repeat in range(8):
            edges = []
            for a,b in combinations(range(n),2):
                if rng.random()<.4 and not any((min(a,c),max(a,c)) in edges and (min(b,c),max(b,c)) in edges for c in range(n) if c not in (a,b)):
                    edges.append((a,b))
            adjacent = [{b if a==x else a for a,b in edges if x in (a,b)} for x in range(n)]
            independent = [mask for mask in range(1<<n) if not any(mask>>a&1 and mask>>b&1 for a,b in edges)]
            mu = F(sum(mask.bit_count() for mask in independent),n*len(independent))
            D = max(1,max(map(len,adjacent)))
            assert float(mu)>=.5*2**(-4*D*float(mu))-1e-14
            assert max(mask.bit_count() for mask in independent)>=n*math.log(D+1)/(8*(D+1))
            for x in range(n):
                outside = set(range(n))-adjacent[x]-{x}
                grouped = defaultdict(list)
                for mask in independent:
                    grouped[tuple(v for v in outside if mask>>v&1)].append(mask)
                for selected,completions in grouped.items():
                    z = sum(not (adjacent[v]&set(selected)) for v in adjacent[x])
                    occupied = F(sum(mask>>x&1 for mask in completions),len(completions))
                    neighbors = F(sum(sum(mask>>v&1 for v in adjacent[x]) for mask in completions),len(completions))
                    assert occupied==F(1,1+2**z)
                    assert neighbors==(F(z*2**(z-1),1+2**z) if z else 0)
                    assert neighbors>=F(z,4)
                    conditionings += 1
            graphs += 1
    return dict(triangle_free_graphs=graphs, exact_neighborhood_conditionings=conditionings)


def selected_tuples():
    rng = random.Random(5808)
    cases = events = 0
    for alphabet,n,ell in [(3,4,2),(3,4,3),(4,4,3)]:
        streams = list(product(range(alphabet),repeat=n))
        for mode in range(4):
            weights = [1 if mode<2 else 1+sum(s)%3 for s in streams]
            total = sum(weights)
            domination = F(max(weights)*len(streams),total)
            law = Counter()
            for stream,w in zip(streams,weights):
                possibilities = [tuple(stream[i] for i in indices) for indices in combinations(range(n),ell)]
                possibilities += [tuple(reversed(t)) for t in possibilities]
                chosen = min(possibilities) if mode%2==0 else max(possibilities)
                law[chosen] += w
            cap = 2*domination*math.comb(n,ell)*F(1,alphabet**ell)
            assert all(F(w,total)<=cap for w in law.values())
            entropy = -sum(float(F(w,total))*math.log(float(F(w,total))) for w in law.values())
            assert entropy>=-math.log(float(cap))-1e-13
            # Conditioning on an auxiliary-dependent acceptance law changes C0 by at most 1/c.
            accepted = [w*F(1+(s[0]%2),2) for s,w in zip(streams,weights)]
            prob = sum(accepted)/total
            assert all(v/sum(accepted)<=domination/prob/len(streams) for v in accepted)
            cases += 1
    for _ in range(100):
        p = np.array([rng.randrange(1,30) for _ in range(5)],float); p/=p.sum()
        q = np.array([rng.randrange(1,30) for _ in range(5)],float); q/=q.sum()
        for mask in range(32):
            event = [i for i in range(5) if mask>>i&1]
            assert q[event].sum() <= (kl(p,q)+p[event].sum())/(1-math.exp(-1))+1e-13
            events += 1
    return dict(exhaustive_stream_models=cases, rare_event_comparisons=events,
                selector='Most and least lexicographic subsequence in either orientation')


def main():
    started = time.perf_counter()
    results = {}
    for fn in (affine_moments,cubic_coordinates,interpolation,subspace_budget,
               off_diagonal,prediction,occupancy,selected_tuples):
        results[fn.__name__] = fn()
        print(fn.__name__, 'passed', flush=True)
    report = dict(status='passed',elapsed_seconds=round(time.perf_counter()-started,3),checks=results,
                  scope='Selected finite mechanisms only; no Ryser, crossing-number, planar-distance or Ramsey headline theorem is certified.')
    Path(__file__).with_name('results.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='checks'}))


if __name__ == '__main__':
    main()
