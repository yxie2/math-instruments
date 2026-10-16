# B033: Holomorphic gluing, curvature, alternating traces and rational certificates

Extraction date: 2026-10-16. This batch adds 4 previously uncatalogued families, 4 source manuscripts and 8 instruments. The original groups of 17 and 21 families remain together in B001.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000368: Match endpoint jets before choosing a thin complex parameter collar](../../catalog/instruments/MI-000368.md) | 042 |
| [MI-000369: Pay for shrinking domains with a quadratic holomorphic splitting recurrence](../../catalog/instruments/MI-000369.md) | 042 |
| [MI-000370: Recover the central frame determinant from a Green-weighted Ricci integral](../../catalog/instruments/MI-000370.md) | 051 |
| [MI-000371: Pass from trace to log-determinant derivatives through a Sobolev boundary sequence](../../catalog/instruments/MI-000371.md) | 051 |
| [MI-000372: Remove derivatives of a moving triangular basis by alternating the trace](../../catalog/instruments/MI-000372.md) | 063 |
| [MI-000373: Select a joint eigenvalue wedge and force independent graded operator directions](../../catalog/instruments/MI-000373.md) | 063 |
| [MI-000374: Express P1 fiber integration as an involution and a divided-difference rule](../../catalog/instruments/MI-000374.md) | 067 |
| [MI-000375: Certify a lifted polynomial consequence with modular rank and rational witnesses](../../catalog/instruments/MI-000375.md) | 067 |

## Source and method

The source revision is [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). Its preprint tree is identical to the B001 snapshot; intervening upstream commits changed repository administration. Records give exact manuscript bindings, labelled source passages and SHA-256 hashes in the [source manifest](../../sources/batches/B033.json).

Eight selected mechanisms from four complex-geometric families. Complete selected proofs were read, with targeted classical comparisons for Cartan splitting and Hochschild trace invariance. No exhaustive novelty search or headline theorem certification.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) contain eight groups.

- Family 042: exact endpoint jets, 21 thin-collar models, quadratic cancellation and 36 exact recurrence steps.
- Family 051: 24 exact Green/determinant models, four area Hessian integrals and sixteen nonsmooth boundary models.
- Family 063: three exact moving-basis models with nonsemisimple matrices and nonidempotent selectors; 206 selector/grading models.
- Family 067: exact involution/product identities, thirty power identities and 27 rational kernel certificates. The source large constraint matrix and its reported modular ranks were not recomputed.

These families have no listed formalization scope document; no Lean build was performed. The global K3, ampleness, Mukai and dimension-six classification claims are not certified. Immutable import edition unchanged.

Potential applications are labelled as proposals. This extraction adds no claim of independent human review or exhaustive novelty certification.
