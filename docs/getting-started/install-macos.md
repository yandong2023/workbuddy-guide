---
title: "macOS 安装 WorkBuddy：芯片版本、系统权限与登录"
description: "介绍 Mac 版 WorkBuddy 的版本选择、安装步骤、首次权限和安全测试方法。"
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
  - https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Installation-Mac-Guide
  - https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/Installation-Mac-Guide
---

# macOS 安装 WorkBuddy：芯片版本、系统权限与登录

> 验证状态：B 级来源核对。本文依据官方中英文安装指南整理，尚未完成本项目的完整人工实测。登录方式和安装包名称可能随地区及版本变化。

## 安装前检查

官方文档要求 macOS 12 Monterey 或更高版本。下载前先确认 Mac 芯片类型：

1. 点击左上角苹果菜单；
2. 选择“关于本机”；
3. 查看“芯片”或“处理器”；
4. M1、M2、M3、M4 等选择 ARM64 版本；
5. Intel 处理器选择 X64 版本。

不要只根据购买年份猜芯片类型。

## 下载和安装

1. 从 WorkBuddy 官方网站进入下载页面；
2. 选择与芯片匹配的 macOS 安装包；
3. 下载并打开 `.dmg` 文件；
4. 将 WorkBuddy 图标拖入 `Applications` 文件夹；
5. 等待复制完成后推出安装磁盘；
6. 从“应用程序”或启动台打开 WorkBuddy。

## 首次打开时的安全提示

macOS 可能要求确认应用来源。处理前先确认安装包来自官方页面。官方英文指南提到，如果系统拒绝打开，可以前往：

```text
系统设置 → 隐私与安全性
```

查看对应提示并决定是否允许打开。来源不确定时不要点击“仍要打开”。

## 系统权限怎么给

根据使用功能，WorkBuddy 可能请求：

- 文件与文件夹访问；
- 通知权限；
- 辅助功能或自动化相关权限。

不要一开始全部开放。推荐按任务逐项授权：

1. 只处理文件时，先授权一个测试目录；
2. 只需要任务完成提醒时，再开放通知；
3. 只有明确使用远程控制等能力时，才考虑辅助功能权限；
4. 任务完成后检查系统设置中的授权范围。

## 登录方式为什么和别人的截图不一样

官方中文和英文安装文档展示的登录方式并不完全相同，可能与地区、账号体系和版本有关。应以当前客户端实际显示的登录入口为准。

安全原则：

- 只在官方客户端拉起的官方页面完成授权；
- 不把浏览器回调链接、Cookie 或 Token 发给他人；
- 授权失败时先检查默认浏览器和网络；
- 不通过陌生人提供的脚本修改登录文件。

## 第一次任务建议

建立一个单独测试目录，放入两三个无敏感信息的文件副本，然后输入：

```text
请只读取当前工作目录，列出所有文件的名称、格式和修改日期。
不要移动、重命名、删除或覆盖文件。
请把结果保存成 inventory.md。
```

完成后检查右侧结果、文件列表和实际 Finder 目录是否一致。

## 更新 WorkBuddy 前

重要文件不应只保存在应用安装目录或临时工作区。升级前建议：

- 把正式交付文件复制到独立业务目录；
- 备份仍需保留的工作空间；
- 关闭正在运行的任务；
- 更新后先用测试目录确认文件读取正常。

## 参考资料

- [Mac 系统安装指南](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Installation-Mac-Guide)
- [Mac Installation Guide](https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/Installation-Mac-Guide)

## 更新记录

- 2026-07-17：创建 macOS 安装、芯片选择和首次权限指南。