# B008: Banach geometry and nonlinear Markov smoothing

Extraction date: 2026-10-16. This batch adds 4 previously uncatalogued families, 4 source manuscripts and 8 instruments. The original groups of 17 and 21 families remain together in B001.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000162: Support propagation creates an invariant convex set for a condensing map](../../catalog/instruments/MI-000162.md) | 322 |
| [MI-000163: Dual cotype gives bounded sign-indexed lifts with prescribed moments](../../catalog/instruments/MI-000163.md) | 326 |
| [MI-000164: A dyadic compact domain preserves fixed-length dual moments](../../catalog/instruments/MI-000164.md) | 326 |
| [MI-000165: A finite reflecting lattice lift transfers Markov type to odd edge sums](../../catalog/instruments/MI-000165.md) | 327 |
| [MI-000166: Ramsey averaging and transposed couplings build reversible chart transport](../../catalog/instruments/MI-000166.md) | 327 |
| [MI-000167: Finite ell1 cuts retain a contractive affine reconstruction](../../catalog/instruments/MI-000167.md) | 332 |
| [MI-000168: A flat cubic converts quartic potential into martingale jump energy](../../catalog/instruments/MI-000168.md) | 332 |
| [MI-000169: Expected medians of stopped-walk endpoints control two smoothing costs](../../catalog/instruments/MI-000169.md) | 332 |

## Source and method

The source revision is [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). Its preprint tree is identical to the B001 snapshot; intervening upstream commits changed repository administration. Records give exact manuscript bindings, labelled source passages and SHA-256 hashes in the [source manifest](../../sources/batches/B008.json).

Selection covers four functional-analysis manuscripts through eight auxiliary constructions. The selected source arguments were read, including the complete elementary stopped-median estimate in family 332. Three available Comparator declarations were compared with their family scope documents; family 332 has no such document in the pinned inventory. Primary sources were retrieved for Darbo fixed points, ultrapowers, type and cotype, Markov type, metric Markov cotype and earlier cubic cut smoothing. The cards distinguish classical ingredients from candidate source-specific combinations; the searches do not certify historical priority.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) contain eight groups of finite checks: support and parameter examples; complete finite sign cubes; dyadic shifts and quotient-kernel controls; exact reversible-walk moment recursions; chart couplings and detailed balance; weighted cut reconstruction; rational quartic-potential identities and revealing martingales; and stopped-walk medians on stationary chains. Negative controls distinguish norm contraction from contraction of noncompactness, compactness from quotient-compatible finite-rank approximation, stationary-average matching from matching conditional on each chart, and the flat cubic from an invalid identity-map replacement.

The earlier Cheng-Wang-Xiang paper already uses the same cubic. The selected additional mechanism is its combination with a quartic potential and a geometrically stopped martingale. The explicit expected-median points belong to the ambient ell1 space and need not remain in an input subspace.

Finite examples do not certify infinite-dimensional fixed points, ordinary AP, general Ramsey existence, the global source theorems or novelty. No Lean solution was built. The source claims about Tingley's problem, the cotype-cotype characterization, superreflexivity and the ell1 extension problem remain distinct from the selected review and computational checks.

Potential applications are labelled as proposals. This extraction adds no claim of independent human review or exhaustive novelty certification.
