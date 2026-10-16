"""Finite B011 checks; matrix spectra and Gaussian integrals are numerical."""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import combinations, permutations, product
from pathlib import Path
import json
import math
import numpy as np
from scipy.integrate import quad

SEED = 126127132192
rng = np.random.default_rng(SEED)


def psd_splitting():
    def split(matrices):
        n = matrices[0].shape[0]
        if len(matrices) == 1:
            return [np.eye(n)]
        if n == 0:
            return [np.zeros((0, 0)) for _ in matrices]
        values, vectors = np.linalg.eigh(matrices[0]-sum(matrices[1:]))
        U, V = vectors[:, values >= 0], vectors[:, values < 0]
        P, Q = U @ U.T, V @ V.T
        A, B = matrices[0], sum(matrices[1:])
        overlap = np.trace(A @ B)
        errors = np.linalg.norm(P @ B @ P)**2+np.linalg.norm(Q @ A @ Q)**2
        assert errors <= overlap+1e-8*max(1, overlap)
        return [P]+[V @ p @ V.T for p in split([V.T @ a @ V for a in matrices[1:]])]
    cases, maximum_ratio = 0, 0.
    for n in [1, 2, 5, 9]:
        for L in range(1, 7):
            for model in range(5):
                matrices = []
                for _ in range(L):
                    X = rng.normal(size=(n, max(1, n-model)))
                    matrices.append(X @ X.T)
                if model == 0:
                    matrices = [np.diag([float(j % L == i) for j in range(n)]) for i in range(L)]
                projections = split(matrices)
                assert np.linalg.norm(sum(projections)-np.eye(n)) < 1e-9
                for i, P in enumerate(projections):
                    assert np.linalg.norm(P @ P-P) < 1e-9
                    for Q in projections[i+1:]:
                        assert np.linalg.norm(P @ Q) < 1e-9
                left = sum(np.linalg.norm(P @ A @ P)**2 for z, A in enumerate(matrices)
                           for s, P in enumerate(projections) if s != z)
                overlap = sum(np.trace(A @ B) for i, A in enumerate(matrices) for j, B in enumerate(matrices) if i != j)
                right = 2**(L-1)*overlap
                assert left <= right+1e-8*max(1, abs(right))
                if right > 1e-12:
                    maximum_ratio = max(maximum_ratio, left/right)
                cases += 1
    return {'recursive_PSD_families': cases, 'largest_error_to_bound_ratio': maximum_ratio,
            'scope': 'Numerical noncommuting and singular PSD families; no proof of all dimensions.'}


def matchings(vertices):
    if not vertices:
        yield []
        return
    a = vertices[0]
    for j in range(1, len(vertices)):
        b = vertices[j]
        rest = vertices[1:j]+vertices[j+1:]
        for pairs in matchings(rest):
            yield [(a, b)]+pairs


def trace_formula(k, d, w, s):
    h, g = (k-d)//2, (w-s)//2
    total = F(0)
    for j in range(min(g, h-g)+1):
        P = F(math.comb(g, j)*math.comb(h-g, j), math.comb(h, g))
        Q = F(math.comb(w, 2*j)*math.comb(k-w, 2*j), math.comb(k, w))
        total += P*P/Q
    return total


