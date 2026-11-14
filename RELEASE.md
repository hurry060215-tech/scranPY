# Release candidate

Distribution `py-scranpool-omicverse`, module `ov_scranpool`, candidate 0.1.0. Not published.

The release branch must be reviewed and merged into the **fork** default branch `main` before publishing. Do not merge namespace/packaging changes into the upstream bug-fix PR.

PyPI pending publisher values:

- Project: `py-scranpool-omicverse`
- GitHub owner: `hurry060215-tech`
- Repository: `scranPY`
- Workflow: `publish.yml`
- Environment: `pypi`

The PyPI account is `hurry`; it is not the GitHub owner field. Publication is manual-only, version-checked, and follows installed-wheel tests. Pushes and tags do not publish. No publisher or release has been created by these source changes.

Before release, run strict metadata checks, installed-wheel tests, side-by-side imports and uninstall/reinstall checks with the original distribution. Then validate the actual PyPI artifact.
