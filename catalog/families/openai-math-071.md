---
id: openai-math-071
record_type: family
title: Zero-trace Sobolev extension and null trace images
source_family: '071'
source_collection: openai/math
batch_id: B064
subject: Real and complex analysis
source_paper_ids:
- P-000383
- P-000384
instrument_ids:
- MI-000614
- MI-000615
headline: The sources claim removable-boundary rigidity and general circle-domain uniformization.
central_instrument: Signed truncations extend continuous zero-trace functions across arbitrary closed
  sets. Arcwise oscillation bounded by a measure turns measure-null traces into null real images.
novelty_assessment: Both are elementary extension and covering arguments. The source use in infinitely
  connected uniformization is not certified by these local tools.
formalization_summary: KoebeCircleDomains states circle-domain uniformization on the Riemann sphere and
  the removability-to-rigidity implication without a component-count bound. Its removable-set definition
  uses orientation-preserving sphere homeomorphisms conformal off the set; rigidity concludes agreement
  with a Mobius transformation on the source domain. Both available scope documents and all four distinct
  linked Comparators in this batch were read in full. Target theorems have sorry proof bodies. No separate
  solution or Lean build was checked.
statement_faithfulness: The extension assumes continuity and zero values on the entire closed set. The
  trace criterion uses outer measure, local connectedness and a bound on every joining simple arc.
dependencies: Sobolev truncation, weak compactness, regular Borel measures and local arc connectedness
  of metric continua.
antecedents: Classical Sobolev zero extension and absolute-continuity covering principles.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Zero-trace Sobolev extension and null trace images

## Source manuscripts and claim

- [Removable Boundaries and Rigidity of Circle Domains](../papers/P-000383.md): selected passages extracted.
- [Koebe's Circle-Domain Conjecture](../papers/P-000384.md): selected passages extracted.

The sources claim removable-boundary rigidity and general circle-domain uniformization.

## Extracted instruments

- [MI-000614: Extend a continuous zero trace by signed truncation](../instruments/MI-000614.md)
- [MI-000615: Convert arcwise measure control into a null trace image](../instruments/MI-000615.md)

## Dependencies and antecedents

Sobolev truncation, weak compactness, regular Borel measures and local arc connectedness of metric continua.

Classical Sobolev zero extension and absolute-continuity covering principles.

## Review and formalization scope

Read the complete zero-trace extension proof and its smoothing application, and the complete null-image criterion. The model transfer, compatible barriers, path laws and uniformization proofs remain unaudited.

KoebeCircleDomains states circle-domain uniformization on the Riemann sphere and the removability-to-rigidity implication without a component-count bound. Its removable-set definition uses orientation-preserving sphere homeomorphisms conformal off the set; rigidity concludes agreement with a Mobius transformation on the source domain. Both available scope documents and all four distinct linked Comparators in this batch were read in full. Target theorems have sorry proof bodies. No separate solution or Lean build was checked.

The extension assumes continuity and zero values on the entire closed set. The trace criterion uses outer measure, local connectedness and a bound on every joining simple arc.

[Batch record](../../batches/B064/README.md)
