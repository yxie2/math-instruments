# B078: Quenched coupling, Gaussian replicas and finite random-cluster identities

Extraction date: 2026-10-16. This batch adds 4 families, 4 source manuscripts and 8 instruments.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000726: Glue conditional order couplings without changing the quenched reference marginal](../../catalog/instruments/MI-000726.md) | 218 |
| [MI-000727: Sum geometrically weighted scale errors without assuming a summable perturbation](../../catalog/instruments/MI-000727.md) | 218 |
| [MI-000728: Transfer path events using unused departure rows](../../catalog/instruments/MI-000728.md) | 220 |
| [MI-000729: Escape a finite directional slab using strict ellipticity alone](../../catalog/instruments/MI-000729.md) | 220 |
| [MI-000730: Replace Gibbs denominators by additional replicas to pass array limits](../../catalog/instruments/MI-000730.md) | 222 |
| [MI-000731: Differentiate Gaussian Gibbs observables with the correct replica diagonals](../../catalog/instruments/MI-000731.md) | 222 |
| [MI-000732: Condition random-cluster edges while retaining physical connectivity conventions](../../catalog/instruments/MI-000732.md) | 223 |
| [MI-000733: Recover loop positivity and planar dual odds directly from Euler identities](../../catalog/instruments/MI-000733.md) | 223 |

## Source and method

Pinned source revision: [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). The [source manifest](../../sources/batches/B078.json) records hashes, exact labels and manuscript coverage.

Eight instruments from four families and four manuscripts; fifteen companions remain inventory-only. Complete selected finite proofs, three scope documents and three named Comparators were read. Primary comparisons cover strictly elliptic slab escape, Gaussian interpolation and finite random-cluster identities.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) check conditional coupling, weighted scale errors, departure-row factorization, repeated trials, bounded array reweighting, Gaussian replica derivatives, random-cluster conditioning and planar loop duality.

No SLE limit, directional zero-one theorem, perceptron free-energy formula or critical-point assertion is certified. No separate Lean solution was built; the fixed edition is unchanged.

Proposed applications are not subsequent results. No independent human review or exhaustive novelty certification is claimed.
