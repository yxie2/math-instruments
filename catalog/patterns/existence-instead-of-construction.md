---
id: PAT-001
record_type: pattern
title: Existence instead of construction
batch_id: B001
source_section: '7.1'
updated: '2026-10-12'
---

# Existence instead of construction

[Pattern index](README.md)

Several arguments establish existence through compactness, spectral duality, random sampling, or a terminating search whose output has not been computed. The resulting existence statement need not supply an object of practical size.

The proof of $`\omega \le 9/4`$ bounds the asymptotic spectrum without providing a competitive finite matrix size. The Hadwiger argument selects m through an ultrafilter, and the Hilbert 10 reduction uses a nonstandard root. The zero-divisor and direct-finiteness constructions use random choices or searches with parameters such as $`q=2^{217}`$ and $`n\gtrsim e^{300000}`$. In the second group, the Hilbert 16 argument gives an ineffective B(d), the nearby-Lagrangian example has no explicit dimension, and the Borsuk construction supplies a continuous set without extracting a finite subset. These examples differ in effectivity, but each leaves some construction data unspecified or unevaluated.
