# B042: Avoidance, logarithmic energies and integral arithmetic interfaces

Extraction date: 2026-10-16. This batch adds 4 previously uncatalogued families, 4 source manuscripts and 8 instruments. The original groups of 17 and 21 families remain together in B001.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000440: Avoid all bounded-degree polynomial equations over one fixed coefficient field](../../catalog/instruments/MI-000440.md) | 001 |
| [MI-000441: Bound the degree needed to force minimal Lagrangian intersections](../../catalog/instruments/MI-000441.md) | 001 |
| [MI-000442: Match logarithmic-kernel damping to the singular endpoint scales](../../catalog/instruments/MI-000442.md) | 005 |
| [MI-000443: Turn negative moment squares into one-variable upper certificates](../../catalog/instruments/MI-000443.md) | 005 |
| [MI-000444: Track ordinary depth additively through the Ihara bracket](../../catalog/instruments/MI-000444.md) | 008 |
| [MI-000445: Certify saturation of a rational span from independent prime reductions](../../catalog/instruments/MI-000445.md) | 008 |
| [MI-000446: Recover a semistable Frobenius polynomial from sufficiently precise finite torsion](../../catalog/instruments/MI-000446.md) | 030 |
| [MI-000447: Compare residual character summands by integral group-ring evaluation](../../catalog/instruments/MI-000447.md) | 030 |

## Source and method

The source revision is [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). Its preprint tree is identical to the B001 snapshot; intervening upstream commits changed repository administration. Records give exact manuscript bindings, labelled source passages and SHA-256 hashes in the [source manifest](../../sources/batches/B042.json).

Eight selected arithmetic and analytic interfaces with exact labels. Complete selected proofs read; targeted primary comparison of the Chebyshev logarithmic identity. Source headline claims remain outside scope.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) contain eight groups: bounded-degree monomial encoding, 72 exact Lagrangian models, 144 high-precision endpoint comparisons, sixty moment-square certificates, exact Ihara expansions, 100 lattice models, 360 bounded Frobenius polynomials and 120 residue-character evaluations.

No Milne rationality, Catalan irrationality, Deligne-Drinfeld freeness or modularity theorem is certified. The 005 Comparator and selected 008 definitions/target were read; main targets contain sorry. The 008 tangent implementation was not audited. Families 001 and 030 have no listed scope. No Lean build. Immutable edition unchanged.

Potential applications are labelled as proposals. This extraction adds no claim of independent human review or exhaustive novelty certification.
