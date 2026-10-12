---
id: openai-math-309
record_type: family
title: Kervaire invariant at the prime three
source_family: '309'
source_collection: openai/math
batch_id: B001
original_group: 2
subject: Operator algebras, topology and symplectic geometry
source_paper_ids:
- P-000059
instrument_ids:
- MI-000104
- MI-000105
- MI-000106
headline: 'Kervaire invariant at $`p=3`$: survivors exactly $`j\in\{0,2,3\}`$'
central_instrument: '“Finite Euler bound”: a coordinate-change coefficient as a nilpotence witness imposes a deadline on the Tate spectral sequence, replacing the Gap and Periodicity theorems of Hill–Hopkins–Ravenel; the Belmont–Ray coefficient model is proved along the way.'
novelty_assessment: combination
formalization_summary: 'no'
statement_faithfulness: —
dependencies: 'no'
antecedents: —
review_status: imported-from-direction-paper
updated: '2026-10-12'
source_status_line: not formalized combination claims a new element exists
map_formalization_summary: 'no'
---

# Kervaire invariant at the prime three

[Family index](../../tables/families.md) · [Batch B001](../../batches/B001/README.md)

The statements and assessments below report the direction paper’s extraction. They do not certify the source proofs.

## Source manuscripts

- [P-000059](../papers/P-000059.md)

## Family description

Source status as recorded in the direction paper: not formalized combination claims a new element exists

With $`b_j\in\mathrm{Ext}^{2,4\cdot3^{j+1}}`$, the survivors are exactly $`j\in\{0,2,3\}`$: $`b_1`$ dies (Toda), $`b_j`$ dies for all $`j \ge 4`$, and $`b_3`$ survives, giving an order-three element in $`\pi_{322}S_{(3)}`$. This is a finite survivor list with a missing index $`j=1`$; the odd-primary Adams-family indexing differs from the classical prime-two Kervaire invariant convention. The result would also refute Belmont–Ray’s Conjecture 0.1(3). HHR’s 2011 odd-primary note explicitly left $`\theta_{4}`$ at $`p=3`$ open.

## Extracted instruments.

- [MI-000104: Finite Euler bound](../instruments/MI-000104.md)

- [MI-000105: Exact cyclic coefficient model and fixed geometry](../instruments/MI-000105.md)

- [MI-000106: Lattice forcing from the known survivor](../instruments/MI-000106.md)

## Reused.

Adams–Novikov spectral sequence; Miller–Ravenel–Wilson 2-line; Toda differentials; Belmont–Ray CM detection via Lubin–Tate; Selick’s criterion; Amelotte’s $`\theta_{3}`$; the positive branch uses a truncated extended-cube construction from the stem-106 element, followed by Moore-spectrum and Adams–Novikov corrections (23,384 unknowns in the finite calculation). This produces stem $`3\cdot108-2=322`$; the ordinary ring cube would lie in stem $`3\cdot106=318`$ and is not the claimed new element.

## Caveats.

The claimed conclusion includes a new stable homotopy class. Its verification requires about 1,700 lines of differential calculations, with several statements specified only “up to nonzero scalar” entering a sign-sensitive character test. Although the paper has a reproducibility section, no code is supplied.

## Recorded assessment

- Novelty: combination
- Formalization: no
- Statement coverage: —
- Dependencies: no
- Antecedents: —
