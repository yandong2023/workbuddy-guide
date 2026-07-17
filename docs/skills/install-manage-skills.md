---
title: "WorkBuddy Skill 怎么安装、更新和卸载"
description: "介绍技能市场的使用方法、安装前检查、测试流程和权限风险。"
category: skills
difficulty: beginner
created_at: 2026-07-17
updated_at: 2026-07-17
verified_at: null
verification: source-verified
status: published
tested_platform: null
workbuddy_version: null
sources:
  - https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market
  - https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Task-Bar
---

# WorkBuddy Skill 怎么安装、更新和卸载

> 验证状态：B 级来源核对。本文依据官方 Skill Marketplace 和任务栏说明整理，尚未完成本项目的完整人工实测。技能名称、作者和可用列表会持续变化。

Skill 用于扩展 WorkBuddy 的能力，例如网页搜索、文档处理、日历、网盘、语音转文字或特定文件操作。

## 从技能市场安装

官方技能市场文档给出的基本流程是：

1. 从侧边栏打开 Skill Marketplace；
2. 按分类浏览或搜索关键词；
3. 打开技能详情；
4. 查看描述、版本和作者；
5. 点击安装；
6. 安装后在任务中启用或选择该技能。

入口名称可能随版本和语言变化，以客户端实际界面为准。

## 安装前不要只看名称

至少检查：

- 作者是谁；
- 是否为官方技能；
- 最近更新时间；
- 需要访问哪些文件；
- 是否访问网络；
- 是否要求第三方 API Key；
- 是否会运行脚本或外部程序；
- 是否有卸载方式；
- 是否能在测试目录运行。

官方文档说明安装前会进行安全扫描，但自动扫描不能替代用户审查和隔离测试。

## 第一次测试一个 Skill

建立测试目录，放入无敏感信息的样例文件，然后输入：

```text
请使用已安装的【Skill 名称】处理当前测试目录。

限制：
1. 只读取当前目录；
2. 不访问其他文件夹；
3. 不删除、覆盖或移动原文件；
4. 不向外部发送数据；
5. 先说明将调用哪些能力；
6. 结果保存到 output/；
7. 完成后列出所有文件变更和网络访问。
```

## Skill 安装后怎么用

官方任务栏文档说明，可以在对话框中选择已安装技能，WorkBuddy 执行任务时会调用相关能力。

任务中仍应明确：

- 为什么需要这个 Skill；
- 输入是什么；
- 输出是什么；
- 哪些操作禁止；
- 成功标准是什么。

不要只写“使用最合适的 Skill 自动完成一切”。

## 更新 Skill

更新前建议记录当前版本和现有任务是否正常。更新后用同一份样例重新测试：

- 触发方式是否变化；
- 输出格式是否变化；
- 新增了哪些权限；
- 是否访问新的网络服务；
- 旧工作流是否仍能执行。

关键工作流不要在正式运行前自动批量更新所有 Skill。

## 暂时禁用还是卸载

- 近期可能继续使用，但不希望自动调用：先禁用；
- 不再使用、来源不可信或权限过大：卸载；
- 卸载后检查是否遗留配置、缓存或 API Key；
- 第三方服务中的授权可能需要到服务端单独撤销。

## 需要 API Key 的 Skill

API Key 应存放在官方推荐的安全配置位置，不要：

- 写进任务提示词；
- 写入 `SKILL.md`；
- 提交到 GitHub；
- 放进截图；
- 发到群聊；
- 直接写在脚本示例中。

同时设置最小权限、费用上限和轮换计划。

## 发现异常怎么办

如果 Skill 出现异常文件修改、未知联网、重复发送或权限请求：

1. 立即停止任务；
2. 禁用该 Skill；
3. 检查文件变更和回收站；
4. 撤销相关第三方授权；
5. 轮换可能泄露的密钥；
6. 保存脱敏后的错误信息；
7. 向官方或作者反馈。

## 参考资料

- [Skill Marketplace](https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market)
- [新建任务栏与 Skills](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Task-Bar)

## 更新记录

- 2026-07-17：创建 Skill 安装、测试、更新、禁用和卸载指南。