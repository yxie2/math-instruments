# B058: Incidence moments, polynomial rank budgets and entropy

Extraction date: 2026-10-16. This batch adds 4 families, 8 source manuscripts and 8 instruments.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000562: Use the exact affine incidence variance before any random selection](../../catalog/instruments/MI-000562.md) | 162 |
| [MI-000563: Turn deletion lines into curves and complete an almost-pencil cover](../../catalog/instruments/MI-000563.md) | 162 |
| [MI-000564: Diagonalize an arbitrary node-order pairing on two triangles](../../catalog/instruments/MI-000564.md) | 165 |
| [MI-000565: Charge paired-subspace intersections to polynomial root multiplicity](../../catalog/instruments/MI-000565.md) | 165 |
| [MI-000566: Cancel singleton tails with an exact distinct-pair coupling](../../catalog/instruments/MI-000566.md) | 167 |
| [MI-000567: Predict bounded center tests from a short strict history prefix](../../catalog/instruments/MI-000567.md) | 167 |
| [MI-000568: Gain a logarithm from uniform independent-set occupancy](../../catalog/instruments/MI-000568.md) | 170 |
| [MI-000569: Protect entropy against an arbitrarily biased subsequence selector](../../catalog/instruments/MI-000569.md) | 170 |

## Source and method

Pinned source revision: [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). The [source manifest](../../sources/batches/B058.json) records hashes, exact labels and manuscript coverage.

Eight selected instruments from four families and all eight associated manuscripts. Complete selected proofs were read, with direct primary comparisons to Murphy-Petridis, Guruswami-Kopparty, Ahlswede and Alon. All four scope documents and all nine linked Comparators were read in full.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) contain eight groups: affine moments, cubic coordinates and mixed covers, triangular interpolation, subspace filtrations, off-diagonal pair laws, fresh-test prediction, triangle-free occupancy and selected-tuple entropy.

The source near-pencil theorem and the geometric integrated-overlap identity remain declared dependencies, not conclusions of the finite checks. The arbitrary-pair subspace inequality is distinguished from the inspected structured subspace-design antecedent without claiming proven novelty. No Lean solution was built and no Ryser, crossing-number, planar-distance or Ramsey headline theorem is certified. The fixed edition is unchanged.

Proposed applications are not subsequent results. No independent human review or exhaustive novelty certification is claimed.
