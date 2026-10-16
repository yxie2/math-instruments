---
id: openai-math-093
record_type: family
title: Prediction and matrix tools for subgaussian log-concave measures
source_family: 093
source_collection: openai/math
batch_id: B004
subject: Convex and metric geometry
source_paper_ids:
- P-000090
instrument_ids:
- MI-000135
- MI-000136
- MI-000137
headline: The source claims a dimension-free logarithmic Sobolev bound from subgaussian linear marginals
  of a log-concave density. This extraction selects three auxiliary tools, not a certification of the
  long global argument.
central_instrument: An exact entropy-deficit change of reference, symmetric-slot averaging and an integrated
  spectral stability estimate separate analytic and matrix parts of the argument.
novelty_assessment: The trace-correlation input is established work. The particular deficit and scale-integrated
  formulations are candidate useful refinements; their historical priority and the global theorem remain
  unverified here.
formalization_summary: No family-specific formalization scope document is listed for 093 in the pinned
  release inventory. No Lean statement comparison or proof build is claimed.
statement_faithfulness: Linear subgaussianity is a tail condition in every direction, stronger than a
  covariance bound. The auxiliary statements below have their own hypotheses; they do not by themselves
  establish a dimension-free logarithmic Sobolev inequality.
dependencies: Logarithmic Sobolev Euler equations and integration by parts; positive correlation maps,
  weighted Schatten interpolation and Lieb trace concavity; scalar functional calculus and Tonelli integration.
antecedents: The Gaussian-channel and entropy-dissipation framework is classical. Lieb and Beigi supply
  trace-concavity/interpolation precedents. The source identifies its full target as the subgaussian log-concave
  conjecture of Bizeul.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Prediction and matrix tools for subgaussian log-concave measures

## Source manuscript and claim

[A dimension-free logarithmic Sobolev inequality for subgaussian log-concave measures](../papers/P-000090.md), by OpenAI, September 23, 2026.

The source claims a dimension-free logarithmic Sobolev bound from subgaussian linear marginals of a log-concave density. This extraction selects three auxiliary tools, not a certification of the long global argument.

## Extracted instruments

- [MI-000135: An entropy optimizer preserves the logarithmic Sobolev deficit under change of reference](../instruments/MI-000135.md)
- [MI-000136: Symmetric-slot averaging compares tensor actions with a geometric trace weight](../instruments/MI-000136.md)
- [MI-000137: Scale-integrated covariance maps are Lipschitz in Hilbert–Schmidt distance](../instruments/MI-000137.md)

## Dependencies and antecedents

Logarithmic Sobolev Euler equations and integration by parts; positive correlation maps, weighted Schatten interpolation and Lieb trace concavity; scalar functional calculus and Tonelli integration.

The Gaussian-channel and entropy-dissipation framework is classical. Lieb and Beigi supply trace-concavity/interpolation precedents. The source identifies its full target as the subgaussian log-concave conjecture of Bizeul. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the change-of-reference proof, symmetric-slot averaging proof and integrated covariance-stability proof. Finite checks test the trace bound, matrix stability and Gaussian deficit algebra. The critical-sequence construction, tensor hierarchy, entropy-loss comparison and final information contradiction were not fully audited.

No family-specific formalization scope document is listed for 093 in the pinned release inventory. No Lean statement comparison or proof build is claimed.

Linear subgaussianity is a tail condition in every direction, stronger than a covariance bound. The auxiliary statements below have their own hypotheses; they do not by themselves establish a dimension-free logarithmic Sobolev inequality.

[Batch record](../../batches/B004/README.md)
