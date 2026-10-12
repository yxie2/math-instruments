---
id: openai-math-266
record_type: family
title: Three mutually unbiased bases in dimension six
source_family: '266'
source_collection: openai/math
batch_id: B001
original_group: 2
subject: Combinatorics, geometry and complexity
source_paper_ids:
- P-000035
- P-000068
instrument_ids:
- MI-000089
- MI-000090
- MI-000091
headline: Exactly three MUBs in dimension six
central_instrument: 'Represent every order-6 complex Hadamard matrix by nine seed phases plus a U(2) polar factor, giving a finite cover of the unclassified continuum; the headline claim uses a binary64 computation with hand-proved margins. Companion: “injective moments” calculus establishing Fourier vanishing outside Tao’s $`S_6`$ equivalence class.'
novelty_assessment: combination
formalization_summary: companion (N(6) ≤ 5, Fourier vanishing outside Tao’s S₆ class) only
statement_faithfulness: —
dependencies: 'no'
antecedents: —
review_status: imported-from-direction-paper
updated: '2026-10-12'
source_status_line: headline not formalized; $`N(6) \le 5`$ formalized combination arithmetic and compiler assumptions
map_formalization_summary: headline no; N(6) ≤ 5 yes
---

# Three mutually unbiased bases in dimension six

[Family index](../../tables/families.md) · [Batch B001](../../batches/B001/README.md)

The statements and assessments below report the direction paper’s extraction. They do not certify the source proofs.

## Source manuscripts

- [P-000035](../papers/P-000035.md)
- [P-000068](../papers/P-000068.md)

## Family description

Source status as recorded in the direction paper: headline not formalized; $`N(6) \le 5`$ formalized combination arithmetic and compiler assumptions

The source claims $`N(6)=3`$ (Zauner’s conjecture), as a theorem explicitly labelled “computer-assisted” and conditional on arithmetic and compiler conditions: a C++ pipeline in binary64 with hand-proved one-sided rounding margins, 4,470 seconds on 4 Oct 2026. The headline computation uses neither interval arithmetic nor exact algebra. The companion proves $`N(6) \le 5`$ exactly, the Matolcsi–Ruzsa–Weiner Fourier-vanishing conjecture for order-6 Hadamard matrices outside Tao’s $`S_6`$ equivalence class, and Phangara’s conjecture, with an exact rational verifier; the Lean covers the companion.

## Extracted instruments.

- [MI-000089: Seed ball plus fixed-frame completion via a U(2) polar-factor cover](../instruments/MI-000089.md)

- [MI-000090: Root certificates and tangent/normal refinement](../instruments/MI-000090.md)

- [MI-000091: Injective moments](../instruments/MI-000091.md)

## Reused.

JMMSW phase discretization and clique search; Rump’s verified norm bounds; Higham’s rounding analysis; Klappenecker–Rötteler lower bound; Newton’s identities; Zauner’s 2-design identity; Weiner’s completion theorem; Peyrl–Parrilo rational certificates.

## Caveats.

The headline rests on about 70 pages of hand-derived rounding margins across seven C++ files, not independently rerun or verified for this survey; one condition is checked by inspecting disassembly addresses. The 24 Sept manuscript’s proof rests on a 4 Oct run; an earlier run’s evidence packet “was not recovered”. The August 2026 classification preprint of Cárdenes Wuttig–Tindall is cited but is not used in the proof.

## Recorded assessment

- Novelty: combination
- Formalization: companion (N(6) ≤ 5, Fourier vanishing outside Tao’s S₆ class) only
- Statement coverage: —
- Dependencies: no
- Antecedents: —
