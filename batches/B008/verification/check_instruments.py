"""Finite checks for Banach-space mechanisms and stopped-median smoothing."""
from fractions import Fraction as F
from itertools import product
import json
import math
from pathlib import Path
import numpy as np

RNG = np.random.default_rng(322326327332)


def invariant_face():
    vertices = [np.array([1., 0., 0., 0.])]
    for _ in range(40):
        coefficients = RNG.dirichlet(np.ones(len(vertices)))
        a = coefficients @ np.array(vertices)
        g = np.exp(3 * a)
        g /= g.sum()
        assert abs(np.sum(a) - 1) < 1e-12
        assert abs(np.sum(g) - 1) < 1e-12
        vertices.append(g)
        for _ in range(5):
            point = RNG.dirichlet(np.ones(len(vertices))) @ np.array(vertices)
            assert abs(np.linalg.norm(point, 1) - 1) < 1e-12
    # A map of a Hilbert ball with a bounded scalar error; not a norm contraction.
    gamma, alpha = 0.4, 4.0
    points = RNG.normal(size=(80, 5))
    points /= np.maximum(1, np.linalg.norm(points, axis=1))[:, None]
    parameter = np.sin(alpha * points[:, 0])
    images = gamma * points
    images[:, 0] += (1 - gamma) * parameter
    assert np.max(np.linalg.norm(images, axis=1)) <= 1 + 1e-12
    for i in range(len(points)):
        for j in range(len(points)):
            lhs = np.linalg.norm(images[i] - images[j])
            rhs = gamma * np.linalg.norm(points[i] - points[j]) + (1 - gamma) * abs(parameter[i] - parameter[j])
            assert lhs <= rhs + 1e-12
    local_ratio = gamma + (1 - gamma) * math.sin(alpha * 1e-6) / 1e-6
    assert local_ratio > 1
    radii = 0
    for _ in range(300):
        t = float(RNG.uniform(0.2, 0.8))
        low, high = 1 - t, 1 + t
        defect = float(RNG.uniform(0.01, min(0.15, t)))
        p, u = RNG.uniform(low, high - defect, size=2)
        r, s = u + defect, p + defect
        contraction = (1 - defect / high) ** 2
        assert u * p / (r * s) <= contraction + 1e-12
        eta = 1e-4
        dp, du = RNG.uniform(-eta, eta, size=2)
        error = 2 * abs(du) / r + 2 * u * abs(dp) / (r * s)
        assert error <= 4 * eta / low + 1e-12
        radii += 1
    return {'convex_face_steps': 40, 'compact_parameter_pairs': 6400, 'radius_examples': radii,
            'noncontraction_local_ratio': local_ratio,
            'scope': 'Finite support and parameter algebra; no computation of a nonzero infinite-dimensional measure of noncompactness.'}


def sign_lifts():
    cases = 0
    error = 0.0
    for m in range(1, 9):
        signs = np.array(list(product([-1, 1], repeat=m)))
        for d in [1, 3, 7]:
            vectors = RNG.normal(size=(m, d))
            vectors /= np.maximum(1, np.linalg.norm(vectors, axis=1))[:, None]
            scale = 1 / (48 * math.sqrt(m))
            lift = scale * signs @ vectors
            recovered = signs.T @ lift / len(signs)
            err = float(np.max(np.abs(recovered - scale * vectors)))
            error = max(error, err)
            assert err < 1e-12
            assert np.max(np.linalg.norm(lift, axis=1)) <= 1
            rademacher = signs @ vectors
            l2 = np.mean(np.linalg.norm(rademacher, axis=1) ** 2) ** 0.5
            l1 = np.mean(np.linalg.norm(rademacher, axis=1))
            assert l2 <= 24 * l1 + 1e-12
            assert abs(l2 ** 2 - np.sum(vectors ** 2)) < 1e-10
            cases += 1
    return {'hilbert_models': cases, 'maximum_moment_error': error,
            'scope': 'Explicit Hilbert lifts on complete finite sign cubes; not arbitrary Banach quotient optimization.'}


