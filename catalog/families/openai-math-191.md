---
id: openai-math-191
record_type: family
title: Norm-coded determinant gaps and singular residue-orbit accounting
source_family: '191'
source_collection: openai/math
batch_id: B013
subject: Combinatorics
source_paper_ids:
- P-000126
instrument_ids:
- MI-000210
- MI-000211
- MI-000212
headline: The source claims point sets in the unit square with every triangle of area at least c n^(-2+eta),
  for fixed positive constants and every sufficiently large n.
central_instrument: An alternating field norm is placed in one determinant digit without cancellation
  by carries. Singular residue orbits and a label-conditional divisor estimate control sampling costs
  even when labels collide.
novelty_assessment: Finite-field norms, alternating tensors, Smith reduction and orbit-stabilizer counting
  are classical. The selected candidate packages are the digit placement and the quantitative singular-orbit
  and conditional-digit accounting. The final geometric improvement is not certified.
formalization_summary: HeilbronnTriangle.lean states a fixed explicit positive exponent on an unbounded
  sequence of point-set sizes, and a consequence refuting the almost-n-minus-two upper bound. The paper
  claims a bound for every sufficiently large size, which is broader. Scope text and Comparator statements
  were compared. No Lean solution was built or kernel-checked; the auxiliary instruments are not separate
  certified targets.
statement_faithfulness: The source fixes odd extension degree 41 and extremely large but fixed digit length.
  Labels may repeat in the conditional moment estimate. The orbit bound includes zero determinants and
  uses positive integer B^k to count a zero diagonal residue.
dependencies: Finite-field coefficient conjugation; alternating monomial expansion without division by
  six; isolated digit sums and carry bounds; prime-power Smith form; stabilizer determinant image; independent
  digit conditioning.
antecedents: The source credits Lidl and Niederreiter for finite-field background and Smith for diagonal
  reduction and determinantal divisors. These classical ingredients are distinct from the selected quantitative
  combination.
review_status: source-and-selected-argument-checks
updated: '2026-10-16'
---

# Norm-coded determinant gaps and singular residue-orbit accounting

## Source manuscript and claim

[A power improvement in the Heilbronn triangle lower bound](../papers/P-000126.md), by OpenAI, None.

The source claims point sets in the unit square with every triangle of area at least c n^(-2+eta), for fixed positive constants and every sufficiently large n.

## Extracted instruments

- [MI-000210: A field-norm coefficient isolated in base digits excludes small determinant residues](../instruments/MI-000210.md)
- [MI-000211: The determinant image of a stabilizer controls singular special-linear orbits](../instruments/MI-000211.md)
- [MI-000212: Four independent digit constraints bound a singular divisor after fixing labels](../instruments/MI-000212.md)

## Dependencies and antecedents

Finite-field coefficient conjugation; alternating monomial expansion without division by six; isolated digit sums and carry bounds; prime-power Smith form; stabilizer determinant image; independent digit conditioning.

The source credits Lidl and Niederreiter for finite-field background and Smith for diagonal reduction and determinantal divisors. These classical ingredients are distinct from the selected quantitative combination. The instrument cards identify the individual comparisons and their limits.

## Review and formalization scope

Read the full norm/digit and residue-orbit sections, including singular cases and fixed-label tails. The lattice enumeration, auxiliary cap, zero-determinant counts and geometric alteration were not audited.

HeilbronnTriangle.lean states a fixed explicit positive exponent on an unbounded sequence of point-set sizes, and a consequence refuting the almost-n-minus-two upper bound. The paper claims a bound for every sufficiently large size, which is broader. Scope text and Comparator statements were compared. No Lean solution was built or kernel-checked; the auxiliary instruments are not separate certified targets.

The source fixes odd extension degree 41 and extremely large but fixed digit length. Labels may repeat in the conditional moment estimate. The orbit bound includes zero determinants and uses positive integer B^k to count a zero diagonal residue.

[Source formalization scope](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/191.md) · [Batch record](../../batches/B013/README.md)
