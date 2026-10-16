---
id: openai-math-205
record_type: family
title: Memoized character-square recurrence and constructive dominance chains
source_family: '205'
source_collection: openai/math
batch_id: B056
subject: Algebra
source_paper_ids:
- P-000321
- P-000322
instrument_ids:
- MI-000552
- MI-000553
headline: The manuscripts claim universal irreducible tensor squares for symmetric groups outside degrees
  2,4,9, and the staircase tensor-square assertion of Saxl.
central_instrument: A repeated-cycle state gives a denominator-controlled recursion for all tensor-square
  multiplicities. A separate constructive horizontal-strip deletion explains the classical dominance support
  of Young permutation modules.
novelty_assessment: Murnaghan-Nakayama, abacus moves, modular nonvanishing, Young rule and Pieri are classical.
  The source recurrence is a concrete computational arrangement; the catalogue does not claim that arrangement
  is historically first or certify either global tensor-square theorem.
formalization_summary: UniversalTensorSquares states existence for every positive n except 2,4,9, including
  irreducibility and injective intertwiners from all finite-dimensional irreducibles. Saxl states positive
  Kronecker multiplicity for every partition in every staircase square. It does not assert a particular
  cyclic vector. Both target proofs contain sorry. The scope document and every linked Comparator were
  read in full. No solution or Lean project was built.
statement_faithfulness: A nonzero residue proves positivity of a known nonnegative integer multiplicity,
  whereas zero residues are inconclusive. One candidate partition must pass every constituent test. The
  horizontal-strip lemma alone has no tensor-square conclusion.
dependencies: Partitions, character orthogonality, signed border strips, bead moves, rational class weights,
  modular arithmetic, dominance order and horizontal-strip induction.
antecedents: Classical Murnaghan-Nakayama and Young-Pieri rules, with a readable comparison in Stacey
  Law lectures recorded by Leonard Tomczak.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Memoized character-square recurrence and constructive dominance chains

## Source manuscripts and claim

- [Universal Tensor Squares for Symmetric Groups](../papers/P-000321.md): selected passages extracted.
- [A Cyclic Polytabloid Proof of Saxl's Conjecture](../papers/P-000322.md): selected passages extracted.

The manuscripts claim universal irreducible tensor squares for symmetric groups outside degrees 2,4,9, and the staircase tensor-square assertion of Saxl.

## Extracted instruments

- [MI-000552: Track repeated cycles in a character-square recurrence](../instruments/MI-000552.md)
- [MI-000553: Construct a horizontal-strip chain from dominance](../instruments/MI-000553.md)

## Dependencies and antecedents

Partitions, character orthogonality, signed border strips, bead moves, rational class weights, modular arithmetic, dominance order and horizontal-strip induction.

Classical Murnaghan-Nakayama and Young-Pieri rules, with a readable comparison in Stacey Law lectures recorded by Leonard Tomczak.

## Review and formalization scope

Read the entire finite recurrence section and the full selected Specht-tools section. Independently tested the recurrence only through degree 8. The source reported computation through degree 64, its large-degree argument and the proposed cyclic-polytabloid construction are not certified.

UniversalTensorSquares states existence for every positive n except 2,4,9, including irreducibility and injective intertwiners from all finite-dimensional irreducibles. Saxl states positive Kronecker multiplicity for every partition in every staircase square. It does not assert a particular cyclic vector. Both target proofs contain sorry. The scope document and every linked Comparator were read in full. No solution or Lean project was built.

A nonzero residue proves positivity of a known nonnegative integer multiplicity, whereas zero residues are inconclusive. One candidate partition must pass every constituent test. The horizontal-strip lemma alone has no tensor-square conclusion.

[Batch record](../../batches/B056/README.md)
