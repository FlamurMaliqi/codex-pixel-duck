#!/bin/sh
set -eu

project_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
codex_dir=${CODEX_HOME:-"$HOME/.codex"}
pet_dir="$codex_dir/pets/pixel-duck"

python3 "$project_dir/scripts/validate.py"
mkdir -p "$pet_dir"
cp "$project_dir/pet.json" "$project_dir/spritesheet.webp" "$pet_dir/"

printf 'Installed Pixel Duck in %s\n' "$pet_dir"
printf 'Open Codex > Settings > Pets, then select Refresh.\n'
