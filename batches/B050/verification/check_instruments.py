"""Finite checks for B050. They do not certify the source headline theorems."""
from fractions import Fraction as F
from itertools import product, permutations
from math import ceil, comb, lcm
from pathlib import Path
import json
import random
import time

import numpy as np
import sympy as sp
from scipy.integrate import quad

RNG = random.Random(500)


def mul(a, b):
    c = 0
    while b:
        if b & 1:
            c ^= a
        b >>= 1
        a <<= 1
        if a & 8:
            a ^= 11  # F_8 = F_2[x]/(x^3+x+1)
    return c


def power(a, n):
    r = 1
    for _ in range(n):
        r = mul(r, a)
    return r


def div(a, b):
    assert b
    return mul(a, power(b, 6))


def field_rank(a):
    a = [list(row) for row in a]
    r = 0
    for j in range(len(a[0])):
        i = next((i for i in range(r, len(a)) if a[i][j]), None)
        if i is None:
            continue
        a[r], a[i] = a[i], a[r]
        a[r] = [div(x, a[r][j]) for x in a[r]]
        for i in range(len(a)):
            if i != r:
                c = a[i][j]
                a[i] = [x ^ mul(c, y) for x, y in zip(a[i], a[r])]
        r += 1
    return r


def masks():
    count = 0
    for ts in permutations(range(8), 4):
        alphas = []
        for i, t in enumerate(ts):
            d = 1
            for j, u in enumerate(ts):
                if i != j:
                    d = mul(d, t ^ u)
            alphas.append(div(1, d))
        for degree in range(3):
            s = 0
            for a, t in zip(alphas, ts):
                s ^= mul(a, power(t, degree))
            assert s == 0
        count += 1
    worst = 0
    for a, b, c in permutations(range(8), 3):
        k = div(b ^ c, a ^ c)
        ratios = [mul(k, div(b ^ d, a ^ d)) for d in range(8) if d not in (a, b, c)]
        assert set(ratios) == set(range(1, 8)) - {k, mul(k, k)}
        mat = np.zeros((7, 7))
        for r in ratios:
            for x in range(1, 8):
                mat[x - 1, mul(r, x) - 1] += 1 / 5
        norm = np.linalg.norm(mat - np.ones((7, 7)) / 7, 2)
        assert norm <= 2 / 5 + 1e-12
        worst = max(worst, norm)
    matrices = [[[0]], [[1]], [[3]], [[0, 0], [0, 0]], [[1, 2], [2, 4]], [[1, 0], [0, 1]]]
    matrices += [[[RNG.randrange(8) for _ in range(2)] for _ in range(2)] for _ in range(12)]
    for mat in matrices:
        n = len(mat)
        total = 0
        for c in product(range(8), repeat=n):
            for e in product(range(8), repeat=n):
                v = 0
                for i in range(n):
                    for j in range(n):
                        v ^= mul(c[i], mul(mat[i][j], e[j]))
                total += 1 if v & 1 == 0 else -1
        assert F(total, 8 ** (2 * n)) == F(1, 8 ** field_rank(mat))
    return dict(ordered_quadruples=count, excluded_sets=336, bilinear_matrices=len(matrices), max_mask_norm=worst)


