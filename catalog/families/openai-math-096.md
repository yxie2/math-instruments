---
id: openai-math-096
record_type: family
title: Deletion loss and residual-score geometry for Gaussian partitions
source_family: 096
source_collection: openai/math
batch_id: B004
subject: Convex and metric geometry
source_paper_ids:
- P-000091
instrument_ids:
- MI-000138
- MI-000139
headline: The source claims the all-dimensional Gaussian propeller bound 9/(8 pi), using the established
  three-dimensional theorem and new constraints on extremizers with at least five active cells.
central_instrument: Deleting one Gaussian score produces a loss bracket via extremality and Ehrhard concavity;
  zero residual first moments turn two competing scores into a covariance-determinant constraint.
novelty_assessment: Candidate combinations built on Khot–Naor extremal reduction, Ehrhard’s inequality
  and the Heilman–Jagannath–Naor three-dimensional theorem. The global elimination and priority are not
  certified here.
formalization_summary: GaussianPropeller targets the bound for arbitrary finite labelled measurable partitions,
  empty cells and unrestricted masses, plus attainment by three planar sectors in dimensions at least
  two. Kernel-clustering and Gaussian-maxima consequences are outside this selected Comparator. No Lean
  solution was built.
statement_faithfulness: Centroids are unnormalized Gaussian first moments. The extracted score bounds
  are for the source’s minimal-active-cell optimal configuration, not arbitrary collections of vectors.
dependencies: Gaussian maximum duality; minimal-cell extremizers and their Gram Laplacian; Ehrhard concavity
  for convex translates; residual Gaussian independence; a planar positive-part integral.
antecedents: Khot–Naor provide the conical partition reduction and clustering context; Heilman–Jagannath–Naor
  prove the three-dimensional bound; Ehrhard/Borell supply Gaussian Minkowski concavity.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Deletion loss and residual-score geometry for Gaussian partitions

## Source manuscript and claim

[The Gaussian propeller bound in every dimension](../papers/P-000091.md), by OpenAI, None.

The source claims the all-dimensional Gaussian propeller bound 9/(8 pi), using the established three-dimensional theorem and new constraints on extremizers with at least five active cells.

## Extracted instruments

- [MI-000138: Deletion and Gaussian translation bracket the loss of a winning score](../instruments/MI-000138.md)
- [MI-000139: Zero residual moments turn two-score competition into a determinant bound](../instruments/MI-000139.md)

## Dependencies and antecedents

Gaussian maximum duality; minimal-cell extremizers and their Gram Laplacian; Ehrhard concavity for convex translates; residual Gaussian independence; a planar positive-part integral.

Khot–Naor provide the conical partition reduction and clustering context; Heilman–Jagannath–Naor prove the three-dimensional bound; Ehrhard/Borell supply Gaussian Minkowski concavity. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the extremal reduction, deletion-loss estimates and two-competing-score proof. Checked the translation derivative, normalization and triangle integral. The scalar certificate tables and elimination of all radius configurations were not fully reproduced.

GaussianPropeller targets the bound for arbitrary finite labelled measurable partitions, empty cells and unrestricted masses, plus attainment by three planar sectors in dimensions at least two. Kernel-clustering and Gaussian-maxima consequences are outside this selected Comparator. No Lean solution was built.

Centroids are unnormalized Gaussian first moments. The extracted score bounds are for the source’s minimal-active-cell optimal configuration, not arbitrary collections of vectors.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/096.md) · [Batch record](../../batches/B004/README.md)
