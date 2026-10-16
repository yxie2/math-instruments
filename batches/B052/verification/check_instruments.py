"""Exact finite checks for B052; not certification of source headline claims."""
from fractions import Fraction as F
from itertools import product, permutations
from pathlib import Path
import json
import random
import time

import sympy as sp

RNG = random.Random(520)


def slope_balance():
    cases = steps = 0
    for rank in range(2, 11):
        for _ in range(60):
            slopes = [F(RNG.randrange(-12, 13), 3) for _ in range(rank)]
            initial_max, initial_mean = max(slopes), sum(slopes) / rank
            count = 0
            while max(slopes) - min(slopes) > 1:
                low, high, mean = min(slopes), max(slopes), sum(slopes) / rank
                multiplicity = slopes.count(low)
                slopes = [x + 1 if x == low else x for x in slopes]
                assert max(slopes) <= high
                assert sum(slopes) / rank - mean == F(multiplicity, rank)
                count += 1
                assert count <= rank * (initial_max - initial_mean)
            mean = sum(slopes) / rank
            variance = sum((x - mean) ** 2 for x in slopes) / rank
            assert variance <= F(1, 4)
            q = [F(RNG.randrange(-20, 21), 7) for _ in slopes]
            mixed = 2 * sum(q) / rank - mean ** 2
            components = sum(2 * a - x * x for a, x in zip(q, slopes)) / rank
            assert mixed == components + variance
            cases += 1
            steps += count
    return dict(models=cases, modification_steps=steps, arithmetic="exact rational",
                scope="Direct-sum slope models; no sheaf existence assertion.")


def divisor_layers():
    cases = equality = 0
    for N in range(1, 7):
        for length in range(1, 7):
            for ns in product(range(N + 1), repeat=length):
                lhs = N * sum((2 * j + 1) * n for j, n in enumerate(ns)) - sum(ns) ** 2
                rhs = sum(n * (N - n) for n in ns)
                rhs += 2 * sum(ns[j] * (N - ns[l]) for j in range(length) for l in range(j))
                assert lhs == rhs and rhs >= 0
                cases += 1
                equality += lhs == 0
    m, q, b = sp.symbols("m q b")
    assert sp.expand(2 * (q + b * m + b ** 2 / 2) - (m + b) ** 2 - (2 * q - m ** 2)) == 0
    mu, k, h, chi, z, d, c2, K2, c1sq = sp.symbols("mu k h chi z d c2 K2 c1sq")
    # z=ch2(G)/rank, d=c1(G).K/rank, c1sq=c1(G)^2/rank^2.
    m_expr = mu - k / (2 * h) - sp.Rational(3, 2)
    q_expr = chi / h + z / h - d / (2 * h) - 1 - sp.Rational(3, 2) * m_expr
    variance = 2 * q_expr - m_expr ** 2
    rr = sp.Rational(1, 4) + 2 * chi / h + (2 * z - d) / h - (mu - k / (2 * h)) ** 2
    assert sp.simplify(variance - rr) == 0
    bogomolov_bound = rr.subs(z, c1sq / 2)
    hodge_remainder = (c1sq - d + K2 / 4) / h - (mu - k / (2 * h)) ** 2
    constant = sp.Rational(1, 4) - (K2 - 2 * c2) / (12 * h)
    assert sp.simplify(bogomolov_bound.subs(chi, (K2 + c2) / 12) - hodge_remainder - constant) == 0
    assert sp.simplify(constant + sp.Rational(1, 4) - (6 * h - K2 + 2 * c2) / (12 * h)) == 0
    return dict(layer_sequences=cases, equality_cases=equality, symbolic_identities=4,
                scope="Layer and Riemann-Roch arithmetic; geometric hypotheses not tested.")


def compose(a, b):
    return tuple(a[b[i]] for i in range(len(a)))


def inverse(a):
    return tuple(a.index(i) for i in range(len(a)))


def subgroup(generators, n):
    S = {tuple(range(n))}
    todo = list(S)
    while todo:
        g = todo.pop()
        for h in generators:
            x = compose(g, h)
            if x not in S:
                S.add(x)
                todo.append(x)
    return sorted(S)


class GroupAlgebra:
    def __init__(self, elements, p):
        self.G, self.p = list(elements), p
        self.n = len(elements)
        index = {g: i for i, g in enumerate(elements)}
        self.mul = [[index[compose(g, h)] for h in elements] for g in elements]
        self.inv = [index[inverse(g)] for g in elements]
        self.one = index[tuple(range(len(elements[0])))]

    def basis(self, indices):
        a = [0] * self.n
        for i in indices:
            a[i] = (a[i] + 1) % self.p
        return a

    def multiply(self, a, b):
        c = [0] * self.n
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    c[self.mul[i][j]] = (c[self.mul[i][j]] + x * y) % self.p
        return c

    def conjugate(self, h, g):
        return self.mul[self.mul[h][g]][self.inv[h]]

    def orbits(self, H):
        left, result = set(range(self.n)), []
        while left:
            orbit = {self.conjugate(h, min(left)) for h in H}
            result.append(orbit)
            left -= orbit
        return result


