---
id: openai-math-346
record_type: family
title: Positive height from frequency control and integer projection counts
source_family: '346'
source_collection: openai/math
batch_id: B063
subject: Differential geometry
source_paper_ids:
- P-000375
- P-000376
instrument_ids:
- MI-000606
- MI-000607
headline: The sources claim a codimension-one singular-set bound and almost-everywhere regularity for
  stationary integral varifolds.
central_instrument: A finite-radius frequency argument rules out open regions of zero height. Projection
  determinants compare pushed mass with integer sheet counts, including deficient-rank errors.
novelty_assessment: The projection calculation uses the classical area formula. The positive-height argument
  is explicitly shared with the source companion; external priority for its exact measure formulation
  was not established.
formalization_summary: No Lean scope document or linked Comparator is supplied for this family in the
  pinned inventory. No formal solution was built.
statement_faithfulness: The height lemma assumes positive matrix measures, all distributional identities
  and the local signed stress bound. The projection error may contain a singular pushforward; absolute
  continuity is not inferred.
dependencies: Positive matrix measures, compact radial kernels, differential inequalities, projection
  spectra and the rectifiable area formula.
antecedents: Classical frequency continuation and area formulas; the source companion supplies the finite-radius
  argument.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Positive height from frequency control and integer projection counts

## Source manuscripts and claim

- [A Codimension-One Bound for the Singular Set of a Stationary Integral Varifold](../papers/P-000375.md): selected passages extracted.
- [Almost-everywhere regularity of stationary integral varifolds](../papers/P-000376.md): selected passages extracted.

The sources claim a codimension-one singular-set bound and almost-everywhere regularity for stationary integral varifolds.

## Extracted instruments

- [MI-000606: Rule out an open zero-height region using finite-radius frequency control](../instruments/MI-000606.md)
- [MI-000607: Compare projected mass with integer counts using determinant and tilt errors](../instruments/MI-000607.md)

## Dependencies and antecedents

Positive matrix measures, compact radial kernels, differential inequalities, projection spectra and the rectifiable area formula.

Classical frequency continuation and area formulas; the source companion supplies the finite-radius argument.

## Review and formalization scope

Read the complete positive-limit-height proof and its kernel identities, and the complete projection-and-integer-count proof with its tensor definitions. Construction of the limiting measures, signed excess and global dimension reduction remain unaudited.

No Lean scope document or linked Comparator is supplied for this family in the pinned inventory. No formal solution was built.

The height lemma assumes positive matrix measures, all distributional identities and the local signed stress bound. The projection error may contain a singular pushforward; absolute continuity is not inferred.

[Batch record](../../batches/B063/README.md)
