---
id: openai-math-232
record_type: family
title: Rounded midpoint amplification and scalar transfer spectra
source_family: '232'
source_collection: openai/math
batch_id: B080
subject: Probability and statistical mechanics
source_paper_ids:
- P-000498
instrument_ids:
- MI-000742
- MI-000743
headline: The family claims Gaussian free-field limits for integer and real Lipschitz surfaces.
central_instrument: Amplify central mass through a rounded midpoint inequality; retain endpoint spectral
  atoms when extending positive transfer powers.
novelty_assessment: Classical ingredients are credited; exact novelty of the source-specific assembly
  is not established.
formalization_summary: No family scope is supplied in the inventory. No Lean verification is claimed.
statement_faithfulness: Weights x^energy require 0<x<=1. Central mass is unconditional in every class.
  Spectral operators commute and the transfer operator is a positive self-adjoint contraction.
dependencies: Discrete midpoint entropy inequality, parity bookkeeping, quadratic tail recursion, positive
  Fejer kernels and Bernstein polynomials.
antecedents: Klartag-Lehec and Gozlan-Roberto-Samson-Tetali midpoint inequalities; classical scalar spectral
  representations.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Rounded midpoint amplification and scalar transfer spectra

## Source manuscripts and claim

- [Gaussian free-field limits of weighted integer Lipschitz heights](../papers/P-000498.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [The Gaussian free field limit of integer Lipschitz heights with two-arc boundary data](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Gaussian-free-field-limit-of-integer-Lipschitz-heights-with-two-arc-boundary-data-October-6-2026)
- [Uniform real Lipschitz surfaces on the triangular lattice](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Uniform-real-Lipschitz-surfaces-on-the-triangular-lattice-October-6-2026)

The family claims Gaussian free-field limits for integer and real Lipschitz surfaces.

## Extracted instruments

- [MI-000742: Amplify classwise central mass using rounded midpoint weights](../instruments/MI-000742.md)
- [MI-000743: Construct scalar transfer measures while preserving zero and unit eigenvalues](../instruments/MI-000743.md)

## Dependencies and antecedents

Discrete midpoint entropy inequality, parity bookkeeping, quadratic tail recursion, positive Fejer kernels and Bernstein polynomials.

Klartag-Lehec and Gozlan-Roberto-Samson-Tetali midpoint inequalities; classical scalar spectral representations.

## Review and formalization scope

Read complete midpoint, weighted-admissibility and amplification proofs and the entire scalar-spectra appendix. Two companions are inventory-only. No surface scaling limit or reflection-positivity input is certified.

No family scope is supplied in the inventory. No Lean verification is claimed.

Weights x^energy require 0<x<=1. Central mass is unconditional in every class. Spectral operators commute and the transfer operator is a positive self-adjoint contraction.

[Batch record](../../batches/B080/README.md)
