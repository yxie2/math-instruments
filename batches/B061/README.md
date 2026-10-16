# B061: Group-action encodings, idempotent diagrams and unitary incidence

Extraction date: 2026-10-16. This batch adds 4 families, 10 source manuscripts and 10 instruments.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000587: Describe a noninjective mapping torus by its direct limit](../../catalog/instruments/MI-000587.md) | 250 |
| [MI-000588: Encode a group action in a terminating monoid normal form](../../catalog/instruments/MI-000588.md) | 250 |
| [MI-000589: Force prime torsion using linked finite idempotent diagrams](../../catalog/instruments/MI-000589.md) | 250 |
| [MI-000590: Separate positive and null Cartan data by weighted squares](../../catalog/instruments/MI-000590.md) | 254 |
| [MI-000591: Turn stable-length polarization into a character on a centralizer](../../catalog/instruments/MI-000591.md) | 254 |
| [MI-000592: Bound the number of witnesses in an arbitrary intersection by rank descent](../../catalog/instruments/MI-000592.md) | 254 |
| [MI-000593: Compute a weighted cycle phase from its monodromy](../../catalog/instruments/MI-000593.md) | 256 |
| [MI-000594: Force a fixed k-plane by a unitary incidence manifold of degree one](../../catalog/instruments/MI-000594.md) | 256 |
| [MI-000595: Cap a free word before transferring it to a counting current](../../catalog/instruments/MI-000595.md) | 258 |
| [MI-000596: Remove stable kernels before passing from virtually free to free mapping tori](../../catalog/instruments/MI-000596.md) | 258 |

## Source and method

Pinned source revision: [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). The [source manifest](../../sources/batches/B061.json) records hashes, exact labels and manuscript coverage.

Ten instruments from four families and all ten associated manuscripts. Complete selected proofs were read, with direct primary comparisons to Geoghegan-Mihalik-Sapir-Wise, Rodenhausen, Moeller-Paris-Varghese and Klyachko-Thom. All three available scope documents and all seven linked Comparators were read in full.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) contain ten groups: direct-limit stages, confluent action words, idempotent relations, positive/null matrices, centralizer characters, finite intersection witnesses, weighted spectral cycles, fixed-plane tangent calculations, capped free words and stable virtually cyclic kernels.

Classical tools are identified as such. The idempotent diagram depends on cross-copy sums. Centralizer additivity does not require its two arguments to commute with each other. The finite intersection consequence is conditional on pairwise structure. The fixed-plane conclusion rests on an inspected degree argument, not numerical existence tests. No Lean solution was built and no embedding, Artin, group-equation or one-relator headline is certified. The fixed edition is unchanged.

Proposed applications are not subsequent results. No independent human review or exhaustive novelty certification is claimed.
