"""Selected finite checks for B053, with explicit controls and scope limits."""
from fractions import Fraction as F
from itertools import product
from math import comb, factorial, gcd, pi
from pathlib import Path
import json
import random
import time

import mpmath as mp
import numpy as np
import sympy as sp

RNG = random.Random(530)
mp.mp.dps = 75


def norm_inf(M):
    return max(sum(abs(M[i, j]) for j in range(M.cols)) for i in range(M.rows))


def particular_error():
    cases = remainders = 0
    for n in range(2, 6):
        for denominator in [10, 100, 1000]:
            eps = sp.Rational(1, denominator)
            A = sp.diag(1 / eps, *([1] * (n - 1)))
            P = A.row_join(sp.zeros(n, 1))
            J = A.inv().col_join(sp.zeros(1, n))
            R = sp.Matrix(n, n, [sp.Rational(RNG.randrange(-2, 3), 16 * n) for _ in range(n * n)])
            R[:, 0] = eps * R[:, 0]
            kernel = sp.zeros(n + 1, n)
            for j in range(1, n):
                kernel[n, j] = sp.Rational(RNG.randrange(-2, 3), 10)
            Dapp = J * (sp.eye(n) + R) + kernel
            D = Dapp * (sp.eye(n) + R).inv()
            assert P * Dapp == sp.eye(n) + R
            assert P * D == sp.eye(n)
            assert P.rank() == n < P.cols
            r = norm_inf(R)
            assert r <= sp.Rational(1, 4)
            assert norm_inf(D) <= norm_inf(Dapp) / (1 - r)
            assert norm_inf(D) >= 1
            exterior = sp.eye(n)[:, 0]
            core = eps ** 2 * sp.Matrix([sp.Rational(RNG.randrange(-2, 3), 2) for _ in range(n)])
            assert D * exterior == Dapp * exterior - D * R * exterior
            bound = norm_inf(D) * norm_inf(core) + norm_inf(Dapp * exterior) + norm_inf(D) * norm_inf(R * exterior)
            assert norm_inf(D * (core + exterior)) <= bound
            assert norm_inf(Dapp * exterior) <= 2 * eps
            assert norm_inf(R * exterior) <= eps / 8
            for terms in [1, 3, 7]:
                finite = sum(((-R) ** j for j in range(terms)), sp.zeros(n))
                assert norm_inf(D - Dapp * finite) <= norm_inf(Dapp) * r ** terms / (1 - r)
                remainders += 1
            cases += 1
    return dict(rectangular_models=cases, neumann_remainder_bounds=remainders,
                control="Right inverse has norm at least one and a nontrivial operator kernel.")


def holder_interpolation():
    cases = modes = 0
    alpha, higher = 0.3, 0.8
    # Finite metric-space seminorms: the crossover estimate is checked independently of a PDE.
    for eta in [1.0, 0.1, 0.01, 0.001]:
        for _ in range(10):
            xs = np.linspace(0, 1, 9)
            ts = np.linspace(0, eta, 7)
            points = [(x, t) for x in xs for t in ts]
            phase = RNG.random()
            values = np.array([t ** (higher / 4) * np.cos(3 * x + phase) for x, t in points])
            U = float(np.max(abs(values)))
            low, high = 0.0, 0.0
            for i in range(len(points)):
                for j in range(i):
                    x, t = points[i]
                    y, s = points[j]
                    distance = abs(x - y) + abs(t - s) ** 0.25
                    difference = abs(values[i] - values[j])
                    low = max(low, difference / distance ** alpha)
                    high = max(high, difference / distance ** higher)
            assert U <= high * eta ** (higher / 4) * (1 + 1e-12)
            assert low <= (2 * U) ** (1 - alpha / higher) * high ** (alpha / higher) * (1 + 1e-12)
            assert low <= 2 ** (1 - alpha / higher) * high * eta ** ((higher - alpha) / 4) * (1 + 1e-12)
            cases += 1
    N, t, z, a = sp.symbols("N t z a", positive=True)
    u = N ** (-4 - a) * (1 - sp.exp(-N ** 4 * t)) * sp.cos(N * z)
    forcing = N ** (-a) * sp.cos(N * z)
    assert sp.simplify(sp.diff(u, t) + sp.diff(u, z, 4) - forcing) == 0
    assert sp.simplify(sp.diff(u, t).subs(t, 0) - forcing) == 0
    for n in [2, 4, 8, 16, 32, 64]:
        for exponent in [alpha, higher]:
            # A concrete pair x=0,y=pi/N gives this lower Holder quotient at T=N^-4.
            quotient = 2 * (1 - np.exp(-1)) * n ** (-exponent) / (pi / n) ** alpha
            reference = 2 * (1 - np.exp(-1)) / pi ** alpha
            assert np.isclose(quotient, reference * n ** (alpha - exponent))
            if exponent == alpha:
                assert np.isclose(quotient, reference)
            modes += 1
    return dict(parabolic_grid_models=cases, fourier_mode_scalings=modes,
                symbolic_pde_identity=True, equal_exponent_control="nonvanishing seminorm")


