---
id: openai-math-199
record_type: family
title: Finite cocycle certificates and transfer through a nonflat trivial extension
source_family: '199'
source_collection: openai/math
batch_id: B056
subject: Algebra
source_paper_ids:
- P-000315
- P-000316
instrument_ids:
- MI-000546
- MI-000547
headline: The two manuscripts claim finite-dimensional counterexamples to the Auslander-Reiten and second
  Tachikawa conjectures over F_2(q,H_1,H_2).
central_instrument: A multiplication table and sparse cochain permit complete polynomial checks of cocycle,
  boundary and nonzero-pairing identities. A separate conditional transfer uses total acyclicity to justify
  induction without assuming flatness.
novelty_assessment: Trivial extensions, bar complexes, duality and induction are classical. The explicit
  179-entry cochain is checked as source data; no priority claim is made for that table or the conditional
  assembly, and neither conjecture counterexample is certified.
formalization_summary: AuslanderReiten states existence of the finite algebra and nonprojective Gorenstein-projective
  module, the positive Ext vanishings, the eight-simple quotient, nonzero fourth radical power and persistence
  under every field extension. Tachikawa states existence of a finite symmetric algebra and finite nonprojective
  module with all positive self-Ext zero. It does not include the manuscript subsequent endomorphism-algebra
  consequences. Both inspected target proofs contain sorry. The scope document and every linked Comparator
  were read in full. No solution or Lean project was built.
statement_faithfulness: Polynomial identities are checked over F_2[q], without numerical specialization.
  The transfer requires vanishing in every positive degree and every degree at most -2, as well as a nonprojective
  cokernel of a totally acyclic finite-projective complex.
dependencies: Associative algebra tables, dual bimodules, normalized relative bar resolutions, Hochschild
  differentials, Nakayama evaluation, injective coresolutions and induction-restriction adjunction.
antecedents: Classical Hochschild and trivial-extension methods; Cibils-Marcos-Redondo-Solotar on split
  algebras and trivial extensions; ordinary finite-projective evaluation duality.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Finite cocycle certificates and transfer through a nonflat trivial extension

## Source manuscripts and claim

- [An explicit counterexample to the Auslander-Reiten conjecture](../papers/P-000315.md): selected passages extracted.
- [A counterexample to Tachikawa's second conjecture](../papers/P-000316.md): selected passages extracted.

The two manuscripts claim finite-dimensional counterexamples to the Auslander-Reiten and second Tachikawa conjectures over F_2(q,H_1,H_2).

## Extracted instruments

- [MI-000546: Check a sparse Hochschild class by a full polynomial certificate](../instruments/MI-000546.md)
- [MI-000547: Transfer two-sided cohomology vanishing through a trivial extension](../instruments/MI-000547.md)

## Dependencies and antecedents

Associative algebra tables, dual bimodules, normalized relative bar resolutions, Hochschild differentials, Nakayama evaluation, injective coresolutions and induction-restriction adjunction.

Classical Hochschild and trivial-extension methods; Cibils-Marcos-Redondo-Solotar on split algebras and trivial extensions; ordinary finite-projective evaluation duality.

## Review and formalization scope

Read the full algebra and cocycle construction, the complete cochain appendix, and the entire conditional transfer proof. The later cones, complete-resolution construction and required infinite vanishing assertions remain unaudited.

AuslanderReiten states existence of the finite algebra and nonprojective Gorenstein-projective module, the positive Ext vanishings, the eight-simple quotient, nonzero fourth radical power and persistence under every field extension. Tachikawa states existence of a finite symmetric algebra and finite nonprojective module with all positive self-Ext zero. It does not include the manuscript subsequent endomorphism-algebra consequences. Both inspected target proofs contain sorry. The scope document and every linked Comparator were read in full. No solution or Lean project was built.

Polynomial identities are checked over F_2[q], without numerical specialization. The transfer requires vanishing in every positive degree and every degree at most -2, as well as a nonprojective cokernel of a totally acyclic finite-projective complex.

[Batch record](../../batches/B056/README.md)
