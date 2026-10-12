# Signed restriction and fixed-depth circuit lower bounds

Status: application described in the direction paper; the separate application manuscript is not included in this repository release.

After extraction, we investigate whether particular instruments can be reused. A separate application manuscript studies the signed restriction lemma identified in family [112](../../catalog/families/openai-math-112.md). The lemma controls correlations through signed combinations of narrow CNFs with bounded expected coefficient mass. Combining it with adaptive averaging, classical depth reduction and quantitative sparsification yields, for the same polynomial-time language as in the source, the gate-count lower bound
``` math
S_D(f_n)\ge 2^{\Omega_D\left((n\log n/\log\log n)^{1/(D-1)}\right)}
 \qquad\text{for every fixed }D\ge3
```
at all sufficiently large input lengths $`n`$. Here $`S_D`$ counts AND/OR gates in exact circuits of depth at most $`D`$, with arbitrary finite fan-in and fan-out and input negations. The source supplies the lemma and the language; the application extends the source’s stated depth-three result. The proof will be presented in the separate application paper. This case illustrates the progression from extracting an instrument to investigating its use and obtaining a further theorem.

## Extracted input

- [MI-000083: Restriction bound independent of clause count](../../catalog/instruments/MI-000083.md)

## Publication and further evidence

This page reserves the place for the application paper, its public citation and supporting material when released. The direction paper supplies the public description of the application.
