# 技术栈档案

```yaml
最后核对: 2026-07-17
```

## 基本盘

- **系统**：Windows【待填写：版本与设备型号】
- **命令行熟练度**：照步骤能跑 —— 所有脚本必须附逐步说明，优先提供 `.bat` 双击包装
- **Python**：【待填写：是否已安装 —— automation 脚本的唯一前提；未装则从 python.org 下载，安装时勾选 "Add Python to PATH"】
- **AI 平台**：Claude / ChatGPT / Gemini / 本地 Ollama **全平台在用**【待填写：各平台付费档位】
- **本地模型**：Ollama【待填写：机器配置、已装模型】
- **自动化第一优先**：AIOS 跨平台打包（✅ 已实现，见下）

## 工具偏好（ai_engineer 引擎默认遵守）

- Python 标准库优先，能不装依赖就不装
- 一切改动可回滚；动真实数据前先备份/dry-run
- API key 只放本地环境变量，绝不入库（RULES R5）

## 自动化项目清单

| 项目 | 状态 | 说明 |
|---|---|---|
| `automation/scripts/build_bundle.py` | ✅ 已实测（2026-07-17） | 跨平台打包，配 `build_bundle.bat` 双击版 |
| `automation/scripts/index_prompts.py` | ✅ 已实测（2026-07-17） | Prompt 索引自动重建 |
| `automation/scripts/stale_check.py` | ✅ 已实测（2026-07-17） | 知识库过期检查 |
| weekly_reminder（每周复盘提醒） | ⬜ 未建 | 方案候选：Windows 任务计划程序 / 手机闹钟 + 清单链接 / Claude Code 定时任务 |
