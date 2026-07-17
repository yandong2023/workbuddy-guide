---
title: "Ask、Plan、Craft 怎么选：WorkBuddy 三种工作模式"
description: "说明问一问、想一想和做一做的区别，以及普通用户在不同任务中如何选择。"
category: getting-started
difficulty: beginner
created_at: 2026-07-17
updated_at: 2026-07-17
verified_at: null
verification: source-verified
status: published
tested_platform: null
workbuddy_version: null
sources:
  - https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Task-Bar
---

# Ask、Plan、Craft 怎么选：WorkBuddy 三种工作模式

> 验证状态：B 级来源核对。本文依据官方任务栏说明整理，尚未完成本项目的完整人工实测。模式名称和入口可能随版本变化。

WorkBuddy 的工作模式决定了它是只回答问题、先给计划，还是直接执行并修改文件。对普通用户来说，选对模式比写很复杂的提示词更重要。

## Ask：先问清楚，不修改文件

官方中文文档把 Ask 对应为“问一问”。它适合：

- 了解一个文件讲了什么；
- 询问应该怎么完成任务；
- 让 AI 解释表格字段或文档结构；
- 讨论方案，但暂时不生成和修改文件；
- 第一次接触陌生任务或陌生 Skill。

示例：

```text
请先阅读这些材料，告诉我它们分别讲了什么、有哪些冲突，以及下一步应该如何整理。
现在不要修改或生成任何文件。
```

## Plan：先给执行计划，再决定是否开始

官方中文文档把 Plan 对应为“想一想”。它适合：

- 多步骤任务；
- 任务可能影响很多文件；
- 需要先确认输出结构；
- 涉及数据清洗、批量重命名或复杂报告；
- 你不确定 WorkBuddy 会调用哪些能力。

示例：

```text
请先检查当前目录并制定执行计划，说明：
1. 将读取哪些文件；
2. 将生成或修改哪些文件；
3. 会使用哪些工具或 Skill；
4. 可能遇到什么风险；
5. 如何备份和回滚。

在我确认计划前不要开始执行。
```

## Craft：直接执行并交付文件

官方中文文档把 Craft 对应为“做一做”。它适合：

- 目标、输入和输出都已经明确；
- 工作目录已经隔离；
- 原文件已有备份；
- 任务步骤已验证或风险较低；
- 你需要直接生成 Word、Excel、PPT 或其他产物。

示例：

```text
请根据已确认的大纲生成 PPT 初稿。
不要修改原始资料，输出到 output 文件夹，并列出所有新建文件。
```

## 最简单的选择规则

| 你的情况 | 推荐模式 |
|---|---|
| 只是想问问题或看懂文件 | Ask |
| 不知道它会怎么做，想先看方案 | Plan |
| 任务清楚、目录隔离、可以直接执行 | Craft |
| 涉及删除、覆盖、发送或公开发布 | 先 Plan，再人工确认 |
| 第一次使用一个新 Skill | 先 Ask 或 Plan |

## 普通用户推荐流程

不要一上来就长期使用 Craft。更稳妥的流程是：

```text
Ask：确认需求和资料
  ↓
Plan：审查执行步骤和影响范围
  ↓
Craft：在隔离目录中执行
  ↓
人工检查结果和文件变更
```

## 模式和权限不是一回事

工作模式决定“怎么完成任务”，权限模式决定“遇到敏感操作时是否需要确认”。

即使选择 Craft，也可以继续使用默认权限；即使选择 Ask，也不要在不必要时开放完全访问。

## 参考资料

- [新建任务栏（本地 AI 工作台）](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Task-Bar)

## 更新记录

- 2026-07-17：创建 Ask、Plan、Craft 模式选择指南。