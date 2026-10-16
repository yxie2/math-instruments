"""Finite checks of B010 mechanisms, not certification of the source headlines."""
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, combinations_with_replacement, permutations, product
from pathlib import Path
import json
import math
import numpy as np

SEED = 111118128131
rng = np.random.default_rng(SEED)


def sample_gluing():
    laws = [F(1, 3), F(2, 5), F(3, 4)]
    vectors = list(product([0, 1], repeat=3))
    def prob(v):
        return math.prod(p if x else 1-p for p, x in zip(laws, v))
    for mask in vectors:
        glued = Counter()
        for s, v in product(vectors, repeat=2):
            w = tuple(s[i] if mask[i] else v[i] for i in range(3))
            glued[w] += prob(s) * prob(v)
        assert all(glued[w] == prob(w) for w in vectors)
    table = [[0, 1], [1, 0]]
    expected_min = sum(F(min(row), 2) for row in table)
    min_expected = min(sum(F(row[j], 2) for row in table) for j in range(2))
    assert expected_min == 0 and min_expected == F(1, 2)
    return {'exact_masks': len(vectors), 'sample_value_pairs_per_mask': 64,
            'expected_minimum': str(expected_min), 'minimum_expectation': str(min_expected)}


@lru_cache(None)
def rank(labels):
    basis = {}
    for x in labels:
        while x:
            b = x.bit_length()-1
            if b not in basis:
                basis[b] = x
                break
            x ^= basis[b]
    return len(basis)


def rk(labels):
    return rank(tuple(sorted(set(labels))))


def closure(labels):
    return {x for x in range(8) if rk(set(labels) | {x}) == rk(labels)}


def pivot_marks(sequence):
    seen, marks, retained = set(), {}, []
    for label, mark, occurrence in sequence:
        if rk(seen | {label}) > rk(seen):
            retained.append(occurrence)
        seen.add(label)
        for f in range(1, 8):
            if f not in marks and f in closure(seen):
                marks[f] = mark
    return tuple(marks[f] for f in range(1, 8)), tuple(sorted(retained))


def marked_pivots():
    cases, enumerated, data = 0, 0, []
    old_labels = [1, 1, 2, 3, 0, 4]
    for bits in product([0, 1], repeat=3):
        old = [(x, bits[i % 3], i) for i, x in enumerate(old_labels)]
        reduced = [old[i] for i in [0, 2, 5]]
        for movable in [[], [1], [3], [0], [3, 5], [2, 2], [0, 7]]:
            s = len(movable)
            patterns, bases = set(), set()
            for order in permutations(range(s)):
                for positions in combinations(range(len(old)+s), s):
                    for marks in product([0, 1], repeat=s):
                        sequence, old_index, new_index = [], 0, 0
                        for t in range(len(old)+s):
                            if t in positions:
                                j = order[new_index]
                                sequence.append((movable[j], marks[j], 10+j))
                                new_index += 1
                            else:
                                sequence.append(old[old_index])
                                old_index += 1
                        pattern, basis = pivot_marks(sequence)
                        filtered = [x for x in sequence if x[2] >= 10 or x in reduced]
                        assert pivot_marks(filtered)[0] == pattern
                        patterns.add(pattern)
                        bases.add(basis)
                        enumerated += 1
            bound = 4**s * sum(math.comb(7, k) for k in range(s+1))
            assert len(patterns) <= bound and len(bases) <= 4**s
            cases += 1
            data.append([s, len(patterns), len(bases)])
    return {'old_mark_and_movable_models': cases, 'interleavings_with_marks': enumerated,
            'max_pattern_count': max(x[1] for x in data), 'scope': 'Binary rank-three matroids with repeated and zero labels.'}


