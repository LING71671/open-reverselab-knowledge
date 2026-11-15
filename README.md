# Open ReverseLab Knowledge

[简体中文](README.zh-CN.md) · [Open ReverseLab application](https://github.com/LING71671/open-reverselab) · [Browse online](https://ling71671.github.io/open-reverselab/en/kb/README.html)

Attack networks, defense networks, and shared analysis methods for Open ReverseLab. This repository maintains the knowledge sources and installable knowledge pack independently of the desktop runtime.

## Install

Open **Extensions** in Open ReverseLab and enter:

```text
https://github.com/LING71671/open-reverselab-knowledge
```

Read the source and install **Open ReverseLab knowledge**. You can also import this repository's downloaded source ZIP or a built `.kbpack.zip`. The application's repository catalog links here, so its existing import URL remains usable.

## Update

For a GitHub installation, open **Extensions → Knowledge → Check for updates**, then choose **Update to …**. The app checks this repository's default branch and installs the exact commit found during that check. New Goals use the enabled new version; existing Goals retain their pinned documents, methods, networks, and cross-package references. Disabled packs stay disabled after updating.

ZIP imports remain local copies. Import a new ZIP to add its version, then enable the copy you want to use. Content updates do not require a desktop release.

## Knowledge

Red and blue keep separate procedures and exchange evidence through related methods. Shared analysis methods have one source; `both` retrieves the relevant red, blue, and shared content.

| Domain | Attack network | Defense network | Shared methods |
| --- | --- | --- | --- |
| Web / CTF | [Red](red/ctf-website/techniques/attack-network.md) | [Blue](blue/ctf-website/techniques/defense-network.md) | [Shared](shared/ctf-website/README.md) |
| Android / APK | [Red](red/apk-reverse/techniques/attack-network.md) | [Blue](blue/apk-reverse/techniques/defense-network.md) | [Shared](shared/apk-reverse/README.md) |
| Windows / PE | [Red](red/pe-reverse/techniques/attack-network.md) | [Blue](blue/pe-reverse/techniques/defense-network.md) | [Shared](shared/pe-reverse/README.md) |
| General | [Red](red/general/techniques/attack-network.md) | [Blue](blue/general/techniques/defense-network.md) | [Shared](shared/general/README.md) |
| Windows topics | [Red](red/windows/README.md) | — | [Shared](shared/windows/README.md) |

## Build and contribute

Python 3.10 or newer is sufficient; no packages or application checkout are required.

```sh
python scripts/build.py
python scripts/build.py --output ../open-reverselab-knowledge.kbpack.zip
```

`knowledge.json` declares stable document/method IDs, networks, and relations. `reverselab.extension.json` declares the content version and payload files. See [Contributing](CONTRIBUTING.md), the [extension protocol](https://github.com/LING71671/open-reverselab/blob/main/EXTENSIONS.md), and the [authoring skill](https://github.com/LING71671/open-reverselab/tree/main/tools/skills/create-reverselab-extension).

The application references this repository as its `kb` Git submodule. Contributions to articles and networks belong here; application code and MCP runtime changes belong in the application repository.

## License and use

[Apache-2.0](LICENSE). Research and examples are intended for lawful, authorized work; read the [disclaimer](DISCLAIMER.md).