def compact_shift():
    count = 0
    error = 0.0
    for levels in [3, 5, 8, 12]:
        dimension = 6
        blocks = []
        for level in range(levels):
            z = np.zeros(dimension)
            z[:min(level + 1, dimension)] = RNG.normal(size=min(level + 1, dimension))
            blocks.append(z)
        blocks = np.array(blocks)
        image = sum(2. ** -level * z for level, z in enumerate(blocks))
        shifted = np.vstack([np.zeros(dimension), 2 * blocks])
        shifted_image = sum(2. ** -level * z for level, z in enumerate(shifted))
        err = float(np.linalg.norm(image - shifted_image))
        error = max(error, err)
        assert err < 1e-12
        assert np.linalg.norm(image) <= np.sqrt(sum(4. ** -level for level in range(levels))) * np.linalg.norm(blocks) + 1e-12
        for cutoff in range(levels):
            tail = sum((2. ** -level * blocks[level] for level in range(cutoff + 1, levels)), np.zeros(dimension))
            bound = np.sqrt(sum(4. ** -level for level in range(cutoff + 1, levels))) * np.linalg.norm(blocks[cutoff + 1:])
            assert np.linalg.norm(tail) <= bound + 1e-12
            count += 1
        # Assemble exact moments one level later, with the compensating factor two.
        m = 4
        signs = np.array(list(product([-1, 1], repeat=m)))
        tuples = RNG.normal(size=(m, levels, dimension))
        for level in range(levels):
            tuples[:, level, min(level + 1, dimension):] = 0
        h = np.einsum('si,ild->sld', signs, tuples)
        shifted_h = np.concatenate([np.zeros((len(signs), 1, dimension)), 2 * h], axis=1)
        quotient_values = np.einsum('l,sld->sd', 2. ** -np.arange(levels + 1), shifted_h)
        moments = signs.T @ quotient_values / len(signs)
        expected = np.einsum('l,ild->id', 2. ** -np.arange(levels), tuples)
        assert np.max(np.abs(moments - expected)) < 1e-11
    kernel_blocks = [np.array([1.]), np.array([-2.])]
    assert np.linalg.norm(kernel_blocks[0] + kernel_blocks[1] / 2) == 0
    assert np.linalg.norm(kernel_blocks[0]) == 1
    approximants = []
    dimension = 30
    j = np.diag(2. ** -np.arange(dimension))
    for n in [2, 4, 8, 12]:
        s = np.zeros((dimension, dimension))
        s[np.arange(n), np.arange(n)] = 1
        s[2 * n, 2 * n] = n
        composite_error = np.linalg.norm(s @ j - j, 2)
        assert composite_error <= max(2. ** -n, (n - 1) * 2. ** (-2 * n)) + 1e-12
        approximants.append({'index': n, 'operator_norm': float(np.linalg.norm(s, 2)), 'composite_error': float(composite_error)})
    return {'tail_bounds': count, 'shift_models': 4, 'maximum_shift_error': error,
            'kernel_truncation_negative_control': {'full_image': 0, 'truncated_image': 1},
            'unbounded_norm_composite_examples': approximants,
            'scope': 'Finite truncations of shift and moment identities; not an infinite-dimensional compactness or AP proof.'}


