# B013: Greedy queries, path budgets, binary repairs and determinant digits

Extraction date: 2026-10-16. This batch adds 4 previously uncatalogued families, 4 source manuscripts and 9 instruments. The original groups of 17 and 21 families remain together in B001.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000204: A chronological paired query exactly represents survival in greedy triangle removal](../../catalog/instruments/MI-000204.md) | 188 |
| [MI-000205: Fresh occurrence randomness yields product equations with an explicit collision coupling](../../catalog/instruments/MI-000205.md) | 188 |
| [MI-000206: Clique-ended path systems turn a forbidden cycle length into an amount interval](../../catalog/instruments/MI-000206.md) | 189 |
| [MI-000207: Reversal-normalized compositions enumerate weighted linear forests without duplicates](../../catalog/instruments/MI-000207.md) | 189 |
| [MI-000208: A shattering corner and dense prefix force an ordered binary anchor into one mode](../../catalog/instruments/MI-000208.md) | 190 |
| [MI-000209: Protected-cell sampling and opposite bit propagation separate copy hitting from repair](../../catalog/instruments/MI-000209.md) | 190 |
| [MI-000210: A field-norm coefficient isolated in base digits excludes small determinant residues](../../catalog/instruments/MI-000210.md) | 191 |
| [MI-000211: The determinant image of a stabilizer controls singular special-linear orbits](../../catalog/instruments/MI-000211.md) | 191 |
| [MI-000212: Four independent digit constraints bound a singular divisor after fixing labels](../../catalog/instruments/MI-000212.md) | 191 |

## Source and method

The source revision is [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). Its preprint tree is identical to the B001 snapshot; intervening upstream commits changed repository administration. Records give exact manuscript bindings, labelled source passages and SHA-256 hashes in the [source manifest](../../sources/batches/B013.json).

Selection covers nine mechanisms from four manuscripts: exact paired survival queries; independent occurrence products and an exposure coupling; clique path budgets; weighted-forest enumeration; binary anchor pinning; protected-cell edit obstructions; norm-coded determinant gaps; singular special-linear orbits; and fixed-label digit tails. The selected source arguments were read and four Comparator statements were compared with their scope documents. The Heilbronn Comparator concerns an unbounded sequence of sizes, whereas the manuscript states an eventual all-size conclusion. Primary antecedents were retrieved for random-priority packing, graph adsorption, cycle-complete Ramsey numbers and ordered matrix removal. Finite-field and Smith-form attributions follow the source; their publisher pages were not retrievable in this batch.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) contain ten check groups. Exact checks include 12,484 chronological query answers; product polynomials on a two-triangle graph; independent recursive and generating-function counts for all 3,099 weighted-forest patterns; 249 explicit clique closure cycles; 13,632 ball-separation implications; 34,112 five-column trace selections; tree-mode and edit-propagation constraints; 276 reduced-degree determinant gaps; singular orbits over rings of sizes 2, 3 and 4; and 263,680 fixed-label digit matrices. Two thousand seeded coupled executions check agreement whenever there is no exposed-type collision; they do not establish an asymptotic collision bound.

Run `python batches/B013/verification/check_instruments.py` from the repository root. Only the Python standard library is required; this run used Python 3.13. The forest counts validate enumeration, not the source's deduction certificates. The matrix checks do not exhaust all 66-by-66 copies or all full-matrix edits. The norm tests use degree one to exercise the digit mechanism, not the enormous degree-41 construction.

The sharp triangle-removal asymptotics, full Ramsey exclusion, complete large ordered-matrix edit search and final geometric alteration were not independently certified. No Lean solution was built. Targeted antecedent searches do not establish historical priority.

Potential applications are labelled as proposals. This extraction adds no claim of independent human review or exhaustive novelty certification.