def modular_projection():
    cases = pairs = quotient_checks = 0
    for n, p, generators in [
        (3, 2, [(1, 0, 2)]), (3, 3, [(1, 2, 0)]),
        (4, 2, [(1, 0, 2, 3)]),
        (4, 2, [(1, 0, 3, 2), (2, 3, 0, 1)]),
        (4, 3, [(1, 2, 0, 3)]),
    ]:
        A = GroupAlgebra(list(permutations(range(n))), p)
        Q = {A.G.index(g) for g in subgroup(generators, n)}
        C = {g for g in range(A.n) if all(A.conjugate(h, g) == g for h in Q)}
        H = {g for g in range(A.n) if {A.conjugate(g, h) for h in Q} == Q}
        assert C <= H and Q <= H

        def br(a):
            return [a[i] if i in C else 0 for i in range(A.n)]

        basis = [A.basis(o) for o in A.orbits(Q)]
        for a, b in product(basis, repeat=2):
            assert br(A.multiply(a, b)) == A.multiply(br(a), br(b))
            pairs += 1
        cosets = {tuple(sorted(A.mul[h][q] for q in Q)) for h in H}
        for orbit in A.orbits(range(A.n)):
            a, ba = A.basis(orbit), br(A.basis(orbit))
            assert [sum(a[g] for g in c) % p for c in cosets] == [sum(ba[g] for g in c) % p for c in cosets]
            quotient_checks += 1
        cases += 1
    # The same orbit average fails in the wrong characteristic.
    A = GroupAlgebra(list(permutations(range(3))), 3)
    Q = {A.one, A.G.index((1, 0, 2))}
    C = {g for g in range(A.n) if all(A.conjugate(h, g) == g for h in Q)}
    a = A.basis([A.G.index((1, 2, 0)), A.G.index((2, 0, 1))])
    assert all(a[g] == 0 for g in C)
    assert A.multiply(a, a)[A.one] == 2
    return dict(group_subgroup_cases=cases, orbit_basis_pairs=pairs, central_quotient_checks=quotient_checks,
                wrong_characteristic_control="fails as expected")


def higman_trace():
    pairs = annihilations = 0
    for n, p in [(3, 2), (3, 3)]:
        A = GroupAlgebra(list(permutations(range(n))), p)
        H = [A.basis([A.conjugate(x, a) for x in range(A.n)]) for a in range(A.n)]
        for a, b in product(range(A.n), repeat=2):
            # L_b R_a permutes the group basis; its matrix trace counts fixed vectors.
            trace = sum(A.mul[A.mul[b][x]][a] == x for x in range(A.n)) % p
            assert A.multiply(H[a], A.basis([b]))[A.one] == trace
            pairs += 1
        d = [0] * A.n
        for a in range(A.n):
            term = A.multiply(H[a], A.basis([A.inv[a]]))
            d = [(x + y) % p for x, y in zip(d, term)]
        direct = A.basis([A.mul[A.mul[A.mul[x][y]][A.inv[x]]][A.inv[y]] for x, y in product(range(A.n), repeat=2)])
        assert d == direct
        for orbit in A.orbits(range(A.n)):
            assert len({d[i] for i in orbit}) == 1
        if p == 2:
            # In F_2[S_3], the norm line is a nonzero square-zero ideal, hence lies in the radical.
            norm = [1] * A.n
            assert A.multiply(norm, norm) == [0] * A.n
            for a in range(A.n):
                assert A.multiply(A.basis([a]), norm) == norm
                assert A.multiply(H[a], norm) == [0] * A.n
                annihilations += 1
            assert A.multiply(d, norm) == [0] * A.n
    matrices = 0
    for p, s in [(2, 2), (2, 4), (3, 3), (5, 5)]:
        for t in range(1, p):
            ti = pow(t, -1, p)
            units = []
            for i, j in product(range(s), repeat=2):
                e = sp.zeros(s)
                e[i, j] = 1
                units.append((e, ti * e.T))
            def H(a):
                return sum((e * a * dual for e, dual in units), sp.zeros(s)).applyfunc(lambda x: int(x) % p)
            for _ in range(5):
                a = sp.Matrix(s, s, [RNG.randrange(p) for _ in range(s * s)])
                assert H(a) == (ti * sp.trace(a) * sp.eye(s)).applyfunc(lambda x: int(x) % p)
                matrices += 1
            d = sum((H(e) * dual for e, dual in units), sp.zeros(s)).applyfunc(lambda x: int(x) % p)
            assert d == (ti * ti % p) * sp.eye(s)
            assert s % p == 0 and d != sp.zeros(s)
    return dict(group_trace_pairs=pairs, radical_line_annihilations=annihilations,
                matrix_examples=matrices, characteristic_divides_size=True)


