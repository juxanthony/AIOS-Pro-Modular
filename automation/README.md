# automation/ · 平台集成与自动化

让同一套 AIOS 在 Claude、ChatGPT、Gemini、Ollama 上通用，并用脚本消灭系统维护的重复劳动。
**状态：三条链路已实测跑通（2026-07-17）**；唯一前提是电脑装有 Python（python.org 下载，安装时勾选 "Add Python to PATH"）。

---

## 1. 已建脚本（实测通过）

| 脚本 | 作用 | 怎么跑（Windows） |
|---|---|---|
| `scripts/build_bundle.py` | 把 system 六件套 + 指定引擎拼成单文件，输出到 `dist/`，供上传各平台 | **双击 `automation/build_bundle.bat`**（一键全打包）；或命令行 `python automation\scripts\build_bundle.py teaching` |
| `scripts/index_prompts.py` | 扫描 prompts/ 自动重建 README 索引表 | `python automation\scripts\index_prompts.py`（加 `--check` 只查不改） |
| `scripts/stale_check.py` | 列出「最后核对」超过 180 天的知识文件 | `python automation\scripts\stale_check.py`（可加 `--days 90`） |

约定：

- 打包产物在 `dist/`，**已被 .gitignore 排除** —— 因为 bundle 含 IDENTITY 等私密层内容，只上传到你本人的 AI 账号，不公开分享。
- 脚本全部只用 Python 标准库，不需要 pip 安装任何东西。
- 每周复盘（`checklists/weekly_review.md`）时顺手跑一遍 `--check` 与 `stale_check`。

## 2. 各平台接入方法（上传物一律用 build_bundle 生成）

### Claude Code（最佳体验，推荐主战场）

- 直接在本仓库开会话：根目录 `CLAUDE.md` 自动生效。AI 能自己读文件、检索、并直接修改系统（沉淀协议全自动执行），无需打包。

### Claude Projects（网页/App 日常使用）

1. 新建 Project「AIOS Pro」，Instructions 粘贴 README 第 3 节的一句话协议。
2. Knowledge 上传 `dist/aios_core.md` + 常用引擎的 bundle（如 `aios_teaching.md`）。
3. 系统更新后重新打包并**替换**旧文件（Knowledge 不会自己同步）。

### ChatGPT（自定义 GPT）

1. 创建 GPT「AIOS Pro」，Instructions 放 `system/MASTER_PROMPT.md` 正文（横线内的八节）。
2. Knowledge 上传对应 bundle（一个引擎一个文件，检索更稳）。

### Gemini（Gems）

1. 新建 Gem，Instructions 放 `system/MASTER_PROMPT.md` 正文（Gems 无文件库，压缩版正合适）。
2. 会话开头按需粘贴引擎 bundle。

### Ollama（本地/离线）

- Modelfile 的 `SYSTEM` 段引用 `dist/aios_core.md` 内容；本地小模型上下文有限，引擎与知识按需粘贴片段。

## 3. 私密层分离（公开分享前必做）

- 本仓库保持 **private**；`dist/` 与 `knowledge/personal/` 属私密层（RULES R5）。
- 如需公开展示系统架构，另建剥离私密层的 showcase 副本。
- API key 永远只在本地环境变量，任何情况不入库。

## 4. 下一步（Backlog）

| 项 | 说明 | 状态 |
|---|---|---|
| weekly_reminder | 每周复盘提醒：Windows 任务计划程序 / 手机闹钟 + 清单链接 / Claude Code 定时任务，三选一 | ⬜ 待 Anthony 选方案 |
| 成绩/表格批处理 | 学生成绩、PBD 记录的批量整理（教学线需求明确后立项） | ⬜ |
| 文献半自动入库 | PDF → P-R-003 精读笔记 → literature/ 的流水线 | ⬜ |
