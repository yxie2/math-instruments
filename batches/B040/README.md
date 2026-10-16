# B040: Adaptive witnesses, permanent gadgets and dynamic evaluation

Extraction date: 2026-10-16. This batch adds 4 previously uncatalogued families, 4 source manuscripts and 8 instruments. The original groups of 17 and 21 families remain together in B001.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000424: Bound an adaptively selected witness set by posterior likelihood ratios](../../catalog/instruments/MI-000424.md) | 105 |
| [MI-000425: Amplify bilinear anti-concentration without a dimension loss](../../catalog/instruments/MI-000425.md) | 105 |
| [MI-000426: Extract a large influence and bound all moderately large influences from juntas](../../catalog/instruments/MI-000426.md) | 106 |
| [MI-000427: Make subchain coordinate lists local before using a game soundness bound](../../catalog/instruments/MI-000427.md) | 106 |
| [MI-000428: Enforce equality of two matching-edge choices by signed cancellation](../../catalog/instruments/MI-000428.md) | 108 |
| [MI-000429: Select two prescribed diagonal-shift exponents with linear permanent overhead](../../catalog/instruments/MI-000429.md) | 108 |
| [MI-000430: Turn divergent field decisions into polynomial factors](../../catalog/instruments/MI-000430.md) | 142 |
| [MI-000431: Extract a cyclic norm solution from a supplied rank-one idempotent](../../catalog/instruments/MI-000431.md) | 142 |

## Source and method

The source revision is [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). Its preprint tree is identical to the B001 snapshot; intervening upstream commits changed repository administration. Records give exact manuscript bindings, labelled source passages and SHA-256 hashes in the [source manifest](../../sources/batches/B040.json).

Eight selected complexity/algebra interfaces with exact source labels. Selected proofs read completely; primary comparisons identify classical small-bias, junta, signed-gadget and dynamic-evaluation antecedents.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) contain eight groups: 62 exact posterior data tuples, 240 bilinear bias models, 75 product-projection models, 200 list/game models, 64 gadget states, twelve full permanent selectors through order 22, 100 polynomial gcd models and sixty cyclic-field norm models.

These checks do not certify the headline hardness, cubic permanent lower bound or deterministic factorization theorem. The four inspected Comparator files for 105, 106 and 108 have sorry target proofs; 142 has no listed scope. No Lean build. Immutable import edition unchanged.

Potential applications are labelled as proposals. This extraction adds no claim of independent human review or exhaustive novelty certification.
