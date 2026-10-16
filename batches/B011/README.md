# B011: Matrix splitting, sensitivity and low-degree observations

Extraction date: 2026-10-16. This batch adds 4 previously uncatalogued families, 4 source manuscripts and 8 instruments. The original groups of 17 and 21 families remain together in B001.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000188: Recursive spectral cuts separate PSD matrices with a dimension-free overlap charge](../../catalog/instruments/MI-000188.md) | 126 |
| [MI-000189: A two-sample density and spectral multiplicity control a matching-cell averaging channel](../../catalog/instruments/MI-000189.md) | 126 |
| [MI-000190: An equal-marginal one-sided displacement bound controls mean squared motion](../../catalog/instruments/MI-000190.md) | 127 |
| [MI-000191: Weighted polynomial grades recover cube edges through an anticommutator](../../catalog/instruments/MI-000191.md) | 127 |
| [MI-000192: A forbidden label pattern bounds the clauses one bit away from acceptance](../../catalog/instruments/MI-000192.md) | 132 |
| [MI-000193: Joint sensitivity profiles control recursive gates while block witnesses multiply](../../catalog/instruments/MI-000193.md) | 132 |
| [MI-000194: A cancellation report saves degree while retaining more than the revealed-coordinate variance](../../catalog/instruments/MI-000194.md) | 192 |
| [MI-000195: Finite observation scores amplify a variance-to-degree advantage into Boolean correlation](../../catalog/instruments/MI-000195.md) | 192 |

## Source and method

The source revision is [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). Its preprint tree is identical to the B001 snapshot; intervening upstream commits changed repository administration. Records give exact manuscript bindings, labelled source passages and SHA-256 hashes in the [source manifest](../../sources/batches/B011.json).

Selection covers eight mechanisms in four manuscripts: orthogonal PSD splitting and symmetric matching-cell averaging; a one-sided equal-marginal estimate and weighted cube grading; tournament candidate lists and joint sensitivity recurrences; reporting cancellation and observation-score amplification. The selected source arguments were read, and five Comparator files were compared with their scope documents. Family 126's selected declarations state superpolynomial unshifted bounds rather than the paper's shifted exponential theorem. Family 132's scope mentions a fixed superquadratic exponent, but its Comparator file contains the quantitative unbounded-ratio statement. Primary antecedents were retrieved for spectral multiplicity, weighted orthogonal polynomials, equal-law primitive cancellation, gated tournament constructions, decision-tree score estimates and probability limits. The Helstrom attribution follows the source; its publisher page was not retrievable in this batch.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) contain eight groups of finite checks. They include recursive noncommuting PSD splittings, full small matching-cell channels, exact stationary cycles, weighted polynomial grades, candidate-clause lists, exhaustive small nested-predicate compositions, exact finite reporting partitions and score/Fourier identities. Matrix spectra and Gaussian integrals are numerical; finite rank counts, probability identities and convolution moments use exact arithmetic where stated.

Install [verification-requirements.txt](../verification-requirements.txt), then run `python batches/B011/verification/check_instruments.py` from the repository root. The run used Python 3.13, NumPy 2.5.4 and SciPy 1.18.1. Gaussian calculations check the normalized subtraction identity at small parameter values; they do not claim a certified positive-gain example at the much larger scale used by the asymptotic argument. The small tournaments use their own checked label threshold rather than the final separation parameters.

The records separate local mechanisms from the complete matching PSD lower bound, final sensitivity-separation optimization and unbounded Boolean counterexample sequence. Later mean-cost and weighted-mixture variants in family 192 were not audited. No Lean solution was built, and no exhaustive priority conclusion is asserted.

Potential applications are labelled as proposals. This extraction adds no claim of independent human review or exhaustive novelty certification.
