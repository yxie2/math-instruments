# B015: Sampling interfaces, skeleton weights and partial graph exposures

Extraction date: 2026-10-16. This batch adds 4 previously uncatalogued families, 4 source manuscripts and 9 instruments. The original groups of 17 and 21 families remain together in B001.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000221: Robust witness menus admit balanced mixtures and simultaneous feasible profiles](../../catalog/instruments/MI-000221.md) | 171 |
| [MI-000222: Separated product comparisons yield aggregate moments despite nearby dependencies](../../catalog/instruments/MI-000222.md) | 171 |
| [MI-000223: Posterior domination retains the mass of a required event](../../catalog/instruments/MI-000223.md) | 171 |
| [MI-000224: Planted posterior resampling gives recoverable fragments and outside-coordinate control](../../catalog/instruments/MI-000224.md) | 176 |
| [MI-000225: Normalized containment maximizers give small cores with conditionally spread extensions](../../catalog/instruments/MI-000225.md) | 176 |
| [MI-000226: A partially acyclic complex with odd-order stabilizers computes low-degree group homology](../../catalog/instruments/MI-000226.md) | 177 |
| [MI-000227: Chamber multiplicities control skeleton weights and the loss in expansion](../../catalog/instruments/MI-000227.md) | 177 |
| [MI-000228: Account-specific expectation discounts let one deterministic choice control many statistics](../../catalog/instruments/MI-000228.md) | 178 |
| [MI-000229: Partial stub pairings have exact low-rank resolvent updates and centered pair cancellation](../../catalog/instruments/MI-000229.md) | 178 |

## Source and method

The source revision is [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). Its preprint tree is identical to the B001 snapshot; intervening upstream commits changed repository administration. Records give exact manuscript bindings, labelled source passages and SHA-256 hashes in the [source manifest](../../sources/batches/B015.json).

Nine instruments were selected from four graph and expansion manuscripts: balanced mixtures and simultaneous profiles; scattered moments; retained-event posteriors; planted resampling with outside-coordinate control; ratio-maximizing graph cores; partial homology resolutions; skeleton weights; discounted conditional expectations; and partial-pairing matrix identities. The selected source proofs were read. The two listed Comparator statements, for families 176 and 177, were compared with the scope documents; families 171 and 178 had no listed scope documents. Primary antecedents were retrieved for planted inference, graph cores, group homology, pessimistic estimators and the Ihara-Bass matrix polynomial. Kakutani's publisher text was not retrievable; the attribution follows the source and the finite response proof was checked directly.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) contain nine groups: 72 menu linear programs, 90 block-dependent moments, 100 exact posterior models, 13,096 planted transitions in 12 models, 728 graph copy ratios, 660 conditional-maximizer tests, four cyclic orbit-chain models and four averaging models, 1,760 exhaustive cochain-distance checks, 600 discounted transitions, 432 scalar-excess models, 288 inverse updates, 432 path coefficients and 963 exact restricted-pair averages. Six resampling models satisfy the source's very small spread-ratio condition. Controls demonstrate best-response cycling, conditional target distortion, failure with even stabilizers, nonzero cohomology and the need for separated product estimates.

Run `python batches/B015/verification/check_instruments.py` from the repository root with NumPy and SciPy from the shared requirements. Rational arithmetic and F2 elimination handle probabilities, orbit chains, weights and pair averages; linear programs and resolvent matrices use floating point. The core-size numerical cases use the elementary inequality; the small graph enumerations do not reproduce a large multi-level hierarchy.

The hypercube embedding, global dependent-tree covering, congruence-complex homology and expansion construction, and complete Ramanujan graph algorithm and exact repair were not certified. No Lean solution was built. Established mechanisms are credited explicitly, and targeted comparisons do not establish historical priority.

Potential applications are labelled as proposals. This extraction adds no claim of independent human review or exhaustive novelty certification.
