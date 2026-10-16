---
id: openai-math-314
record_type: family
title: Automorphism-weighted integration and p-adic subgroup counts
source_family: '314'
source_collection: openai/math
batch_id: B025
subject: Topology
source_paper_ids:
- P-000173
instrument_ids:
- MI-000308
- MI-000309
headline: The source claims that optimal chromatic fixed-point loss for every subgroup of a finite p-group
  equals the minimum length of a subnormal chain with cyclic quotients, at every finite target height
  including zero.
central_instrument: Derive integration and pushforward weights from diagonal transfer and automorphism
  groups. Use the classical subgroup generating function of Z_p^d to obtain a nonzero p-adic limit with
  explicit precision.
novelty_assessment: Automorphism-weighted groupoid integration and the subgroup-count formula have explicit
  earlier sources. Their role in the proposed chromatic argument is recorded without certifying its new
  character construction or height-gluing theorem.
formalization_summary: No family-specific scope document or Comparator target is listed for this family.
  No Lean artifact was built or kernel-checked.
statement_faithfulness: Cyclic quotients of arbitrary p-power order count as one step. Embedded subgroups,
  not just their abstract isomorphism type, matter. Homotopy fibers retain automorphisms in the kernel
  of a functor.
dependencies: Finite groupoid cardinality, diagonal transfer, the projection formula, triangular lattice
  bases, geometric series and p-adic convergence.
antecedents: Strickland finite-groupoid Frobenius character formulas; Tamanoi Lemma 5-5 on subgroups of
  Z_p^d.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Automorphism-weighted integration and p-adic subgroup counts

## Source manuscript and claim

[Cyclic length and chromatic fixed-point loss](../papers/P-000173.md), by OpenAI, September 24, 2026.

The source claims that optimal chromatic fixed-point loss for every subgroup of a finite p-group equals the minimum length of a subnormal chain with cyclic quotients, at every finite target height including zero.

## Extracted instruments

- [MI-000308: Diagonal transfer forces inverse-automorphism integration weights](../instruments/MI-000308.md)
- [MI-000309: Subgroup counts of Z_p^d stabilize to a nonzero p-adic unit](../instruments/MI-000309.md)

## Dependencies and antecedents

Finite groupoid cardinality, diagonal transfer, the projection formula, triangular lattice bases, geometric series and p-adic convergence.

Strickland finite-groupoid Frobenius character formulas; Tamanoi Lemma 5-5 on subgroups of Z_p^d. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete integration-weight proposition and lattice-limit lemma. The pro-character splitting, integral scalar theorem, shrinking actions, kernel argument and chromatic gluing were not audited.

No family-specific scope document or Comparator target is listed for this family. No Lean artifact was built or kernel-checked.

Cyclic quotients of arbitrary p-power order count as one step. Embedded subgroups, not just their abstract isomorphism type, matter. Homotopy fibers retain automorphisms in the kernel of a functor.

[Batch record](../../batches/B025/README.md)
