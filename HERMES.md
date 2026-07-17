# Hermes 维护说明

本仓库已把后续内容维护设计成一个可由 Hermes 执行的工作流。核心规则位于 [SKILL.md](SKILL.md)。

## 推荐安装结构

将本仓库中的 `SKILL.md` 及其依赖文件放入 Hermes 的 Skill 目录，例如：

```text
~/.hermes/skills/workbuddy-guide-maintainer/
├── SKILL.md
├── config/quality-rules.yaml
├── sources/sources.yaml
└── templates/
```

不同 Hermes 版本的安装命令可能变化，请以本机 `hermes skills --help` 的实际输出为准。

## 推荐调用方式

```text
/workbuddy-guide-maintainer 执行本周维护：发现新内容、检查旧教程，并为通过质量门槛的内容创建 Draft PR。不要自动合并。
```

也可以执行单一任务：

```text
/workbuddy-guide-maintainer 研究“WorkBuddy 如何分析 Excel”，建立证据包并生成一篇 C 级草稿，不要发布。
```

## 必须授予的能力

- 读取当前仓库；
- 访问公开网页和官方文档；
- 创建 Git 分支、提交和 Pull Request；
- 运行 `python scripts/validate_content.py`。

不应授予自动合并、删除仓库、修改密钥、访问私人客户数据或直接公开发布内容的权限。

## 建议频率

- 每周一次完整扫描；
- 官方出现明显更新时额外执行一次；
- 用户提交 Issue 后按需研究；
- 不建议为了数量每日批量生成文章。

## 人工审核清单

合并 PR 前确认：

- 是否至少有一个官方来源；
- 是否与已有教程重复；
- 是否存在虚构步骤；
- 是否准确标注“实测”或“来源核对”；
- 是否泄露隐私或密钥；
- 是否大段复刻第三方内容；
- 是否包含高风险操作的提醒；
- 是否能解决一个清晰、真实的用户问题。
