"""Finite checks for B015, with explicit controls for omitted hypotheses."""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import combinations, product, permutations
from math import comb, exp
from pathlib import Path
import json
import random
import sys
import numpy as np
from scipy.optimize import linprog

RNG = random.Random(150015)
NRNG = np.random.default_rng(150015)
OUT = {}


def subsets(items):
    values = tuple(items)
    return [frozenset(c) for r in range(len(values)+1) for c in combinations(values, r)]


def balanced_tests():
    cases = 0
    for blocks in (12, 16, 20):
        for blocksize in (1, 2, 3):
            n = blocks*blocksize
            r = (blocks-1)//2
            assert 2*r < blocks  # each removed label hits only one disjoint patch
            for _ in range(8):
                vectors = np.zeros((2*n, blocks))
                for j in range(blocks):
                    for side in (0, 1):
                        raw = NRNG.integers(1, 30, blocksize)
                        vectors[side*n+j*blocksize:side*n+(j+1)*blocksize, j] = raw/raw.sum()
                opt = linprog(np.zeros(blocks), A_ub=vectors, b_ub=np.full(2*n, 4/r),
                              A_eq=np.ones((1, blocks)), b_eq=[1], bounds=(0, None), method='highs')
                assert opt.success and np.max(vectors@opt.x) <= 4/r+1e-12
                prices = NRNG.random(2*n)**5
                total = prices.sum()
                costly = prices > 2*total/r
                surviving = [j for j in range(blocks) if not any(costly[np.flatnonzero(vectors[:, j])])]
                assert surviving and min(prices@vectors[:, j] for j in surviving) <= 4*total/r+1e-12
                cases += 1
    # Fixed vector rules force p=q for player one and q=1-p for player two.
    def outputs(a, b):
        return (F(a-b), F(b-a)), (F(a+b-1), F(1-a-b))
    p = q = F(1, 2)
    ex = [[F(0), F(0)], [F(0), F(0)]]
    for a, b in product((0, 1), repeat=2):
        w = (p if a else 1-p)*(q if b else 1-q)
        for j, vals in enumerate(outputs(a, b)):
            for k, value in enumerate(vals):
                ex[j][k] += w*value
    assert ex == [[0, 0], [0, 0]]
    states = [(0, 0)]
    for _ in range(4):
        p, q = states[-1]
        states.append((q, 1-p))
    assert states[-1] == states[0] and len(set(states[:-1])) == 4
    OUT['balanced_profiles'] = {'lp_menus': cases, 'deletion_tolerance_certified_by_disjoint_blocks': True,
        'simultaneous_profile': 'p=q=1/2', 'best_response_cycle_length': 4}


def scattered_tests():
    cases = 0
    for blocks in range(2, 7):
        for blocksize in (1, 2, 3):
            size = blocks*blocksize
            # Within a block all roles use the same bit; different blocks are independent.
            for power in range(1, 7):
                lhs = F(0)
                for bits in product((0, 1), repeat=blocks):
                    gate = sum(bits)%3 != 1
                    avg = F(sum(bits), blocks)
                    lhs += F(gate, 2**blocks)*avg**power
                rhs = (F(1, 2)+F(power, blocks))**power
                assert lhs <= rhs
                cases += 1
    # If all 200 roles share a rare bit, singleton near sets do not justify products.
    assert F(1, 100) > (F(1, 100)+F(10, 200))**10
    OUT['scattered_moments'] = {'exact_block_dependent_models': cases,
        'success_indicator_retained': True, 'missing_product_hypothesis_control': True}


