---
id: openai-math-324
record_type: family
title: Transporting graph norms and absorbing a lifted correction
source_family: '324'
source_collection: openai/math
batch_id: B048
subject: Functional analysis
source_paper_ids:
- P-000265
- P-000266
instrument_ids:
- MI-000486
- MI-000487
headline: The sources claim separable Banach counterexamples to linear classification under bi-Lipschitz
  equivalence, including nonlinear c0 absorption without a linear c0 copy.
central_instrument: An intertwining identity transports both parts of a weighted graph norm. An exact
  lifted correction gives an explicit absorption inverse without assuming its linear projection is onto.
novelty_assessment: Classical triangular change-of-variable mechanisms, related to Aharoni-Lindenstrauss
  and Godefroy-Kalton. The difficult infinite-dimensional constructions and linear obstructions remain
  unverified here.
formalization_summary: The supplied targets assert nonisomorphic bi-Lipschitz equivalent separable spaces,
  with specified constants, and a separable space absorbing c0 while containing no linear c0 copy. The
  scope document and linked Comparator definitions and target statements were read. The inspected targets
  contain sorry; no solution or Lean project was built.
statement_faithfulness: The maps intertwine nonlinearly; this does not supply a Lipschitz right inverse
  of the linear operator. Norm-null image sequences and the exact correction identity are essential.
dependencies: Bi-Lipschitz bijections, bounded linear maps, zero-preserving intertwining maps, weighted
  sequence sums and explicit inverse formulas.
antecedents: Godefroy-Kalton Theorem 2.12 gives a triangular free-space splitting; Corollary 3.2 concerns
  actual Lipschitz right inverses and requires separate hypotheses.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Transporting graph norms and absorbing a lifted correction

## Source manuscripts and claim

- [Lipschitz Equivalent Separable Banach Spaces Need Not Be Linearly Isomorphic](../papers/P-000265.md): selected passages extracted.
- [Bi-Lipschitz Absorption of c0 Without a Linear Copy of c0](../papers/P-000266.md): selected passages extracted.

The sources claim separable Banach counterexamples to linear classification under bi-Lipschitz equivalence, including nonlinear c0 absorption without a linear c0 copy.

## Extracted instruments

- [MI-000486: Transport a weighted graph norm through an intertwining bijection](../instruments/MI-000486.md)
- [MI-000487: Build an absorption bijection from an exactly lifted correction](../instruments/MI-000487.md)

## Dependencies and antecedents

Bi-Lipschitz bijections, bounded linear maps, zero-preserving intertwining maps, weighted sequence sums and explicit inverse formulas.

Godefroy-Kalton Theorem 2.12 gives a triangular free-space splitting; Corollary 3.2 concerns actual Lipschitz right inverses and requires separate hypotheses.

## Review and formalization scope

Read the full weighted graph criterion and lifted-correction absorption proof, plus the graph-space completeness argument. Only the transport and inverse interfaces are extracted; neither the special nonlinear maps nor their linear-obstruction properties were certified. Both manuscripts have selected extractions.

The supplied targets assert nonisomorphic bi-Lipschitz equivalent separable spaces, with specified constants, and a separable space absorbing c0 while containing no linear c0 copy. The scope document and linked Comparator definitions and target statements were read. The inspected targets contain sorry; no solution or Lean project was built.

The maps intertwine nonlinearly; this does not supply a Lipschitz right inverse of the linear operator. Norm-null image sequences and the exact correction identity are essential.

[Batch record](../../batches/B048/README.md)
