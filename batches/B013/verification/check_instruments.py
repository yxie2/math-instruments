"""Exact small models for B013; no full theorem or Lean certification."""
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, permutations, product
from math import comb, factorial, gcd
from pathlib import Path
import json
import random
import sys

RNG = random.Random(2026101613)
RESULTS = []


def triangles(n, edges):
    return tuple(frozenset(combinations(vs, 2)) for vs in combinations(range(n), 3)
                 if set(combinations(vs, 2)) <= edges)


def query(focus, parent, threshold, ts, priority, expose=None):
    candidates = [t for t in ts if t != parent and t & focus]
    assert all(len(t & focus) == 1 for t in candidates)
    values = [(expose(t) if expose else priority[t], j, t) for j, t in enumerate(candidates)]
    for value, j, t in sorted(values):
        if value >= threshold:
            break
        if query(t-focus, t, value, ts, priority, expose):
            return False
    return True


def paired_queries():
    cases = answers = 0
    models = []
    all_edges = tuple(combinations(range(4), 2))
    for mask in range(64):
        edges = {e for j, e in enumerate(all_edges) if mask >> j & 1}
        ts = triangles(4, edges)
        for order in permutations(ts):
            models.append((edges, ts, order))
    for _ in range(150):
        edges = {e for e in combinations(range(5), 2) if RNG.random() < .8}
        ts = triangles(5, edges)
        order = list(ts)
        RNG.shuffle(order)
        models.append((edges, ts, order))
    for edges, ts, order in models:
        priority = {t: F(j+1, len(ts)+1) for j, t in enumerate(order)}
        for threshold in [F(0), *priority.values(), F(1)]:
            present = set(edges)
            for t in order:
                if priority[t] < threshold and t <= present:
                    present -= t
            for e in edges:
                assert query(frozenset([e]), None, threshold, ts, priority) == (e in present)
                answers += 1
        for t in ts:
            present = set(edges)
            for s in order:
                if priority[s] < priority[t] and s <= present:
                    present -= s
            for e in t:
                focus = t-{e}
                assert query(focus, t, priority[t], ts, priority) == (focus <= present)
                answers += 1
        cases += 1
    RESULTS.append(dict(check='chronological singleton and parent-pair queries', priority_models=cases,
                        answers=answers, exact=True))


