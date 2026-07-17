# P-B-001 · 单次训练课生成

| 项 | 说明 |
|---|---|
| 场景 | 周计划确定主题后，生成某一次课的完整细案（workflows/weekly_training_plan.md 第 3 步） |
| 变量 | {{track}} 线别（校队 A/校外 B/个人 C）；{{theme}} 周主题；{{session_role}} 本课在周结构中的角色（技术/对抗/赛前减量）；{{logistics}} 时长/人数/场地/器材 |
| 依赖 | engines/basketball.md；knowledge/basketball/drills.md、team_profile.md；templates/training_session.md |
| 局限 | 到场人数临时变化时，分组方案需现场调整（模板的组织栏给出 A/B 方案更稳） |

---

挂载篮球引擎。生成一次训练课细案（格式：templates/training_session.md）：

- 线别：{{track}}；周主题：{{theme}}；本课角色：{{session_role}}
- 现实条件：{{logistics}}

规则：
1. Drill 优先从 drills.md 选取（写库内名称），确需新练习则按库格式写全并建议入库；
2. 对抗环节必须带**规则杠杆**且指向周主题（如主题是退防 → 条件赛「被快攻得分翻倍」）；
3. 遵守模板自检项：讲解 ≤2 分钟、排队 ≤4 人、时长总和 = 课时、高强度在热身后；
4. 校队 A 线按小学生适配总则；备战期按「距比赛天数」调整对抗占比与强度（赛前 48h 减量）；
5. 每个环节给「人数异动 B 方案」一句（少 2 人/多 2 人怎么改分组）。

---
使用记录: 0 次
