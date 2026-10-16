# B030: Local degree, modular rank and probability mechanisms in group theory

Extraction date: 2026-10-16. This batch adds 4 previously uncatalogued families, 4 source manuscripts and 8 instruments. The original groups of 17 and 21 families remain together in B001.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000344: Turn a minimum-norm mixture of crossings into dual weights](../../catalog/instruments/MI-000344.md) | 246 |
| [MI-000345: Use a tree energy budget to bound the frequency of unfavorable ancestors](../../catalog/instruments/MI-000345.md) | 246 |
| [MI-000346: Localize SU(2) word-map degree by cyclic conjugation](../../catalog/instruments/MI-000346.md) | 249 |
| [MI-000347: Convert exact translated relator counts into a uniform quadratic error](../../catalog/instruments/MI-000347.md) | 249 |
| [MI-000348: Retain matrix rank modulo a prime using row norms and determinant divisibility](../../catalog/instruments/MI-000348.md) | 252 |
| [MI-000349: Assemble a block diagonal rank certificate from low-degree punctured-line weights](../../catalog/instruments/MI-000349.md) | 252 |
| [MI-000350: Bound affine product-density perturbations independently of dimension](../../catalog/instruments/MI-000350.md) | 253 |
| [MI-000351: Push approximate invariance to a subgroup and extract a finite Folner set](../../catalog/instruments/MI-000351.md) | 253 |

## Source and method

The source revision is [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). Its preprint tree is identical to the B001 snapshot; intervening upstream commits changed repository administration. Records give exact manuscript bindings, labelled source passages and SHA-256 hashes in the [source manifest](../../sources/batches/B030.json).

Eight selected mechanisms from four group-theoretic source families. Complete selected proofs were read; Albin-Poggi-Corradini Theorem 5.1 and Froyshov Proposition 2.1 were checked as direct antecedents. All four Comparator files were inspected. The source global group-theoretic claims are not certified.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) contain eight groups.

- Family 246: 36 finite crossing optimization/decomposition models and 360 probability-tree levels.
- Family 249: 45 torus fiber counts, 60 complex-normal determinant identities and 240 quaternion cancellation models. These are algebraic checks, not a computation of local mapping degree.
- Family 252: 74 integer rank models, six regular-block trace models with characteristic dividing the group order and 60 exact finite-field tensor certificates. A control detects the invalid deletion of all marks.
- Family 253: 48 product-density quadratures, 60 nonnormal-subgroup pushforwards and 30 exact layer-cake models. The quadrature square root is C2, not the source C-infinity function; the partition coupling is not verified.

All four Comparator targets contain sorry. No Lean build, global conjecture certification or exhaustive novelty search was performed. The immutable import edition is unchanged.

Potential applications are labelled as proposals. This extraction adds no claim of independent human review or exhaustive novelty certification.
