---
title: "WorkBuddy 为什么总是询问权限"
description: "解释频繁授权提示的常见原因，以及减少提示但不牺牲安全的方法。"
category: troubleshooting
difficulty: beginner
created_at: 2026-07-17
updated_at: 2026-07-17
verified_at: null
verification: source-verified
status: published
tested_platform: null
workbuddy_version: null
sources:
  - https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Permission-Modes
---

# WorkBuddy 为什么总是询问权限

> 验证状态：B 级来源核对。本文根据官方权限说明整理，尚未完成本项目的完整人工实测。

频繁出现授权提示，通常是因为任务需要修改文件、运行程序、访问工作区外路径或执行其他敏感操作。默认权限会在这些边界前停下来让用户确认。

## 先检查工作区

把本次任务需要的文件复制到单独工作目录，并在创建任务时选择该目录。Agent 频繁跨目录查找文件，更容易触发额外确认。

## 把任务范围写清楚

```text
只在当前工作目录内读取和生成文件。
不要访问其他目录。
不要删除或覆盖原文件。
需要运行外部程序、访问网络或修改工作区外文件时先询问我。
```

## 是否应该切换完全访问

完全访问可以减少确认，但不建议长期默认开启。只应在任务可信、目录隔离、文件已备份、操作可恢复时临时使用，完成后再切回默认权限。

## 仍然频繁询问时

记录触发提示的具体动作、目标路径和当前权限模式，再对照官方文档或提交 Issue。不要仅凭提示次数判断为软件故障。

## 参考资料

- [WorkBuddy Permission Modes](https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Permission-Modes)

## 更新记录

- 2026-07-17：依据官方权限说明创建。
