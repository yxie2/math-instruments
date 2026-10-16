# B028: Tensor algebra, finite-type uniqueness and quadratic envelopes

Extraction date: 2026-10-16. This batch adds 4 previously uncatalogued families, 4 source manuscripts and 8 instruments. The original groups of 17 and 21 families remain together in B001.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000328: Certify tensor Gram blocks using integer-scaled orthogonal projections](../../catalog/instruments/MI-000328.md) | 367 |
| [MI-000329: Retain trace-free structure to obtain sharp five-dimensional contraction constants](../../catalog/instruments/MI-000329.md) | 367 |
| [MI-000330: Resolve null-conic polarizations with an explicit nonsplit quotient sequence](../../catalog/instruments/MI-000330.md) | 372 |
| [MI-000331: Close a Hessian equation on the gradient and scalar trace ambiguity](../../catalog/instruments/MI-000331.md) | 372 |
| [MI-000332: Use an inverse profile to turn stability into a weighted defect inequality](../../catalog/instruments/MI-000332.md) | 375 |
| [MI-000333: Push overlapping lifted tests down by their Euclidean norm](../../catalog/instruments/MI-000333.md) | 375 |
| [MI-000334: Add an explicit correction when moving a quadratic-envelope center](../../catalog/instruments/MI-000334.md) | 377 |
| [MI-000335: Enforce a barycenter while optimizing a variance-penalized envelope](../../catalog/instruments/MI-000335.md) | 377 |

## Source and method

The source revision is [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). Its preprint tree is identical to the B001 snapshot; intervening upstream commits changed repository administration. Records give exact manuscript bindings, labelled source passages and SHA-256 hashes in the [source manifest](../../sources/batches/B028.json).

Eight selected algebraic and variational mechanisms from four PDE families. Complete proofs of the selected lemmas were read, with primary comparisons to Liu-Luo-Wang-Wei-Wei-Wu Lemma 2.1 and Evans-Savin quadratic slice comparisons. Two Comparator targets were inspected. Global PDE classifications are not certified.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) contain eight groups.

- Family 367: four exact full tensor projection matrices of sizes 25 and 125; 200 normalized tensor examples and exact sharp constants. The large coefficient tables and universal certificate are not verified.
- Family 372: exact null-conic and quotient formulas, 48 projective frames, 240 prolonged-system coefficient checks and an exact variable-coefficient solution. The analytic transport matching remains unaudited.
- Family 375: symbolic inverse-profile and ground-state identities, 160 rational overlap-variance models and the normal Jacobian identity. The source high-dimensional rigidity argument remains unaudited.
- Family 377: symbolic envelope cost and moving-center Hessian identities, 100 exact semigroup examples, 60 finite-support primal-dual programs and 45 exact continuum envelope examples. No contact propagation or Liouville theorem is certified.

The Bernoulli Comparator covers only existence in dimension seven, not classification through dimension six. Both Comparator files contain sorry target statements; no Lean build was performed. The immutable import edition is unchanged.

Potential applications are labelled as proposals. This extraction adds no claim of independent human review or exhaustive novelty certification.
