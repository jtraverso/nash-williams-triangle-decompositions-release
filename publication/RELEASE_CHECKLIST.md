# Coordinated release operations

Current operational state: **HOLD_FOR_AUTHOR_PUBLICATION_AUTHORIZATION**.

The articles and companions use final publication-facing metadata, including their reserved DOI identifiers. Both selected source archives and their licences are installed. This preparation does not activate the DOI or change repository visibility.

1. Verify the current repository manifest, article manifests, archive hashes, document audit and website screenshots.
2. Obtain the author's authorization to publish this exact package.
3. Publish the repository and connect Cloudflare Pages using the documented configuration. Verify the live document links.
4. Complete the two reserved Zenodo deposits with the four final PDFs for each paper. Verify uploaded hashes and metadata before publishing.
5. Record publication receipts and concept DOI identifiers; verify the live DOI and site links.

The production builder remains blocked while `public_release_authorized` is false. Previous source packages and manuscripts remain in the research archive; this release tree includes only the selected edition.
