---
id: openai-math-082
record_type: family
title: Supported matrix costs and dyadic energy increments
source_family: 082
source_collection: openai/math
batch_id: B072
subject: Real and complex analysis
source_paper_ids:
- P-000447
- P-000448
instrument_ids:
- MI-000678
- MI-000679
headline: The family claims full annular variation, a dyadic absolute bound and a maximal bound for triangular
  Hilbert forms.
central_instrument: A square-root Hessian cost is jointly convex under averaging; a parity-constrained
  four-child split pays for a cyclic trace.
novelty_assessment: Selected mechanisms are compared with established antecedents where directly checked.
  No exhaustive novelty determination or certification of a source headline is claimed.
formalization_summary: Read the scope and complete TriangularHilbert Comparator. Its target is the maximal
  hard-truncation L3 x L3 to L(3/2) bound for arbitrary complex inputs, together with a common almost-everywhere
  domain and measurability. It does not state the newer full variation or dyadic absolute-summation theorem.
  Each inspected Comparator has a sorry target body. No separate solution or Lean build was checked.
statement_faithfulness: Probability averaging keeps a common fixed support. The dyadic argument is for
  real atom-constant inputs and uses four pairwise-independent child signs, not three independent signs.
dependencies: Divided differences, operator square-root order, inverse quadratic variational formulas,
  Gram matrices and cyclic trace bounds.
antecedents: Classical matrix entropy convexity and Bellman/telescoping energy methods.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Supported matrix costs and dyadic energy increments

## Source manuscripts and claim

- [Annular variation of the triangular Hilbert transform at the symmetric point](../papers/P-000447.md): selected passages extracted.
- [An L³ bound for the dyadic triangular Hilbert form](../papers/P-000448.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [The maximal triangular Hilbert transform at the symmetric point](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-maximal-triangular-Hilbert-transform-at-the-symmetric-point-September-24-2026)

The family claims full annular variation, a dyadic absolute bound and a maximal bound for triangular Hilbert forms.

## Extracted instruments

- [MI-000678: Average a square-root Hessian cost on a fixed support](../instruments/MI-000678.md)
- [MI-000679: Pay a cyclic trace with the energy gained by four parity-compatible children](../instruments/MI-000679.md)

## Dependencies and antecedents

Divided differences, operator square-root order, inverse quadratic variational formulas, Gram matrices and cyclic trace bounds.

Classical matrix entropy convexity and Bellman/telescoping energy methods.

## Review and formalization scope

Read the supported Hessian, order, insertion and joint convexity proofs in the annular manuscript. Read the complete local split, midpoint gap and real mixed-trace proof in the dyadic manuscript. Two of three manuscripts receive extractions; the earlier maximal manuscript remains inventory-only. Heat dissipation and global Hilbert estimates are not certified.

Read the scope and complete TriangularHilbert Comparator. Its target is the maximal hard-truncation L3 x L3 to L(3/2) bound for arbitrary complex inputs, together with a common almost-everywhere domain and measurability. It does not state the newer full variation or dyadic absolute-summation theorem. Each inspected Comparator has a sorry target body. No separate solution or Lean build was checked.

Probability averaging keeps a common fixed support. The dyadic argument is for real atom-constant inputs and uses four pairwise-independent child signs, not three independent signs.

[Batch record](../../batches/B072/README.md)
