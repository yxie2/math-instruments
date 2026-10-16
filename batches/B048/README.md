# B048: Affine balancing, uniform sampling and nonlinear transport

Extraction date: 2026-10-16. This batch adds 4 families, 8 source manuscripts and 8 instruments.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000480: Find an interior balancing zero by projecting a strictly inward field](../../catalog/instruments/MI-000480.md) | 088 |
| [MI-000481: Multiply normalized projection-body volumes using Cartesian products](../../catalog/instruments/MI-000481.md) | 088 |
| [MI-000482: Stabilize a selected branch by exposing one fresh noise per comparison](../../catalog/instruments/MI-000482.md) | 089 |
| [MI-000483: Glue consistent bag laws into a global cut metric](../../catalog/instruments/MI-000483.md) | 089 |
| [MI-000484: Upgrade a small bad fraction to a uniform subset-sum lower bound](../../catalog/instruments/MI-000484.md) | 092 |
| [MI-000485: Periodize a buffered covering window without losing boundary coverage](../../catalog/instruments/MI-000485.md) | 092 |
| [MI-000486: Transport a weighted graph norm through an intertwining bijection](../../catalog/instruments/MI-000486.md) | 324 |
| [MI-000487: Build an absorption bijection from an exactly lifted correction](../../catalog/instruments/MI-000487.md) | 324 |

## Source and method

Pinned source revision: [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). The [source manifest](../../sources/batches/B048.json) records hashes, exact labels and manuscript coverage.

Eight selected instruments from all eight manuscripts in four two-manuscript families. Every card has an explicit manuscript slug; the source manifest records extracted and inventory-only companions separately. Full selected arguments were read. Primary comparisons include Cauchy projection, CKR Markov sampling, Li-Liu potential squaring, Rogers-Prosanov periodization and Godefroy-Kalton triangular splitting.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) test eight finite/local mechanisms, with controls for missing freshness, overlap consistency, a coverage buffer and an exact lift. The projection-product computation reproduces the source dimension-20 rational witness.

The supplied scope documents and all nine linked Comparator targets were inspected. Their target proofs contain sorry; no solution was built or kernel-checked. The source global Petty, graph-embedding, covering-order and Banach counterexample claims remain outside these selected checks. The fixed edition is unchanged.

Proposed applications are not subsequent results. No independent human review or exhaustive novelty certification is claimed.
