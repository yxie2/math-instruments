# B070: Cycle ranks, finite covers, Liouville arguments and integral residues

Extraction date: 2026-10-16. This batch adds 4 families, 8 source manuscripts and 8 instruments.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000662: Count birational contractions by losses of analytic cycle classes](../../catalog/instruments/MI-000662.md) | 056 |
| [MI-000663: Bound a local difficulty deficit by the number of varying branches](../../catalog/instruments/MI-000663.md) | 056 |
| [MI-000664: Extend a finite cover of a normal subgroup across a lattice quotient](../../catalog/instruments/MI-000664.md) | 057 |
| [MI-000665: Recover a differential line from ratios of sections](../../catalog/instruments/MI-000665.md) | 057 |
| [MI-000666: Kill an abelian deck character by integrating the logarithmic energy](../../catalog/instruments/MI-000666.md) | 058 |
| [MI-000667: Propagate uniform local compactness to properness of a disc-chain distance](../../catalog/instruments/MI-000667.md) | 058 |
| [MI-000668: Lift squares and two-square representations in a finite odd-adic algebra](../../catalog/instruments/MI-000668.md) | 059 |
| [MI-000669: Recover an integral lattice from projection-transfer residues](../../catalog/instruments/MI-000669.md) | 059 |

## Source and method

Pinned source revision: [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). The [source manifest](../../sources/batches/B070.json) records hashes, exact labels and manuscript coverage.

Eight instruments from four families and eight selected manuscripts. Four companions remain inventory-only. Complete selected proofs, one scope document and its Comparator were read. Primary comparisons include weighted difficulty, Lyons-Sullivan Liouville theory and Hensel lifting.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) check cycle-rank models, branch rounding, finite-kernel covers, exterior algebra, discrete character energy, intrinsic-distance budgets, odd-adic lifting and integral lattice residues.

The lattice extraction is explicitly conditional on the source exact-sequence and signed Bockstein inputs. None of the source termination, abelianity, cover classification, symmetry or multiplicity-counterexample headlines is certified. No separate Lean solution was built. The fixed edition is unchanged.

Proposed applications are not subsequent results. No independent human review or exhaustive novelty certification is claimed.