def rank_mod(matrix, p):
    rows = [[int(x) % p for x in row] for row in matrix]
    r = 0
    for c in range(len(rows[0]) if rows else 0):
        pivot = next((i for i in range(r, len(rows)) if rows[i][c]), None)
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        inv = pow(rows[r][c], -1, p)
        rows[r] = [x * inv % p for x in rows[r]]
        for i in range(len(rows)):
            if i != r:
                a = rows[i][c]
                rows[i] = [(x - a * y) % p for x, y in zip(rows[i], rows[r])]
        r += 1
    return r


def mod(M, p):
    return M.applyfunc(lambda x: int(x) % p)


def norm_projectivity():
    examples = tensors = 0
    blocks = {}
    for p in [2, 3, 5]:
        for s in range(1, p + 1):
            J = sp.zeros(s)
            for i in range(s - 1):
                J[i, i + 1] = 1
            T = sp.eye(s) + J
            norm = mod(sum((T ** i for i in range(p)), sp.zeros(s)), p)
            assert norm == mod(J ** (p - 1), p)
            blocks[p, s] = (T, norm)
        for length in range(1, 5):
            for sizes in product(range(1, p + 1), repeat=length):
                N = sp.diag(*(blocks[p, s][1] for s in sizes))
                # Each block contributes one invariant and one coinvariant generator.
                norm_rank = rank_mod(N.tolist(), p)
                assert norm_rank == sizes.count(p)
                assert (norm_rank == length) == all(s == p for s in sizes)
                examples += 1
        for s, t in product(range(1, p + 1), repeat=2):
            A, NA = blocks[p, s]
            B, NB = blocks[p, t]
            direct = sum((sp.kronecker_product(A ** i, B ** j) for i, j in product(range(p), repeat=2)), sp.zeros(s * t))
            assert mod(direct, p) == sp.kronecker_product(NA, NB)
            tensors += 1
    return dict(jordan_module_examples=examples, independent_action_products=tensors,
                scope="Cyclic p-groups and ordinary matrix tensor products; no simulation of a tensor category.")


class Field:
    def __init__(self, p, coefficients):
        self.p, self.f = p, coefficients
        self.m, self.q = len(coefficients) - 1, p ** (len(coefficients) - 1)

    def digits(self, a):
        result = []
        for _ in range(self.m):
            result.append(a % self.p)
            a //= self.p
        return result

    def encode(self, digits):
        return sum((x % self.p) * self.p ** i for i, x in enumerate(digits))

    def add(self, a, b):
        return self.encode([x + y for x, y in zip(self.digits(a), self.digits(b))])

    def neg(self, a):
        return self.encode([-x for x in self.digits(a)])

    def mul(self, a, b):
        A, B = self.digits(a), self.digits(b)
        c = [0] * (2 * self.m - 1)
        for i, j in product(range(self.m), repeat=2):
            c[i + j] += A[i] * B[j]
        for i in reversed(range(self.m, len(c))):
            value = c[i] % self.p
            for j in range(self.m + 1):
                c[i - self.m + j] -= value * self.f[j]
        return self.encode(c[:self.m])

    def power(self, a, n):
        b = 1
        while n:
            if n & 1:
                b = self.mul(b, a)
            a, n = self.mul(a, a), n // 2
        return b

    def sum(self, values):
        result = 0
        for v in values:
            result = self.add(result, v)
        return result

    def independent(self, values):
        return rank_mod([self.digits(a) for a in values], self.p) == len(values)

    def kernel(self, rows, n):
        rows = [row[:] for row in rows]
        pivots, r = [], 0
        for c in range(n):
            pivot = next((i for i in range(r, len(rows)) if rows[i][c]), None)
            if pivot is None:
                continue
            rows[r], rows[pivot] = rows[pivot], rows[r]
            inv = self.power(rows[r][c], self.q - 2)
            rows[r] = [self.mul(x, inv) for x in rows[r]]
            for i in range(len(rows)):
                if i != r:
                    a = rows[i][c]
                    rows[i] = [self.add(x, self.neg(self.mul(a, y))) for x, y in zip(rows[i], rows[r])]
            pivots.append(c)
            r += 1
        assert r == n - 1
        free = next(i for i in range(n) if i not in pivots)
        v = [0] * n
        v[free] = 1
        for i, c in enumerate(pivots):
            v[c] = self.neg(rows[i][free])
        return v


