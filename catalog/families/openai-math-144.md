---
id: openai-math-144
record_type: family
title: Finite phase substitution and spectral normalization
source_family: '144'
source_collection: openai/math
batch_id: B014
subject: Dynamical systems and ergodic theory
source_paper_ids:
- P-000127
instrument_ids:
- MI-000213
- MI-000214
headline: The source claims a smooth volume-preserving diffeomorphism of the three-torus with simple Lebesgue
  spectrum on mean-zero functions and a real cyclic vector whose integer iterates form an orthonormal
  basis.
central_instrument: A superincreasing choice of integer frequencies reproduces finitely many product-phase
  integrals. Spectral functional calculus then normalizes a packet even where its spectral density vanishes.
novelty_assessment: Both selected tools use established Fourier and spectral principles. Their concrete
  interfaces are useful extractions; the headline construction and its priority are not certified here.
formalization_summary: ThreeTorus.lean includes smoothness of the map and inverse, volume preservation,
  a real mean-zero orthonormal cyclic orbit, ergodicity and an intertwining spectral representation. Scope
  text and Comparator statements were read. No Lean solution was built or kernel-checked; the extracted
  auxiliary lemmas are not separately certified targets.
statement_faithfulness: Phase substitution is for a prescribed finite list of tests. A vector with flat
  spectral density need not be cyclic. The zero-density correction requires another flat vector for the
  same operator.
dependencies: Riemann-Lebesgue decay, separated integer frequencies, spectral measures, measurable functional
  calculus and orthogonal spectral projections.
antecedents: Fourier decay and the spectral theorem are classical. Taylor, Spectral Theory, Section 1
  gives the normal-operator multiplication representation used in the comparison.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Finite phase substitution and spectral normalization

## Source manuscript and claim

[A smooth three-torus diffeomorphism with simple Lebesgue spectrum](../papers/P-000127.md), by OpenAI, September 23, 2026.

The source claims a smooth volume-preserving diffeomorphism of the three-torus with simple Lebesgue spectrum on mean-zero functions and a real cyclic vector whose integer iterates form an orthonormal basis.

## Extracted instruments

- [MI-000213: Separated integer frequencies reproduce a finite collection of phase averages](../instruments/MI-000213.md)
- [MI-000214: Spectral whitening fills zero-density sets without an inverse lower bound](../instruments/MI-000214.md)

## Dependencies and antecedents

Riemann-Lebesgue decay, separated integer frequencies, spectral measures, measurable functional calculus and orthogonal spectral projections.

Fourier decay and the spectral theorem are classical. Taylor, Spectral Theory, Section 1 gives the normal-operator multiplication representation used in the comparison. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the finite phase-test proof, flat-vector construction, whitening formula and spectral-density continuity estimate. The iterative smooth construction and final cyclicity argument were not audited.

ThreeTorus.lean includes smoothness of the map and inverse, volume preservation, a real mean-zero orthonormal cyclic orbit, ergodicity and an intertwining spectral representation. Scope text and Comparator statements were read. No Lean solution was built or kernel-checked; the extracted auxiliary lemmas are not separately certified targets.

Phase substitution is for a prescribed finite list of tests. A vector with flat spectral density need not be cyclic. The zero-density correction requires another flat vector for the same operator.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/144.md) · [Batch record](../../batches/B014/README.md)
