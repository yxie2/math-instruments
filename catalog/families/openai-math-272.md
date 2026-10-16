---
id: openai-math-272
record_type: family
title: Entanglement, PPT composition and the obstruction to secret key
source_family: '272'
source_collection: openai/math
batch_id: B002
subject: Mathematical physics
source_paper_ids:
- P-000082
instrument_ids:
- MI-000116
- MI-000117
- MI-000118
headline: The source constructs an entangled state on C^10 tensor C^10 with zero distillable key under
  its specified completed-protocol model, and a dimension-21 PPT channel whose square is not entanglement
  breaking.
central_instrument: A four-effect coherence bound, a symmetric/exterior-square rank-loss construction,
  and a trace-preserving channel completion.
novelty_assessment: 'mixed: candidate combinations and an operational inequality; component constructions
  have explicit antecedents'
formalization_summary: Comparator statements inspected for the dimension-ten PPT pair and dimension-21
  channel; the zero-key theorem is outside their scope. No Lean build performed.
statement_faithfulness: The two selected Comparator statements concern PPT composition, not the operational
  zero-key claim.
dependencies: CP/Choi correspondence, PPT stability, product-vector range criterion; the zero-key conclusion
  additionally requires the full-transcript factorization theorem and an explicit algebraic certificate.
antecedents: Unextendible product bases; polynomial constructions of completely entangled subspaces; two-block
  channel switches; flagged trace-preserving extensions.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Entanglement, PPT composition and the obstruction to secret key

## Source manuscript and claim

[Entanglement with zero distillable secret key in local dimension ten](../papers/P-000082.md), by OpenAI, September 27, 2026.

The source constructs an entangled state on C^10 tensor C^10 with zero distillable key under its specified completed-protocol model, and a dimension-21 PPT channel whose square is not entanglement breaking.

## Extracted instruments

- [MI-000116: Four-effect coherence control for two-sided PPT images](../instruments/MI-000116.md)
- [MI-000117: Symmetric and exterior squares turn rank loss into a product-free Choi range](../instruments/MI-000117.md)
- [MI-000118: A two-block switch with an absorbing flag preserves an entangled Choi corner](../instruments/MI-000118.md)

## Dependencies and antecedents

CP/Choi correspondence, PPT stability, product-vector range criterion; the zero-key conclusion additionally requires the full-transcript factorization theorem and an explicit algebraic certificate.

Unextendible product bases; polynomial constructions of completely entangled subspaces; two-block channel switches; flagged trace-preserving extensions. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the three extracted arguments and checked their dimensions, transpose conventions and stated hypotheses. The integer-pencil certificate and the infinite-history protocol theorem were not independently reconstructed. The headline is reported as a source claim, not certified by these checks.

Comparator statements inspected for the dimension-ten PPT pair and dimension-21 channel; the zero-key theorem is outside their scope. No Lean build performed.

The two selected Comparator statements concern PPT composition, not the operational zero-key claim.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/272.md) · [Batch record](../../batches/B002/README.md)
