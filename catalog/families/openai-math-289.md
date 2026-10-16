---
id: openai-math-289
record_type: family
title: Intertwining by polar decomposition and two classical operator obstructions
source_family: '289'
source_collection: openai/math
batch_id: B062
subject: Operator algebras
source_paper_ids:
- P-000368
- P-000369
- P-000370
instrument_ids:
- MI-000599
- MI-000600
- MI-000601
headline: The sources claim universal strong Kadison-Kastler stability, near inclusions without small
  embeddings, and close separable C-star algebras without spatial conjugacy.
central_instrument: An almost-flip produces an intertwiner; the clock-and-shift pair carries a nonzero
  integer obstruction; free-word cancellation gives a square-root norm bound.
novelty_assessment: These are classical perturbation, Voiculescu obstruction and free-group cancellation
  mechanisms. They are extracted independently of the much stronger source headlines.
formalization_summary: StrongKadisonKastler quantifies over arbitrary Hilbert spaces and all unital von
  Neumann subalgebras, with universal epsilon-to-delta control and a near-identity conjugating unitary.
  It covers only the first manuscript, not either counterexample companion. Both available scope documents
  and both linked Comparators in this batch were read in full. Target theorems have sorry proof bodies;
  some supporting definitions have explicit proofs. No separate solution or Lean build was checked.
statement_faithfulness: Representation closeness is completely bounded. The logarithm needs its branch
  cut avoided. The free-generator estimate is an upper bound, not an exact norm.
dependencies: Trace-class duality, commutants, polar decomposition, determinant and principal logarithm,
  orthogonal word prefixes.
antecedents: Classical derivation-distance and intertwining arguments; Voiculescu and Exel-Loring almost-commuting
  matrices; free-group cancellation estimates.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Intertwining by polar decomposition and two classical operator obstructions

## Source manuscripts and claim

- [Universal strong Kadison–Kastler stability](../papers/P-000368.md): selected passages extracted.
- [Near Inclusions of von Neumann Algebras Without Small Spatial Embeddings](../papers/P-000369.md): selected passages extracted.
- [Close Separable C*-Algebras Without Spatial Conjugacy](../papers/P-000370.md): selected passages extracted.

The sources claim universal strong Kadison-Kastler stability, near inclusions without small embeddings, and close separable C-star algebras without spatial conjugacy.

## Extracted instruments

- [MI-000599: Extract a nearby unitary intertwiner from the off-diagonal block of an almost-flip](../instruments/MI-000599.md)
- [MI-000600: Detect a persistent obstruction in almost-commuting clock and shift matrices](../instruments/MI-000600.md)
- [MI-000601: Bound a sum of free generators by splitting cancellation prefixes](../instruments/MI-000601.md)

## Dependencies and antecedents

Trace-class duality, commutants, polar decomposition, determinant and principal logarithm, orthogonal word prefixes.

Classical derivation-distance and intertwining arguments; Voiculescu and Exel-Loring almost-commuting matrices; free-group cancellation estimates.

## Review and formalization scope

Read the complete commutant-distance and paired-representation proofs, complete clock-and-shift obstruction, and complete free-generator norm estimate. Global stability and counterexample constructions remain unaudited.

StrongKadisonKastler quantifies over arbitrary Hilbert spaces and all unital von Neumann subalgebras, with universal epsilon-to-delta control and a near-identity conjugating unitary. It covers only the first manuscript, not either counterexample companion. Both available scope documents and both linked Comparators in this batch were read in full. Target theorems have sorry proof bodies; some supporting definitions have explicit proofs. No separate solution or Lean build was checked.

Representation closeness is completely bounded. The logarithm needs its branch cut avoided. The free-generator estimate is an upper bound, not an exact norm.

[Batch record](../../batches/B062/README.md)
