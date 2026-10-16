# B027: Potential fields, reciprocal kernels and transport obstructions

Extraction date: 2026-10-16. This batch adds 4 previously uncatalogued families, 4 source manuscripts and 8 instruments. The original groups of 17 and 21 families remain together in B001.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000320: Project a compact jump field to a decaying divergence-free field](../../catalog/instruments/MI-000320.md) | 366 |
| [MI-000321: Use harmonic translation and amplitude variation to force an interaction to vanish](../../catalog/instruments/MI-000321.md) | 366 |
| [MI-000322: Regularize a logarithmic Green singularity through a positive-semidefinite defect](../../catalog/instruments/MI-000322.md) | 369 |
| [MI-000323: Preserve reciprocal inertia under current-column updates](../../catalog/instruments/MI-000323.md) | 369 |
| [MI-000324: Pair two potential gradients before estimating a localized virial term](../../catalog/instruments/MI-000324.md) | 370 |
| [MI-000325: Control interval endpoint defects using the sign of midpoint displacement](../../catalog/instruments/MI-000325.md) | 370 |
| [MI-000326: Rule out deterministic branches by testing selected subsets](../../catalog/instruments/MI-000326.md) | 373 |
| [MI-000327: Approximate separated couplings by graph plans with exact cell masses](../../catalog/instruments/MI-000327.md) | 373 |

## Source and method

The source revision is [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). Its preprint tree is identical to the B001 snapshot; intervening upstream commits changed repository administration. Records give exact manuscript bindings, labelled source passages and SHA-256 hashes in the [source manifest](../../sources/batches/B027.json).

Eight instruments from four PDE and transport families. Selected complete proofs were read, with primary comparisons to Agler-McCarthy reciprocal inertia, Qi-Zhang-Li logarithmic means and Colombo-Di Marino equality of transport infima. Three Comparator targets were inspected. These are not certifications of global regularity, hot spots, nonexistence or the Coulomb counterexample.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) contain eight check groups.

- Family 366: an exact unit-circle projection model, 36 exterior harmonic energies and 420 amplitude-polynomial checks. A nonconstant harmonic interaction shows that minimality cannot be omitted.
- Family 369: 220 regularized disk matrices, six scalar mean integrals, 150 column updates and 50 bordered distance matrices. No boundary-kernel limit or global spectral reduction is certified.
- Family 370: an exact weighted divergence identity, 140 paired-kernel sums and 175 interval comparisons. The exact-potential representation and global pressure estimates remain unaudited.
- Family 373: 5,460 deterministic branch assignments, 40 exact cell-mass models and 2,400 separated Coulomb samples. The dual cost certificate and forced optimal support remain unaudited.

The three Comparator files contain sorry target statements; no Lean build was performed. The immutable import edition is unchanged.

Potential applications are labelled as proposals. This extraction adds no claim of independent human review or exhaustive novelty certification.
