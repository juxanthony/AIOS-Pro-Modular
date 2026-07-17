# workflows/ · 工作流（SOP）规范

**工作流 = 步骤 ≥3、顺序重要、会反复执行的标准作业流程。**
一次性的做法不入库；单步指令去 prompts/；成品骨架去 templates/。

## 命名与结构

- 文件名：`<动宾短语>.md`，如 `lesson_planning.md`。
- 统一结构：

```markdown
# Workflow: <名称>
yaml 元信息（模块/版本/状态/所属引擎/预计耗时）
## 触发条件      ← 什么情况下启动本流程
## 输入          ← 开始前要备齐什么
## 步骤          ← 编号步骤；每步 = 动作 + 产物；标注哪步用哪个 prompt/模板
## 完成标准      ← 怎样算做完
## 常见坑        ← 实战踩过的坑（越用越厚）
```

## 首批工作流

| 文件 | 所属引擎 | 状态 |
|---|---|---|
| `lesson_planning.md` | teaching | 骨架（第 2 周实战校准） |
| `literature_review.md` | research | 骨架（第 3 周实战校准） |
| `youtube_video_pipeline.md` | youtube_business | 骨架（第 6 周实战校准） |

## 质量纪律

- 每条工作流必须**经过至少一次真实任务检验**才能标「正式」。
- 执行中发现步骤不对 → 当场改文件（这正是 SELF_IMPROVEMENT 循环）。
- 「常见坑」小节只写真实踩过的坑，不写想象的。