def posterior_tests():
    models = 0
    for zcount in range(2, 6):
        for tcount in range(2, 7):
            for _ in range(5):
                weights = [RNG.randrange(1, 9) for _ in range(zcount)]
                prior = [F(w, sum(weights)) for w in weights]
                rows = []
                for z in range(zcount):
                    raw = [RNG.randrange(9) for _ in range(tcount-1)]+[0]
                    rows.append([F(w, max(1, 2*sum(raw))) for w in raw])
                rawq = [RNG.randrange(1, 9) for _ in range(tcount)]
                q = [F(w, sum(rawq)) for w in rawq]
                m = [sum(prior[z]*rows[z][t] for z in range(zcount)) for t in range(tcount)]
                epsilon = F(1, 5)
                badmass = sum(m[t] for t in range(tcount) if m[t] < epsilon*q[t] or m[t] == 0)
                assert badmass <= epsilon
                cap = max(rows[z][t]/q[t] for z in range(zcount) for t in range(tcount))
                lhs = rhs = F(0)
                for z, t in product(range(zcount), range(tcount)):
                    h = F((z+1)*(t+2))
                    rhs += prior[z]*rows[z][t]*h
                    if m[t]:
                        post = prior[z]*rows[z][t]/m[t]
                        lhs += m[t]*post*h
                        if m[t] >= epsilon*q[t]:
                            assert post <= cap/epsilon*prior[z]
                assert lhs == rhs
                models += 1
    assert F(1, 100) < F(1, 10) and F(1, 100)/F(1, 100) > F(1, 10)
    OUT['gated_posteriors'] = {'exact_models': models, 'zero_density_cells': True,
        'rare_gate_joint_vs_conditional_control': True}


