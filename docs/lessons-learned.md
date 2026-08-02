# Horizon 项目经验教训

## 2026-08-01：DeepSeek API 从 GitHub Actions 无法访问

**问题：** Horizon 日报部署到 GitHub Actions 后，AI 评分全部失败，报告为空。

**根因：**
1. GitHub Actions 服务器在美国，DeepSeek API 在中国，跨国直连被阻断
2. `deepseek-v4-pro` 不支持 OpenAI 的 `response_format: json_object` 参数
3. Horizon 的评分失败是静默降级的，不会报错中断

**解决：** 换用 GitHub Models 免费 API（详见 [配置文档](data/config.github.json)）

**教训：**
- 选 AI API 时考虑服务器地理位置
- 给自动化流程加"至少 1 条过线"的健康检查
- 调试时先加日志，不要靠猜