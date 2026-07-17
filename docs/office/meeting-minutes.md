---
title: "用 WorkBuddy 整理会议纪要：结论、待办和责任人模板"
description: "把录音转写、聊天记录或零散笔记整理成可确认的会议纪要。"
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
  - https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/File-Recognition
  - https://www.workbuddy.ai/docs/workbuddy/Create-Task
---

# 用 WorkBuddy 整理会议纪要：结论、待办和责任人模板

> 验证状态：B 级来源核对。官方实践文档列出了会议纪要整理场景；本文模板尚未完成本项目的完整人工实测。

会议纪要不是简单缩写原文。真正有用的纪要应当把讨论、明确结论、待确认问题和行动项分开。

## 可以使用哪些输入

- 会议录音转写文本；
- 聊天记录；
- 手写笔记整理后的文本；
- 多个人分别记录的会议笔记；
- 会议材料和议程。

音频无法直接处理时，可以先通过你确认可信的转写方式得到文本，再让 WorkBuddy 整理。

## 可直接复制的任务描述

```text
请根据 input/meeting-notes.txt 整理正式会议纪要。

要求：
1. 提取会议主题、日期、参会角色和议程；
2. 按议题整理讨论要点；
3. 单独列出已经明确达成的结论；
4. 单独列出仍有争议或待确认的问题；
5. 将行动项整理成表格，字段包括：事项、负责人、截止时间、依赖、状态；
6. 原记录没有明确负责人或截止时间时写“待确认”，不要猜测；
7. 保留重要数字、日期和原话含义；
8. 不要修改原文件；
9. 输出 output/meeting-minutes.md；
10. 最后列出需要人工确认的项目。
```

## 多份记录如何合并

```text
请合并 input/ 中的三份会议记录。

规则：
- 相同内容合并；
- 不同记录互相冲突时并列展示并标记来源文件；
- 不要自行选择其中一个版本作为事实；
- 输出冲突清单和缺失信息清单。
```

## 推荐输出结构

```text
会议基本信息
会议目标
议题一：讨论与结论
议题二：讨论与结论
行动项表格
待确认事项
风险与依赖
附件与参考资料
```

## 重点检查

- 是否把某个人的建议误写成全体结论；
- 是否给未明确的任务编造负责人；
- 是否漏掉截止时间和依赖；
- 是否误写姓名、项目名和金额；
- 是否删除了重要的反对意见；
- 行动项是否足够具体，可以执行。

## 会后跟进模板

确认纪要后，可以继续让 WorkBuddy生成一份待办清单，但不要直接发送：

```text
请根据已确认的会议纪要生成跟进清单。
按负责人分组，并标记本周、下周和长期事项。
只生成草稿，不要向任何人发送。
```

## 隐私提醒

会议记录可能包含员工、客户、商业计划和未公开决策。处理前应遵守公司的会议录音、数据存储和第三方模型使用规定。公开截图时必须脱敏。

## 参考资料

- [实践一：文件内容识别与处理](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Practice-Cases/File-Recognition)
- [Create Task](https://www.workbuddy.ai/docs/workbuddy/Create-Task)

## 更新记录

- 2026-07-17：创建会议纪要、行动项和冲突信息模板。