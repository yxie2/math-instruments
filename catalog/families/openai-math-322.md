---
id: openai-math-322
record_type: family
title: Support propagation and compact parameter errors in sphere geometry
source_family: '322'
source_collection: openai/math
batch_id: B008
subject: Functional analysis
source_paper_ids:
- P-000103
instrument_ids:
- MI-000162
headline: The source claims that every surjective isometry between unit spheres of nonzero real Banach
  spaces has a unique surjective real-linear isometric extension. The selected mechanism constructs a
  convex invariant set of extremal directions and applies a classical fixed-point theorem.
central_instrument: Common supports preserve an extremal set under carefully chosen convex hulls; finitely
  many bounded scalar parameters turn a return-map estimate into contraction of the Kuratowski measure
  of noncompactness.
novelty_assessment: Supporting functionals, ultrapowers and Darbo fixed points are established. The selected
  source-specific combination is the invariant extremal set and its scalar-parameter contraction estimate.
  The full sphere-isometry result and priority are not certified.
formalization_summary: TingleySphereIsometry.lean states the radial formula, real-linear isometric extension,
  surjectivity and uniqueness for arbitrary nonzero real Banach spaces. The scope document and Comparator
  declarations were compared. No Lean solution was built or kernel-checked, and the auxiliary instruments
  are not separate Comparator targets.
statement_faithfulness: No finite-dimensionality, separability, smoothness, strict convexity or reflexivity
  is assumed. For complex spaces viewed as real spaces the conclusion is real linearity, not complex linearity.
  The constructed invariant set is separable even when the ambient spaces are not.
dependencies: Hahn-Banach supports; continuous radial contact from an interior point; an attained positive
  defect, obtained in the source by an ultrapower; a closed extremal set; finite partitions of bounded
  radius parameters; Darbo contraction of noncompactness.
antecedents: Darbo supplies the fixed-point theorem and Dacunha-Castelle the Banach ultrapower background.
  Facial approaches to Tingley’s problem and the Mazur-Ulam theorem are prior methods, not new results
  of this extraction.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Support propagation and compact parameter errors in sphere geometry

## Source manuscript and claim

[A positive solution to Tingley’s problem](../papers/P-000103.md), by OpenAI, September 23, 2026.

The source claims that every surjective isometry between unit spheres of nonzero real Banach spaces has a unique surjective real-linear isometric extension. The selected mechanism constructs a convex invariant set of extremal directions and applies a classical fixed-point theorem.

## Extracted instruments

- [MI-000162: Support propagation creates an invariant convex set for a condensing map](../instruments/MI-000162.md)

## Dependencies and antecedents

Hahn-Banach supports; continuous radial contact from an interior point; an attained positive defect, obtained in the source by an ultrapower; a closed extremal set; finite partitions of bounded radius parameters; Darbo contraction of noncompactness.

Darbo supplies the fixed-point theorem and Dacunha-Castelle the Banach ultrapower background. Facial approaches to Tingley’s problem and the Mazur-Ulam theorem are prior methods, not new results of this extraction. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the source’s support, radial-contact, defect-attainment, invariant-set and noncompactness arguments, its chord comparison, and the fixed-point appendix. The card isolates the invariant-set mechanism; finite tests do not certify the universal sphere-isometry conclusion.

TingleySphereIsometry.lean states the radial formula, real-linear isometric extension, surjectivity and uniqueness for arbitrary nonzero real Banach spaces. The scope document and Comparator declarations were compared. No Lean solution was built or kernel-checked, and the auxiliary instruments are not separate Comparator targets.

No finite-dimensionality, separability, smoothness, strict convexity or reflexivity is assumed. For complex spaces viewed as real spaces the conclusion is real linearity, not complex linearity. The constructed invariant set is separable even when the ambient spaces are not.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/322.md) · [Batch record](../../batches/B008/README.md)
