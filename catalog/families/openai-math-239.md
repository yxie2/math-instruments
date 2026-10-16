---
id: openai-math-239
record_type: family
title: Stable lattice quotients and phase-uniform Gaussian Fourier bounds
source_family: '239'
source_collection: openai/math
batch_id: B054
subject: Probability and statistical mechanics
source_paper_ids:
- P-000304
- P-000305
instrument_ids:
- MI-000535
- MI-000536
headline: The sources claim sharp exponential singularity rates for symmetric Bernoulli matrices and biased
  symmetric sign matrices.
central_instrument: Minimizing a normalized sublattice determinant leaves a stable orthogonal quotient.
  Poisson summation converts a Fourier product into a positive Gaussian translate ratio, permitting uniform
  removal of phases.
novelty_assessment: Stable lattice filtration and Gaussian translate bounds have direct classical antecedents
  summarized by Regev-Stephens-Davidowitz. The selected source combines these tools with its own random-matrix
  separation inputs, which remain unverified.
formalization_summary: No family scope document or Comparator target is listed in the pinned inventory.
  No formal verification is claimed.
statement_faithfulness: Lattice quotients are orthogonal Euclidean quotients of primitive sublattices.
  Fourier decay is conditional on separated subset sums; positivity of the Gaussian ratio is what allows
  the phases to be discarded.
dependencies: Discrete exterior-power lattices, saturation, determinant factorization, Poisson summation,
  Gaussian tails and Bernoulli pattern probabilities.
antecedents: Canonical stable lattice filtration and Gaussian estimates in Regev-Stephens-Davidowitz,
  with earlier Harder-Narasimhan, Stuhler, Grayson and Banaszczyk antecedents noted there.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Stable lattice quotients and phase-uniform Gaussian Fourier bounds

## Source manuscripts and claim

- [The sharp exponential rate of singularity for symmetric Bernoulli matrices](../papers/P-000304.md): selected passages extracted.
- [The sharp singularity rate for biased symmetric sign matrices](../papers/P-000305.md): selected passages extracted.

The sources claim sharp exponential singularity rates for symmetric Bernoulli matrices and biased symmetric sign matrices.

## Extracted instruments

- [MI-000535: Minimize normalized covolume to obtain a stable orthogonal lattice quotient](../instruments/MI-000535.md)
- [MI-000536: Discard Fourier phases through a positive lattice Gaussian ratio](../instruments/MI-000536.md)

## Dependencies and antecedents

Discrete exterior-power lattices, saturation, determinant factorization, Poisson summation, Gaussian tails and Bernoulli pattern probabilities.

Canonical stable lattice filtration and Gaussian estimates in Regev-Stephens-Davidowitz, with earlier Harder-Narasimhan, Stuhler, Grayson and Banaszczyk antecedents noted there.

## Review and formalization scope

Read the full determinant minimization and quotient proofs, and the full dual Fourier average proof. The lattice separation construction, exceptional-set bounds and claimed sharp singularity theorems were not certified.

No family scope document or Comparator target is listed in the pinned inventory. No formal verification is claimed.

Lattice quotients are orthogonal Euclidean quotients of primitive sublattices. Fourier decay is conditional on separated subset sums; positivity of the Gaussian ratio is what allows the phases to be discarded.

[Batch record](../../batches/B054/README.md)