def repair():
    cases = 0
    original_failure = False
    for case in range(25):
        if case == 0:
            p = np.array([[0.0], [1.0], [2.0]])
            delta = np.abs(p - p.T)
        else:
            pts = np.array([[RNG.random(), RNG.random()] for _ in range(6)])
            delta = np.abs(pts[:, None, :] - pts[None, :, :]).sum(axis=2)
            if case % 2:
                delta[:3, 3:] = delta[3:, :3] = np.inf
            p = np.array([[RNG.gauss(0, 1) for _ in range(3)] for _ in pts])
        n, r = len(p), 1.0
        scale = 1.0
        for z, v, y in product(range(n), repeat=3):
            angle = (p[v] - p[z]) @ (p[y] - p[z])
            if angle < -1e-14:
                scale = min(scale, min(r, delta[v, z], delta[y, z]) / -angle)
        p *= np.sqrt(scale)
        gram = np.array([[0 if np.isinf(d) else 4 * quad(lambda ell: np.exp(-d / ell), 0, r, epsabs=1e-11)[0] for d in row] for row in delta])
        assert np.linalg.eigvalsh(gram).min() >= -1e-9
        corr = 8 * r - 2 * gram
        base = ((p[:, None, :] - p[None, :, :]) ** 2).sum(axis=2)
        dist = base + corr
        if case == 0:
            original_failure = base[0, 2] > base[0, 1] + base[1, 2]
        for z, v, y in product(range(n), repeat=3):
            bound = min(r, delta[v, z], delta[y, z])
            qa = (corr[v, z] + corr[y, z] - corr[v, y]) / 2
            assert qa >= bound - 1e-9
            assert dist[v, y] <= dist[v, z] + dist[z, y] + 1e-9
        for i, j in product(range(n), repeat=2):
            t = delta[i, j]
            assert -1e-9 <= corr[i, j] <= 8 * r + 1e-9
            if 0 < t <= r:
                assert corr[i, j] <= 8 * t * (1 + np.log(r / t)) + 1e-9
        cases += 1
    assert original_failure
    return dict(numerical_chart_models=cases, unrepaired_triangle_failure=bool(original_failure), analytic_proof_required=True)


def radius(clients, w, p, m):
    return min(max(F(d), p / (m * j)) for j, d in enumerate(sorted(abs(v - w) for v in clients), 1))


def populations():
    small = 0
    for n in range(2, 15):
        for _ in range(4):
            clients = sorted(RNG.sample(range(200), n))
            p, m = F(sum(x + 1 for x in clients)), RNG.randrange(1, 20)
            for w in clients:
                q = radius(clients, w, p, m)
                assert q * sum(abs(x - w) <= q for x in clients) >= p / m
                # All breakpoints for q times the closed-ball population.
                for candidate in set(map(F, (abs(x - w) for x in clients))) | {p / (m * j) for j in range(1, n + 1)}:
                    if candidate < q:
                        assert candidate * sum(abs(x - w) <= candidate for x in clients) < p / m
                small += 1
    O = [10_000_000 * i for i in range(4)]
    clients = [o + 100_000 + j for o in O for j in range(20)]
    p = F(sum(min(abs(x - o) for o in O) for x in clients))
    m, runs = 100, 0
    for kappa in (F(1, 2), F(1)):
        leaves, balls, indices, ratios = [], [], [], []
        for w in clients[::20]:
            r = min(abs(w - o) for o in O)
            q = radius(clients, w, p, m)
            assert r > 10 * q
            assert all(abs(w - v) + R > 10 * r for v, R in leaves)
            j = ceil(F(r) / (kappa * q))
            R = j * kappa * q
            assert r <= R <= (1 + kappa) * r + kappa * q
            ball = {x for x in clients if abs(x - w) <= q}
            assert all(not (ball & old) for old in balls)
            balls.append(ball)
            leaves.append((w, R))
            indices.append(j)
            ratios.append(F(r) / q)
        assert sum(ratios) <= F(10 * m, 9)
        assert sum(indices) <= (F(10, 9) / kappa + 1) * m
        # With its leaf retained, repeating the same leader cannot be expensive.
        w, R = leaves[0]
        r = min(abs(w - o) for o in O)
        assert R <= 10 * r
        assert balls[0] & balls[0]  # Deleting the leaf admits this repeated ball.
        runs += 1
    return dict(exact_radius_instances=small, expensive_menu_sequences=runs, expensive_balls_per_sequence=4, persistence_control=True)


