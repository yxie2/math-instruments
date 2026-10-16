# B051: Entropy localization, stationary scales and percolation kernels

Extraction date: 2026-10-16. This batch adds 4 families, 4 source manuscripts and 8 instruments.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000504: Read approximate tree geometry from determinant-one matrix growth](../../catalog/instruments/MI-000504.md) | 146 |
| [MI-000505: Split a positive dilation balance without subtracting infinite masses](../../catalog/instruments/MI-000505.md) | 146 |
| [MI-000506: Localize zero entropy under pointwise attraction](../../catalog/instruments/MI-000506.md) | 151 |
| [MI-000507: Bound radial orbit descriptions by a chain of label vectors](../../catalog/instruments/MI-000507.md) | 151 |
| [MI-000508: Control stationary fluctuations relative to each dyadic block chord](../../catalog/instruments/MI-000508.md) | 152 |
| [MI-000509: Choose scales where a summable cost loses to a divergent test budget](../../catalog/instruments/MI-000509.md) | 152 |
| [MI-000510: Use stabilizer weights to obtain a finite invariant trace](../../catalog/instruments/MI-000510.md) | 214 |
| [MI-000511: Control percolation sprinkling by a positive connection-kernel series](../../catalog/instruments/MI-000511.md) | 214 |

## Source and method

Pinned source revision: [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). The [source manifest](../../sources/batches/B051.json) records hashes, exact labels and manuscript coverage.

Eight selected instruments from families 146, 151, 152 and 214. Full selected proofs and all seven linked Comparator targets were read. Primary comparisons identify Bestvina tree geometry, the classical variational principle, Aldous-Lyons invariant traces and the exact Hutchcroft sprinkling antecedent. The stationary chord formulation has no settled priority claim.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) check matrix comparisons, positive shift balances, entropy coding, monotone itineraries, stationary chord bounds, weighted scale selection, invariant traces and percolation sprinkling. Exact and numerical parts are distinguished.

These checks do not certify standard-map positive entropy, the C1 homology counterexample, the smooth-model obstruction or the general nonuniqueness theorem. The smooth-model formalization target has finite entropy; zero entropy is the stronger manuscript claim. No Lean solution was built; the fixed edition is unchanged.

Proposed applications are not subsequent results. No independent human review or exhaustive novelty certification is claimed.
