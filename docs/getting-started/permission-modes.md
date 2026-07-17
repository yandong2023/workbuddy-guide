---
title: "WorkBuddy 权限模式怎么选：默认权限与完全访问"
description: "说明两种权限模式的区别、适用场景和安全使用方法。"
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
  - https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Permission-Modes
  - https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Task-Bar
---

# WorkBuddy 权限模式怎么选：默认权限与完全访问

> 验证状态：B 级来源核对。按钮位置和名称可能随版本变化，尚未完成本项目的完整人工实测。

WorkBuddy 可以读取和写入文件，也可能运行脚本或外部程序。官方文档提供默认权限和完全访问两种模式。

## 默认权限

适合日常使用。Agent 可以在工作区内完成常规任务，但遇到可能跨越重要边界的操作时会停下来请求确认。

推荐用于：

- 第一次执行的新任务；
- 不熟悉的 Skill 或脚本；
- 含有重要文件的目录；
- 涉及网络、发送、删除或覆盖的任务。

## 完全访问

它会减少确认步骤，允许 Agent 直接执行更多操作。效率更高，但错误指令、脚本缺陷或误判也可能造成更大影响。

只建议在以下条件同时满足时临时使用：

- 任务来源可信；
- 工作目录已隔离；
- 重要文件已有备份；
- 操作可以恢复；
- 你理解它将运行的命令或修改范围。

## 推荐做法

1. 默认保持“默认权限”；
2. 给任务单独建立工作目录；
3. 复制文件后再让 Agent 修改；
4. 明确写出“不要删除和覆盖原文件”；
5. 只在受控任务中临时切换完全访问；
6. 完成后切回默认权限并检查变更。

## 参考资料

- [Permission Modes](https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Permission-Modes)
- [新建任务栏与权限管理](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Task-Bar)

## 更新记录

- 2026-07-17：依据官方权限文档创建。