def delayed_radii():
    cases = prefixes = bad_count = good_count = 0
    theta, c, eta, Q = map(mp.mpf, ['0.4', '0.2', '0.1', '1.2'])
    p = (theta - c) / (1 - c)
    kappa, q = (1 - eta) / (1 - c), Q ** 2
    h = kappa / 8
    delta = mp.mpf('0.01')
    rho = delta ** (kappa * q - 1) / (1 - delta ** (kappa * (q - 1)))
    assert rho < mp.mpf('0.5')
    for length in [5, 10, 20, 40]:
        for trial in range(5):
            raw = [mp.mpf(10) ** (-RNG.randrange(1, 13)) if RNG.random() > .2 else mp.mpf(0) for _ in range(length)]
            if not any(raw):
                raw[0] = 1
            tail = mp.mpf('0.1') * sum(x * x for x in raw)
            scale = delta / mp.sqrt(tail + sum(x * x for x in raw))
            a = [x * scale for x in raw]
            E = [scale ** 2 * tail + sum(x * x for x in a[j:]) for j in range(length + 1)]
            assert abs(E[0] - delta ** 2) < mp.mpf('1e-70')
            Rin = mp.mpf(4 + 2 * trial)
            radii, b = [], []
            for j in range(length):
                local = mp.sqrt(8 * mp.log(1 / a[j])) if a[j] else mp.inf
                radius = min([Q ** j * Rin] + [Q ** (j - i) * mp.sqrt(8 * mp.log(1 / a[i])) for i in range(j + 1) if a[i]])
                recursive = min(Q * radii[-1], local) if j else min(Rin, local)
                assert mp.almosteq(radius, recursive)
                radii.append(radius)
                b.append(mp.exp(-(1 - eta) * radius ** 2 / 8))
            C = max(E[j + 1] ** (1 - theta) / (a[j] + b[j]) for j in range(length))
            K = (2 * C) ** (1 / (1 - c))
            Cprime = max(K * 2 ** (1 - p) / p, 1 / (1 - 2 ** (-p)))
            B = mp.exp(-h * Rin ** 2) / (1 - mp.exp(-h * (q - 1) * Rin ** 2))
            good_sum, bad_sum, double_sum, total = map(mp.mpf, [0, 0, 0, 0])
            for j in range(length):
                total += a[j]
                if b[j] <= a[j] ** (1 - c):
                    assert a[j] <= Cprime * (E[j] ** p - E[j + 1] ** p) + mp.mpf('1e-60')
                    good_sum += a[j]
                    good_count += 1
                else:
                    initial = mp.exp(-h * q ** j * Rin ** 2)
                    terms = [a[i] ** (kappa * q ** (j - i)) for i in range(j + 1)]
                    maximum = max([initial] + terms)
                    assert mp.almosteq(maximum, mp.exp(-h * radii[j] ** 2))
                    assert a[j] < maximum
                    if a[j]:
                        assert terms[-1] < a[j]
                    convolution = sum(terms[:-1])
                    assert a[j] <= initial + convolution
                    bad_sum += a[j]
                    double_sum += convolution
                    bad_count += 1
                assert double_sum <= rho * total + mp.mpf('1e-60')
                assert bad_sum <= B + rho * total + mp.mpf('1e-60')
                assert total <= 2 * (Cprime * E[0] ** p + B) + mp.mpf('1e-60')
                prefixes += 1
            cases += 1
    x = mp.mpf('0.1')
    assert x ** 1 == x and x ** mp.mpf('0.5') > x
    return dict(energy_sequences=cases, prefixes=prefixes, good_indices=good_count,
                bad_indices=bad_count, rho_upper_bound=float(rho),
                scope="C is computed for each finite model; no geometric gradient inequality is certified.")


