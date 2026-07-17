# knowledge/ · 知识库规范

存放各领域的**稳定事实与资料**（MEMORY.md 的 L2 层），供引擎按需调用。
这里放「是什么」；「怎么做」放 workflows/，「说什么」放 prompts/。

## 目录

| 子目录 | 领域 | 供给引擎 |
|---|---|---|
| `teacher/` | 课标摘要、班级档案、学校语境、教学实绩 | teaching, guru_cemerlang |
| `phd/` | 课题档案、文献笔记、格式规范、导师偏好 | research, writing |
| `basketball/` | 球队档案、drill 库、战术库、赛程 | basketball |
| `youtube/` | 频道定位、观众画像、选题池、数据基线 | youtube_business |
| `ai/` | 技术栈档案、项目清单、工具清单 | ai_engineer |
| `personal/` | 当前进行事项（L3）、目标、风格样本、归档 | 全部（私密层） |

## 条目规范

1. **一文件一主题**，文件名小写下划线（`team_profile.md`）。
2. 每个文件头部标注：`最后核对: YYYY-MM-DD`。超过 6 个月未核对，引用时须提醒可能过期。
3. 有来源的资料注明来源（尤其政策类：注明 pekeliling/文件号与获取日期）。
4. 事实条目带日期：`- [2026-07-17] 内容`（格式见 MEMORY.md）。
5. **宁缺毋滥**：没有真实内容前不建空文件；每个子目录的 README 列着「首批待建清单」。

## 隐私分级

- `personal/` 整体 + 各目录中涉及学生/成绩/个人数据的文件 = **私密层**（RULES R5）。
- 若仓库需要公开分享，先按 automation/README.md 的私密层分离方案处理。
