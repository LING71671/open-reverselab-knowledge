# Knowledge Base AI Usage

本仓库维护可复用知识。应用仓库通过 `kb/` 子模块引用这里；下文 `kb/` 是该兼容挂载路径，当前仓库根目录已经是知识库根目录。

## 写入规则

- 可复用技巧、payload 模式、CVE workflow、绕过方法写入 `kb/`。
- 单题/单样本证据不要写进 `kb/`，应写 `notes/` 或 `reports/`。
- 每篇技巧应包含：适用场景、输入信号、验证步骤、常见误判、工具命令、输出位置。

## 当前重点

- Web CTF：`red/ctf-website/README.md` 与 `blue/ctf-website/README.md`
- APK 逆向：`red/apk-reverse/README.md` 与 `blue/apk-reverse/README.md`
- PE 逆向：`red/pe-reverse/README.md` 与 `blue/pe-reverse/README.md`
- 通用安全：`red/general/README.md` 与 `blue/general/README.md`
- CVE 关联网：`red/ctf-website/techniques/09-cve/cve-correlation-graph.md`

## AI 联动

- 发现新通用技巧后，从 case 笔记提炼到 `kb/`。
- 用 `kb/` 指导脚本和模板更新，而不是只停留在文字说明。

## 轨道与关联

使用 `track: red | blue | both`；共享技术标为 `both`。防御文档用 `defends` 指向对应技术路径，并同步领域 `kb-index.json` 中的分类。技术文档放在 `kb/red/<领域>/`、`kb/blue/<领域>/`，共享方法放在 `kb/shared/<领域>/`。统一索引位于 `kb/catalog/<领域>.json`，文件路径以仓库根目录为基准。更新索引后检查桌面关联阅读与 `kb_router --track` 的结果。

red 与 blue 使用独立文件，攻击方法与 `*-defense.md` 分别维护完整操作路径；通过关联链接交换线索。red 从本领域 `attack-network.md` 进入，blue 从 `defense-network.md` 进入；both 的每个分支沿自己的入口检索和执行。

扩展内容通过 `knowledge.json` 与 `reverselab.extension.json` 登记。修改后执行 `python scripts/build.py`；具体步骤见 [贡献指南](CONTRIBUTING.zh-CN.md)。
