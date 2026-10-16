---
id: openai-math-299
record_type: family
title: Algebraic tensor independence and representation-resistant labels
source_family: '299'
source_collection: openai/math
batch_id: B034
subject: Operator algebras
source_paper_ids:
- P-000209
instrument_ids:
- MI-000380
- MI-000381
headline: The source claims the Kirchberg-Rordam character criterion and Jiang-Su absorption for infinite
  tensor powers of characterless algebras.
central_instrument: A support-projection argument proves algebraic tensor independence of commuting factors.
  A real incidence construction builds tensor labels independent under all rank-two quotient maps.
novelty_assessment: Factor independence and incidence avoidance are classical mechanisms. The selected
  conjunction is useful for representation-uniform constructions; no priority or global absorption certification.
formalization_summary: 'Inspected the central-algebra definition and final CharacterCriterion.lean target:
  no nonzero characters is equivalent to Jiang-Su absorption for a nonzero unital separable C*-algebra
  and a free ultrafilter. The target contains sorry. The long supporting construction was not audited
  or built.'
statement_faithfulness: The multiplication conclusion is for the algebraic tensor product, not an assertion
  that every representation is spatial. Real tensor labels use selfadjoint inputs to preserve independence
  after complexification.
dependencies: Weakly closed left ideals, support projections, factor centers, commutator ideals, Sard
  and complexification of real selfadjoint spaces.
antecedents: Classical factor and incidence methods; no first-priority claim.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Algebraic tensor independence and representation-resistant labels

## Source manuscript and claim

[The Kirchberg–Rørdam character criterion](../papers/P-000209.md), by OpenAI, September 25, 2026.

The source claims the Kirchberg-Rordam character criterion and Jiang-Su absorption for infinite tensor powers of characterless algebras.

## Extracted instruments

- [MI-000380: Prove algebraic tensor independence using a central support projection](../instruments/MI-000380.md)
- [MI-000381: Choose tensor labels that remain independent under every rank-two quotient](../instruments/MI-000381.md)

## Dependencies and antecedents

Weakly closed left ideals, support projections, factor centers, commutator ideals, Sard and complexification of real selfadjoint spaces.

Classical factor and incidence methods; no first-priority claim. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete factor-independence, grouped-factor, detecting-space, real-label and represented-label arguments. The full square-zero element and dimension-drop constructions were not audited.

Inspected the central-algebra definition and final CharacterCriterion.lean target: no nonzero characters is equivalent to Jiang-Su absorption for a nonzero unital separable C*-algebra and a free ultrafilter. The target contains sorry. The long supporting construction was not audited or built.

The multiplication conclusion is for the algebraic tensor product, not an assertion that every representation is spatial. Real tensor labels use selfadjoint inputs to preserve independence after complexification.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/299.md) · [Batch record](../../batches/B034/README.md)
