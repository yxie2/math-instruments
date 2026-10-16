# B010: Matroid, packing, string and sampling mechanisms

Extraction date: 2026-10-16. This batch adds 4 previously uncatalogued families, 4 source manuscripts and 9 instruments. The original groups of 17 and 21 families remain together in B001.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000179: Sample/value gluing preserves an expected worst-order guarantee](../../catalog/instruments/MI-000179.md) | 111 |
| [MI-000180: Marked matroid pivots admit a timeline-independent pattern bound](../../catalog/instruments/MI-000180.md) | 111 |
| [MI-000181: One common generator set pays for all layered rank losses](../../catalog/instruments/MI-000181.md) | 111 |
| [MI-000182: Two trees separate individual multiple hits from shared one-hit quotas](../../catalog/instruments/MI-000182.md) | 118 |
| [MI-000183: Scalar packing encodings retain a bounded defect budget through conservation](../../catalog/instruments/MI-000183.md) | 118 |
| [MI-000184: Nearest-mismatch brackets make periodic occurrence lower bounds sound](../../catalog/instruments/MI-000184.md) | 128 |
| [MI-000185: Sorting periodic windows preserves a closed-walk edge multiset](../../catalog/instruments/MI-000185.md) | 128 |
| [MI-000186: Pair-equality projections are dominated by the slice transposition generator](../../catalog/instruments/MI-000186.md) | 131 |
| [MI-000187: An exponentially rare residual branch corrects a rational approximate sampler exactly](../../catalog/instruments/MI-000187.md) | 131 |

## Source and method

The source revision is [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). Its preprint tree is identical to the B001 snapshot; intervening upstream commits changed repository administration. Records give exact manuscript bindings, labelled source passages and SHA-256 hashes in the [source manifest](../../sources/batches/B010.json).

Selection covers nine mechanisms in four algorithmic manuscripts: sample/value simulation, marked-pivot counting and shared rank accounting; competing tree quotas and conservative scalar encodings; forced periodic occurrence counts and ordered layers; slice projection comparison and exact sampling. The selected arguments were read and five Comparator files were compared with their scope documents. Primary antecedents were retrieved for the single-sample reduction, bin-packing encodings, the collapsing superstring framework, Boolean-slice harmonic analysis and approximate-to-perfect sampling. The fire-containment attribution follows the source and bibliographic record; its full antecedent PDF was not retrieved in this batch. Targeted searches do not establish historical priority.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) contain nine groups of finite checks, using exact integer and rational arithmetic except for the slice eigenvalue comparisons. They cover sample gluing, exhaustive marked-pivot interleavings, shared rank charges, small tree phases, all 6,188 five-item subclass multisets, scalar scale separation, label-prefix conservation, periodic occurrence bounds, exact layer edge multisets and rational residual sampling. Negative controls show why expected minima, a common generator set and adequate sampler accuracy matter.

Install [verification-requirements.txt](../verification-requirements.txt), then run `python batches/B010/verification/check_instruments.py` from the repository root. The run used Python 3.13 and NumPy 2.5.4. The small-tree checks do not construct the enormous general trees, and the exact-sampling checks use finite cycle chains rather than certify the source graph-switch bound.

The full matroid competitive proof, packing reduction, superstring connection budget and graph-switch spectral argument were not audited. The exact-sampling principle is explicitly credited to earlier work; its expected-time guarantee is distinguished from a worst-case time bound. No Lean solution was built or kernel-checked.

Potential applications are labelled as proposals. This extraction adds no claim of independent human review or exhaustive novelty certification.
