---
id: openai-math-141
record_type: family
title: Coefficient extraction and sign recovery using only modular data
source_family: '141'
source_collection: openai/math
batch_id: B024
subject: Theoretical computer science
source_paper_ids:
- P-000170
instrument_ids:
- MI-000302
- MI-000303
headline: The source claims that true existential-universal real sentences with explicit arithmetic circuits
  belong to a fixed level of the counting hierarchy, independent of input dimension, degree and coefficient
  height.
central_instrument: Extract multivariate coefficients by finite multiplicative Fourier averaging. Determine
  the sign of a bounded integer from modular residues by a rounded CRT phase and its first escape under
  doubling.
novelty_assessment: Finite-group orthogonality and approximate CRT sign determination are established.
  The source provides a particular bounded-precision first-escape formulation; the full real-sentence
  complexity theorem and exact hierarchy level are not certified.
formalization_summary: No family-specific Lean scope document or Comparator target is listed for this
  family. No Lean artifact was built or kernel-checked.
statement_faithfulness: Circuits use addition, subtraction and multiplication with signed binary constants,
  not division or exponentiation gates. Coefficient extraction needs p-1 larger than the degree. Sign
  recovery requires a modulus-product bound relative to the unknown integer.
dependencies: Finite-field character sums, Chinese remaindering, fixed-point rounding and a first-threshold
  argument. Counting-hierarchy closure and algebraic witness/deformation machinery are separate inputs.
antecedents: Classical finite multiplicative Fourier inversion; Allender-Buergisser-Kjeldgaard-Pedersen-Miltersen
  approximate CRT analysis of PosSLP.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Coefficient extraction and sign recovery using only modular data

## Source manuscript and claim

[Existential–universal real sentences in the counting hierarchy](../papers/P-000170.md), by OpenAI, October 4, 2026.

The source claims that true existential-universal real sentences with explicit arithmetic circuits belong to a fixed level of the counting hierarchy, independent of input dimension, degree and coefficient height.

## Extracted instruments

- [MI-000302: Extract a multivariate coefficient by averaging over nonzero field elements](../instruments/MI-000302.md)
- [MI-000303: Recover an integer sign from the first escape of a rounded CRT phase](../instruments/MI-000303.md)

## Dependencies and antecedents

Finite-field character sums, Chinese remaindering, fixed-point rounding and a first-threshold argument. Counting-hierarchy closure and algebraic witness/deformation machinery are separate inputs.

Classical finite multiplicative Fourier inversion; Allender-Buergisser-Kjeldgaard-Pedersen-Miltersen approximate CRT analysis of PosSLP. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete field-coefficient lemma and CRT sign proof. The algebraic witnesses, root labels, deformation argument and hierarchy closure proofs supporting the main theorem were not audited.

No family-specific Lean scope document or Comparator target is listed for this family. No Lean artifact was built or kernel-checked.

Circuits use addition, subtraction and multiplication with signed binary constants, not division or exponentiation gates. Coefficient extraction needs p-1 larger than the degree. Sign recovery requires a modulus-product bound relative to the unknown integer.

[Batch record](../../batches/B024/README.md)