def local_channel():
    rows = []
    for k in [6, 8]:
        d = 2
        for y in product([0, 1], repeat=d):
            b, s = sum(y) % 2, sum(y)
            w = k//2 if k//2 % 2 == b else k//2+1
            X = [frozenset(c) for c in combinations(range(k), w)]
            index = {a: i for i, a in enumerate(X)}
            T = []
            for terminals in permutations(range(k), d):
                rest = [v for v in range(k) if v not in terminals]
                for pairs in matchings(rest):
                    line = np.zeros(len(X))
                    choices = list(combinations(range(len(pairs)), (w-s)//2))
                    for chosen in choices:
                        subset = {terminals[i] for i in range(d) if y[i]}
                        for j in chosen:
                            subset.update(pairs[j])
                        line[index[frozenset(subset)]] += 1/len(choices)
                    T.append(line)
            T = np.array(T)
            assert np.max(abs(T.mean(axis=0)-1/len(X))) < 1e-12
            K = len(X)/len(T)*(T.T @ T)
            trace = trace_formula(k, d, w, s)
            assert abs(np.trace(K @ K)-float(trace)) < 1e-10
            eigenvalues = np.linalg.eigvalsh(K)
            assert abs(eigenvalues[-1]-1) < 1e-10
            mu = eigenvalues[-2]
            assert k/2*mu*mu <= float(trace)-1+1e-10
            B = rng.normal(size=(len(X), 12))
            B -= B.mean(axis=0)
            assert np.mean(np.sum((T @ B)**2, axis=1)) <= mu*np.mean(np.sum(B**2, axis=1))+1e-10
            rows.append({'k': k, 'terminal_bits': list(y), 'column_data': len(T), 'slice_size': len(X),
                         'trace_square': str(trace), 'mean_zero_eigenvalue': float(mu)})
    larger = []
    for k in [20, 40, 80, 160]:
        tr = trace_formula(k, 2, k//2, 0)
        larger.append({'k': k, 'trace_square': float(tr), 'trace_over_k': float(tr/k)})
    return {'enumerated_channels': rows, 'larger_exact_binomial_sums': larger,
            'scope': 'Finite channel identities; an asymptotic rate is not inferred from a numerical fit.'}


def stationary_coupling():
    cases = 0
    def check(U, V):
        nonlocal cases
        n = len(U)
        m = F(sum(U), n)
        variance = sum((F(x)-m)**2 for x in U)/n
        a = max(0, max(v-u for u, v in zip(U, V)))
        motion = sum(F((u-v)**2, n) for u, v in zip(U, V))
        primitive = lambda x: (F(x)-m)*abs(F(x)-m)/2
        changes = [primitive(v)-primitive(u) for u, v in zip(U, V)]
        assert sum(changes) == 0
        assert sum(abs(x) for x in changes) == 2*sum(max(F(0), x) for x in changes)
        assert motion**2 <= 64*a*a*variance
        for u, v in zip(U, V):
            lo, hi = sorted([F(u), F(v)])
            increment = primitive(hi)-primitive(lo)
            assert (hi-lo)**2/4 <= increment <= (hi-lo)*(abs(lo-m)+abs(hi-m))/2
        cases += 1
    for n in range(2, 35):
        U = list(range(n))
        check(U, U[1:]+U[:1])
        check(U, U)
    for _ in range(200):
        U = [int(x) for x in rng.integers(-15, 16, size=10)]
        V = [U[i] for i in rng.permutation(10)]
        check(U, V)
    # Dropping equal marginals: V=U-1 has a=0 but motion one.
    U, V = [0, 1, 2], [-1, 0, 1]
    a = max(0, max(v-u for u, v in zip(U, V)))
    motion = sum(F((u-v)**2, len(U)) for u, v in zip(U, V))
    assert a == 0 and motion == 1 and Counter(U) != Counter(V)
    return {'exact_stationary_permutations': cases, 'negative_control': 'V=U-1, a=0, E(U-V)^2=1; unequal marginals.'}


def cube(n):
    return np.array(list(product([-1, 1], repeat=n)), dtype=int)


def characters(X):
    n = X.shape[1]
    masks = [c for k in range(n+1) for c in combinations(range(n), k)]
    A = np.array([np.prod(X[:, c], axis=1) if c else np.ones(len(X)) for c in masks]).T
    return A, np.array([len(c) for c in masks])


def weighted_grading():
    models, polynomial_models = 0, 0
    for n in range(1, 6):
        X = cube(n)
        A, degrees = characters(X)
        N = len(X)
        distances = np.sum(X[:, None, :] != X[None, :, :], axis=2)
        for trial in range(12):
            polynomial = trial >= 6
            d = min(n, 1+trial % 3)
            if polynomial:
                coeff = rng.integers(-3, 4, size=N)*(degrees <= d)
                p = 1+2*(A @ coeff)
                weight = abs(p)
                h = np.prod(X, axis=1)*np.sign(p)
            else:
                weight = np.exp(rng.uniform(-4, 4, size=N))
                h = rng.choice([-1, 1], size=N)
            Q, _ = np.linalg.qr(np.sqrt(weight)[:, None]*A)
            projections = [Q[:, degrees == j] @ Q[:, degrees == j].T for j in range(n+1)]
            L = (Q*degrees) @ Q.T
            M = L-n/2*np.eye(N)
            assert abs(np.linalg.norm(M)**2-n*N/4) < 1e-9
            for i in range(n):
                Z = np.diag(X[:, i])
                C = M @ Z-Z @ M
                assert np.linalg.norm(C, 2) <= 1+1e-9
                for r in range(n+1):
                    for s in range(n+1):
                        if abs(r-s) > 1:
                            assert np.linalg.norm(projections[s] @ Z @ projections[r]) < 1e-9
            assert np.max(abs(M[distances > 0])) <= .5+1e-9
            A0 = np.sum(np.diag(M)**2)
            far = np.sum(M[distances >= 2]**2)
            deficit = np.sum(.25-M[distances == 1]**2)
            assert far <= A0+1e-9 and deficit <= 2*A0+1e-9
            H = np.diag(h)
            anticommutator = M @ H+H @ M
            edges = np.count_nonzero((distances == 1) & (h[:, None] == h[None, :]))
            assert edges <= 2*np.linalg.norm(anticommutator)**2+1e-8
            if polynomial:
                law = np.array([[np.linalg.norm(projections[s] @ H @ projections[r])**2/N
                                 for s in range(n+1)] for r in range(n+1)])
                binomial = np.array([math.comb(n, j)/N for j in range(n+1)])
                assert np.max(abs(law.sum(axis=0)-binomial)) < 1e-10
                assert np.max(abs(law.sum(axis=1)-binomial)) < 1e-10
                moment = 0.
                for r in range(n+1):
                    for s in range(n+1):
                        if r+s < n-d:
                            assert law[r, s] < 1e-20
                        moment += (r+s-n)**2*law[r, s]
                assert abs(moment-np.linalg.norm(anticommutator)**2/N) < 1e-9
                assert moment <= 4*d*math.sqrt(n)+1e-9
                polynomial_models += 1
            models += 1
    return {'weighted_cube_models': models, 'polynomial_parity_models': polynomial_models,
            'largest_cube': 32, 'tolerance': 1e-8}


def tournament_candidate_lists():
    tested = 0
    for k, r in [(3, 1), (3, 2), (5, 2)]:
        arcs = [(i, j) for i in range(k) for j in range(k) if 0 < (j-i) % k <= (k-1)//2]
        labels = {edge: int(rng.integers(r)) for edge in arcs}
        def consistent(I):
            return all(len({labels[i, j] for i in I if (i, j) in labels}) <= 1 for j in I)
        maximum = max(len(I) for size in range(1, k+1) for I in combinations(range(k), size) if consistent(I))
        t = maximum+1
        states = product(range(4), repeat=k*r) if k*r <= 6 else (rng.integers(4, size=k*r) for _ in range(4000))
        for state in states:
            grid = np.array(state).reshape(k, r)
            for gate in [1, 2]:
                T, G = [], []
                for i in range(k):
                    target_fails = [c for c in range(r) if grid[i, c] < 3]
                    gate_fails = [(j, labels[i, j]) for j in range(k) if (i, j) in labels and grid[j, labels[i, j]] >= gate]
                    if len(target_fails) == 1 and not gate_fails:
                        T.append(i)
                    if len(gate_fails) == 1 and not target_fails:
                        G.append(i)
                assert len(T) < t and len(G) <= 3
                assert sum(not any((i, j) in labels for j in G) for i in G) <= 1
                tested += 1
    for M in range(3, 60):
        assert F(3**16, M**20) < 1
    return {'candidate_list_states_and_gate_indices': tested,
            'source_union_bound_parameters': 57, 'scope': 'Small tournaments use their computed forbidden-set threshold.'}


def profiles(values, n):
    # values[q,x] for nested predicates q on a common n-bit cube.
    S, J = [0, 0], [0, 0]
    idx = np.arange(2**n)
    flipped = np.stack([values[:, idx ^ (1 << i)] for i in range(n)], axis=2)
    changed = flipped != values[:, :, None]
    for q in range(len(values)):
        for b in [0, 1]:
            counts = changed[q].sum(axis=1)[values[q] == b]
            S[b] = max(S[b], int(max(counts, default=0)))
    for q, r in combinations(range(len(values)), 2):
        joint = (changed[q] & changed[r]).sum(axis=1)
        for b in [0, 1]:
            counts = joint[(values[q] == b) & (values[r] == b)]
            J[b] = max(J[b], int(max(counts, default=0)))
    return S, J


def joint_profiles():
    bases = []
    for d in [1, 2, 3]:
        L, M = d+2, 2
        n = L*M
        centers = [(1 << L)-1, ((1 << L)-1) << L]
        distance = np.array([min((x ^ z).bit_count() for z in centers) for x in range(2**n)])
        values = np.array([distance <= d+1-q for q in range(1, d+2)])
        S, J = profiles(values, n)
        assert S[0] <= L and S[1] <= L*M and J == [0, 0]
        assert not np.any(values[:, 0])
        assert all(np.all(values[:, z]) for z in centers)
        bases.append({'d': d, 'bits': n, 'S': S, 'J': J})
    compositions = 0
    k, r, child_n = 3, 2, 2
    n = k*r*child_n
    idx = np.arange(2**n)
    arcs = [(0, 1), (1, 2), (2, 0)]
    for _ in range(12):
        scores = rng.permutation(4)
        child = np.array([scores >= q for q in range(1, 4)])
        S, J = profiles(child, child_n)
        labels = {edge: int(rng.integers(r)) for edge in arcs}
        # No 4-set exists, hence t=4 is a valid small-model threshold.
        t, outdegree = 4, 1
        grid = np.array([scores[(idx >> (child_n*a)) & 3] for a in range(k*r)]).reshape(k, r, -1)
        parent = []
        for q in [1, 2]:
            clauses = []
            for i in range(k):
                clause = np.all(grid[i] >= 3, axis=0)
                for j in range(k):
                    if (i, j) in labels:
                        clause &= grid[j, labels[i, j]] < 3-q
                clauses.append(clause)
            parent.append(np.any(clauses, axis=0))
        parent = np.array(parent)
        SP, JP = profiles(parent, n)
        assert SP[1] <= outdegree*S[0]+r*S[1]
        assert JP[1] <= outdegree*J[0]+r*S[1]
        assert SP[0] <= t*S[0]+S[1]+3*J[1]
        assert JP[0] <= t*S[0]+3*J[1]
        # A zero-child state and a strongest-accepting state give row block witnesses.
        low, high = int(np.argmin(scores)), int(np.argmax(scores))
        zero_input = sum(low << (child_n*a) for a in range(k*r))
        masks = [sum((low ^ high) << (child_n*(i*r+c)) for c in range(r)) for i in range(k)]
        assert not np.any(parent[:, zero_input])
        assert all(mask and np.all(parent[:, zero_input ^ mask]) for mask in masks)
        assert all(a & b == 0 for a, b in combinations(masks, 2))
        compositions += 1
    return {'exhaustive_separated_center_bases': bases, 'exhaustive_twelve_bit_compositions': compositions,
            'scope': 'Small-model recurrence and row-block identities, not the source final parameter separation.'}


def reporting_rule():
    # Rademacher inputs, arbitrary interval membership and selector, evaluated exactly.
    m, states = 3, list(product([-1, 1], repeat=4))
    cases = 0
    for _ in range(70):
        allowed = [{x for x in [-1, 1] if rng.integers(2)} for j in range(m)]
        selector = {-1: int(rng.integers(m)), 1: int(rng.integers(m))}
        b = int(rng.integers(-3, 4))
        cells, deficit, error = defaultdict(list), F(0), F(0)
        for state in states:
            u, z = state[0], state[1:]
            i = selector[u]
            B = all(z[j] in allowed[j] for j in range(m))
            P = all(z[j] in allowed[j] for j in range(m) if j != i)
            A = P and not B
            indicator = sum(int(selector[u] == a)*math.prod(int(z[j] in allowed[j]) for j in range(m) if j != a)
                            for a in range(m))-int(B)
            assert indicator == int(A)
            if A:
                label, predictor = ('A',), b
            elif B:
                label, predictor = ('B', z), sum(z)
            else:
                label = ('C', u, i, tuple(z[j] for j in range(m) if j != i))
                predictor = u+sum(z[j] for j in range(m) if j != i)
            L = sum(state)
            cells[label].append((state, L))
            deficit += F(int(A)*(1-(L-b)**2), len(states))
            error += F((L-predictor)**2, len(states))
        assert error == 1-deficit
        retained = sum(F(sum(L for _, L in cell)**2, len(states)*len(cell)) for cell in cells.values())
        assert retained >= m+deficit
        for cell in cells.values():
            # Vanishing full-coordinate Fourier coefficient = degree at most m here.
            assert sum(math.prod(state) for state, _ in cell) == 0
        cases += 1
    # Normalized Gaussian identity avoids underflow of the extremely small p*.
    gaussian = []
    phi = lambda x: math.exp(-x*x/2)/math.sqrt(2*math.pi)
    for m in [3, 5, 9, 17]:
        R, h = math.sqrt(8*math.log(m)), m**(-1.5)
        centers = np.linspace(1-R, 1+R, m)
        beta, mean, variance = [], [], []
        for a in centers:
            # Integrating local offsets avoids cancellation in narrow interval moments.
            mass = quad(lambda v: phi(a+v), -h, h, epsabs=1e-16)[0]
            shift = quad(lambda v: v*phi(a+v), -h, h, epsabs=1e-16)[0]/mass
            var = quad(lambda v: (v-shift)**2*phi(a+v), -h, h, epsabs=1e-16)[0]/mass
            beta.append(mass)
            mean.append(a+shift)
            variance.append(var)
        S = sum(variance)
        intervals = [(-math.inf, -R, m//2), (R, math.inf, m//2)]
        cuts = [-R]+[(centers[i]+centers[i+1])/2-1 for i in range(m-1)]+[R]
        intervals += [(cuts[i], cuts[i+1], i) for i in range(m)]
        J = 0.
        a_mass, a_first, a_second = 0., 0., 0.
        for lo, hi, i in intervals:
            q = quad(lambda t: phi(t)/beta[i]*((1+t-mean[i])**2+S-variance[i]), lo, hi, epsabs=1e-10)[0]
            J += q
            # Direct conditional moments of P minus B, normalized by p*.
            a_mass += quad(lambda t: phi(t)*(1/beta[i]-1), lo, hi, epsabs=1e-10)[0]
            a_first += quad(lambda t: phi(t)*((1+t-mean[i])/beta[i]-(1+t)), lo, hi, epsabs=1e-10)[0]
            a_second += quad(lambda t: phi(t)*((1+S-variance[i]+(1+t-mean[i])**2)/beta[i]-(S+(1+t)**2)), lo, hi, epsabs=1e-10)[0]
        normalized_deficit = 1+S-J
        assert abs((a_mass-a_second)-normalized_deficit) <= 1e-6*max(1, abs(normalized_deficit))
        gaussian.append({'m': m, 'S': S, 'J': J, 'deficit_over_p_star': normalized_deficit,
                         'conditional_variance_on_A': a_second/a_mass-(a_first/a_mass)**2})
    return {'exact_finite_reporting_rules': cases, 'normalized_Gaussian_integrals': gaussian,
            'scope': 'Identity checks at small m; no numerical positive-gain or asymptotic certification claimed.'}


def observation_scores():
    cases = 0
    for n in [2, 3, 4]:
        X = cube(n)
        chars, degrees = characters(X)
        N = len(X)
        H = X.sum(axis=1)
        for _ in range(18):
            labels = rng.integers(1, 6, size=N)
            score = [F(0)]*N
            degree = 0
            for label in set(labels):
                mask = labels == label
                cellscore = F(int(sum(H[mask])), int(sum(mask)))
                for i in np.flatnonzero(mask):
                    score[int(i)] = cellscore
                coefficients = np.array(mask, dtype=int) @ chars
                degree = max(degree, int(max(degrees[coefficients != 0], default=0)))
            v = sum(x*x for x in score)/N
            if v == 0:
                continue
            readout = np.array([1 if x >= 0 else -1 for x in score])
            coefficients = readout @ chars
            actual_degree = int(max(degrees[coefficients != 0], default=0))
            singleton_sum = F(int(sum(coefficients[degrees == 1])), N)
            assert singleton_sum == sum(abs(x) for x in score)/N and actual_degree <= degree
            score_law = Counter()
            for value in score:
                score_law[value] += F(1, N)
            fourth = sum(x**4*p for x, p in score_law.items())
            law = {F(0): F(1)}
            for M in range(1, 7):
                new = Counter()
                for a, pa in law.items():
                    for b, pb in score_law.items():
                        new[a+b] += pa*pb
                law = new
                assert sum(x*x*p for x, p in law.items()) == M*v
                normalized_fourth = sum(x**4*p for x, p in law.items())/(M*v)**2
                assert normalized_fourth == fourth/(M*v*v)+F(3*(M-1), M)
            cases += 1
    return {'exact_finite_observations': cases, 'copy_counts_per_observation': 6,
            'scope': 'Fourier and score calculus; arbitrary tested partitions need not have a variance advantage.'}


CHECKS = [psd_splitting, local_channel, stationary_coupling, weighted_grading,
          tournament_candidate_lists, joint_profiles, reporting_rule, observation_scores]
if __name__ == '__main__':
    result = {}
    for check in CHECKS:
        result[check.__name__] = check()
        print(check.__name__+': passed', flush=True)
    output = {'batch': 'B011', 'status': 'passed', 'seed': SEED,
              'scope': 'Eight groups of finite checks; no global source theorem, Lean build or priority certification.',
              'checks': result}
    Path(__file__).with_name('results.json').write_text(json.dumps(output, indent=2)+'\n', encoding='utf-8')
