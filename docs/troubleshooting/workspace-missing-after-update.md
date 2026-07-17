---
title: "WorkBuddy 更新或重启后工作空间不见了怎么办"
description: "检查默认工作目录、历史任务和独立备份，并避免把正式文件只保存在应用工作区。"
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
  - https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/FQA
---

# WorkBuddy 更新或重启后工作空间不见了怎么办

> 验证状态：B 级来源核对。本文依据官方中文 FAQ 整理，尚未完成本项目的完整人工实测。默认目录可能随系统和版本变化。

界面中看不到历史工作空间，不一定代表文件已经删除。先停止新任务，避免新文件覆盖旧目录，然后从磁盘和任务列表分别检查。

## 第一步：不要重装或清理目录

发现工作空间不见后，先不要：

- 反复卸载和重装；
- 清理应用数据；
- 删除看不懂的工作目录；
- 使用磁盘清理工具；
- 在原位置创建大量新文件。

这些操作可能降低恢复机会。

## 第二步：检查默认 WorkBuddy 目录

官方中文 FAQ 给出的常见目录包括：

```text
Windows：C:/Users/你的用户名/Tencent WorkBuddy
Mac：/Users/你的用户名/Tencent WorkBuddy
```

实际目录可能不同。可以按修改时间查找近期创建的文件夹，并检查是否存在以日期或任务名称命名的目录。

不要把完整用户名或个人路径发到公开 Issue 中。

## 第三步：检查任务列表和工作空间列表

官方 FAQ 提到，最近对话可能显示在“助理”区域，而其他任务仍在工作空间列表中。分别检查：

- 左侧任务列表；
- 工作空间列表；
- 搜索功能；
- 历史任务；
- 最近使用的目录；
- Assistant 或远程任务入口。

找到任务后先查看文件路径，再决定是否继续执行。

## 第四步：全盘搜索已知文件名

如果记得某个结果文件名，可以在 Finder 或文件资源管理器中搜索：

```text
weekly-report.md
report.pptx
meeting-minutes.docx
```

也可以按最近修改日期和扩展名查找，但不要使用会修改文件的批处理脚本。

## 第五步：找到后立即复制到独立目录

恢复文件后：

1. 复制到独立业务目录；
2. 检查文件是否完整；
3. 记录原始路径；
4. 不要只保留在 WorkBuddy 自动创建的工作空间；
5. 重要文件建立外部备份。

## 如何预防再次发生

推荐结构：

```text
正式资料目录/
├── source/          # 原始资料
├── workbuddy/       # 给 WorkBuddy 的副本
├── deliverables/    # 已确认交付物
└── backups/         # 备份
```

任务结束后，把确认过的结果从 WorkBuddy 工作目录复制到 `deliverables/`，不要把临时工作区当作永久存储。

## 更新前检查清单

- 关闭正在运行的任务；
- 导出或复制重要结果；
- 记录关键工作目录；
- 检查安装目录中是否误放个人文件；
- 更新后先进行小任务测试；
- 确认历史工作空间仍能打开。

## 仍无法找到时

收集以下信息并向官方反馈：

- 操作系统和版本；
- WorkBuddy 版本；
- 更新或重启时间；
- 原工作空间名称；
- 记得的文件名；
- 已检查的路径；
- 是否进行过重装或清理。

日志和截图可能包含路径、对话和设备信息，上传前先确认隐私范围。

## 参考资料

- [WorkBuddy 中文常见问题](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/FQA)

## 更新记录

- 2026-07-17：创建工作空间查找、恢复和外部备份指南。