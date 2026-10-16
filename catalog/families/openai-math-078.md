---
id: openai-math-078
record_type: family
title: From small information to product domination with actual retained marginals
source_family: 078
source_collection: openai/math
batch_id: B032
subject: Real and complex analysis
source_paper_ids:
- P-000201
instrument_ids:
- MI-000364
- MI-000365
headline: The source claims the full strict Bochner-Riesz multiplier range in three dimensions.
central_instrument: A likelihood tail converts sublinear relative entropy into pointwise domination after
  removing a small mass. Iterative deletion of low-mass factor values replaces comparison marginals by
  the actual marginals of one common retained law.
novelty_assessment: Likelihood truncation, KL decomposition and density pruning are standard. The simultaneous-marginal
  bookkeeping is a useful finite interface; no global multiplier theorem or first-priority result is certified.
formalization_summary: The pinned release inventory lists no linked formalization scope or Comparator
  for this family. No Lean build was performed.
statement_faithfulness: Small relative entropy compared with a growing scale yields subexponential domination
  after restriction; it does not imply small total variation by itself. The marginal-core constant includes
  the retained mass and counts repeated observations with different reference laws separately.
dependencies: The bound x log(1/x)<=1/e, Markov inequality, KL decomposition into total correlation and
  marginal terms, and a terminating finite deletion procedure.
antecedents: Classical information-density truncation, relative-entropy chain rules and pruning methods.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# From small information to product domination with actual retained marginals

## Source manuscript and claim

[Bochner–Riesz multipliers in three dimensions](../papers/P-000201.md), by OpenAI, September 24, 2026.

The source claims the full strict Bochner-Riesz multiplier range in three dimensions.

## Extracted instruments

- [MI-000364: Convert small information rate into domination after a likelihood truncation](../instruments/MI-000364.md)
- [MI-000365: Replace several product comparison laws by the actual marginals of one retained core](../instruments/MI-000365.md)

## Dependencies and antecedents

The bound x log(1/x)<=1/e, Markov inequality, KL decomposition into total correlation and marginal terms, and a terminating finite deletion procedure.

Classical information-density truncation, relative-entropy chain rules and pruning methods. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete zero-information/product-domination and simultaneous actual-marginal replacement proofs. Projection incidence, characteristic traces, packet repayment and multiplier estimates were not audited.

The pinned release inventory lists no linked formalization scope or Comparator for this family. No Lean build was performed.

Small relative entropy compared with a growing scale yields subexponential domination after restriction; it does not imply small total variation by itself. The marginal-core constant includes the retained mass and counts repeated observations with different reference laws separately.

[Batch record](../../batches/B032/README.md)
