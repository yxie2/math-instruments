---
id: openai-math-084
record_type: family
title: Stable grid keys and open repair of exceptional centers
source_family: 084
source_collection: openai/math
batch_id: B072
subject: Real and complex analysis
source_paper_ids:
- P-000449
- P-000450
instrument_ids:
- MI-000680
- MI-000681
headline: The family claims avoidance of affine copies of geometric sequences, extending an earlier dyadic
  construction.
central_instrument: Nested dyadic grids work for a general geometric ratio; openness and compact projection
  turn almost-everywhere success into an all-center repair.
novelty_assessment: Selected mechanisms are compared with established antecedents where directly checked.
  No exhaustive novelty determination or certification of a source headline is claimed.
formalization_summary: Read the scope and complete DyadicAvoidance Comparator. It targets a compact subset
  of [0,1] of measure greater than 1-eta avoiding every affine dyadic tail, for both signs of a nonzero
  dilation. It does not state avoidance for every geometric ratio q. Each inspected Comparator has a sorry
  target body. No separate solution or Lean build was checked.
statement_faithfulness: The grid construction fixes q in (0,1) and normalized positive scales in [1,2].
  The repair assumes the stated density and all-scale failure bounds; those probabilistic inputs are not
  established here.
dependencies: Preorder trees, geometric gaps, periodic grid nesting, finite probability spaces, compact
  projection and measure continuity.
antecedents: Kolountzakis open-cover completion and classical grid discretization.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Stable grid keys and open repair of exceptional centers

## Source manuscripts and claim

- [The geometric case of the Erdős similarity conjecture](../papers/P-000449.md): selected passages extracted.
- [The dyadic case of the Erdős similarity conjecture](../papers/P-000450.md): selected passages extracted.

The family claims avoidance of affine copies of geometric sequences, extending an earlier dyadic construction.

## Extracted instruments

- [MI-000680: Separate current geometric tests while preserving earlier grid keys](../instruments/MI-000680.md)
- [MI-000681: Repair exceptional centers by an open neighborhood and a vanishing tail](../instruments/MI-000681.md)

## Dependencies and antecedents

Preorder trees, geometric gaps, periodic grid nesting, finite probability spaces, compact projection and measure continuity.

Kolountzakis open-cover completion and classical grid discretization.

## Review and formalization scope

Read the complete preorder-span, stability and separation proofs and the full exceptional-center repair. Both manuscripts receive extractions. Random routing and the uniform all-scale probability estimates are not certified.

Read the scope and complete DyadicAvoidance Comparator. It targets a compact subset of [0,1] of measure greater than 1-eta avoiding every affine dyadic tail, for both signs of a nonzero dilation. It does not state avoidance for every geometric ratio q. Each inspected Comparator has a sorry target body. No separate solution or Lean build was checked.

The grid construction fixes q in (0,1) and normalized positive scales in [1,2]. The repair assumes the stated density and all-scale failure bounds; those probabilistic inputs are not established here.

[Batch record](../../batches/B072/README.md)
