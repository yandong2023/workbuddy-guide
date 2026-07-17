---
title: "WorkBuddy 任务一直执行、卡住或无响应怎么办"
description: "区分正常长任务与异常卡住，并按停止、拆分、换模型和反馈逐步处理。"
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
  - https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/FQA
---

# WorkBuddy 任务一直执行、卡住或无响应怎么办

> 验证状态：B 级来源核对。本文依据官方中英文 FAQ 整理，尚未完成本项目的完整人工实测。

复杂任务运行较久不一定代表故障。先判断它是否仍在产生进度、文件或新的执行步骤，再决定是否停止。

## 先区分“慢”和“卡住”

可能仍在正常执行：

- 对话区持续出现新步骤；
- 结果目录中持续生成文件；
- 当前正在处理较大的 PDF、视频或表格；
- 网络速度较慢，但没有错误提示。

更像异常卡住：

- 很长时间没有任何新输出；
- 同一步骤反复重试；
- 任务一直提示正在执行，但文件没有变化；
- 已出现超时、网络或模型错误；
- 客户端明显无响应。

## 第一步：不要连续重复点击

重复发送相同任务可能创建多个并行执行，增加资源占用和文件冲突。先确认左侧任务列表中是否已经存在重复任务。

## 第二步：停止当前任务

官方 FAQ 建议任务卡住时点击停止按钮中断。停止后先检查：

- 已经生成了哪些文件；
- 是否存在半成品；
- 原文件是否被修改；
- 当前执行到哪一步；
- 是否出现临时脚本或锁文件。

不要在未知状态下立刻重新执行覆盖同一输出文件。

## 第三步：把任务拆小

原任务：

```text
分析 30 个文件，生成报告、图表和 PPT，然后发送给项目组。
```

拆成：

1. 只检查文件列表；
2. 只读取三份样例；
3. 生成分析计划；
4. 分批处理文件；
5. 汇总结果；
6. 生成 PPT；
7. 人工确认后再发送。

每一步都能单独检查，也更容易定位失败原因。

## 第四步：换模型前先记录

官方 FAQ 建议尝试切换模型。切换前记录：

- 当前模型；
- 卡住的具体步骤；
- 已运行时间；
- 输入文件大小；
- 错误提示；
- 已生成文件。

换模型后使用相同的小任务测试，不要立刻重跑全部流程。

## 第五步：检查网络和文件

- 网络是否稳定；
- 是否正在使用 VPN 或代理；
- 文件是否过大；
- 是否有损坏或加密文件；
- 是否需要下载额外组件；
- 第三方 API 是否超时；
- 磁盘空间是否充足。

## 重新执行模板

```text
刚才的任务在【具体步骤】停止。

这次只执行以下范围：
1. 读取 input/sample.xlsx；
2. 列出字段和前 20 行；
3. 不生成图表；
4. 不调用外部服务；
5. 不修改原文件；
6. 如果 5 分钟内无法完成，请停止并报告当前步骤和错误。
```

## 如何提交反馈

官方 FAQ 提供了客户端反馈和日志入口。提交前准备：

- WorkBuddy 版本；
- 系统版本；
- 模型和 Skill；
- 可复现的脱敏样例；
- 完整任务描述；
- 错误发生时间；
- 日志和截图。

日志可能包含对话、设备和路径信息，上传或公开前应确认隐私范围。

## 参考资料

- [WorkBuddy 中文常见问题](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/FQA)
- [WorkBuddy FAQ](https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/FQA)

## 更新记录

- 2026-07-17：创建任务卡住的停止、检查、拆分和反馈流程。