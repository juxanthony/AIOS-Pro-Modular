# automation/ · 平台集成与自动化

让同一套 AIOS 在 Claude、ChatGPT、Gemini、Ollama 上通用，并逐步接上真正的自动化（脚本、API、定时任务）。
本目录第 7 周转正；当前先固化**接入方法**。

---

## 1. 各平台接入方法

### Claude Code（最佳体验，推荐主战场）

- 直接在本仓库开会话：根目录 `CLAUDE.md` 会自动生效，指挥 AI 按协议加载模块。
- 优势：AI 能自己读文件、检索、并**直接修改系统**（沉淀协议全自动执行）。

### Claude Projects（网页/App 日常使用）

1. 新建 Project「AIOS Pro」。
2. Project Instructions 粘贴：`README.md` 第 3 节的一句话协议。
3. Project Knowledge 上传：system/ 六件套 + 常用引擎 + 对应 knowledge 文件。
4. 系统更新后记得**替换**旧文件（Knowledge 不会自己同步）。

### ChatGPT（自定义 GPT）

1. 创建 GPT「AIOS Pro」。
2. Instructions 放 `system/SYSTEM.md` 全文（它是总协议）。
3. Knowledge 上传其余五件套与常用引擎（可先用第 3 节脚本拼包）。
4. 说明局限：文件检索质量不如 Claude Projects，重要会话可手动粘贴引擎全文。

### Gemini（Gems）

1. 新建 Gem，Instructions 放 `SYSTEM.md` + `RULES.md`（Gems 无文件库，核心协议须内嵌）。
2. 会话开头按需粘贴引擎全文。

### Ollama（本地/离线）

- Modelfile 思路：`SYSTEM` 段放 system/ 拼接产物（用第 3 节脚本生成 `dist/aios_core.md`）。
- 注意本地小模型上下文有限：只喂 SYSTEM + RULES + 当前引擎，knowledge 按需粘贴片段。

## 2. 私密层分离（公开分享前必做）

`knowledge/personal/` 与各处学生/成绩数据 = 私密层（RULES R5）。方案：

- 本仓库保持 **private**；如需公开展示系统架构，另建剥离私密层的 showcase 副本。
- 或将私密层移入 `.gitignore` 的本地目录，仓库只留结构 README。
- API key 永远只在本地环境变量，任何情况不入库。

## 3. 待建脚本（第 7 周，Backlog 见 ROADMAP）

| 脚本 | 作用 | 优先级 |
|---|---|---|
| `build_bundle.py` | 把 system/+指定引擎拼成单文件 `dist/`，供 ChatGPT/Gemini/Ollama 上传 | 高 |
| `index_prompts.py` | 扫描 prompts/ 自动重建 README 索引表 | 中 |
| `weekly_reminder` | 定时触发每周复盘（Claude Code 定时任务 / cron） | 中 |
| `stale_check.py` | 列出「最后核对」超 6 个月的 knowledge 文件 | 低 |

> 纪律：每条脚本交付 = 代码 + 一行运行命令 + 预期输出示例（engines/ai_engineer.md 输出标准）。
