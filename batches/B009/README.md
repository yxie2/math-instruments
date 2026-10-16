# B009: Adaptive compression and transport sensitivity

Extraction date: 2026-10-16. This batch adds 4 previously uncatalogued families, 4 source manuscripts and 9 instruments. The original groups of 17 and 21 families remain together in B001.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000170: A compact semigroup anchor permits convex return after adaptive tail choices](../../catalog/instruments/MI-000170.md) | 328 |
| [MI-000171: Weighted telescoping finds a common witness without minimum branch weights](../../catalog/instruments/MI-000171.md) | 328 |
| [MI-000172: Partition labels compress logarithmic distance profiles independently of center count](../../catalog/instruments/MI-000172.md) | 329 |
| [MI-000173: A row support function converts column compression into a polar cover](../../catalog/instruments/MI-000173.md) | 329 |
| [MI-000174: Continuation records permit signed opposing tests with degree-averaged loss](../../catalog/instruments/MI-000174.md) | 330 |
| [MI-000175: Pointed wedges preserve AP while accumulating unbounded approximation constants](../../catalog/instruments/MI-000175.md) | 330 |
| [MI-000176: A midpoint coupling controls first-moment derivatives by cell-mass derivatives](../../catalog/instruments/MI-000176.md) | 374 |
| [MI-000177: Test a mass Laplacian in its range to avoid an inverse-norm loss](../../catalog/instruments/MI-000177.md) | 374 |
| [MI-000178: A thin tilted cell separates transport-map movement from target movement](../../catalog/instruments/MI-000178.md) | 374 |

## Source and method

The source revision is [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). Its preprint tree is identical to the B001 snapshot; intervening upstream commits changed repository administration. Records give exact manuscript bindings, labelled source passages and SHA-256 hashes in the [source manifest](../../sources/batches/B009.json).

Selection covers nine mechanisms in four manuscripts: adaptive convex return and weighted witnesses, partition-label compression and polar covers, signed tests and wedge reductions, and cell-moment and transport estimates. The selected statements and proofs were read and five Comparator declarations were compared with the four scope documents. The extra entropy-ratio statement in the family 329 scope is distinguished from its single Comparator declaration. Primary antecedents were retrieved for semigroup idempotents, entropy duality, signed representations, uniformly discrete free spaces, continuation records and optimal transport. The Bruck publisher link was not retrievable through the browser; that attribution follows the source and its bibliographic DOI, rather than a claimed full-text comparison.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) contain nine groups of finite checks. These include 96 resolvent models, exact rational weighted trees, nonlinear leaf switches, 1,099 profile-distance checks, 36 explicit greedy encodings, 150 support-function calculations, finite continuation records and signed extensions, scalar dual optimization on a metric wedge, rational interval and numerical polygon-cell derivatives, nearly singular Laplacians and twelve three-atom transport optimizations.

Install the dependencies from [verification-requirements.txt](../verification-requirements.txt), then run `python batches/B009/verification/check_instruments.py` from the repository root. The recorded run used Python 3.13, NumPy 2.5.4 and SciPy 1.18.1. Linear programs and polygon finite differences are numerical cross-checks; rational tree and slice formulas are exact arithmetic.

The cards distinguish the finite conditional mechanisms from the full fixed-point theorem, finite-field entropy counterexample, infinite metric block construction and finite-to-Borel transport limit. No Lean solution was built and no exhaustive priority determination was made. The three-atom exponent obstruction follows from the explicit analytic formulas, not a numerical fitted slope.

Potential applications are labelled as proposals. This extraction adds no claim of independent human review or exhaustive novelty certification.
