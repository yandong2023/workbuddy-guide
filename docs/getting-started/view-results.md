---
title: "WorkBuddy 任务完成后怎么看结果：产物、文件和变更检查"
description: "说明如何检查右侧结果区、实际文件、修改范围和交付质量。"
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
  - https://www.workbuddy.ai/docs/workbuddy/Quickstart
  - https://www.workbuddy.ai/docs/workbuddy/Create-Task
  - https://www.workbuddy.ai/docs/zh/
---

# WorkBuddy 任务完成后怎么看结果：产物、文件和变更检查

> 验证状态：B 级来源核对。本文依据官方快速开始、创建任务和文档导航整理，尚未完成本项目的完整人工实测。结果区名称和布局可能随版本变化。

WorkBuddy 回复“已完成”不等于任务真的完成。你还需要检查产物是否生成、文件能否打开、内容是否正确，以及是否修改了不该修改的文件。

## 先看右侧结果区

官方快速开始说明，右侧结果面板通常会展示：

- 生成的产物；
- 当前任务涉及的全部文件；
- 文件变更；
- 可以预览的结果。

如果右侧面板没有展开，可以查看任务标题栏附近是否有结果或面板入口。

## 再到实际目录检查

不要只看预览。打开 Finder 或文件资源管理器，确认：

1. 文件确实存在；
2. 保存位置符合要求；
3. 扩展名正确；
4. 文件大小不是 0；
5. 能用目标软件正常打开；
6. 原始文件没有被覆盖。

## 检查内容是否可验收

不同产物的最低检查标准：

### Word 或 Markdown

- 标题和章节是否完整；
- 是否遗漏关键输入；
- 是否把推测写成事实；
- 引用和数字能否追溯；
- 是否出现重复段落或占位符。

### Excel

- 工作表名称是否合理；
- 公式是否正确；
- 数字、日期和百分比格式是否正确；
- 汇总结果能否抽样复算；
- 原始数据是否被意外删除。

### PPT

- 页面数量和结构是否符合要求；
- 数字和结论是否来自资料；
- 文本是否溢出；
- 图表单位和时间范围是否明确；
- 内容是否仍可编辑。

### 批量文件任务

- 文件数量是否一致；
- 是否有漏处理或重复处理；
- 新旧文件名映射是否保存；
- 是否出现文件丢失或扩展名错误。

## 让 WorkBuddy 自己输出交付清单

任务结束前补充：

```text
请输出一份交付清单，包含：
1. 读取的文件；
2. 新建的文件；
3. 修改的文件；
4. 删除或移动的文件；
5. 每个结果文件的完整路径；
6. 尚未完成或需要人工确认的事项。
```

这不能代替人工检查，但能降低遗漏概率。

## 发现结果不对怎么办

不要立刻从头重跑。先在同一任务中指出具体差异：

```text
结果需要修改：
1. 第 3 页的数据与 sales.xlsx 不一致；
2. 不要使用推测原因；
3. 图表需要显示单位；
4. 请只修改 output/report.pptx；
5. 修改后再次列出变更文件。
```

## 高风险任务必须额外检查

涉及发送、发布、覆盖、删除、支付或账号修改时，在执行最终动作前进行人工确认。预览正确不代表发送对象、公开范围和权限一定正确。

## 参考资料

- [WorkBuddy Quick Start](https://www.workbuddy.ai/docs/workbuddy/Quickstart)
- [Create Task](https://www.workbuddy.ai/docs/workbuddy/Create-Task)
- [WorkBuddy 中文文档导航](https://www.workbuddy.ai/docs/zh/)

## 更新记录

- 2026-07-17：创建结果、文件和变更检查指南。