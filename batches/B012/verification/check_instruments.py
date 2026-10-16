"""Finite checks for B012; not a proof or Lean verification of source theorems."""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import log2
from pathlib import Path
import json
import random
import sys

RNG = random.Random(2026101612)
RESULTS = []


def subsets(items):
    items = tuple(items)
    for mask in range(1 << len(items)):
        yield {x for j, x in enumerate(items) if mask >> j & 1}


def cover(adj, right):
    matched = {}
    def augment(u, seen):
        for v in adj[u]:
            if v in seen:
                continue
            seen.add(v)
            if v not in matched or augment(matched[v], seen):
                matched[v] = u
                return True
        return False
    for u in adj:
        augment(u, set())
    inverse = {u: v for v, u in matched.items()}
    left_seen = set(adj) - inverse.keys()
    right_seen = set()
    queue = list(left_seen)
    while queue:
        u = queue.pop()
        for v in adj[u]:
            if inverse.get(u) == v or v in right_seen:
                continue
            right_seen.add(v)
            if v in matched and matched[v] not in left_seen:
                left_seen.add(matched[v])
                queue.append(matched[v])
    ans = (set(adj) - left_seen) | right_seen
    assert len(ans) == len(matched)
    assert all(u in ans or v in ans for u in adj for v in adj[u])
    return ans


def pruning():
    cases = 0
    pairs2 = tuple(product(range(2), repeat=2))
    instances = ((2, rel, r, c) for rel in subsets(pairs2)
                 for r in subsets(pairs2) for c in subsets(pairs2))
    random_cases = []
    for n in (3, 4, 5):
        pairs = tuple(product(range(n), repeat=2))
        for _ in range(100):
            random_cases.append((n, *({p for p in pairs if RNG.random() < .45} for j in range(3))))
    from itertools import chain
    for n, rel, r, c in chain(instances, random_cases):
        conflicts = [((p, j), (i, s)) for p, j in r for i, s in c
                     if (p, i) in rel and (s, j) in rel]
        z = {(i, j) for (p, j), (i, s) in conflicts}
        h = {(p, s) for (p, j), (i, s) in conflicts}
        left = [('r', x) for x in r] + [('zl', x) for x in z]
        right = [('c', x) for x in c] + [('zr', x) for x in z]
        adj = {u: set() for u in left}
        for rp, cp in conflicts:
            adj['r', rp].add(('c', cp))
        for i, j in z:
            for p, jj in r:
                if jj == j and (p, i) in rel:
                    adj['r', (p, j)].add(('zr', (i, j)))
            for ii, s in c:
                if ii == i and (s, j) in rel:
                    adj['zl', (i, j)].add(('c', (i, s)))
        k = cover(adj, right)
        assert len(k) <= len(z) + len(h)
        rp = {x for x in r if ('r', x) not in k}
        cp = {x for x in c if ('c', x) not in k}
        assert not any(a in rp and b in cp for a, b in conflicts)
        assert all(a in rp for a in r if not any(x == a for x, y in conflicts))
        assert all(b in cp for b in c if not any(y == b for x, y in conflicts))
        uncovered = sum(not any(jj == j and (p, i) in rel for p, jj in rp)
                        and not any(ii == i and (s, j) in rel for ii, s in cp)
                        for i, j in z)
        assert len(r) + len(c) - len(rp) - len(cp) <= len(h) + uncovered
        cases += 1
    RESULTS.append(dict(check='augmented matching-cover pruning', instances=cases,
                        exact=True, exhaustive='all relations and R,C subsets on two labels; seeded larger cases'))


def image(mask, out):
    result = 0
    while mask:
        bit = mask & -mask
        result |= out[bit.bit_length()-1]
        mask -= bit
    return result


