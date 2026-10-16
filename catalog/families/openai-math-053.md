---
id: openai-math-053
record_type: family
title: Coefficient algebras and coefficient-preserving polarization
source_family: '053'
source_collection: openai/math
batch_id: B039
subject: Algebraic and complex geometry
source_paper_ids:
- P-000229
instrument_ids:
- MI-000420
- MI-000421
headline: The source claims a high-arity counterexample to Pixton completeness in Chow.
central_instrument: A coefficient algebra records morphisms of a tensor functor without requiring realization
  faithfulness. Finite scalar evaluations detect polynomial tensors while retaining these coefficients.
novelty_assessment: Coefficient-algebra reconstruction has a direct antecedent in O Sullivan, Lemma 2.3.1.
  Rational polarization is classical. Their use in the claimed Chow counterexample is not independently
  certified.
formalization_summary: No formalization scope document is listed for this family in the pinned inventory.
  No Lean build.
statement_faithfulness: The coefficient algebra may contain nilpotents and nontrivial unit endomorphisms.
  Scalar evaluation acts only on color variables and is not augmentation of that algebra. The tensor-functor
  construction is an input.
dependencies: Semisimple representation categories, super signs, rigidity, finite-group coinvariants in
  characteristic zero and rational polynomial interpolation.
antecedents: O Sullivan, Algebraic cycles on an abelian variety, Lemma 2.3.1; classical polarization.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Coefficient algebras and coefficient-preserving polarization

## Source manuscript and claim

[A high-arity counterexample to Pixton completeness in Chow](../papers/P-000229.md), by OpenAI, None.

The source claims a high-arity counterexample to Pixton completeness in Chow.

## Extracted instruments

- [MI-000420: Retain extra tensor-category morphisms in a coefficient algebra](../instruments/MI-000420.md)
- [MI-000421: Detect polynomial tensors by finitely many scalar evaluations without discarding coefficients](../instruments/MI-000421.md)

## Dependencies and antecedents

Semisimple representation categories, super signs, rigidity, finite-group coinvariants in characteristic zero and rational polynomial interpolation.

O Sullivan, Algebraic cycles on an abelian variety, Lemma 2.3.1; classical polarization. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete selected coefficient-algebra and color-polarization proofs and their definitions. The earlier construction of the Chow tensor functor and the final counterexample were not audited.

No formalization scope document is listed for this family in the pinned inventory. No Lean build.

The coefficient algebra may contain nilpotents and nontrivial unit endomorphisms. Scalar evaluation acts only on color variables and is not augmentation of that algebra. The tensor-functor construction is an input.

[Batch record](../../batches/B039/README.md)