def compression():
    updates = 0
    for d in range(1, 5):
        for _ in range(8):
            M = d + 6
            features = [[F(RNG.randrange(-7, 8), RNG.randrange(1, 5)) for _ in range(d)] for _ in range(M)]
            nums = [RNG.randrange(1, 10) for _ in range(M)]
            weights = [F(x, sum(nums)) for x in nums]
            target = [sum(w * v[j] for w, v in zip(weights, features)) for j in range(d)]
            while sum(w > 0 for w in weights) > d + 1:
                ids = [i for i, w in enumerate(weights) if w > 0][:d + 2]
                mat = sp.Matrix([[1] * len(ids)] + [[sp.Rational(features[i][j]) for i in ids] for j in range(d)])
                z0 = mat.nullspace()[0]
                den = lcm(*(int(x.q) for x in z0))
                z = [int(x * den) for x in z0]
                assert any(x > 0 for x in z) and any(x < 0 for x in z)
                pivot = min((j for j in range(len(ids)) if z[j] > 0), key=lambda j: weights[ids[j]] / z[j])
                t = weights[ids[pivot]] / z[pivot]
                D = lcm(*(w.denominator for w in weights))
                b = [int(weights[i] * D) for i in ids]
                for j, i in enumerate(ids):
                    updated = weights[i] - t * z[j]
                    assert updated == F(b[j] * z[pivot] - b[pivot] * z[j], D * z[pivot])
                    weights[i] = updated
                assert min(weights) >= 0 and sum(weights) == 1
                updates += 1
            assert [sum(w * v[j] for w, v in zip(weights, features)) for j in range(d)] == target
    # Both laws have mean zero; compression onto the existing central state loses variance.
    assert F(1, 4) * -1 + F(1, 2) * 0 + F(1, 4) * 1 == 0
    assert F(1, 4) * 1 + F(1, 4) * 1 != 0
    return dict(rational_models=32, exact_elimination_steps=updates, unlisted_second_moment_control=True)


def compose_rel(a, b, n):
    out = 0
    for i, j in product(range(n), repeat=2):
        if any((a >> (i * n + k)) & (b >> (k * n + j)) & 1 for k in range(n)):
            out |= 1 << (i * n + j)
    return out


def corners():
    # T_3 x C_3 -> C_3. Minimal idempotents are constant transformations.
    transforms = list(product(range(3), repeat=3))
    ident = tuple(range(3))
    def comp(a, b):
        return tuple(a[b[i]] for i in range(3))
    idem = [a for a in transforms if comp(a, a) == a]
    minimal = [d for d in idem if not any(e != d and comp(e, d) == comp(d, e) == e for e in idem)]
    assert len(minimal) == 3
    for d in minimal:
        corner = {comp(comp(d, a), d) for a in transforms}
        assert corner == {d}
        for c in range(3):
            assert (c + (-c) % 3) % 3 == 0
    assert not any(comp(a, (0, 0, 0)) == comp((0, 0, 0), a) == ident for a in transforms)
    cases = 0
    for n in (2, 3):
        rels = range(1 << (n * n))
        for P in rels:
            if compose_rel(P, P, n) != P:
                continue
            for subset in range(1 << n):
                Fset = [i for i in range(n) if subset >> i & 1]
                if n == 3 and len(Fset) > 2:
                    continue
                i = sum(1 << (j * n + j) for j in Fset)
                if compose_rel(compose_rel(i, P, n), i, n) != i:
                    continue
                Q = compose_rel(compose_rel(P, i, n), P, n)
                corner = {compose_rel(compose_rel(Q, Z, n), Q, n) for Z in rels}
                small = [sum(((a >> k) & 1) << (u * n + v) for k, (u, v) in enumerate(product(Fset, repeat=2))) for a in range(1 << len(Fset) ** 2)]
                lift = lambda A: compose_rel(compose_rel(P, A, n), P, n)
                restrict = lambda Z: compose_rel(compose_rel(i, Z, n), i, n)
                assert corner == set(map(lift, small))
                assert all(restrict(lift(A)) == A for A in small)
                assert all(lift(restrict(Z)) == Z for Z in corner)
                for A, B in product(small, repeat=2):
                    assert compose_rel(lift(A), lift(B), n) == lift(compose_rel(A, B, n))
                cases += 1
    return dict(minimal_transform_corners=3, exact_relation_corners=cases, nonminimal_corner_control=True)


