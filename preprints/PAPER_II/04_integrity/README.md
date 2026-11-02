# Integrity

`MANIFEST.json` binds the current document artifacts and navigation files in the coordinated series assembly. The selected source archive has its own SHA-256 sidecar and internal `SHA256SUMS.txt`.

The archive's `tools/verify_attribution.py` checks its complete manifest and historical source correspondence without executing Lean. The [validation summary](../02_validation/REVIEW_SUMMARY.md) states the audit scope. Earlier manifests apply only to the snapshots they identify.
