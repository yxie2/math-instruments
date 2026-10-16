# B035: Exact algorithmic interfaces, sparse reductions and fixed-block estimates

Extraction date: 2026-10-16. This batch adds 4 previously uncatalogued families, 4 source manuscripts and 8 instruments. The original groups of 17 and 21 families remain together in B001.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000384: Implement a rational matrix shear with one interchange per rank](../../catalog/instruments/MI-000384.md) | 109 |
| [MI-000385: Cancel synthetic characters without division and retain the FFT output order](../../catalog/instruments/MI-000385.md) | 109 |
| [MI-000386: Reduce a matching cardinality threshold using a sparse permutation network](../../catalog/instruments/MI-000386.md) | 120 |
| [MI-000387: Reduce perfect matching to maximum degree three with odd incidence paths](../../catalog/instruments/MI-000387.md) | 120 |
| [MI-000388: Telescope weighted curvature when parent and child masses do not conserve](../../catalog/instruments/MI-000388.md) | 121 |
| [MI-000389: Use fixed block masses to remove large predictable cost offsets from entropy regret](../../catalog/instruments/MI-000389.md) | 121 |
| [MI-000390: Preserve a global priority suffix while pruning only locally relevant list entries](../../catalog/instruments/MI-000390.md) | 124 |
| [MI-000391: Bound surviving upward-closed injections by a shared boundary slot](../../catalog/instruments/MI-000391.md) | 124 |

## Source and method

The source revision is [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). Its preprint tree is identical to the B001 snapshot; intervening upstream commits changed repository administration. Records give exact manuscript bindings, labelled source passages and SHA-256 hashes in the [source manifest](../../sources/batches/B035.json).

Eight selected algorithmic mechanisms from four families. Complete selected proofs were read, with targeted comparisons to established polynomial transforms, matching reductions and optimistic learning. Full fast algorithms and end-to-end complexity arguments were not audited.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) contain eight groups.

- Family 109: 60 exact rational/modular shear models and 48 exact synthetic transforms with retained frequency order.
- Family 120: 213 exhaustive small-graph cardinality thresholds and 814 exhaustive nonisolated graph degree reductions, including witness decoding.
- Family 121: 100 rational nonconservative trees and 1,600 block-entropy prefix checks, including 910 steps exceeding the stronger global variation condition.
- Family 124: 200 poset list models, a pruning-order negative control and 2,426 finite boundary-witness families.

Families 109 and 120 have no listed formalization scope. The edit-distance final target and the scheduling comparison were inspected; their targets contain sorry. The long edit-distance support construction was not audited. No Lean build or global complexity certificate. Immutable import edition unchanged.

Potential applications are labelled as proposals. This extraction adds no claim of independent human review or exhaustive novelty certification.
