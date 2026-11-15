# Open ReverseLab 知识库

[English](README.md) · [Open ReverseLab 应用](https://github.com/LING71671/open-reverselab) · [在线阅读](https://ling71671.github.io/open-reverselab/kb/README.html)

本仓库独立维护攻击网、防御网、技术文章与可安装知识包。应用源码中的 `kb` 通过 Git 子模块链接到这里，内容版本与桌面版本分别发布。

在应用的“扩展”中输入 `https://github.com/LING71671/open-reverselab-knowledge`，读取并安装官方知识包。也可导入 GitHub 下载的源码 ZIP 或构建后的 `.kbpack.zip`；原应用仓库的扩展目录仍可找到本知识包。

技术文档按策略和领域组织，red 与 blue 分别维护完整操作流程，通用方法只保留一份。

- [Red](red/README.md)：攻击网、分析路径与复现方法。
- [Blue](blue/README.md)：防御网、检测、控制措施与验证。
- [共享方法](shared/README.md)：两边都会使用的识别、调试、算法和协议方法。

`both` 分别检索 red、blue 与共享文档，通过关联链接交换证据，不复制第三套技术文档。

| 领域 | red | blue | 共享 |
| --- | --- | --- | --- |
| Web / CTF | [Red](red/ctf-website/README.md) | [Blue](blue/ctf-website/README.md) | [共享方法](shared/ctf-website/README.md) |
| Android / APK | [Red](red/apk-reverse/README.md) | [Blue](blue/apk-reverse/README.md) | [共享方法](shared/apk-reverse/README.md) |
| Windows / PE | [Red](red/pe-reverse/README.md) | [Blue](blue/pe-reverse/README.md) | [共享方法](shared/pe-reverse/README.md) |
| General | [Red](red/general/README.md) | [Blue](blue/general/README.md) | [共享方法](shared/general/README.md) |
| Windows 专项 | [Red](red/windows/README.md) | — | [共享方法](shared/windows/README.md) |

## 检索与维护

```sh
python scripts/build.py
python scripts/build.py --output ../open-reverselab-knowledge.kbpack.zip
```

`catalog/<领域>.json` 维护信号、轨道、工具和配对关系，`files` 使用仓库相对路径。文档仍通过 `defends` / `defended_by` 关联。`path-aliases.json` 将旧路径映射到当前文档，供桌面、MCP 和官网保留历史链接。

Python 3.10 以上即可构建，无需安装依赖或检出应用源码。`knowledge.json` 声明文档、方法与网络关系，`reverselab.extension.json` 声明内容版本与包内文件。

写作约定见 [AI-USAGE.md](AI-USAGE.md)，贡献方式见[贡献指南](CONTRIBUTING.zh-CN.md)，自定义包可使用[扩展创建 skill](https://github.com/LING71671/open-reverselab/tree/main/tools/skills/create-reverselab-extension)。

采用 [Apache-2.0](LICENSE) 许可。研究和示例用于合法授权范围内的工作，见[免责声明](DISCLAIMER.zh.md)。
