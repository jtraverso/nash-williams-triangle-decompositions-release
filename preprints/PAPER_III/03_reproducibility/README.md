# Reproduction — preprint 1.0

The `lean/` folder and the [formal source archive](../../../archives/PAPER_III_LEAN_SOURCE_v1.0.zip) contain the same formal supplement.
Its README specifies the pinned Lean/Mathlib versions, eight targets and six
separate endpoint queries. `HEIGHT_PROGRAM_en.md` and `HEIGHT_PROGRAM_es.md`
print the same arithmetic definitions.

Document tools require Python with PyMuPDF and Pillow, Pandoc, Tectonic and
Poppler. The `typeset.py` paths record the Windows tools used for this build;
adapt executable/cache locations for another machine. The files in `layout/`
are the series preambles, retained from Papers I and II. Run from the containing
repository, in this order:

```
python preprints/PAPER_III/03_reproducibility/generate_figures.py
python preprints/PAPER_III/03_reproducibility/typeset.py
python preprints/PAPER_III/03_reproducibility/audit_documents.py
python preprints/PAPER_III/03_reproducibility/render_review.py
```

Rendering does not itself certify visual quality: inspect the resulting pages.
The internal verdict is tied to the delivered file hashes. Regeneration may
change PDF metadata and therefore hashes; it requires a new artifact review.
The recorded mathematical audit uses validated object reuse, as described in
the companion, and is not a fresh empty-cache reconstruction.
