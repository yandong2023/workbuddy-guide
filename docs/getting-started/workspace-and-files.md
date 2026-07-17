---
title: "WorkBuddy 工作目录怎么设置：避免误删、误改和找不到文件"
description: "说明工作目录的作用、推荐目录结构、文件引用方法和安全边界。"
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
  - https://www.workbuddy.ai/docs/workbuddy/Create-Task
  - https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Task-Bar
  - https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Permission-Modes
---

# WorkBuddy 工作目录怎么设置：避免误删、误改和找不到文件

> 验证状态：B 级来源核对。本文依据官方创建任务、任务栏和权限说明整理，尚未完成本项目的完整人工实测。

工作目录是 WorkBuddy 当前任务主要读取和保存文件的位置。目录选得越清楚，Agent 越不容易到处找文件，也越容易检查它做了什么。

## 不要直接选择整个桌面或磁盘

第一次使用时，不建议把以下位置作为工作目录：

- 整个桌面；
- 下载目录；
- 用户主目录；
- 整个移动硬盘；
- 公司共享盘根目录；
- 唯一一份正式资料所在目录。

这些目录通常包含大量无关文件，一旦任务描述不清楚，可能产生误移动、误重命名或覆盖风险。

## 推荐目录结构

每个任务建立单独文件夹：

```text
销售分析-2026-07/
├── input/        # 原始文件副本，只读使用
├── output/       # 生成结果
├── backup/       # 必要备份
└── notes.md      # 任务说明和人工备注
```

告诉 WorkBuddy：

```text
只读取 input 文件夹。
所有新文件保存到 output 文件夹。
不要修改、移动、重命名或删除 input 中的任何文件。
```

## 如何把文件提供给 WorkBuddy

官方创建任务文档列出了几种方式：

- 选择工作目录；
- 使用 `@` 引用文件或上下文；
- 拖入或上传文件；
- 粘贴截图；
- 在任务描述中明确文件名和输出格式。

文件很多时，优先选择工作目录并点名关键文件，不要只写“分析一下这些资料”。

## 一个清晰的文件任务模板

```text
工作目录：当前目录。

输入：
- input/sales.xlsx
- input/product-notes.md

任务：
1. 读取两个文件；
2. 先说明字段和资料结构；
3. 分析销售变化及可能原因；
4. 无法从资料确认的原因标记为“待确认”；
5. 不要修改 input 中的文件；
6. 把结果保存到 output/report.md；
7. 完成后列出读取、新建和修改过的文件。
```

## 为什么找不到生成文件

常见原因包括：

- 没有指定工作目录；
- 没有指定输出路径；
- 只要求“生成报告”，没有说明文件格式；
- 结果保存在 WorkBuddy 自动创建的任务目录；
- 只在对话中输出了文本，没有要求生成文件。

任务结束前可以补充：

```text
请确认最终文件已经实际保存，并给出完整文件名和所在目录。
```

## 权限边界

官方权限说明建议日常保持默认权限。工作目录不是无限授权：当任务尝试访问目录之外的位置、运行程序或执行敏感操作时，仍可能请求确认。

不要因为提示频繁，就把整个电脑长期设为完全访问。更好的办法是缩小工作目录、减少跨目录引用并把输入复制到任务文件夹。

## 任务完成后的检查

至少检查：

- `input/` 是否保持不变；
- `output/` 中是否只有预期文件；
- 是否出现未知脚本或临时文件；
- 文件名和扩展名是否正确；
- 内容是否可以打开；
- WorkBuddy 的变更列表是否与磁盘实际情况一致。

## 参考资料

- [Create Task](https://www.workbuddy.ai/docs/workbuddy/Create-Task)
- [新建任务栏](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Task-Bar)
- [Permission Modes](https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Permission-Modes)

## 更新记录

- 2026-07-17：创建工作目录和文件安全指南。