def blowups():
    count = 0
    for n, m in ((1, 2), (2, 3), (3, 4)):
        base_pairs = tuple(combinations(range(n), 2))
        for choices in product(range(3), repeat=len(base_pairs)):
            arcs = set()
            for (u, v), choice in zip(base_pairs, choices):
                if choice:
                    arcs.add((u, v) if choice == 1 else (v, u))
            out = [sum(1 << v for x, v in arcs if x == u) for u in range(n)]
            lifted = []
            for u in range(n):
                for a in range(m):
                    lifted.append(sum(1 << (v*m+b) for v in range(n) for b in range(m)
                                      if (u, v) in arcs or (v == u and b > a)))
            for mask in range(1 << (n*m)):
                s = sum(1 << u for u in range(n) if mask >> (u*m) & ((1 << m)-1))
                fs, ffs = image(s, out), image(image(s, out), out)
                fu = image(mask, lifted)
                lhs = mask.bit_count() + image(fu, lifted).bit_count() - 2*fu.bit_count()
                rhs = m*((ffs & ~fs).bit_count() - (fs & ~s).bit_count()) + n
                assert lhs <= rhs
                count += 1
    RESULTS.append(dict(check='unconditional transitive-blowup accounting', subsets=count,
                        exact=True, hypothetical_deficit_graph_constructed=False))


def bipyramid(m):
    faces = [(m, i, (i+1) % m) for i in range(m)]
    faces += [(m+1, (i+1) % m, i) for i in range(m)]
    black = {i for i in range(2*m) if (i < m and i % 2 == 0) or (i >= m and i % 2 == 1)}
    left = {}
    for k, face in enumerate(faces):
        for u, v in zip(face, face[1:]+face[:1]):
            left[u, v] = k
    assert all(left[v, u] != k for (u, v), k in left.items())
    roots = set(faces[0])
    x = set(range(m+2))-roots
    a = sorted(black-{0})
    states = []
    def extend(j, chosen):
        if j == len(a):
            states.append(tuple(chosen))
            return
        for v in sorted(set(faces[a[j]]) & x - set(chosen)):
            extend(j+1, chosen+[v])
    extend(0, [])
    return faces, black, left, roots, x, a, states


def directed_cycles(out):
    found = set()
    for start in out:
        route, pos = [], {}
        v = start
        while v in out and v not in pos:
            pos[v] = len(route)
            route.append(v)
            v = out[v]
        if v in pos:
            cyc = route[pos[v]:]
            j = cyc.index(min(cyc))
            found.add(tuple(cyc[j:]+cyc[:j]))
    return found


def planar_states():
    cuts = state_count = selections = cycle_count = 0
    negative = False
    for m in (4, 6, 8):
        faces, black, left, roots, x, a, states = bipyramid(m)
        edges = {tuple(sorted(edge)) for edge in left}
        assert states and any(all(u != v for u, v in zip(r, s)) for r in states for s in states)
        for s in subsets(x):
            flow = sum(min(2, len(set(faces[t]) & s)) for t in a)
            u = set(range(m+2))-s
            density = sum(set(e) <= u for e in edges)-sum(set(faces[t]) <= u for t in black)
            assert flow >= 2*len(s)
            assert density <= 2*len(u)-4
            assert flow-2*len(s) == 2*len(u)-4-density
            cuts += 1
        for state in states:
            targets = [sorted(set(faces[t])-{v}) for t, v in zip(a, state)]
            for choices in product(*targets):
                out = dict(zip(state, choices))
                selections += 1
                for cyc in directed_cycles(out):
                    assert not roots.intersection(cyc)
                    boundary = {tuple(sorted(e)) for e in zip(cyc, cyc[1:]+cyc[:1])}
                    # Components of the dual after deleting boundary crossings.
                    outside = {0}
                    queue = [0]
                    while queue:
                        f = queue.pop()
                        face = faces[f]
                        for u, v in zip(face, face[1:]+face[:1]):
                            other = left[v, u]
                            if tuple(sorted((u, v))) not in boundary and other not in outside:
                                outside.add(other)
                                queue.append(other)
                    inside = set(range(len(faces)))-outside
                    interior = set().union(*(set(faces[t]) for t in inside))-set(cyc)
                    b, w = len(inside & black), len(inside-black)
                    ell = sum(left[u, v] in inside and left[u, v] in black
                              or left[v, u] in inside and left[v, u] in black for u, v in boundary)
                    h = len(cyc)
                    assert b+w == 2*len(interior)+h-2
                    assert 3*(b-w) == 2*ell-h
                    assert b == len(interior)+ell
                    delta = sum(1 if left[u, v] in black else -1 for u, v in zip(cyc, cyc[1:]+cyc[:1]))
                    assert abs(delta) == 3
                    inside_left = all(left[u, v] in inside for u, v in zip(cyc, cyc[1:]+cyc[:1]))
                    assert delta == (-3 if inside_left else 3)
                    cycle_count += 1
        state_count += len(states)
        # Equatorial cycle is not constrained by a selected state.
        arbitrary = sum(1 if left[i, (i+1) % m] in black else -1 for i in range(m))
        negative |= abs(arbitrary) != 3
    assert cycle_count > 0 and negative
    RESULTS.append(dict(check='two disjoint planar incidence states', bipyramids=[4, 6, 8],
                        subset_cuts=cuts, states=state_count, exact=True))
    RESULTS.append(dict(check='matched disk identities and directed-cycle signs', selections=selections,
                        cycles=cycle_count, arbitrary_cycle_negative_control=negative, exact=True))


