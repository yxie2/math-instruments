"""Finite models for B014. These checks do not certify the headline theorems."""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import product, combinations
from math import ceil, floor, log, log2, exp
from pathlib import Path
import json
import random
import sys
import numpy as np
from scipy.optimize import linprog

RNG = random.Random(140014)
NRNG = np.random.default_rng(140014)
OUT = {}


def entropy(probs, base=2):
    return -sum(float(p)*log(float(p), base) for p in probs if p > 0)


def frequency_tests():
    tests = 0
    for n in range(1, 5):
        for degree in (1, 2, 3):
            for radius in (0, 2, 7):
                freqs = []
                for j in range(n):
                    freqs.append(radius+degree*sum(freqs)+1+j)
                for nu in product(range(-degree, degree+1), repeat=n):
                    v = sum(a*b for a, b in zip(nu, freqs))
                    for coeff_freq in range(-radius, radius+1):
                        assert (v+coeff_freq == 0) == (not any(nu) and coeff_freq == 0)
                        tests += 1
                assert -freqs[0]+freqs[0] == 0  # adaptive w1 e(-L1 z)
    OUT['phase_tests'] = {'exact_monomial_integrals': tests, 'adaptive_test_discrepancy': 1}


def spectral_tests():
    worst = 0.0
    for trial in range(120):
        n = 5+trial%17
        g = NRNG.normal(size=(n, 2))+1j*NRNG.normal(size=(n, 2))
        g[0] = 0
        g[1] *= 1e-12
        v = NRNG.normal(size=(n, 2))+1j*NRNG.normal(size=(n, 2))
        v /= np.linalg.norm(v, axis=1)[:, None]
        p = np.sum(abs(g)**2, axis=1)
        out = v.copy()
        nz = p > 0
        out[nz] = g[nz]/np.sqrt(p[nz, None])
        assert np.max(abs(np.sum(abs(out)**2, axis=1)-1)) < 2e-15
        lhs = np.mean(np.sum(abs(out-g)**2, axis=1))
        rhs = np.mean((np.sqrt(p)-1)**2)
        worst = max(worst, abs(lhs-rhs))
        assert abs(lhs-rhs) < 1e-13
        other = np.stack((-np.conj(out[:, 1]), np.conj(out[:, 0])), axis=1)
        assert np.max(abs(np.sum(np.conj(other)*out, axis=1))) < 1e-14
        # Every U^j out is fiberwise collinear with out: other proves noncyclicity.
        z = np.exp(2j*np.pi*np.arange(n)/n)
        for j in range(n):
            assert abs(np.mean(np.sum(np.conj(other)*out*z[:, None]**j, axis=1))) < 1e-13
        f = NRNG.normal(size=g.shape)+1j*NRNG.normal(size=g.shape)
        pf = np.sum(abs(f)**2, axis=1)
        norm = lambda a: np.sqrt(np.mean(np.sum(abs(a)**2, axis=1)))
        assert np.mean(abs(p-pf)) <= (norm(g)+norm(f))*norm(g-f)+1e-12
    OUT['spectral_whitening'] = {'models': 120, 'max_distance_error': worst,
        'zero_and_tiny_densities': True, 'multiplicity_two_noncyclic_control': True}


def cancellation_tests():
    cases = 0
    for n in range(2, 11):
        signs = np.array(list(product((-1, 1), repeat=n)), dtype=float)
        phases = np.exp(2j*np.pi*np.arange(n)/7)
        chi = signs*phases
        for code_size in (2, 3, 5):
            code = np.array([[RNG.choice((-1, 1)) for _ in range(n)] for _ in range(code_size)])
            selected = np.argmax(signs@code.T, axis=1)
            words = code[selected]*phases
            counts = Counter(map(tuple, code[selected]))
            hn = entropy([v/len(signs) for v in counts.values()], exp(1))
            corr = np.mean(abs(np.mean(words*np.conj(chi), axis=0)))
            assert hn <= log(code_size)+1e-12
            for theta in (0.1, 0.3, 0.8):
                w = np.array([complex(RNG.uniform(-0.6, 0.6), RNG.uniform(-0.6, 0.6)) for _ in range(n)])
                lhs = np.mean(np.exp(theta*np.real(chi@w)))
                assert lhs <= exp(2*theta**2*n)+1e-10
            a = (hn/n)**0.5+n**-0.5
            unlikely = sum(v/len(signs) for v in counts.values() if v/len(signs) < exp(-a*n))
            assert unlikely <= hn/(a*n)+1e-12
            eps = 0.4
            assert corr <= eps+hn/(a*n)+exp(a*n-eps**2*n/8)+1e-12
            cases += 1
        assert np.allclose(np.mean(chi*np.conj(chi), axis=0), 1)
        assert abs(entropy([1/len(signs)]*len(signs), exp(1))-n*log(2)) < 1e-12
        repeated = np.repeat(signs[:, :1], n, axis=1)
        assert np.mean(repeated**2) == 1 and len(set(map(tuple, repeated))) == 2
    OUT['dependent_entropy_cancellation'] = {'dependent_codebook_models': cases,
        'finite_bound_can_be_loose': True, 'linear_entropy_and_repeated_character_controls': True}


