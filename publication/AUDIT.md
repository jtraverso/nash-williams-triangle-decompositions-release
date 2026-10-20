# Repository preparation audit

Scope: the **private preparation** of the first public edition. This is a
packaging and navigation audit, not a new mathematical, bibliographic or
Lean-kernel audit.

## Protected content

The twelve Paper I manuscript/companion files (EN/ES; MD/TeX/PDF) and the
selected ZIP, SHA sidecar and seal were imported byte for byte from private
review commit `2c99ea261d0af6261e173975b4f6264f8334004d`.
[INTAKE.json](INTAKE.json) records the hashes of all fifteen files.
No Lean, mathematical manuscript or generated document was edited.

The previous private navigation citation dated Paper I 19 October; the
new repository's citation metadata uses the actual manuscript date,
20 October 2026. This changes new navigation metadata only.

## Checks

Run:

```text
python scripts/verify_repository.py
python scripts/build_site.py --preview
python scripts/build_site.py
```

The first two commands must succeed. The last must currently fail with
`RELEASE HELD` and must not create a production output. The checks cover
all imported hashes, the 3,237 internal archive hashes, exact licence texts,
all repository-manifest entries, local Markdown/HTML links, selected archive
inventory and the bounded site allowlist.

The [test record](PREPARATION_CHECKS.json) records the checks performed.
The [visual review](VISUAL_REVIEW.md) records browser inspection.

## Open release conditions

- Paper II's final documents, archive, licences and proof evidence have not
  been received here. Its directories contain only structural README files.
- Current Paper I artifacts still contain private-review references. These
  must be reconciled with the final joint public edition, followed by
  affected document audits and manifests.
- Manuscript public-distribution rights remain to be recorded; the original
  software packaging uses Apache-2.0 with third-party notices preserved.
- The [author-header review](AUTHORSHIP_REVIEW.md) confirms 1,008 missing
  headers, 59 surname errors and one tool attribution in the selected
  source archive. A verified comment-only patch is prepared privately;
  it has not been applied to the selected ZIP or its build receipts.
- The final joint audit and public-release authorization remain pending.

Historical audits and superseded editions remain in the private review
repository. They are not copied into the first-public-edition tree.

There is no publication workflow, Cloudflare deployment, public Pages URL,
Zenodo deposit or DOI in this preparation.
