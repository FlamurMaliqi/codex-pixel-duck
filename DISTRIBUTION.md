# Distribution plan

Keep this repository as Pixel Duck's canonical package. Use upstream catalogs
only for discovery and installation links.

## 1. Publish here

1. The original GIF is owned by Flamur Maliqi and licensed under CC BY 4.0.
2. Create the public GitHub repository.
3. Tag `v1.0.0` and attach a ZIP containing `pet.json` and
   `spritesheet.webp`.
4. Add the `codex-pets`, `pixel-art`, and `codex-desktop` GitHub topics.

## 2. List in Awesome Codex Pet

Open one pull request containing:

```text
pets/pixel-duck--flamurmaliqi/
├── submission.json
├── pet.json
└── spritesheet.webp
```

That catalog requires clear authorship and asset usage terms. Its ID convention
adds the author suffix; the animation itself stays unchanged.

## 3. List in Petdex

Submit this repository's two-file package through Petdex's documented upload
flow. Petdex is already the broad community gallery, so there is no benefit in
copying its web app or thousands of hosted assets into this project.

## 4. Link related collections

Codex Anime Pets is a themed fan-art collection rather than a general registry.
Link to it as a related project; do not vendor its images. Its artwork is
limited to personal, non-commercial use and is not covered by its MIT
documentation license.

## Why not merge the repositories?

Their code, catalogs, and artwork have different maintainers and licenses.
Publishing one canonical pet package and listing it in multiple catalogs gives
users one maintained version without silently relicensing anyone else's work.
