---
id: openai-math-207
record_type: family
title: Trace-preserving idempotent repair and lift-independent Pfaffian cocycles
source_family: '207'
source_collection: openai/math
batch_id: B057
subject: Algebra
source_paper_ids:
- P-000325
- P-000326
instrument_ids:
- MI-000556
- MI-000557
headline: The sources claim the l1-Bass trace theorem for all discrete groups and the complex group-ring
  Bass theorem with torsion-free idempotent consequences.
central_instrument: Repair a finite-support approximation in a small exponential weight without changing
  its trace class. Eliminate lift dependence of a skew form by taking an alternating Pfaffian deletion
  sum.
novelty_assessment: Banach-algebra idempotent perturbation and nearby similarity are classical; the source
  adds an explicit weighted-group-algebra reduction. Exterior-algebra cancellation and Pfaffian expansion
  are classical. The later analytic and sparse-chain vanishing arguments remain unaudited.
formalization_summary: The inspected BassTrace and BassTorsionFree targets concern finite-support complex
  group rings, ordinary algebraic K0, torsion-free trace rank and characteristic-zero scalar idempotents.
  They do not state the l1 completion theorem. The trace and K0 constructions include explicit Lean proofs,
  while the two headline target proofs contain sorry. The scope document and every linked Comparator were
  read in full. No solution or Lean project was built.
statement_faithfulness: The decay rate may depend on the idempotent and its approximation. The Pfaffian
  weights are finite complex sums, not probability distributions, and the raw skew function need not be
  bounded or descend to the quotient.
dependencies: Submultiplicative exponential norms, inverse-square-root power series, trace cyclicity,
  similarity, free quotient actions, skew forms, Pfaffians and simplicial deletion.
antecedents: Blackadar on equivalence and perturbation of idempotents; classical exterior powers and Pfaffian
  identities.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Trace-preserving idempotent repair and lift-independent Pfaffian cocycles

## Source manuscripts and claim

- [The ℓ¹-Bass Conjecture for Discrete Groups](../papers/P-000325.md): selected passages extracted.
- [The Bass trace conjecture and the characteristic-zero Kaplansky idempotent conjecture](../papers/P-000326.md): selected passages extracted.

The sources claim the l1-Bass trace theorem for all discrete groups and the complex group-ring Bass theorem with torsion-free idempotent consequences.

## Extracted instruments

- [MI-000556: Repair an idempotent in an exponential weight while preserving every class trace](../instruments/MI-000556.md)
- [MI-000557: Cancel lift dependence in a Pfaffian deletion cocycle](../instruments/MI-000557.md)

## Dependencies and antecedents

Submultiplicative exponential norms, inverse-square-root power series, trace cyclicity, similarity, free quotient actions, skew forms, Pfaffians and simplicial deletion.

Blackadar on equivalence and perturbation of idempotents; classical exterior powers and Pfaffian identities.

## Review and formalization scope

Read the complete exponential-representative proof, the path-deletion identities and the entire Pfaffian detector construction. The spatial channels, curvature estimates and sparse-chain vanishing theorem are not certified.

The inspected BassTrace and BassTorsionFree targets concern finite-support complex group rings, ordinary algebraic K0, torsion-free trace rank and characteristic-zero scalar idempotents. They do not state the l1 completion theorem. The trace and K0 constructions include explicit Lean proofs, while the two headline target proofs contain sorry. The scope document and every linked Comparator were read in full. No solution or Lean project was built.

The decay rate may depend on the idempotent and its approximation. The Pfaffian weights are finite complex sums, not probability distributions, and the raw skew function need not be bounded or descend to the quotient.

[Batch record](../../batches/B057/README.md)
