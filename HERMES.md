# Hermes 维护说明

本仓库已把后续内容维护设计成一套“先搜集、再整理、后写作、定期核对”的工作流。核心规则位于 [SKILL.md](SKILL.md)。

## 推荐安装结构

将以下文件同步到 Hermes 的 Skill 目录：

```text
~/.hermes/skills/workbuddy-guide-maintainer/
├── SKILL.md
├── config/
│   ├── quality-rules.yaml
│   └── maintenance.yaml
├── content/
│   └── coverage-matrix.yaml
├── sources/
│   ├── sources.yaml
│   └── community-tutorials.yaml
├── templates/
└── docs/standards/visual-tutorial-standard.md
```

不同 Hermes 版本的安装命令可能变化，请以本机 `hermes skills --help` 的实际输出为准。

## 最重要的执行原则

Hermes 不应直接凭模型记忆批量写教程。每次流程必须是：

```text
搜集现有资料
  ↓
更新来源库
  ↓
与覆盖矩阵和已有文章去重
  ↓
建立研究证据包
  ↓
设计配图
  ↓
生成 Draft PR
  ↓
人工审核和实测
```

## 推荐定时任务

详细配置见 [`config/maintenance.yaml`](config/maintenance.yaml)。

### 每周一：只做内容发现

```text
/workbuddy-guide-maintainer 执行每周内容发现：
1. 搜索过去 7 天 WorkBuddy 官方更新、公开教程和高频问题；
2. 更新 sources/community-tutorials.yaml；
3. 更新 content/coverage-matrix.yaml；
4. 输出来源、重复内容、内容缺口和 P0 候选报告；
5. 这次不要写文章，不要创建发布 PR。
```

### 每周三：最多生成 2 篇 Draft

```text
/workbuddy-guide-maintainer 从覆盖矩阵中选择最多 2 个 P0/P1 高价值主题。
必须先读取来源库、建立证据包和配图计划。
按图文教程标准生成 B 级草稿并创建 Draft PR。
不要自动合并，不要为了数量选择低价值主题。
```

### 每月 1 日：检查过期内容

```text
/workbuddy-guide-maintainer 执行月度过期检查：
核对官方文档、外链、界面、模型、Skill、连接器、权限和版本变化；
找出受影响教程并创建更新 PR；无法确认的标记为待验证或过期；
不要自动合并。
```

### 每季度：把重点教程升级为实测

```text
/workbuddy-guide-maintainer 从高流量和 P0 教程中选择最多 5 篇，
安排完整人工实测、脱敏截图、可复现样例和失败记录；
满足条件后从 B 级来源核对升级为 A 级已实测。
```

## 单个主题调用方式

```text
/workbuddy-guide-maintainer 研究“WorkBuddy 如何做竞品调研”：
先搜集官方和社区教程，更新来源库，建立证据包与 4 张配图计划，
生成 C 级草稿和 Draft PR，不要发布。
```

## 必须授予的能力

- 读取当前仓库；
- 访问公开网页和官方文档；
- 创建 Git 分支、提交和 Draft Pull Request；
- 运行 `python scripts/validate_content.py`；
- 运行 `python scripts/check_sources.py`；
- 生成原创 SVG 示意图；
- 在实测任务中保存脱敏截图。

不应授予：

- 自动合并；
- 删除仓库；
- 修改或读取生产密钥；
- 访问私人客户数据；
- 直接发送、公开发布、付款或修改重要账号权限。

## 内容数量上限

- 每周最多生成 2 篇新教程；
- 一个 PR 最多包含 2 篇教程；
- 没有 75 分以上选题时可以不写；
- 不允许为了“日更”制造重复或低质量文章；
- P0 教程没有配图计划时不得进入可合并状态。

## 人工审核清单

合并 PR 前确认：

- 是否先搜集并记录了现成教程；
- 是否至少有一个官方来源；
- 是否与已有教程重复；
- 是否补充了第三方教程缺少的步骤和风险；
- 是否存在虚构步骤、按钮、版本或效果；
- 是否准确标注“实测”“来源核对”或“自动草稿”；
- 是否泄露隐私、密钥或业务数据；
- 是否大段复刻第三方内容；
- 是否包含高风险操作的提醒和恢复方案；
- 是否有至少 2 张真正帮助理解的配图；
- 图片是否原创、授权清楚或来自本项目脱敏实测；
- 是否能解决一个清晰、真实的用户问题。

## GitHub 自动检查

仓库中的 GitHub Actions 会：

- 在每次提交和 PR 中检查教程结构、链接和明显敏感信息；
- 每周一自动检查来源链接；
- 明确返回 404/410 的来源会导致检查失败；
- 403、429 和超时只标记为需要人工复核。
