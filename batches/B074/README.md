# B074: Coefficient descent, trace smoothing, parity lifts and finite corrections

Extraction date: 2026-10-16. This batch adds 4 families, 8 source manuscripts and 8 instruments.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000694: Preserve a nonzero matrix evaluation through a finite coefficient ring](../../catalog/instruments/MI-000694.md) | 116 |
| [MI-000695: Convert formal integration coefficients into a nonzero first column](../../catalog/instruments/MI-000695.md) | 116 |
| [MI-000696: Keep a product uniformly inside the Cayley half-plane](../../catalog/instruments/MI-000696.md) | 122 |
| [MI-000697: Amplify adjacent-power overlap by hiding labels in a fixed-count schedule](../../catalog/instruments/MI-000697.md) | 122 |
| [MI-000698: Compare parity lifts by binary solvability and expose a dual witness](../../catalog/instruments/MI-000698.md) | 133 |
| [MI-000699: Recover vertex potentials from a vanishing cyclic sum](../../catalog/instruments/MI-000699.md) | 133 |
| [MI-000700: Compile deterministic episode updates from universally sound splits](../../catalog/instruments/MI-000700.md) | 134 |
| [MI-000701: Choose one affine correction that hides a coordinate on every input](../../catalog/instruments/MI-000701.md) | 134 |

## Source and method

Pinned source revision: [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). The [source manifest](../../sources/batches/B074.json) records hashes, exact labels and manuscript coverage.

Eight instruments from four families and eight selected manuscripts; five companions remain inventory-only. Complete selected proofs, four scope documents and five Comparators were read. Primary comparisons cover parity-lift duality and the original local-lemma estimate.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) check finite coefficient descent, integration jets, damped products, hypergeometric smoothing, parity lifts, cycle potentials, split expressions and affine corrections.

No source hitting theorem, trace-reconstruction bound, WL complexity result or uniform star-height theorem is certified. Separate Lean solutions were not run; the fixed edition is unchanged.

Proposed applications are not subsequent results. No independent human review or exhaustive novelty certification is claimed.
