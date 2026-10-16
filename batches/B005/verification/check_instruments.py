"""Selected finite checks; not a certification of infinite-volume source theorems."""
from fractions import Fraction as F
from itertools import combinations, permutations, product
import json
import math
from pathlib import Path
import numpy as np

RNG = np.random.default_rng(231234236)


def determinant(a):
    n = len(a)
    total = F(0)
    for p in permutations(range(n)):
        inversions = sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
        total += (-1) ** inversions * math.prod(a[i][p[i]] for i in range(n))
    return total


def covariance(states, weights):
    z = sum(weights)
    n = len(states[0])
    means = [sum(w * s[i] for s, w in zip(states, weights)) / z for i in range(n)]
    cov = [[sum(w * s[i] * s[j] for s, w in zip(states, weights)) / z - means[i] * means[j] for j in range(n)] for i in range(n)]
    return means, cov


def response_checks():
    count = 0
    graphs = [(3, [(0, 1), (1, 2), (0, 2)]), (4, list(combinations(range(4), 2))), (5, list(combinations(range(4), 2)) + [(3, 4)])]
    for n, edges in graphs:
        states = []
        for chosen in combinations(range(len(edges)), n - 1):
            seen = {0}
            for _ in range(n):
                for e in chosen:
                    u, v = edges[e]
                    if u in seen or v in seen:
                        seen.update([u, v])
            if len(seen) == n:
                states.append([int(i in chosen) for i in range(len(edges))])
        for trial in range(8):
            weights = [math.prod((1 + (i + trial) % 5) ** s[i] for i in range(len(edges))) for s in states]
            means, cov = covariance(states, list(map(F, weights)))
            for i, row in enumerate(cov):
                assert all(c <= 0 for j, c in enumerate(row) if j != i)
                assert sum(row) == 0
                assert sum(map(abs, row)) == 2 * means[i] * (1 - means[i]) <= F(1, 2)
            count += 1
    dpp_count = 0
    for trial in range(12):
        a = RNG.integers(-2, 3, (3, 3))
        lmat = a @ a.T + np.eye(3, dtype=int)
        states = list(product([0, 1], repeat=3))
        weights = []
        for s in states:
            idx = [i for i in range(3) if s[i]]
            principal = [[F(int(lmat[i, j])) for j in idx] for i in idx]
            weights.append(determinant(principal) * math.prod((i + 2) ** s[i] for i in range(3)))
        means, cov = covariance(states, weights)
        for i, row in enumerate(cov):
            assert all(c <= 0 for j, c in enumerate(row) if j != i)
            assert sum(map(abs, row)) <= 2 * means[i] * (1 - means[i]) <= F(1, 2)
        dpp_count += 1
    return dict(weighted_tree_examples=count, exact_determinantal_examples=dpp_count, arithmetic='rational', limitation='Finite covariance identities only; no infinite-forest construction is simulated.')


def picard_checks():
    errors = []
    previous = None
    max_ratio = 0.0
    for steps in [1024, 2048]:
        t = np.linspace(0, 0.75, steps + 1)
        w = np.array([np.sin((i + 1) * t) + offset for i, offset in enumerate([0, 1, -1, 100, -100])]).T
        z = w.copy()
        for k in range(8):
            field = 0.5 * z + 0.25 * np.roll(z, 1, axis=1) + 0.25 * np.roll(z, -1, axis=1)
            drift = 0.5 + 0.25 * np.tanh(field)
            integ = np.vstack([np.zeros(5), np.cumsum((drift[1:] + drift[:-1]) * (t[1] - t[0]) / 2, axis=0)])
            nxt = w + integ
            increment = float(np.max(np.abs(nxt - z)))
            bound = 0.25 ** k * t[-1] ** (k + 1) / math.factorial(k + 1)
            assert increment <= bound + 2e-10
            max_ratio = max(max_ratio, increment / bound)
            z = nxt
        if previous is not None:
            errors.append(float(np.max(np.abs(z[::2] - previous))))
        previous = z
    return dict(grids=[1024, 2048], iterations=8, max_majorant_ratio=max_ratio, grid_refinement_differences=errors, limitation='Deterministic finite path quadrature, with additive floating tolerance 2e-10; not Brownian sampling or a proof for countably many paths.')


def atomic_r(nodes, weights, x):
    if x == 0:
        return float(weights @ nodes)
    lo, hi = float(max(nodes)), float(max(nodes) + 1 / x)
    for _ in range(100):
        mid = (lo + hi) / 2
        if mid == lo or mid == hi:
            break
        if np.sum(weights / (mid - nodes)) > x:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2 - 1 / x


def triangular_r(x):
    # Density (4-lambda)/8 on [0,4]; H(4+)=1/2.
    if x == 0:
        return 4 / 3
    if x >= 0.5:
        return 4 - 1 / x
    lo, hi = 4.0, 4 + 1 / x
    for _ in range(100):
        mid = (lo + hi) / 2
        h = (4 - (mid - 4) * math.log1p(4 / (mid - 4))) / 8
        if h > x:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2 - 1 / x


