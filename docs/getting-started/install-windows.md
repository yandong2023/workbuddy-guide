---
title: "Windows 安装 WorkBuddy：下载、登录与首次启动"
description: "介绍 Windows 版 WorkBuddy 的系统要求、安装流程、登录方式和首次启动检查。"
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
  - https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/Installation-Win-Guide
  - https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/FQA
---

# Windows 安装 WorkBuddy：下载、登录与首次启动

> 验证状态：B 级来源核对。本文依据官方安装指南和 FAQ 整理，尚未完成本项目的完整人工实测。不同版本、地区和设备架构的实际界面可能不同。

## 安装前先检查

官方英文安装指南列出的基础要求包括：

- Windows 10 1809 或更高版本，或 Windows 11；
- 64 位操作系统；
- 至少 4 GB 内存，建议 8 GB；
- 至少 500 MB 可用磁盘空间；
- 可以正常访问模型服务的网络环境。

### 关于 ARM64 的特别提醒

官方英文安装页列出了 ARM64 安装包，但中文 FAQ 同时记录了 Windows 11 ARM64 无法安装的已知情况。两处信息目前存在差异，因此 ARM64 用户应以当前官方下载页、安装包说明和客户端实际结果为准，不要仅根据旧教程判断兼容性。

## 下载和安装

1. 从 WorkBuddy 官方网站进入下载页；
2. 根据电脑架构选择 Windows 安装包；
3. 下载完成后双击 `.exe` 文件；
4. 按安装向导完成安装；
5. 安装完成后启动 WorkBuddy。

不要从不明网盘、群文件或第三方下载站安装所谓“绿色版”或“破解版”。

## 如果被 Windows 安全提示拦截

官方安装指南提到，Windows Defender SmartScreen 可能显示安全提醒。此时先确认：

- 安装包确实来自官方页面；
- 文件名和下载时间与刚才操作一致；
- 没有经过他人重新打包。

确认来源后，再根据系统提示继续。来源无法确认时不要绕过安全提示。

## 登录

官方不同语言页面展示的登录方式可能不同。启动后，请按当前客户端实际提供的方式登录，例如浏览器授权、扫码或第三方账号授权。

如果点击登录无反应，官方 FAQ 建议优先检查：

1. 是否设置了可用的默认浏览器；
2. 浏览器是否成功打开授权页面；
3. 安全软件是否拦截客户端或浏览器跳转；
4. 当前 Windows 用户是否拥有应用数据目录权限。

不要在非官方页面输入账号密码、验证码或授权 Token。

## 第一次启动建议

首次进入后不要直接把整个桌面或资料盘交给 WorkBuddy。建议：

1. 创建一个测试文件夹，例如 `WorkBuddy测试`；
2. 放入几份无敏感信息的副本；
3. 保持默认权限；
4. 先执行只读任务；
5. 确认输出目录和文件变更记录后，再处理真实资料。

## 一个安全的首次任务

```text
请只读取当前工作目录中的文件，列出文件名、类型和大小。
不要修改、删除、移动或重命名任何文件。
请把结果保存为 file-list.md，并告诉我保存位置。
```

## 安装或启动失败时记录什么

提交反馈前建议记录：

- Windows 版本和系统架构；
- WorkBuddy 版本；
- 安装包来源；
- 错误提示完整文本；
- 是否被安全软件拦截；
- 首次启动还是升级后出现；
- 已尝试的处理方法。

截图前应隐藏用户名、文件路径中的个人信息和授权页面内容。

## 参考资料

- [Windows Installation Guide](https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/Installation-Win-Guide)
- [WorkBuddy 中文常见问题](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/FQA)

## 更新记录

- 2026-07-17：创建 Windows 安装与首次启动指南，并标注 ARM64 官方信息差异。