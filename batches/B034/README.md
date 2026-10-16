# B034: Continuous scaling, central correction and representation-uniform tensor methods

Extraction date: 2026-10-16. This batch adds 4 previously uncatalogued families, 4 source manuscripts and 8 instruments. The original groups of 17 and 21 families remain together in B001.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000376: Avoid small collective images by a Grassmann incidence dimension bound](../../catalog/instruments/MI-000376.md) | 294 |
| [MI-000377: Normalize expanding bundle maps through a unique determinant minimizer](../../catalog/instruments/MI-000377.md) | 294 |
| [MI-000378: Correct mixed central inputs by an explicit bounded Hochschild homotopy](../../catalog/instruments/MI-000378.md) | 295 |
| [MI-000379: Transfer a bounded-ball L2 modulus through repeated tracial ultrapowers](../../catalog/instruments/MI-000379.md) | 295 |
| [MI-000380: Prove algebraic tensor independence using a central support projection](../../catalog/instruments/MI-000380.md) | 299 |
| [MI-000381: Choose tensor labels that remain independent under every rank-two quotient](../../catalog/instruments/MI-000381.md) | 299 |
| [MI-000382: Recover the ideal lattice and trace finiteness ideals from the extended trace cone](../../catalog/instruments/MI-000382.md) | 301 |
| [MI-000383: Preserve a lower spectral-rank signal under normalized block averaging](../../catalog/instruments/MI-000383.md) | 301 |

## Source and method

The source revision is [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). Its preprint tree is identical to the B001 snapshot; intervening upstream commits changed repository administration. Records give exact manuscript bindings, labelled source passages and SHA-256 hashes in the [source manifest](../../sources/batches/B034.json).

Eight selected mechanisms from four operator-algebra families. Complete selected mathematical proofs were read. Operator-scaling and trace-cone antecedents were compared with primary sources. Comparator targets and selected definitions were inspected; the long CharacterCriterion support construction was not audited.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) contain eight groups.

- Family 294: 600 exact incidence counts and 24 expanding matrix normalizations, maximum error below 3.7e-13.
- Family 295: 240 exact noncommutative central-homotopy checks in degrees one through four and 240 bounded-ball matrix examples.
- Family 299: nine finite factor products, a nonfactor negative control and 75 sampled rank-two tensor quotient maps. Sampling does not certify the universal quotient statement.
- Family 301: 1,364 finite ideal pairs and 60 rank-deficient normalized block averages, with a negative control for ordinary averaging.

Five listed Comparator files were inspected at the target/definition level; relevant targets contain sorry. No Lean build or global operator-algebra theorem certification. Immutable import edition unchanged.

Potential applications are labelled as proposals. This extraction adds no claim of independent human review or exhaustive novelty certification.
