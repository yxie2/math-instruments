---
id: openai-math-206
record_type: family
title: Nonabelian coordinate compression and persistent lattice insertions
source_family: '206'
source_collection: openai/math
batch_id: B057
subject: Algebra
source_paper_ids:
- P-000323
- P-000324
instrument_ids:
- MI-000554
- MI-000555
headline: The manuscripts claim a finite congruence-lattice characterization and undecidability, and a
  negative solution to finite lattice representability.
central_instrument: Three-cycle differences compress invariant cosets in a bounded coordinate group. Private
  interval insertions preserve old lattice operations and keep reserved comparability components separate.
novelty_assessment: The ingredients are elementary group actions and lattice amalgamation. The particular
  bounded-control estimate and persistent-fence interface are recorded from the sources without an earliest-priority
  claim. The global classification and undecidability arguments are not audited.
formalization_summary: The actual FiniteCongruenceGraph target is the equivalence between representability
  as the full congruence lattice of a finite nonempty algebra and the specified finite colored-graph witness.
  Its proof contains sorry. Neither undecidability, subgroup-interval conclusions nor the companion negative
  solution is included in this target. The scope document and every linked Comparator were read in full.
  No solution or Lean project was built.
statement_faithfulness: Compression assumes natural alternating factors of degree at least seven, independent
  across alphabets, with complexity counting repeated copies and fixed points. Private insertions introduce
  only comparisons forced through their two endpoints.
dependencies: Coordinatewise multiplication in finite groups, three-cycles, two-transitivity, invariant
  cosets, finite lattices, comparability components and subgroup modularity.
antecedents: Classical alternating-group support manipulations and interval gluing of lattices; the source
  bounds and persistence conditions are stated explicitly.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Nonabelian coordinate compression and persistent lattice insertions

## Source manuscripts and claim

- [Finite congruence lattices: characterization and undecidability](../papers/P-000323.md): selected passages extracted.
- [A negative solution to the finite lattice representation problem](../papers/P-000324.md): selected passages extracted.

The manuscripts claim a finite congruence-lattice characterization and undecidability, and a negative solution to finite lattice representability.

## Extracted instruments

- [MI-000554: Compress invariant cosets with three-cycle differences](../instruments/MI-000554.md)
- [MI-000555: Insert lattice witnesses while preserving old operations and fences](../instruments/MI-000555.md)

## Dependencies and antecedents

Coordinatewise multiplication in finite groups, three-cycles, two-transitivity, invariant cosets, finite lattices, comparability components and subgroup modularity.

Classical alternating-group support manipulations and interval gluing of lattices; the source bounds and persistence conditions are stated explicitly.

## Review and formalization scope

Read the full bounded-base compression lemma and the private-insertion and persistent-fence proofs, together with the definition and normal-subgroup test for fences. The long finite-group classification, gluing and Diophantine reductions remain unaudited.

The actual FiniteCongruenceGraph target is the equivalence between representability as the full congruence lattice of a finite nonempty algebra and the specified finite colored-graph witness. Its proof contains sorry. Neither undecidability, subgroup-interval conclusions nor the companion negative solution is included in this target. The scope document and every linked Comparator were read in full. No solution or Lean project was built.

Compression assumes natural alternating factors of degree at least seven, independent across alphabets, with complexity counting repeated copies and fixed points. Private insertions introduce only comparisons forced through their two endpoints.

[Batch record](../../batches/B057/README.md)