def rank_budget():
    maximum = 0
    for _ in range(500):
        order = list(rng.permutation(np.arange(1, 8)))
        J = set(int(x) for x in rng.choice(8, size=3, replace=True))
        previous, total, telescoped = set(), 0, 0
        for end in [2, 4, 7]:
            current = set(int(x) for x in order[:end])
            new = list(current - previous)
            A = previous | set(new[:len(new)//2])
            S = current - A
            B = A | {x for x in closure(A | J) if rng.integers(2)}
            loss = rk(A | S)-rk(A)-rk(B | S)+rk(B)
            charge = rk(previous | J)-rk(previous)-rk(current | J)+rk(current)
            assert 0 <= loss <= charge
            total += loss
            telescoped += charge
            previous = current
        assert total <= telescoped <= rk(J) <= len(J)
        maximum = max(maximum, total)
    previous, losses = set(), []
    for x in [1, 2, 4]:
        A, S, J = previous, {x}, {x}
        losses.append(rk(A | S)-rk(A)-rk(A | J | S)+rk(A | J))
        previous |= S
    assert sum(losses) == 3 > 1
    return {'random_exact_rank_chains': 500, 'max_total_loss': maximum,
            'changing_generator_negative_control': losses}


def tree_quotas():
    inequalities = 0
    for n in range(1, 21):
        quota = [2**j for j in range(n)]
        for i in range(1, n+1):
            assert sum(quota[:i]) == 2**i-1 < 2**i
            if i < n:
                assert 1+sum(quota[i:]) > sum(quota[i:])
            inequalities += 1
    checked = 0
    for n in [1, 2]:
        for i in range(1, n+1):
            paths, nodes = [], [set() for _ in range(n)]
            for spine in range(2**i):
                prefix = []
                for depth in range(i):
                    v = ('s', spine, depth)
                    nodes[depth].add(v)
                    prefix.append(v)
                tails = 1 if i == n else 1+sum(2**(j-1) for j in range(i+1, n+1))
                for tail in range(tails):
                    path = list(prefix)
                    for depth in range(i, n):
                        v = ('t', spine, tail, depth)
                        nodes[depth].add(v)
                        path.append(v)
                    paths.append(set(path))
            choices = [[set(c) for k in range(min(2**j, len(level))+1)
                        for c in combinations(sorted(level), k)] for j, level in enumerate(nodes)]
            for levels in product(*choices):
                marking = set().union(*levels)
                assert any(not path & marking for path in paths)
                checked += 1
    for red, blue in product([0, 1], repeat=2):
        if red+blue <= 1:
            assert not (red and blue)
    return {'phase_quota_inequalities': inequalities, 'exhaustive_small_phase_markings': checked,
            'two_tree_depth_one_case': 'passed', 'scope': 'General d pruning is an analytic argument, not exhaustively tested.'}


def scalar_encoding():
    subclasses = ['Tp', 'Tm', 'S', 'Z', 'Y', 'Up', 'Um', 'W', 'DM', 'DG', 'FT', 'FM', 'FG']
    roles = ['X']*3+['A']*2+['U']*3+['D']*2+['F']*3
    extra = [{'Tp': 1, 'Tm': 1, 'FT': -1}, {'Z': 1, 'FT': -1, 'FM': -1},
             {'Up': 1, 'Um': 1, 'FT': -1, 'FM': -1}, {'DM': 1, 'FT': -1, 'FM': -1}, {'Tm': 1, 'Um': -1}]
    digits = {s: [5*(r == role)-1 for r in ['X', 'A', 'U', 'D', 'F']]+[e.get(s, 0) for e in extra]
              for s, role in zip(subclasses, roles)}
    primary = {s: sum(100**j * x for j, x in enumerate(digits[s])) for s in subclasses}
    expected = {tuple(sorted(x)) for x in [('Tp', 'Z', 'Up', 'DM', 'FT'), ('Tm', 'Z', 'Um', 'DM', 'FT'),
                ('S', 'Z', 'Up', 'DM', 'FM'), ('S', 'Y', 'W', 'DG', 'FG')]}
    found, tuples = set(), 0
    for items in combinations_with_replacement(subclasses, 5):
        score = sum(primary[s] for s in items)
        zero_digits = all(sum(digits[s][j] for s in items) == 0 for j in range(10))
        assert (score == 0) == zero_digits
        if score == 0:
            found.add(tuple(sorted(items)))
        tuples += 1
    assert found == expected
    P0 = 4*sum(100**j for j in range(10))+1
    gamma, n = F(1, 1000*P0), 4
    mu = gamma/(1000*3**n)
    nu = mu/1000
    sizes = []
    for s, role in zip(subclasses, roles):
        for v in range(1, n+1):
            q = (1 if role in ['X', 'D'] else -2 if role == 'A' else 0)*3**v
            for w in [-6, 0, 6]:
                a = F(1, 5)+gamma*primary[s]+mu*q+nu*w
                assert F(1, 6) < a < F(7, 30)
                sizes.append((s, v, w, a, q))
    for _ in range(500):
        chosen = [sizes[int(i)] for i in rng.integers(len(sizes), size=5)]
        a = sum(x[3] for x in chosen)
        p = sum(primary[x[0]] for x in chosen)
        q = sum(x[4] for x in chosen)
        w = sum(x[2] for x in chosen)
        assert abs(mu*q+nu*w) < gamma and abs(nu*w) < mu
        if a <= 1:
            assert p <= 0
            if p == 0:
                assert q <= 0
                if q == 0:
                    assert w <= 0
    for x, a, d in product(range(1, 7), repeat=3):
        q = 3**x+3**d-2*3**a
        if q <= 0:
            assert x <= a and d <= a
        assert (q == 0) == (x == a == d)
    for _ in range(100):
        labels = list(range(1, 7))*3
        stock_x, stock_d = Counter(labels), Counter(labels)
        tuples_by_label = []
        outside_a = Counter()
        for a in rng.permutation(labels):
            a = int(a)
            xs = [x for x in stock_x if x <= a and stock_x[x]]
            ds = [d for d in stock_d if d <= a and stock_d[d]]
            if xs and ds and rng.integers(3):
                x, d = int(rng.choice(xs)), int(rng.choice(ds))
                stock_x[x] -= 1
                stock_d[d] -= 1
                tuples_by_label.append((x, a, d))
            else:
                outside_a[a] += 1
        K = sum(outside_a.values())+sum(stock_x.values())+sum(stock_d.values())
        for h in range(1, 7):
            for r, outside in [(0, stock_x), (2, stock_d)]:
                crossing = sum(t[r] <= h < t[1] for t in tuples_by_label)
                assert crossing == sum(outside_a[j]-outside[j] for j in range(1, h+1))
                assert crossing <= K
            bad = outside_a[h]+sum(t[1] == h and (t[0] != h or t[2] != h) for t in tuples_by_label)
            assert bad <= 3*K
    return {'five_item_subclass_multisets': tuples, 'zero_patterns': len(found),
            'exact_item_sizes': len(sizes), 'random_tuple_scale_checks': 500, 'prefix_inventory_models': 100}


def words(length):
    return [''.join(x) for x in product('ab', repeat=length)]


def occurrences(t, s):
    return sum(t[i:i+len(s)] == s for i in range(len(t)-len(s)+1))


def block_coefficient(period, s, r):
    A = lambda k: period[k % len(period)]
    return sum(r[j:j+len(s)] == s and all(r[h] == A(h-j) for h in range(1, len(r)-1))
               and r[0] != A(-j) and r[-1] != A(len(r)-1-j)
               for j in range(1, len(r)-len(s)))


def forced_counts(inputs):
    required = {s for s in inputs if s and not any(s != r and s in r for r in inputs)}
    V = {s[i:j] for s in required for i in range(len(s)) for j in range(i+1, len(s)+1)}
    m = {}
    def B(period, s):
        return sum(block_coefficient(period, s, r)*m[r] for r in V if len(r) >= len(s)+2)
    for s in sorted(V, key=lambda x: (-len(x), x)):
        values = [sum(m.get(c+s, 0) for c in 'ab'), sum(m.get(s+c, 0) for c in 'ab'), int(s in required)]
        for v in V:
            if len(v) <= len(s) or not v.startswith(s):
                continue
            for p in range(1, len(v)):
                if (len(v)-len(s)) % p or any(v[i] != v[i % p] for i in range(len(v))):
                    continue
                if m[v] > B(v[:p], v):
                    values.append(B(v[:p], s)+(len(v)-len(s))//p+1)
        m[s] = max(values)
    return required, V, m


def periodic_counts():
    instances = [(s,) for k in range(1, 5) for s in words(k)]
    pool = [s for k in range(1, 4) for s in words(k)]
    instances += list(combinations(pool, 2))
    instances += [tuple(rng.choice(pool, size=3, replace=False)) for _ in range(40)]
    comparisons, brackets = 0, 0
    test_texts = [t for k in range(1, 8) for t in words(k)]
    for inputs in instances:
        required, V, m = forced_counts(inputs)
        u = {s: m[s]-sum(m.get(c+s, 0) for c in 'ab') for s in V}
        d = {s: m[s]-sum(m.get(s+c, 0) for c in 'ab') for s in V}
        assert all(x >= 0 for x in list(u.values())+list(d.values()))
        assert sum(u.values()) == sum(d.values()) == sum(m.get(c, 0) for c in 'ab')
        for s in V:
            assert u[s]+sum(d.get(c+s, 0) for c in 'ab') == d[s]+sum(u.get(s+c, 0) for c in 'ab')
        for t in test_texts:
            if not all(s in t for s in required):
                continue
            N = {s: occurrences(t, s) for s in V}
            assert all(m[s] <= N[s] for s in V)
            assert sum(m.get(c, 0) for c in 'ab') <= len(t)
            comparisons += 1
        # Direct nearest-mismatch comparison, independent of the coefficient implementation.
        t = ''.join(inputs)+'ba'+''.join(reversed(inputs))
        for period in ['a', 'b', 'ab', 'aab', 'abab']:
            for s in V:
                if any(s[j] != period[j % len(period)] for j in range(len(s))):
                    continue
                count = 0
                for pos in range(len(t)-len(s)+1):
                    if t[pos:pos+len(s)] != s:
                        continue
                    left = [i for i in range(pos) if t[i] != period[(i-pos) % len(period)]]
                    right = [i for i in range(pos+len(s), len(t)) if t[i] != period[(i-pos) % len(period)]]
                    if left and right and t[left[-1]:right[0]+1] in V:
                        count += 1
                calculated = sum(block_coefficient(period, s, r)*occurrences(t, r) for r in V)
                assert calculated == count <= occurrences(t, s)
                brackets += 1
    for h in range(2, 11):
        _, _, m = forced_counts(['a'*h])
        assert all(m['a'*j] == h-j+1 for j in range(1, h+1))
    return {'instances': len(instances), 'actual_common_superstrings': comparisons,
            'nearest_mismatch_identities': brackets, 'constant_words': 9}


def periodic_layers():
    models, turns = 0, 0
    for p in [1, 2, 3, 5]:
        for _ in range(25):
            texts = 'abcab'[:p]
            walks = []
            for d in [1, 2, 3]:
                P = d*p
                increments = np.bincount(rng.integers(P, size=P), minlength=P)
                raw = [int(x) for x in np.cumsum(increments)]
                offset = max(x+1-raw[x] for x in range(P))+int(rng.integers(4))
                values = [x+offset for x in raw]
                def make_z(v, P):
                    return lambda x: v[x % P]+(x//P)*P
                z = make_z(values, P)
                assert all(z(x-1) >= x and z(x) >= z(x-1) for x in range(-P, 2*P))
                walks.append((d, z))
            def word(x, e):
                return ''.join(texts[i % p] for i in range(x, e))
            def edges(x, entry, exit):
                result = Counter()
                for e in range(entry, exit):
                    result[('u', word(x, e), word(x, e+1))] += 1
                result[('d', word(x, exit), word(x+1, exit))] += 1
                return result
            original = Counter()
            for d, z in walks:
                for x in range(d*p):
                    original.update(edges(x, z(x-1), z(x)))
            E = lambda x: sorted(z(x+r*p)-r*p for d, z in walks for r in range(d))
            sorted_edges, layer_cost = Counter(), [0]*6
            for x in range(p):
                assert E(x+p) == [a+p for a in E(x)]
                for i, (entry, exit) in enumerate(zip(E(x-1), E(x))):
                    assert x <= entry <= exit
                    sorted_edges.update(edges(x, entry, exit))
                    layer_cost[i] += exit-entry
            assert sorted_edges == original and layer_cost == [p]*6
            models += 1
            turns += sum(d*p for d, _ in walks)
    return {'periodic_window_models': models, 'original_turn_steps': turns,
            'scope': 'Exact integer edge multisets, including multi-turn walks and empty windows.'}


def equality_projections():
    cases, smallest = 0, 0.
    for N in range(10):
        for q in range(N+1):
            states = [sum(1 << i for i in c) for c in combinations(range(N), q)]
            index = {x: i for i, x in enumerate(states)}
            M = len(states)
            G, S = np.zeros((M, M)), np.zeros((M, M))
            for i, j in combinations(range(N), 2):
                tau = np.zeros((M, M))
                equal = []
                for row, x in enumerate(states):
                    a, b = (x >> i) & 1, (x >> j) & 1
                    y = x if a == b else x ^ (1 << i) ^ (1 << j)
                    tau[row, index[y]] = 1
                    equal.append(float(a == b))
                G += (np.eye(M)-tau)/2
                z = np.array(equal)-np.mean(equal)
                if z @ z > 1e-20:
                    S += np.outer(z, z)/(z @ z)
            ev = np.linalg.eigvalsh(G-S)
            smallest = min(smallest, float(ev[0]))
            assert ev[0] > -1e-10
            assert np.linalg.norm(S @ np.ones(M)) < 1e-10
            if N >= 3 and 0 < q < N:
                p = F(q*(q-1)+(N-q)*(N-q-1), N*(N-1))
                mu1 = F((2*q-N)**2, 2*(N-2))/p
                assert mu1 <= F(N, 2)
                linear = np.array([(x & 1)-F(q, N) for x in states], dtype=float)
                assert np.linalg.norm(G @ linear-N/2*linear) < 1e-10
                assert np.linalg.norm(S @ linear-float(mu1)*linear) < 1e-10
            if (N, q) == (4, 2):
                assert abs(max(np.linalg.eigvalsh(S))-3) < 1e-10
            cases += 1
    return {'full_slice_matrices': cases, 'largest_state_space': math.comb(9, 4),
            'minimum_numerical_difference_eigenvalue': smallest, 'tolerance': 1e-10}


def exact_residual():
    examples = []
    for M in [2, 3, 4, 5, 7]:
        # Half lazy cycle; M=2 counts its repeated two directed neighbors.
        A = [[0]*M for _ in range(M)]
        for i in range(M):
            A[i][i] += 2
            A[i][(i+1) % M] += 1
            A[i][(i-1) % M] += 1
        D = (M-1).bit_length()+3
        delta = F(1, 2**D)
        counts, Q, steps = [1]+[0]*(M-1), 1, 0
        while True:
            tv = sum(abs(F(a, Q)-F(1, M)) for a in counts)/2
            if tv <= delta**2:
                break
            counts = [sum(counts[i]*A[i][j] for i in range(M)) for j in range(M)]
            Q *= 4
            steps += 1
            assert steps < 2000
        weights = [2**D*Q-M*(2**D-1)*a for a in counts]
        assert min(weights) >= 0 and sum(weights) == M*Q
        for a, w in zip(counts, weights):
            assert (1-delta)*F(a, Q)+delta*F(w, M*Q) == F(1, M)
        examples.append({'states': M, 'steps': steps, 'D': D, 'denominator_bits': Q.bit_length()})
    delta, p = F(1, 4), [F(9, 10), F(1, 10)]
    residual = [(F(1, 2)-(1-delta)*x)/delta for x in p]
    assert min(residual) < 0
    return {'exact_cycle_examples': examples, 'insufficient_accuracy_residual': [str(x) for x in residual],
            'scope': 'Finite rational-law correction, not the global graph-switch mixing theorem.'}


CHECKS = [sample_gluing, marked_pivots, rank_budget, tree_quotas, scalar_encoding,
          periodic_counts, periodic_layers, equality_projections, exact_residual]
if __name__ == '__main__':
    results = {}
    for check in CHECKS:
        results[check.__name__] = check()
        print(check.__name__+': passed', flush=True)
    output = {'batch': 'B010', 'status': 'passed', 'seed': SEED,
              'scope': 'Nine groups of finite mechanism checks; no full source theorem, Lean or priority certification.',
              'checks': results}
    Path(__file__).with_name('results.json').write_text(json.dumps(output, indent=2)+'\n', encoding='utf-8')
