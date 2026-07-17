---
title: "用 WorkBuddy 创建每日资讯简报：先生成，再决定是否发送"
description: "建立包含天气、行业信息和个人待办的每日简报，并降低自动发送风险。"
category: automation
difficulty: intermediate
created_at: 2026-07-17
updated_at: 2026-07-17
verified_at: null
verification: source-verified
status: published
tested_platform: null
workbuddy_version: null
sources:
  - https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/Daily-Briefing
  - https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Automation-Guide
---

# 用 WorkBuddy 创建每日资讯简报：先生成，再决定是否发送

> 验证状态：B 级来源核对。本文依据官方每日简报案例和 Automation 文档整理，尚未完成本项目的完整人工实测。连接器、邮件和通知能力以当前版本为准。

每日简报适合把固定信息源、行业新闻和个人任务整理到一份文档中。第一版建议只自动生成，不自动发送；确认内容稳定后，再考虑邮件或消息通知。

## 先确定简报范围

不要写“每天给我所有重要新闻”。先限制：

- 地区和天气位置；
- 关注行业；
- 信息时间范围；
- 固定官方来源；
- 每个栏目条数；
- 是否需要原始链接；
- 输出文件和阅读时长。

## 第一次手动任务模板

```text
请生成今天的个人资讯简报。

时间范围：过去 24 小时。
栏目：
1. 北京天气和出行提醒；
2. AI Agent 与办公自动化的 5 条重要动态；
3. WorkBuddy 官方更新；
4. 我的待办摘要；
5. 今天最值得关注的 3 件事。

要求：
- 新闻必须附原始来源链接和发布日期；
- 同一事件去重；
- 区分事实、媒体观点和你的判断；
- 无法确认的信息不要收录；
- 每条说明“为什么值得我关注”；
- 保存为 output/YYYY-MM-DD-briefing.md；
- 先不要发送邮件或消息。
```

## 先验证三次

至少连续手动生成三次，检查：

- 信息是否真的来自过去 24 小时；
- 链接是否能打开；
- 是否把旧闻当成新消息；
- 是否重复收录同一事件；
- 是否混入与目标无关的内容；
- 待办是否来自正确来源；
- 输出是否可以在几分钟内读完。

## 创建每日自动化

手动结果稳定后，进入 Automation 创建每日任务。建议：

- 固定早晨执行时间；
- 固定工作目录；
- 文件名包含日期；
- 没有新内容时明确写“无重要更新”；
- 失败时保留错误说明；
- 不覆盖历史简报；
- 默认只生成文件。

## 连接邮箱或消息平台

官方每日简报案例展示了连接邮箱后发送简报的做法，官方 Automation 文档也提到可通过 Assistant 推送结果。

在启用发送前，增加这些限制：

```text
发送前先生成预览。
收件人必须与配置中的白名单完全一致。
没有通过内容检查时不要发送。
正文不得包含密钥、客户信息或未脱敏业务数据。
附件超过限制时只发送摘要和本地文件路径。
```

首次发送应使用自己的测试邮箱，不要直接发送到客户或工作群。

## 推荐简报结构

```text
日期与生成时间
今日摘要
天气与出行
行业重要动态
WorkBuddy 官方更新
个人待办
今日三项优先级
来源列表
生成限制与待确认事项
```

## 如何避免自动化变成信息垃圾

- 每个栏目限制条数；
- 设定“必须带来源”的硬规则；
- 优先官方和一手来源；
- 相同事件只保留一条主来源；
- 没有重要内容时允许输出空栏目；
- 每周检查哪些栏目从未产生价值；
- 定期删除无用信息源。

## 参考资料

- [实践五：每日自动推送资讯简报](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/Daily-Briefing)
- [Automation](https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Automation-Guide)

## 更新记录

- 2026-07-17：创建每日简报的手动验证、自动生成和发送安全流程。