---
id: openai-math-281
record_type: family
title: Bounded odd formula approximation and coercivity modulo a derivative
source_family: '281'
source_collection: openai/math
batch_id: B055
subject: Mathematical physics
source_paper_ids:
- P-000313
- P-000314
instrument_ids:
- MI-000544
- MI-000545
headline: The sources claim QAOA attainment of the SK optimum in a thermodynamic-first limit and full
  support of zero-temperature SK minimizers.
central_instrument: Approximate outer maps before their inputs to turn a finite odd Gaussian formula into
  bounded trigonometric controls. A rational polynomial identity turns an indefinite curvature integrand
  into positive terms after subtracting a zero-mean derivative.
novelty_assessment: Cutoff, odd symmetrization and Fourier approximation are classical. Sum-of-squares
  bounds modulo zero-mean derivatives have an established auxiliary-function precedent. The source particular
  rational certificate is checked algebraically without certifying its PDE sign hypotheses.
formalization_summary: SKValue states conditional Parisi value identities and convergence of finite Gaussian
  coefficient sums; it does not state convergence of QAOA circuit energies. SKFullSupport states full
  relative Stieltjes support and self-consistency moments for every admissible minimizer, without separately
  asserting existence. Both target proofs contain sorry. The scope document and every linked Comparator
  were read in full. No solution or Lean project was built.
statement_faithfulness: Formula approximation is for a fixed finite expression, with no uniform circuit-size
  or derivative bound. The coercive expectation inequality requires all sign, integrability and boundary
  assumptions; the original integrand is not pointwise positive.
dependencies: Gaussian moments and aggregation isometry, clipping, Lipschitz propagation and Fourier approximation;
  exact rational polynomial arithmetic, favorable sign constraints and integration by parts.
antecedents: Classical smooth approximation in Lp; auxiliary-function and sum-of-squares bounds for expectations
  as in Fantuzzi-Goluskin-Huang-Chernyshenko.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Bounded odd formula approximation and coercivity modulo a derivative

## Source manuscripts and claim

- [QAOA attains the SK ground-state energy in the thermodynamic-first limit](../papers/P-000313.md): selected passages extracted.
- [Full support of the zero-temperature Sherrington-Kirkpatrick order parameter](../papers/P-000314.md): selected passages extracted.

The sources claim QAOA attainment of the SK optimum in a thermodynamic-first limit and full support of zero-temperature SK minimizers.

## Extracted instruments

- [MI-000544: Approximate a finite odd Gaussian formula from its output toward its leaves](../instruments/MI-000544.md)
- [MI-000545: Prove an expectation inequality with an exact positive certificate modulo a derivative](../instruments/MI-000545.md)

## Dependencies and antecedents

Gaussian moments and aggregation isometry, clipping, Lipschitz propagation and Fourier approximation; exact rational polynomial arithmetic, favorable sign constraints and integration by parts.

Classical smooth approximation in Lp; auxiliary-function and sum-of-squares bounds for expectations as in Fantuzzi-Goluskin-Huang-Chernyshenko.

## Review and formalization scope

Read the complete bounded trigonometric approximation proof, the full rational certificate and integrated coercivity proof, and the derivative-rule/integration-by-parts lemma. The preceding shape inequalities, full-support theorem and quantum synthesis are not certified.

SKValue states conditional Parisi value identities and convergence of finite Gaussian coefficient sums; it does not state convergence of QAOA circuit energies. SKFullSupport states full relative Stieltjes support and self-consistency moments for every admissible minimizer, without separately asserting existence. Both target proofs contain sorry. The scope document and every linked Comparator were read in full. No solution or Lean project was built.

Formula approximation is for a fixed finite expression, with no uniform circuit-size or derivative bound. The coercive expectation inequality requires all sign, integrability and boundary assumptions; the original integrand is not pointwise positive.

[Batch record](../../batches/B055/README.md)
