# Distribution plan

Keep this repository as Pixel Duck's canonical package. Use upstream catalogs
only for discovery and installation links.

## 1. Published here

- Repository: <https://github.com/FlamurMaliqi/codex-pixel-duck>
- Release: <https://github.com/FlamurMaliqi/codex-pixel-duck/releases/tag/v1.0.0>
- Artwork: CC BY 4.0 by Flamur Maliqi
- Topics: `codex-pets`, `pixel-art`, and `codex-desktop`

## 2. List in Awesome Codex Pet

[Pull request #34](https://github.com/legeling/awesome-codex-pet/pull/34)
contains:

```text
pets/pixel-duck--flamurmaliqi/
├── submission.json
├── pet.json
└── spritesheet.webp
```

That catalog requires clear authorship and asset usage terms. Its ID convention
adds the author suffix; the animation itself stays unchanged.

## 3. List in Petdex

Petdex requires an authenticated account. After `npx petdex login`, submit this
repository's two-file package with `npx petdex submit .`. Petdex is already the
broad community gallery, so there is no benefit in copying its web app or
thousands of hosted assets into this project.

## 4. Link related collections

Codex Anime Pets is a themed fan-art collection rather than a general registry.
Link to it as a related project; do not vendor its images. Its artwork is
limited to personal, non-commercial use and is not covered by its MIT
documentation license.

## Why not merge the repositories?

Their code, catalogs, and artwork have different maintainers and licenses.
Publishing one canonical pet package and listing it in multiple catalogs gives
users one maintained version without silently relicensing anyone else's work.
