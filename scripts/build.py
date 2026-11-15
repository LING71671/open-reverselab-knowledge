#!/usr/bin/env python3
"""Validate or build this knowledge pack with Python's standard library."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from extension_protocol import MANIFEST, json_bytes, load, pack, validate

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", help="Set the content SemVer before building")
    parser.add_argument("--output", type=Path, help="ZIP destination outside this repository")
    args = parser.parse_args()
    payload, archive = load(ROOT)
    manifest = json.loads(payload[MANIFEST])
    if args.version:
        manifest["version"] = args.version
        payload[MANIFEST] = json_bytes(manifest)
    validate(payload, archive)
    if args.version:
        (ROOT / MANIFEST).write_bytes(payload[MANIFEST])
    knowledge = json.loads(payload[manifest["knowledge"]])
    result = {"id": manifest["id"], "version": manifest["version"],
              "documents": len(knowledge["documents"]), "methods": len(knowledge["methods"]),
              "networks": len(knowledge["networks"])}
    if args.output:
        result.update(pack(ROOT, args.output))
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
