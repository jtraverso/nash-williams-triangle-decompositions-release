# Repository and document audit

The current articles and companions have separate editorial audit records under each paper's `02_validation` directory. The response tables address every external-review item. The audits check bilingual mathematical parity, bibliographic attribution, rendered pages and exact artifact hashes; they do not claim a new mathematical peer review or a new Lean compilation.

The [intake record](INTAKE.json) binds the installed documents and selected evidence to the research commit. The repository verifier checks every imported hash, both source archives (7,801 internal hashes), dependency licence texts, all local links, the complete repository manifest and six desktop/mobile website captures.

```text
python scripts/verify_repository.py
python scripts/build_site.py --preview
```

The production command `python scripts/build_site.py` must remain blocked until publication is authorized. See [operational state](RELEASE_STATE.json) and [release checklist](RELEASE_CHECKLIST.md).

[Paper I review response](../preprints/PAPER_I/02_validation/RESPONSE_TO_REVIEW.md) · [Paper II review response](../preprints/PAPER_II/02_validation/RESPONSE_TO_REVIEW.md) · [Browser review](VISUAL_REVIEW.md).
