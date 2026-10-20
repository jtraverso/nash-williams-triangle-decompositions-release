# Static website and Cloudflare Pages

The root `index.html` is a bilingual series guide. Each paper has its own
`index.html`, document table, contribution summary and formalization scope.
The site uses local CSS, relative links and no runtime JavaScript, external
fonts or third-party mathematics renderer.

The organization follows the Erdős-series repository, inspected at commit
`a66dcecfce5bcd6010ee8ca6cd95ef0c2f2ecc5e`. That reference repository has a
static HTML guide but no versioned Cloudflare deployment configuration.
The Cloudflare preparation below is new for this series.

## Local review

```text
python scripts/verify_repository.py
python scripts/build_site.py --preview
python -m http.server 8000 --bind 127.0.0.1 --directory _preview
```

Open `http://127.0.0.1:8000/`. `_preview` is local and ignored by Git.
This runs no Lean/Lake commands and uploads nothing.

For the recorded browser checks, serve the same output on port 8765 and run
`node scripts/review_site.cjs` with Playwright and its Chromium browser
available. `BROWSER_PATH` optionally selects a local Chromium executable.
The script writes six screenshots and their input hashes under
`publication/web-qa/`; it makes no external requests.

## Pages configuration

| Setting | Prepared value |
|---|---|
| Framework preset | None |
| Root directory | Repository root |
| Build command | `python3 scripts/build_site.py` |
| Output directory | `dist` |
| Production branch | `main` |
| Preview branch deployments | Disabled |
| Required runtime | Python 3.12 or newer |
| Custom domain | Unassigned |

`wrangler.jsonc` records the proposed project name and output directory.
It does not create a project, bind a domain or perform a deployment.
No Cloudflare token, project ID, account ID or deploy workflow is included.
The only CI workflow validates repository integrity.

The production build exits nonzero while any release condition in
`publication/RELEASE_STATE.json` remains false. In particular, it requires
the final Paper II documents and source archive, reconciled public
references, documented manuscript rights and publication authorization.
Setting a status flag is not a substitute for those checks.

When the author authorizes launch, verify the final package first, then
connect Cloudflare Pages. A private GitHub repository does not itself make
a Pages website private. Until that authorization, do not create production
or preview deployments.

Only files enumerated in `publication/SITE_FILES.json` enter the output.
Research backups and development trees are excluded. The builder checks
local links, excludes files larger than 25 MiB and limits the file count
to 20,000. The current site is substantially smaller.

References:
[build configuration](https://developers.cloudflare.com/pages/configuration/build-configuration/),
[Pages limits](https://developers.cloudflare.com/pages/platform/limits/),
[preview deployments](https://developers.cloudflare.com/pages/configuration/preview-deployments/).

## First public edition only

The selected files constitute the first public edition; no prior editions or
`superseded` directory are included. The research repository retains the
development record. Commit attribution uses the GitHub account `jtraverso`
and its GitHub-provided no-reply address.
Both papers, their bilingual companions and their selected source archives are available in this repository. Repository visibility is controlled by GitHub settings; changing visibility requires no change to the manuscripts.