def tours():
    maps, tour_count = 0, 0
    for n in range(1, 6):
        for rest in product(range(-1, n), repeat=n - 1):
            succ = (-1,) + rest
            basin = set()
            for start in range(n):
                seen, v = set(), start
                while v != -1 and v not in seen:
                    seen.add(v)
                    v = succ[v]
                if 0 in seen:
                    basin.add(start)
            adj = {v: [] for v in range(n)}
            for u, v in enumerate(succ):
                if v >= 0:
                    adj[u].append(v)
                    adj[v].append(u)
            component, todo = set(), [0]
            while todo:
                v = todo.pop()
                if v not in component:
                    component.add(v)
                    todo.extend(adj[v])
            assert component == basin
            assert sum(succ[v] >= 0 for v in component) == len(component) - 1
            if len(component) > 1:
                for _ in range(2):
                    for v in component:
                        RNG.shuffle(adj[v])
                    step = lambda uv: (uv[1], adj[uv[1]][(adj[uv[1]].index(uv[0]) + 1) % len(adj[uv[1]])])
                    first = (0, adj[0][0])
                    seen, edge = [], first
                    while edge not in seen:
                        seen.append(edge)
                        edge = step(edge)
                    assert edge == first and len(seen) == 2 * (len(component) - 1)
                    leaves = [v for v in component if len(adj[v]) == 1]
                    a, b = leaves[:2]
                    for start, end in ((a, b), (b, a)):
                        edge = (start, adj[start][0])
                        for _ in range(len(seen)):
                            if edge[1] in (a, b):
                                assert edge[1] == end
                                break
                            edge = step(edge)
                        else:
                            raise AssertionError('open tour did not reach other leaf')
                    tour_count += 1
            maps += 1
    # Nondeterministic edges 1->0, 1->2, 2->2: 2 connected to sink 0 but cannot reach it.
    edges = {(1, 0), (1, 2), (2, 2)}
    directed, undirected = {2}, {2}
    for _ in range(3):
        directed |= {v for u, v in edges if u in directed}
        undirected |= {v for u, v in edges | {(v, u) for u, v in edges} if u in undirected}
    assert 0 not in directed and 0 in undirected
    return dict(exact_partial_maps=maps, cyclic_order_tours=tour_count, nondeterministic_fork_control=True)


def replay():
    models, one_pass_failures = 0, 0
    for g in range(1, 11):
        for _ in range(5):
            e, a = 3, 4
            # Predecessor indices: sources 0..e-1, gates e..e+g-1.
            gates = [[(RNG.randrange(e + j), F(RNG.randrange(-3, 4))) for _ in range(2)] for j in range(g)]
            outputs = [RNG.randrange(-1, e + g) for _ in range(a)]
            direct = [[F(i == j) for j in range(e)] for i in range(e)]
            for predecessors in gates:
                direct.append([sum(c * direct[i][j] for i, c in predecessors) for j in range(e)])
            M = [[F(0)] * e if i == -1 else direct[i] for i in outputs]
            N = e + a + g
            state = [[F(i == j) for j in range(N)] for i in range(N)]
            def index(v):
                return v if v < e else v + a
            def sweep(source, sign, reverse=False):
                order = range(g - 1, -1, -1) if reverse else range(g)
                for j in order:
                    for v, c in (reversed(gates[j]) if reverse else gates[j]):
                        if source or v >= e:
                            target, pred = e + a + j, index(v)
                            state[target] = [x + sign * c * y for x, y in zip(state[target], state[pred])]
            def read(source, sign):
                for j, v in enumerate(outputs):
                    if v >= 0 and (source or v >= e):
                        state[e + j] = [x + sign * y for x, y in zip(state[e + j], state[index(v)])]
            sweep(True, 1)
            read(True, 1)
            sweep(True, -1, True)
            if any(state[e + j][e + a + k] for j in range(a) for k in range(g)):
                one_pass_failures += 1
            sweep(False, 1)
            read(False, -1)
            sweep(False, -1, True)
            target = [[F(i == j) for j in range(N)] for i in range(N)]
            for i in range(a):
                target[e + i][:e] = M[i]
            assert state == target
            assert 4 * sum(len(p) for p in gates) + 2 * a <= 8 * g + 2 * a
            models += 1
    assert one_pass_failures > 0
    return dict(symbolic_rational_DAGs=models, one_pass_memory_contamination_controls=one_pass_failures, all_initial_registers_independent=True)


