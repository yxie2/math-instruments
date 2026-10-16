---
id: openai-math-321
record_type: family
title: Finite plus constructions and exact twisted-boundary certificates
source_family: '321'
source_collection: openai/math
batch_id: B031
subject: Topology
source_paper_ids:
- P-000198
instrument_ids:
- MI-000358
- MI-000359
headline: The source claims a finite D(2) complex with no homotopy-equivalent finite two-dimensional complex.
central_instrument: A split third boundary preserves twisted homology while killing a perfect normal subgroup.
  Evaluating Fox derivatives at a finite-order character yields a small exact certificate for twisted
  second-homology vanishing.
novelty_assessment: The finite plus construction is classical and explicit in Mannan 2009, Section 2.
  Fox differentiation is standard. The source character and presentation give a concrete instance; its
  separate tower obstruction and global D(2) counterexample are not certified here.
formalization_summary: The pinned release inventory lists no linked formalization scope or Comparator
  for this family. No Lean project was inspected or built.
statement_faithfulness: Finite normal generation is weaker than finite generation of the perfect subgroup.
  A split injection, not injectivity alone, gives vanishing for every coefficient module. The computed
  Fox matrix is written with boundary vectors as rows.
dependencies: Van Kampen, covering spaces, the degree-two Hurewicz theorem, split chain complexes, tensor/Hom
  functors and Fox derivatives evaluated at a character.
antecedents: Quillen plus construction; Mannan 2009, Section 2; Fox free differential calculus.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Finite plus constructions and exact twisted-boundary certificates

## Source manuscript and claim

[A Counterexample to Wall's D(2) Problem](../papers/P-000198.md), by OpenAI, October 6, 2026.

The source claims a finite D(2) complex with no homotopy-equivalent finite two-dimensional complex.

## Extracted instruments

- [MI-000358: Use a split third boundary to obtain a finite plus construction for all coefficients](../instruments/MI-000358.md)
- [MI-000359: Certify twisted second-homology vanishing by an exact Fox minor](../instruments/MI-000359.md)

## Dependencies and antecedents

Van Kampen, covering spaces, the degree-two Hurewicz theorem, split chain complexes, tensor/Hom functors and Fox derivatives evaluated at a character.

Quillen plus construction; Mannan 2009, Section 2; Fox free differential calculus. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete finite plus-construction proof and the full explicit construction section, including perfectness and the twisted-boundary computation. The tower obstruction and its character/torsion corollary were not audited.

The pinned release inventory lists no linked formalization scope or Comparator for this family. No Lean project was inspected or built.

Finite normal generation is weaker than finite generation of the perfect subgroup. A split injection, not injectivity alone, gives vanishing for every coefficient module. The computed Fox matrix is written with boundary vectors as rows.

[Batch record](../../batches/B031/README.md)
