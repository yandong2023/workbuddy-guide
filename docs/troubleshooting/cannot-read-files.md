---
title: "WorkBuddy 无法读取 PDF、Excel、Word 或图片怎么办"
description: "按文件、模型、Skill、工作目录和权限逐步排查文件读取失败。"
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
  - https://www.workbuddy.ai/docs/workbuddy/Create-Task
---

# WorkBuddy 无法读取 PDF、Excel、Word 或图片怎么办

> 验证状态：B 级来源核对。本文依据官方中文 FAQ 和创建任务文档整理，尚未完成本项目的完整人工实测。

文件读取失败不一定是文件损坏，也可能是模型不支持、缺少 Skill、工作目录不正确或任务描述没有引用目标文件。

## 先确认现象

区分以下情况：

- 完全找不到文件；
- 能看到文件名，但无法读取内容；
- 只能读取文字，无法识别图片或表格；
- 读取到一部分后报错；
- 文件可以读取，但输出乱码；
- 文件被读取，却没有生成结果。

把完整错误提示保存下来，不要只描述“不能用”。

## 第一步：检查文件本身

- 用原生软件确认文件能打开；
- 检查文件大小是否为 0；
- 确认扩展名和真实格式一致；
- 检查是否加密或需要密码；
- 把文件名改成简短英文或中文，避免特殊字符；
- 复制一份小文件进行测试。

## 第二步：确认工作目录和引用

官方创建任务文档支持选择目录、`@` 引用、拖入文件和上传文件。建议明确点名：

```text
请读取当前工作目录中的 input/report.pdf。
先告诉我文件页数和是否可以识别文字、表格和图片。
暂时不要生成摘要。
```

如果文件不在当前目录，先复制到测试工作目录，而不是直接开放整个电脑访问权限。

## 第三步：检查模型能力

官方 FAQ 提到，当前模型可能不支持对应文件类型。可以：

1. 切换到支持文档或图片输入的模型；
2. 只测试一页 PDF 或一张图片；
3. 把复杂任务拆成“读取测试”和“正式处理”两步；
4. 记录换模型前后的结果。

模型列表和能力可能变化，以客户端当前标记为准。

## 第四步：检查 Skill

某些文档处理任务需要对应 Skill。检查：

- 是否安装了文档处理类 Skill；
- Skill 是否启用；
- 是否更新后失效；
- 是否要求额外程序或第三方服务；
- 当前任务是否选择了正确 Skill。

先用无敏感信息的样例测试，不要直接在正式文件上排查。

## 第五步：缩小任务

错误示例：

```text
把这个文件夹里的所有文件整理、总结、翻译并做成 PPT。
```

改为：

```text
第一步只读取 input/sample.pdf，并回答：
1. 是否能识别文字；
2. 是否能识别表格；
3. 是否能识别图片；
4. 哪些页无法读取。
不要修改或生成其他文件。
```

## 仍无法解决时收集信息

- 操作系统和版本；
- WorkBuddy 版本；
- 文件类型和大小；
- 使用的模型；
- 使用的 Skill；
- 工作目录；
- 完整错误文本；
- 是否所有文件都失败；
- 是否在更新后出现。

不要公开上传原始敏感文件。必要时制作可以复现问题的脱敏样例。

## 参考资料

- [WorkBuddy 中文常见问题](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/FQA)
- [Create Task](https://www.workbuddy.ai/docs/workbuddy/Create-Task)

## 更新记录

- 2026-07-17：创建文件、模型、Skill 和工作目录分层排查流程。