def gevrey_telescope():
    moments = remainders = 0
    for k in [1, 2, 3]:
        ts = [mp.mpf(2) ** j for j in range(12)]
        rs = [t ** (-mp.mpf(1) / k) for t in ts]
        amps = [mp.exp(-t) for t in ts]
        C0 = mp.exp(-mp.mpf('.5')) / (1 - mp.exp(-mp.mpf('.5')))
        for n in range(51):
            x = mp.mpf(n) / k
            moment = sum(amp * t ** x for amp, t in zip(amps, ts))
            bound = C0 * ((2 * x / mp.e) ** x if n else 1)
            assert moment <= bound * (1 + mp.mpf('1e-60'))
            assert moment <= C0 * 2 ** x * mp.gamma(1 + x) * (1 + mp.mpf('1e-60'))
            moments += 1
        theta = mp.mpf('.6')
        for J in range(1, 6):
            s = theta * (rs[J] + rs[J + 1]) / 2
            assert theta * rs[J + 1] < s <= theta * rs[J]
            # D_j=exp(-t_j)/(1-s/(2r_j)), bounded by 2 exp(-t_j) on its full disk.
            FJ = sum(amps[j] / (1 - s / (2 * rs[j])) for j in range(J + 1))
            for N in [1, 2, 4, 8, 16, 32, 48]:
                coefficients = [sum(amps[j] / (2 * rs[j]) ** n for j in range(len(ts))) for n in range(N)]
                polynomial = sum(coefficients[n] * s ** n for n in range(N))
                low = sum(amps[j] * (s / (2 * rs[j])) ** N / (1 - s / (2 * rs[j])) for j in range(J + 1))
                high = sum(amps[j] * sum((s / (2 * rs[j])) ** n for n in range(N)) for j in range(J + 1, len(ts)))
                assert abs((FJ - polynomial) - (low - high)) <= mp.mpf('1e-60') * max(1, abs(polynomial))
                # Direct Cauchy and tail bounds used in the general proof, not a fitted constant.
                low_bound = 2 / (1 - theta) * s ** N * sum(amps[j] / rs[j] ** N for j in range(J + 1))
                high_bound = 2 * N * theta ** (-N) * s ** N * sum(amps[j] / rs[j] ** N for j in range(J + 1, len(ts)))
                assert abs(FJ - polynomial) <= low_bound + high_bound + mp.mpf('1e-60')
                x = mp.mpf(N) / k
                envelope = (2 / (1 - theta) + 2 * N * theta ** (-N)) * C0 * 2 ** x * mp.gamma(1 + x) * s ** N
                assert low_bound + high_bound <= envelope * (1 + mp.mpf('1e-60'))
                remainders += 1
    return dict(moment_bounds=moments, stopped_remainders=remainders, precision_digits=mp.mp.dps,
                scope="Finite analytic telescopes, including orders beyond the stopping scale.")


