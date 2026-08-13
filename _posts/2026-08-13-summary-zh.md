---
layout: default
title: "Horizon Summary: 2026-08-13 (ZH)"
date: 2026-08-13
lang: zh
---

> 从 53 条内容中筛选出 10 条重要资讯。

---

1. [Gemini 3.7 Flash 发布 新视觉功能与优惠定价](#item-1) ⭐️ 9.0/10
2. [Cerebras 加速 GPT‑5.6 Sol Ultrafast](#item-2) ⭐️ 9.0/10
3. [IBM 与 OpenAI 合作培训数千名顾问](#item-3) ⭐️ 9.0/10
4. [X 开源排名算法，新增阴影封禁透明度](#item-4) ⭐️ 9.0/10
5. [美国允许私营公司进行网络攻击](#item-5) ⭐️ 9.0/10
6. [把 DRAM 变成意大利面](#item-6) ⭐️ 8.0/10
7. [HN Digest 2026-08-12 · Tailscale 追踪到 SQLite 16 年前的 Bug](#item-7) ⭐️ 8.0/10
8. [If Apple sends you a push notification alerting you to a spyware attack, take it seriously](#item-8) ⭐️ 8.0/10
9. [DeepSeek V4 Pro 0813 \(on OpenRouter\)](#item-9) ⭐️ 7.0/10
10. [Databricks wanted to raise $1B, investors wanted $15B. It settled on $5B at a $190B valuation.](#item-10) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Gemini 3.7 Flash 发布 新视觉功能与优惠定价](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/) ⭐️ 9.0/10

Google 发布了 Gemini 3.7 Flash，这是一款多模态 LLM，提升了视觉性能，并在 2026 年 12 月 31 日之前以每百万输入令牌 0.75 美元、每百万输出令牌 3.75 美元的优惠价格提供。 该模型通过更强的图像理解能力扩展了 Google 的 LLM 组合，支持更丰富的多模态应用，并且低价促销降低了大规模文本和视觉工作负载的成本。 Gemini 3.7 Flash 保留了前代模型的 100 万令牌上下文窗口，采用 3 代理图循环加速训练，并保持与 Gemini 3.6 Flash 相当的安全性和语调指标。

hackernews · thisisauserid · 8月13日 17:23 · [社区讨论](https://news.ycombinator.com/item?id=49289112)

**背景**: Gemini 是 Google 的旗舰大型语言模型系列，基于 Transformer 架构，支持文本、图像和代码。3.x 系列侧重于高性能多模态推理和代理功能，每一次迭代都提升了安全性和指令遵循能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/models/gemini/flash/">Gemini 3.7 Flash — Google DeepMind</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/models/gemini-3.7-flash">Gemini 3.7 Flash | Gemini API | Google AI for Developers</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/latest-model">What&#x27;s new in Gemini 3.7 Flash | Gemini API | Google AI for Developers</a></li>

</ul>
</details>

**社区讨论**: 社区成员赞赏 Gemini 3.7 Flash 的视觉性能和低成本，但有人担心 2027 年的价格大幅上涨，并质疑其与 Luna 等竞争对手相比的价值。还有人指出该模型的 100 万令牌上下文和代理功能使其在大规模文本任务中具有吸引力。

**标签**: `#AI`, `#Gemini`, `#Google`, `#LLM`, `#Vision`

---

<a id="item-2"></a>
## [Cerebras 加速 GPT‑5.6 Sol Ultrafast](https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai) ⭐️ 9.0/10

Cerebras 与 OpenAI 公布了 GPT‑5.6 Sol Ultrafast，一种新的推理模式，据称在 2,500 题目基准测试中比以往 Sol 版本快 7 倍，完成时间为 11 小时 11 分钟，而 Claude Fable 5 则需 78 小时。 速度提升使 AI 工作流几乎实时化，帮助开发者更快迭代并提升生成内容质量，同时降低大规模部署的运营成本和能耗。 Ultrafast 运行在 Cerebras 的晶圆级引擎上，声称最高可达 14 倍速度提升，但基准测试显示 7 倍改进；准确性似乎与标准 Sol 相当，但 OpenAI 尚未公布定价或详细性能指标。

hackernews · pr337h4m · 8月13日 18:10 · [社区讨论](https://news.ycombinator.com/item?id=49289844)

**背景**: GPT‑5.6 是 OpenAI 最新的大型语言模型，Sol 是其最强大变体。Cerebras 的晶圆级引擎是一块集成计算、内存和互连的单片晶圆处理器，能够为 AI 工作负载提供高吞吐量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai">Accelerating GPT-5.6 Sol Ultrafast with OpenAI</a></li>
<li><a href="https://techcrunch.com/2026/08/13/openai-introduces-ultrafast-a-new-mode-that-makes-gpt-5-6-sol-work-at-14x-the-speed/">OpenAI introduces &#x27; Ultrafast ,&#x27; a new mode that makes GPT-5.6 Sol ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cerebras">Cerebras - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区成员对速度提升表示兴奋，但对声称的性能和缺乏定价细节持怀疑态度。有人质疑 Ultrafast 是否与标准 Sol 的准确性相当，并指出基准测试可能不反映真实工作负载。

**标签**: `#OpenAI`, `#Cerebras`, `#GPT-5.6`, `#LLM performance`, `#AI acceleration`

---

<a id="item-3"></a>
## [IBM 与 OpenAI 合作培训数千名顾问](https://techcrunch.com/2026/08/13/ibm-partners-with-openai-to-bolster-enterprise-ai-push/) ⭐️ 9.0/10

IBM 宣布与 OpenAI 合作，培训并认证数万名顾问掌握 OpenAI 技术，包括 GPT‑4 与 ChatGPT Enterprise，以将先进 AI 融入其企业服务。 此举表明 IBM 正在转向以 AI 为核心的咨询服务，并将 OpenAI 模型推向庞大的全球客户群，可能加速各行业的 AI 采用。 该合作基于 IBM 与大型系统集成商的现有合作，培训计划将涵盖模型微调、安全最佳实践和企业部署场景。

rss · TechCrunch · 8月13日 19:19

**背景**: IBM 过去与 Infosys、Tata Consultancy Services 等 IT 服务公司合作，将 AI 解决方案推向企业。OpenAI 的 ChatGPT Enterprise 与 GPT‑4 提供企业级安全、更快访问和定制功能，适合大规模部署。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/08/13/ibm-partners-with-openai-to-bolster-enterprise-ai-push/">IBM partners with OpenAI to bolster enterprise AI push | TechCrunch</a></li>
<li><a href="https://openai.com/index/introducing-chatgpt-enterprise/">Introducing ChatGPT Enterprise - OpenAI</a></li>
<li><a href="https://blockchaindesk.co/ibm-openai-enterprise-ai-partnership/">IBM and OpenAI partner to accelerate enterprise ... - Blockchain Desk</a></li>

</ul>
</details>

**标签**: `#IBM`, `#OpenAI`, `#enterprise AI`, `#partnership`, `#AI training`

---

<a id="item-4"></a>
## [X 开源排名算法，新增阴影封禁透明度](https://techcrunch.com/2026/08/13/x-open-sources-its-ranking-algorithm-letting-users-see-if-theyve-been-shadowbanned/) ⭐️ 9.0/10

X 已将其“为你”推荐算法开源，并推出工具，让用户查看自己是否被阴影封禁。新仓库包含 Heavy Ranker 神经网络和候选帖子选择逻辑。 开源透明度可能改变平台的内容审核方式，让用户了解算法决策，减少阴影封禁的不可见性。它还可能促使其他社交媒体采取类似的问责机制。 该算法每个会话大约拉取 1,500 条候选帖子，使用 Heavy Ranker 评分并为“为你”推荐排序；新工具公开单个帖子和账户的排名影响。

rss · TechCrunch · 8月13日 16:00

**背景**: X 的“为你”推荐是大多数用户的默认算法化推送，基于名为 Heavy Ranker 的神经网络模型评估互动、时效和用户兴趣等信号。平台过去将其排名逻辑保密，导致对阴影封禁的批评。通过开源代码，X 试图阐明帖子如何被展示以及如何执行审核决策。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://adlibrary.com/guides/x-twitter-algorithm-explained">X (Twitter) Algorithm Explained 2026: How For You Ranks Posts</a></li>
<li><a href="https://petdesk.com/blog/avoid-being-shadowbanned-on-social-media">How To Avoid Being Shadowbanned On Social Media | PetDesk</a></li>

</ul>
</details>

**标签**: `#social media`, `#algorithm transparency`, `#open source`, `#X \(Twitter\)`, `#shadowbanning`

---

<a id="item-5"></a>
## [美国允许私营公司进行网络攻击](https://techcrunch.com/2026/08/13/in-a-first-us-will-allow-some-private-firms-to-carry-out-cyberattacks/) ⭐️ 9.0/10

美国政府发布行政命令，允许特定私营公司开展进攻性网络行动，结束了数十年来禁止 hack‑back 活动的政策。 此举可能重塑国家安全战略，将网络防御委托给商业实体，并引发关于责任和升级的法律与伦理问题。 该命令仅适用于国防部审查的公司，并要求严格监管，但批评者警告此举可能模糊国家与非国家网络战主体的界限。

rss · TechCrunch · 8月13日 14:09

**背景**: 多年来，美国政策禁止私营实体进行进攻性网络行动，源于对升级、归因和国际法的担忧。&\#x27;hack back&\#x27; 概念——受害者对攻击者进行报复——一直存在争议，关于其合法性和有效性的讨论不断。近期关于网络主权和科技公司在国防中日益重要的辩论为此政策转变奠定了基础。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Hacking_back">Hacking back</a></li>
<li><a href="https://www.csis.org/analysis/offensive-cyber-capabilities-operational-level">Offensive Cyber Capabilities at the Operational Level</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#policy`, `#hackback`, `#cyber warfare`, `#US government`

---

<a id="item-6"></a>
## [把 DRAM 变成意大利面](https://github.com/xoreaxeaxeax/skitter-creek-bath-salts) ⭐️ 8.0/10

GitHub 项目展示了一种新的 DRAM 攻击，能够将权限提升到完全系统控制，引发安全专家热烈讨论。

hackernews · matt\_d · 8月13日 14:17 · [社区讨论](https://news.ycombinator.com/item?id=49286341)

**标签**: `#hardware security`, `#DRAM`, `#memory attack`, `#exploit`, `#hardware backdoor`

---

<a id="item-7"></a>
## [HN Digest 2026-08-12 · Tailscale 追踪到 SQLite 16 年前的 Bug](https://zeli.app/zh/digest/2026-08-12) ⭐️ 8.0/10

A digest featuring Tailscale’s discovery of a 16‑year‑old SQLite bug and DeepSeek’s launch of a 1M‑token context LLM via OpenRouter.

rss · Zeli · 8月12日 23:59

**标签**: `#SQLite`, `#Tailscale`, `#DeepSeek`, `#LLM`, `#Database`

---

<a id="item-8"></a>
## [If Apple sends you a push notification alerting you to a spyware attack, take it seriously](https://techcrunch.com/2026/08/13/if-apple-sends-you-a-push-notification-alerting-you-to-a-spyware-attack-take-it-seriously/) ⭐️ 8.0/10

Apple now notifies iPhone users via lock‑screen push notifications when it detects government spyware targeting their devices.

rss · TechCrunch · 8月13日 21:50

**标签**: `#Apple`, `#Security`, `#Spyware`, `#Privacy`, `#Government Surveillance`

---

<a id="item-9"></a>
## [DeepSeek V4 Pro 0813 \(on OpenRouter\)](https://simonwillison.net/2026/Aug/12/deepseek-v4-pro-0813/) ⭐️ 7.0/10

DeepSeek V4 Pro 0813, a 1.7T‑parameter LLM, is now available via OpenRouter and its weights have been released on Hugging Face.

rss · Simon Willison · 8月12日 23:59

**标签**: `#DeepSeek`, `#LLM`, `#OpenRouter`, `#Hugging Face`, `#Model Release`

---

<a id="item-10"></a>
## [Databricks wanted to raise $1B, investors wanted $15B. It settled on $5B at a $190B valuation.](https://techcrunch.com/2026/08/13/databricks-wanted-to-raise-1b-investors-wanted-15b-it-settled-on-5b-at-a-190b-valuation/) ⭐️ 7.0/10

Databricks secured a $5B funding round, valuing the company at $190B after investors pushed the valuation higher than initially sought.

rss · TechCrunch · 8月13日 20:14

**标签**: `#Databricks`, `#Funding`, `#AI`, `#Data Engineering`, `#Investment`

---