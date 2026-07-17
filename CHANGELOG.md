# CHANGELOG

本系统的所有重要变更都记录在此文件。
格式遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)；版本号遵循语义化版本（主.次.修订）。

规则：

- **主版本**：架构级变化（目录重组、加载协议变更）。
- **次版本**：新增或完成一个模块/引擎。
- **修订**：内容修正、措辞打磨、小幅补充。
- 每次修改系统，先改文件，再在 `[Unreleased]` 下记一行；发布时归档为新版本号。

---

## [Unreleased]

（暂无）

## [0.1.0] - 2026-07-17

### Added

- 建立模块化仓库骨架：`system/`、`knowledge/`、`engines/`、`workflows/`、`prompts/`、`templates/`、`checklists/`、`automation/`。
- **第 1 周 · System 内核六件套**（状态：正式）：
  - `system/SYSTEM.md` —— 启动协议、加载顺序、优先级与冲突裁决
  - `system/IDENTITY.md` —— 用户档案与 AI 角色定位
  - `system/MEMORY.md` —— 三层记忆架构与更新协议
  - `system/RULES.md` —— 全局规则（语言、格式、诚实性、隐私、边界）
  - `system/THINKING.md` —— 思考框架库与深度分级
  - `system/SELF_IMPROVEMENT.md` —— 自我改进循环
- 七个引擎的启动版（状态：骨架，按 ROADMAP 逐周转正）：
  teaching / research / writing / guru_cemerlang / ai_engineer / youtube_business / basketball。
- 各内容目录的规范 README 与首批示例（工作流 ×3、Prompt ×6、模板 ×3、清单 ×2）。
- 根文档：`README.md`、`ROADMAP.md`、`CLAUDE.md`（Claude Code 加载入口）、`automation/README.md`（四平台接入指南）。

### Notes

- 本版本对应 ROADMAP「第 1 周」交付物；私人信息以 `【待填写：…】` 占位，待 Anthony 补充。
