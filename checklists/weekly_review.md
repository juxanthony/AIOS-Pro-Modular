# Checklist: 每周复盘（约 20 分钟）

> 引擎: 无（系统级）· 依据: system/SELF_IMPROVEMENT.md 第 4 节
> 建议固定时段：周日晚。可让 AI 陪跑：挂载任意会话直接说「跑每周复盘」。

## A. 记忆刷新（MEMORY.md L3）

- [ ] 打开 `knowledge/personal/current.md`：完成的条目划掉/归档
- [ ] 过期或不再重要的条目删除
- [ ] 写下下周每条主线的「最重要一件事」（≤5 条）

## B. 系统改进（SELF_IMPROVEMENT）

- [ ] 回看本周的摩擦记录/聊天缓存：有没有解释了第二遍的背景？→ 入 IDENTITY/knowledge
- [ ] 有没有第二次手写的指令？→ 入 prompts/（记得更新 prompts/README 索引）
- [ ] 有没有返工超过一轮的成品？→ 修对应模板或规则
- [ ] 本周被批准的系统修改都记入 CHANGELOG `[Unreleased]` 了吗？

## C. 进度对表（ROADMAP）

- [ ] 本周所属的 ROADMAP 模块达成「完成标准」了吗？达成 → 版本号 +0.1 并归档 CHANGELOG
- [ ] 未达成 → 写一句卡点原因，决定：顺延 / 缩小范围 / 调整计划

## D. 收尾

- [ ] 跑维护脚本并处理报告项：`python automation\scripts\index_prompts.py --check` + `python automation\scripts\stale_check.py`
- [ ] git commit 本周全部改动（信息格式：`weekly: <周次> <一句话>`)
- [ ] 用一句话给本周打分留档（current.md 底部）
