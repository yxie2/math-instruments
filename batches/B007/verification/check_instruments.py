"""Finite checks of selected auxiliary identities; not global number-theory proofs."""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, permutations, product
from functools import lru_cache
import json
import math
from pathlib import Path
import numpy as np

RNG = np.random.default_rng(12013020021)


def cut_sampling():
    count = 0
    worst_slack = math.inf
    for n in range(2, 8):
        signs = np.array(list(product([-1, 1], repeat=n)))
        matrices = []
        for _ in range(5):
            a = RNG.integers(-3, 4, size=(n, n)).astype(float)
            matrices.append((a + a.T) / 2)
        spike = np.zeros((n, n))
        spike[0, 1] = spike[1, 0] = 100
        matrices.extend([spike, np.zeros((n, n))])
        for a in matrices:
            sums = signs @ a.T
            best = int(np.argmax(np.sum(np.abs(sums), axis=1)))
            delta = signs[best]
            cut = float(np.sum(np.abs(sums[best])) / n)
            q = np.sum(a * a) / n
            d = np.max(np.sum(np.abs(a), axis=1))
            for m in range(1, n + 1):
                best_residual = 0.0
                average_sign_loss = 0.0
                subsets = list(combinations(range(n), m))
                for chosen in subsets:
                    j = list(chosen)
                    rest = [i for i in range(n) if i not in chosen]
                    estimate = n / m * (a[:, j] @ delta[j])
                    g = np.where(estimate >= 0, 1, -1)
                    residual = float(np.abs(a[np.ix_(rest, rest)].T @ g[rest]).sum() / n)
                    best_residual = max(best_residual, residual)
                    average_sign_loss += float((np.abs(sums[best]) - sums[best] * g).sum() / n)
                average_sign_loss /= len(subsets)
                assert average_sign_loss <= 2 * math.sqrt(n * q / m) + 1e-10
                bound = best_residual + 2 * math.sqrt(n * q / m) + 2 * m * d / n
                assert cut <= bound + 1e-10
                worst_slack = min(worst_slack, bound - cut)
                count += 1
    return {'cases': count, 'minimum_bound_slack': worst_slack,
            'scope': 'Exhaustive signs and column subsets for the deterministic inequality; no efficient optimization claim.'}


def adaptive_product_space():
    n = 6
    sites = np.array(list(product([0, 1], repeat=n)))
    def matrix(x):
        a = np.zeros((n, n))
        for i in range(n):
            for j in range(i):
                a[i, j] = a[j, i] = (i + j + 1) / 31 * (x[i] + x[j] - 0.8)
        return a
    arrays = np.array([matrix(x) for x in sites])
    q = float(np.max(np.mean(np.sum(arrays ** 2, axis=2), axis=0)))
    assignments = 0
    extension_cases = 0
    for sampled in range(n):
        rest = [i for i in range(n) if i != sampled]
        for bit in [0, 1]:
            mask = sites[:, sampled] == bit
            xs = sites[mask]
            mats = arrays[mask]
            for sign in [-1, 1]:
                gs = np.where(sign * mats[:, :, sampled] >= 0, 1, -1)
                col = np.einsum('sik,si->sk', mats[:, rest][:, :, rest], gs[:, rest])
                z = np.abs(col).sum(axis=1) / n
                mean_target = 0.0
                deviation = 0.0
                for pos, k in enumerate(rest):
                    means = {v: float(np.mean(col[xs[:, k] == v, pos])) for v in [0, 1]}
                    a = np.array([means[v] for v in xs[:, k]])
                    mean_target += np.abs(a).mean() / n
                    deviation += np.abs(col[:, pos] - a).mean() / n
                assert z.mean() <= mean_target + math.sqrt(q) + 1e-12
                assert deviation <= math.sqrt(q) + 1e-12
                sub = mats[:, rest][:, :, rest]
                degrees = np.max(np.abs(sub).sum(axis=2), axis=1)
                cutoff = float(np.median(degrees))
                good = degrees <= cutoff
                distance = np.sum(xs[:, None, rest] != xs[None, :, rest], axis=2)
                lip = 4 * cutoff / n
                idx = np.flatnonzero(good)
                assert np.all(np.abs(z[idx, None] - z[None, idx]) <= lip * distance[np.ix_(idx, idx)] + 1e-12)
                level = float(np.median(z) + 0.01)
                clamped = np.minimum(z, level)
                extension = np.minimum(level, np.min(clamped[None, idx] + lip * distance[:, idx], axis=1))
                assert np.max(np.abs(extension[idx] - clamped[idx])) < 1e-12
                assert np.all(np.abs(extension[:, None] - extension[None, :]) <= lip * distance + 1e-12)
                assert extension.mean() <= z.mean() + level * np.mean(~good) + 1e-12
                assignments += 1
                extension_cases += len(xs) ** 2
    return {'conditioned_assignments': assignments, 'extension_pair_checks': extension_cases,
            'scope': 'Exact finite product-space averages, conditional fluctuation bound and common-good-set extension; no asymptotic concentration certification.'}


