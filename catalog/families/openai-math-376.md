---
id: openai-math-376
record_type: family
title: Universal computation in forced Navier–Stokes flows
source_family: '376'
source_collection: openai/math
batch_id: B001
original_group: 2
subject: Operator algebras, topology and symplectic geometry
source_paper_ids:
- P-000006
- P-000029
- P-000036
- P-000040
- P-000043
- P-000049
- P-000051
- P-000076
- P-000078
instrument_ids:
- MI-000113
- MI-000114
- MI-000115
headline: Universal computation in forced Navier–Stokes flows
central_instrument: Defining the force as the residual enforces Navier–Stokes for a chosen smooth divergence-free flow; the required mean, regularity and time-dependence of that force still need proof; the construction is Moore’s generalized shifts plus Bennett reversibility plus Hamiltonian box-moving. The extracted construction uses scale-nested memories under rapidly vanishing forcing.
novelty_assessment: incremental
formalization_summary: of 9 manuscripts, engineering lemmas
statement_faithfulness: —
dependencies: dependencies among nine public manuscripts; main self-contained
antecedents: Agrachev–Sarychev (not engaged)
review_status: imported-from-direction-paper
updated: '2026-10-12'
source_status_line: lemmas formalized; main paper not incremental
map_formalization_summary: lemmas only
---

# Universal computation in forced Navier–Stokes flows

[Family index](../../tables/families.md) · [Batch B001](../../batches/B001/README.md)

The statements and assessments below report the direction paper’s extraction. They do not certify the source proofs.

## Source manuscripts

- [P-000006](../papers/P-000006.md)
- [P-000029](../papers/P-000029.md)
- [P-000036](../papers/P-000036.md)
- [P-000040](../papers/P-000040.md)
- [P-000043](../papers/P-000043.md)
- [P-000049](../papers/P-000049.md)
- [P-000051](../papers/P-000051.md)
- [P-000076](../papers/P-000076.md)
- [P-000078](../papers/P-000078.md)

## Family description

Source status as recorded in the direction paper: lemmas formalized; main paper not incremental

For each fixed positive computable viscosity $`\nu`$, an effective procedure maps a Turing machine and input to a smooth mean-zero force on $`\mathbb{T}^{3}`$, time-independent for $`t \ge 1`$, such that Navier–Stokes from rest has a global smooth solution and a marked material particle enters a fixed region in finite time iff the machine halts. Variants: $`\mathbb{R}^{3}`$ with compact support, force decaying faster than any power, an Eulerian velocity observer. The family contains nine closely related manuscripts.

## Extracted instruments.

- [MI-000113: Injective local compiler](../instruments/MI-000113.md)

- [MI-000114: Effective parking and routing isotopy](../instruments/MI-000114.md)

- [MI-000115: Scale-nested memories under rapidly vanishing forcing](../instruments/MI-000115.md)

## Reused.

Moore’s generalized shifts and gapped radix coding; Turing’s printing problem; Leray’s energy uniqueness; Helmholtz–Leray projection; heat-kernel bounds.

## Caveats.

For a chosen smooth divergence-free $`U`$ with $`U(0)=0`$, setting $`f=U_t+(U\cdot\nabla)U-\nu\Delta U`$ makes the Navier–Stokes identity hold with zero pressure. This residual construction does not automatically establish the required mean-zero condition, effective description, bounded derivatives, spatial support, eventual stationarity or time decay of the force; the properties prescribed in each version still require proof. Stationary Euler solutions are not generally Beltrami. The cited Cardona–Miranda–Peralta-Salas–Presas construction uses Beltrami fields, a special class of stationary Euler flows, to realize computation. The forced constructions therefore have a different scope from that construction and from unforced or low-mode-controlled flows. Computation is exact-real reachability with no finite-precision tolerance, as the papers concede. No fresh literature search was completed for this entry.

## Recorded assessment

- Novelty: incremental
- Formalization: of 9 manuscripts, engineering lemmas
- Statement coverage: —
- Dependencies: dependencies among nine public manuscripts; main self-contained
- Antecedents: Agrachev–Sarychev (not engaged)
