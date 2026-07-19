# .claude/agents/ · Claude Code 子代理团队

**Agent 团队 = 三层流水线**，套在现有引擎体系之上（引擎本身就是领域专家，agent 不重复它们）：

```text
strategist（Opus·分析）→ builder（Sonnet·执行）→ qa-gate（Opus·质检 95/100）→ 交付 Anthony
```

| Agent | 模型 | 一句话职责 |
|---|---|---|
| `strategist.md` | Opus | 拆解任务、选定引擎、产出任务简报（成品规格 + 验收标准） |
| `builder.md` | Sonnet | 挂载简报指定的引擎，产出可直接使用的成品 |
| `qa-gate.md` | Opus | 按验收标准打分，< 95 退回 builder；R2/R5 问题一票否决 |

## 使用方式

- **自动**：在本仓库运行 Claude Code，复杂任务会按 description 自动委派（strategist 与 qa-gate 均标记 PROACTIVELY）。
- **手动**：对话中直接点名，如「用 strategist 先拆解这个任务」「让 qa-gate 检查这份教案」。
- 简单单步任务无需走全流水线：strategist 会直说「builder 可直接执行」，或你直接找 builder。

## 设计原则

1. **一个 agent 一个职责**（分析 / 执行 / 质检），领域专业性来自 `engines/`，不在 agent 里复制。
2. **一次一个引擎**：沿用 `system/SYSTEM.md` 第 2 节的挂载规则。
3. **质量门槛前置声明**：验收标准写进任务简报，builder 按合同交付，qa-gate 按合同验收。
4. 新增 agent 的门槛比照 `engines/README.md`：确有独立职责且高频出现，否则并入现有三员。
