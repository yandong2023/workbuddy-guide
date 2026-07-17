---
title: "用 WorkBuddy 批量重命名文件：先预览，再小批量执行"
description: "根据日期、主题和类型统一文件名，并保留映射表和恢复方案。"
category: office
difficulty: intermediate
created_at: 2026-07-17
updated_at: 2026-07-17
verified_at: null
verification: source-verified
status: published
tested_platform: null
workbuddy_version: null
sources:
  - https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/File-Recognition
  - https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Permission-Modes
  - https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/FQA
---

# 用 WorkBuddy 批量重命名文件：先预览，再小批量执行

> 验证状态：B 级来源核对。官方实践文档列出了批量命名场景；本文安全流程尚未完成本项目的完整人工实测。

批量重命名看起来简单，但一旦命名规则错误，可能导致文件难以恢复、扩展名变化或同名覆盖。因此不要直接让 WorkBuddy 对正式目录全量执行。

## 准备测试副本

1. 复制 5—10 个代表性文件到测试目录；
2. 保留原目录不动；
3. 检查文件扩展名是否真实；
4. 保持默认权限；
5. 先选择 Plan 模式或只要求生成预览。

## 第一步：只生成重命名预览

```text
请分析当前目录中的文件，但暂时不要重命名。

命名规则：YYYY-MM-DD_主题_类型_序号.原扩展名

要求：
1. 根据文件内容、创建时间或现有文件名判断日期和主题；
2. 无法确认时标记“待确认”，不要猜测；
3. 保留原扩展名；
4. 检查是否会出现同名冲突；
5. 生成 rename-preview.csv，字段包括：原文件名、新文件名、判断依据、风险；
6. 等我确认后再执行。
```

## 第二步：人工检查预览表

重点检查：

- 日期来源是否正确；
- 主题是否过于宽泛；
- 是否出现非法字符；
- 文件扩展名是否改变；
- 是否有两个文件得到相同新名称；
- 是否有文件无法识别；
- 排序后是否仍容易查找。

## 第三步：小批量执行

```text
请只对 rename-preview.csv 中 status=approved 的前 5 个文件执行重命名。

要求：
1. 不得覆盖已有文件；
2. 遇到同名时停止并报告；
3. 不得移动或删除文件；
4. 生成 rename-result.csv，记录执行前后名称和结果；
5. 完成后等待我检查，不要继续处理剩余文件。
```

确认无误后再扩大批次。

## 恢复方案

重命名前必须保存原名和新名映射。需要恢复时：

```text
请根据 rename-result.csv 生成恢复预览，只展示将如何把新文件名改回原文件名。
不要立即执行，先检查是否存在名称冲突或缺失文件。
```

## 不适合自动判断的情况

以下文件应进入人工确认：

- 内容相似但版本不同；
- 扫描件无法识别；
- 合同、发票等需要严格编号；
- 文件名包含法务或合规要求；
- 同一文件可能属于多个主题；
- 原文件时间信息不可靠。

## 文件丢失怎么办

官方 FAQ 记录过整理桌面后疑似文件丢失的情况。发生异常时：

1. 立即停止后续任务；
2. 检查目标目录和回收站；
3. 保存生成脚本、预览表和执行结果；
4. 不要继续运行可能覆盖文件的操作；
5. 从备份恢复，并保留异常信息用于反馈。

## 参考资料

- [实践一：文件内容识别与处理](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/File-Recognition)
- [Permission Modes](https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Permission-Modes)
- [WorkBuddy 中文 FAQ](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/FQA)

## 更新记录

- 2026-07-17：创建批量重命名预览、小批量执行和恢复流程。