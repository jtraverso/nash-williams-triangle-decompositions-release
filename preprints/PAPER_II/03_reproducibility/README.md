# Reproducibility

Extract `PAPER_II_LEAN_20261020_ALIGNED_v4.zip` from the series `archives/` directory. From its extracted root run:

```text
python tools/verify_attribution.py
```

This standalone static verifier checks corrected sources, reconstructs the original compiled bytes, checks the historical receipts and import hashes, and checks the internal manifest. It does not run Lean.

The [companion](../05_formalization/FORMALIZATION_COMPANION_preprint_v1.0_en.pdf) gives the exact toolchain and dependency revision for a new compilation. Obtain the pinned Mathlib cache using `lake exe cache get`; preserve the dependency lock and do not run `lake update`. The historical build/alignment scripts contain fixed Windows paths and require adaptation. Their comments may reference development notes or generators that are not supplied as reproduction resources; see the [inventory](../02_validation/SOURCE_NOTE_INVENTORY.json).

Markdown, TeX and PDF versions of both documents are supplied. Their generation is separate from Lean compilation. Relative repository links assume the complete series monorepository; copying this Paper II folder alone is not a standalone distribution.
