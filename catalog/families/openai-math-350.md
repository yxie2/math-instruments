---
id: openai-math-350
record_type: family
title: Normalized logarithmic potentials and local affine correction
source_family: '350'
source_collection: openai/math
batch_id: B085
subject: Differential geometry
source_paper_ids:
- P-000521
instrument_ids:
- MI-000788
- MI-000789
headline: The family claims sharp surface nodal length and higher-dimensional counterexamples to nodal
  upper bounds.
central_instrument: Control the mass of a logarithmic potential from one normalization, then remove its
  far-field affine part before averaging growth.
novelty_assessment: Classical mechanisms are identified explicitly; exact priority of source-specific
  interfaces is not established.
formalization_summary: Read the full scope and all three complete Comparators. Their targets concern surface
  nodal length and two higher-dimensional constructions. Targets have sorry; no separate solution or Lean
  build was checked.
statement_faithfulness: The profile is subharmonic, nonpositive and nontrivial. The source measure is
  nonnegative; atoms are allowed. Constants depend on the fixed outer radius.
dependencies: Submean inequalities, the Riesz measure, harmonic interior estimates, disk averages and
  dyadic annuli.
antecedents: Classical planar potential theory and Taylor subtraction of a far-field singular kernel.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Normalized logarithmic potentials and local affine correction

## Source manuscripts and claim

- [Sharp nodal length on smooth surfaces](../papers/P-000521.md): selected passages extracted.

The following companions are inventoried but have no extraction in this batch:

- [Smooth counterexamples to Yau's nodal upper bound in dimensions three and four](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Smooth-counterexamples-to-Yaus-nodal-upper-bound-in-dimensions-three-and-four-September-23-2026)
- [Power-law violations of Yau's nodal upper bound](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Power-law-violations-of-Yaus-nodal-upper-bound-September-23-2026)

The family claims sharp surface nodal length and higher-dimensional counterexamples to nodal upper bounds.

## Extracted instruments

- [MI-000788: Normalize a subharmonic profile to control its logarithmic potential](../instruments/MI-000788.md)
- [MI-000789: Subtract the far-field slope before averaging logarithmic growth](../instruments/MI-000789.md)

## Dependencies and antecedents

Submean inequalities, the Riesz measure, harmonic interior estimates, disk averages and dyadic annuli.

Classical planar potential theory and Taylor subtraction of a far-field singular kernel.

## Review and formalization scope

Read complete uniform potential decomposition and affine-profile correction proofs and the growth definitions. Two companions are inventory-only. Subharmonic extraction from eigenfunctions, persistence packing and the final nodal theorem were not certified.

Read the full scope and all three complete Comparators. Their targets concern surface nodal length and two higher-dimensional constructions. Targets have sorry; no separate solution or Lean build was checked.

The profile is subharmonic, nonpositive and nontrivial. The source measure is nonnegative; atoms are allowed. Constants depend on the fixed outer radius.

[Batch record](../../batches/B085/README.md)
