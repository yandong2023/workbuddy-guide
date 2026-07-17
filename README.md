# WorkBuddy 非官方中文使用手册

> 面向普通人的 WorkBuddy 教程、案例、Skills、提示词与问题解决库。

[![Content Check](https://github.com/yandong2023/workbuddy-guide/actions/workflows/content-check.yml/badge.svg)](https://github.com/yandong2023/workbuddy-guide/actions/workflows/content-check.yml)
[![License: MIT](https://img.shields.io/badge/code-MIT-blue.svg)](LICENSE)
[![Content: CC BY-NC-SA 4.0](https://img.shields.io/badge/content-CC%20BY--NC--SA%204.0-lightgrey.svg)](CONTENT_LICENSE.md)

本项目希望把分散在官方文档、社区文章、视频和真实使用案例中的信息，整理成普通人可以照着完成的中文教程。

**本项目为非官方社区项目，与 WorkBuddy、腾讯及其关联公司不存在隶属、合作或官方授权关系。** “WorkBuddy”等名称和商标归其权利人所有。

## 从这里开始

### 新手入门

- [WorkBuddy 是什么](docs/getting-started/what-is-workbuddy.md)
- [第一次任务怎么描述](docs/getting-started/first-task.md)
- [权限模式怎么选](docs/getting-started/permission-modes.md)

### 办公场景

- [用 WorkBuddy 分析 Excel：教程模板](docs/office/excel-analysis.md)
- [用 WorkBuddy 制作 PPT：教程模板](docs/office/create-ppt.md)

### 自动化与 Skills

- [自动化教程目录](docs/automation/README.md)
- [Skills 教程目录](docs/skills/README.md)
- [创建自己的 Skill](docs/skills/create-custom-skill.md)

### 常见问题

- [常见问题目录](docs/troubleshooting/README.md)
- [任务执行前总是询问权限怎么办](docs/troubleshooting/permission-prompts.md)

## 内容可信度

每篇教程都必须标注验证等级：

- **A：已实测**——在当前版本完整执行，并记录验证日期。
- **B：来源核对**——根据官方文档及可靠公开来源核对，但尚未完整实测。
- **C：自动草稿**——由自动化生成，仅保留在 PR 或 `drafts/`，不得直接发布。

项目不允许把“来源核对”写成“亲测有效”，也不允许模型虚构按钮、路径、版本、截图或执行结果。

## 自动化维护方式

后期由 Hermes 定期维护：

1. 发现官方更新、新教程和高频问题；
2. 与现有内容去重；
3. 建立来源证据包；
4. 生成 Markdown 草稿；
5. 执行格式、来源、链接和重复度检查；
6. 创建独立分支和 Pull Request；
7. **不得自动合并到 `main`**。

具体规则见 [SKILL.md](SKILL.md) 和 [HERMES.md](HERMES.md)。

## 参与贡献

欢迎提交：

- 新教程；
- 旧教程更新；
- 错误修复；
- 真实使用截图；
- 失败案例和解决方法；
- 新的可靠信息源。

请先阅读 [贡献指南](CONTRIBUTING.md)。教程正文应当是原创整理或在授权范围内使用，不得大段搬运第三方内容。

## 项目结构

```text
workbuddy-guide/
├── docs/                  # 已发布教程
├── drafts/                # 自动生成、待审核草稿
├── templates/             # 教程和证据包模板
├── sources/               # 信息源配置
├── config/                # 内容质量规则
├── scripts/               # 自动检查脚本
├── .github/               # Actions、Issue 和 PR 模板
├── SKILL.md               # Hermes/Agent 维护技能
└── HERMES.md              # Hermes 执行说明
```

## 许可证

- 代码、脚本和自动化配置：[MIT License](LICENSE)
- 教程、图片和其他内容：[CC BY-NC-SA 4.0](CONTENT_LICENSE.md)

## 安全红线

公开仓库禁止提交：

- `.env`、API Key、Token、Cookie、OAuth 凭据；
- 数据库地址、账号、密码和生产配置；
- 原始运行日志或完整个人画像；
- 客户姓名、身份信息、订单号和未脱敏业务数据；
- 未获授权的付费教程、视频字幕或大段转载内容。

发现泄露后应立即删除相关内容、清理 Git 历史，并轮换密钥。