# B073: Hashing, geometric coverings, game strategies and online policies

Extraction date: 2026-10-16. This batch adds 4 families, 8 source manuscripts and 8 instruments.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000686: Remove alphabet size by collision-controlled hashing and a direct sum](../../catalog/instruments/MI-000686.md) | 099 |
| [MI-000687: Convert finite l1 cuts into exponential collisions and histogram bounds](../../catalog/instruments/MI-000687.md) | 099 |
| [MI-000688: Cover the plane by squares centered on a strongly sheared lattice](../../catalog/instruments/MI-000688.md) | 100 |
| [MI-000689: Compute simplex shadow area from its longest parallel chord](../../catalog/instruments/MI-000689.md) | 100 |
| [MI-000690: Turn finite-valued gain and bounded bias into pathwise average bounds](../../catalog/instruments/MI-000690.md) | 104 |
| [MI-000691: Preserve all-prefix guarantees when restarting parity sub-strategies](../../catalog/instruments/MI-000691.md) | 104 |
| [MI-000692: Extend finite-word policy constraints by compactness](../../catalog/instruments/MI-000692.md) | 110 |
| [MI-000693: Extract causal rational flow tables and round them with a diameter budget](../../catalog/instruments/MI-000693.md) | 110 |

## Source and method

Pinned source revision: [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). The [source manifest](../../sources/batches/B073.json) records hashes, exact labels and manuscript coverage.

Eight instruments from four families and eight selected manuscripts; five companion manuscripts remain inventory-only. Complete selected proofs, four scope documents and six Comparators were read. Primary comparisons identify binary edit-distance embeddings, the known simplex chord identity, increasing-round game strategies and finite-horizon k-server linear programs.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) check hashing, partition histograms, square coverings, simplex projections, finite martingale paths, restart budgets, compact-policy finite models and rational flow rounding.

These checks do not certify the source edit-distance bounds, swept-set covering theorems, quasipolynomial game algorithms or squared-logarithmic k-server claims. Separate Lean solutions were not run; the fixed edition is unchanged.

Proposed applications are not subsequent results. No independent human review or exhaustive novelty certification is claimed.
