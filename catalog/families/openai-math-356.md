---
id: openai-math-356
record_type: family
title: Bounded distance modifications and resolvent control under measure change
source_family: '356'
source_collection: openai/math
batch_id: B063
subject: Differential geometry
source_paper_ids:
- P-000379
- P-000380
instrument_ids:
- MI-000610
- MI-000611
headline: The sources claim a distributional characterization of Alexandrov curvature and transfer of
  weak Hessian bounds to every prescribed geodesic in finite-dimensional RCD spaces.
central_instrument: A monotone cutoff flattens model distance without worsening its radial Hessian coefficient.
  Original heat-flow resolvents control the weighted generator before any weighted curvature theorem is
  invoked.
novelty_assessment: The cutoff is classical chain-rule calculus. Brena-Gigli explicitly identify the regularity
  obstacle for measure changes; the selected source uses a bounded-drift resolvent argument under bounded
  Lipschitz weights.
formalization_summary: WeakHessian defines test-plan weak gradients, the nonpositive Laplacian, unreduced
  CD(K,N) and quadratic Cheeger energy. It assumes completeness, separability, full support and finite
  measure on bounded sets, N>1, bounded globally Lipschitz F and bounded continuous G. It concludes the
  distributional second derivative inequality for every constant-speed minimizing geodesic, including
  constants. It states neither the first manuscript curvature characterization nor a separate weighted
  generator theorem. All three available scope documents and all three linked Comparators in this batch
  were read in full. Their target theorems have sorry proof bodies. No separate solution or Lean project
  was built.
statement_faithfulness: Distance flattening is conditional on the stated local Hessian comparison. Bounded
  weights preserve the generator domain, not automatically the test-function class. Finite models check
  the contraction mechanism only.
dependencies: Distributional chain rules, model sine functions, equivalent weighted Sobolev norms, heat-gradient
  bounds, resolvents and Banach contraction.
antecedents: Classical Hessian comparison and bounded drift; Brena-Gigli Remark 2.4 identifies the weighted
  regularity issue.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Bounded distance modifications and resolvent control under measure change

## Source manuscripts and claim

- [Gigli’s distributional curvature characterization of Alexandrov spaces](../papers/P-000379.md): selected passages extracted.
- [Weak Hessian bounds along every geodesic in RCD spaces](../papers/P-000380.md): selected passages extracted.

The sources claim a distributional characterization of Alexandrov curvature and transfer of weak Hessian bounds to every prescribed geodesic in finite-dimensional RCD spaces.

## Extracted instruments

- [MI-000610: Flatten model distance while keeping its upper Hessian bound](../instruments/MI-000610.md)
- [MI-000611: Obtain weighted-generator regularity from the original heat resolvent](../instruments/MI-000611.md)

## Dependencies and antecedents

Distributional chain rules, model sine functions, equivalent weighted Sobolev norms, heat-gradient bounds, resolvents and Banach contraction.

Classical Hessian comparison and bounded drift; Brena-Gigli Remark 2.4 identifies the weighted regularity issue.

## Review and formalization scope

Read the full bounded-modification proof and full bounded-drift proof, plus source background on the generator/test-class distinction. The distributional curvature theorem, weighted Bochner closure and every-geodesic conclusion remain unaudited.

WeakHessian defines test-plan weak gradients, the nonpositive Laplacian, unreduced CD(K,N) and quadratic Cheeger energy. It assumes completeness, separability, full support and finite measure on bounded sets, N>1, bounded globally Lipschitz F and bounded continuous G. It concludes the distributional second derivative inequality for every constant-speed minimizing geodesic, including constants. It states neither the first manuscript curvature characterization nor a separate weighted generator theorem. All three available scope documents and all three linked Comparators in this batch were read in full. Their target theorems have sorry proof bodies. No separate solution or Lean project was built.

Distance flattening is conditional on the stated local Hessian comparison. Bounded weights preserve the generator domain, not automatically the test-function class. Finite models check the contraction mechanism only.

[Batch record](../../batches/B063/README.md)
