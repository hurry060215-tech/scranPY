# py-scranpool-omicverse

An independently maintained packaging of patched [scranPY](https://github.com/sfortma2/scranPY) for OmicVerse integration. Distribution: `py-scranpool-omicverse`; import: `ov_scranpool`. It does not install or overwrite the upstream `scranPY` namespace. Original attribution and license are retained.

## Status and installation

Version 0.1.0 is a candidate, not yet published to PyPI. Build and install this checkout for validation:

```sh
python -m pip install ".[test]"
python -m pytest -q
```

The R-reference certificate covers dense QR pooling on the frozen 240-cell/two-cluster fixture and even/odd pool medians. CVXPY constraints, small-cluster fallback and other upstream paths are not certified as R-equivalent. Upstream defaults are preserved; the OmicVerse adapter explicitly selects the validated QR subset.

## Provenance

Validated base: `17b6aeabd02fa6ceae8e4f5e3838a10276337b29`. See [attribution](ATTRIBUTION.md), the unchanged [license](LICENSE), and [upstream documentation](UPSTREAM_README.md) for history. The historical upstream README/Conda recipe refers to the original distribution, not this candidate. This variant is not affiliated with or endorsed by the upstream authors.

## Release validation

CI builds a wheel from the source archive, installs it, and runs the retained reference tests outside the checkout. See [release instructions](RELEASE.md). Coexistence with the upstream distribution must pass before release. No numerical gate is widened.