def fixed_square_tests():
    cases = 0
    maxerr = 0.0
    for q in (2, 3, 5):
        dim = 3
        gauges = [np.linalg.qr(NRNG.normal(size=(dim, dim))+1j*NRNG.normal(size=(dim, dim)))[0] for _ in range(4)]
        r1, r2, r3, r4 = gauges
        p = np.diag([1, 0.1, 1e-6])
        s = [np.diag(np.exp(2j*np.pi*t*np.arange(dim)/q)) for t in range(q)]
        ff = [r1@u@p@r2.conj().T for u in s]
        gg = [r3@u@p@r4.conj().T for u in s]
        kk = [r1@u@p@r3.conj().T for u in s]
        nn = [r2@u@p@r4.conj().T for u in s]
        triples = [Counter() for _ in range(4)]
        polar = lambda a: (lambda u, sv, vh: u@vh)(*np.linalg.svd(a))
        for family in (ff, gg, kk, nn):
            for a in family:
                assert np.allclose(a.conj().T@a, family[0].conj().T@family[0], atol=1e-12)
                assert np.allclose(a@a.conj().T, family[0]@family[0].conj().T, atol=1e-12)
        for x, y, c in product(range(q), repeat=3):
            d = (c+y-x)%q
            row = (x, y, c, d)
            for j in range(4):
                triples[j][row[:j]+row[j+1:]] += 1
            f, g, k, n = ff[x], gg[y], kk[c], nn[d]
            assert np.allclose(f@n, k@g, atol=1e-12)
            assert np.allclose(f.conj().T@k, n@g.conj().T, atol=1e-12)
            err = np.max(abs(polar(f)@polar(n)-polar(k)@polar(g)))
            maxerr = max(maxerr, float(err))
            assert err < 1e-8
            cases += 1
        assert all(len(t) == q**3 and set(t.values()) == {1} for t in triples)
    a, b = np.diag([1, .2]), np.diag([.7, .4])
    assert not np.allclose(a@a, b@b)  # all four parameters equal: identities but no fixed squares
    assert np.linalg.matrix_rank(np.diag([1, 0])) == 1  # missing active span
    OUT['fixed_squares'] = {'three_wise_independent_rectangles': cases,
        'max_polar_error': maxerr, 'missing_independence_and_span_controls': True}


def law(items):
    ans = defaultdict(F)
    for x, p in items:
        ans[F(x)] += F(p)
    return dict(ans)


def convolve(a, b):
    return law((x+y, p*q) for x, p in a.items() for y, q in b.items())


def mix(a, b, t):
    return law(list((x, t*p) for x, p in a.items())+list((x, (1-t)*p) for x, p in b.items()))


def grid_entropy(a, scale, shift=F(0)):
    bins = defaultdict(F)
    for x, p in a.items():
        bins[floor(x/scale+shift)] += p
    return entropy(bins.values())


def hbar(a, scale):
    cuts = sorted({F(0), F(1)} | {(-x/scale)%1 for x in a})
    return sum(float(v-u)*grid_entropy(a, scale, (u+v)/2) for u, v in zip(cuts, cuts[1:]))


def smoothing_entropy(a, scale):
    cuts = sorted({x for x in a} | {x+scale for x in a})
    value = 0.0
    for u, v in zip(cuts, cuts[1:]):
        mid = (u+v)/2
        density = sum(p/scale for x, p in a.items() if x <= mid < x+scale)
        if density:
            value -= float((v-u)*density)*log2(float(density))
    return value-log2(float(scale))


def band(x):
    ell = 0
    while x < F(2)**(-ell):
        ell += 1
    while x >= F(2)**(1-ell):
        ell -= 1
    return ell


