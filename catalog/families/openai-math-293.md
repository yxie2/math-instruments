---
id: openai-math-293
record_type: family
title: Hyperinvariant subspaces and transitive algebras
source_family: '293'
source_collection: openai/math
batch_id: B001
original_group: 2
subject: Operator algebras, topology and symplectic geometry
source_paper_ids:
- P-000025
- P-000044
instrument_ids:
- MI-000098
- MI-000099
- MI-000100
headline: No hyperinvariant subspace; transitive algebra problem
central_instrument: '“Backward intertwiner over an ergodic base”: unicellular weighted shifts glued over the 2-adic odometer; multipliers force a tail index per fiber, a commuting operator lowers it along orbits, and a finite integer-valued measurable label cannot strictly decrease almost everywhere under a measure-preserving map.'
novelty_assessment: new
formalization_summary: ',108-module closure, two formal routes'
statement_faithfulness: 'yes'
dependencies: mutual elementary lemmas with companion
antecedents: —
review_status: imported-from-direction-paper
updated: '2026-10-12'
source_status_line: Lean, 1,108-module import closure new
map_formalization_summary: 'yes'
---

# Hyperinvariant subspaces and transitive algebras

[Family index](../../tables/families.md) · [Batch B001](../../batches/B001/README.md)

The statements and assessments below report the direction paper’s extraction. They do not certify the source proofs.

## Source manuscripts

- [P-000025](../papers/P-000025.md)
- [P-000044](../papers/P-000044.md)

## Family description

Source status as recorded in the direction paper: Lean, 1,108-module import closure new

On every infinite-dimensional separable complex Hilbert space there is a nonzero bounded quasinilpotent operator S ($`\|S^n\|\le\exp(-10\lfloor(n+1)^2/4\rfloor)`$) with no nontrivial closed hyperinvariant subspace; its commutant is a proper strongly closed transitive algebra, refuting Kadison’s transitive-algebra problem as well, which the catalogue summary omits. Companion: for every irrational rotation, an operator in the hyperfinite $`\mathrm{II}_{1}`$ factor with no nontrivial invariant projection in the factor, answering Zhu–Fang–Shi and the point-mass Brown-measure case left open by Haagerup–Schultz. Nothing is said about the ordinary invariant subspace problem.

## Extracted instruments.

- [MI-000098: Backward intertwiner over an ergodic base](../instruments/MI-000098.md)

- [MI-000099: Endpoint-conditioned convolution obstruction](../instruments/MI-000099.md)

- [MI-000100: Affiliated transport](../instruments/MI-000100.md)

## Reused.

Domar’s convex-envelope theorems (reproved); Douglas–Pearcy equivalence of the hyperinvariant and transitive-commutant problems; Dykema 2005 on projections of hyperinvariant subspaces; Anantharaman–Popa crossed products; Borel–Cantelli; Fejér kernels.

## Caveats.

The repository provides two formalization routes; neither was compiled or kernel-checked for this survey. The companion’s estimates ($`m^{(7/10)m}`$, $`m^{1000}`$) were not independently verified. Remark 1.5 asserts a published 2017 corollary is false. The companion estimates and comparisons with earlier equivalence claims require further checking.

## Recorded assessment

- Novelty: new
- Formalization: ,108-module closure, two formal routes
- Statement coverage: yes
- Dependencies: mutual elementary lemmas with companion
- Antecedents: —