def primitive_root(p):
    for g in range(2, p):
        if len({pow(g, k, p) for k in range(p - 1)}) == p - 1:
            return g
    raise AssertionError(p)


def affine_mixing():
    cases = 0
    mellin_cases = 0
    maximum_ratio = 0.0
    maximum_identity_error = 0.0
    for q in [3, 5, 7, 11, 17, 23]:
        fiber = Counter()
        for r in range(1, q):
            for s in range(1, q):
                inv = pow(r, -1, q)
                fiber[((s * inv) ** 2 % q, (s - s * s * inv) % q)] += 1
        assert fiber[(1, 0)] == q - 1
        assert max(v for k, v in fiber.items() if k != (1, 0)) <= 2
        root = primitive_root(q)
        chars = np.zeros((q - 1, q), dtype=complex)
        for k in range(q - 1):
            for j in range(q - 1):
                chars[k, pow(root, j, q)] = np.exp(2j * np.pi * k * j / (q - 1))
        exps = np.exp(-2j * np.pi * np.outer(np.arange(q), np.arange(q)) / q) / q
        vectors = []
        for _ in range(5):
            g = RNG.normal(size=q) + 1j * RNG.normal(size=q)
            g[0] = 0
            g /= np.sqrt(np.mean(np.abs(g) ** 2))
            vectors.append(g)
        spike = np.zeros(q, complex)
        spike[1] = math.sqrt(q)
        vectors.append(spike)
        for g in vectors:
            operator = np.zeros((q, q), dtype=complex)
            for t in range(q):
                for r in range(1, q):
                    operator[t, (r - r * r * t) % q] += np.conj(g[r]) / q
            projection = np.eye(q) - np.ones((q, q)) / q
            norm_sq = np.linalg.norm(operator @ projection, 2) ** 2
            bound = math.sqrt(3 / q)
            assert norm_sq <= bound + 1e-11
            maximum_ratio = max(maximum_ratio, norm_sq / bound)
            assert np.mean(np.abs(operator @ g) ** 2) <= abs(np.mean(g)) ** 4 + bound + 1e-11
            epsilon = np.max(np.abs((chars * g) @ exps.T))
            pchi = np.empty((q - 1, q), dtype=complex)
            for k in range(q - 1):
                f = g * np.conj(chars[k])
                for d in range(q):
                    pchi[k, d] = np.sum(f * np.conj(f[(np.arange(q) - d) % q])) / (q - 1)
            w = pchi @ exps.T
            expected_w = q / (q - 1) * np.abs((g * np.conj(chars)) @ exps.T) ** 2
            err = float(np.max(np.abs(w - expected_w)))
            maximum_identity_error = max(maximum_identity_error, err)
            assert err < 1e-11
            assert np.sum(np.abs(w) ** 2) <= 2 * q / (q - 1) + 1e-11
            for eta in chars:
                coeffs = (pchi * chars * eta) @ exps.T
                lhs = np.sum(np.abs(coeffs) ** 2, axis=0)
                rhs = q / (q - 1) * (epsilon ** 4 + math.sqrt(3 / q))
                assert np.max(lhs) <= rhs + 1e-10
                mellin_cases += q
            cases += 1
    return {'operator_cases': cases, 'mellin_frequency_cases': mellin_cases,
            'maximum_operator_bound_ratio': maximum_ratio,
            'maximum_autocorrelation_identity_error': maximum_identity_error,
            'scope': 'Finite prime fields; includes L2-normalized spikes and all character/frequency pairs.'}