def pair_tests():
    models = 0
    for trial in range(36):
        support = sorted({F(RNG.randrange(-12, 13), 8) for _ in range(6)})
        if trial%3 == 0:
            support.append(support[0]+F(1, 2**40))
            support.sort()
        weights = [RNG.randrange(1, 10) for _ in support]
        a = dict(zip(support, [F(w, sum(weights)) for w in weights]))
        edges = defaultdict(list)
        for i, j in combinations(range(len(support)), 2):
            edges[band(support[j]-support[i])].append((i, j))
        caps = {}
        for ell, es in edges.items():
            mat = np.zeros((len(support), len(es)))
            for j, (u, v) in enumerate(es):
                mat[u, j] = mat[v, j] = .5
            opt = linprog(-np.ones(len(es)), A_ub=mat, b_ub=list(map(float, a.values())), bounds=(0, None), method='highs')
            assert opt.success and np.max(mat@opt.x-np.array(list(map(float, a.values())))) < 1e-8
            caps[ell] = -opt.fun
            assert -1e-9 <= caps[ell] <= 1+1e-9
        for k in (1, 2, 3):
            sums = {F(0)}
            for _ in range(k):
                sums = {x+y for x in sums for y in support}
            for rho in (F(1, 16), F(1), F(4)):
                lhs = k*(entropy(a.values())-grid_entropy(a, rho))
                rhs = log2(len(sums))+60000*k**4*sum(c for ell, c in caps.items() if F(2)**(-ell) <= 2*rho)
                assert lhs <= rhs+1e-8
                models += 1
    local = 0
    for k in (1, 2, 3, 4):
        for prob in (F(1, 2), F(1, 10), F(1, 1000), F(1, 10**20)):
            # Identical two-atom coordinates, one internal cut at 1/2.
            mean = prob
            if mean == F(1, 2):
                cut = F(1, 3)
            else:
                cut = F(1, 2)
            distance = abs(mean-cut)
            joint, ys = defaultdict(F), defaultdict(F)
            q = pb = F(0)
            pi = sum(p for x, p in ((F(0), 1-prob), (F(1), prob)) if abs(x-mean) >= distance/(4*k))
            for bits in product((0, 1), repeat=k):
                weight = prob**sum(bits)*(1-prob)**(k-sum(bits))
                y = sum(bits)
                labels = tuple(int(F(x) >= cut) for x in bits)
                exc = sum(abs(F(x)-mean) >= distance/(4*k) for x in bits)
                q += weight*(exc >= 2)
                pb += weight*(abs(F(y)-k*mean) >= distance/2)
                joint[(y, labels)] += weight
                ys[y] += weight
            t = k*pi
            assert q <= t*t and q <= t and pb <= t
            conditional = entropy(joint.values())-entropy(ys.values())
            assert conditional <= entropy([q, 1-q])+3*k*float(q+pb)+1e-12
            assert conditional <= 9*k*float(t)+1e-12
            local += 1
    rare = 1e-20
    assert entropy([rare, 1-rare]) > 9*rare
    OUT['pair_capacity'] = {'finite_law_inequalities': models, 'observed_sum_models': local,
        'spacing_as_small_as': '2^-40', 'unobserved_sum_rare_event_control': True,
        'lp_and_logarithms_use_floating_point': True}


def entropy_gain_tests():
    cases = 0
    worst = 0.0
    for _ in range(100):
        raw = [RNG.randrange(1, 8) for _ in range(4)]
        a = law((F(RNG.randrange(-15, 16), 7), F(w, sum(raw))) for w in raw)
        v = F(RNG.randrange(3, 13), 5)
        s = v*F(RNG.randrange(1, 7), 8)
        t = v*F(RNG.randrange(9, 30), 8)
        y = convolve(a, {F(0): F(1, 2), v: F(1, 2)})
        delta = 1-hbar(a, v)+hbar(a, 2*v)
        err = abs(hbar(y, v)-hbar(a, v)-delta)
        worst = max(worst, err)
        assert err < 1e-12
        assert abs(hbar(a, s)-smoothing_entropy(a, s)) < 1e-11
        gain = hbar(y, s)-hbar(y, t)-hbar(a, s)+hbar(a, t)
        assert gain >= delta-float(s/v+v/t)-1e-11
        cases += 1
    future = 0
    for trial in range(60):
        a = law([(F(RNG.randrange(9), 5), F(1, 3)), (F(RNG.randrange(9), 5), F(2, 3))])
        b = law([(F(RNG.randrange(9), 5), F(1, 2)), (F(RNG.randrange(9), 5), F(1, 2))])
        avg = mix(a, b, F(2, 5))
        v = F(RNG.randrange(5, 20), 5)
        deficit = lambda z: 1-hbar(z, v)+hbar(z, 2*v)
        assert .4*deficit(a)+.6*deficit(b) >= deficit(avg)-1e-11
        c = F(2, 3)
        prefix = mix({F(0): F(1, 2), v: F(1, 2)}, {F(-1): F(1)}, c)
        window = lambda z: hbar(z, F(1, 10))-hbar(z, F(10))
        gain = .4*(window(convolve(a, prefix))-window(a))+.6*(window(convolve(b, prefix))-window(b))
        assert gain >= float(c)*(deficit(avg)-.5)-1e-11
        future += 1
    OUT['shifted_entropy'] = {'two_point_models': cases, 'future_mixture_models': future,
        'max_matching_scale_error': worst, 'rational_breakpoint_integration_numeric_logarithms': True}