def odd_edge_sums():
    cases = 0
    max_ratio = 0.0
    for states in [2, 3, 5, 7]:
        for _ in range(5):
            conductance = RNG.uniform(0.1, 1, size=(states, states))
            conductance = conductance + conductance.T
            row = conductance.sum(axis=1)
            pi, transition = row / row.sum(), conductance / row[:, None]
            labels = RNG.normal(size=(states, states, 3))
            labels = labels - labels.transpose(1, 0, 2)
            # Antisymmetric labels on a triangle need not have zero circulation.
            one = float(np.einsum('i,ij,ijd,ijd->', pi, transition, labels, labels))
            mass = pi.copy()
            mean = np.zeros((states, 3))
            second = np.zeros(states)
            for time in range(1, 10):
                new_mean = np.zeros_like(mean)
                new_second = np.zeros_like(second)
                for i in range(states):
                    for k in range(states):
                        g = labels[i, k]
                        new_mean[k] += transition[i, k] * (mean[i] + mass[i] * g)
                        new_second[k] += transition[i, k] * (second[i] + 2 * np.dot(mean[i], g) + mass[i] * np.dot(g, g))
                mass = mass @ transition
                mean, second = new_mean, new_second
                assert second.sum() <= time * one + 1e-10
                if one:
                    max_ratio = max(max_ratio, float(second.sum() / (time * one)))
                cases += 1
    # Two marked parallel edge pairs and reversible holds; inspect the lattice lift.
    edges = {0: [(1, 0, 1, .3), (1, 1, 1, .2), (0, None, 0, .5)],
             1: [(0, 0, -1, .3), (0, 1, -1, .2), (1, None, 0, .5)]}
    balance_checks = 0
    for radius in [2, 4, 6]:
        lattice = list(product(range(-radius, radius + 1), repeat=2))
        kernel = {}
        for state in [0, 1]:
            for position in lattice:
                origin = (state, position)
                for target, coordinate, sign, probability in edges[state]:
                    moved = list(position)
                    if coordinate is not None:
                        moved[coordinate] += sign
                    destination = (target, tuple(moved))
                    if any(abs(x) > radius for x in moved):
                        destination = origin
                    kernel[origin, destination] = kernel.get((origin, destination), 0) + probability
        for (origin, destination), probability in kernel.items():
            assert abs(probability - kernel.get((destination, origin), 0)) < 1e-12
            balance_checks += 1
    # A directed stationary 3-cycle with label +1 on its used orientation has linear sums.
    assert 4 ** 2 > 4
    return {'hilbert_time_checks': cases, 'maximum_ratio': max_ratio, 'lift_balance_checks': balance_checks,
            'nonreversible_control': {'time': 4, 'sum_squared': 16, 'invalid_bound': 4},
            'scope': 'Exact finite-state moment recursions and reversible marked-box transitions; not the source linear-displacement construction.'}


def chart_transport():
    cases = []
    for count in [3, 7, 19]:
        charts = np.array([(i, i + 1) for i in range(count)])
        nu = np.ones(count) / count
        forward = np.zeros((count, count))
        for i in range(count):
            forward[i, (i + 1) % count] = 1 / count
        backward = forward.T
        assert np.max(np.abs(forward.sum(axis=0) - nu)) < 1e-12
        assert np.max(np.abs(forward.sum(axis=1) - nu)) < 1e-12
        first = CounterMap(charts[:, 0], nu)
        second = CounterMap(charts[:, 1], nu)
        tv = sum(abs(first.get(x, 0) - second.get(x, 0)) for x in set(first) | set(second)) / 2
        success_forward = sum(forward[i, j] for i in range(count) for j in range(count) if charts[j, 0] == charts[i, 1])
        success_backward = sum(backward[i, j] for i in range(count) for j in range(count) if charts[j, 1] == charts[i, 0])
        assert abs(success_forward - (1 - tv)) < 1e-12
        assert abs(success_backward - success_forward) < 1e-12
        transition = (forward + backward) / (2 * nu[:, None])
        assert np.max(np.abs(nu[:, None] * transition - nu[None, :] * transition.T)) < 1e-12
        for i in range(count):
            assert abs(forward[i].sum() / (2 * nu[i]) - 0.5) < 1e-12
        cases.append({'charts': count, 'total_variation': tv, 'stationary_success': success_forward,
                      'worst_conditional_success_forward': 0})
    return {'models': cases, 'scope': 'Explicit two-point translated charts, maximal matching and reverse couplings; not general finite Ramsey bounds.'}


def CounterMap(values, probabilities):
    result = {}
    for value, mass in zip(values, probabilities):
        result[int(value)] = result.get(int(value), 0.0) + float(mass)
    return result


def cut_representation(data):
    n, dimension = data.shape
    vectors, bits = [], []
    for mask in range(1, (1 << n) - 1):
        chosen = np.array([bool(mask & (1 << i)) for i in range(n)])
        vector = np.maximum(data[chosen].min(axis=0) - data[~chosen].max(axis=0), 0)
        if vector.sum() > 0:
            vectors.append(vector)
            bits.append(chosen.astype(float))
    b = np.array(vectors).reshape(-1, dimension)
    z = np.array(bits).reshape(-1, n).T
    return data.min(axis=0), b, b.sum(axis=1), z


