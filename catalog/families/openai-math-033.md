---
id: openai-math-033
record_type: family
title: Finite section-ring pullback and norm descent of global generation
source_family: '033'
source_collection: openai/math
batch_id: B067
subject: Algebraic and complex geometry
source_paper_ids:
- P-000409
- P-000410
instrument_ids:
- MI-000640
- MI-000641
headline: The family concerns orbifold/logarithmic Iitaka inequalities and b-semiampleness.
central_instrument: Integral section-ring extensions preserve Iitaka dimension. A norm along the finite
  Stein factor descends global generation with a uniform explicit exponent.
novelty_assessment: The cards identify classical mechanisms and source-specific quantitative interfaces.
  No exhaustive novelty assessment or certification of the global headline is claimed.
formalization_summary: The scope document and all 245 lines of LogKodairaFiberNegative were read. It targets
  only the negative-fiber branch of logarithmic additivity for stratum-smooth connected-fiber SNC pairs,
  with vanishing of every positive-degree log pluriform. The finite-dimension and negative-base branches
  are outside the target. The target has a sorry body and belongs to an inventory-only companion. No separate
  solution or Lean build was checked.
statement_faithfulness: The section-ring argument uses normal projective varieties and rational Cartier
  divisors. Analytic semiampleness descent uses proper surjectivity, compactness and normality of the
  base, without finite flatness.
dependencies: Codimension-one regularity, characteristic polynomials, Stein factorization, analytic norms
  and hyperplane avoidance.
antecedents: Classical norm and section-ring arguments; Stacks Project Norms supplies the algebraic finite-map
  counterparts.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Finite section-ring pullback and norm descent of global generation

## Source manuscripts and claim

- [Orbifold and logarithmic Iitaka subadditivity](../papers/P-000409.md): selected passages extracted.
- [B-semiampleness for compact log-smooth Kähler fibrations](../papers/P-000410.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [Logarithmic Kodaira dimension and whole-fiber variation](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Logarithmic-Kodaira-dimension-and-whole-fiber-variation-September-26-2026)
- [The reverse logarithmic Kodaira inequality and additivity](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-reverse-logarithmic-Kodaira-inequality-and-additivity-September-26-2026)
- [Projective Hodge lines and ordinary Iitaka subadditivity](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Projective-Hodge-lines-and-ordinary-Iitaka-subadditivity-September-27-2026)

The family concerns orbifold/logarithmic Iitaka inequalities and b-semiampleness.

## Extracted instruments

- [MI-000640: Preserve Iitaka dimension by integral finite pullback of section rings](../instruments/MI-000640.md)
- [MI-000641: Descend a globally generated power through the finite Stein norm](../instruments/MI-000641.md)

## Dependencies and antecedents

Codimension-one regularity, characteristic polynomials, Stein factorization, analytic norms and hyperplane avoidance.

Classical norm and section-ring arguments; Stacks Project Norms supplies the algebraic finite-map counterparts.

## Review and formalization scope

Read the complete divisorial section test, finite-pullback proof and analytic semiampleness-descent proof. Two of five manuscripts receive extractions; three companions remain inventory-only. Period positivity, Hodge-line comparison and subadditivity are not certified.

The scope document and all 245 lines of LogKodairaFiberNegative were read. It targets only the negative-fiber branch of logarithmic additivity for stratum-smooth connected-fiber SNC pairs, with vanishing of every positive-degree log pluriform. The finite-dimension and negative-base branches are outside the target. The target has a sorry body and belongs to an inventory-only companion. No separate solution or Lean build was checked.

The section-ring argument uses normal projective varieties and rational Cartier divisors. Analytic semiampleness descent uses proper surjectivity, compactness and normality of the base, without finite flatness.

[Batch record](../../batches/B067/README.md)
