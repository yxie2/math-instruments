# B075: Recomputation, replica information, occupation and directed flux

Extraction date: 2026-10-16. This batch adds 4 families, 8 source manuscripts and 8 instruments.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000702: Measure subset-sum compression by a bounded-difference deficiency](../../catalog/instruments/MI-000702.md) | 138 |
| [MI-000703: Separate task starts, raw matches and reused arrays in prefix recomputation](../../catalog/instruments/MI-000703.md) | 138 |
| [MI-000704: Pay only a root-of-count cost when selecting on one data domain](../../catalog/instruments/MI-000704.md) | 140 |
| [MI-000705: Bound message information by the correlation lost under projection](../../catalog/instruments/MI-000705.md) | 140 |
| [MI-000706: Close endpoint momentum using an invariant graph before differentiating action](../../catalog/instruments/MI-000706.md) | 147 |
| [MI-000707: Control local occupation after stopping above a distant level](../../catalog/instruments/MI-000707.md) | 147 |
| [MI-000708: Trap trajectories on a compact maximum plateau of a finite affine minimum](../../catalog/instruments/MI-000708.md) | 149 |
| [MI-000709: Regroup weighted directed edges into nonnegative level-cut fluxes](../../catalog/instruments/MI-000709.md) | 149 |

## Source and method

Pinned source revision: [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). The [source manifest](../../sources/batches/B075.json) records hashes, exact labels and manuscript coverage.

Eight instruments from four families and eight manuscripts; four regression companions remain inventory-only. Complete selected proofs, the two available scope documents and three Comparators were read. Primary comparisons cover total correlation, posterior resampling and ordered reaction-flux decompositions.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) check support deficiency, prefix recomputation, common-domain selection, replica information, stationary chains, occupation bounds, affine plateaux and directed cut fluxes.

No source Subset Sum exponent, memory-sample lower bound, billiard rigidity or mass-action permanence theorem is certified. Separate Lean solutions were not run; the fixed edition is unchanged.

Proposed applications are not subsequent results. No independent human review or exhaustive novelty certification is claimed.
