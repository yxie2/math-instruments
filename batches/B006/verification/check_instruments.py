"""Finite checks for selected planar-model mechanisms, not global scaling limits."""
from fractions import Fraction as F
from itertools import combinations, product
import json
import math
from pathlib import Path
import numpy as np

RNG = np.random.default_rng(225226233)


def energy_checks():
    count = 0
    max_ratio = 0.0
    for n in [3, 6, 9]:
        for _ in range(12):
            scale = float(RNG.uniform(0.2, 3))
            levels = np.r_[0, 0.5, RNG.uniform(1.1, 6, n - 2)] / scale
            energy = np.diag(levels)
            d = RNG.normal(size=(n, n))
            d = (d + d.T) / 2
            b1 = np.diag((levels <= 1 / scale).astype(float))
            b2 = np.diag((levels <= 2 / scale).astype(float))
            first = energy @ d - d @ energy
            double = d @ first - first @ d
            compression = np.linalg.norm(b2 @ d @ b2, 2)
            commutator = scale * np.linalg.norm(double, 2)
            lhs = np.linalg.norm(d @ b1, 2) ** 2
            rhs = 2 * compression ** 2 + commutator / 2
            assert lhs <= rhs + 1e-11
            max_ratio = max(max_ratio, lhs / rhs)
            u = RNG.normal(size=n) * np.diag(b1)
            u /= np.linalg.norm(u)
            identity_lhs = (d @ u) @ energy @ (d @ u)
            identity_rhs = 0.5 * u @ double @ u + (d @ u) @ d @ energy @ u
            assert abs(identity_lhs - identity_rhs) < 1e-10
            count += 1
    # Compression vanishes while the one-sided norm grows without a commutator bound.
    negative = []
    for magnitude in [1, 10, 100]:
        d = np.array([[0.0, magnitude], [magnitude, 0.0]])
        b = np.diag([1.0, 0.0])
        assert np.linalg.norm(b @ d @ b) == 0
        negative.append(float(np.linalg.norm(d @ b, 2)))
    return dict(examples=count, max_bound_ratio=max_ratio, compression_only_negative_control=negative, limitation='Finite Hermitian matrices; no infinite-operator domain verification or uniform lattice moment estimate.')


def variogram_checks():
    max_error, count = 0.0, 0
    for n in [4, 8, 12]:
        features = RNG.normal(size=(n, n))
        cov = features @ features.T
        variogram = np.diag(cov)[:, None] + np.diag(cov)[None, :] - 2 * cov
        for _ in range(20):
            w, v = RNG.normal(size=(2, n))
            w -= w.mean()
            v -= v.mean()
            error = abs(w @ cov @ v + 0.5 * w @ variogram @ v)
            max_error = max(max_error, float(error))
            assert error < 1e-10
            i, j, k, l = RNG.choice(n, 4, replace=False)
            direct = cov[i, k] - cov[i, l] - cov[j, k] + cov[j, l]
            four = 0.5 * (variogram[i, l] + variogram[j, k] - variogram[i, k] - variogram[j, l])
            assert abs(direct - four) < 1e-12
            count += 1
    max_ratio, same_cell = 0.0, 0
    for delta in [1, 0.1, 0.001, 1e-6]:
        for distance in np.geomspace(1e-9, 3, 80):
            x = np.array([0.3 * delta, 0.2 * delta])
            y = x + distance * np.array([0.6, 0.8])
            lattice = np.floor(x / delta) - np.floor(y / delta)
            same_cell += int(np.linalg.norm(lattice) == 0)
            value = 2 * math.log(max(1, np.linalg.norm(lattice)))
            ratio = abs(value - 2 * math.log(1 / delta)) / (1 + abs(math.log(distance)))
            max_ratio = max(max_ratio, ratio)
            assert ratio < 5
    return dict(covariance_examples=count, max_identity_error=max_error, rounding_examples=320, same_cell_examples=same_cell, max_rounding_ratio=max_ratio, limitation='Checks finite covariance cancellation and sampled rounding bounds. The finite weights are not asserted to be continuum finite-energy atomic measures.')


