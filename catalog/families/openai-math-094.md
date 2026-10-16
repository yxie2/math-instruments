---
id: openai-math-094
record_type: family
title: Relative moment criteria and coordinate obstructions for Lp dimension reduction
source_family: 094
source_collection: openai/math
batch_id: B003
subject: Convex and metric geometry
source_paper_ids:
- P-000087
instrument_ids:
- MI-000127
- MI-000128
- MI-000129
headline: The source claims subpolynomial coordinate dimension for fixed distortion D>1 and fixed 1<p<infinity,
  with p!=2, while exact embeddings require quadratic-order dimension in the number of points.
central_instrument: Convex separation converts weighted relative-moment tests into one distribution of
  coordinates; electrical-flow reweighting controls its projection, while antipodal support incidences
  obstruct exact compression.
novelty_assessment: The sampling and electrical localization inputs have explicit antecedents. The relative-moment
  formulation, its projection assembly and the exact-support configuration are extracted as candidate
  reusable combinations, without a priority certification.
formalization_summary: The SubpolynomialLp Comparator records the universal coordinate-dimension bounds,
  attainment and logarithmic limits for p>1, p!=2, including D=1. It permits arbitrary real Lp inputs
  and unrestricted maps. No Lean solution was built.
statement_faithfulness: The target is coordinate ell_p with the same exponent, the maps need not be linear,
  and the constants depend on fixed p and D. Exact, finite-distortion and fixed infinite-set questions
  are different.
dependencies: Finite-dimensional convex separation, Carathéodory, bounded sampling, the electrical-flow
  localization theorem and Brouwer fixed points; the full upper bound additionally uses stable or signed-Poisson
  constructions.
antecedents: Ball gives the exact-coordinate upper bound and quadratic sharpness below two; Lamperti supplies
  disjoint-support detection; Eskenazis uses empirical approximation of distance matrices; Gurel-Gurevich–Nachmias–Sachdeva
  supply the electrical localization estimate.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Relative moment criteria and coordinate obstructions for Lp dimension reduction

## Source manuscript and claim

[Subpolynomial dimension reduction in Lp](../papers/P-000087.md), by OpenAI, September 23, 2026.

The source claims subpolynomial coordinate dimension for fixed distortion D>1 and fixed 1<p<infinity, with p!=2, while exact embeddings require quadratic-order dimension in the number of points.

## Extracted instruments

- [MI-000127: Weighted relative moments can be separated into simultaneous embedding coordinates](../instruments/MI-000127.md)
- [MI-000128: A fixed-point reweighting turns average electrical localization into uniform row control](../instruments/MI-000128.md)
- [MI-000129: Antipodal row and column incidences force quadratic exact coordinate dimension](../instruments/MI-000129.md)

## Dependencies and antecedents

Finite-dimensional convex separation, Carathéodory, bounded sampling, the electrical-flow localization theorem and Brouwer fixed points; the full upper bound additionally uses stable or signed-Poisson constructions.

Ball gives the exact-coordinate upper bound and quadratic sharpness below two; Lamperti supplies disjoint-support detection; Eskenazis uses empirical approximation of distance matrices; Gurel-Gurevich–Nachmias–Sachdeva supply the electrical localization estimate. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the weighted-moment, projection and exact-obstruction arguments in full. Checked weighted projection examples and exact row/column defect identities. The heavy-tail construction and all estimates giving the main subpolynomial upper bound were not independently audited.

The SubpolynomialLp Comparator records the universal coordinate-dimension bounds, attainment and logarithmic limits for p>1, p!=2, including D=1. It permits arbitrary real Lp inputs and unrestricted maps. No Lean solution was built.

The target is coordinate ell_p with the same exponent, the maps need not be linear, and the constants depend on fixed p and D. Exact, finite-distortion and fixed infinite-set questions are different.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/094.md) · [Batch record](../../batches/B003/README.md)
