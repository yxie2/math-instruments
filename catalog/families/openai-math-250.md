---
id: openai-math-250
record_type: family
title: Mapping tori, action monoids and additive idempotent diagrams
source_family: '250'
source_collection: openai/math
batch_id: B061
subject: Group theory
source_paper_ids:
- P-000356
- P-000357
- P-000358
instrument_ids:
- MI-000587
- MI-000588
- MI-000589
headline: The sources claim Boone-Higman embeddings, simple overgroups of type F-infinity, and one universal
  group of type F-infinity containing every finitely presented group.
central_instrument: A direct limit describes a mapping torus even for a noninjective map. A length-decreasing
  action monoid has a confluent normal form. Two small-characteristic idempotent diagrams force prime
  torsion in additive assignments.
novelty_assessment: Mapping-torus and rewriting principles are classical. The particular linked idempotent
  diagram is shared by two source companions; an external earliest-priority result for that exact diagram
  was not established.
formalization_summary: BooneHigman states the finitely generated decidable-word-problem equivalence with
  embeddings in finitely presented simple groups. SimpleOvergroups uses a finite-type classifying CW space
  with contractible cover and a nontrivial simple target. UniversalFInfinity fixes one target before all
  finitely presented input groups; it assumes no decidable word problem and does not include the recursive-subgroup
  converse. All three available scope documents and all seven linked Comparators in this batch were read
  in full. Headline targets have sorry proof bodies; supporting definitions sometimes have explicit proofs.
  No separate solution or Lean project was built.
statement_faithfulness: The initial group need not inject into a noninjective mapping torus. The action-monoid
  presentation includes an absorbing zero. Idempotents are actual operators, and cross-algebra orthogonal
  sums are essential.
dependencies: Direct limits, semidirect products, terminating rewriting, group actions, rank-one matrix
  identities and prefix operators.
antecedents: Classical ascending mapping tori and confluent rewriting; elementary idempotent additivity.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Mapping tori, action monoids and additive idempotent diagrams

## Source manuscripts and claim

- [Finite algebraic envelopes and the Boone–Higman conjecture](../papers/P-000356.md): selected passages extracted.
- [Simple F∞ overgroups of groups with decidable word problem](../papers/P-000357.md): selected passages extracted.
- [A universal group of type F∞](../papers/P-000358.md): selected passages extracted.

The sources claim Boone-Higman embeddings, simple overgroups of type F-infinity, and one universal group of type F-infinity containing every finitely presented group.

## Extracted instruments

- [MI-000587: Describe a noninjective mapping torus by its direct limit](../instruments/MI-000587.md)
- [MI-000588: Encode a group action in a terminating monoid normal form](../instruments/MI-000588.md)
- [MI-000589: Force prime torsion using linked finite idempotent diagrams](../instruments/MI-000589.md)

## Dependencies and antecedents

Direct limits, semidirect products, terminating rewriting, group actions, rank-one matrix identities and prefix operators.

Classical ascending mapping tori and confluent rewriting; elementary idempotent additivity.

## Review and formalization scope

Read the complete mapping-torus and affine-limit arguments, the complete action-monoid normal form, and the full finite-idempotent diagram proof. The compiler, Steinberg kernel annihilation, controlled fillings and embedding theorems remain unaudited.

BooneHigman states the finitely generated decidable-word-problem equivalence with embeddings in finitely presented simple groups. SimpleOvergroups uses a finite-type classifying CW space with contractible cover and a nontrivial simple target. UniversalFInfinity fixes one target before all finitely presented input groups; it assumes no decidable word problem and does not include the recursive-subgroup converse. All three available scope documents and all seven linked Comparators in this batch were read in full. Headline targets have sorry proof bodies; supporting definitions sometimes have explicit proofs. No separate solution or Lean project was built.

The initial group need not inject into a noninjective mapping torus. The action-monoid presentation includes an absorbing zero. Idempotents are actual operators, and cross-algebra orthogonal sums are essential.

[Batch record](../../batches/B061/README.md)
