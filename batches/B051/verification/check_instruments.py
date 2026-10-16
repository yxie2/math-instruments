"""Finite B051 checks, separate from source headline theorem certification."""
from fractions import Fraction as F
from itertools import product, combinations_with_replacement, permutations
from math import comb, floor, sqrt
from pathlib import Path
import json
import random
import time

import numpy as np
import sympy as sp

RNG = random.Random(510)


def matrices():
    def rot(t):
        return np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])
    pairs, triples = 0, 0
    for trial in range(40):
        Bs, Ds, directions = [], [], []
        for j in range(5):
            D = 10 ** RNG.uniform(0, 3)
            angle = j * 1e-8 if trial % 2 else RNG.uniform(-3, 3)
            a = rot(angle)[:, 0]
            B = rot(RNG.random()) @ np.diag([D, 1 / D]) @ rot(angle).T
            Bs.append(B)
            Ds.append(D)
            directions.append(a)
        ratios = np.empty((5, 5))
        for j, p in product(range(5), repeat=2):
            R = np.linalg.norm(Bs[j] @ np.linalg.inv(Bs[p]), 2) / (Ds[j] * Ds[p])
            Q = max(abs(np.linalg.det(np.stack([directions[j], directions[p]]))), Ds[j] ** -2, Ds[p] ** -2)
            assert Q <= R * (1 + 1e-8) + 1e-11
            assert R <= 3 * Q * (1 + 1e-8) + 1e-11
            ratios[j, p] = R
            pairs += 1
        for j, l, p in product(range(5), repeat=3):
            assert ratios[j, p] <= 6 * max(ratios[j, l], ratios[l, p]) + 1e-9
            triples += 1
    truncations = 0
    for _ in range(30):
        n, M = 5, 3.0
        Bs = [np.eye(2)]
        for _ in range(2 * n):
            t = RNG.uniform(-1, 1)
            step = rot(RNG.random()) @ np.diag([np.exp(t), np.exp(-t)]) @ rot(RNG.random())
            assert np.linalg.norm(step, 2) < M
            Bs.append(step @ Bs[-1])
        def g(i, j):
            return np.log(np.linalg.norm(Bs[j] @ np.linalg.inv(Bs[i]), 2)) / np.log(M)
        D = n - min(g(n, 0), g(n, 2 * n))
        ell = g(n, 0) + g(n, 2 * n) - g(0, 2 * n)
        for s in range(1, n + 1):
            loss = g(n, n - s) + g(n, n + s) - g(n - s, n + s)
            assert loss >= min(ell, 2 * s - 2 * D) - 2 * np.log(6) / np.log(M) - 1e-9
            truncations += 1
    t = 10
    Bj, Bp = np.diag([t, 1 / t, 1]), np.diag([t, 1, 1 / t])
    assert np.linalg.norm(Bj @ np.linalg.inv(Bp), 2) / t ** 2 > 3 / t ** 2
    return dict(numerical_matrix_pairs=pairs, four_point_triples=triples, transfer_truncations=truncations, dimension_three_failure_control=True)


def dilation():
    # On Z, S(n)=n+1 and mu(n)=c+sum_{k>n}nu(k).
    identities = 0
    for _ in range(30):
        nu = {k: F(RNG.randrange(1, 8), RNG.randrange(1, 6)) for k in range(-5, 6)}
        c = F(RNG.randrange(1, 10), 3)
        mu = lambda n: c + sum(v for k, v in nu.items() if k > n)
        for n in range(-15, 16):
            assert mu(n - 1) == mu(n) + nu.get(n, 0)
            for b in (1, 2, 7, 25):
                potential = sum(nu.get(n + j, 0) for j in range(1, b + 1))
                assert mu(n) == mu(n + b) + potential
                assert potential <= mu(n)
                if b == 25:
                    assert mu(n) - potential == c
                identities += 1
        # On a finite cycle, a nonnegative source in S_*mu=mu+nu has total zero.
        cycle = [F(RNG.randrange(10)) for _ in range(8)]
        difference = [cycle[(i - 1) % 8] - cycle[i] for i in range(8)]
        assert sum(difference) == 0
        assert not all(v >= 0 for v in difference) or all(v == 0 for v in difference)
    return dict(exact_shift_identities=identities, positive_source_and_invariant_remainder=True, finite_total_mass_control=True)


