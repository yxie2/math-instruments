# B002: Quantum information, entropy and threshold mechanisms

Extraction date: 2026-10-16. This batch adds 4 previously uncatalogued families, 4 source manuscripts and 9 instruments. The original groups of 17 and 21 families remain together in B001.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000116: Four-effect coherence control for two-sided PPT images](../../catalog/instruments/MI-000116.md) | 272 |
| [MI-000117: Symmetric and exterior squares turn rank loss into a product-free Choi range](../../catalog/instruments/MI-000117.md) | 272 |
| [MI-000118: A two-block switch with an absorbing flag preserves an entangled Choi corner](../../catalog/instruments/MI-000118.md) | 272 |
| [MI-000119: Four diagonal-form comparisons interpolate to a thermal hyperbolic weight](../../catalog/instruments/MI-000119.md) | 273 |
| [MI-000120: Fourth-moment Gibbs regularization supplies seventh-moment control](../../catalog/instruments/MI-000120.md) | 273 |
| [MI-000121: A thermal block decomposition preserves the scalar entropy term](../../catalog/instruments/MI-000121.md) | 276 |
| [MI-000122: Common Kraus columns retain conditional partner entropy](../../catalog/instruments/MI-000122.md) | 276 |
| [MI-000123: A tested-set conditioning budget gives an explicit threshold exponent](../../catalog/instruments/MI-000123.md) | 277 |
| [MI-000124: Reference-state rounding on question-support components](../../catalog/instruments/MI-000124.md) | 277 |

## Source and method

The source revision is [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). Its preprint tree is identical to the B001 snapshot; intervening upstream commits changed repository administration. Records give exact manuscript bindings, labelled source passages and SHA-256 hashes in the [source manifest](../../sources/batches/B002.json).

Selection concentrates on finite-dimensional quantum information and bosonic entropy methods. We read the extracted statements and selected proof steps, compared the supplied formalization scope documents with their Comparator challenge statements, and retrieved the primary antecedents identified on the cards. Targeted searches were supplementary; they were not exhaustive prior-art searches. Existing ingredients are explicitly credited, including the triangular block theorem, product-exclusion arguments, channel switches and classical concentration methods.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) checks selected finite identities and examples; its [results](verification/results.json) state the scope. It does not certify the source theorems. No Lean solution was built or kernel-checked.

From the repository root:

```sh
python -m pip install -r batches/B002/verification/requirements.txt
python batches/B002/verification/check_instruments.py
```

- Family 272: the selected Comparator statements concern PPT compositions; the zero-secret-key theorem is outside their scope.
- Family 273: the selected inequality permits dependence among modes within each of the two independent inputs. The interpolation theorem has explicit test-space hypotheses.
- Family 276: arbitrary-partner additivity is in the manuscript but outside the selected Comparator statement. The common-scalar thermal extension is separated from its cited zero-block antecedent.
- Family 277: the paper states a universal fifth-power threshold rate and a distribution-dependent cubic rate; the selected Comparator states a weaker thirteenth-power rate.

Potential applications are labelled as proposals. This extraction adds no claim of independent human review or exhaustive novelty certification.
