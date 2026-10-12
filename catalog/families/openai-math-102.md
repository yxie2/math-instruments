---
id: openai-math-102
record_type: family
title: Unique Games Conjecture
source_family: '102'
source_collection: openai/math
batch_id: B001
original_group: 1
subject: Combinatorics and theoretical computer science
source_paper_ids:
- P-000005
- P-000030
- P-000031
- P-000056
- P-000065
instrument_ids:
- MI-000025
- MI-000026
- MI-000027
headline: Unique Games Conjecture
central_instrument: '“Latent alphabet gadget”: a nonlinear shift-equivariant decoder on a big latent space with a noise law that rarely changes the honest decoder but is detected by every linear family with sufficiently large rank on the output subspace, so the degree-two KMS inverse theorem applies unchanged.'
novelty_assessment: new
formalization_summary: files; PCP and KMS reproved
statement_faithfulness: yes, full UGC
dependencies: 'no'
antecedents: —
review_status: imported-from-direction-paper
updated: '2026-10-12'
source_status_line: Lean, 475 files, full statement, PCP theorem reproved new gadget
map_formalization_summary: 'yes'
---

# Unique Games Conjecture

[Family index](../../tables/families.md) · [Batch B001](../../batches/B001/README.md)

The statements and assessments below report the direction paper’s extraction. They do not certify the source proofs.

## Source manuscripts

- [P-000005](../papers/P-000005.md)
- [P-000030](../papers/P-000030.md)
- [P-000031](../papers/P-000031.md)
- [P-000056](../papers/P-000056.md)
- [P-000065](../papers/P-000065.md)

## Family description

Source status as recorded in the direction paper: Lean, 475 files, full statement, PCP theorem reproved new gadget

For every fixed $`\varepsilon,\delta\in(0,1/2)`$ there is a fixed alphabet $`\mathbb{F}_2^s`$ and a deterministic polynomial-time reduction from 3SAT to bipartite Unique Games with translation constraints, value $`\ge 1-\varepsilon`$ on satisfiable and $`\le \delta`$ on unsatisfiable inputs. The formal object fixes alphabet, machine and predicates; $`\varepsilon`$ and $`\delta`$ are independent. The development also formalizes a Dinur-style PCP theorem, Håstad’s 3LIN and the Khot–Minzer–Safra Grassmann expansion theorem from scratch.

## Extracted instruments.

- [MI-000025: Latent alphabet gadget](../instruments/MI-000025.md)

- [MI-000026: Exact table keys with translation-orbit folding](../instruments/MI-000026.md)

- [MI-000027: Row-fiber abundance by erasure](../instruments/MI-000027.md)

## Reused.

Håstad’s 3LIN gap; KMS Grassmann expansion through BKS’s matrix chart; Khot–Saket folding and list decoding; KMS/DKKMS/Minzer–Zheng smooth advice game; Dinur–Steurer parallel repetition twice; Schwartz–Zippel. Not used: Majority is Stablest, high-dimensional expanders, sum-of-squares.

## Caveats.

The argument does not use other OpenAI manuscripts as inputs. Its reduction exponent and alphabet size are tower-like in $`1/p^*`$, which accounts for compatibility with the Arora–Barak–Steurer subexponential algorithm, although the paper does not discuss this point. The reasoning summary records that UGC arose as a subgoal of a different prompt about the basic SDP threshold.

## Recorded assessment

- Novelty: new
- Formalization: files; PCP and KMS reproved
- Statement coverage: yes, full UGC
- Dependencies: no
- Antecedents: —