def covering_indices():
    cases = controls = 0
    for n in range(1, 41):
        for a in range(n):
            image = {a * x % n for x in range(n)}
            fibers = [[x for x in range(n) if a * x % n == y] for y in image]
            index = n // len(image)
            assert all(len(fiber) == gcd(a, n) == index for fiber in fibers)
            assert (len(image) == n) == (index == 1)
            cases += 1
    # Circle cover z -> z^k: induced map on Z has image kZ and index |k|.
    for k in list(range(-10, 0)) + list(range(1, 11)):
        sheets = abs(k)
        assert (sheets == 1) == (k in [-1, 1])
        controls += sheets > 1
    return dict(finite_cyclic_homomorphisms=cases, multiple_sheet_circle_controls=controls,
                scope="Illustrates the index mechanism; the manifold theorem is checked analytically.")


def determinant_gain():
    cases = 0
    for n in range(2, 6):
        for _ in range(15):
            e = sp.eye(n)[:, n - 1]
            p = sp.Matrix([RNG.randrange(-3, 4) for _ in range(n - 1)] + [RNG.randrange(1, 5)])
            q = (p.T * e)[0]
            # Columns span p-perp but need not be orthonormal: determinant cancellation still holds.
            Q = sp.Matrix(n, n - 1, lambda i, j: int(i == j) if i < n - 1 else -p[j] / q)
            W = Q.row_join(e)
            B = sp.Matrix(n, n, [RNG.randrange(-3, 4) for _ in range(n * n)])
            V = B.T * B + sp.eye(n)
            m, gamma, d = [sp.Rational(RNG.randrange(1, 6), RNG.randrange(1, 6)) for _ in range(3)]
            pi_vec = p + d * e
            P = sp.eye(n) - e * p.T / q
            assert P * P == P and p.T * P == sp.zeros(1, n)
            base = m * P.T * V * P + gamma * pi_vec * pi_vec.T
            transformed = W.T * V * W
            A, z, h = transformed[:-1, :-1], transformed[:-1, -1], transformed[-1, -1]
            S = h - (z.T * A.inv() * z)[0]
            beta = (e.T * V * e)[0] / q ** 2
            ratio = base.det() / V.det()
            assert ratio == m ** (n - 1) * gamma * (pi_vec.T * e)[0] ** 2 / S
            assert ratio >= m ** (n - 1) * gamma / beta
            assert (W.T * base * W).det() == W.det() ** 2 * base.det()
            v = sp.Matrix([RNG.randrange(-2, 3) for _ in range(n)])
            assert (base + v * v.T).det() >= base.det()
            assert (m * P.T * V * P).det() == 0
            cases += 1
    return dict(exact_positive_definite_models=cases, missing_direction_control="zero determinant")


def compositions(total, count):
    if count == 1:
        return [(total,)]
    return [(first,) + rest for first in range(total + 1) for rest in compositions(total - first, count - 1)]


def choose(n, k):
    return comb(n, k) if n >= k >= 0 else 0


def beta_integer(a, b):
    return F(factorial(a - 1) * factorial(b - 1), factorial(a + b - 1))


def hopf_weights():
    cases = matrices = 0
    for s in range(2, 8):
        for l in range(0, 21):
            weights = []
            for b in range(l + 1):
                h = choose(s + b - 1, s - 1) * choose(s + l - b - 1, s - 1) - choose(s + b - 2, s - 1) * choose(s + l - b - 2, s - 1)
                simplified = F(l + s - 1, s - 1) * choose(b + s - 2, s - 2) * choose(l - b + s - 2, s - 2)
                assert h == simplified
                weights.append(h)
            N = sum(weights)
            assert N == choose(2 * s - 1 + l, 2 * s - 1) - choose(2 * s - 3 + l, 2 * s - 1)
            aggregated = {}
            for b, h in enumerate(weights):
                prob = F(comb(l, b)) * beta_integer(b + s - 1, l - b + s - 1) / beta_integer(s - 1, s - 1)
                assert prob == F(h, N)
                aggregated[(2 * b - l) ** 2] = aggregated.get((2 * b - l) ** 2, 0) + h
            assert sum(aggregated.values()) == N
            if l:
                EX2 = beta_integer(s + 1, s - 1) / beta_integer(s - 1, s - 1)
                EK2 = sum(F(h, N) * F(b * b, l * l) for b, h in enumerate(weights))
                coupling_error = EK2 - EX2  # E[(K/l-X)^2]=E[(K/l)^2]-E[X^2].
                expected = beta_integer(s, s) / beta_integer(s - 1, s - 1) / l
                assert coupling_error == expected <= F(1, 4 * l)
            cases += 1
    for s in [2, 3]:
        for b, c in product(range(1, 4), repeat=2):
            domain = list(product(compositions(b, s), compositions(c, s)))
            target = list(product(compositions(b - 1, s), compositions(c - 1, s)))
            index = {pair: i for i, pair in enumerate(target)}
            C = sp.zeros(len(target), len(domain))
            for j, (aa, bb) in enumerate(domain):
                for i in range(s):
                    if aa[i] and bb[i]:
                        ar, br = list(aa), list(bb)
                        ar[i] -= 1
                        br[i] -= 1
                        C[index[tuple(ar), tuple(br)], j] += aa[i] * bb[i]
            assert C.rank() == len(target)
            assert len(domain) - C.rank() == choose(s + b - 1, s - 1) * choose(s + c - 1, s - 1) - choose(s + b - 2, s - 1) * choose(s + c - 2, s - 1)
            matrices += 1
    return dict(multiplicity_laws=cases, surjective_contraction_matrices=matrices,
                beta_binomial_and_coupling_checks="exact")


