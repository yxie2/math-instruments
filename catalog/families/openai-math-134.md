---
id: openai-math-134
record_type: family
title: Sound split expressions and affine corrections
source_family: '134'
source_collection: openai/math
batch_id: B074
subject: Theoretical computer science
source_paper_ids:
- P-000469
- P-000470
instrument_ids:
- MI-000700
- MI-000701
headline: The family claims uniform generalized star-height bounds, including bounds thirteen, four and
  three.
central_instrument: Universally sound prefix/suffix tests compile deterministic updates; the local lemma
  chooses one correction with a constant coordinate line for every input state.
novelty_assessment: Established mechanisms and directly checked antecedents are identified below. No exhaustive
  novelty determination or source headline certification is claimed.
formalization_summary: Read the scope and complete GeneralizedStarHeight Comparator. It targets height
  at most three for every regular language over its original finite alphabet, with complement in the same
  free monoid. This common target is stronger than the bounds thirteen and four of the two selected manuscripts.
  The inspected theorem targets contain sorry; no separate solution or Lean build was checked.
statement_faithfulness: Every independently successful prefix/suffix pair must be sound on the actual
  word. The correction is fixed before the input state and tuple; only the successful coordinate may depend
  on them. Finite existence does not imply efficient computation.
dependencies: Prefix codes, finite graph languages, affine maps, independent finite random variables and
  the Lovasz local lemma.
antecedents: Classical regular-expression composition, affine recovery and the Erdos-Lovasz local lemma.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Sound split expressions and affine corrections

## Source manuscripts and claim

- [Finite Monoid Computations and a Uniform Generalized Star-Height Bound](../papers/P-000469.md): selected passages extracted.
- [Generalized Star Height at Most Four](../papers/P-000470.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [Generalized Star Height at Most Three](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Generalized-Star-Height-at-Most-Three-September-25-2026)

The family claims uniform generalized star-height bounds, including bounds thirteen, four and three.

## Extracted instruments

- [MI-000700: Compile deterministic episode updates from universally sound splits](../instruments/MI-000700.md)
- [MI-000701: Choose one affine correction that hides a coordinate on every input](../instruments/MI-000701.md)

## Dependencies and antecedents

Prefix codes, finite graph languages, affine maps, independent finite random variables and the Lovasz local lemma.

Classical regular-expression composition, affine recovery and the Erdos-Lovasz local lemma.

## Review and formalization scope

Read the complete split identity, affine recovery and homogeneous-lift discussion in the finite-monoid manuscript, and the full affine-line constancy proof and finite-choice remark in the height-four manuscript. Two of three manuscripts receive extractions; the height-three manuscript remains inventory-only. Marker geometry, end guards and full language-height bounds are not certified.

Read the scope and complete GeneralizedStarHeight Comparator. It targets height at most three for every regular language over its original finite alphabet, with complement in the same free monoid. This common target is stronger than the bounds thirteen and four of the two selected manuscripts. The inspected theorem targets contain sorry; no separate solution or Lean build was checked.

Every independently successful prefix/suffix pair must be sound on the actual word. The correction is fixed before the input state and tuple; only the successful coordinate may depend on them. Finite existence does not imply efficient computation.

[Batch record](../../batches/B074/README.md)