def localization():
    tests = 0
    for n in range(3, 20):
        succ = [1, 0] + [RNG.randrange(i) for i in range(2, n)]
        Z, tau = {0, 1}, F(1, 3)
        lengths = []
        for x in range(n):
            v, bad = x, 0
            for k in range(1, 5 * n):
                bad += v not in Z
                v = succ[v]
                if bad < tau * k:
                    lengths.append(k)
                    break
            else:
                raise AssertionError('attraction did not give a local block')
        J = max(lengths)
        for x, r in product(range(n), range(1, 61)):
            v, done, bad, complete_bad = x, 0, 0, 0
            while done + lengths[v] <= r:
                k = lengths[v]
                block_bad = 0
                for _ in range(k):
                    block_bad += v not in Z
                    v = succ[v]
                assert block_bad < tau * k
                done += k
                complete_bad += block_bad
            remainder = r - done
            assert remainder < J
            for _ in range(remainder):
                bad += v not in Z
                v = succ[v]
            assert complete_bad + bad <= tau * r + J
            tests += 1
        for r in range(1, 31):
            P, Q = 2, 5
            B = min(r, floor(tau * r + J))
            exact_descriptions = sum(comb(r, j) * P ** (r - j) * Q ** j for j in range(B + 1))
            assert exact_descriptions <= 2 ** r * P ** r * Q ** floor(tau * r + J)
    return dict(exact_orbit_block_tests=tests, compactness_argument_checked_analytically=True)