def sphere_integral(poly, variables):
    result = sp.Rational(0)
    for powers, coefficient in sp.Poly(sp.expand(poly), *variables).terms():
        if any(n % 2 for n in powers):
            continue
        half = [n // 2 for n in powers]
        numerator = sp.prod(sp.factorial2(2 * n - 1) if n else 1 for n in half)
        denominator = sp.factorial2(2 * sum(half) + 1)
        result += coefficient * numerator / denominator
    return result


def conformal_splitting():
    x, y, z = sp.symbols("x y z")
    u, v = sp.sqrt(3) * x, sp.sqrt(3) * y
    U = [u * u - v * v, 2 * u * v]
    integral = lambda f: sphere_integral(f, (x, y, z))
    assert integral(u * u) == integral(v * v) == 1 and integral(u * v) == 0
    assert all(integral(f) == 0 for f in U)
    G = sp.Matrix(2, 2, lambda i, j: integral(U[i] * U[j]))
    assert G == sp.diag(sp.Rational(12, 5), sp.Rational(12, 5))
    entries = []
    for direction in U:
        M = sp.Matrix(2, 2, lambda i, j: -4 * integral([u, v][i] * [u, v][j] * direction))
        assert sp.trace(M) == 0
        entries.append(sp.Matrix([M[0, 0] - M[1, 1], 2 * M[0, 1]]))
        assert sp.expand(direction.subs({x: -x, y: -y, z: -z}, simultaneous=True) - direction) == 0
    assert sp.Matrix.hstack(*entries).det() != 0
    matrices = 0
    for n in range(3, 9):
        for _ in range(10):
            lam = RNG.randrange(1, 10)
            A = sp.diag(lam, lam, *[lam + i + 1 for i in range(n - 2)])
            B = sp.Matrix(n, n, [RNG.randrange(-4, 5) for _ in range(n * n)])
            commutator = B * A - A * B
            assert commutator[:2, :2] == sp.zeros(2)
            matrices += 1
    return dict(sphere_gram_matrix=str(G), independent_splitting_directions=2,
                even_directions=True, commutator_models=matrices,
                scope="Degree-one sphere pair and finite eigenspace compression; unique continuation is an analytic input.")


def main():
    start = time.perf_counter()
    checks = {}
    for fn in [particular_error, holder_interpolation, delayed_radii, gevrey_telescope,
               covering_indices, determinant_gain, hopf_weights, conformal_splitting]:
        checks[fn.__name__] = {"status": "passed", **fn()}
    result = dict(batch="B053", status="passed", checks=checks,
                  elapsed_seconds=round(time.perf_counter() - start, 3),
                  scope="Finite identities and models only; no source headline theorem or Lean solution certified.")
    (Path(__file__).parent / 'results.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
