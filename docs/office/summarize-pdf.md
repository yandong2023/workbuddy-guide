---
title: "用 WorkBuddy 总结 PDF：从摘要到可核对的结构化笔记"
description: "提供 PDF 阅读、摘要、证据定位和输出文件的安全任务模板。"
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
  - https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/FQA
  - https://www.workbuddy.ai/docs/workbuddy/Create-Task
---

# 用 WorkBuddy 总结 PDF：从摘要到可核对的结构化笔记

> 验证状态：B 级来源核对。官方文档确认 WorkBuddy 支持文档处理；本文任务模板尚未完成本项目的完整人工实测。

PDF 总结最常见的问题不是“写得不够流畅”，而是遗漏页、识别错误、把作者观点和模型推测混在一起。因此任务中要明确范围、证据位置和输出结构。

## 开始前准备

- 使用无密码或你有权访问的 PDF；
- 涉及客户、患者、合同或内部资料时先脱敏；
- 文件较长时先确认页数；
- 把原文件放在 `input/`，结果放在 `output/`；
- 保持默认权限。

## 可直接复制的任务描述

```text
请阅读 input/report.pdf，并生成结构化中文笔记。

要求：
1. 先告诉我 PDF 的页数、目录和主要章节；
2. 用 300 字以内概括全文核心结论；
3. 按章节整理关键观点、数据、方法和限制；
4. 每个重要结论后标注对应页码；
5. 区分“原文明确陈述”和“你的推断”；
6. 无法识别或无法确认的内容标记“待核对”；
7. 不要修改原 PDF；
8. 输出到 output/report-notes.md；
9. 完成后列出未成功读取的页面或图表。
```

## PDF 中有表格或图片时

先让 WorkBuddy说明它是否能读取这些内容：

```text
请先检查第 8—15 页中的表格和图片是否可以准确识别。
暂时不要总结全文，只列出识别成功、识别不完整和无法识别的内容。
```

如果当前模型不支持文档或图片输入，官方 FAQ 建议切换到支持对应输入的模型，或安装文档处理相关 Skill。

## 长 PDF 建议分阶段处理

1. 获取目录和章节范围；
2. 每章分别提取观点和证据；
3. 汇总跨章节结论；
4. 检查页码和数字；
5. 最后生成短摘要。

直接要求“总结一本 300 页 PDF”容易产生遗漏，也难以发现是哪一部分出错。

## 如何检查摘要是否可靠

抽查至少五处：

- 摘要中的数字是否能在对应页找到；
- 是否误读表格单位；
- 是否把讨论部分写成确定结论；
- 是否遗漏原文的重要限制；
- 页码是否正确；
- 是否出现 PDF 中根本不存在的术语。

## 文件打不开或读取失败

可以依次检查：

- 文件是否损坏或加密；
- 文件扩展名是否真实；
- 当前模型是否支持 PDF；
- 是否启用了文档处理 Skill；
- 文件是否位于当前工作目录；
- 文件名是否包含特殊字符；
- 是否可以先用较小 PDF 测试。

## 隐私提醒

不要把机密 PDF 交给不明确的数据处理链路。使用自定义模型、第三方 Skill 或连接器时，还要确认文件是否会发送到外部服务。

## 参考资料

- [WorkBuddy 官方概览](https://www.workbuddy.ai/docs/workbuddy/)
- [WorkBuddy 中文 FAQ](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/FQA)
- [Create Task](https://www.workbuddy.ai/docs/workbuddy/Create-Task)

## 更新记录

- 2026-07-17：创建 PDF 总结和页码核对任务模板。