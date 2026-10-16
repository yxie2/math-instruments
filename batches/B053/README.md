# B053: Geometric error estimates, covering maps and spectral control

Extraction date: 2026-10-16. This batch adds 4 families, 6 source manuscripts and 8 instruments.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000520: Preserve smallness of a particular error through a Neumann correction](../../catalog/instruments/MI-000520.md) | 352 |
| [MI-000521: Gain short-time spatial smallness by lowering the Holder exponent](../../catalog/instruments/MI-000521.md) | 352 |
| [MI-000522: Absorb delayed Gaussian errors on every finite energy prefix](../../catalog/instruments/MI-000522.md) | 355 |
| [MI-000523: Convert exponentially close stopped approximants into all-orders Gevrey bounds](../../catalog/instruments/MI-000523.md) | 355 |
| [MI-000524: Globalize a locally injective map through its homotopy class](../../catalog/instruments/MI-000524.md) | 360 |
| [MI-000525: Recover the missing determinant direction after an oblique projection](../../catalog/instruments/MI-000525.md) | 360 |
| [MI-000526: Identify Hopf-weight multiplicities with a beta-binomial distribution](../../catalog/instruments/MI-000526.md) | 361 |
| [MI-000527: Obtain two conformal splitting directions while preserving parity and gauge](../../catalog/instruments/MI-000527.md) | 361 |

## Source and method

Pinned source revision: [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). The [source manifest](../../sources/batches/B053.json) records hashes, exact labels and manuscript coverage.

Eight selected instruments from four families and six source manuscripts. Selected arguments were read in full, with targeted comparisons to Colding-Minicozzi, the Ramis-Sibuya statement recalled by Lastra-Malek, Hatcher, Tanno and Greilhuber-Kepplinger. Both available scope documents and all three linked Comparators were inspected.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) test particular-error correction, short-time interpolation, delayed-radius summation, Gevrey telescoping, finite covering indices, determinant gains, Hopf multiplicities and conformal splitting. The covering-space theorem and infinite-dimensional steps also require the stated analytic arguments.

The harmonic-growth Comparator invokes an explicit axiom. Its target is existential in even dimension and does not cover the three-dimensional companion. No source singularity, tangent uniqueness, optimal-transport or harmonic-dimension headline theorem is certified. No Lean solution was built; the fixed edition is unchanged.

Proposed applications are not subsequent results. No independent human review or exhaustive novelty certification is claimed.
