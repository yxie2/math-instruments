---
id: openai-math-226
record_type: family
title: Damped exterior insertions and positivity for double-dimer curves
source_family: '226'
source_collection: openai/math
batch_id: B006
subject: Probability and statistical mechanics
source_paper_ids:
- P-000097
instrument_ids:
- MI-000150
- MI-000151
headline: The source claims convergence of all nested half-plane Temperleyan double-dimer loops as curves
  to nested CLE4, strengthening established puncture and nesting-field information. This extraction selects
  the short-segment operator and positivity mechanisms.
central_instrument: Two-particle insertion coefficients are minors of a localized projection; spectral
  damping controls their state sum. Geometrically decaying cap weights make the resulting signed observable
  nonnegative.
novelty_assessment: Transfer matrices, exterior powers and Cauchy-Binet are established. The candidate
  combination is the damped short-segment insertion with cap-local nesting weights and quantitative positivity.
  The full curve limit and historical priority remain unverified here.
formalization_summary: No family-specific formalization scope document is listed in the pinned release
  inventory. No Comparator comparison or Lean proof build is claimed.
statement_faithfulness: The source concerns the standard half-plane Temperleyan law and matching of loops
  as unrooted curves with multiplicities, not merely convergence of loop traces or finite puncture data.
  Its limits take the mesh to zero before the short interval and cap cutoff limits.
dependencies: Lieb transfer matrices and open-boundary singular modes; exterior-algebra insertion signs;
  summable damped occupation weights; planar nesting and alternating intersection signs; marked-cap normalization.
antecedents: Lieb and Rasmussen-Ruelle supply transfer and spectral precedents. Kenyon, Dubedat, Basok-Chelkak,
  Bai-Wan and Basok-Izyurov supply topological and nesting-field convergence. Those results are not themselves
  the new geometric estimates selected here.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Damped exterior insertions and positivity for double-dimer curves

## Source manuscript and claim

[The curve scaling limit of half-plane double dimers](../papers/P-000097.md), by OpenAI, None.

The source claims convergence of all nested half-plane Temperleyan double-dimer loops as curves to nested CLE4, strengthening established puncture and nesting-field information. This extraction selects the short-segment operator and positivity mechanisms.

## Extracted instruments

- [MI-000150: Delocalized exterior minors and spectral damping give a quadratic short-interval bound](../instruments/MI-000150.md)
- [MI-000151: Geometric nesting weights make a two-chain signed observable quantitatively positive](../instruments/MI-000151.md)

## Dependencies and antecedents

Lieb transfer matrices and open-boundary singular modes; exterior-algebra insertion signs; summable damped occupation weights; planar nesting and alternating intersection signs; marked-cap normalization.

Lieb and Rasmussen-Ruelle supply transfer and spectral precedents. Kenyon, Dubedat, Basok-Chelkak, Bai-Wan and Basok-Izyurov supply topological and nesting-field convergence. Those results are not themselves the new geometric estimates selected here. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the spectral state-sum proof, sandwiched insertion proof, color contraction calculation and cap-weight positivity argument. The localization via Wilson sampling and the full no-backtracking identification were not audited in detail.

No family-specific formalization scope document is listed in the pinned release inventory. No Comparator comparison or Lean proof build is claimed.

The source concerns the standard half-plane Temperleyan law and matching of loops as unrooted curves with multiplicities, not merely convergence of loop traces or finite puncture data. Its limits take the mesh to zero before the short interval and cap cutoff limits.

[Batch record](../../batches/B006/README.md)
