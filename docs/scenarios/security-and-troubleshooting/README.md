# 安全、权限与故障解决

适合所有用户，尤其是处理正式资料、连接外部平台和运行自动化的人。

## 已发布

- ✅ [权限模式怎么选](../../getting-started/permission-modes.md)
- ✅ [总是询问权限怎么办](../../troubleshooting/permission-prompts.md)
- ✅ [无法读取文件](../../troubleshooting/cannot-read-files.md)
- ✅ [任务卡住或无响应](../../troubleshooting/task-stuck.md)
- ✅ [生成文件打不开](../../troubleshooting/generated-file-cannot-open.md)
- ✅ [更新后工作空间不见](../../troubleshooting/workspace-missing-after-update.md)
- ✅ [登录失败](../../troubleshooting/login-failed.md)

## P0：优先完善

| 主题 | 状态 | 重点内容 | 计划路径 |
|---|---|---|---|
| WorkBuddy 安全使用总指南 | ⚪ 待研究 | 数据去向、模型、Skill、连接器和权限 | `security-basics.md` |
| 敏感文件脱敏 | ⚪ 待研究 | 姓名、电话、账号、合同、日志 | `redact-sensitive-data.md` |
| 完全访问权限风险 | 🟡 已有基础内容 | 适用条件、隔离目录、备份、撤销 | `full-access-risks.md` |
| 第三方 Skill 安全检查 | 🟡 已有基础内容 | 作者、代码、联网、目录、密钥 | `skill-security-review.md` |
| 连接器授权和撤销 | 🔵 官方有指南 | 最小权限、账号、频道、删除授权 | `connector-permissions.md` |
| 文件误删、误移动和恢复 | 🔵 官方 FAQ 有相关问题 | 停止任务、回收站、映射表、备份 | `file-recovery.md` |
| 自动化重复执行/发送 | ⚪ 待研究 | 幂等、运行锁、历史记录、停用 | `duplicate-automation.md` |
| 积分/额度异常消耗 | 🔵 社区有大量讨论 | 模型、任务范围、循环、自动化 | `usage-consumption.md` |
| 模型不可用或输出不完整 | 🔵 官方 FAQ | 能力、上下文、拆分任务、换模型 | `model-errors.md` |
| 更新后功能或入口变化 | 🔵 官方更新日志 | 版本、截图、旧教程标记 | `version-changes.md` |

## P1：排障目录

- 安装包无法打开；
- Windows SmartScreen 或 macOS 安全提示；
- ARM64 兼容问题；
- 登录回调失败；
- 默认浏览器无法拉起；
- 工作目录没有权限；
- 找不到生成文件；
- 文件格式损坏；
- PDF/图片 OCR 失败；
- Excel 处理超时；
- 视频转写失败；
- Skill 安装后不生效；
- 连接器授权失败；
- 自动化没有触发；
- 消息发送到错误对象；
- 任务重复运行；
- 模型调用失败；
- 客户端崩溃和日志反馈。

## 安全教程的强制标准

1. 不指导用户关闭所有系统安全防护；
2. 不把“本地处理”表述为“完全离线”；
3. 不在示例中展示真实 Token、Cookie、账号和客户数据；
4. 涉及管理员命令时说明影响范围和恢复方式；
5. 恢复操作先保护现场，避免继续覆盖；
6. 连接器、Skill 和自定义模型都要说明数据可能流向哪里；
7. 对高风险操作提供更安全替代方案。

## 每篇教程需要的配图

- 权限边界图；
- 数据从本地文件到模型/Skill/连接器的路径图；
- 停止任务和恢复文件流程图；
- 常见错误的分层排查树；
- 自动化正常、失败、重复和停用状态图。