def moore_selection():
    cases = equations = 0
    fields = [(2, [1, 1, 0, 1]), (2, [1, 1, 0, 0, 1]),
              (3, [1, 0, 1]), (3, [1, 2, 0, 1]), (5, [2, 0, 1])]
    for p, polynomial in fields:
        K = Field(p, polynomial)
        # This exhaustively confirms every nonzero element is invertible in each quotient.
        for a in range(1, K.q):
            assert K.mul(a, K.power(a, K.q - 2)) == 1
        samples = []
        if K.q == 8:
            samples += [a for a in product(range(K.q), repeat=3) if K.independent(a)]
        for r in range(1, K.m + 1):
            for _ in range(60):
                while True:
                    alpha = [RNG.randrange(K.q) for _ in range(r)]
                    if K.independent(alpha):
                        break
                samples.append(alpha)
        for alpha in samples:
            r = len(alpha)
            beta = [K.power(a, p ** ((-(r - 2)) % K.m)) for a in alpha]
            B = [[K.power(b, p ** s) for b in beta] for s in range(r - 1)]
            lam = K.kernel(B, r)
            assert K.independent(lam)
            for j in range(r - 1):
                assert K.sum(K.mul(a, K.power(l, p ** j)) for a, l in zip(alpha, lam)) == 0
                equations += 1
            cases += 1
        bad = K.kernel([[1, 1]], 2)
        assert not K.independent(bad)
    return dict(extension_fields=len(fields), independent_inputs=cases,
                frobenius_equations=equations, dependent_input_controls=len(fields))


def torus_gluing():
    a, b = sp.symbols("a b", positive=True)
    M = sp.Matrix([[1, 1], [1, 0]])
    assert (M.T * sp.diag(a, b) * M)[0, 1] == a
    compatible = incompatible = 0
    for w, x, y, z in product(range(-3, 4), repeat=4):
        if abs(w * z - x * y) != 1:
            continue
        U, V = w * x, y * z
        possible = U * V < 0 or U == V == 0
        if possible:
            A, B = (abs(V), abs(U)) if U * V < 0 else (1, 1)
            assert A > 0 and B > 0 and U * A + V * B == 0
            compatible += 1
        else:
            assert (U >= 0 and V >= 0 or U <= 0 and V <= 0) and (U or V)
            for A, B in product(range(1, 5), repeat=2):
                assert U * A + V * B != 0
            incompatible += 1
    return dict(compatible_matrices=compatible, obstructed_matrices=incompatible,
                source_shear="forces a positive squared length to vanish")


def boundary_penalty():
    cases = sharp = 0
    for n in range(2, 6):
        for _ in range(10):
            A = sp.Matrix(n, n, [RNG.randrange(-3, 4) for _ in range(n * n)])
            H = A.T * A + sp.eye(n)
            B = sp.Matrix(2, n, [RNG.randrange(-3, 4) for _ in range(2 * n)])
            if B.rank() < 2:
                B[0, 0], B[1, 1] = 9, 9
            assert B.rank() == 2
            S = B * H.inv() * B.T
            e, p = sp.Matrix([1, 0]), sp.Matrix([RNG.randrange(-3, 4), RNG.randrange(-3, 4)])
            mu = sp.Rational(RNG.randrange(1, 8), RNG.randrange(1, 8))
            se, spe, spp = (e.T * S * e)[0], (p.T * S * e)[0], (p.T * S * p)[0]
            factor = spp - spe ** 2 / (se + 1 / mu)
            updated = (S.inv() + mu * e * e.T).inv()
            assert sp.simplify((p.T * updated * p)[0] - factor) == 0
            Hnew = H + mu * B.T * e * e.T * B
            for _ in range(4):
                v = sp.Matrix([RNG.randrange(-5, 6) for _ in range(n)])
                X = B * v
                assert (p.T * X)[0] ** 2 <= factor * (v.T * Hnew * v)[0]
                cases += 1
            v = Hnew.inv() * B.T * p
            assert (p.T * B * v)[0] ** 2 == factor * (v.T * Hnew * v)[0]
            sharp += 1
    S, e, p = sp.diag(2, 3), sp.Matrix([1, 0]), sp.Matrix([0, 1])
    assert (p.T * S * e)[0] == 0
    assert (p.T * (S.inv() + e * e.T).inv() * p)[0] == (p.T * S * p)[0]
    return dict(inequality_examples=cases, sharp_models=sharp, orthogonal_control="no improvement")


def main():
    started = time.perf_counter()
    checks = {}
    for fn in [slope_balance, divisor_layers, modular_projection, higman_trace,
               norm_projectivity, moore_selection, torus_gluing, boundary_penalty]:
        checks[fn.__name__] = {"status": "passed", **fn()}
    result = dict(batch="B052", status="passed", checks=checks,
                  elapsed_seconds=round(time.perf_counter() - started, 3),
                  scope="Selected finite identities and models only; no source headline theorem or Lean solution certified.")
    (Path(__file__).parent / "results.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