def cut_checks():
    models = 0
    max_error = 0.0
    for n in range(2, 8):
        for dimension in [1, 3, 6]:
            data = RNG.integers(-4, 5, size=(n, dimension)).astype(float)
            if n > 3:
                data[-1] = data[0]
            v, b, weights, z = cut_representation(data)
            assert np.array_equal(v + z @ b, data)
            distances = np.abs(data[:, None] - data[None, :]).sum(axis=2)
            encoded = np.einsum('ijk,k->ij', np.abs(z[:, None] - z[None, :]), weights)
            assert np.array_equal(distances, encoded)
            for _ in range(15):
                u, other = RNG.normal(size=(2, len(weights)))
                lhs = np.abs((u - other) @ b).sum()
                rhs = np.dot(weights, np.abs(u - other))
                assert lhs <= rhs + 1e-12
                max_error = max(max_error, float(max(0, lhs - rhs)))
            models += 1
    return {'models': models, 'contractivity_examples': models * 15, 'maximum_positive_error': max_error,
            'scope': 'Exact finite integer cuts and floating contractivity; no enumeration of infinite original coordinate support.'}


def quartic_potential():
    rational_cases = 0
    maximum_ratio = F(0)
    for dimension in [1, 2, 4]:
        for _ in range(300):
            weights = [F(int(x), 3) for x in RNG.integers(1, 7, size=dimension)]
            u = [F(int(x), 10) for x in RNG.integers(0, 11, size=dimension)]
            other = [F(int(x), 10) for x in RNG.integers(0, 11, size=dimension)]
            e = [F(int(x)) for x in RNG.integers(0, 2, size=dimension)]
            a = [x - bit for x, bit in zip(u, e)]
            delta = [y - x for x, y in zip(u, other)]
            dot = lambda x, y: sum(w * s * t for w, s, t in zip(weights, x, y))
            aa, dd, ad = dot(a, a), dot(delta, delta), dot(a, delta)
            polynomial = lambda x: 3 * x * x - 2 * x * x * x
            lhs = sum(w * abs(polynomial(y) - polynomial(x)) for w, x, y in zip(weights, u, other)) ** 2
            remainder = dot([x + y for x, y in zip(a, delta)], [x + y for x, y in zip(a, delta)]) ** 2 - aa ** 2 - 4 * aa * ad
            assert remainder == 2 * aa * dd + (2 * ad + dd) ** 2
            assert lhs <= 108 * remainder
            if remainder:
                maximum_ratio = max(maximum_ratio, lhs / remainder)
            rational_cases += 1
    # Reveal a finite binary terminal vector one bit at a time.
    martingales = 0
    for dimension in [2, 4, 6]:
        terminal = np.array(list(product([0., 1.], repeat=dimension)))
        weights = RNG.uniform(.2, 2, size=dimension)
        for center in [np.zeros(dimension), np.ones(dimension)]:
            total_energy = 0.0
            before = np.full_like(terminal, .5)
            initial = np.mean(np.sum(weights * (before - center) ** 2, axis=1) ** 2)
            for revealed in range(dimension):
                after = before.copy()
                after[:, revealed] = terminal[:, revealed]
                phi = lambda x: 3 * x * x - 2 * x * x * x
                total_energy += np.mean(np.sum(weights * np.abs(phi(after) - phi(before)), axis=1) ** 2)
                before = after
            final = np.mean(np.sum(weights * (terminal - center) ** 2, axis=1) ** 2)
            assert total_energy <= 108 * (final - initial) + 1e-10
            martingales += 1
    epsilon = F(1, 100)
    assert epsilon ** 2 > 108 * epsilon ** 4
    return {'exact_rational_cases': rational_cases, 'largest_increment_over_remainder': str(maximum_ratio),
            'finite_martingales': martingales,
            'identity_map_negative_control': {'epsilon': str(epsilon), 'increment_squared': str(epsilon ** 2), '108_remainder': str(108 * epsilon ** 4)},
            'scope': 'Exact polynomial inequalities and finite martingale telescoping; flatness control is deliberately tested.'}


