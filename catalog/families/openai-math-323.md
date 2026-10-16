---
id: openai-math-323
record_type: family
title: Evaluation criteria for quotients and small restrictions
source_family: '323'
source_collection: openai/math
batch_id: B043
subject: Functional analysis
source_paper_ids:
- P-000245
instrument_ids:
- MI-000452
- MI-000453
headline: The source claims relative independence of the separable quotient problem.
central_instrument: Norm separability of an evaluation image is equivalent to a separable infinite-dimensional
  quotient. Strict singularity yields a whole infinite-dimensional subspace of small operator norm by
  a controlled basic sequence.
novelty_assessment: The proofs use classical basic-sequence, duality and strictly singular operator methods.
  No novelty certification of either the abstract tools or independence theorem.
formalization_summary: Read SeparableQuotientNegative.lean in full and the scope document. The negative_main
  target has sorry and covers the CH negative assertion over R and C. Positive consistency is outside
  that target. No Lean build.
statement_faithfulness: The evaluation image must be norm separable, not merely weak-star separable. Small
  restrictions require a controlled basic sequence, not just individually small vectors.
dependencies: Finite half-norming sets, annihilator induction, bounded coordinate functionals, Hahn-Banach
  separation and residual-halving surjectivity.
antecedents: Classical Banach-space quotient duality and strictly singular operator basic-sequence arguments.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Evaluation criteria for quotients and small restrictions

## Source manuscript and claim

[Relative independence of the separable quotient problem](../papers/P-000245.md), by OpenAI, September 23, 2026.

The source claims relative independence of the separable quotient problem.

## Extracted instruments

- [MI-000452: Recognize separable quotients from a norm-separable evaluation image](../instruments/MI-000452.md)
- [MI-000453: Upgrade strict singularity to a uniformly small restriction](../instruments/MI-000453.md)

## Dependencies and antecedents

Finite half-norming sets, annihilator induction, bounded coordinate functionals, Hahn-Banach separation and residual-halving surjectivity.

Classical Banach-space quotient duality and strictly singular operator basic-sequence arguments. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete evaluation section, including the prefix lemma, criterion and small-restriction proof. Neither the CH construction nor positive consistency proof was audited.

Read SeparableQuotientNegative.lean in full and the scope document. The negative_main target has sorry and covers the CH negative assertion over R and C. Positive consistency is outside that target. No Lean build.

The evaluation image must be norm separable, not merely weak-star separable. Small restrictions require a controlled basic sequence, not just individually small vectors.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/323.md) · [Batch record](../../batches/B043/README.md)