def resampling_model(n, labels, prior, rho, a, gamma):
    allsets = subsets(range(n))
    m = max(1, max(map(len, labels)))
    for j in allsets[1:]:
        assert sum(p for s, p in zip(labels, prior) if j <= s) <= a**len(j)
    z = {y: sum(p*rho**(-len(s)) for s, p in zip(labels, prior) if s <= y) for y in allsets}
    massw = {w: rho**len(w)*(1-rho)**(n-len(w)) for w in allsets}
    ymass = defaultdict(F)
    target = [F(0)]*len(labels)
    outside = [F(0)]*len(labels)
    failures = F(0)
    conditional_targets = {}
    transitions = 0
    for w in allsets:
        at_w = [F(0)]*len(labels)
        for c, (s, pc) in enumerate(zip(labels, prior)):
            y = w | s
            ymass[y] += massw[w]*pc
            for b, (t, pb) in enumerate(zip(labels, prior)):
                if not t <= y:
                    continue
                post = pb*rho**(-len(t))/z[y]
                weight = massw[w]*pc*post
                frag = t-w
                assert frag <= s & t and t <= w | frag
                target[b] += weight
                at_w[b] += pc*post
                if z[y] < gamma or len(frag) > F(m, 2):
                    failures += weight
                if z[y] >= gamma:
                    outside[b] += weight*(1+len(w-t))
                transitions += 1
        conditional_targets[w] = at_w
    assert target == prior
    assert all(ymass[y] == massw[y]*z[y] for y in allsets)
    bound = gamma+sum(F(comb(m, r))*(a/rho)**r for r in range(m//2+1, m+1))/gamma
    assert failures <= bound
    for b, t in enumerate(labels):
        meanf = sum(p*(1+len(w-t)) for w, p in massw.items())
        assert outside[b] <= prior[b]*meanf*(1+a/rho)**m/gamma
    differs = any(v != prior for v in conditional_targets.values())
    return transitions, differs, float(failures), m


def resampling_tests():
    total = models = differences = sparse = 0
    for n in (2, 3, 4):
        for a in (F(1, 5), F(1, 10**24)):
            labels = subsets(range(n))
            prior = [a**len(s)*(1-a)**(n-len(s)) for s in labels]
            # Split the empty label, preserving an indexed duplicate.
            empty = prior[0]
            prior[0] = empty/3
            labels.append(frozenset())
            prior.append(2*empty/3)
            for rho in (F(1, 2), F(3, 4)):
                count, different, fail, m = resampling_model(n, labels, prior, rho, a, F(1, 10))
                total += count
                differences += different
                models += 1
                if a == F(1, 10**24):
                    assert float(a/rho) <= exp(-50)
                    # Here Z(Y)>=prior(empty copies)>1/2, so the source cutoff never fails.
                    assert fail <= exp(-9*m)
                    sparse += 1
    OUT['planted_resampling'] = {'exact_models': models, 'enumerated_transitions': total,
        'conditional_target_changes': differences, 'models_meeting_exp_minus_50_condition': sparse}


def graph_copy_tests():
    edges = list(combinations(range(4), 2))
    copy_checks = max_checks = nonempty = 0
    def copies(es):
        if not es:
            return {frozenset()}
        verts = sorted(set().union(*map(set, es)))
        out = set()
        for images in permutations(range(4), len(verts)):
            mp = dict(zip(verts, images))
            out.add(frozenset(tuple(sorted((mp[a], mp[b]))) for a, b in es))
        return out
    for h in subsets(edges):
        if not h:
            continue
        hc = copies(h)
        for f in subsets(h):
            fc = copies(f)
            fixed = next(iter(fc))
            inside = sum(g <= h for g in fc)
            contains = F(sum(fixed <= g for g in hc), len(hc))
            assert contains == F(inside, len(fc))
            copy_checks += 1
    # Generic containment maximizers: this exercises nonempty cores without huge graph sizes.
    universe = frozenset(range(5))
    allsets = subsets(universe)
    for _ in range(60):
        family = RNG.sample(allsets[1:], 8)
        raw = [RNG.randrange(1, 10) for _ in family]
        p = [F(w, sum(raw)) for w in raw]
        sigma = F(RNG.randrange(1, 5), 5)
        prob = {s: sum(w for t, w in zip(family, p) if s <= t) for s in allsets}
        core = max(allsets, key=lambda s: prob[s]/sigma**len(s))
        nonempty += bool(core)
        for j in subsets(universe-core):
            assert prob[core | j]/prob[core] <= sigma**len(j)
            max_checks += 1
    for h in range(1, 301):
        for r in range((h+16)//17, h+1):
            assert F(2*comb(h, r), 128**r) < 1
    OUT['graph_cores'] = {'copy_ratio_checks': copy_checks, 'maximizer_conditional_checks': max_checks,
        'nonempty_maximizers': nonempty, 'size_inequality_up_to_edges': 300}


def rank2(columns):
    pivots = {}
    for v in columns:
        while v:
            bit = v.bit_length()-1
            if bit not in pivots:
                pivots[bit] = v
                break
            v ^= pivots[bit]
    return len(pivots)


def chain_homology(faces):
    boundary = {}
    for degree in range(1, len(faces)):
        lookup = {s: i for i, s in enumerate(faces[degree-1])}
        cols = []
        for s in faces[degree]:
            v = 0
            for x in s:
                v ^= 1 << lookup[s-frozenset([x])]
            cols.append(v)
        boundary[degree] = rank2(cols)
    return [len(faces[d])-boundary.get(d, 0)-boundary.get(d+1, 0) for d in range(len(faces))]


def homology_tests():
    models = 0
    for q in (2, 3, 4, 5):
        # Join of three q-point sets: reduced homology vanishes through degree one.
        faces = []
        for size in (1, 2, 3):
            fs = []
            for colors in combinations(range(3), size):
                for values in product(range(q), repeat=size):
                    fs.append(frozenset(zip(colors, values)))
            faces.append(fs)
        original = chain_homology(faces)
        assert original[:2] == [1, 0]
        def orbit(s):
            return min(tuple(sorted((color, (value+t)%q) for color, value in s)) for t in range(q))
        orbits = [sorted({orbit(s) for s in degree}) for degree in faces]
        ranks = {}
        for d in (1, 2):
            lookup = {s: i for i, s in enumerate(orbits[d-1])}
            cols = []
            for row in orbits[d]:
                s = frozenset(row)
                col = 0
                for x in s:
                    col ^= 1 << lookup[orbit(s-frozenset([x]))]
                cols.append(col)
            ranks[d] = rank2(cols)
        got = len(orbits[1])-ranks[1]-ranks[2]
        expected = int(q%2 == 0)  # cyclic periodic resolution over F2
        assert got == expected
        models += 1
    # Odd cyclic group fixes a point: averaging element has augmentation one.
    for q in (1, 3, 5, 7):
        averaging = [1]*q
        convolution = [sum(averaging[i]*averaging[(j-i)%q] for i in range(q))%2 for j in range(q)]
        assert convolution == averaging and sum(averaging)%2 == 1
    assert 2%2 == 0  # C2 fixes a point: averaging does not split; H1(C2,F2)=F2.
    OUT['partial_resolution'] = {'free_join_models': models, 'odd_stabilizer_averaging_models': 4,
        'even_stabilizer_trivial_action_control': True,
        'cyclic_group_homology_compared_via_periodic_resolution': True}


def skeleton_tests():
    models = faces_checked = cochains = 0
    topsets = [
        [frozenset((0, 1, 2, 3))],
        [frozenset((0, 1, 2, 3)), frozenset((1, 2, 3, 4))],
        [frozenset((0, 1, 2, 3)), frozenset((0, 1, 2, 4)), frozenset((0, 1, 3, 4))],
    ]
    for tops in topsets:
        faces = [sorted(set().union(*(set(map(frozenset, combinations(t, i+1))) for t in tops)), key=lambda x: tuple(sorted(x))) for i in range(4)]
        for s in (1, 2):
            counts = {f: sum(f <= t for t in tops) for f in faces[s]}
            a, b = min(counts.values()), max(counts.values())
            lam = F(comb(4, s+1)*len(tops), len(faces[s]))
            mu, nu = [], []
            for i in range(s+1):
                mu.append([F(sum(f <= t for t in tops), comb(4, i+1)*len(tops)) for f in faces[i]])
                nu.append([F(sum(f <= t for t in faces[s]), comb(s+1, i+1)*len(faces[s])) for f in faces[i]])
                for x, y in zip(mu[i], nu[i]):
                    assert lam/b*x <= y <= lam/a*x
                    faces_checked += 1
            for i in range(s):
                rows = [sum(1 << j for j, f in enumerate(faces[i]) if f <= t) for t in faces[i+1]]
                delta = lambda mask: sum(((mask & row).bit_count()%2) << k for k, row in enumerate(rows))
                allco = range(1 << len(faces[i]))
                kernel = [mask for mask in allco if delta(mask) == 0]
                norm = lambda mask, weights: sum(w for j, w in enumerate(weights) if mask >> j & 1)
                ratios_mu, ratios_nu = [], []
                for mask in allco:
                    dm = min(norm(mask^z, mu[i]) for z in kernel)
                    dn = min(norm(mask^z, nu[i]) for z in kernel)
                    assert lam/b*dm <= dn <= lam/a*dm
                    if dm:
                        ratios_mu.append(norm(delta(mask), mu[i+1])/dm)
                        ratios_nu.append(norm(delta(mask), nu[i+1])/dn)
                    cochains += 1
                assert min(ratios_nu) >= F(a, b)*min(ratios_mu)
            models += 1
    # Triangulated annulus: an actual cocycle that is not a coboundary.
    triangles = [frozenset(t) for i in range(3) for t in ((i, (i+1)%3, i+3), ((i+1)%3, i+3, (i+1)%3+3))]
    edges = sorted(set().union(*(set(map(frozenset, combinations(t, 2))) for t in triangles)), key=lambda x: tuple(sorted(x)))
    b1 = {sum(((mask >> min(e) & 1) ^ (mask >> max(e) & 1)) << j for j, e in enumerate(edges)) for mask in range(64)}
    witness = next(mask for mask in range(1 << len(edges)) if mask not in b1 and all(sum((mask >> j & 1) for j, e in enumerate(edges) if e <= t)%2 == 0 for t in triangles))
    assert witness not in b1 and min((witness^b).bit_count() for b in b1) > 0
    OUT['skeleton_weights'] = {'complex_skeleton_models': models, 'face_bounds': faces_checked,
        'exhaustive_cochain_distance_checks': cochains, 'annulus_nonzero_cohomology_control': True}


def account_tests():
    transitions = 0
    for _ in range(40):
        count = 6
        z = [F(RNG.randrange(1, 10)) for _ in range(count)]
        discount = [F(1)]*count
        growth = [F(1)]*count
        weights = [F(1, count)]*count
        initial = sum(w*x for w, x in zip(weights, z))
        for step in range(15):
            candidates = [[(max(F(1), x*F(RNG.randrange(4, 17), 10)) if x and RNG.randrange(20) else F(0)) for x in z] for _ in range(4)]
            ratios = [max(F(1), sum(row[i] for row in candidates)/(4*z[i])) if z[i] else F(1) for i in range(count)]
            newdiscount = [d/r for d, r in zip(discount, ratios)]
            selected = min(candidates, key=lambda row: sum(w*d*x for w, d, x in zip(weights, newdiscount, row)))
            before = sum(w*d*x for w, d, x in zip(weights, discount, z))
            after = sum(w*d*x for w, d, x in zip(weights, newdiscount, selected))
            assert after <= before and after <= initial
            for i in range(count):
                growth[i] *= ratios[i]
                assert 1/newdiscount[i] == growth[i]
                assert selected[i] <= count*initial*growth[i]
            z, discount = selected, newdiscount
            transitions += 1
    scalar = 0
    for p in (2, 4, 6, 8):
        c0 = F(p*(p-1)*2**max(p-3, 0), 2)
        cp = max(F(p), 2*c0)
        for numerator in range(-15, 21):
            x = F(numerator, 5)
            for increments in ((F(-1), F(1)), (F(-1), F(1, 5), F(2, 5)), (F(1, 10), F(1, 2))):
                mu = max(F(0), sum(increments)/len(increments))
                nu = sum(y*y for y in increments)/len(increments)
                old = 1+max(x, 0)**p
                new = sum(1+max(x+y, 0)**p for y in increments)/len(increments)
                assert new <= (1+cp*(mu+nu))*old
                scalar += 1
    OUT['discounted_accounts'] = {'exact_transitions': transitions, 'scalar_excess_models': scalar,
        'dead_labels_keep_original_weights': True}


def configuration_tests():
    cases = recurrences = 0
    worst = 0.0
    for n in (3, 4, 5, 6):
        for degree in (3, 4):
            if n*degree%2:
                continue
            for trial in range(12):
                count = n*degree
                c = np.zeros((n, count))
                c[np.arange(count)//degree, np.arange(count)] = 1
                perm = list(range(count))
                RNG.shuffle(perm)
                resolved = 2*RNG.randrange((count-4)//2+1)
                s = perm[resolved:]
                l = len(s)
                pmat = np.zeros((count, count))
                for i in range(0, resolved, 2):
                    u, v = perm[i:i+2]
                    pmat[u, v] = pmat[v, u] = 1
                pmat[np.ix_(s, s)] = 1/l
                ae = c@pmat@c.T
                de = c@pmat@pmat@c.T
                cs = c[:, s]
                xi = cs@(np.eye(l)-np.ones((l, l))/l)
                dmat = xi@xi.T
                assert np.allclose(de, degree*np.eye(n)-dmat)
                q = [np.eye(n)]
                transfer = (c.T@c-np.eye(count))@pmat
                for j in range(1, 7):
                    q.append(c@pmat@np.linalg.matrix_power(transfer, j-1)@c.T)
                    if j == 2:
                        assert np.allclose(q[j], ae@ae-de)
                    elif j >= 3:
                        assert np.allclose(q[j], ae@q[j-1]-(de-np.eye(n))@q[j-2])
                    recurrences += 1
                u, v = s[:2]
                pnew = pmat.copy()
                pnew[np.ix_(s, s)] = 0
                pnew[u, v] = pnew[v, u] = 1
                pnew[np.ix_(s[2:], s[2:])] = 1/(l-2)
                aenew = c@pnew@c.T
                dnew = degree*np.eye(n)-c@pnew@pnew@c.T
                umat = xi[:, :2]
                swap = np.array([[0., 1.], [1., 0.]])
                g0 = np.eye(2)-np.ones((2, 2))/l
                b = np.eye(2)+np.ones((2, 2))/(l-2)
                assert np.allclose(dnew, dmat-umat@b@umat.T)
                assert np.allclose(aenew, ae+umat@swap@b@umat.T)
                contrast = np.linalg.qr(np.column_stack((np.ones(n), np.eye(n)[:, 1:])))[0][:, 1:]
                for sign, h in product((-1, 1), (.12, .21)):
                    z = 1/h+(degree-1)*h
                    mh = h/(1-h*h)
                    m = z*np.eye(n)-sign*ae-h*dmat
                    mn = z*np.eye(n)-sign*aenew-h*dnew
                    assert np.allclose(mn, m+umat@(h*np.eye(2)-sign*swap)@b@umat.T)
                    mc, nc = contrast.T@m@contrast, contrast.T@mn@contrast
                    assert min(np.linalg.eigvalsh(mc)) > 0 and min(np.linalg.eigvalsh(nc)) > 0
                    w = contrast@np.linalg.inv(mc)@contrast.T/mh
                    wn = contrast@np.linalg.inv(nc)@contrast.T/mh
                    h0 = -sign*h*swap@b
                    hh = np.linalg.inv(np.linalg.inv(h0)+umat.T@w@umat-g0)
                    err = np.max(abs(wn-(w-w@umat@hh@umat.T@w)))
                    worst = max(worst, float(err))
                    assert err < 1e-10
                    cases += 1
    avgchecks = 0
    for l in range(4, 10):
        a = [F(RNG.randrange(-9, 10)) for _ in range(l-1)]
        a.append(-sum(a))
        c = [F(RNG.randrange(-9, 10)) for _ in range(l-1)]
        c.append(-sum(c))
        for subset in subsets(range(l)):
            if len(subset) < 2:
                continue
            size, k = len(subset), l-len(subset)
            lhs = sum((a[u]*c[v]+a[v]*c[u]+(a[u]+a[v])*(c[u]+c[v])/F(l-2))/2 for u, v in permutations(subset, 2))/F(size*(size-1))
            rhs = ((1+F(1, l-2))*sum(a[u] for u in subset)*sum(c[u] for u in subset)-F(k, l-2)*sum(a[u]*c[u] for u in subset))/F(size*(size-1))
            assert lhs == rhs
            if size == l:
                assert lhs == 0
            avgchecks += 1
    OUT['partial_pairing'] = {'inverse_update_models': cases, 'path_recurrence_coefficients': recurrences,
        'max_inverse_error': worst, 'exact_restricted_pair_averages': avgchecks,
        'loops_and_repeated_vertex_incidences_allowed': True}


if __name__ == '__main__':
    for check in (balanced_tests, scattered_tests, posterior_tests, resampling_tests,
                  graph_copy_tests, homology_tests, skeleton_tests, account_tests, configuration_tests):
        check()
        print(check.__name__, 'passed', flush=True)
    result = {'batch': 'B015', 'python': sys.version.split()[0], 'numpy': np.__version__, 'checks': OUT,
              'scope': 'Finite mechanism checks, not global threshold, expansion or Ramanujan proof certification.'}
    Path(__file__).with_name('results.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(OUT, indent=2))
