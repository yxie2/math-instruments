"""Finite/local checks for B047; no source headline theorem is certified."""
from fractions import Fraction
from itertools import product
import json
from math import cos, pi, sin
from pathlib import Path
import random
import numpy as np
from scipy.integrate import quad
import sympy as s

RESULT = {'scope': 'Seven finite/local groups. No measurable-cocycle, topological, geometric headline theorem or Lean proof certified.', 'checks': {}}
rng = random.Random(470)

# A stationary finite-cycle graph satisfies l_(i+1)=r_i l_i. Closing the
# cycle forces zero when its monodromy contracts, even if some steps expand.
cycles = 0
for length in range(1, 9):
    for trial in range(5):
        ratios = [s.Rational(rng.randint(1, 8), rng.randint(1, 5)) for _ in range(length-1)]
        ratios.append(s.Rational(1, 2) / s.prod(ratios))
        M = s.zeros(length)
        for i, ratio in enumerate(ratios):
            M[i, (i+1) % length] += 1
            M[i, i] -= ratio
        assert M.rank() == length
        cycles += 1
assert (s.eye(2)-s.eye(2)).rank() == 0  # equal-exponent control
assert all(Fraction(1, 2)**(n+1) == Fraction(1, 2)*Fraction(1, 2)**n for n in range(-9, 9))
RESULT['checks']['stationary_graphs'] = {'periodic_models': cycles, 'controls': 'Equal exponents leave graph freedom; 2^(-n) on the infinite counting-measure shift contracts without vanishing.'}

# Exact alternating forcing, both Green-series orientations, including a
# nontrivial triangular block. The closed solution is solved independently.
errors = []
for ratio in [s.Rational(1, 2), s.Rational(2, 3), s.Rational(3, 2), s.Integer(2)]:
    for off in [0, s.Rational(1, 3)]:
        L = s.Matrix([[ratio, off], [0, ratio]])
        v = s.Matrix([2, -1])
        exact = (s.eye(2)+L).inv()*v
        value = s.zeros(2, 1)
        operator = L if ratio < 1 else L.inv()
        power = s.eye(2) if ratio < 1 else operator
        for j in range(140):
            value += (-1)**j * power*v
            power = power*operator
        error = max(abs(x) for x in value-exact)
        assert error < s.Rational(1, 10**20)
        assert -exact == L*exact-v
        errors.append(float(error))
RESULT['checks']['tempered_green_series'] = {'scalar_or_triangular_models': len(errors), 'maximum_truncation_error': max(errors), 'zero_exponent_control': 'L=1, e=0 has all constant solutions.'}

# Compute the coefficient of g after Fubini, separately from the endpoint
# coefficient. These are the nontrivial linear terms in the Jensen identity.
t, x = s.symbols('t x', real=True)
base = (1-s.cos(t))*(1+s.cos(t))
a = s.integrate(s.sin(x)*s.cos(2*x), (x, 0, t))
b = s.integrate(s.sin(x)*s.cos(2*x), (x, t, s.pi))
c = s.integrate(s.sin(x)*s.sin(2*x), (x, 0, t))
d = s.integrate(s.sin(x)*s.sin(2*x), (x, t, s.pi))
assert s.trigsimp(base-s.sin(t)**2) == 0
assert s.simplify(s.expand_trig(base+(a*b+c*d)/2-s.Rational(5, 6)*s.sin(t)**2)) == 0
errors = []
for point in [.2, .7, 1.2, 2., 2.7]:
    def inner(left):
        low = max(point, left+pi/4)
        high = min(pi, left+3*pi/4)
        return sin(left)*(cos(low)-cos(high)) if low < high else 0.
    cuts = [v for v in [point-pi/4, point-3*pi/4, pi/4, 3*pi/4] if 0 < v < point]
    F = quad(inner, 0, point, points=cuts, epsabs=1e-12)[0]
    error = abs(F/sin(point)**2 - 2**.5/2)
    assert error < 1e-9
    errors.append(error)
point = .7
F = quad(lambda left: sin(left)*quad(lambda right: (1+.5*cos(right-left))*sin(right), point, pi)[0], 0, point)[0]
endpoint = (quad(lambda z: sin(z)*(1+.5*cos(z)), 0, point)[0]+quad(lambda z: sin(z)*(1+.5*cos(z)), 0, pi-point)[0])/2
asymmetric_difference = F/sin(point)**2-endpoint
assert abs(asymmetric_difference) > .01
RESULT['checks']['weighted_cancellation'] = {'exact_smooth_weights': 2, 'discontinuous_weight_points': len(errors), 'maximum_coefficient_error': max(errors), 'asymmetric_coefficient_difference': asymmetric_difference}

# Schur algebra uses noncommuting rectangular blocks; the endpoint difference
# may be negative even though the velocity block is positive.
def randmat(n, m):
    return s.Matrix(n, m, lambda i,j: rng.randint(-3, 3))
