---
id: openai-math-052
record_type: family
title: Parallel metric orthogonalization and transport on supplied tangent boxes
source_family: '052'
source_collection: openai/math
batch_id: B069
subject: Algebraic and complex geometry
source_paper_ids:
- P-000427
- P-000428
instrument_ids:
- MI-000658
- MI-000659
headline: The sources claim universal-cover product splitting and automatic integrability of rationally
  connected tangent splittings.
central_instrument: Parallel projectors orthogonalize a metric without changing its completion. A projected-bracket
  connection transports bundles across an existing rational tangent box.
novelty_assessment: The cards distinguish established antecedents from explicit source calculations. No
  exhaustive priority determination or headline-theorem certification is claimed.
formalization_summary: The scope and both Comparators were read in full. KahlerSplitting assumes both
  positive-rank summands are integrable and targets a compatible biholomorphic universal-cover product.
  SplitTangentIntegrability separately targets integrability of both summands on a projectively embedded
  rationally connected compact complex manifold; it does not include the compatible product conclusion.
  Both targets have sorry bodies. No separate solution or Lean build was checked.
statement_faithfulness: Parallelism and the metric completion identification are inputs to the first card.
  Existence of a global tangent box is an input to the second, not a conclusion of its transport argument.
dependencies: Parallel tensors, Levi-Civita uniqueness, metric completions, holomorphic relative connections
  and simply connected rational curves.
antecedents: Classical Riemannian product geometry and flat holomorphic connection transport.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Parallel metric orthogonalization and transport on supplied tangent boxes

## Source manuscripts and claim

- [Universal-cover splitting for compact Kähler manifolds](../papers/P-000427.md): selected passages extracted.
- [Integrability of split tangent bundles on rationally connected manifolds](../papers/P-000428.md): selected passages extracted.

The sources claim universal-cover product splitting and automatic integrability of rationally connected tangent splittings.

## Extracted instruments

- [MI-000658: Orthogonalize parallel summands without changing the metric completion](../instruments/MI-000658.md)
- [MI-000659: Transport complementary bundles across an existing rational tangent box](../instruments/MI-000659.md)

## Dependencies and antecedents

Parallel tensors, Levi-Civita uniqueness, metric completions, holomorphic relative connections and simply connected rational curves.

Classical Riemannian product geometry and flat holomorphic connection transport.

## Review and formalization scope

Read both full selected proofs and the tangent-box definition. Both manuscripts receive extractions. Canonical metric existence, global box construction and global splitting/integrability are not audited.

The scope and both Comparators were read in full. KahlerSplitting assumes both positive-rank summands are integrable and targets a compatible biholomorphic universal-cover product. SplitTangentIntegrability separately targets integrability of both summands on a projectively embedded rationally connected compact complex manifold; it does not include the compatible product conclusion. Both targets have sorry bodies. No separate solution or Lean build was checked.

Parallelism and the metric completion identification are inputs to the first card. Existence of a global tangent box is an input to the second, not a conclusion of its transport argument.

[Batch record](../../batches/B069/README.md)
