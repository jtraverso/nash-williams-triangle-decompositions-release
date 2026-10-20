# Joint first-release checklist

Current state: **HOLD_FOR_PAPER_II**. Website preparation is not publication.

1. Receive Paper II's final manuscript and companion in EN/ES and MD/TeX/PDF,
   its selected source freeze, SHA-256, licences, build and axiom evidence.
   Do not infer its status from Paper I's dependency closure.
2. Import only that final package. Update Paper I–II cross-references and
   companions against the final public source locations. Preserve protected
   mathematics and sources; regenerate document artifacts only if edited.
3. Close the joint editorial, bibliography, visual, provenance and integrity
   audit. Explicitly inspect private URLs and machine-local paths in the
   selected public material; preserve original evidence privately when a
   public derivative needs redaction.
4. Record manuscript distribution rights and Paper II's third-party licences.
   Apache-2.0 already governs the original packaging code.
   Reconcile the [Paper I author-header correction](AUTHORSHIP_REVIEW.md)
   with the final source archive, its hashes and verification scope.
   Apply the same attribution inventory to the incoming Paper II package.
5. Update CFF/BibTeX, document tables, `PUBLICATION_INDEX.json`, the site
   allowlist and checksums. Run `python scripts/verify_repository.py`.
6. Retain previous versions only in the private research repository.
   If necessary export the final tree without preparation history for the
   first public commit. Do not include `superseded`, old freezes, old PDFs,
   caches or duplicated historical release archives.
7. Obtain the author's authorization for this complete joint package.
   Then change the release conditions and run the production site builder.
8. Publish the verified first edition on GitHub and activate Cloudflare Pages
   using the documented settings. Verify the live document links.
9. Deposit the eight final PDFs on Zenodo: two manuscripts and two companions,
   in two languages. Verify titles, versions, licences, checksums and receipts.
10. Update the GitHub/site citation metadata with the confirmed version and
    concept DOI; repeat navigation and manifest checks.

No step in this preparation has created a public release or deposit.
