---
title: "如何让 WorkBuddy 创建自己的 Skill"
description: "把重复工作沉淀为可复用 Skill，并明确触发条件、输入输出和权限边界。"
category: skills
difficulty: intermediate
created_at: 2026-07-17
updated_at: 2026-07-17
verified_at: null
verification: source-verified
status: published
tested_platform: null
workbuddy_version: null
sources:
  - https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/Create-Skills
  - https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/Create-Skills
---

# 如何让 WorkBuddy 创建自己的 Skill

> 验证状态：B 级来源核对。本文依据官方中英文文档整理，尚未完成本项目的完整人工实测。

官方文档说明，可以直接在任务中描述需要的能力，让 WorkBuddy 生成 Skill 配置和实现文件，再安装并测试。

## 先定义一个单一能力

首个 Skill 不要试图解决十种任务。适合从高频、输入稳定、输出可检查的流程开始，例如：

- 将 CSV 统一转换成指定格式；
- 根据固定模板生成周报；
- 监控一个文件夹并整理新文件；
- 把会议记录整理成结构化待办。

## 可直接复制的创建指令

```text
请为我创建一个自定义 Skill，用于【明确任务】。

触发条件：
- 当我说【触发语句或意图】时触发。

输入：
- 【文件类型、字段或必要信息】。

处理规则：
1. 【规则一】
2. 【规则二】
3. 遇到不确定信息时标记“待确认”，不要编造。

输出：
- 保存为【格式】；
- 保存到【目录】；
- 完成后列出生成文件。

权限限制：
- 不得删除或覆盖原文件；
- 不得向外部发送数据；
- 执行工作目录之外的操作前先询问我。

请同时生成 README，说明安装、测试、权限和卸载方法。
```

## 安装前检查

- Skill 将运行哪些脚本；
- 是否访问网络或第三方 API；
- 读写哪些目录；
- 是否需要完全访问；
- 失败后是否可能覆盖或删除数据；
- 配置中是否意外写入密钥。

## 测试方法

先使用一份无敏感信息的样例文件，并在隔离目录中运行。确认输入、输出、失败处理和日志都符合预期后，再处理真实任务。

## 参考资料

- [实践八：创建自己的 Skills](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/Create-Skills)
- [Practice 8: Creating Custom Skills](https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/Create-Skills)

## 更新记录

- 2026-07-17：依据官方文档创建 B 级教程。
