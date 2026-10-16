---
id: openai-math-240
record_type: family
title: Countable torsor alignment and small-code uniformization
source_family: '240'
source_collection: openai/math
batch_id: B059
subject: Mathematical logic
source_paper_ids:
- P-000339
- P-000340
instrument_ids:
- MI-000570
- MI-000571
headline: One source claims a CH obstruction to a specified categoricity threshold; its companion claims
  eventual categoricity with an unspecified uniform threshold.
central_instrument: A triangular split absorbs any countable bit-matrix discrepancy using finite translations
  in each fiber. Directed presentations recover an AEC from small models and strong pairs, permitting
  a set-sized uniformity reduction.
novelty_assessment: Countable back-and-forth, triangular allocation and directed-limit coding are classical.
  Vasey already states the qualitative/uniform equivalence in Remark 1.3. These selected mechanisms do
  not establish either source headline theorem.
formalization_summary: The sole CHObstruction target uses set-coded relational structures, an explicit
  AEC definition and CH. It asserts LS number aleph_0, two models at beth_(omega_2)=h(aleph_0), and categoricity
  from beth_((2^aleph_1)^+) upward. Neither the separate eventual-categoricity theorem nor the canonical-point
  obstruction occurs in that target. The scope document and all linked Comparators were read in full.
  Their headline targets have sorry proof bodies; some supporting definitions contain explicit proofs.
  No separate solution or Lean project was built.
statement_faithfulness: The matrix alignment uses countable enumerations and finite-support torsors with
  exactly the stated bit action. The coding reduction concerns finitary AECs with an infinite LS bound
  and includes their strong relation, not only their object isomorphism types.
dependencies: Countable dense-order back-and-forth, finite-support binary groups, directed unions, coherence,
  the downward LS axiom and Replacement.
antecedents: Classical directed-limit and Hanf-number arguments; Vasey, Shelah eventual categoricity in
  universal classes, Part I, Remark 1.3.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Countable torsor alignment and small-code uniformization

## Source manuscripts and claim

- [A CH obstruction to a prescribed categoricity threshold](../papers/P-000339.md): selected passages extracted.
- [Eventual categoricity for abstract elementary classes](../papers/P-000340.md): selected passages extracted.

One source claims a CH obstruction to a specified categoricity threshold; its companion claims eventual categoricity with an unspecified uniform threshold.

## Extracted instruments

- [MI-000570: Absorb a countable bit matrix with finite row and column translations](../instruments/MI-000570.md)
- [MI-000571: Recover a class and its strong maps from small pairs before uniformizing](../instruments/MI-000571.md)

## Dependencies and antecedents

Countable dense-order back-and-forth, finite-support binary groups, directed unions, coherence, the downward LS axiom and Replacement.

Classical directed-limit and Hanf-number arguments; Vasey, Shelah eventual categoricity in universal classes, Part I, Remark 1.3.

## Review and formalization scope

Read the basic torsor definition and complete countable-base alignment proof. Read the complete directed-limit, small-code and uniform-reduction arguments in the companion. No global categoricity-transfer proof was audited.

The sole CHObstruction target uses set-coded relational structures, an explicit AEC definition and CH. It asserts LS number aleph_0, two models at beth_(omega_2)=h(aleph_0), and categoricity from beth_((2^aleph_1)^+) upward. Neither the separate eventual-categoricity theorem nor the canonical-point obstruction occurs in that target. The scope document and all linked Comparators were read in full. Their headline targets have sorry proof bodies; some supporting definitions contain explicit proofs. No separate solution or Lean project was built.

The matrix alignment uses countable enumerations and finite-support torsors with exactly the stated bit action. The coding reduction concerns finitary AECs with an infinite LS bound and includes their strong relation, not only their object isomorphism types.

[Batch record](../../batches/B059/README.md)
