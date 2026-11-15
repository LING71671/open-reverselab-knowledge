# Contributing knowledge

[简体中文](CONTRIBUTING.zh-CN.md)

Edit knowledge in this repository. The [Open ReverseLab application](https://github.com/LING71671/open-reverselab) tracks a reviewed commit through its `kb` submodule; app and content versions are independent.

1. Add reusable documents under `red/<domain>/techniques`, `blue/<domain>/techniques`, or `shared/<domain>/techniques`. Keep red and blue procedures in separate documents and connect their relevant methods.
2. Register each document and method in `knowledge.json`. Retain existing entity IDs when renaming or moving files, and retain old paths as aliases. Add the method to the appropriate attack or defense network with explicit, supported relations.
3. Add new payload files to `reverselab.extension.json`. Update `catalog/<domain>.json` when the document is used by the source-tree search tools. Its `kb/` paths are compatibility aliases for the application's submodule mount.
4. Run `python scripts/build.py`. To create a versioned ZIP, run `python scripts/build.py --version <CONTENT-VERSION> --output ../knowledge.kbpack.zip`. The destination must be outside the repository. The ZIP contains only declared content plus computed checksums.
5. Open a pull request here. Once accepted, update the application's submodule commit and repository catalog entry together if that application version should include the new content.

Use the [extension authoring skill](https://github.com/LING71671/open-reverselab/tree/main/tools/skills/create-reverselab-extension) and [v1 contract](https://github.com/LING71671/open-reverselab/blob/main/tools/skills/create-reverselab-extension/references/contract.md) for custom packs and MCP bindings. The standard-library validator is vendored in `scripts/extension_protocol.py`; update it from the application's canonical implementation when the protocol changes.

Preserve source attribution and licenses. Publish reusable material only; private cases, credentials, target identifiers and machine paths belong outside this repository. Research and examples are for lawful, authorized work; see [DISCLAIMER.md](DISCLAIMER.md).
