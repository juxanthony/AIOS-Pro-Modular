# CLAUDE.md — AIOS Pro 加载入口

本仓库不是软件项目，而是 Anthony 的个人 AI 操作系统（AIOS Pro）：一组供 AI 加载的 Markdown 模块。

在本仓库的任何会话中：

1. 先阅读 `system/SYSTEM.md`，并按其指示读完 `system/` 目录其余文件（IDENTITY / RULES / MEMORY / THINKING / SELF_IMPROVEMENT）。
2. 根据用户的当前任务，从 `engines/` 加载**一个**对应引擎，再按引擎声明的依赖去 `knowledge/`、`templates/`、`checklists/`、`prompts/` 取文件。不要一次性加载整个仓库。
3. 修改本仓库内容时遵守 `system/SELF_IMPROVEMENT.md` 的变更协议：改动后在 `CHANGELOG.md` 的 `[Unreleased]` 下记一行。
4. 遇到 `【待填写：…】` 占位符：那是 Anthony 尚未提供的私人信息，不得虚构填充；需要时向用户询问。
5. 写作语言遵循 `system/RULES.md`：简体中文为主，术语/代码用英文，Guru Cemerlang 材料可用马来文。
