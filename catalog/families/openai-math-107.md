---
id: openai-math-107
record_type: family
title: Matrix multiplication exponent ω ≤ 9/4
source_family: '107'
source_collection: openai/math
batch_id: B001
original_group: 1
subject: Combinatorics and theoretical computer science
source_paper_ids:
- P-000028
- P-000045
- P-000052
instrument_ids:
- MI-000028
- MI-000029
- MI-000030
headline: Matrix multiplication exponent $`\omega \le 9/4`$
central_instrument: 'The proof bounds every point of Strassen’s asymptotic spectrum using polynomial multiplication, without giving a matrix-multiplication algorithm: a DFT-over-copies degeneration keeps all blocks sharing a leg and yields a “shared-leg entropy inequality”; concavity plus tripling force growth $`a^{4/3}`$.'
novelty_assessment: new as a proof of an ω bound
formalization_summary: supplied; unbuilt here
statement_faithfulness: yes, straight-line programs over ℂ
dependencies: 'no'
antecedents: Alman–Li 2026
review_status: imported-from-direction-paper
updated: '2026-10-12'
source_status_line: Lean, straight-line definition of $`\omega`$ over $`\mathbb{C}`$ new as a proof of an $`\omega`$ bound
map_formalization_summary: 'yes'
---

# Matrix multiplication exponent ω ≤ 9/4

[Family index](../../tables/families.md) · [Batch B001](../../batches/B001/README.md)

The statements and assessments below report the direction paper’s extraction. They do not certify the source proofs.

## Source manuscripts

- [P-000028](../papers/P-000028.md)
- [P-000045](../papers/P-000045.md)
- [P-000052](../papers/P-000052.md)

## Family description

Source status as recorded in the direction paper: Lean, straight-line definition of $`\omega`$ over $`\mathbb{C}`$ new as a proof of an $`\omega`$ bound

$`\omega(\mathbb C)\le9/4`$, compared with the previous bound 2.371177 cited by the initial extraction. The 13-page argument is non-constructive: it bounds every point of Strassen’s asymptotic spectrum and gives “no competitive finite matrix size”.

## Extracted instruments.

- [MI-000028: Finite separation of a shared leg and the shared-leg entropy inequality](../instruments/MI-000028.md)

- [MI-000029: Spectral growth on polynomial multiplication](../instruments/MI-000029.md)

- [MI-000030: Detecting characters](../instruments/MI-000030.md)

## Reused.

Bini interpolation; Strassen’s asymptotic spectrum; combinatorial degeneration; method of types; Clebsch–Gordan exact sequence.

## Caveats.

The stated theorem concerns $`\mathbb C`$. The argument bounds spectral profiles through a specified collection of inequalities; a better exponent would require a further argument. No Lean build was performed for this survey.

## Recorded assessment

- Novelty: new as a proof of an ω bound
- Formalization: supplied; unbuilt here
- Statement coverage: yes, straight-line programs over ℂ
- Dependencies: no
- Antecedents: Alman–Li 2026