def insertion_checks():
    max_error, examples = 0.0, 0
    for n in [3, 5, 7, 11]:
        q = np.sqrt(2 / (n + 1)) * np.sin(np.pi * np.outer(np.arange(1, n + 1), np.arange(1, n + 1)) / (n + 1))
        assert np.linalg.norm(q.T @ q - np.eye(n)) < 1e-12
        constant = float(np.max(abs(q)) * math.sqrt(n))
        pairs = list(combinations(range(n), 2))
        for size in [1, max(2, n // 2), n]:
            selected = list(range(size))
            p = q[selected].T @ q[selected]
            matrix = np.empty((len(pairs), len(pairs)))
            for a, r in enumerate(pairs):
                for b, t in enumerate(pairs):
                    lhs = sum(np.linalg.det(q[np.ix_(ij, r)]) * np.linalg.det(q[np.ix_(ij, t)]) for ij in combinations(selected, 2))
                    rhs = np.linalg.det(p[np.ix_(r, t)])
                    max_error = max(max_error, abs(lhs - rhs))
                    assert abs(lhs - rhs) < 1e-12
                    assert abs(rhs) <= 2 * constant ** 4 * (size / n) ** 2 + 1e-12
                    matrix[a, b] = rhs
                    examples += 1
            left = np.exp(-np.arange(len(pairs)) / 2)
            right = np.exp(-np.arange(len(pairs)) / 3)
            damped = left[:, None] * matrix * right[None, :]
            bound = 2 * constant ** 4 * (size / n) ** 2 * sum(left) * sum(right)
            assert np.linalg.norm(damped, 2) <= bound + 1e-12
    state_examples, max_state_error = 0, 0.0
    for n in [3, 5, 7, 9]:
        p = (n - 1) // 2
        u = np.arcsinh(np.cos(np.pi * np.arange(1, p + 1) / (n + 1)))
        logs = np.r_[u, 0, -u[::-1]]
        for eta in [0.2, 1, 2]:
            t = eta * n
            direct = sum(math.exp(t * (np.dot(bits, logs) - sum(u))) for bits in product([0, 1], repeat=n))
            closed = 2 * float(np.prod((1 + np.exp(-t * u)) ** 2))
            max_state_error = max(max_state_error, abs(direct - closed))
            assert abs(direct - closed) < 1e-10
            state_examples += 1
    return dict(minor_examples=examples, max_minor_error=max_error, state_sum_examples=state_examples, max_state_sum_error=max_state_error, limitation='Finite mode-pair matrices and occupation sums; does not reproduce marked-cap partition normalization or a curve scaling limit.')


def chain_checks():
    count = 0
    min_ratio = None
    choices = [F(0), F(1, 4), F(1, 2)]
    for _ in range(2000):
        weights_u, weights_v, signs = [], [], []
        for chain in range(2):
            length = int(RNG.integers(0, 6))
            u, v = F(int(RNG.integers(0, 4))), F(int(RNG.integers(0, 4)))
            for depth in range(length):
                weights_u.append(u)
                weights_v.append(v)
                signs.append((-1) ** (depth + chain))
                u *= choices[int(RNG.integers(0, 3))]
                v *= choices[int(RNG.integers(0, 3))]
        value = -sum((weights_u[i] * weights_v[j] * signs[i] * signs[j] for i in range(len(signs)) for j in range(len(signs)) if i != j), F(0)) / 4
        assert value >= 0
        has_cross = any(weights_u[i] * weights_v[j] > 0 for i in range(len(signs)) for j in range(len(signs)) if i != j)
        if has_cross:
            q = min(w for w in weights_u + weights_v if w > 0)
            assert value >= q * q / 16
            ratio = value / (q * q)
            min_ratio = ratio if min_ratio is None else min(min_ratio, ratio)
        count += 1
    # Violating decay, the first and third equal-sign members can contribute negatively.
    u = [1, 0, 1]
    signs = [1, -1, 1]
    negative = -F(sum(u[i] * u[j] * signs[i] * signs[j] for i in range(3) for j in range(3) if i != j), 4)
    assert negative == -F(1, 2)
    return dict(exact_rational_examples=count, min_positive_ratio=str(min_ratio), nondecaying_negative_control=str(negative), limitation='Abstract one- and two-chain inequality only; does not enumerate planar cap diagrams or prove arch spanning.')


def projection_checks():
    max_error = 0.0
    for _ in range(30):
        a = RNG.normal(size=(5, 8))
        y = RNG.normal(size=(3, 8))
        full = y.T @ np.linalg.solve(y @ y.T, y)
        for r in [1, 2, 3]:
            partial = y[:r].T @ np.linalg.solve(y[:r] @ y[:r].T, y[:r])
            q = a @ full
            qr = a @ partial
            cov_residual = (a - q) @ (a - q).T
            identity = a @ a.T - q @ q.T
            error = np.linalg.norm(cov_residual - identity)
            max_error = max(max_error, float(error))
            assert error < 1e-10
            norm_tail = np.linalg.norm(q - qr, 'fro') ** 2
            variance_tail = np.trace(q @ q.T - qr @ qr.T)
            assert abs(norm_tail - variance_tail) < 1e-10
    # G_n observes (X,Z/n) fully. The limiting local field X loses Z, although F=(X,Z) stays fixed.
    residual_before = np.zeros((2, 2))
    residual_after = np.diag([0.0, 1.0])
    mismatch = float(np.linalg.norm(residual_after - residual_before))
    assert mismatch == 1
    return dict(gaussian_examples=90, max_covariance_error=max_error, disappearing_coordinate_residual_mismatch=mismatch, indicator_hidden_coordinate_correlation=1 / math.sqrt(2 * math.pi), limitation='Finite Gaussian projection algebra and a counterexample to a missing covariance hypothesis; not metric-graph Green convergence.')


def likelihood_checks():
    nodes, weights = np.polynomial.hermite.hermgauss(128)
    z = math.sqrt(2) * nodes
    weights /= math.sqrt(math.pi)
    max_error, count = 0.0, 0
    for shift in [0, 0.1, 0.5, 1, 2, 3]:
        likelihood = np.exp(shift * z - shift ** 2 / 2)
        for r in [1, 2, 3]:
            numerical = weights @ likelihood ** r
            exact = math.exp(r * (r - 1) * shift ** 2 / 2)
            relative_error = abs(numerical - exact) / exact
            max_error = max(max_error, float(relative_error))
            assert relative_error < 1e-11
            count += 1
    for distance in np.linspace(0, 8, 81):
        exact_l1 = 2 * math.erf(distance / (2 * math.sqrt(2)))
        assert exact_l1 <= min(2, distance) + 1e-14
    return dict(likelihood_moment_examples=count, max_relative_quadrature_error=max_error, shift_distance_examples=81, limitation='One-dimensional Gaussian identities after reduction to the shift direction; no random-domain or infinite-dimensional convergence is simulated.')


if __name__ == '__main__':
    result = {'status': 'passed', 'numpy_version': np.__version__, 'seed': 225226233, 'scope': 'Selected finite identities and negative controls; not proof or novelty certification.', 'checks': {name: fn() for name, fn in [('energy', energy_checks), ('variogram', variogram_checks), ('insertion', insertion_checks), ('alternating_chains', chain_checks), ('conditional_projection', projection_checks), ('likelihood', likelihood_checks)]}}
    Path(__file__).with_name('results.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))
