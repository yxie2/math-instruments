# B003: Geometric inequalities and dimension reduction

Extraction date: 2026-10-16. This batch adds 4 previously uncatalogued families, 4 source manuscripts and 10 instruments. The original groups of 17 and 21 families remain together in B001.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000125: A moment-coordinate tensor square decomposition gives summandwise variance control](../../catalog/instruments/MI-000125.md) | 091 |
| [MI-000126: Removing affine obstructions from double-divergence tests without a global lower bound](../../catalog/instruments/MI-000126.md) | 091 |
| [MI-000127: Weighted relative moments can be separated into simultaneous embedding coordinates](../../catalog/instruments/MI-000127.md) | 094 |
| [MI-000128: A fixed-point reweighting turns average electrical localization into uniform row control](../../catalog/instruments/MI-000128.md) | 094 |
| [MI-000129: Antipodal row and column incidences force quadratic exact coordinate dimension](../../catalog/instruments/MI-000129.md) | 094 |
| [MI-000130: Separated displacement scales keep unbounded sheet multiplicity uniformly doubling](../../catalog/instruments/MI-000130.md) | 098 |
| [MI-000131: Lexicographic derivative extrema turn crossing sheets into a packing obstruction](../../catalog/instruments/MI-000131.md) | 098 |
| [MI-000132: Finite Hilbert obstructions can be assembled into a compact obstruction in any Banach space](../../catalog/instruments/MI-000132.md) | 098 |
| [MI-000133: Nonlinear Jacobian compatibility forces a linear symmetric matrix field to commute](../../catalog/instruments/MI-000133.md) | 101 |
| [MI-000134: An exponential cone density transfers entropy gaps to isotropic-constant gaps](../../catalog/instruments/MI-000134.md) | 101 |

## Source and method

The source revision is [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). Its preprint tree is identical to the B001 snapshot; intervening upstream commits changed repository administration. Records give exact manuscript bindings, labelled source passages and SHA-256 hashes in the [source manifest](../../sources/batches/B003.json).

Selection covers convex geometry and metric dimension reduction. The extracted statements and selected proof arguments were read in the pinned TeX sources. The supplied formalization scope and Comparator targets were compared for families 091, 094 and 098; none is listed for 101. Primary antecedents were retrieved for moment maps, Brascamp?Lieb methods, empirical dimension reduction, electrical localization, support detection and entropy?cone transfer. These targeted comparisons are not exhaustive priority searches.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) distinguish exact finite identities from numerical examples. They check tensor symmetrization, the Gaussian operator model, finite weighted projections, row/column defects, covering constants, Jacobian coefficient identities and cone constants. These checks do not certify the source theorems. No Lean solution was built or kernel-checked.

- Family 091: the matrix-square trace must not be replaced by a Frobenius norm; the density lemma retains both operator identities and local positivity.
- Family 094: the weighted criterion needs uniform bounds across testing probabilities. Exact coordinate obstructions do not contradict approximate finite-set reduction.
- Family 098: the initial sheet space and the compact Banach-space assembly are separate constructions, with different covering constants.
- Family 101: the local rigidity argument and the classical cone reduction do not independently establish the source?s global sharp entropy inequality. The cone reduction is credited as established work.

Potential applications are labelled as proposals. This extraction adds no claim of independent human review or exhaustive novelty certification.
