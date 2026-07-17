---
title: "用 WorkBuddy 分析 Excel：一份可复制的安全任务模板"
description: "让 WorkBuddy 检查表格、生成统计结果和图表，同时保留原始文件。"
category: office
difficulty: beginner
created_at: 2026-07-17
updated_at: 2026-07-17
verified_at: null
verification: source-verified
status: published
tested_platform: null
workbuddy_version: null
sources:
  - https://www.workbuddy.ai/docs/workbuddy/
  - https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market
---

# 用 WorkBuddy 分析 Excel：一份可复制的安全任务模板

> 验证状态：B 级来源核对。官方文档确认 WorkBuddy 支持表格和数据分析场景；本文任务模板尚未完成本项目的完整人工实测。

## 开始前准备

- 复制一份待分析的 Excel 文件；
- 删除或脱敏身份证号、手机号、客户姓名等不必要信息；
- 新建一个独立输出目录；
- 先使用默认权限。

## 可直接复制的任务描述

```text
请分析我提供的 Excel 文件。

要求：
1. 先读取字段名、数据量和工作表结构；
2. 检查空值、重复数据、格式异常和明显异常值；
3. 不要修改原始文件；
4. 将清洗后的数据另存为新文件；
5. 按时间、产品和地区汇总核心指标；
6. 生成适合汇报的图表；
7. 输出一份 Markdown 分析说明，列出方法、发现和限制；
8. 无法确认的数据含义请标记“待确认”，不要自行猜测；
9. 完成后列出所有生成文件及其路径。
```

## 建议分两步执行

数据量较大或字段复杂时，先让 WorkBuddy只做结构检查和分析计划。确认计划后，再让它处理数据并生成图表，便于提前发现字段理解错误。

## 怎么判断结果是否可靠

至少检查：

- 汇总数字能否从原表抽样复算；
- 是否误把文本、百分比或日期当成普通数字；
- 是否说明删除、填充或转换了哪些数据；
- 图表标题、单位和时间范围是否正确；
- 原始文件是否保持不变。

## 权限与隐私提醒

不要上传与分析目标无关的个人信息。涉及生产经营和客户数据时，应先确认公司的数据安全要求和 WorkBuddy 当前的数据处理条款。

## 参考资料

- [WorkBuddy 官方概览](https://www.workbuddy.ai/docs/workbuddy/)
- [WorkBuddy Skill Marketplace](https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market)

## 更新记录

- 2026-07-17：创建 B 级任务模板，等待真实表格实测。
