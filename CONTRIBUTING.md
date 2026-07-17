# 贡献指南

感谢你帮助完善 WorkBuddy 非官方中文使用手册。

第一次参与、不熟悉 GitHub 或不会写代码，可以先看：[第一次贡献指南](docs/contributing/README.md)。提交纠错、来源、实测结果和脱敏截图，都属于有价值的贡献。

## 可以贡献什么

- 新手教程、办公案例、岗位工作流、自动化和 Skill 教程；
- 已有教程的版本更新；
- 错别字、失效链接、错误步骤和安全风险修复；
- 真实执行结果、失败原因和脱敏截图；
- 原创 SVG 流程图；
- 可靠来源和用户高频问题；
- `content/coverage-matrix.yaml` 中的内容缺口。

## 提交前要求

1. **先搜集现成资料**：至少检查官方文档、已有仓库教程和社区来源库；
2. 优先使用官方文档和官方更新作为产品事实来源；
3. 第三方内容只能用于研究、交叉核对和发现缺口，不得大段复制或近似改写；
4. 不得把“来源核对”描述为“已实测”；
5. 不得虚构按钮、路径、版本、截图、积分消耗或执行结果；
6. 每篇非目录教程必须使用 `templates/tutorial-template.md` 的元数据结构；
7. 每篇 B 级教程至少提供一个官方来源，并明确说明尚未完成本项目完整实测；
8. A 级教程必须写明 `verified_at`、测试平台、WorkBuddy 版本和可复现样例；
9. 涉及删除、覆盖、发送、支付、账号、隐私或完全访问权限时，必须加入风险和恢复方法；
10. 面向普通用户的 P0 教程至少提供 2 张真正有帮助的图；
11. 自动生成内容只能通过 Draft PR 提交，不能直接推送到 `main`；
12. 新教程必须更新或核对 `content/coverage-matrix.yaml` 的状态。

## 写作前需要阅读

- [全场景教程目录](docs/scenarios/README.md)
- [图文教程标准](docs/standards/visual-tutorial-standard.md)
- [教程覆盖矩阵](content/coverage-matrix.yaml)
- [官方和社区来源库](sources/community-tutorials.yaml)
- [教程模板](templates/tutorial-template.md)
- [研究证据包模板](templates/research-pack-template.yaml)

## 验证等级

- `tested`：A 级，完整人工实测；
- `source-verified`：B 级，可靠来源核对；
- `automated-draft`：C 级，自动草稿，只能位于 `drafts/` 或 Draft PR 中。

## 推荐流程

1. 从覆盖矩阵选择清晰主题；
2. 搜集官方与社区教程；
3. 与现有文章和历史 PR 去重；
4. 创建 `drafts/research-packs/<slug>.yaml`；
5. 写清楚来源差异、内容缺口和待验证步骤；
6. 制定配图计划；
7. 编写或修改教程；
8. 添加原创 SVG 或脱敏截图；
9. 运行 `python scripts/validate_content.py`；
10. 运行 `python scripts/check_sources.py`；
11. 创建 Draft Pull Request；
12. 完成人工审核和必要实测后再合并。

## 截图规范

- 仅使用本项目实际操作时拍摄、官方允许使用或明确授权的截图；
- 不得制作虚假的 WorkBuddy 界面；
- 隐去姓名、邮箱、Token、二维码、真实用户名、客户信息和业务数据；
- 图片放在 `assets/screenshots/<文章 slug>/`；
- 文件名使用两位序号、小写英文和连字符，例如 `01-select-folder.png`；
- 教程中说明截图平台、日期和 WorkBuddy 版本；
- 旧版本截图必须明确标注，不得误导为当前界面。

## SVG 示意图规范

- 无法获得可靠界面截图时，优先使用原创 SVG；
- 文件放在 `assets/illustrations/<文章 slug>/`；
- 不依赖外部字体、脚本和远程图片；
- 中文文字清晰，GitHub 页面可直接查看；
- 每张图只解释一个主要难点；
- 不使用第三方教程中的独特图片布局进行复刻。

## Pull Request 说明

PR 中应列出：

- 解决的用户问题；
- 使用过的官方和社区来源；
- 与现有教程相比新增了什么；
- 验证等级；
- 配图清单；
- 尚未实测或存在冲突的步骤；
- 隐私、权限和版权风险；
- 内容检查结果。

## 公共仓库安全红线

严禁提交密钥、Cookie、授权回调链接、完整个人画像、客户身份、订单号、生产数据库信息、原始日志和未脱敏文件。发现泄露后应立即删除相关内容、清理 Git 历史并轮换密钥。
