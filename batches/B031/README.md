# B031: Averaging, couplings, graphings and finite chain certificates

Extraction date: 2026-10-16. This batch adds 4 previously uncatalogued families, 4 source manuscripts and 8 instruments. The original groups of 17 and 21 families remain together in B001.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000352: Compare Radon masses to Haar volumes uniformly over translated set shapes](../../catalog/instruments/MI-000352.md) | 255 |
| [MI-000353: Choose nested recurrence sets before sampling a sequence of transitions](../../catalog/instruments/MI-000353.md) | 255 |
| [MI-000354: Turn summed extension-count errors into a normalized coupling law](../../catalog/instruments/MI-000354.md) | 257 |
| [MI-000355: Bound dependent conditional tests through inductive means in a CAT(0) cone](../../catalog/instruments/MI-000355.md) | 257 |
| [MI-000356: Build a complete Borel set at the finite-class mass threshold](../../catalog/instruments/MI-000356.md) | 259 |
| [MI-000357: Generate commuting edges from sparse markers and propagate a height window](../../catalog/instruments/MI-000357.md) | 259 |
| [MI-000358: Use a split third boundary to obtain a finite plus construction for all coefficients](../../catalog/instruments/MI-000358.md) | 321 |
| [MI-000359: Certify twisted second-homology vanishing by an exact Fox minor](../../catalog/instruments/MI-000359.md) | 321 |

## Source and method

The source revision is [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). Its preprint tree is identical to the B001 snapshot; intervening upstream commits changed repository administration. Records give exact manuscript bindings, labelled source passages and SHA-256 hashes in the [source manifest](../../sources/batches/B031.json).

Eight selected mechanisms from four group/topology families. Complete selected proofs were read. Direct antecedents checked: Sturm 2003 Theorem 4.7(a), Gaboriau 2000 Proposition VI.23 and Mannan 2009 Section 2. Two listed Comparator files were inspected; the other families have no listed scope documents.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) contain eight groups.

- Family 255: 120 finite averaging identities, 124 singular interval examples and 68 exact three-stage recurrence models.
- Family 257: 160 count normalizations, 243 collision bounds and exact enumeration of 3,279 lists in a non-Hilbert tripod cone, plus 100 total-variation tests.
- Family 259: seven exhaustive marker models, 1,500 commuting paths and twelve height-window inductions. No distinct-cost lower bound checked.
- Family 321: 60 split-boundary models over non-fields and exact reconstruction of all 20 Fox-matrix entries, the chain identity and the nonzero minor. The tower obstruction is not verified.

No global group or topology claim is certified. The two Comparator files contain sorry targets; no Lean build was performed. Immutable import edition unchanged.

Potential applications are labelled as proposals. This extraction adds no claim of independent human review or exhaustive novelty certification.
