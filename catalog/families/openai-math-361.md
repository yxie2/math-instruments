---
id: openai-math-361
record_type: family
title: Hopf-weight counting and two-direction eigenvalue splitting
source_family: '361'
source_collection: openai/math
batch_id: B053
subject: Differential geometry
source_paper_ids:
- P-000295
- P-000296
instrument_ids:
- MI-000526
- MI-000527
headline: The sources claim counterexamples to Euclidean integer-degree harmonic-dimension comparison,
  first in even dimension and then in dimension three.
central_instrument: Bihomogeneous polynomial contraction gives exact Hopf-weight multiplicities and a
  beta-binomial law. Unique continuation ensures two independent conformal splitting directions for a
  real eigenfunction pair.
novelty_assessment: Hopf-charge decomposition and conformal spectral transversality are classical. The
  source packages exact counting and parity-compatible splitting for its proposed moving-link constructions.
formalization_summary: The scope describes a dimension-16, degree-50000 example and excludes tangent-cone
  conclusions. The inspected Comparator instead states existential even dimension n>=8 and degree k>=2,
  with complete nonnegative-Ricci geometry and excess independent harmonic functions. It declares MainClaim
  through the axiom mainStatement and derives main from that axiom. This is not an inspected proof, and
  the three-dimensional companion is outside this target. The scope document and every linked Comparator
  were read in full. No solution or Lean project was built.
statement_faithfulness: The multiplicity formula uses s>=2 and adds both charge signs without another
  factor of two. The splitting statement concerns a positive repeated eigenvalue and a real orthonormal
  pair; parity-restricted variations require the pair to have the same parity.
dependencies: Bihomogeneous polynomial dimensions, adjoint contraction, binomial convolution and beta-binomial
  mixing; conformal Dirichlet forms, unique continuation and compressed commutators.
antecedents: Tanno Hopf-charge decomposition; conformal spectral-transversality criteria discussed and
  proved by Greilhuber-Kepplinger with attribution to Besson and earlier work.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Hopf-weight counting and two-direction eigenvalue splitting

## Source manuscripts and claim

- [A counterexample to integer-degree harmonic dimension comparison](../papers/P-000295.md): selected passages extracted.
- [A Three-Dimensional Counterexample to Integer-Degree Harmonic Dimension Comparison](../papers/P-000296.md): selected passages extracted.

The sources claim counterexamples to Euclidean integer-degree harmonic-dimension comparison, first in even dimension and then in dimension three.

## Extracted instruments

- [MI-000526: Identify Hopf-weight multiplicities with a beta-binomial distribution](../instruments/MI-000526.md)
- [MI-000527: Obtain two conformal splitting directions while preserving parity and gauge](../instruments/MI-000527.md)

## Dependencies and antecedents

Bihomogeneous polynomial dimensions, adjoint contraction, binomial convolution and beta-binomial mixing; conformal Dirichlet forms, unique continuation and compressed commutators.

Tanno Hopf-charge decomposition; conformal spectral-transversality criteria discussed and proved by Greilhuber-Kepplinger with attribution to Besson and earlier work.

## Review and formalization scope

Read the full Hopf-weight distribution proof and the complete two-direction splitting proof, including the fixed-area gauge setup. Spectral surplus, transmission matching, radial realization and the claimed global counterexamples remain unverified.

The scope describes a dimension-16, degree-50000 example and excludes tangent-cone conclusions. The inspected Comparator instead states existential even dimension n>=8 and degree k>=2, with complete nonnegative-Ricci geometry and excess independent harmonic functions. It declares MainClaim through the axiom mainStatement and derives main from that axiom. This is not an inspected proof, and the three-dimensional companion is outside this target. The scope document and every linked Comparator were read in full. No solution or Lean project was built.

The multiplicity formula uses s>=2 and adds both charge signs without another factor of two. The splitting statement concerns a positive repeated eigenvalue and a real orthonormal pair; parity-restricted variations require the pair to have the same parity.

[Batch record](../../batches/B053/README.md)