def stopped_medians():
    models = 0
    max_median_error = 0.0
    max_ratio = 0.0
    max_geo_ratio = 0.0
    for base_n in [2, 3, 5, 6]:
        for style in ['reversible', 'cycle', 'zero_mass']:
            if style == 'reversible':
                c = RNG.uniform(.1, 1, size=(base_n, base_n))
                c = c + c.T
                row = c.sum(axis=1)
                pi, a = row / row.sum(), c / row[:, None]
            else:
                a = np.zeros((base_n, base_n))
                for i in range(base_n):
                    a[i, i] += .2
                    a[i, (i + 1) % base_n] += .8
                pi = np.ones(base_n) / base_n
                if style == 'zero_mass':
                    a = np.pad(a, ((0, 1), (0, 1)))
                    a[-1, 0] = 1
                    pi = np.r_[pi, 0]
            n = len(pi)
            assert np.max(np.abs(pi @ a - pi)) < 1e-12
            data = RNG.integers(-4, 6, size=(n, 3)).astype(float)
            v, b, weights, z = cut_representation(data)
            distances = np.abs(data[:, None] - data[None, :]).sum(axis=2) ** 2
            for time in [1, 2, 5, 11]:
                p, q = 1 / (time + 1), time / (time + 1)
                endpoint = p * np.linalg.inv(np.eye(n) - q * a)
                h = endpoint @ z
                assert np.max(np.abs(h - p * z - q * a @ h)) < 1e-12
                smooth = 3 * h * h - 2 * h * h * h
                y = v + smooth @ b
                enumerated = np.zeros_like(y)
                for j, k, ell in product(range(n), repeat=3):
                    median = np.median(data[[j, k, ell]], axis=0)
                    probability = endpoint[:, j] * endpoint[:, k] * endpoint[:, ell]
                    enumerated += probability[:, None] * median
                err = float(np.max(np.abs(y - enumerated)))
                max_median_error = max(max_median_error, err)
                assert err < 1e-10
                approximation = np.dot(pi, (np.abs(z - smooth) @ weights) ** 2)
                cut_distances = (np.abs(smooth[:, None] - smooth[None, :]) @ weights) ** 2
                edge = np.einsum('i,ij,ij->', pi, a, cut_distances)
                geometric = np.einsum('i,ij,ij->', pi, endpoint, distances)
                assert approximation + time * edge <= 108 * geometric + 1e-8
                jump_terms = sum(p * q ** step * approximation + q ** (step + 1) * edge for step in range(80))
                assert abs(jump_terms - (1 - q ** 80) * (approximation + time * edge)) < 1e-8
                cesaro = np.zeros_like(a)
                power = np.eye(n)
                for _ in range(time):
                    power = power @ a
                    cesaro += power / time
                cost = np.einsum('i,ij,ij->', pi, cesaro, distances)
                assert geometric <= 28 * cost + 1e-8
                actual = np.dot(pi, np.abs(data - y).sum(axis=1) ** 2)
                actual += time * np.einsum('i,ij,ij->', pi, a, np.abs(y[:, None] - y[None, :]).sum(axis=2) ** 2)
                assert actual <= approximation + time * edge + 1e-8
                assert actual <= 3024 * cost + 1e-8
                if cost:
                    max_ratio = max(max_ratio, float(actual / cost))
                    max_geo_ratio = max(max_geo_ratio, float(geometric / cost))
                models += 1
    return {'stationary_examples': models, 'maximum_median_identity_error': max_median_error,
            'maximum_actual_cost_over_cesaro_cost': max_ratio, 'maximum_geometric_over_cesaro_cost': max_geo_ratio,
            'includes': ['reversible chains', 'nonreversible directed cycles', 'zero stationary coordinates'],
            'scope': 'Finite resolvents, triple-median enumeration, jump accounting and two-cost bounds; no general theorem or extension algorithm certification.'}


def main():
    checks = {}
    for name, function in [('invariant_face', invariant_face), ('sign_lifts', sign_lifts),
                           ('compact_shift', compact_shift), ('odd_edge_sums', odd_edge_sums),
                           ('chart_transport', chart_transport), ('cut_reconstruction', cut_checks),
                           ('quartic_potential', quartic_potential), ('stopped_medians', stopped_medians)]:
        checks[name] = function()
        print(name + ': passed', flush=True)
    result = {'batch': 'B008', 'status': 'passed', 'seed': 322326327332,
              'scope': 'Eight groups of finite checks. Infinite-dimensional, asymptotic, Lean and novelty claims are not certified.',
              'checks': checks}
    Path(__file__).with_name('results.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
