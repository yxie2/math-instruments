# B064: Traces, equality barriers and stable analytic estimates

Extraction date: 2026-10-16. This batch adds 4 families, 8 source manuscripts and 8 instruments.

## Instruments

| Instrument | Family |
| --- | --- |
| [MI-000614: Extend a continuous zero trace by signed truncation](../../catalog/instruments/MI-000614.md) | 071 |
| [MI-000615: Convert arcwise measure control into a null trace image](../../catalog/instruments/MI-000615.md) | 071 |
| [MI-000616: Translate conformal derivative integrability into a Sobolev pullback bound](../../catalog/instruments/MI-000616.md) | 072 |
| [MI-000617: Exclude a critical Jacobian equality by a growing harmonic barrier](../../catalog/instruments/MI-000617.md) | 072 |
| [MI-000618: Convexify a capacity functional into a norm compatible with coordinate masks](../../catalog/instruments/MI-000618.md) | 077 |
| [MI-000619: Insert an elliptic graph germ into a continued spherical phase](../../catalog/instruments/MI-000619.md) | 077 |
| [MI-000620: Approximate uniformly locally integrable envelopes by Gaussians](../../catalog/instruments/MI-000620.md) | 080 |
| [MI-000621: Preserve a polynomial envelope exponent through anisotropic sampling](../../catalog/instruments/MI-000621.md) | 080 |

## Source and method

Pinned source revision: [`1581d4cbdd69a0faf34b2089614fe2a814316a6a`](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a). The [source manifest](../../sources/batches/B064.json) records hashes, exact labels and manuscript coverage.

Eight instruments from four families and all eight associated manuscripts. Complete selected source proofs were read, together with the Goldshtein-Ukhlov primary composition theorem and equivalence argument. Both available scope documents and all four distinct linked Comparators were read in full.

## Mathematical checks and scope

The [verification program](verification/check_instruments.py) and [results](verification/results.json) cover signed truncation, arcwise image covers, conformal pullback, harmonic barriers, finite atomic dictionaries, local phase insertion, Gaussian approximation and anisotropic envelope sums.

The finite dictionary only approximates the full atomic norm. Finite lattice sums do not certify an infinite-lattice bound. Derivative integrability and endpoint error envelopes remain conditional inputs. No circle-domain, Brennan, strict-spectrum, Fourier restriction or Schrodinger endpoint headline is certified. No Lean solution was built. The fixed edition is unchanged.

Proposed applications are not subsequent results. No independent human review or exhaustive novelty certification is claimed.
