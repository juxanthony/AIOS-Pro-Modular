# AIOS Pro · 个人 AI 操作系统（模块化版）

> 一套陪伴多年、持续进化的个人知识与工作平台。
> 不是一份 Prompt，而是一个可以像软件一样维护、扩充、升级的系统。

**版本**：v1.0.0 ·「建设完成 · 运营期」
**owner**：Anthony
**上游**：由 AIOS Ultimate v5 Master（单文件版）演化而来，本仓库是其模块化重构。

---

## 1. 这是什么

AIOS Pro 把「你希望 AI 如何为你工作」拆分成一组相互独立、可以按需加载的 Markdown 模块：

- **system/** —— 内核。身份、规则、记忆、思考方式、自我改进机制。任何时候都应加载。
- **engines/** —— 引擎。教学、研究、写作、AI 工程、YouTube、篮球等专业模式，按当前任务加载其中一个。
- **knowledge/** —— 知识库。按领域沉淀的长期事实与资料，供引擎调用。
- **workflows/** —— 工作流。跨越多个步骤的标准作业流程（SOP）。
- **prompts/** —— Prompt 库。可直接复用的指令，按领域编号管理。
- **templates/** —— 模板。教案、论文笔记、视频脚本等成品的骨架。
- **checklists/** —— 清单。发布前、复盘时逐项核对的检查表。
- **automation/** —— 自动化。与 Claude、ChatGPT、Gemini、Ollama、API 及脚本的集成方式。

设计原则只有三条：

1. **模块化**：一个文件只讲一件事，改一处不牵动全局。
2. **可加载**：每个模块自带元信息（版本、状态、依赖），AI 读到就知道怎么用。
3. **可进化**：所有变更走 `CHANGELOG.md`，系统随着使用不断变好，永远不需要推倒重来。

## 2. 目录地图

```text
AIOS-Pro-Modular/
│
├── README.md                  ← 你在这里：总览与使用方法
├── CHANGELOG.md               ← 版本历史
├── ROADMAP.md                 ← 8 周建设计划与长期愿景
├── CLAUDE.md                  ← Claude Code / Claude Projects 的自动加载入口
│
├── system/                    ← 内核（永远加载）
│   ├── SYSTEM.md              ← 启动协议：加载顺序、优先级、冲突裁决
│   ├── IDENTITY.md            ← 我是谁 + AI 是谁
│   ├── MEMORY.md              ← 记忆系统：记什么、怎么记、何时更新
│   ├── RULES.md               ← 全局规则：语言、格式、诚实性、隐私
│   ├── THINKING.md            ← 思考框架：何时用哪种思维模型
│   └── SELF_IMPROVEMENT.md    ← 系统自我改进循环
│
├── knowledge/                 ← 领域知识库（按需加载）
│   ├── teacher/               ← 教学：课标、班级、学校语境
│   ├── phd/                   ← 博士研究：课题、文献、导师要求
│   ├── basketball/            ← 篮球：训练体系、球队资料
│   ├── youtube/               ← 频道定位、数据、选题池
│   ├── ai/                    ← AI 工程：技术栈、项目档案
│   └── personal/              ← 个人：目标、习惯、长期记忆存档
│
├── engines/                   ← 专业引擎（一次加载一个）
│   ├── teaching.md            ← 教学引擎
│   ├── research.md            ← 研究引擎
│   ├── writing.md             ← 写作引擎
│   ├── guru_cemerlang.md      ← Guru Cemerlang 引擎
│   ├── ai_engineer.md         ← AI 工程引擎
│   ├── youtube_business.md    ← YouTube 商业引擎
│   └── basketball.md          ← 篮球引擎
│
├── workflows/                 ← 多步骤 SOP
├── prompts/                   ← Prompt 库（带编号与元数据）
├── templates/                 ← 成品模板
├── checklists/                ← 检查清单
└── automation/                ← 平台集成与脚本
```

## 3. 快速开始（给 AI 的加载协议）

任何 AI 会话中使用 AIOS Pro，按以下顺序：

1. **必读**：`system/SYSTEM.md` →（它会指示继续读完 system/ 其余五个文件）
2. **按任务选一个引擎**：例如备课 → `engines/teaching.md`
3. **引擎会声明依赖**：按它列出的清单去 `knowledge/`、`templates/`、`checklists/` 取所需文件
4. **不要一次加载全部仓库** —— 上下文预算优先留给当前任务

一句话版本（可直接粘贴给任何 AI）：

> 请先阅读 system/ 目录下全部文件并遵守其中协议，然后根据我接下来的任务，从 engines/ 中加载对应引擎再开始工作。

## 4. 在各平台使用

| 平台 | 方法 | 详见 |
|---|---|---|
| Claude Code | 仓库根目录的 `CLAUDE.md` 自动生效 | `automation/README.md` |
| Claude Projects | 将 system/ + 常用引擎上传为 Project Knowledge | `automation/README.md` |
| ChatGPT (GPTs) | system/ 六件套合并上传为 Knowledge，SYSTEM.md 摘要放 Instructions | `automation/README.md` |
| Gemini | Gems 的 Instructions 放 SYSTEM.md，其余作为对话首条粘贴 | `automation/README.md` |
| Ollama（本地） | Modelfile 的 SYSTEM 段引用 system/ 拼接产物 | `automation/README.md` |

## 5. 约定

- **语言**：正文以简体中文为主；专业术语、代码、文件名用英文；Guru Cemerlang 相关材料可用马来文。
- **文件命名**：目录小写；系统级文件大写（`SYSTEM.md`）；引擎与其他内容文件小写下划线（`youtube_business.md`）。
- **状态标签**：每个模块头部标注 `状态: 正式 / 骨架 / 草稿`。骨架 = 结构已定、内容待第 N 周填充（见 ROADMAP）。
- **版本**：整个系统一个版本号（语义化：主.次.修订），变更记入 `CHANGELOG.md`。
- **占位符**：`【待填写：…】` 表示需要 Anthony 本人补充的私人信息，AI 不得虚构。

## 6. 现在处于哪一步

**8 周建设计划已收官（v1.0.0，2026-07-17）**：System 内核正式、七个引擎试运行、
31 条 Prompt（八域全覆盖，索引自动化）、8 条工作流、8 个模板、2 份清单、
3 条自动化脚本实测跑通（打包 / 索引 / 保鲜）。

当前是**运营期**，两件事并行：

1. **引擎转正**：每个引擎经一次真实任务检验后由「试运行」改「正式」（条件清单见 `engines/README.md`）。
2. **持续进化**：每周复盘（可让 AI 主持，见 `P-S-002`）驱动 SELF_IMPROVEMENT 循环 —— 系统随使用越来越贴手。
