# Attribution and maintenance boundary

Derived from https://github.com/sfortma2/scranPY. The original LICENSE and author declarations are retained.

This independent maintenance variant is based on validated commit `17b6aeabd02fa6ceae8e4f5e3838a10276337b29` in the hurry060215-tech fork. It is not an upstream-author release. Haoliang Zhu maintains this distribution.

The R-reference certificate covers dense QR pooling on the frozen 240-cell/two-cluster fixture and even/odd pool medians. CVXPY constraints, small-cluster fallback and other upstream paths are not certified as R-equivalent. Upstream defaults are preserved; the OmicVerse adapter explicitly selects the validated QR subset.

Only distribution/import identity and packaging are changed relative to the patched source for this first independent release. The original upstream fix branches remain separate.
