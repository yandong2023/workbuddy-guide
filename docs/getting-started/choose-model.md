---
title: "WorkBuddy 模型怎么选：先用自动模式，再按任务切换"
description: "介绍自动模式、内置模型和自定义模型的选择原则，避免只凭排行榜选模型。"
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
  - https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Model
  - https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Task-Bar
---

# WorkBuddy 模型怎么选：先用自动模式，再按任务切换

> 验证状态：B 级来源核对。本文依据官方模型配置和任务栏说明整理，尚未完成本项目的完整人工实测。可用模型会随版本、账号、地区和服务状态变化。

模型不是越贵、参数越大就一定越适合。WorkBuddy 需要模型理解任务、调用工具、读取文件并连续执行，因此应根据任务类型和失败表现选择。

## 新手先用自动模式

官方模型配置页说明，自动模式会根据任务选择模型。对新用户来说，自动模式适合：

- 不知道模型之间有什么区别；
- 日常文档、表格、PPT 和问答任务；
- 希望先观察 WorkBuddy 的默认选择；
- 不想频繁手动切换。

第一次执行时，可以记录自动模式选择了什么模型、耗时多久、是否成功，再决定是否固定模型。

## 按任务类型选择

官方任务栏文档给出了不同模型的场景建议，但具体列表可能变化。可以把它们理解成以下原则，而不是永久排名：

| 任务特点 | 优先关注的能力 |
|---|---|
| Excel、数据分析、PPT | 工具调用、结构化输出、执行速度 |
| 多步骤复杂任务 | 长流程规划和稳定执行 |
| 截图、图片转文档 | 图片理解或多模态能力 |
| 日常问答、文案 | 响应速度和成本 |
| 中文会议纪要、中文报告 | 中文表达和信息整理 |

## 什么时候应该切换模型

遇到以下情况时，可以暂停任务后换模型重试：

- 模型无法识别图片或文档；
- 反复输出文字，却没有真正调用工具；
- 长任务执行到一半丢失前文要求；
- 表格字段和数字频繁理解错误；
- 任务长时间无响应；
- 当前模型不支持所需输入类型。

不要在同一任务里无目的地连续切换很多模型。每次只改变一个变量，并记录结果。

## 一个简单的模型对比方法

准备同一份无敏感信息的样例文件，用相同指令分别执行：

```text
请读取 sample.xlsx：
1. 列出字段和数据量；
2. 检查空值和重复项；
3. 生成一个汇总表；
4. 不要修改原文件；
5. 完成后列出生成文件。
```

比较：

- 是否完成全部步骤；
- 数字能否复算；
- 是否生成正确格式的文件；
- 是否频繁中断或请求无关权限；
- 执行时间；
- 需要人工修改多少。

## 自定义模型要注意什么

官方文档说明，可在设置页面通过图形界面添加自定义模型。配置前应确认：

- 提供商和接口地址是否可信；
- 模型是否支持工具调用；
- 是否支持图片或文件输入；
- API Key 的计费和权限范围；
- 数据是否会发送到第三方服务；
- 是否设置了额度和费用提醒。

不要把 API Key 写进公开教程、截图、GitHub 仓库或聊天记录。

## 推荐决策顺序

1. 新手先使用自动模式；
2. 失败时先检查任务描述和文件，而不是立刻怪模型；
3. 根据失败类型切换到能力匹配的模型；
4. 用固定样例做小规模对比；
5. 对稳定重复任务再固定模型；
6. 模型列表变化后重新验证。

## 参考资料

- [模型配置](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Model)
- [新建任务栏与模型选择](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Task-Bar)

## 更新记录

- 2026-07-17：创建模型选择与小样本对比指南。