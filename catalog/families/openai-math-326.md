---
id: openai-math-326
record_type: family
title: Moment lifts and compact domains under ordinary approximation
source_family: '326'
source_collection: openai/math
batch_id: B008
subject: Functional analysis
source_paper_ids:
- P-000104
instrument_ids:
- MI-000163
- MI-000164
headline: The source claims that a nonzero real Banach space with the ordinary approximation property
  is K-convex exactly when it and its dual have finite cotype, with possibly different finite exponents.
central_instrument: Cotype on a dual gives bounded sign-indexed moment lifts. Nested finite-dimensional
  spaces and a dyadic shift turn those lifts into a compact factorization with a controlled fixed-length
  dual moment constant.
novelty_assessment: Kahane comparison, Hahn-Banach and quotient duality are established. The compact domain
  retaining dual moment control is the selected candidate source-specific construction. The scalar Fourier-rank
  mechanism and full characterization are not certified here.
formalization_summary: Cotype.lean defines ordinary approximation on compact sets, finite Rademacher cotype
  and the finite-cube Rademacher projection, and states the equivalence for nonzero real Banach spaces.
  The scope document and Comparator declarations were compared. No Lean solution was built or kernel-checked,
  and the auxiliary instruments are not separate Comparator targets.
statement_faithfulness: Ordinary AP does not supply uniformly bounded approximating operators. Cotype
  does not generally pass from X* to the quotient E*. The constructed domain depends on a fixed tuple
  length m and the finite-dimensional subspace E; its estimate is not a uniform all-length cotype assertion.
dependencies: Fixed-length cotype constants; Kahane L1-L2 comparison; quotient norms and Hahn-Banach;
  finite nets with exact moment correction; dyadically weighted Hilbert sums; a quotient by the kernel
  of a compact map; AP on one compact image.
antecedents: Maurey-Pisier and Pisier supply the classical type, cotype and K-convexity background. Pisier’s
  earlier approximation results and Gupta-Misra-Ray’s tensor-norm formulation motivate the source. The
  elementary moment-lifting tools are credited separately from its compact construction.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Moment lifts and compact domains under ordinary approximation

## Source manuscript and claim

[The cotype–cotype conjecture under the approximation property](../papers/P-000104.md), by OpenAI, September 23, 2026.

The source claims that a nonzero real Banach space with the ordinary approximation property is K-convex exactly when it and its dual have finite cotype, with possibly different finite exponents.

## Extracted instruments

- [MI-000163: Dual cotype gives bounded sign-indexed lifts with prescribed moments](../instruments/MI-000163.md)
- [MI-000164: A dyadic compact domain preserves fixed-length dual moments](../instruments/MI-000164.md)

## Dependencies and antecedents

Fixed-length cotype constants; Kahane L1-L2 comparison; quotient norms and Hahn-Banach; finite nets with exact moment correction; dyadically weighted Hilbert sums; a quotient by the kernel of a compact map; AP on one compact image.

Maurey-Pisier and Pisier supply the classical type, cotype and K-convexity background. Pisier’s earlier approximation results and Gupta-Misra-Ray’s tensor-norm formulation motivate the source. The elementary moment-lifting tools are credited separately from its compact construction. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the moment comparison and lifting proofs, the full compact-domain construction and the AP transfer to compact composites. The scalar rank-two coefficient lemma and the uniform Walsh-decay proof were not fully audited.

Cotype.lean defines ordinary approximation on compact sets, finite Rademacher cotype and the finite-cube Rademacher projection, and states the equivalence for nonzero real Banach spaces. The scope document and Comparator declarations were compared. No Lean solution was built or kernel-checked, and the auxiliary instruments are not separate Comparator targets.

Ordinary AP does not supply uniformly bounded approximating operators. Cotype does not generally pass from X* to the quotient E*. The constructed domain depends on a fixed tuple length m and the finite-dimensional subspace E; its estimate is not a uniform all-length cotype assertion.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/326.md) · [Batch record](../../batches/B008/README.md)
