---
id: openai-math-268
record_type: family
title: The spin-one Haldane gap
source_family: '268'
source_collection: openai/math
batch_id: B001
original_group: 2
subject: Analysis, dynamics and mathematical physics
source_paper_ids:
- P-000011
- P-000069
instrument_ids:
- MI-000077
- MI-000078
- MI-000079
headline: Haldane gap for the spin-1 Heisenberg ring
central_instrument: '“Coupled purity bootstrap”: one partition function written as Gibbs weights and as powers of spatial transfer eigenvalues; squaring one doubles inverse temperature, squaring the other doubles length, and exact identities couple them. The criterion does not require frustration-freeness.'
novelty_assessment: new criterion
formalization_summary: no (computer-assisted, Python verifier)
statement_faithfulness: —
dependencies: companion depends on main’s intermediate data
antecedents: —
review_status: imported-from-direction-paper
updated: '2026-10-12'
source_status_line: not formalized; computer-assisted new criterion
map_formalization_summary: 'no'
---

# The spin-one Haldane gap

[Family index](../../tables/families.md) · [Batch B001](../../batches/B001/README.md)

The statements and assessments below report the direction paper’s extraction. They do not certify the source proofs.

## Source manuscripts

- [P-000011](../papers/P-000011.md)
- [P-000069](../papers/P-000069.md)

## Family description

Source status as recorded in the direction paper: not formalized; computer-assisted new criterion

For the pure spin-1 Heisenberg antiferromagnet on even periodic rings, the source claims a unique ground state for all even $`L \ge 60`$ and a uniform gap: $`\gamma_L>\frac4{105}\log\frac{80}{79}>4.79\times10^{-4}`$ for $`L \ge 60`$ and $`>3.8\times10^{-3}`$ for $`L \ge 2304`$, versus the numerical 0.4105. Odd rings are not covered. A companion discharges Tasaki’s Assumption 2 for boundary-field chains. Haldane’s 1983 conjecture for the actual Heisenberg chain had no rigorous proof; the chain is not frustration-free, so the usual AKLT and frustration-free finite-size criteria do not directly establish this claim.

## Extracted instruments.

- [MI-000077: Coupled purity bootstrap](../instruments/MI-000077.md)

- [MI-000078: Self-adjoint spatial transfer operator on bond histories](../instruments/MI-000078.md)

- [MI-000079: Moment-to-spectrum extraction with exact-integer certificates](../instruments/MI-000079.md)

## Reused.

Aizenman–Nachtergaele 1994; Suzuki’s quantum transfer matrix; Fannes–Nachtergaele–Werner MPS; Fox–Glynn truncation; Tasaki’s 2025 index theorem (companion).

## Caveats.

The argument uses 27 thermal cases and 2 MPS contractions. The verifier was not run for this survey. Self-adjointness requires the real Cartesian decomposition, which restricts the scope of the criterion.

## Recorded assessment

- Novelty: new criterion
- Formalization: no (computer-assisted, Python verifier)
- Statement coverage: —
- Dependencies: companion depends on main’s intermediate data
- Antecedents: —