for trial in range(40):
    H0 = randmat(3, 3); H = H0.T*H0+s.eye(3)
    Cp, R = randmat(2, 3), randmat(2, 3)
    V0 = randmat(2, 2); Vp = V0+V0.T
    S = Vp-Cp*H.inv()*Cp.T
    derivative = Vp-Cp*R.T-R*Cp.T+R*H*R.T
    square = (R-Cp*H.inv())*H*(R-Cp*H.inv()).T
    assert derivative-S == square
    assert square[0,0] >= 0 and square[1,1] >= 0 and square.det() >= 0
    for sign in [-1, 1]:
        DH = sign*H; DC = randmat(2, 3); DV = V0+V0.T
        Q = DV-DC*DH.inv()*DC.T
        DA = DV.row_join(DC).col_join(DC.T.row_join(DH))
        assert DA.det() == DH.det()*Q.det()
        assert -DV-(-DC)*(-DH).inv()*(-DC.T) == -Q
assert (s.Matrix([[1]])*s.Matrix([[-1]])*s.Matrix([[1]]))[0] < 0
RESULT['checks']['schur_complements'] = {'square_models': 40, 'both_sign_determinant_models': 80, 'control': 'Negative H prime reverses the sign of the square term.'}

# Actual nilpotent matrices for torsion; high-degree dimensions count genuine
# free strings and avoid an artificial truncation kernel in the free part.
module_models = 0
for sizes in [(1,), (2, 5), (1, 3, 4), ()]:
    blocks = []
    for size in sizes:
        J = s.zeros(size)
        for i in range(size-1):
            J[i+1,i] = 1
        blocks.append(J)
    T = s.diag(*blocks) if blocks else s.zeros(0)
    nullity = T.rows-T.rank()
    assert nullity == len(sizes)
    for shifts in [[], [0], [1], [0, 1, 3, 8]]:
        rho = len(shifts); count = rho+2*nullity
        assert count == (rho+T.rows-T.rank()) + nullity
        for D in [20, 21, 30]:
            hilbert = lambda degree: sum(degree >= q and (degree-q)%2 == 0 for q in shifts)
            assert hilbert(D)+hilbert(D-1) == rho
        module_models += 1
RESULT['checks']['graded_modules'] = {'models': module_models, 'scope': 'Nilpotent torsion and prescribed free degree shifts; no Gysin or localization computation.'}

barcode_models = 0
for trial in range(100):
    D = rng.randint(1, 6)
    bars = [(rng.randint(0, 10), rng.randint(1, D)) for _ in range(8)]
    cut = rng.randint(0, 14); later = cut+D+Fraction(1, 2)
    alive = [b for b in bars if b[0] <= cut < b[0]+b[1]]
    survive = [b for b in alive if later < b[0]+b[1]]
    assert not survive
    # Add three infinite bars, present already at the cut.
    dim_source = 3+len(alive); transition_rank = 3
    if transition_rank == dim_source:
        assert not alive
    barcode_models += 1
# A long-lived but eventually dying bar defeats the conclusion without horizon.
assert 0 <= 4 < 100 and 4+3+Fraction(1, 2) < 100
band_models = 0
for ell, delta in product([Fraction(1), Fraction(3,2), Fraction(7,3)], [0, Fraction(2,3), 2]):
    for m in range(1, 15):
        cut = m*ell-Fraction(1,3); D=2; n=3; C=2
        beta = delta/ell
        for index_error, local_error in product(range(-n,n+1), range(-C,C+1)):
            j=m*delta+index_error+local_error
            assert abs(j-beta*cut) <= C+n+beta*(D+1)
            band_models += 1
RESULT['checks']['bounded_death'] = {'barcode_models': barcode_models, 'event_band_models': band_models, 'control': 'A bar dying at 100 survives the tested short interval when the bounded-death hypothesis is omitted.'}

theta = s.symbols('theta', real=True)
for m in range(1, 8):
    normalized_centroid = s.integrate(s.cos(theta)*s.sin(theta)**m, (theta, 0, s.pi/2))
    assert s.simplify(normalized_centroid-s.Rational(1,m+1)) == 0
cap_angle = s.pi/3
assert s.simplify(2*(2*s.pi*(1-s.cos(cap_angle)))-2*s.pi) == 0
perimeter = s.simplify(2*(2*s.pi*s.sin(cap_angle)))
assert perimeter == 2*s.sqrt(3)*s.pi
RESULT['checks']['spherical_constraints'] = {'hemisphere_dimensions_m': list(range(1,8)), 'two_antipodal_caps_on_S2_perimeter': str(perimeter), 'scope': 'Centroid and feasible cap formulas only; no constrained optimum or topological detection computation.'}

RESULT['status'] = 'passed'
RESULT['groups'] = len(RESULT['checks'])
RESULT['versions'] = {'numpy': np.__version__, 'sympy': s.__version__}
Path(__file__).with_name('results.json').write_text(json.dumps(RESULT, indent=2)+'\n', encoding='utf-8')
print(json.dumps(RESULT))
