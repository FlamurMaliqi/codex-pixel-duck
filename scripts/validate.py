#!/usr/bin/env python3
"""Validate the two-file Codex pet package without third-party dependencies."""

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "pet.json"
SPRITESHEET = ROOT / "spritesheet.webp"
VALID_SIZES = {(1536, 1872): 1, (1536, 2288): 2}


def webp_size(path: Path) -> tuple[int, int]:
    data = path.read_bytes()
    if data[:4] != b"RIFF" or data[8:12] != b"WEBP":
        raise ValueError("spritesheet.webp is not a WebP RIFF file")

    offset = 12
    while offset + 8 <= len(data):
        kind = data[offset : offset + 4]
        length = int.from_bytes(data[offset + 4 : offset + 8], "little")
        payload = data[offset + 8 : offset + 8 + length]

        if kind == b"VP8X" and len(payload) >= 10:
            return (
                int.from_bytes(payload[4:7], "little") + 1,
                int.from_bytes(payload[7:10], "little") + 1,
            )
        if kind == b"VP8L" and len(payload) >= 5 and payload[0] == 0x2F:
            bits = int.from_bytes(payload[1:5], "little")
            return (bits & 0x3FFF) + 1, ((bits >> 14) & 0x3FFF) + 1
        if kind == b"VP8 " and len(payload) >= 10 and payload[3:6] == b"\x9d\x01\x2a":
            return (
                int.from_bytes(payload[6:8], "little") & 0x3FFF,
                int.from_bytes(payload[8:10], "little") & 0x3FFF,
            )

        offset += 8 + length + (length % 2)

    raise ValueError("could not read WebP dimensions")


def main() -> None:
    pet = json.loads(MANIFEST.read_text(encoding="utf-8"))
    required = {"id", "displayName", "description", "spritesheetPath"}
    missing = sorted(required - pet.keys())
    if missing:
        raise ValueError(f"pet.json is missing: {', '.join(missing)}")
    if pet["id"] != "pixel-duck":
        raise ValueError("pet.json id must be pixel-duck")
    if pet["spritesheetPath"] != SPRITESHEET.name:
        raise ValueError("pet.json spritesheetPath must be spritesheet.webp")

    dimensions = webp_size(SPRITESHEET)
    if dimensions not in VALID_SIZES:
        raise ValueError(f"unsupported spritesheet dimensions: {dimensions}")

    version = pet.get("spriteVersionNumber", 1)
    if version != VALID_SIZES[dimensions]:
        raise ValueError("spriteVersionNumber does not match spritesheet dimensions")

    digest = hashlib.sha256(SPRITESHEET.read_bytes()).hexdigest()
    print(f"OK: {pet['displayName']} · {dimensions[0]}x{dimensions[1]} · sha256:{digest}")


if __name__ == "__main__":
    main()
