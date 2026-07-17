---
title: "第一次使用 WorkBuddy：怎样把任务说清楚"
description: "通过一个通用任务模板，减少遗漏步骤、错误输出和反复沟通。"
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
  - https://www.workbuddy.ai/docs/workbuddy/Quickstart
  - https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/Efficient-Tips
---

# 第一次使用 WorkBuddy：怎样把任务说清楚

> 验证状态：B 级来源核对。本文依据官方文档整理，尚未完成本项目的完整人工实测。

“帮我做一个报告”通常太模糊。更稳定的任务描述应当包含：目标、输入、步骤、输出、限制和成功标准。

## 通用任务模板

```text
请帮我完成【任务目标】。

输入材料：
- 【文件或资料】

请按以下步骤处理：
1. 【第一步】
2. 【第二步】
3. 【第三步】

输出要求：
- 输出格式：【Word / Excel / PPT / Markdown / PDF】
- 保存位置：【目标文件夹】
- 面向对象：【领导 / 客户 / 同事 / 自己】
- 风格或长度：【要求】

限制：
- 不要修改原始文件；
- 不确定的信息请标记，不要自行编造；
- 执行删除、覆盖、发送或公开发布前先询问我；
- 完成后列出生成和修改的文件。
```

## 示例：整理会议材料

```text
请读取我提供的会议记录，整理成一份会议纪要。

要求：
1. 提取会议主题、时间、参与角色、结论和待办；
2. 待办按负责人和截止时间整理；
3. 无法确认的负责人标记为“待确认”；
4. 输出 Markdown 和 Word 两个版本；
5. 不要修改原始会议记录；
6. 完成后告诉我文件保存位置。
```

## 提升成功率的做法

- 引用明确的文件，而不是让 Agent 猜文件位置；
- 把“好看”“专业”改成可检查的要求；
- 大任务先让它列计划，再开始执行；
- 在同一个任务中继续修改，而不是每次重新开始；
- 检查生成文件和变更列表后再接受结果。

## 权限提醒

涉及文件修改、外部程序或工作区以外的路径时，WorkBuddy 可能要求确认。不要在不清楚影响范围时直接开放完全访问。

## 参考资料

- [WorkBuddy Quick Start](https://www.workbuddy.ai/docs/workbuddy/Quickstart)
- [WorkBuddy Tips & Tricks](https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/Efficient-Tips)

## 更新记录

- 2026-07-17：创建通用任务描述模板。
