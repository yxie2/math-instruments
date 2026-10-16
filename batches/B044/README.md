# B044: Sampling, graph alphabets and exact constraint preservation

Extraction date: 2026-10-16. This batch adds 4 previously uncatalogued families, 4 source manuscripts and 8 instruments. The original groups of 17 and 21 families remain together in B001.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000456: Concentrate reserved sampling roles before adaptive selection](../../catalog/instruments/MI-000456.md) | 136 |
| [MI-000457: Recover replica consensus and mean residual after clipping](../../catalog/instruments/MI-000457.md) | 136 |
| [MI-000458: Encode admissible permutations by independent inversion digits](../../catalog/instruments/MI-000458.md) | 169 |
| [MI-000459: Prove graph-alphabet commutation by switching odd path components](../../catalog/instruments/MI-000459.md) | 169 |
| [MI-000460: Smooth an indefinite second-order operator with small projected negative mass](../../catalog/instruments/MI-000460.md) | 172 |
| [MI-000461: Rationalize a convolution input while retaining exact cancellations and moments](../../catalog/instruments/MI-000461.md) | 172 |
| [MI-000462: Expose returning sweep activity by shifting the rank](../../catalog/instruments/MI-000462.md) | 183 |
| [MI-000463: Turn uniform small packing constants into a fixed exponent saving](../../catalog/instruments/MI-000463.md) | 183 |

## Source and method

The source revision is [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). Its preprint tree is identical to the B001 snapshot; intervening upstream commits changed repository administration. Records give exact manuscript bindings, labelled source passages and SHA-256 hashes in the [source manifest](../../sources/batches/B044.json).

Eight selected mechanisms from complexity, graph alphabets, Euclidean Ramsey theory and planar sweeps. Complete selected proofs read; Shareshian-Wachs Lemma 4.4 and Theorem 4.5 compared directly with the source involution.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) contain eight finite groups: stationary walk variance, clipped consensus, all 64 natural unit interval graphs through five vertices, exact quantum-torus products, indefinite Gaussian differentiation, rational convolution constraints, sampled sweep intervals and fixed-scale recurrence arithmetic.

No PCP, elementary-positivity, Ramsey-classification or halving-line theorem is certified. The ElementaryPositivity, EuclideanRamsey and HalvingLines Comparators were read in full and contain sorry. Six companion Ramsey Comparators were acquired but not inspected. Family 136 has no listed scope. No Lean build. Immutable edition unchanged.

Potential applications are labelled as proposals. This extraction adds no claim of independent human review or exhaustive novelty certification.
