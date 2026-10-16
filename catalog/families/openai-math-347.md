---
id: openai-math-347
record_type: family
title: Integral chain bounds and finite-order Hamiltonian perturbations
source_family: '347'
source_collection: openai/math
batch_id: B085
subject: Differential geometry
source_paper_ids:
- P-000519
instrument_ids:
- MI-000784
- MI-000785
headline: The family claims fixed-point examples below stable-Morse, Morse or critical-number bounds in
  several dimensions.
central_instrument: Keep integral torsion in a stabilized Morse lower bound; use commutation and a short-period
  estimate to identify every fixed point after perturbation.
novelty_assessment: Classical mechanisms are identified explicitly; exact priority of source-specific
  interfaces is not established.
formalization_summary: Read the full scope and ArnoldCounterexample Comparator. Its target is the degenerate
  quadric example, not the selected nondegenerate dimension-22 manuscript. The target has sorry; no separate
  solution or Lean build was checked.
statement_faithfulness: The stable-Morse convention here is exactly quadratic outside a compact set. The
  perturbed map starts from a Hamiltonian involution and an invariant extension.
dependencies: Smith normal form, relative Morse theory, compact flow charts, symplectic eigenspaces and
  matrix exponentials.
antecedents: Classical torsion-sensitive Morse inequalities and finite-order perturbation methods.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Integral chain bounds and finite-order Hamiltonian perturbations

## Source manuscripts and claim

- [Hamiltonian Fixed Points Below the Stable Morse Number in Dimension Twenty-Two](../papers/P-000519.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [Sharpness of the Cyclic Integral Floer Bound Below the Stable Morse Number](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026)
- [Hamiltonian Fixed Points Below the Stable Morse Number](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026)
- [A nondegenerate counterexample to the Morse-number Arnold bound](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026)
- [Three fixed points on the symplectic quadric threefold](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026)

The family claims fixed-point examples below stable-Morse, Morse or critical-number bounds in several dimensions.

## Extracted instruments

- [MI-000784: Retain integral torsion in a Morse lower bound after stabilization](../instruments/MI-000784.md)
- [MI-000785: Square a commuting perturbation to locate all fixed points](../instruments/MI-000785.md)

## Dependencies and antecedents

Smith normal form, relative Morse theory, compact flow charts, symplectic eigenspaces and matrix exponentials.

Classical torsion-sensitive Morse inequalities and finite-order perturbation methods.

## Review and formalization scope

Read the complete free-chain bound, exact-quadratic stable lower-bound proof, short-period lemma and involution perturbation proposition. Four companions are inventory-only. The claimed counterexample manifolds, counts and handle cancellation are not certified.

Read the full scope and ArnoldCounterexample Comparator. Its target is the degenerate quadric example, not the selected nondegenerate dimension-22 manuscript. The target has sorry; no separate solution or Lean build was checked.

The stable-Morse convention here is exactly quadratic outside a compact set. The perturbed map starts from a Hamiltonian involution and an invariant extension.

[Batch record](../../batches/B085/README.md)
