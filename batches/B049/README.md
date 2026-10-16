# B049: Counting interfaces and binary-information reductions

Extraction date: 2026-10-16. This batch adds 4 families, 8 source manuscripts and 8 instruments.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000488: Make every row tight by one decreasing multiplicative sweep](../../catalog/instruments/MI-000488.md) | 113 |
| [MI-000489: Use covariance rank to obstruct an interior entropy maximum](../../catalog/instruments/MI-000489.md) | 113 |
| [MI-000490: Build one center that controls every affine slack](../../catalog/instruments/MI-000490.md) | 114 |
| [MI-000491: Bound empirical error using only the observed subspace](../../catalog/instruments/MI-000491.md) | 114 |
| [MI-000492: Correct a dyadic approximate sampler by a rare exact residual](../../catalog/instruments/MI-000492.md) | 115 |
| [MI-000493: Choose a maximum-capacity forest before normalizing free variables](../../catalog/instruments/MI-000493.md) | 115 |
| [MI-000494: Control binary entropy-production curvature through two moments](../../catalog/instruments/MI-000494.md) | 119 |
| [MI-000495: Compress a Boolean function and choose a bias-controlled small coordinate](../../catalog/instruments/MI-000495.md) | 119 |

## Source and method

Pinned source revision: [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). The [source manifest](../../sources/batches/B049.json) records hashes, exact labels and manuscript coverage.

Eight selected instruments, one from each manuscript in four two-manuscript families. Full selected arguments and all ten distinct linked Comparator targets were inspected. Antecedent comparisons include exponential covariance, barycentric spanners, restricted Poincare averages, residual perfect sampling, maximum-capacity forests and Boolean compression. References distinguish manuscript versions and theorem numbering.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) test eight local mechanisms using exact finite calculations and explicitly identified numerical checks. They include controls for infeasible scaling, insufficient residual mass and an unsuitable spanning tree.

These are selected-argument extractions, not certification of general-graph matching, polymatroid or contingency-table counting, Courtade-Kumar, or Hellinger claims. The inspected Comparator target statements contain sorry; no Lean solution was built. Scope mismatches for the polymatroid and Hellinger companions are stated explicitly. The fixed edition is unchanged.

Proposed applications are not subsequent results. No independent human review or exhaustive novelty certification is claimed.