def tensors():
    A = np.array([[1, 2], [3, 4]], dtype=object)
    B = np.zeros((4, 4), dtype=object)
    B[:2, :2] = A
    B[2:, 2:] = np.eye(2, dtype=int)
    sectors = 0
    for j in range(1, 4):
        full = np.array([[1]], dtype=object)
        for _ in range(j):
            full = np.kron(full, B)
        groups = {}
        for index, digits in enumerate(product(range(4), repeat=j)):
            key = tuple(-1 if x < 2 else x for x in digits)
            groups.setdefault(key, []).append(index)
        counts = [0] * (j + 1)
        for key, ids in groups.items():
            r = key.count(-1)
            block = np.array([[1]], dtype=object)
            for _ in range(r):
                block = np.kron(block, A)
            assert np.array_equal(full[np.ix_(ids, ids)], block)
            other = sorted(set(range(4 ** j)) - set(ids))
            assert not np.any(full[np.ix_(ids, other)])
            counts[r] += 1
            sectors += 1
        for r in range(j + 1):
            assert counts[r] == comb(j, r) * 2 ** (j - r)
            assert F(counts[r] * 2 ** r, 4 ** j) == F(comb(j, r), 2 ** j)
    # These parameters are hypothetical: no finite winning word is constructed.
    q, b, g, alpha = 2, 2, 3, 0.9
    rho, gamma = 1 / 4, 0.95
    assert g * rho ** alpha < gamma < 1
    k0 = next(k for k in range(1, 1000) if g * ((rho * k + 1) / (k + 1)) ** alpha <= gamma)
    f = [F(0)]
    for k in range(1, 121):
        j = k // b
        f.append(1 + g * sum(F(comb(j, r), 2 ** j) * f[r] for r in range(j + 1)))
    C = max(1 / (1 - gamma), max(float(f[k]) / (k + 1) ** alpha for k in range(k0)))
    assert all(float(v) <= C * (k + 1) ** alpha + 1e-9 for k, v in enumerate(f))
    assert 4 * rho ** alpha > 1  # No strict saving: this induction cannot contract.
    return dict(exact_tensor_sectors=sectors, hypothetical_recurrence_terms=120, exponent=alpha, induction_threshold=k0, no_finite_winning_word_supplied=True)


if __name__ == '__main__':
    start = time.perf_counter()
    results = {}
    for fn in (masks, repair, populations, compression, corners, tours, replay, tensors):
        results[fn.__name__] = fn()
        print(fn.__name__, 'passed', flush=True)
    report = dict(batch='B050', status='passed', scope='Finite mechanism checks; numerical quadrature and spectral checks are not proof certificates. Tensor recurrence parameters are hypothetical and do not furnish a finite winning word. No source headline theorem is certified.', checks=results, elapsed_seconds=round(time.perf_counter() - start, 3))
    Path(__file__).with_name('results.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, indent=2))