@lru_cache(None)
def stirling(n, k):
    if n == k == 0:
        return 1
    if n == 0 or k == 0 or k > n:
        return 0
    return k * stirling(n - 1, k) + stirling(n - 1, k - 1)


def overlaps():
    records = []
    for r, m in [(2, 3), (3, 2), (4, 2)]:
        bad = 0
        total = 0
        for perm in permutations(range(r * m)):
            parent = list(range(2 * r))
            def find(x):
                while parent[x] != x:
                    x = parent[x]
                return x
            for position, variable in enumerate(perm):
                u, v = find(variable // m), find(r + position // m)
                parent[u] = v
            components = {}
            for v in range(2 * r):
                components.setdefault(find(v), [0, 0])[v // r] += 1
            assert all(a == b for a, b in components.values())
            bad += int(len(components) > 3 * r / 4)
            total += 1
        ar = sum(stirling(r, t) ** 2 * math.factorial(t) for t in range(1, r + 1))
        bound = ar * math.factorial(m) ** r * math.exp(r * m * (math.log(r) + 1) / 4)
        assert bad <= bound
        if r == 4:
            assert bad == math.factorial(r) * math.factorial(m) ** r
        records.append({'blocks': r, 'block_size': m, 'permutations': total, 'bad': bad})
    inequalities = 0
    for a in range(1, 21):
        for m in range(1, 21):
            assert math.factorial(a * m) <= math.factorial(m) ** a * a ** (a * m)
            inequalities += 1
    return {'enumerations': records, 'exact_factorial_checks': inequalities,
            'scope': 'Small complete permutation enumerations and exact factorial bounds, not growing-depth asymptotics.'}


def deletion():
    cases = 0
    tightest = F(1)
    for n in [7, 8, 9]:
        pool = tuple(range(n))
        for threshold in [1, 2, 3]:
            def record(a):
                return max(0, threshold - len(a))
            # The data depend only on the rank record, so equality of records implies stability.
            def marks(a):
                v = record(a)
                return {(2 * v) % n, (2 * v + 1) % n}
            for ell, length in [(1, 3), (2, 3), (3, 3)]:
                lhs = F(0)
                change = F(0)
                telescoped = F(0)
                for t in range(ell, ell + length):
                    subsets = list(combinations(pool, t))
                    for subset in subsets:
                        a = frozenset(subset)
                        weight = F(1, length * len(subsets) * t)
                        for q in subset:
                            smaller = a - {q}
                            assert record(smaller) >= record(a)
                            lhs += weight * (q in marks(a))
                            change += weight * (record(smaller) != record(a))
                            telescoped += weight * (record(smaller) - record(a))
                rhs = F(threshold, length) + F(2, n - ell - length + 2)
                assert change <= telescoped <= F(threshold, length)
                assert lhs <= rhs
                tightest = min(tightest, rhs - lhs)
                cases += 1
    # Constant record without stable data: each singleton marks its own element.
    # There is one mark per data value, yet the actual marked fraction is one, not 1/N.
    negative_n = 11
    assert F(1) > F(1, negative_n)
    return {'exact_subset_models': cases, 'minimum_slack': str(tightest),
            'negative_control': {'pool_size': negative_n, 'actual_fraction': 1,
                                 'invalid_bound_without_stability': str(F(1, negative_n))},
            'scope': 'Finite deletion lemma; polynomial heights and adaptive geometric patches are not computed.'}


def hilbert_series(h, a, b, q, e, limit):
    values = [0] * (limit + 1)
    values[0] = 1
    for weight in [1] + [a] * h + [b] * h:
        for n in range(weight, limit + 1):
            values[n] += values[n - weight]
    for degree in [q] * (h - 1) + [e]:
        values = [value - (values[n - degree] if n >= degree else 0) for n, value in enumerate(values)]
    return values


def weighted_hilbert():
    identities = 0
    for a1 in [F(1, 2), F(2), F(-3)]:
        for a2 in [F(1, 3), F(3), F(-2)]:
            # F1 = a1 + a2 + n, no factor extracted.
            n = -a1 - a2
            b1, b2 = n / a1 ** 2, (n - 1) / a2 ** 2
            assert a1 ** 2 * b1 == a2 ** 2 * b2 + 1
            assert a1 ** 2 * b1 + a1 + a2 == 0
            # F1 = a1 + a2*n, e1=1; C1=1+a1*a2*b1.
            n = -a1 / a2
            b1, b2 = n / a1 ** 2, (n - 1) / a2 ** 2
            assert a1 ** 2 * b1 == a2 ** 2 * b2 + 1
            assert 1 + a1 * a2 * b1 == 0
            identities += 2
    series = []
    for h, a, b, k, e in [(2, 1, 1, 2, 3), (2, 1, 2, 2, 4), (3, 2, 3, 2, 4), (3, 2, 4, 2, 6)]:
        q = k * a + b
        values = hilbert_series(h, a, b, q, e, 1200)
        lead = F(q ** (h - 1) * e, a ** h * b ** h * math.factorial(h))
        relative = [float(abs(F(values[n], n ** h) - lead) / lead) for n in [300, 600, 1200]]
        assert relative[-1] < relative[0]
        assert relative[-1] < 0.05
        series.append({'h': h, 'weights': [a, b], 'degrees': [q, e],
                       'leading_coefficient': str(lead), 'relative_errors_at_300_600_1200': relative})
    return {'rational_equation_checks': identities, 'series': series,
            'scope': 'Extracted-equation examples and formal Hilbert-series coefficients; no general irreducibility or saturation computation.'}


def sieve_path():
    # The common positive factor 2 exp(gamma) cancels, so set it to one.
    def phi(parity, s):
        if parity == 0:
            assert 1.98 <= s <= 4
            return s / (s - 1) - math.log(s - 1)
        assert 0.95 <= s <= 3
        return 1.0
    local = 0
    for s in np.linspace(1.98, 4, 80):
        # Integral from s-1 to 3 of (t+1)/t^2 plus the remaining phi_even(4).
        a = s - 1
        partial = math.log(3) - 1 / 3 - math.log(a) + 1 / a
        assert abs(phi(0, s) - partial - phi(0, 4)) < 1e-12
        local += 1
    max_error = 0.0
    for _ in range(150):
        s = float(RNG.uniform(1.99, 2.3))
        initial_s = s
        r = initial_r = float(RNG.uniform(10, 100))
        harmonic = probability = 1.0
        parity = 0
        exponents = []
        for _ in range(12):
            lower = s - 1 if parity == 0 else max(2, s - 1)
            upper = 3 if parity == 0 else 4
            t = float(RNG.uniform(max(lower, 0.95), upper))
            x = r / (t + 1)
            assert x <= r / s + 1e-12
            if exponents:
                assert x <= exponents[-1] + 1e-12
            exponents.append(x)
            kernel = (t + 1) / t ** 2 * phi(1 - parity, t) / phi(parity, s)
            harmonic *= 1 / (t + 1)
            probability *= kernel
            r, s, parity = r * t / (t + 1), t, 1 - parity
            converted = probability * (r / initial_r) ** 2 * phi(0, initial_s) / phi(parity, s)
            error = abs(converted / harmonic - 1)
            max_error = max(max_error, error)
            assert error < 1e-10
            for ell in [x / 2, x * 2]:
                assert all(v > ell for v in exponents) == (s < r / ell)
    return {'low_range_integral_checks': local, 'finite_prefixes': 1800,
            'maximum_relative_conversion_error': max_error,
            'scope': 'Explicit low-range derivative identities and finite path likelihoods; not infinite-tail normalization or renewal estimates.'}


def forbidden_classes():
    cases = []
    pair_count = 0
    perturbation_count = 0
    for primes in [[2, 3], [2, 3, 5], [2, 3, 5, 7]]:
        configurations = list(product(*[range(p) for p in primes]))
        v0 = math.prod(F(p - 1, p) for p in primes)
        for length in [3, 8, 13, 24]:
            indicators = np.array([[all(j % p != a for p, a in zip(primes, residues))
                                    for j in range(-3, length - 3)] for residues in configurations], dtype=int)
            total = len(configurations)
            assert all(F(int(n), total) == v0 for n in indicators.sum(axis=0))
            pair_sum = F(0)
            for h in range(1, length):
                direct = math.prod(F(p - (1 if h % p == 0 else 2), p) for p in primes)
                factor = F(2 if h % 2 == 0 else 0)
                for p in primes[1:]:
                    factor *= 1 - F(1, (p - 1) ** 2)
                    if h % p == 0:
                        factor *= 1 + F(1, p - 2)
                assert direct == v0 * v0 * factor
                assert F(int(np.sum(indicators[:, 0] * indicators[:, h])), total) == direct
                pair_sum += 2 * (length - h) * direct
                pair_count += 1
            mean = length * v0
            variance = sum((F(int(x)) - mean) ** 2 for x in indicators.sum(axis=1)) / total
            assert variance == length * v0 + pair_sum - mean ** 2
            # A finite positive measure with density between 1-zeta and 1+zeta.
            for zeta in [F(1, 10), F(1, 2)]:
                densities = [1 + zeta * (1 if index % 3 else -1) for index in range(total)]
                perturbed_var = sum(density * (F(int(x)) - mean) ** 2
                                    for density, x in zip(densities, indicators.sum(axis=1))) / total
                assert perturbed_var <= (1 + zeta) * variance
                for h in range(1, length):
                    joint = sum(densities[i] * int(indicators[i, 0] * indicators[i, h]) for i in range(total)) / total
                    independent = math.prod(F(p - (1 if h % p == 0 else 2), p) for p in primes)
                    assert joint <= (1 + zeta) * independent
                perturbation_count += 1
            cases.append({'primes': primes, 'length': length, 'mean': str(mean), 'variance': str(variance)})
    return {'models': cases, 'pair_factor_checks': pair_count, 'perturbed_measures': perturbation_count,
            'scope': 'Exact finite means, variances and multiplicative pair controls; no uniform asymptotic conclusion from the finite samples.'}


def main():
    checks = {}
    for name, function in [('cut_sampling', cut_sampling), ('adaptive_product_space', adaptive_product_space),
                           ('affine_mixing', affine_mixing), ('overlap_counting', overlaps),
                           ('adaptive_deletion', deletion), ('weighted_hilbert', weighted_hilbert),
                           ('sieve_path', sieve_path), ('forbidden_classes', forbidden_classes)]:
        checks[name] = function()
        print(name + ': passed', flush=True)
    result = {'batch': 'B007', 'status': 'passed', 'seed': 12013020021,
              'scope': 'Eight finite checks of extracted auxiliary mechanisms. No global number-theory theorem, asymptotic estimate, Lean proof or novelty claim is certified.',
              'checks': checks}
    Path(__file__).with_name('results.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
