# B050: Metric repairs, finite-state reductions and tensor amplification

Extraction date: 2026-10-16. This batch adds 4 families, 8 source manuscripts and 8 instruments.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000496: Mix four parity positions by deleting only two mask permutations](../../catalog/instruments/MI-000496.md) | 117 |
| [MI-000497: Repair squared-distance triangles by integrating local Gaussian kernels](../../catalog/instruments/MI-000497.md) | 117 |
| [MI-000498: Pay for rare radius guesses with disjoint client populations](../../catalog/instruments/MI-000498.md) | 125 |
| [MI-000499: Compress a finite distribution while preserving chosen rational features](../../catalog/instruments/MI-000499.md) | 125 |
| [MI-000500: Pass to a minimal idempotent corner without losing unit lifts](../../catalog/instruments/MI-000500.md) | 129 |
| [MI-000501: Turn deterministic sink reachability into one tree contour tour](../../catalog/instruments/MI-000501.md) | 129 |
| [MI-000502: Replay a linear DAG twice to restore arbitrary borrowed memory](../../catalog/instruments/MI-000502.md) | 130 |
| [MI-000503: Amplify a finite tensor saving by weighting sectors by dimension](../../catalog/instruments/MI-000503.md) | 130 |

## Source and method

Pinned source revision: [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). The [source manifest](../../sources/batches/B050.json) records hashes, exact labels and manuscript coverage.

Eight selected instruments from all eight manuscripts in families 117, 125, 129 and 130. Full selected arguments were read, as were all ten linked Comparator targets. Primary comparisons distinguish Alon-Chung reprint numbering, Schoenberg scanned pages, CGLSS dummy centers, Bayer-Teichmann moments and transparent computation. The unavailable reversible-simulation full text is explicitly marked source-attributed.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) check finite-field masks, triangle repair, population budgets, affine compression, semigroup corners, sink tours, borrowed-memory replay and tensor-sector accounting. Numerical checks and hypothetical recurrence parameters are identified explicitly.

The checks do not certify source hardness, approximation thresholds, automata state lower bounds or Fourier power savings. In particular, a contracting recurrence is not evidence for existence of its finite winning word. No Lean solution was built; the fixed edition is unchanged.

Proposed applications are not subsequent results. No independent human review or exhaustive novelty certification is claimed.
