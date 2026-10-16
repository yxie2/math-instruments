---
id: openai-math-135
record_type: family
title: Product-rank bottlenecks and uniform-composition moments
source_family: '135'
source_collection: openai/math
batch_id: B024
subject: Theoretical computer science
source_paper_ids:
- P-000167
instrument_ids:
- MI-000296
- MI-000297
headline: The source claims a characteristic-zero lower bound n^(sqrt(n)/400) for homogeneous depth-five
  circuits computing the (1,1) entry of a product of n generic n-by-n matrices, for sufficiently large
  n, without a bottom-support restriction.
central_instrument: Order commuting differential-multiplication factors by signed degree discrepancy to
  expose an intermediate dimension bottleneck. Compare uniform-composition factorial moments with independent
  geometric moments.
novelty_assessment: Degree-residue arguments in circuit lower bounds and composition factorial moments
  have established antecedents. The extracted operator ordering and quantitative comparison are useful
  source formulations, not certified new theorems.
formalization_summary: Read the depth-five scope and DepthFive.lean Comparator, including the shared-DAG
  circuit model, repeated product inputs, gate count including leaves, characteristic-zero lower bound
  and all-field upper bound. These are inspected target statements with sorry placeholders; no Lean solution
  was built or kernel-checked.
statement_faithfulness: The differential operator is multiplicative before taking a fixed bidegree component;
  the fixed-component map is not multiplicative. Moment comparison requires nonnegative coefficients in
  the falling-factorial basis.
dependencies: Commuting operators on disjoint variable groups, ranks through intermediate homogeneous
  spaces, stars-and-bars generating functions and elementary logarithmic inequalities.
antecedents: Amireddy-Garg-Kayal-Saha-Thankey degree residue; classical weak-composition and geometric
  factorial moments.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Product-rank bottlenecks and uniform-composition moments

## Source manuscript and claim

[Homogeneous depth-five lower bounds for iterated matrix multiplication](../papers/P-000167.md), by OpenAI, None.

The source claims a characteristic-zero lower bound n^(sqrt(n)/400) for homogeneous depth-five circuits computing the (1,1) entry of a product of n generic n-by-n matrices, for sufficiently large n, without a bottom-support restriction.

## Extracted instruments

- [MI-000296: Order positive degree discrepancies first to expose a rank bottleneck](../instruments/MI-000296.md)
- [MI-000297: Uniform weak compositions are dominated in the nonnegative factorial basis](../instruments/MI-000297.md)

## Dependencies and antecedents

Commuting operators on disjoint variable groups, ranks through intermediate homogeneous spaces, stars-and-bars generating functions and elementary logarithmic inequalities.

Amireddy-Garg-Kayal-Saha-Thankey degree residue; classical weak-composition and geometric factorial moments. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the complete product-rank proof and occupation-moment lemma. The IMM trace lower bound and the asymptotic word/path summation were not audited.

Read the depth-five scope and DepthFive.lean Comparator, including the shared-DAG circuit model, repeated product inputs, gate count including leaves, characteristic-zero lower bound and all-field upper bound. These are inspected target statements with sorry placeholders; no Lean solution was built or kernel-checked.

The differential operator is multiplicative before taking a fixed bidegree component; the fixed-component map is not multiplicative. Moment comparison requires nonnegative coefficients in the falling-factorial basis.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/135.md) · [Batch record](../../batches/B024/README.md)
