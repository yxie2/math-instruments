# B038: Geometric positivity and inverse-matrix budgets

Extraction date: 2026-10-16. This batch adds 4 previously uncatalogued families, 4 source manuscripts and 8 instruments. The original groups of 17 and 21 families remain together in B001.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000408: Certify a Hermitian determinant optimum by finitely many contact directions](../../catalog/instruments/MI-000408.md) | 338 |
| [MI-000409: Realize a constant-volume finite jet by polynomial shears](../../catalog/instruments/MI-000409.md) | 338 |
| [MI-000410: Translate positivity of a three-form frame into taming of an almost-complex structure](../../catalog/instruments/MI-000410.md) | 341 |
| [MI-000411: Expose a convex Lorentz cone inside a common-Lagrangian definite-pair constraint](../../catalog/instruments/MI-000411.md) | 341 |
| [MI-000412: Lift anti-invariant two-forms to closed forms by an elliptic inverse](../../catalog/instruments/MI-000412.md) | 342 |
| [MI-000413: Correct positive separators while distinguishing existence from a fixed class](../../catalog/instruments/MI-000413.md) | 342 |
| [MI-000414: Compare positive matrix decrements with inverse increments without commutativity](../../catalog/instruments/MI-000414.md) | 357 |
| [MI-000415: Control inverse-matrix derivatives without multiplying the exponential base](../../catalog/instruments/MI-000415.md) | 357 |

## Source and method

The source revision is [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). Its preprint tree is identical to the B001 snapshot; intervening upstream commits changed repository administration. Records give exact manuscript bindings, labelled source passages and SHA-256 hashes in the [source manifest](../../sources/batches/B038.json).

Eight selected geometric algebra interfaces with exact source labels. Complete selected proofs read; primary antecedents checked for shear generation, exact-form correction and cohomology splitting. Geometric headline proofs were not audited.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) contain eight groups.

- Sixteen contact-constrained determinant optimizations; seven exact shear-span dimensions and forty exact shear inverses.
- 120 definite-pair wedge models and 1,100 common-Lagrangian convex/basic-addition checks.
- One hundred closed-lift Fourier symbols and one hundred finite separator-correction models.
- Six hundred noncommuting inverse increments, factorial ratios through order 200 and eighteen exact inverse-series models.

The tests do not certify global uniformization, hypersymplectic deformation, tamed-to-compatible existence or RCD coordinates. The 342 Comparator existence target contains sorry. Its scope document links a September manuscript, while the extraction binds the October-6 manuscript; this version mismatch is not silently treated as exact agreement. Families 338, 341 and 357 have no listed scope. No Lean build. Immutable import edition unchanged.

Potential applications are labelled as proposals. This extraction adds no claim of independent human review or exhaustive novelty certification.
