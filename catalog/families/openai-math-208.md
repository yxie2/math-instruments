---
id: openai-math-208
record_type: family
title: Norm-based projectivity and Frobenius nullvector selection
source_family: '208'
source_collection: openai/math
batch_id: B052
subject: Algebra
source_paper_ids:
- P-000289
instrument_ids:
- MI-000516
- MI-000517
headline: The source claims a fiber functor from every finite symmetric tensor category in positive characteristic
  to a finite level of the higher Verlinde tower.
central_instrument: A projective-generator evaluation can transfer projectivity through internal norm
  maps without preserving tensor products. A Moore-matrix nullvector solves Frobenius constraints while
  retaining prime-field independence.
novelty_assessment: Norm/projectivity and Moore determinants are classical. Coulembier-Flake explicitly
  supplies the Steinberg support equations. The source combines these interfaces; no full novelty certification.
formalization_summary: No family scope document or linked Comparator target is listed in the pinned release
  inventory. No formal verification is claimed.
statement_faithfulness: The converse norm criterion is for finite p-groups in characteristic p. Evaluation
  is exact faithful, not assumed monoidal. The nullvector selection requires prime-field independent input
  coordinates and a perfect field.
dependencies: Local self-injective group algebras, socles, Nakayama, exact tensor products, invariants
  and coinvariants; additive polynomials, Frobenius automorphism and Moore matrices.
antecedents: Classical projective-free norm vanishing; Coulembier-Flake rank-support description of restricted
  Steinberg modules.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Norm-based projectivity and Frobenius nullvector selection

## Source manuscripts and claim

- [Fiber functors for finite symmetric tensor categories in positive characteristic](../papers/P-000289.md): selected passages extracted.

The source claims a fiber functor from every finite symmetric tensor category in positive characteristic to a finite level of the higher Verlinde tower.

## Extracted instruments

- [MI-000516: Transfer projectivity through internal norms without a monoidal evaluation](../instruments/MI-000516.md)
- [MI-000517: Choose an independent Frobenius-constrained nullvector](../instruments/MI-000517.md)

## Dependencies and antecedents

Local self-injective group algebras, socles, Nakayama, exact tensor products, invariants and coinvariants; additive polynomials, Frobenius automorphism and Moore matrices.

Classical projective-free norm vanishing; Coulembier-Flake rank-support description of restricted Steinberg modules.

## Review and formalization scope

Read the complete norm criterion, internal norm-product proof, support-independence proof, Steinberg support calculation and Moore-selection lemma. Restricted tilting and the full fiber-functor construction remain unverified.

No family scope document or linked Comparator target is listed in the pinned release inventory. No formal verification is claimed.

The converse norm criterion is for finite p-groups in characteristic p. Evaluation is exact faithful, not assumed monoidal. The nullvector selection requires prime-field independent input coordinates and a perfect field.

[Batch record](../../batches/B052/README.md)
