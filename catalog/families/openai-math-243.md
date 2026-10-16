---
id: openai-math-243
record_type: family
title: Sparse cochain representatives and persistent grid components
source_family: '243'
source_collection: openai/math
batch_id: B059
subject: Mathematical logic
source_paper_ids:
- P-000341
- P-000342
instrument_ids:
- MI-000572
- MI-000573
headline: The sources claim that choiceless polynomial time with counting does not capture polynomial
  time and that one witnessed symmetric-choice occurrence strictly increases expressive power.
central_instrument: Successive coordinate prefix sums replace an edge functional by a sparse representative
  modulo gradients. A discrete projection inequality controls the total size of components after edge
  deletion.
novelty_assessment: The ingredients are discrete gauge elimination and the classical Loomis-Whitney projection
  inequality. Source quantitative bounds and their support interfaces are useful extractions without a
  new complexity-separation certification.
formalization_summary: ChoicelessPolynomialTime specifies an eight-relation F3 linear query, explicit
  HF operational syntax and polynomial bounds on complete occurring-object closure; its target asserts
  isomorphism invariance, ordinary Turing polynomial time and nondefinability. WitnessedChoice separately
  defines witnessed iteration with automorphisms fixing every preceding state and the free parameters;
  its target is one total Boolean sentence with exactly one occurrence and a true-model class different
  from every choice-free sentence. The scope document and all linked Comparators were read in full. Their
  headline targets have sorry proof bodies; some supporting definitions contain explicit proofs. No separate
  solution or Lean project was built.
statement_faithfulness: The cochain construction is on a box, over F3, with ordinary boundary rather than
  periodic coordinates. The giant-component assertion is asymptotic for the source deletion scale; finite
  tests instead check its explicit mass estimate.
dependencies: Graph incidence, face curls, prefix sums, gradients, Cauchy-Schwarz, projection cardinalities
  and connected components.
antecedents: Discrete exactness on contractible boxes; Loomis-Whitney projection inequality.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Sparse cochain representatives and persistent grid components

## Source manuscripts and claim

- [Choiceless polynomial time with counting does not capture polynomial time](../papers/P-000341.md): selected passages extracted.
- [Witnessed symmetric choice is strictly stronger than choiceless polynomial time with counting](../papers/P-000342.md): selected passages extracted.

The sources claim that choiceless polynomial time with counting does not capture polynomial time and that one witnessed symmetric-choice occurrence strictly increases expressive power.

## Extracted instruments

- [MI-000572: Concentrate an edge cochain by subtracting three prefix gradients](../instruments/MI-000572.md)
- [MI-000573: Control all small components by a projection boundary budget](../instruments/MI-000573.md)

## Dependencies and antecedents

Graph incidence, face curls, prefix sums, gradients, Cauchy-Schwarz, projection cardinalities and connected components.

Discrete exactness on contractible boxes; Loomis-Whitney projection inequality.

## Review and formalization scope

Read the full sparse-cochain proof and its central-flow definitions in the first manuscript. Read the full boundary and persistent-component proofs in the witnessed-choice companion. Hereditary support transfer, full computation coding and the separation theorems remain unaudited.

ChoicelessPolynomialTime specifies an eight-relation F3 linear query, explicit HF operational syntax and polynomial bounds on complete occurring-object closure; its target asserts isomorphism invariance, ordinary Turing polynomial time and nondefinability. WitnessedChoice separately defines witnessed iteration with automorphisms fixing every preceding state and the free parameters; its target is one total Boolean sentence with exactly one occurrence and a true-model class different from every choice-free sentence. The scope document and all linked Comparators were read in full. Their headline targets have sorry proof bodies; some supporting definitions contain explicit proofs. No separate solution or Lean project was built.

The cochain construction is on a box, over F3, with ordinary boundary rather than periodic coordinates. The giant-component assertion is asymptotic for the source deletion scale; finite tests instead check its explicit mass estimate.

[Batch record](../../batches/B059/README.md)