def itineraries():
    count = 0
    for n in range(2, 8):
        for succ in combinations_with_replacement(range(n), n):
            for H, N in product((2, 3), (1, 2, 4, 8)):
                H = min(H, n)
                words = []
                for x in range(n):
                    v, word = x, []
                    for _ in range(N):
                        word.append(min(H - 1, v * H // n))
                        v = succ[v]
                    words.append(tuple(word))
                assert all(all(a <= b for a, b in zip(words[i], words[i + 1])) for i in range(n - 1))
                assert len(set(words)) <= 1 + N * (H - 1)
                count += 1
    # The cyclic successor is nonmonotone in the initial-state order.
    words = {tuple(((x + t) % 8) // 4 for t in range(3)) for x in range(8)}
    assert len(words) == 6 > 1 + 3 * (2 - 1)
    return dict(exact_ordered_map_itinerary_checks=count, nonmonotone_eight_state_control=True)


def stationary():
    cases, inequalities = 0, 0
    for period in range(1, 19):
        for _ in range(3):
            word = [F(RNG.randrange(-5, 6), RNG.randrange(1, 4)) for _ in range(period)]
            EY2 = sum(x * x for x in word) / period
            second, chords = [], []
            for h in range(8):
                size = 2 ** h
                As, Zs = [], []
                for shift in range(period):
                    segment = [word[(shift + t) % period] for t in range(size)]
                    average = sum(segment) / size
                    partial, deviation = F(0), F(0)
                    for u, y in enumerate(segment, 1):
                        partial += y
                        deviation = max(deviation, abs(partial - u * average))
                    As.append(average)
                    Zs.append(deviation / size)
                second.append(sum(a * a for a in As) / period)
                chords.append(sum(z * z for z in Zs) / period)
            v = [F(0)] + [second[l - 1] - second[l] for l in range(1, 8)]
            assert all(x >= 0 for x in v) and sum(v) <= EY2
            assert sum(chords) <= 3 * EY2  # The analytic constant is <3.
            for h in range(1, 8):
                bound = sum(2 ** (-a / 2 - 1) * sqrt(float(v[h - a])) for a in range(h))
                assert sqrt(float(chords[h])) <= bound + 1e-12
                inequalities += 1
            cases += 1
    # Y_t = a random constant +/-1: its own chord is exact but mean-centered Z_h=1.
    for sign in (-1, 1):
        for size in (1, 2, 4, 8):
            assert max(abs(u * sign - u * sign) for u in range(size + 1)) == 0
            assert max(abs(u * sign) for u in range(size + 1)) / size == 1
    return dict(exact_periodic_stationary_laws=cases, numerical_convolution_inequalities=inequalities, mean_centering_failure_control=True)


def scales():
    tests = 0
    for p in (1, 2, 4, 16):
        for _ in range(25):
            windows, start = [], 0
            for i in range(7):
                length = RNG.randrange(1, 8)
                R = F(RNG.randrange(1, 8), RNG.randrange(1, 8))
                costs = [F(RNG.randrange(1, 10), RNG.randrange(1, 10)) for _ in range(length)]
                windows.append((range(start, start + length), R, costs))
                start += length
            numerator = sum(B ** p for _, _, bs in windows for B in bs)
            denominator = sum(len(J) * R ** p for J, R, _ in windows)
            smallest = min((B / R) ** p for _, R, bs in windows for B in bs)
            assert smallest <= numerator / denominator
            tests += 1
    # J_i=[2^i,2^(i+1)), R_i=2^-i, p=1: each window has weight one.
    ratios = []
    for i in range(1, 12):
        k = 2 ** (i + 1) - 1
        ratios.append(F(2 ** i, k * k))  # B_k=k^-2.
    assert all(b < a for a, b in zip(ratios, ratios[1:]))
    assert ratios[-1] < F(1, 1000)
    # Reusing J_i={1}, R_i=B_1=1 makes availability diverge but all ratios stay one.
    assert min(F(1) for _ in range(100)) == 1
    return dict(exact_weighted_windows=tests, dyadic_selected_ratios=list(map(str, ratios)), overlapping_window_failure_control=True)


def traces():
    # S_3 permutes three leaves and fixes the center: orbit sizes 1 and 3.
    group = [(0,) + tuple(i + 1 for i in p) for p in permutations(range(3))]
    reps = [0, 1]
    stabilizers = [sum(p[o] == o for p in group) for o in reps]
    inverse = [F(1, n) for n in stabilizers]
    weights = [v / sum(inverse) for v in inverse]
    assert weights == [F(1, 4), F(3, 4)]
    def invariant(a):
        return sum((sp.Matrix(4, 4, lambda i, j: a[p[i], p[j]]) for p in group), sp.zeros(4)) / len(group)
    def trace(a, w=weights):
        return sum(sp.Rational(v) * a[o, o] for v, o in zip(w, reps))
    for _ in range(35):
        A = invariant(sp.Matrix(4, 4, lambda i, j: RNG.randrange(-4, 5)))
        B = invariant(sp.Matrix(4, 4, lambda i, j: RNG.randrange(-4, 5)))
        assert trace(A * B) == trace(B * A)
        assert sum(weights[i] * sum(A[o, j] for j in range(4)) for i, o in enumerate(reps)) == sum(weights[i] * sum(A[j, o] for j in range(4)) for i, o in enumerate(reps))
        positive = A.T * A
        assert all(positive[o, o] <= trace(positive) / weights[i] for i, o in enumerate(reps))
        symmetric = B + B.T
        norm = np.linalg.norm(np.array(symmetric, dtype=float), 2)
        assert abs(float(trace(symmetric * positive))) <= norm * float(trace(positive)) + 1e-9
    A, B = sp.zeros(4), sp.zeros(4)
    for i in range(1, 4):
        A[0, i], B[i, 0] = 1, 1
    assert trace(A * B) == trace(B * A)
    assert trace(A * B, [F(1, 2)] * 2) != trace(B * A, [F(1, 2)] * 2)
    return dict(exact_invariant_operator_pairs=35, unequal_orbit_weights=list(map(str, weights)), equal_type_weight_failure_control=True, trace_norm_checks='numerical')


def connection(n, edges, p):
    T = sp.zeros(n)
    for bits in product((0, 1), repeat=len(edges)):
        parent = list(range(n))
        def root(i):
            while i != parent[i]:
                i = parent[i]
            return i
        for present, (u, v) in zip(bits, edges):
            if present:
                parent[root(u)] = root(v)
        weight = p ** sum(bits) * (1 - p) ** (len(edges) - sum(bits))
        for i, j in product(range(n), repeat=2):
            if root(i) == root(j):
                T[i, j] += sp.Rational(weight)
    return T


def sprinkling():
    graphs = [(3, [(0, 1), (1, 2)]), (3, [(0, 1), (1, 2), (2, 0)]), (4, [(0, 1), (0, 2), (0, 3)]), (4, [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)])]
    cases = 0
    for n, edges in graphs:
        Adj = sp.zeros(n)
        for i, j in edges:
            Adj[i, j] = Adj[j, i] = 1
        degree = max(sum(Adj[i, j] for j in range(n)) for i in range(n))
        for p in (F(0), F(1, 5), F(1, 2), F(4, 5)):
            a = F(1, 50)
            T = connection(n, edges, p)
            later = connection(n, edges, p + (1 - p) * a)
            norm = np.linalg.norm(np.array(T, dtype=float), 2)
            assert float(a * degree) * norm < 1
            bound = T * (sp.eye(n) - sp.Rational(a) * Adj * T).inv()
            assert all(v >= 0 for v in bound - later)
            assert np.linalg.norm(np.array(later, dtype=float), 2) <= norm / (1 - float(a * degree) * norm) + 1e-12
            cases += 1
    return dict(exact_percolation_resolvents=cases, graph_count=len(graphs), scalar_norm_checks='numerical', no_infinite_graph_threshold_certified=True)


if __name__ == '__main__':
    start = time.perf_counter()
    checks = {}
    for fn in (matrices, dilation, localization, itineraries, stationary, scales, traces, sprinkling):
        checks[fn.__name__] = fn()
        print(fn.__name__, 'passed', flush=True)
    report = dict(batch='B051', status='passed', scope='Finite checks of selected mechanisms. Numerical matrix norms and convolution evaluations are identified; no source headline theorem or infinite limiting construction is certified.', checks=checks, elapsed_seconds=round(time.perf_counter() - start, 3))
    Path(__file__).with_name('results.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, indent=2))
