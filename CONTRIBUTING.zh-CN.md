# 贡献知识库

[English](CONTRIBUTING.md)

知识内容在本仓库修改。[Open ReverseLab 应用](https://github.com/LING71671/open-reverselab)通过 `kb` 子模块固定一个已检查的提交，应用版本与内容版本分别维护。

1. 文档分别放在 `red/<领域>/techniques`、`blue/<领域>/techniques` 或 `shared/<领域>/techniques`。红蓝两方保留独立操作流程，通过相关方法建立联系。
2. 在 `knowledge.json` 登记文档与方法。移动或重命名时保留已有实体 ID，并将旧路径保留为别名；将方法加入对应攻击网或防御网，关系依据实际内容填写。
3. 在 `reverselab.extension.json` 声明新增内容文件。供源码检索工具使用的文章同时更新 `catalog/<领域>.json`；其中 `kb/` 路径兼容应用中的子模块挂载位置。
4. 发布内容修改时提升 `reverselab.extension.json` 中的 `version`，包括文档修订。应用检查仓库默认分支上的 SemVer 版本；只修改 ZIP 文件名或 Git 标签不会通知新版。保留实体 ID，跨包依赖声明精确版本。
5. 执行 `python scripts/build.py`。打包使用 `python scripts/build.py --output ../knowledge.kbpack.zip`，输出放在仓库外。ZIP 只包含声明的内容文件与计算得到的摘要；`--version <CONTENT-VERSION>` 只覆盖 ZIP 的版本，不修改源码清单。
6. 向本仓库提交 PR。内容合入后，需要更新应用所引用的内容时，再同步更新应用的子模块提交与仓库目录条目。

自定义包与 MCP 绑定参照[扩展创建 skill](https://github.com/LING71671/open-reverselab/tree/main/tools/skills/create-reverselab-extension)和 [v1 协议](https://github.com/LING71671/open-reverselab/blob/main/tools/skills/create-reverselab-extension/references/contract.zh-CN.md)。`scripts/extension_protocol.py` 是随仓库提供的标准库校验器，协议变化时从应用仓库的规范实现同步。

保留来源与许可，只提交可复用知识；私人案例、凭据、真实目标标识与机器路径保存在仓库外。研究和示例用于合法授权范围内的工作，见[免责声明](DISCLAIMER.zh.md)。
