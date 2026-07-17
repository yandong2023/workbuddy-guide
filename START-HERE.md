# 5 分钟开始使用 WorkBuddy

这是一条给第一次使用 WorkBuddy 的最短路线。不要先研究所有模型、Skill 和高级功能，先安全地跑通一个小任务。

## 第一步：准备一个测试目录

新建一个文件夹：

```text
workbuddy-first-task/
├── input/
├── output/
└── notes.md
```

把一份**无敏感信息的文件副本**放进 `input/`。不要使用唯一一份原文件，也不要把整个桌面、下载目录或公司共享盘作为第一次任务的工作目录。

## 第二步：选择合适的模式

第一次任务建议选择 **Plan**：先查看 WorkBuddy 打算做什么，再决定是否执行。

- 只是提问、了解文件：Ask
- 任务复杂或可能修改文件：Plan
- 计划已经确认，需要生成结果：Craft

详细说明见：[Ask、Plan、Craft 怎么选](docs/getting-started/work-modes.md)。

## 第三步：复制这段安全指令

```text
请只处理当前工作目录。

第一步先检查 input/ 中的文件，告诉我：
1. 有哪些文件；
2. 每个文件是什么格式；
3. 你是否可以正常读取；
4. 你准备如何处理；
5. 会生成哪些结果文件。

现在只输出计划，不要修改、移动、重命名、覆盖或删除任何文件。
不要访问当前工作目录之外的位置。
涉及联网、安装工具、运行脚本或发送内容时先询问我。
```

确认计划没有问题后，再补充：

```text
按刚才确认的计划执行。
所有结果保存到 output/，不要修改 input/ 中的原文件副本。
完成后列出所有读取、新建、修改、移动和删除的文件。
```

## 第四步：检查结果

不要只看对话中的“已完成”。打开实际文件夹，确认：

- `input/` 中的文件没有变化；
- `output/` 中存在预期结果；
- 文件可以正常打开；
- 数字、页码、时间戳或来源能够抽查；
- WorkBuddy 的变更列表和磁盘实际情况一致。

详细清单见：[任务完成后怎么看结果](docs/getting-started/view-results.md)。

## 第五步：从真实工作场景继续

### 文档与文件

- [总结 PDF](docs/office/summarize-pdf.md)
- [对比多份 Word/PDF](docs/scenarios/documents-and-files/compare-documents.md)
- [处理本地电脑大文件](docs/office/process-large-local-files.md)

### 数据和报表

- [分析 Excel](docs/office/excel-analysis.md)
- [合并多份 Excel](docs/scenarios/data-and-reporting/merge-excel-files.md)

### 调研和产品

- [竞品调研](docs/scenarios/research-and-analysis/competitor-research.md)
- [用户反馈转产品需求](docs/scenarios/product-and-design/feedback-to-requirements.md)

### 内容和运营

- [公众号文章生产](docs/scenarios/marketing-and-content/wechat-article.md)
- [创建每日资讯简报](docs/automation/daily-briefing.md)

## 三条必须记住的边界

1. **本地文件不等于完全离线。** 模型、Skill 或连接器可能调用网络服务。
2. **未经确认不自动发送和发布。** 邮件、公众号、群聊和公开内容先生成草稿。
3. **高风险决定由人完成。** 合同、付款、招聘、客户承诺和产品排期不能由 AI 最终决定。

项目的完整场景地图见：[WorkBuddy 全场景教程目录](docs/scenarios/README.md)。

这份手册对你有帮助时，欢迎在仓库右上角点一个 **Star**，也欢迎提交纠错、实测结果和新教程需求。