def prefix_values(lam, n):
    return [(bits, sum((F(bit)*lam**i for i, bit in enumerate(bits)), F(0))) for bits in product((0, 1), repeat=n)]


def prefix_tests():
    cases = 0
    for lam in (F(3, 5), F(2, 3), F(3, 4)):
        rows = prefix_values(lam, 12)
        assert len({x for _, x in rows}) == len(rows)
        assert not ({x for bits, x in rows if bits[0] == 0} & {x for bits, x in rows if bits[0] == 1})
        for n in range(1, 9):
            qcount, joint = Counter(), Counter()
            for bits, x in rows:
                q = floor(x/lam**n)
                qcount[q] += 1
                joint[(bits[:n], q)] += 1
            hq = entropy([c/len(rows) for c in qcount.values()])
            hj = entropy([c/len(rows) for c in joint.values()])
            assert hj >= n-1e-12
            assert hq <= log2(float(1/(1-lam)/lam**n+2))+1e-12
            assert 0 <= hj-hq+1e-12 <= n+2e-12
            cases += 1
    OUT['first_bit_capacity'] = {'finite_entropy_models': cases,
        'exact_atomic_branch_overlap_zero_for_all_tested_truncations': True,
        'does_not_certify_limit_common_mass': True}


def bin_mass_tests():
    models = pairs = nonvacuous = 0
    for n in range(3, 10):
        lam, length, a = F(3, 4), F(4), F(1)
        scale = lam**n
        width = a*scale
        rows = prefix_values(lam, n)
        sets = [defaultdict(set), defaultdict(set)]
        masses = [defaultdict(F), defaultdict(F)]
        incidence = Counter()
        for bits, value in rows:
            first = bits[0]
            lo, hi = value+scale*a, value+scale*(length-a)
            for cell in range(floor(lo/width), floor(hi/width)+1):
                sets[first][cell].add(bits)
                incidence[bits] += 1
            for tail in (a, length/2, length-a):
                masses[first][floor((value+scale*tail)/width)] += F(1, 3*2**n)
        cells = sorted(set(sets[0]) | set(sets[1]))
        c = ceil((length-2*a)/a)+2
        assert max(incidence.values()) <= c
        beta = sum(min(masses[0][j], masses[1][j]) for j in cells)
        for first in (0, 1):
            for cell in cells:
                assert masses[first][cell] <= F(len(sets[first][cell]), 2**n)
        for threshold in (1, 2, 3, 5, 8):
            good = [j for j in cells if len(sets[1][j]) >= threshold]
            union = set().union(*(sets[0][j] for j in good))
            bound = (2**n*beta-len(cells)*threshold)/c
            assert len(union) >= bound
            nonvacuous += bound > 0
            lookup = dict(rows)
            for cell in good:
                for u in sets[0][cell]:
                    for v in sets[1][cell]:
                        assert abs(lookup[u]-lookup[v]) <= (length-a)*scale
                        pairs += 1
            models += 1
    OUT['cross_prefix_bins'] = {'mass_models': models, 'positive_lower_bounds': nonvacuous,
        'same_bin_word_pairs_checked': pairs, 'no_singularity_inference': True}


if __name__ == '__main__':
    for check in (frequency_tests, spectral_tests, cancellation_tests, fixed_square_tests,
                  pair_tests, entropy_gain_tests, prefix_tests, bin_mass_tests):
        check()
        print(check.__name__, 'passed', flush=True)
    result = {'batch': 'B014', 'python': sys.version.split()[0], 'numpy': np.__version__,
              'checks': OUT, 'scope': 'Selected finite models and negative controls; no global theorem, Lean build or priority certification.'}
    Path(__file__).with_name('results.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(OUT, indent=2))
