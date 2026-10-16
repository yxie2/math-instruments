---
id: openai-math-038
record_type: family
title: Uniform restriction growth and rational supporting profiles
source_family: 038
source_collection: openai/math
batch_id: B026
subject: Algebraic and complex geometry
source_paper_ids:
- P-000175
instrument_ids:
- MI-000312
- MI-000313
headline: The source claims that K_X+(n+1)L is globally generated for every ample line bundle L on a smooth
  projective complex n-fold, with n>=1.
central_instrument: A fixed number of independent generic-fiber values gives a lower bound uniform over
  all integral subvarieties. Rational approximation inside minimal faces preserves both polytope incidences
  and supporting inequalities.
novelty_assessment: Finite projection, interpolation and rational-face approximation are classical. The
  source supplies a uniform restriction-image estimate and an incidence-preserving support lemma. No exhaustive
  novelty or global Fujita proof certification is claimed.
formalization_summary: No family-specific scope document or Comparator target is listed for this family.
  No Lean artifact was built or kernel-checked.
statement_faithfulness: Global generation is not very ampleness. Restriction images are bounded below
  without assuming restriction surjectivity. Rationalizing a profile and its support functional independently
  can destroy their equality and incidence constraints.
dependencies: A very ample multiple, finite separable projection, point interpolation, multiplication
  in an integral coordinate ring, rational polytope faces and density of rational points.
antecedents: Classical projective projection and Hilbert-function methods; rational polyhedral geometry.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Uniform restriction growth and rational supporting profiles

## Source manuscript and claim

[Fujita's freeness conjecture](../papers/P-000175.md), by OpenAI, September 23, 2026.

The source claims that K_X+(n+1)L is globally generated for every ample line bundle L on a smooth projective complex n-fold, with n>=1.

## Extracted instruments

- [MI-000312: Bound restriction images uniformly using only a fixed part of the generic fiber](../instruments/MI-000312.md)
- [MI-000313: Rationalize a supporting profile without changing which polytopes contain it](../instruments/MI-000313.md)

## Dependencies and antecedents

A very ample multiple, finite separable projection, point interpolation, multiplication in an integral coordinate ring, rational polytope faces and density of rational points.

Classical projective projection and Hilbert-function methods; rational polyhedral geometry. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete uniform-restriction and rational-support proofs and their surrounding definitions. The exponential minimizer, elimination of positive-dimensional centers and final adjoint lifting were not audited.

No family-specific scope document or Comparator target is listed for this family. No Lean artifact was built or kernel-checked.

Global generation is not very ampleness. Restriction images are bounded below without assuming restriction surjectivity. Rationalizing a profile and its support functional independently can destroy their equality and incidence constraints.

[Batch record](../../batches/B026/README.md)
