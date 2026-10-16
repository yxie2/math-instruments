# B022: Uniform arithmetic parameters, entropy and finite obstructions

Extraction date: 2026-10-16. This batch adds 4 previously uncatalogued families, 4 source manuscripts and 8 instruments. The original groups of 17 and 21 families remain together in B001.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000280: Weighted adjacent-block success becomes ordinary gap density](../../catalog/instruments/MI-000280.md) | 026 |
| [MI-000281: A smooth profile with fixed L1 and L2 norms and arbitrarily small first moment](../../catalog/instruments/MI-000281.md) | 026 |
| [MI-000282: One finite field supplies unit-separated spectra and all unit determinant roots](../../catalog/instruments/MI-000282.md) | 027 |
| [MI-000283: Two flags reconstruct through a once-crossing gallery with compatible graded maps](../../catalog/instruments/MI-000283.md) | 027 |
| [MI-000284: Pay a shared conditioning entropy once before averaging sampled coordinates](../../catalog/instruments/MI-000284.md) | 028 |
| [MI-000285: A periodic graph without an infinite path has a finite-cell component bound](../../catalog/instruments/MI-000285.md) | 028 |
| [MI-000286: Extend to a kernel normalizer using unique conjugation implementers](../../catalog/instruments/MI-000286.md) | 031 |
| [MI-000287: Distinct Kummer exponents separate overlapping prime lists simultaneously](../../catalog/instruments/MI-000287.md) | 031 |

## Source and method

The source revision is [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). Its preprint tree is identical to the B001 snapshot; intervening upstream commits changed repository administration. Records give exact manuscript bindings, labelled source passages and SHA-256 hashes in the [source manifest](../../sources/batches/B022.json).

Eight instruments are extracted from four number-theory families. Complete selected arguments were read, with primary antecedent checks for Maynard product profiles, Dirichlet unit finite generation and Chebotarev. Publisher records for Uchida and Vardi were retrieved, but their complete proofs were not independently audited. Three Comparator target statements were inspected; no Lean solution was built.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) give eight check groups.

- Family 026: 500 weighted models, 3,072 exact adjacent-block models and 12 smooth compact profiles. These support the moment and charging mechanisms, not the prime-weight estimates. The actual PrimeGaps Comparator includes the full arbitrary-C gap statement as well as ratio-increase density; its scope note describes only the latter.
- Family 027: ten exact integral cyclotomic inverses and 100 integer flag matrices checked in all five coordinate-order extensions. The fixed field uses unit finite generation; freeness and ambient integrality are kept distinct from stronger claims. The selected Comparator is conditional seam compatibility, not integral-point density.
- Family 028: 90 shared-entropy models and exhaustive period-two/three nearest-neighbor patterns, including 266 finite patterns and their exceptional-vertex components. The finite Gaussian-prime obstruction and coverage schedule remain unaudited.
- Family 031: an order-72 group with a proper kernel normalizer, 1,296 homomorphism checks and five simultaneous power-residue witness primes for overlapping lists. These do not certify Uchida reconstruction, Kummer independence or infinitude. No family-specific formalization scope is listed in the inventory.

The finite checks support selected mechanisms only. They are not global source-theorem certification, and the antecedent comparisons are not exhaustive novelty audits. The immutable import edition is unchanged.

Potential applications are labelled as proposals. This extraction adds no claim of independent human review or exhaustive novelty certification.