def potential():
    eps = 1/32
    triples = trees = overlaps = 0
    def f(x, t):
        return 1+1/log2(t/2)-1/log2(max(x, t/2))
    for t in (4, 16, 64, 100):
        for _ in range(500):
            u = RNG.randint(max(t+1, 100), 10**8)
            u1 = RNG.randint(1, 3*u//4)
            extra = RNG.randint(0, int(eps*u1/log2(u)**2))
            u2 = u-u1+extra
            if u2 >= u:
                continue
            assert u1*f(u1, t)+u2*f(u2, t) <= u*f(u, t)+1e-7
            triples += 1
        for n in (3000, 30000, 100000):
            stack, leaves = [n], 0
            while stack:
                u = stack.pop()
                if u <= t:
                    leaves += u
                    continue
                u1 = RNG.randint(max(1, u//4), max(1, 3*u//4))
                extra = int(eps*u1/log2(u)**2)
                overlaps += extra
                stack.extend((u1, u-u1+extra))
            assert leaves <= n*f(n, t)+1e-7
            trees += 1
    assert overlaps > 0
    RESULTS.append(dict(check='overlap potential and full split trees', child_triples=triples,
                        trees=trees, total_duplicated_orders=overlaps, arithmetic='floating logarithms'))


def pairings(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    a = items[0]
    for j in range(1, len(items)):
        b = items[j]
        for tail in pairings(items[1:j]+items[j+1:]):
            yield ((a, b),)+tail


def folding():
    prob_cases = total = 0
    for m in (8, 9):
        pp = list(pairings(range(m+(m % 2))))
        p1 = Fraction(sum((0, 1) in p for p in pp), len(pp))
        p2 = Fraction(sum((0, 1) in p and (2, 3) in p for p in pp), len(pp))
        assert p1 == Fraction(1, m-1 if m % 2 == 0 else m)
        assert p2 == Fraction(1, (m-1)*(m-3) if m % 2 == 0 else m*(m-2))
        prob_cases += 1
    graphs = []
    for m in (8, 9):
        edges = {tuple(sorted((i, (i+1) % m))) for i in range(m)}
        graphs.append((m, [tuple(range(m))], edges, 2))
    # Two folding sets, cross-set collisions, and external shared neighbors.
    graphs.append((16, [tuple(range(8)), tuple(range(8, 16))],
                   {(i, 8+i) for i in range(8)} | {(i, 8+(i+1) % 8) for i in range(8)}, 2))
    graphs.append((12, [tuple(range(8))],
                   {(i, 8+i//2) for i in range(8)} | {(i, (i+1) % 8) for i in range(0, 8, 2)}, 2))
    for n, sets, edges, a in graphs:
        assert all(len(x) >= max(8, a*a) for x in sets)
        for x in sets:
            assert all(sum(v in e for e in edges) <= a for v in x)
            assert all(sum(v in e and bool((set(e)-{v}) & set(x)) for e in edges) <= a for v in range(n))
        options = []
        for x in sets:
            options.append(list(pairings(x+((-1,) if len(x) % 2 else ()))))
        zsum = count = 0
        min_error = len(edges)
        for choices in product(*options):
            pi = list(range(n))
            for pairs in choices:
                for u, v in pairs:
                    if u >= 0 and v >= 0:
                        pi[u] = pi[v] = min(u, v)
            bins = Counter(tuple(sorted((pi[u], pi[v]))) for u, v in edges)
            loops = sum(s for (u, v), s in bins.items() if u == v)
            z = loops+sum(s*(s-1)//2 for (u, v), s in bins.items() if u != v)
            deleted = loops+sum(s-1 for (u, v), s in bins.items() if u != v)
            assert deleted <= z
            assert len(set(pi)) == n-sum(len(x)//2 for x in sets)
            zsum += z
            count += 1
            min_error = min(min_error, deleted)
        assert Fraction(zsum, count) <= Fraction(332, 245)*len(sets)*a*a
        assert min_error <= 2*sum(map(len, sets))
        total += count
    # K_(m,a) violates only the external-neighbor bound for suitable m,a.
    m, a = 36, 6
    assert m >= max(8, a*a) and a*m//2 > 2*m
    RESULTS.append(dict(check='pairing probabilities and folding cleanup', parity_probability_models=prob_cases,
                        complete_pairing_models=total, graphs=len(graphs), external_neighbor_negative_control=True,
                        exact=True))


def matroids():
    checked = 0
    for n in (4, 6):
        full = (1 << n)-1
        partitions = [[(full, n//2)], [(3 << i, 1) for i in range(0, n, 2)]]
        shifted = [((1 << i) | (1 << ((i+1) % n)), 1) for i in range(1, n, 2)]
        partitions.append(shifted)
        ranks = [[sum(min((s & block).bit_count(), r) for block, r in partition)
                  for s in range(1 << n)] for partition in partitions]
        for rank in ranks:
            assert all(rank[s] == s.bit_count()+rank[full ^ s]-rank[full] for s in range(1 << n))
        for rank0, rank1 in product(ranks, repeat=2):
            for p in range(1 << n):
                c = full ^ p
                for labels in product(range(3), repeat=n):
                    s0 = s1 = i0 = i1 = 0
                    for v, label in enumerate(labels):
                        bit = 1 << v
                        if p & bit:
                            if label == 0: s0 |= bit
                            if label == 1: s1 |= bit
                        else:
                            if label != 1: i0 |= bit
                            if label != 0: i1 |= bit
                    if rank0[s0] != rank0[p] or rank1[s1] != rank1[p]:
                        continue
                    if rank0[i0 | p]-rank0[p] != i0.bit_count() or rank1[i1 | p]-rank1[p] != i1.bit_count():
                        continue
                    a0, a1 = s0 | (c ^ i0), s1 | (c ^ i1)
                    assert not a0 & a1
                    assert rank0[a0] == rank0[full] and rank1[a1] == rank1[full]
                    j0, j1 = full ^ a0, full ^ a1
                    assert rank0[j0] == j0.bit_count() and rank1[j1] == j1.bit_count()
                    assert j0 | j1 == full
                    checked += 1
    RESULTS.append(dict(check='self-dual mixed-witness conversion', successful_witnesses=checked,
                        ground_sizes=[4, 6], ordered_matroid_pairs=18, exact=True))


def descent():
    for edge in range(-8, 9):
        endpoints = (edge, edge+1)
        assert {n % 2 for n in endpoints} == {0, 1}
    for direction in (-1, 1):
        vertex = -1 if direction == -1 else 0
        received = -1
        for _ in range(10):
            inward = vertex if vertex <= -1 else vertex-1
            outward = vertex-1 if vertex <= -1 else vertex
            assert inward == received
            received = outward
            vertex += direction
    chains = 0
    universe = set(range(12))
    # This cardinality rank is only a finite model of the antitone inequality.
    for _ in range(500):
        order = list(universe)
        RNG.shuffle(order)
        a, b, c, d = sorted(RNG.sample(range(13), 4))
        x, u, y, nxt = (set(order[:j]) for j in (a, b, c, d))
        rho = lambda s: len(universe-s)
        assert x <= u and y <= nxt
        assert rho(x) >= rho(u) > rho(y) >= rho(nxt)
        chains += 1
    RESULTS.append(dict(check='double-ray orientation and rank propagation', finite_chains=chains,
                        exact=True, constructs_infinite_matroid=False, constructs_ultrafilter=False,
                        scope='finite bookkeeping only; no finite approximation certifies the ordinal obstruction'))


def main():
    for test in (pruning, blowups, planar_states, potential, folding, matroids, descent):
        test()
        print(test.__name__, 'passed', flush=True)
    out = dict(batch='B012', status='passed', python=sys.version.split()[0], seed=2026101612,
               scope='Selected finite identities and examples; no global theorem, priority or Lean certification.',
               checks=RESULTS)
    Path(__file__).with_name('results.json').write_text(json.dumps(out, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
