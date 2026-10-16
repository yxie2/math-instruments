"""Finite checks for B009; these do not certify the global source theorems.

Run with Python and the packages in batches/verification-requirements.txt.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, product
from pathlib import Path
import json
import math
import numpy as np
from scipy.optimize import linprog

SEED = 328329330374
rng = np.random.default_rng(SEED)


def adaptive_return():
    cases = 0
    for dim in [1, 2, 5]:
        for _ in range(8):
            A = rng.normal(size=(dim, dim))
            A *= rng.uniform(.2, 1) / np.linalg.norm(A, 2)
            b = rng.normal(size=dim)
            b *= .5 * (1 - np.linalg.norm(A, 2)) / max(np.linalg.norm(b), 1e-9)
            points = rng.normal(size=(12, dim))
            points *= .5 / np.maximum(np.linalg.norm(points, axis=1), 1)[:, None]
            for n in [1, 2, 7, 31]:
                q = 1 - 1 / n
                R = np.linalg.solve(np.eye(dim) - q * A, (points / n + q * b).T).T
                defects = np.linalg.norm(R @ A.T + b - R, axis=1)
                assert np.max(defects) <= 1 / n + 1e-12
                assert np.all(np.linalg.norm(R - points, axis=1) <= (n - 1) * np.linalg.norm(points @ A.T + b - points, axis=1) + 1e-12)
                for i, j in combinations(range(len(points)), 2):
                    assert np.linalg.norm(R[i] - R[j]) <= np.linalg.norm(points[i] - points[j]) + 1e-12
                cases += 1
    # Two weak-limit targets +/- e_0 and orthogonal tail errors e_(m_i).
    # Distinct, adaptively growing indices do not alter their Gram matrix.
    tail = []
    last = 0
    for pairs in [1, 2, 8, 32, 128]:
        indices = []
        for i in range(2 * pairs):
            threshold = last + (i + 1) ** 2
            last = threshold + i + 1
            indices.append(last)
        assert len(set(indices)) == 2 * pairs
        # Use an exact Gram calculation for the specified number of distinct tails.
        squared_return_error = F(1, 2 * pairs)
        signs = [1 if i % 2 == 0 else -1 for i in range(2 * pairs)]
        gram_sum = sum(F(int(i == j) + signs[i] * signs[j]) for i in range(2 * pairs) for j in range(2 * pairs))
        assert gram_sum / (2 * pairs) ** 2 == squared_return_error
        tail.append({'selected_points': 2 * pairs, 'squared_return_error': str(squared_return_error)})
        last = 0
    return {'affine_resolvent_cases': cases, 'orthogonal_tail_models': tail,
            'scope': 'Finite resolvent and Gram identities, not compact-semigroup existence or a stopping-rate theorem.'}


def weighted_tree():
    weighted_cases = 0
    smallest = F(1)
    for depth in range(1, 7):
        leaves = list(product([0, 1], repeat=depth))
        weights = {s: math.prod(F(1, 101) if bit == 0 else F(100, 101) for bit in s) for s in leaves}
        smallest = min(smallest, min(weights.values()))
        assert sum(weights.values()) == 1
        d = {s: (F(-1) if s == (0,) * depth else F(1)) for s in leaves}
        E = F(0)
        for level in range(1, depth + 1):
            for v in product([0, 1], repeat=level):
                block = [s for s in leaves if s[:level] == v]
                Wv = sum(weights[s] for s in block)
                delta = sum(weights[s] * d[s] for s in block)
                deficit = Wv - delta
                assert deficit == sum(weights[s] * (1 - d[s]) for s in block)
                E += deficit
        bad = sum(weights[s] for s in leaves if d[s] <= F(1, 2))
        assert bad <= 2 * E
        weighted_cases += 1
    # A genuinely nonlinear tree: only consecutive root outputs are telescoped.
    depth = 4
    leaves = list(product([0, 1], repeat=depth))
    alpha = {v: float(rng.uniform(.02, .98)) for level in range(depth) for v in product([0, 1], repeat=level)}
    W = {(): 1.0}
    for level in range(depth):
        for v in product([0, 1], repeat=level):
            W[v + (0,)] = W[v] * alpha[v]
            W[v + (1,)] = W[v] * (1 - alpha[v])
    values = {s: float(rng.uniform(-.5, .5)) for s in leaves}
    def output(v):
        if len(v) == depth:
            return values[v]
        return math.tanh(alpha[v] * output(v + (0,)) + (1 - alpha[v]) * output(v + (1,)))
    outputs = [output(())]
    for s in reversed(leaves):
        values[s] = 0
        outputs.append(output(()))
    differences = dict(zip(reversed(leaves), np.array(outputs[:-1]) - np.array(outputs[1:])))
    assert abs(sum(differences.values()) - (outputs[0] - outputs[-1])) < 1e-12
    for s in leaves:
        assert abs(differences[s]) <= W[s] + 1e-12
    return {'exact_weighted_trees': weighted_cases, 'smallest_leaf_weight': str(smallest),
            'nonlinear_leaf_switches': len(leaves)}


def partition_compression():
    profile_checks = 0
    for h in [2, 8, 26, 80, 242]:
        gamma = np.log(np.arange(2, h + 2) / np.arange(1, h + 1)) / math.log(h + 1)
        assert abs(sum(gamma) - 1) < 1e-12
        for d in list(range(3 * h + 4)) + [float('inf')]:
            phi = max(0, 1 - math.log1p(d) / math.log1p(h))
            exact = sum(gamma[j] for j in range(h) if d <= j)
            dilated = sum(gamma[j] for j in range(h) if d <= 3 * j + 2)
            assert abs(exact - phi) < 1e-12
            assert dilated <= phi + math.log(3) / math.log(h + 1) + 1e-12
            profile_checks += 1
    examples = 0
    max_error = 0
    for n, u, q, theta, h in [(12, 3, 6, .5, 8), (25, 4, 10, .25, 80), (8, 2, 8, .5, 8)]:
        labels = rng.integers(q, size=(u, n))
        Ts = [T for size in range(1, u + 1) for T in combinations(range(u), size) if u - size <= theta * u]
        distances = []
        for T in Ts:
            adjacent = np.any(labels[list(T), :, None] == labels[list(T), None, :], axis=0)
            distance = np.where(adjacent, 1., np.inf)
            np.fill_diagonal(distance, 0)
            for k in range(n):
                distance = np.minimum(distance, distance[:, k, None] + distance[None, k, :])
            distances.append(distance)
        columns = [(v, ti) for ti in range(len(Ts)) for v in range(n)]
        column_distance = np.array([distances[ti][:, v] for v, ti in columns]).T
        profiles = np.maximum(0, 1 - np.log1p(column_distance) / math.log1p(h))
        gamma = np.log(np.arange(2, h + 2) / np.arange(1, h + 1)) / math.log1p(h)
        slots = math.ceil(1 / theta)
        mesh = theta / (slots * 2 ** u)
        previous_pair = None
        for _ in range(12):
            mu = rng.random(len(columns)) ** 5
            mu *= rng.uniform(.6, 1) / sum(mu)
            omissions = [sum(mu[k] for k, (_, ti) in enumerate(columns) if i not in Ts[ti]) for i in range(u)]
            i0 = int(np.argmin(omissions))
            assert omissions[i0] <= theta + 1e-12
            eligible = np.array([i0 in Ts[ti] for _, ti in columns])
            representatives = {label: int(np.flatnonzero(labels[i0] == label)[0]) for label in set(labels[i0])}
            approximation = np.zeros(n)
            for j in range(h):
                memberships = (column_distance <= j) & eligible[None, :]
                assigned = np.full(len(columns), -1)
                pivots = []
                while True:
                    residual = (memberships & (assigned[None, :] < 0)) @ mu
                    if max(residual) <= theta + 1e-13:
                        break
                    pivot = int(np.argmax(residual))
                    chosen = memberships[pivot] & (assigned < 0)
                    assigned[chosen] = len(pivots)
                    pivots.append(pivot)
                assert len(pivots) <= slots
                level = np.zeros(n)
                rounded = np.zeros(n)
                for slot, pivot in enumerate(pivots):
                    representative = representatives[labels[i0, pivot]]
                    for ti, T in enumerate(Ts):
                        selected = [k for k, (_, t) in enumerate(columns) if t == ti and assigned[k] == slot]
                        w = sum(mu[k] for k in selected)
                        indicator = distances[ti][:, representative] <= 2 * j + 1
                        for k in selected:
                            v = columns[k][0]
                            assert distances[ti][v, representative] <= j + 1
                        level += w * indicator
                        rounded += mesh * math.floor(w / mesh) * indicator
                original = (column_distance <= j) @ mu
                expanded = (column_distance <= 3 * j + 2) @ mu
                assert np.all(level >= original - 2 * theta - 1e-12)
                assert np.all(level <= expanded + 1e-12)
                assert np.max(level - rounded) <= theta + 1e-12
                approximation += gamma[j] * rounded
            original = profiles @ mu
            assert np.all(approximation >= original - 3 * theta - 1e-12)
            assert np.all(approximation <= original + theta + 1e-12)
            max_error = max(max_error, float(np.max(abs(approximation - original))))
            if previous_pair is not None:
                old_original, old_approximation = previous_pair
                # Halving ensures the combined signed coefficient norm is at most one.
                signed_error = ((approximation - old_approximation) - (original - old_original)) / 2
                assert np.max(abs(signed_error)) <= 6 * theta + 1e-12
            previous_pair = original, approximation
            examples += 1
    return {'profile_distance_checks': profile_checks, 'coefficient_examples': examples,
            'maximum_uniform_error': max_error, 'scope': 'Explicit greedy encodings, not enumeration of the entire universal list or finite-field row separation.'}


def polar_conversion():
    cases = 0
    for rows, columns in [(3, 2), (4, 3), (2, 5)]:
        A = rng.integers(-2, 3, size=(rows, columns)).astype(float)
        if len(set(map(tuple, A))) != rows:
            continue
        for _ in range(50):
            x, y = rng.normal(size=(2, columns))
            x /= max(1, sum(abs(x)))
            y /= max(1, sum(abs(y)))
            delta = x - y
            t = .07
            support = max(3 * sign * row @ delta + t * np.array(cube) @ delta for row in A for sign in [-1, 1] for cube in product([-1, 1], repeat=columns))
            exact = 3 * max(abs(A @ delta)) + t * sum(abs(delta))
            assert abs(support - exact) < 1e-11
            epsilon = max(abs(A @ delta)) / 2
            assert support <= 6 * epsilon + 2 * t + 1e-11
            cases += 1
        for i, j in combinations(range(rows), 2):
            assert max(abs(3 * A[i] - 3 * A[j])) >= 3
    # A kernel direction is invisible in column-function error but visible after thickening.
    A = np.array([[1., 1.], [-1., -1.]])
    delta = np.array([1., -1.])
    assert np.max(abs(A @ delta)) == 0
    assert .1 * sum(abs(delta)) == .2
    return {'support_and_cluster_checks': cases, 'thickening_kernel_control': .2}


def signed_tests():
    # State-dependent continuation records on finite paths; no arbitrary truncation of a cyclic record.
    record_checks = 0
    for n in [4, 8, 15]:
        compatible = rng.random((n, 5)) > .2
        transitions = rng.random((5, 5)) > .5
        transitions |= transitions.T
        np.fill_diagonal(transitions, True)
        @lru_cache(maxsize=None)
        def record(x, direction, state):
            y = x + direction
            if not 0 <= y < n or not compatible[x, state]:
                return 0
            successors = [j for j in range(5) if compatible[y, j] and transitions[state, j]]
            return max([0] + [1 + record(y, direction, j) for j in successors])
        records = {(x, direction, j): record(x, direction, j) for x in range(n) for direction in [-1, 1] for j in range(5)}
        for x in range(n - 1):
            for j, k in product(range(5), repeat=2):
                if compatible[x, j] and compatible[x + 1, k] and transitions[j, k]:
                    left_exception = records[x, 1, j] > records[x, -1, j]
                    right_exception = records[x + 1, -1, k] > records[x + 1, 1, k]
                    assert left_exception or right_exception
                    record_checks += 1
    signed_cases = 0
    points = np.arange(11, dtype=float)
    distance = abs(points[:, None] - points[None, :])
    L = 2.
    bx = np.maximum(0, L - abs(points - 2))
    by = np.maximum(0, L - abs(points - 8))
    for _ in range(200):
        Ex = rng.random(11) < .3
        Ey = rng.random(11) < .3
        # Exclude the opposite positive bump to make joint prescriptions consistent.
        Ex |= by > 0
        Ey |= bx > 0
        prescription = {}
        for i in range(11):
            if not Ex[i]:
                prescription[i] = bx[i]
            if not Ey[i]:
                if i in prescription:
                    assert prescription[i] == -by[i]
                prescription[i] = -by[i]
        f = np.zeros(11) if not prescription else np.clip(np.min(np.array([v + distance[i] for i, v in prescription.items()]), axis=0), -L, L)
        assert np.all(abs(f[:, None] - f[None, :]) <= distance + 1e-12)
        mu, nu = rng.normal(size=(2, 11))
        mu[0] += 1 - sum(mu)
        nu[0] += 1 - sum(nu)
        lower = mu @ bx + nu @ by - 2 * L * (sum(abs(mu[Ex])) + sum(abs(nu[Ey])))
        assert (mu - nu) @ f >= lower - 1e-11
        signed_cases += 1
    average_checks = 0
    for degree in [4, 10, 50]:
        for states in [1, 20, 500]:
            mass = rng.normal(size=states)
            choice = rng.integers(-1, degree, size=states)
            losses = [sum(abs(mass[choice == e])) for e in range(degree)]
            assert sum(losses) / degree <= sum(abs(mass)) / degree + 1e-10
            average_checks += 1
    assert abs(F(2) + F(-2)) == 0 and abs(F(2)) + abs(F(-2)) == 4
    return {'continuation_checks': record_checks, 'signed_extension_cases': signed_cases,
            'degree_average_models': average_checks, 'zero_signed_mass_positive_variation_control': 4}


def free_norm(coefficients, distance):
    n = len(coefficients)
    rows, bounds = [], []
    for i in range(n):
        for j in range(n):
            if i != j:
                row = np.zeros(n)
                row[i], row[j] = 1, -1
                rows.append(row)
                bounds.append(distance[i, j])
    solution = linprog(-np.asarray(coefficients), A_ub=rows, b_ub=bounds,
                       bounds=[(0, 0)] + [(None, None)] * (n - 1), method='highs')
    assert solution.success
    return -solution.fun


def metric_wedge():
    # Three finite path blocks based at their common left endpoint.
    points = [(0, 0)] + [(p, k) for p, length in enumerate([2, 3, 4], 1) for k in range(1, length + 1)]
    n = len(points)
    distance = np.array([[abs(a[1] - b[1]) if a[0] == b[0] else a[1] + b[1] for b in points] for a in points], dtype=float)
    for k in range(n):
        assert np.all(distance <= distance[:, k, None] + distance[None, k, :])
    checks = 0
    for p in [1, 2, 3]:
        retained = [0] + [i for i, (block, _) in enumerate(points) if block == p]
        retraction = [i if i in retained else 0 for i in range(n)]
        assert np.all(distance[np.ix_(retraction, retraction)] <= distance)
        for _ in range(12):
            c = rng.integers(-4, 5, size=n).astype(float)
            c[0] = 0
            full = free_norm(c, distance)
            cp = c.copy()
            cp[[i for i in range(n) if i not in retained]] = 0
            compressed = free_norm(cp, distance)
            assert compressed <= full + 1e-10
            assert .5 * sum(abs(c)) <= full + 1e-10
            assert full <= np.max(distance) * sum(abs(c)) + 1e-10
            checks += 1
    return {'metric_points': n, 'scalar_dual_optimization_cases': checks,
            'scope': 'Finite retractions and coefficient bounds; finite-dimensional spaces themselves have MAP.'}


def clip(poly, normal, offset):
    result = []
    if not poly:
        return result
    for a, b in zip(poly, poly[1:] + poly[:1]):
        va, vb = np.dot(normal, a) + offset, np.dot(normal, b) + offset
        inside_a, inside_b = va >= 0, vb >= 0
        if inside_a:
            result.append(a)
        if inside_a != inside_b:
            result.append(a + (b - a) * va / (va - vb))
    return result


def cell_moments(slopes, intercepts):
    masses, moments = [], []
    for i in range(len(slopes)):
        poly = [np.array(p, dtype=float) for p in [(-1, -1), (1, -1), (1, 1), (-1, 1)]]
        for j in range(len(slopes)):
            if i != j:
                poly = clip(poly, slopes[i] - slopes[j], intercepts[i] - intercepts[j])
        area = 0.
        first = np.zeros(2)
        for a, b in zip(poly, poly[1:] + poly[:1]):
            cross = a[0] * b[1] - a[1] * b[0]
            area += cross / 2
            first += (a + b) * cross / 6
        masses.append(area / 4)
        moments.append(first / 4)
    return np.array(masses), np.array(moments)


def moment_derivatives():
    exact_cases = 0
    for k in range(2, 9):
        endpoints = [F(-1)] + [F(-1) + F(2 * i, k) for i in range(1, k)] + [F(1)]
        for _ in range(20):
            speeds = [F(0)] + [F(int(x), 7) for x in rng.integers(-8, 9, size=k - 1)] + [F(0)]
            masses = [(endpoints[i + 1] - endpoints[i]) / 2 for i in range(k)]
            dm = [(speeds[i + 1] - speeds[i]) / 2 for i in range(k)]
            db = [(endpoints[i + 1] * speeds[i + 1] - endpoints[i] * speeds[i]) / 2 for i in range(k)]
            assert sum(db[i] ** 2 / masses[i] for i in range(k)) <= 162 * sum(dm[i] ** 2 / masses[i] for i in range(k))
            exact_cases += 1
    polygon_cases = 0
    maximum_ratio = 0.
    for n in [3, 4, 7]:
        for _ in range(20):
            angle = np.arange(n) * 2 * math.pi / n + rng.uniform(0, 1)
            slopes = np.c_[np.cos(angle), np.sin(angle)]
            c = rng.uniform(-.03, .03, size=n)
            q = rng.normal(size=n)
            mass, moment = cell_moments(slopes, c)
            assert min(mass) > 0
            assert abs(sum(mass) - 1) < 1e-12 and np.max(abs(sum(moment))) < 1e-12
            eps = 1e-5
            minus, bminus = cell_moments(slopes, c - eps * q)
            plus, bplus = cell_moments(slopes, c + eps * q)
            dm, db = (plus - minus) / (2 * eps), (bplus - bminus) / (2 * eps)
            lhs = sum(np.sum(db * db, axis=1) / mass)
            rhs_base = 2 * sum(dm * dm / mass)  # R^2=2 for the square.
            assert lhs <= 162 * rhs_base + 1e-8
            maximum_ratio = max(maximum_ratio, float(lhs / rhs_base))
            polygon_cases += 1
    # Uniform-box quantile midpoint: volume = product of mean side lengths.
    for dim in [1, 2, 5]:
        for _ in range(30):
            lengths = np.exp(rng.uniform(-3, 3, size=(2, dim)))
            midpoint_volume = np.prod(np.mean(lengths, axis=0))
            assert midpoint_volume >= np.sqrt(np.prod(lengths)) * (1 - 1e-12)
    return {'rational_interval_derivatives': exact_cases, 'polygon_derivatives': polygon_cases,
            'maximum_moment_to_mass_ratio_after_R_squared': maximum_ratio, 'box_couplings': 90}


def range_energy():
    examples = []
    for epsilon in [1., 1e-2, 1e-4, 1e-6, 1e-8]:
        # Weakly connected graph; Bq=Gq is a valid image-relative bound with C=1.
        conductance = np.array([[0., 1., 0., 0.], [1., 0., epsilon, 0.], [0., epsilon, 0., 1.], [0., 0., 1., 0.]])
        G = np.diag(conductance.sum(axis=1)) - conductance
        m = np.array([.1, .2, .3, .4])
        v = np.array([1., 2., -1., -2.])
        r = -v + m @ v
        target = m * r
        q = np.linalg.solve(G + np.ones((4, 4)) / 4, target)
        assert np.max(abs(G @ q - target)) < 2e-8
        assert abs(r @ (G @ q) + v @ (G @ q)) < 2e-8
        assert np.sqrt(m @ (r * r)) <= np.sqrt(m @ (v * v)) + 1e-12
        examples.append({'weak_edge': epsilon, 'preimage_norm': float(np.linalg.norm(q)), 'r_norm': float(np.sqrt(m @ (r * r)))})
    assert examples[-1]['preimage_norm'] > 1e6 * examples[0]['preimage_norm']
    return {'models': examples, 'scope': 'Abstract energy principle; the geometric moment estimate is tested separately.'}


def three_atom_transport():
    cases = []
    # Two-point Gauss integration on each sign-half is exact for the cubic slice formulas.
    nodes = [(.5 - 1 / (2 * math.sqrt(3)), .25), (.5 + 1 / (2 * math.sqrt(3)), .25)]
    for denominator in [3, 5, 10, 30, 100, 1000]:
        a, b = F(1, denominator), F(1, 2 * denominator)
        masses = np.array([float((1 - a) / 2), float((1 - a) / 2), float(a)])
        first = np.array([[-1., 0.], [1., 0.], [0., 0.]])
        second = first.copy()
        second[2, 1] = float(b)
        equalities = []
        for i in range(3):
            row = np.zeros((3, 3)); row[i] = 1
            equalities.append(row.ravel())
        for j in range(3):
            row = np.zeros((3, 3)); row[:, j] = 1
            equalities.append(row.ravel())
        squared = np.sum((first[:, None, :] - second[None, :, :]) ** 2, axis=2)
        for power, cost, expected in [(2, squared, a * b * b), (1, np.sqrt(squared), a * b)]:
            solved = linprog(cost.ravel(), A_eq=equalities, b_eq=np.r_[masses, masses], bounds=(0, None), method='highs')
            assert solved.success
            assert abs(solved.fun - float(expected)) < 1e-12
        symmetric = b / 2
        exact_map_squared = symmetric + a * b * b
        potential_squared = a * b * b / 3 - b ** 3 / 24
        assert potential_squared == F(5, 16) * a * b * b
        numeric_map = 0.
        numeric_potential = 0.
        for positive in [True, False]:
            for node, weight in nodes:
                t = node if positive else -node
                q = float(b) * abs(t)
                numeric_map += weight * (q + float(b * b) * (float(a) + float(b) * t))
                numeric_potential += weight * (float(a) * q * q + (q ** 3 / 3 if positive else -2 * q ** 3 / 3))
        assert abs(numeric_map - float(exact_map_squared)) < 1e-14
        assert abs(numeric_potential - float(potential_squared)) < 1e-14
        cases.append({'a': str(a), 'W2_squared': str(a * b * b), 'W1': str(a * b),
                      'map_L2_squared': str(exact_map_squared), 'potential_L2_squared': str(potential_squared)})
    return {'exact_formula_and_LP_examples': cases, 'transport_optimizations': 2 * len(cases),
            'scope': 'Analytic formulas and numerical LP cross-checks; no regression-based claim of an exponent.'}


CHECKS = [adaptive_return, weighted_tree, partition_compression, polar_conversion,
          signed_tests, metric_wedge, moment_derivatives, range_energy, three_atom_transport]
if __name__ == '__main__':
    results = {}
    for check in CHECKS:
        results[check.__name__] = check()
        print(check.__name__ + ': passed', flush=True)
    output = {'batch': 'B009', 'status': 'passed', 'seed': SEED,
              'scope': 'Nine groups of finite checks; no global, infinite-dimensional, Lean or priority certification.',
              'checks': results}
    Path(__file__).with_name('results.json').write_text(json.dumps(output, indent=2) + '\n', encoding='utf-8')
