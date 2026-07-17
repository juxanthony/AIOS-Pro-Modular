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

> 进行中：第 2–6 周五个引擎（Teacher / Research+Writing / GC / Basketball / YouTube）均内容就绪，各自实战检验后转正并发布版本

### Added

- `knowledge/teacher/subject_curriculum.md` —— 历史/数学/英文三科 KSSR 框架层摘要（含「编号只抄 DSKP」纪律）。
- `knowledge/teacher/class_profiles.md`、`school_context.md` —— 班级与学校语境骨架（私密层，待填写）。
- `prompts/teaching/P-T-003_remarks_pbd.md` —— 学生评语与 PBD 等级说明。
- **第 3 周**：`knowledge/phd/` 四件 —— 课题档案（数学教育·混合方法·开题）、格式规范与论证铁律、导师档案、文献笔记库规范。
- `workflows/proposal_writing.md` —— 开题六关工作流（问题→文献→框架→方法→成文→defence），当前研究主线。
- `prompts/research/P-R-003_paper_reading.md`、`P-R-004_rq_refinement.md`；`prompts/writing/P-W-002_argument_check.md`。
- `templates/supervisor_update.md` —— 导师进度汇报模板。
- **第 4 周**：`knowledge/teacher/gc_profile.md` —— GC 申报档案（复盘/条件对照/证据清单/时间线，数学科·今年再战）。
- `workflows/gc_application.md` —— 申报再战六关（情报→复盘→证据→文书→评审→提交）。
- `templates/gc_evidence_entry.md`、`gc_innovation_report.md`；`prompts/guru_cemerlang/P-G-001`、`P-G-002`。
- **第 5 周**：`knowledge/basketball/team_profile.md`（三线档案：校队/校外/个人 + 对手情报）、`drills.md`（起步库 8 类 26 条，含小学生适配总则）。
- `workflows/weekly_training_plan.md`（备战周计划）、`workflows/game_review.md`（赛后复盘）。
- `templates/training_session.md`；`prompts/basketball/P-B-001`（课案）、`P-B-002`（复盘）、`P-B-003`（个人自训）。
- **第 6 周**：`knowledge/youtube/channel_profile.md`（起步期档案 + 四候选定位分析）、`topic_pool.md`（打分规则 + 四方向 20 个实验选题）、`analytics_log.md`（双时点复盘骨架）。
- `workflows/channel_positioning.md` —— 定位决策（资产盘点→三环检验→实验→定案），起步期第一优先。
- `templates/shorts_script.md`；`prompts/youtube/P-Y-002`（选题工厂）、`P-Y-003`（脚本起草，长/短双模板）。

### Changed

- `system/IDENTITY.md` —— 教学主线占位符补全：小学 KSSR，三科（2026-07-17，来自 Anthony 本人）。
- `templates/lesson_plan.md` —— 升级为 KSSR RPH 正式格式（马来文字段 + 中文注释，含 EMK/KBAT/PBD）。
- `engines/teaching.md` —— 按真实科目校准；状态 骨架 → 试运行；依赖清单落到具体文件。
- `workflows/lesson_planning.md` —— 接入 DSKP 抄录纪律与 PBD 自检点。
- `ROADMAP.md` —— 第 2 周标记「内容就绪，待实战检验」。
- **第 3 周**：`engines/research.md` 按课题语境校准（骨架 → 试运行，接入「当前卡点」机制）；`engines/writing.md` 接入学术论证铁律（骨架 → 试运行）。
- `system/IDENTITY.md` —— 博士主线占位符补全：数学教育、混合方法、开题阶段（2026-07-17，来自 Anthony 本人）。
- `ROADMAP.md` —— 第 3 周标记「内容就绪，待实战检验」。
- **第 4 周**：`engines/guru_cemerlang.md` 按申报语境校准（骨架 → 试运行，接入时间线报警机制）。
- `system/IDENTITY.md` —— GC 主线占位符补全：数学科、曾申报、今年再战（2026-07-17，来自 Anthony 本人）。
- `ROADMAP.md` —— 第 4 周标记「内容就绪，待实战检验」，完成标准改为「情报关+复盘关跑通」。
- **第 5 周**：`engines/basketball.md` 按三线语境校准（骨架 → 试运行，接入备战模式与安全红线）。
- `system/IDENTITY.md` —— 篮球主线占位符补全：三线并行、每周 3+ 次、备战比赛（2026-07-17，来自 Anthony 本人）。
- `ROADMAP.md` —— 第 5 周标记「内容就绪，待实战检验」。
- **第 6 周**：`engines/youtube_business.md` 按起步语境校准（骨架 → 试运行：定位优先、产能现实主义、产品链经营）；`workflows/youtube_video_pipeline.md` 加入起步期定位实验规则。
- `system/IDENTITY.md` —— YouTube 主线占位符补全：起步期、定位四候选、长短结合、自有产品变现（2026-07-17，来自 Anthony 本人）。
- `ROADMAP.md` —— 第 6 周标记「内容就绪，待实战检验」，完成标准改为「定位定案 + 首支视频全流程」。

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