def transform_checks():
    xs = np.r_[0, np.linspace(0.01, 1, 200)]
    target = np.array([triangular_r(float(x)) for x in xs])
    errors = []
    for n in [16, 32, 64]:
        nodes, weights = np.polynomial.legendre.leggauss(n)
        nodes = 2 * (nodes + 1)
        weights = weights * (4 - nodes) / 4
        assert abs(sum(weights) - 1) < 1e-12
        actual = np.array([atomic_r(nodes, weights, float(x)) for x in xs])
        errors.append(float(max(abs(actual - target))))
    assert errors[2] < errors[1] < errors[0]
    # Weak convergence to delta_0 with a vanishing atom at 3 violates edge convergence.
    outliers = [atomic_r(np.array([0.0, 3.0]), np.array([1 - p, p]), 1.0) for p in [0.1, 0.01, 0.001, 0.0001]]
    assert abs(outliers[-1] - 2) < 0.001 and outliers[-1] > 1.9
    return dict(atomic_approximations=[16, 32, 64], sampled_uniform_errors=errors, weak_only_negative_control=outliers, limitation='Sampled transform values, including an active capped branch; neither a uniform error enclosure nor a thermodynamic pressure computation.')


def multiplicity_checks():
    max_error, examples = 0.0, 0
    for n, spectrum, changed in [(5, [0, 0, 0, 2, 2], [0, 0, 2, 2, 2]), (6, [-1, -1, 0, 0, 3, 3], [-1, 0, 0, 0, 3, 3])]:
        spins = np.array(list(product([-1, 1], repeat=n)), dtype=float)
        delta = np.array(changed) - spectrum
        diameter = max(spectrum) - min(spectrum)
        for endpoint in [spectrum, changed]:
            groups = [np.flatnonzero(np.array(endpoint) == a) for a in sorted(set(endpoint))]
            relative = max(np.count_nonzero(delta[g]) / len(g) for g in groups)
            for _ in range(6):
                u, _ = np.linalg.qr(RNG.normal(size=(n, n)))
                projections = spins @ u.T
                energy = 0.5 * (projections ** 2) @ endpoint + spins @ RNG.normal(size=n)
                weights = np.exp(energy - max(energy))
                weights /= sum(weights)
                norms = weights @ (projections ** 2)
                perm_values = []
                for choices in product(*(list(permutations(g)) for g in groups)):
                    order = np.arange(n)
                    for g, p in zip(groups, choices):
                        order[g] = p
                    perm_values.append(float(delta @ norms[order] / (2 * n)))
                expected = sum(float(sum(delta[g])) * float(sum(norms[g])) / len(g) for g in groups) / (2 * n)
                error = abs(np.mean(perm_values) - expected)
                max_error = max(max_error, error)
                assert error < 2e-14
                assert abs(expected) <= diameter * relative / 2 + 1e-14
                examples += 1
    return dict(endpoint_examples=examples, max_block_averaging_error=max_error, limitation='Checks the endpoint symmetry algebra by finite permutations; does not approximate the full Haar expected pressure or certify an infinite-size limit.')


def kernel_checks():
    examples = 0
    for weights in [[F(1), F(0), F(0)], [F(1, 2), F(1, 3), F(1, 6)], [F(0), F(1), F(0)]]:
        values = [-2, 1, 4]
        mean = sum(p * x for p, x in zip(weights, values))
        variance = sum(p * (x - mean) ** 2 for p, x in zip(weights, values))
        difference = sum(weights[i] * weights[j] * (values[i] - values[j]) ** 2 for i in range(3) for j in range(3))
        assert difference == 2 * variance
        assert (variance == 0) == (sum(p > 0 for p in weights) == 1)
        examples += 1
    return dict(exact_conditional_laws=examples, non_dirac_negative_control=True, limitation='Finite conditional variance identity only; Brownian compatibility and stochastic integral transport require the analytic argument.')


def critical_checks():
    count = 0
    c = 0.5
    for j in np.geomspace(1, 1e6, 70):
        for log_v in -np.geomspace(0.01, 1e4, 70):
            size = 1 + math.log(2) - log_v
            log_lhs = min(0.0, -c * j - log_v)
            assert log_lhs <= math.log(4 * size / j) + 1e-12
            count += 1
    cutoffs = 0
    for omega in [0.001, 0.01, 0.1, 1]:
        for size in np.geomspace(1.01, 1e6, 30):
            r = math.ceil(10 * (1 / omega + math.log(size))) + 1
            assert math.log(0.7 / 2) + 0.5 * r * math.log(2) >= math.log(2 * size)
            cutoffs += 1
    # Integrate after t=exp(-u), avoiding a numerical singularity at t=0.
    nodes, weights = np.polynomial.legendre.leggauss(256)
    u = 1 + (nodes + 1) * 500
    numerical = float(500 * weights @ (np.exp(-u) + np.exp(-u / 4) + 1 / u ** 2))
    exact_truncated = math.exp(-1) - math.exp(-1001) + 4 * (math.exp(-0.25) - math.exp(-1001 / 4)) + 1 - 1 / 1001
    assert abs(numerical - exact_truncated) < 1e-9
    return dict(logarithmic_bad_event_examples=count, adaptive_cutoff_examples=cutoffs, coefficient_integral_on_zero_to_exp_minus_one=math.exp(-1) + 4 * math.exp(-0.25) + 1, quadrature_error=abs(numerical - exact_truncated), limitation='Scalar examples and integrability algebra; the critical information and weighted path estimates are not reproduced.')


if __name__ == '__main__':
    results = {name: fn() for name, fn in [('response', response_checks), ('picard', picard_checks), ('spectral_transform', transform_checks), ('multiplicity', multiplicity_checks), ('conditional_kernel', kernel_checks), ('critical_comparison', critical_checks)]}
    output = {'status': 'passed', 'numpy_version': np.__version__, 'seed': 231234236, 'scope': 'Selected finite checks, not proof or novelty certification.', 'checks': results}
    Path(__file__).with_name('results.json').write_text(json.dumps(output, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(output, indent=2))
