---
id: openai-math-265
record_type: family
title: Two-dimensional area law from a global gap
source_family: '265'
source_collection: openai/math
batch_id: B001
original_group: 2
subject: Analysis, dynamics and mathematical physics
source_paper_ids:
- P-000020
- P-000047
instrument_ids:
- MI-000074
- MI-000075
- MI-000076
headline: 2D area law from a global gap, frustration allowed
central_instrument: “Optimized nested positive filters” whose only cost is excitation energy, and “replica metric transport” encoding conditional mutual information as the derivative of a log-norm comparable to energy, with a displayed information term linear in the transport parameter and additional energy cost quadratic in that parameter and linear in the split probability.
novelty_assessment: new
formalization_summary: 'no'
statement_faithfulness: —
dependencies: PEPS companion depends on main
antecedents: —
review_status: imported-from-direction-paper
updated: '2026-10-12'
source_status_line: not formalized new
map_formalization_summary: 'no'
---

# Two-dimensional area law from a global gap

[Family index](../../tables/families.md) · [Batch B001](../../batches/B001/README.md)

The statements and assessments below report the direction paper’s extraction. They do not certify the source proofs.

## Source manuscripts

- [P-000020](../papers/P-000020.md)
- [P-000047](../papers/P-000047.md)

## Family description

Source status as recorded in the direction paper: not formalized new

Let $`\Lambda`$ be a finite induced square-lattice graph, with local dimension $`q\ge1`$, and let $`H=\sum_Xh_X`$ have one Hermitian term per nonempty support $`X`$, with $`\|h_X\|\le J`$ and support diameter at most $`R`$ in the graph distance of $`\Lambda`$. Assume a unique ground state and a full-system gap $`\Delta>0`$. The source claims $`S(A)\le C(q,R,J,\Delta)|\partial_\Lambda A|`$ for every $`A\subseteq\Lambda`$, where $`\partial_\Lambda A`$ is the set of lattice edges crossing from $`A`$ to its complement within $`\Lambda`$. No gap on restrictions, frustration-freeness or translation invariance is assumed. For the open $`L\times L`$ square grid with bounded on-site and nearest-neighbor interactions, a companion gives a normalized PEPS approximation with vector error at most $`L^{-1}`$ and bond dimension at most $`CL^c`$, with $`C,c`$ depending on $`q,J,\Delta`$. The constant is existential. Earlier proofs cited in the initial extraction (Anshu–Arad–Gosset 2022) need frustration-freeness.

## Extracted instruments.

- [MI-000074: Optimized nested positive filters with stationarity and Schmidt pinning](../instruments/MI-000074.md)

- [MI-000075: Replica metric transport](../instruments/MI-000075.md)

- [MI-000076: Positive replacement, randomized scanner, amplification](../instruments/MI-000076.md)

## Reused.

Lieb–Robinson bounds; Kitaev filter; Alicki–Fannes–Winter; strong subadditivity; Schur–Weyl; de Finetti; Kubo–Ando means; Schatten interpolation; random-order chain rule.

## Caveats.

The exponent estimates have a small margin ($`\varepsilon=10^{-5}`$, 0.999952 versus 0.99999), and the replica errors must be controlled uniformly over all histories. The argument gives no quantitative $`\Delta`$-dependence. Not every instrument received a fresh literature search.

## Recorded assessment

- Novelty: new
- Formalization: no
- Statement coverage: —
- Dependencies: PEPS companion depends on main
- Antecedents: —
