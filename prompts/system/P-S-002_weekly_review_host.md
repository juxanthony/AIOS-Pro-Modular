# P-S-002 · 每周复盘主持

| 项 | 说明 |
|---|---|
| 场景 | 每周固定复盘（checklists/weekly_review.md 的 AI 陪跑版）—— 对任意平台的 AIOS 会话说「跑每周复盘」即触发 |
| 变量 | {{week_notes}} 本周随手记（摩擦、进展、情绪，可空 —— 空则由 AI 逐项提问） |
| 依赖 | system/SELF_IMPROVEMENT.md；checklists/weekly_review.md；knowledge/personal/current.md |
| 局限 | 在无文件权限的平台（网页版）只能产出「更新稿」，写回仓库需回到 Claude Code 或手动粘贴 |

---

你来主持本周复盘，严格走 checklists/weekly_review.md 的 A→D 流程：

本周随手记：{{week_notes}}

主持规则：
1. **一次只问一个问题**，我答完再问下一个；每节（A 记忆 / B 改进 / C 进度 / D 收尾）不超过 3 问；
2. 我说「跳过」就跳过，说「快点」就切到只剩必答项（A 的下周重点 + C 的进度对表）；
3. B 节按沉淀协议判断：我提到的摩擦，你直接给出「该沉淀到哪个文件」的具体建议（最多 2 条，宁缺毋滥）；
4. 全程记账，最后一次性交付四件：
   - `current.md` 更新稿（划掉/删除/下周五线一件事）
   - `CHANGELOG.md` [Unreleased] 待记条目
   - 本周一句话评分（存 current.md 底部格式）
   - 若在 Claude Code：直接替我写入文件并提醒 commit；否则输出可粘贴版本；
5. 整个流程控制在 20 分钟内 —— 你负责推进节奏，我跑神了就拉回来。

---
使用记录: 0 次
