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

> 进行中：第 2 周 Teacher Engine、第 3 周 Research/Writing Engine —— 均为内容就绪，各自实战检验后转正并发布版本

### Added

- `knowledge/teacher/subject_curriculum.md` —— 历史/数学/英文三科 KSSR 框架层摘要（含「编号只抄 DSKP」纪律）。
- `knowledge/teacher/class_profiles.md`、`school_context.md` —— 班级与学校语境骨架（私密层，待填写）。
- `prompts/teaching/P-T-003_remarks_pbd.md` —— 学生评语与 PBD 等级说明。
- **第 3 周**：`knowledge/phd/` 四件 —— 课题档案（数学教育·混合方法·开题）、格式规范与论证铁律、导师档案、文献笔记库规范。
- `workflows/proposal_writing.md` —— 开题六关工作流（问题→文献→框架→方法→成文→defence），当前研究主线。
- `prompts/research/P-R-003_paper_reading.md`、`P-R-004_rq_refinement.md`；`prompts/writing/P-W-002_argument_check.md`。
- `templates/supervisor_update.md` —— 导师进度汇报模板。

### Changed

- `system/IDENTITY.md` —— 教学主线占位符补全：小学 KSSR，三科（2026-07-17，来自 Anthony 本人）。
- `templates/lesson_plan.md` —— 升级为 KSSR RPH 正式格式（马来文字段 + 中文注释，含 EMK/KBAT/PBD）。
- `engines/teaching.md` —— 按真实科目校准；状态 骨架 → 试运行；依赖清单落到具体文件。
- `workflows/lesson_planning.md` —— 接入 DSKP 抄录纪律与 PBD 自检点。
- `ROADMAP.md` —— 第 2 周标记「内容就绪，待实战检验」。
- **第 3 周**：`engines/research.md` 按课题语境校准（骨架 → 试运行，接入「当前卡点」机制）；`engines/writing.md` 接入学术论证铁律（骨架 → 试运行）。
- `system/IDENTITY.md` —— 博士主线占位符补全：数学教育、混合方法、开题阶段（2026-07-17，来自 Anthony 本人）。
- `ROADMAP.md` —— 第 3 周标记「内容就绪，待实战检验」。

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