def pmul(a, b):
    c = [F(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    while len(c) > 1 and c[-1] == 0:
        c.pop()
    return tuple(c)


def unfoldings():
    edges = {(0, 1), (0, 2), (1, 2), (0, 3), (1, 3)}
    ts = triangles(4, edges)
    @lru_cache(None)
    def polynomial(focus, parent):
        answer = (F(1),)
        for t in ts:
            if t != parent and t & focus:
                child = polynomial(t-focus, t)
                no_success = (F(1),)+tuple(-a/F(j+1) for j, a in enumerate(child))
                answer = pmul(answer, no_success)
        return answer
    assert polynomial(frozenset([(0, 1)]), None) == (F(1), F(-2), F(1))
    assert polynomial(frozenset([(0, 2)]), None) == (F(1), F(-1), F(1, 2))
    for t in ts:
        for omitted in t:
            f, g = tuple(t-{omitted})
            assert polynomial(t-{omitted}, t) == pmul(polynomial(frozenset([f]), t),
                                                       polynomial(frozenset([g]), t))
    trials = collision_count = disagreements = clean = 0
    graph_models = [(n, tuple(combinations(range(n), 2))) for n in (4, 5)]
    graph_models.append((6, tuple(combinations(range(3), 2))+tuple(combinations(range(3, 6), 2))))
    graph_models.append((5, ((0, 1), (0, 2), (1, 2), (0, 3), (1, 3), (3, 4))))
    for n, edges in graph_models:
        ts = triangles(n, set(edges))
        for _ in range(500):
            priority = {t: RNG.random() for t in ts}
            roots = [RNG.choice(edges) for j in range(2)]
            seen = set()
            collided = False
            def expose(t):
                nonlocal collided
                if t in seen:
                    collided = True
                    return RNG.random()
                seen.add(t)
                return priority[t]
            independent = [query(frozenset([e]), None, 1, ts, priority, expose) for e in roots]
            finite = [query(frozenset([e]), None, 1, ts, priority) for e in roots]
            if not collided:
                assert independent == finite
                clean += 1
            disagreements += independent != finite
            collision_count += collided
            trials += 1
    assert disagreements <= collision_count and clean > 0
    # A sparse graph also exercises executions with genuinely no exposure collisions.
    single = triangles(3, set(combinations(range(3), 2)))
    for _ in range(20):
        seen = set()
        priority = {single[0]: RNG.random()}
        def expose_one(t):
            assert t not in seen
            seen.add(t)
            return priority[t]
        assert query(frozenset([(0, 1)]), None, 1, single, priority, expose_one) is False
        clean += 1
    RESULTS.append(dict(check='independent product polynomials and exposure coupling',
                        exact_two_triangle_polynomials=True, coupled_trials=trials,
                        exposure_collisions=collision_count, answer_disagreements=disagreements,
                        clean_executions=clean, scope='pathwise coupling check, not a collision-rate theorem'))


def compositions(total, length):
    if length == 0:
        if total == 0:
            yield ()
        return
    for first in range(1, total-length+2):
        for tail in compositions(total-first, length-1):
            yield (first,)+tail


@lru_cache(None)
def patterns(t, budget):
    types = [()]
    for r in range(1, t):
        for m in range(r, budget+1):
            types.extend(p for p in compositions(m, r) if p <= p[::-1])
    types.sort()
    @lru_cache(None)
    def collect(vertices, amount, low):
        if vertices == 0:
            return ((),)
        out = []
        for j in range(low, len(types)):
            p = types[j]
            if len(p)+1 <= vertices and sum(p) <= amount:
                out.extend((p,)+tail for tail in collect(vertices-len(p)-1, amount-sum(p), j))
        return tuple(out)
    return collect(t, budget, 0)


def series_count(t, budget):
    dp = {(v, 0): 1 for v in range(t+1)}
    for r in range(1, t):
        for m in range(r, budget+1):
            if r % 2:
                pal = comb((m-1)//2, r//2)
            else:
                pal = comb(m//2-1, r//2-1) if m % 2 == 0 else 0
            a = (comb(m-1, r-1)+pal)//2
            nxt = Counter()
            for (v, weight), coefficient in dp.items():
                for copies in range(min((t-v)//(r+1), (budget-weight)//m)+1):
                    nxt[v+copies*(r+1), weight+copies*m] += coefficient*comb(a+copies-1, copies)
            dp = dict(nxt)
    return sum(dp.get((t, m), 0) for m in range(budget+1))


def path_patterns():
    expected = [7, 14, 26, 34, 63, 75, 142, 164, 311, 315, 601, 468, 879]
    total = pairs = cycle_checks = 0
    for k in range(5, 18):
        subtotal = 0
        for t in range(max(3, k//2), min(8, k)+1):
            pp = patterns(t, k-t)
            assert len(pp) == len(set(pp)) == series_count(t, k-t)
            subtotal += len(pp)
            pairs += 1
        assert subtotal == expected[k-5]
        total += subtotal
    assert total == 3099 and pairs == 42
    for t in range(3, 7):
        for pat in patterns(t, 5):
            clique = set(range(t))
            edges = {frozenset(e) for e in combinations(clique, 2)}
            paths, singletons = [], []
            q = sum(map(sum, pat))
            v = sum(len(p)+1 for p in pat if p)
            next_clique, next_outside = 0, t
            for p in pat:
                chain = list(range(next_clique, next_clique+len(p)+1))
                next_clique += len(p)+1
                if not p:
                    singletons.append(chain[0])
                    continue
                expanded = [chain[0]]
                for j, amount in enumerate(p):
                    extension = list(range(next_outside, next_outside+amount))+[chain[j+1]]
                    next_outside += amount
                    expanded.extend(extension)
                edges.update(frozenset(e) for e in zip(expanded, expanded[1:]))
                paths.append(expanded)
            if not paths:
                continue
            for ell in range(q+v, q+t+1):
                cyc = sum(paths, [])+singletons[:ell-q-v]
                assert len(cyc) == len(set(cyc)) == ell >= 3
                assert all(frozenset((cyc[j], cyc[(j+1) % ell])) in edges for j in range(ell))
                cycle_checks += 1
    RESULTS.append(dict(check='weighted forest canonical recursion and independent generating function',
                        parameter_pairs=pairs, patterns=total, exact=True))
    RESULTS.append(dict(check='explicit clique closure cycles', constructed_cycles=cycle_checks, exact=True))


def ball_separation():
    edges = tuple(combinations(range(5), 2))
    checks = 0
    for mask in range(1 << len(edges)):
        adj = [set() for _ in range(5)]
        for j, (u, v) in enumerate(edges):
            if mask >> j & 1:
                adj[u].add(v)
                adj[v].add(u)
        for xset in ({0, 1}, {0, 1, 2}):
            outside = set(range(5))-xset
            balls = []
            for root in (0, 1):
                seq = [adj[root] & outside]
                for _ in range(2):
                    seq.append(seq[-1] | set().union(*(adj[v] & outside for v in seq[-1])))
                balls.append(seq)
            min_internal = 100
            def visit(v, visited):
                nonlocal min_internal
                if 1 in adj[v]:
                    min_internal = min(min_internal, len(visited))
                for w in adj[v] & outside - visited:
                    visit(w, visited | {w})
            for v in adj[0] & outside:
                visit(v, {v})
            for r, s in product(range(-1, 3), repeat=2):
                a = {0} if r == -1 else balls[0][r]
                b = {1} if s == -1 else balls[1][s]
                hypothesis = 1 not in adj[0] if r == s == -1 else min_internal > r+s+2
                if hypothesis:
                    assert not a & b
                    assert not any(v in adj[u] for u in a for v in b)
                    checks += 1
    RESULTS.append(dict(check='outside-path and ball compatibility', implications=checks, exact=True))


def tree_model(h):
    def node(i, p, sign):
        return (i, p, 'l' if i == h else sign)
    def order(i, p, column=False):
        if i == h:
            return [node(i, p, 'l')]
        first, last = ('+', '-') if column else ('-', '+')
        return [node(i, p, first)]+order(i+1, 2*p, column)+order(i+1, 2*p+1, column)+[node(i, p, last)]
    dummy = ('dummy',)
    rows, cols = order(0, 0)+[dummy], [dummy]+order(0, 0, True)
    def group(i, sign, parity=None):
        return [node(i, p, sign) for p in range(1 << i) if parity is None or p % 2 == parity]
    modes = []
    for i in range(1, h+1):
        modes.extend([(('V', i, '+', None), group(i, '+'), group(i-1, '+'), [dummy], group(i-1, '+')),
                      (('V', i, '-', None), group(i-1, '-'), group(i, '-'), [dummy], group(i-1, '-'))])
        for sign, d in product(('+', '-'), range(2)):
            left, right = (group(i-1, sign), group(i, sign, d)) if sign == '+' else (group(i, sign, d), group(i-1, sign))
            modes.append((('W', i, sign, d), group(i, sign, d), [dummy], left, right))
    def value(row, col, flip=False):
        if row == dummy or col == dummy:
            return 1
        i, p, sr = row
        j, q, sc = col
        if i == h and j == h:
            return int(p <= q and not (flip and p == q))
        if i == j and sr == sc == '+': return int(p <= q)
        if i == j and sr == sc == '-': return int(p < q)
        if i == j+1 and sr in ('+', 'l') and sc == '+': return int(p//2 <= q)
        if i == j+1 and sr in ('-', 'l') and sc == '-': return int(p//2 < q)
        return 0
    return rows, cols, modes, value, node, dummy


def anchors_and_repairs():
    anchor = [[int(u != v) for v in range(64)] for u in range(64)]
    for u in range(32, 64):
        for v in range(59, 64):
            anchor[u][v] = ((u-32) >> (63-v)) & 1
    assert len(set(map(tuple, anchor))) == 64
    assert len(set(zip(*anchor))) == 64
    assert min(map(sum, anchor)) >= 58
    assert min(map(sum, zip(*anchor))) >= 48
    assert all(sum(row[:32]) >= 31 for row in anchor)
    assert all(sum(col[:32]) >= 31 for col in zip(*anchor))
    assert len({tuple(row[59:]) for row in anchor[32:]}) == 32
    trace_checks = body_checks = original_bodies = new_bodies = 0
    for h in (1, 2, 3):
        rows, cols, modes, value, node, dummy = tree_model(h)
        ri, ci = {x:j for j,x in enumerate(rows)}, {x:j for j,x in enumerate(cols)}
        for selection in combinations(cols, 5):
            traces = {tuple(value(r, c) for c in selection) for r in rows}
            assert len(traces) <= 27
            trace_checks += 1
        for r in rows[:-1]:
            assert sum(r in a or r in b for tag, a, b, c, d in modes) <= 4
        for c in cols[1:]:
            assert sum(c in a or c in b for tag, r, s, a, b in modes) <= 4
        for tag, r1s, r2s, c1s, c2s in modes:
            for r1, r2, c1, c2 in product(r1s, r2s, c1s, c2s):
                if ri[r1] >= ri[r2] or ci[c1] >= ci[c2]: continue
                body = tuple(value(r, c) for r in (r1, r2) for c in (c1, c2))
                if body == (1, 0, 1, 1):
                    assert tag[0:3] == ('W', h, '-') and r1 == c1 and r1[0] == h
                    original_bodies += 1
                body_checks += 1
        for p in range(1 << h):
            leaf, parent = node(h, p, '+'), node(h-1, p//2, '+')
            assert tuple(value(r, c, True) for r in (leaf, dummy) for c in (parent, leaf)) == (1, 0, 1, 1)
            assert ci[parent] < ci[leaf]
            new_bodies += 1
        m = 1 << h
        for i in range(h+1):
            # Marginal probability for each individual position in a signed level.
            assert F(1, 1 << i)*F(1, m >> i) == F(1, m)
        assert F(1, m) > F(1, m*m)  # Shared leaf correlation is not a product law.
    core_assignments = 0
    for h in (1, 2, 3):
        for bits in product(range(2), repeat=4*h-1):
            plus, minus = [1], [0]
            offset = 0
            accepted = True
            for i in range(1, h+1):
                cp, cm = bits[offset:offset+2]
                offset += 2
                if i < h:
                    dp, dm = bits[offset:offset+2]
                    offset += 2
                else:
                    dp = dm = bits[offset]
                bodies = [(1, cp, 1, plus[-1]), (1, minus[-1], 1, cm),
                          (cp, dp, 1, 1), (dm, cm, 1, 1)]
                if (1, 0, 1, 1) in bodies:
                    accepted = False
                plus.append(dp)
                minus.append(dm)
            assert not accepted
            core_assignments += 1
    RESULTS.append(dict(check='binary anchor properties and bounded nonanchor traces',
                        five_column_selections=trace_checks, exact=True,
                        scope='structural ingredients; not exhaustive search for every anchor copy'))
    RESULTS.append(dict(check='tree modes, leaf-copy location and protected propagation',
                        mode_bodies=body_checks, original_bodies=original_bodies,
                        new_bodies_after_leaf_flips=new_bodies, core_assignments=core_assignments,
                        exact=True, scope='selected body constraints, not exhaustive full-matrix edit distance'))


def det(a):
    return a[0]*(a[4]*a[8]-a[5]*a[7])-a[1]*(a[3]*a[8]-a[5]*a[6])+a[2]*(a[3]*a[7]-a[4]*a[6])


def norm_digits():
    matching = 0
    for t in range(1, 9):
        k = t*t+1
        for a, b, c in product(range(t), repeat=3):
            assert (a+t*b+t*t-(t+1)*c == k-1) == (a == b == c)
            matching += 1
    gaps = 0
    # Degree-one norm models preserve the full digit/carry mechanism.
    for r in (3, 5, 7):
        l, k = r*r, 2
        base = 100*k*k*l**3+1
        while any(base % p == 0 for p in range(2, int(base**.5)+1)):
            base += 1
        modulus = base**k
        for labels in permutations(range(r), 3):
            cols = []
            digits = []
            for x in labels:
                residues = [(1, 0), (x, 0), (0, x*x % r)]
                dc = [tuple(RNG.choice([v for v in range(1, l+1) if v % r == residue])
                            for residue in row) for row in residues]
                cols.append([d0+base*d1 for d0, d1 in dc])
                digits.append(dc)
            matrix = [cols[j][i] for i in range(3) for j in range(3)]
            gamma0 = det([digits[j][i][0] for i in range(3) for j in range(3)])
            gamma1 = 0
            for chosen_row in range(3):
                gamma1 += det([digits[j][i][int(i == chosen_row)] for i in range(3) for j in range(3)])
            vandermonde = (labels[1]-labels[0])*(labels[2]-labels[0])*(labels[2]-labels[1])
            assert gamma1 % r == vandermonde % r != 0
            assert abs(gamma0) <= 6*k*k*l**3 and abs(gamma1) <= 6*k*k*l**3
            centered = gamma0+gamma1*base
            assert centered % modulus == det(matrix) % modulus
            assert abs(centered)*2 < modulus and abs(centered) > base//2
            gaps += 1
    RESULTS.append(dict(check='isolated digit positions and norm-coded residue gaps',
                        position_triples=matching, degree_one_gap_models=gaps, exact=True,
                        scope='reduced degree-one models, not the d=41 construction'))


def residue_orbits():
    models = 0
    for prime, k in ((2, 1), (3, 1), (2, 2)):
        h = prime**k
        gl = [a for a in product(range(h), repeat=9) if gcd(det(a), h) == 1]
        sl = [a for a in gl if det(a) % h == 1]
        assert len(gl) == h**9*F(prime-1, prime)*F(prime**2-1, prime**2)*F(prime**3-1, prime**3)
        units = sum(gcd(a, h) == 1 for a in range(h))
        for b in range(k+1):
            for e in range(b, k+1):
                d, ee = prime**b, prime**e
                diag = (1, d, ee)
                act = lambda a: tuple(a[3*i+j]*diag[j] % h for i in range(3) for j in range(3))
                origin = act((1, 0, 0, 0, 1, 0, 0, 0, 1))
                orbit_gl = {act(a) for a in gl}
                orbit_sl = {act(a) for a in sl}
                stabilizer = [a for a in gl if act(a) == origin]
                det_image = {det(a) % h for a in stabilizer}
                assert F(len(orbit_sl), len(orbit_gl)) == F(len(det_image), units)
                assert F(len(det_image), units) >= F(ee, h)
                assert len(stabilizer) <= d**3*ee**3
                assert len(orbit_sl) >= F(21, 64)*F(h**8, d**3*ee**2)
                rows = {(x, d*y % h, ee*z % h) for x, y, z in product(range(h), repeat=3)}
                assert len(rows)*d*ee == h**3
                assert all((ee*x % h, ee*y % h, ee*z % h) in rows for x, y, z in product(range(h), repeat=3))
                models += 1
    RESULTS.append(dict(check='singular GL and SL orbit accounting', smith_models=models,
                        rings=[2, 3, 4], exact=True))


def digit_divisors():
    models = matrices = 0
    row_pairs = tuple(combinations(range(3), 2))
    for prime, k, r, l, signatures in [(5, 1, 2, 4, (0, 0, 0)),
                                      (5, 1, 2, 4, (0, 1, 1)),
                                      (7, 1, 3, 6, (0, 1, 2)),
                                      (5, 2, 2, 4, (0, 0, 0))]:
        h = prime**k
        options = []
        for i, j in product(range(3), repeat=2):
            digit_options = [[v for v in range(1, l+1) if v % r == (signatures[j]+i+u) % r] for u in range(k)]
            options.append([sum(d*prime**u for u, d in enumerate(ds)) for ds in product(*digit_options)])
        tails = [0]*(k+1)
        divisor_sum = count = 0
        for a in product(*options):
            b = k
            for (i, j), (v, w) in product(row_pairs, repeat=2):
                minor = (a[3*i+v]*a[3*j+w]-a[3*i+w]*a[3*j+v]) % h
                val = 0
                while val < k and minor % prime == 0:
                    val += 1
                    minor //= prime
                b = min(b, val)
                if b == 0: break
            for j in range(1, b+1): tails[j] += 1
            divisor_sum += prime**b
            count += 1
        for j in range(1, k+1):
            assert F(tails[j], count) <= F(r, l)**(4*j)
        theta = prime*F(r, l)**4
        assert theta < 1 and F(divisor_sum, count) <= 1+sum(theta**j for j in range(1, k+1))
        models += 1
        matrices += count
    RESULTS.append(dict(check='fixed-label digit tails and divisor moments', label_models=models,
                        matrices=matrices, repeated_labels_included=True, exact=True))


def main():
    for test in (paired_queries, unfoldings, path_patterns, ball_separation,
                 anchors_and_repairs, norm_digits, residue_orbits, digit_divisors):
        test()
        print(test.__name__, 'passed', flush=True)
    out = dict(batch='B013', status='passed', python=sys.version.split()[0], seed=2026101613,
               scope='Exact finite identities and seeded coupling executions; no full theorem, priority or Lean certification.',
               checks=RESULTS)
    Path(__file__).with_name('results.json').write_text(json.dumps(out, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
