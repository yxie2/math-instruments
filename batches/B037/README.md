# B037: Formal groups, completion and directed homotopies

Extraction date: 2026-10-16. This batch adds 4 previously uncatalogued families, 4 source manuscripts and 8 instruments. The original groups of 17 and 21 families remain together in B001.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000400: Separate formal coefficients by deep Frobenius roots](../../catalog/instruments/MI-000400.md) | 311 |
| [MI-000401: Use invariant differentials and p-bases to prove formal smoothness](../../catalog/instruments/MI-000401.md) | 311 |
| [MI-000402: Reflect to unique high-dimensional fillers without changing low cells](../../catalog/instruments/MI-000402.md) | 312 |
| [MI-000403: Replace a globular pasting shape by a finite spine of controlled height](../../catalog/instruments/MI-000403.md) | 312 |
| [MI-000404: Kill lim-one by uniformly small corrections in a dense Banach tower](../../catalog/instruments/MI-000404.md) | 313 |
| [MI-000405: Derive finite generation from finite mod-p homotopy and derived completeness](../../catalog/instruments/MI-000405.md) | 313 |
| [MI-000406: Build a relative monotone zigzag through a greatest new element](../../catalog/instruments/MI-000406.md) | 317 |
| [MI-000407: Turn a full sieve cover into an exact Street-nerve union](../../catalog/instruments/MI-000407.md) | 317 |

## Source and method

The source revision is [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). Its preprint tree is identical to the B001 snapshot; intervening upstream commits changed repository administration. Records give exact manuscript bindings, labelled source passages and SHA-256 hashes in the [source manifest](../../sources/batches/B037.json).

Eight selected formal-group and topology interfaces. Read the selected proofs and their required definitions; compare explicit antecedents in Henry-Lanari and Le Bras. Chai bibliographic provenance was found but its author-hosted PDF was inaccessible in this pass.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) contain eight groups.

- 120 finite Puiseux separation models and 12 additive formal-group graph identities.
- Forty underlying globular cutoff models and 100 recursive shapes at five spine levels.
- 480 finite backward-correction steps and 120 finite p-power digit lifts.
- 603 exhaustive small-poset sieve retractions and 17,131 ideal-cover pairs covering 154,679 nondegenerate chains.

The tests do not model arbitrary coherator operations, spectra, infinite-dimensional dense nonsurjective towers, Gray cylinders or higher orientals. Neither chromatic headline theorem nor the two global higher-category theorems is certified. Selected Comparator targets for 312 and 317 contain sorry; their support developments were not fully audited. No listed scope for 311 or 313. No Lean build. Immutable import edition unchanged.

Potential applications are labelled as proposals. This extraction adds no claim of independent human review or exhaustive novelty certification.
