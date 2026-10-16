# B036: Combinatorial constraints and algebraic isolation

Extraction date: 2026-10-16. This batch adds 4 previously uncatalogued families, 4 source manuscripts and 8 instruments. The original groups of 17 and 21 families remain together in B001.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000392: Propagate an affine shadow from a clean four-by-four square](../../catalog/instruments/MI-000392.md) | 155 |
| [MI-000393: Stack common tiling equations using a full-difference cyclic partition](../../catalog/instruments/MI-000393.md) | 155 |
| [MI-000394: Turn near-integral samples into exact repeated-root divisibility](../../catalog/instruments/MI-000394.md) | 164 |
| [MI-000395: Choose monochromatic product blocks with ordered tails and pivots](../../catalog/instruments/MI-000395.md) | 164 |
| [MI-000396: Build exact defining equations from squared-distance separators](../../catalog/instruments/MI-000396.md) | 166 |
| [MI-000397: Separate isolated singular points using a local Artin determinant](../../catalog/instruments/MI-000397.md) | 166 |
| [MI-000398: Recover a free full-rank lattice from height-one localizations](../../catalog/instruments/MI-000398.md) | 168 |
| [MI-000399: Reduce a restriction kernel modulo a regular transverse label](../../catalog/instruments/MI-000399.md) | 168 |

## Source and method

The source revision is [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). Its preprint tree is identical to the B001 snapshot; intervening upstream commits changed repository administration. Records give exact manuscript bindings, labelled source passages and SHA-256 hashes in the [source manifest](../../sources/batches/B036.json).

Eight selected mechanisms from four combinatorial families. Read the selected affine-shadow, stacking, rational-interpolation, product-chain and polynomial-toolkit proofs, plus the selected lattice and saturation arguments. Targeted primary comparisons identify explicit classical antecedents.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) contain eight groups.

- Affine-square constraints over five prime fields and two clean-square count bounds.
- Forty-eight finite stacking models, decoding all 385 exact-cover complements.
- Nine exact near-integral interpolation models and sixteen conditional product-chain models.
- Three exact distance-separator zero sets, nonreduced and positive-dimensional interpolation examples, and first jets.
- Eighty rational-coordinate lattice models, 120 saturation models and negative controls for missing hypotheses.

These checks cover selected finite interfaces. They do not certify dimension-three aperiodicity, the integer sums-and-products theorem, the global distinct-distance theorem or combinatorial invariance. The tiling and KL Comparator targets contain sorry; families 164 and 166 have no listed scope document. No Lean build. Immutable import edition unchanged.

Potential applications are labelled as proposals. This extraction adds no claim of independent human review or exhaustive novelty certification.
