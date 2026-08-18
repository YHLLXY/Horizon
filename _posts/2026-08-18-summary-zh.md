---
layout: default
title: "Horizon Summary: 2026-08-18 (ZH)"
date: 2026-08-18
lang: zh
---

> 从 52 条内容中筛选出 10 条重要资讯。

---

1. [Linux 7.3 提升 vRAM 管理性能](#item-1) ⭐️ 9.0/10
2. [Einride 新增 500 辆 Tesla Semi 卡车](#item-2) ⭐️ 9.0/10
3. [亚马逊推荐算法的隐形税](#item-3) ⭐️ 8.0/10
4. [Mojo 1.0 开源发布](#item-4) ⭐️ 8.0/10
5. [修复被砖化的 AMD 7040 Framework 13 笔记本](#item-5) ⭐️ 8.0/10
6. [司法部调查 Andreessen Horowitz 的董事会席位冲突](#item-6) ⭐️ 8.0/10
7. [苹果将欧盟 App Store 费用降至 5%并放宽替代商店规则](#item-7) ⭐️ 8.0/10
8. [TikTok explores peer-to-peer payments via DMs, report says](#item-8) ⭐️ 7.0/10
9. [OpenAI institutes new safeguards after Hugging Face breach](#item-9) ⭐️ 7.0/10
10. [OpenAI president urges enterprises to hasten AI security defences](#item-10) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Linux 7.3 提升 vRAM 管理性能](https://pixelcluster.dev/VRAM-Overcommit/) ⭐️ 9.0/10

Linux 7.3 内核新增多项虚拟 GPU 内存优化，降低页面错误并提升低 VRAM 时的分配速度。 改进的 VRAM 管理可提升游戏、渲染和机器学习工作负载的图形性能，并减少因内存耗尽导致的崩溃。 这些改动主要针对 DRM 内存分配器，加入更智能的页面错误处理和新的碎片整理提示，但仍需 GPU 驱动支持虚拟内存；Nvidia 驱动目前缺乏分页支持。

hackernews · flaburgan · 8月18日 07:51 · [社区讨论](https://news.ycombinator.com/item?id=49342719)

**背景**: 虚拟 GPU 内存允许 GPU 访问超过实际物理内存的地址空间，通过在系统 RAM 中分页来实现。Linux DRM 子系统通过内存分配器跟踪 VRAM 使用并与 MMU 交互来管理这一过程。高效的分配对高端图形工作负载至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.kernel.org/gpu/drm-mm.html">DRM Memory Management — The Linux Kernel documentation</a></li>
<li><a href="https://developer.nvidia.com/blog/introducing-low-level-gpu-virtual-memory-management/">Introducing Low-Level GPU Virtual Memory Management | NVIDIA Technical Blog</a></li>

</ul>
</details>

**社区讨论**: 社区成员对新内核能防止 RAM 用尽导致的冻结表示乐观，并赞扬性能提升。有人指出 Nvidia 驱动仍缺乏分页支持，限制了收益，亦有人关注碎片整理与驱动协作。

**标签**: `#Linux Kernel`, `#GPU Memory Management`, `#Performance`, `#Systems`, `#Hardware Acceleration`

---

<a id="item-2"></a>
## [Einride 新增 500 辆 Tesla Semi 卡车](https://techcrunch.com/2026/08/18/einride-strikes-deal-to-add-500-tesla-semis-to-its-fleet/) ⭐️ 9.0/10

Einride 已与 Tesla 签订协议，采购 500 辆 Tesla Semi 电动卡车，使其车队规模翻三倍。此举将提升其 Saga AI 自动驾驶平台在北美的吸引力。 此合作加速了电动自动化货运的部署，可能降低货运商的排放和运营成本。它也使 Einride 成为电动物流市场的主要参与者。 Tesla Semi 具备 500 英里续航、主动安全系统和宽敞驾驶舱，Saga AI 则整合车辆遥测、路线规划和充电管理。车队扩张将依赖 Tesla 现有生产能力和 Einride 基于云的控制层。

rss · TechCrunch · 8月18日 10:30

**背景**: Tesla Semi 是一款全电动半挂卡车，提供 500 英里续航和主动安全功能。它采用大型电池组和宽敞驾驶舱以提升可视性。Einride 的 Saga AI 是一个智能操作系统，连接自动驾驶卡车、电动车和充电站。该平台利用云计算和机器学习来优化路线规划和车队管理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tesla.com/semi">Semi – Electric Semi Truck | Tesla</a></li>
<li><a href="https://www.einride.tech/saga-ai">Saga AI | Einride</a></li>

</ul>
</details>

**标签**: `#autonomous trucking`, `#electric vehicles`, `#Tesla`, `#logistics`, `#AI software`

---

<a id="item-3"></a>
## [亚马逊推荐算法的隐形税](https://seths.blog/2026/08/the-amazon-tax/) ⭐️ 8.0/10

塞思·戈丁于 2026 年 8 月发表的博客文章批评亚马逊的推荐和搜索机制，将其视为一种让消费者承担的“税”，促使购物者购买平台想要卖出的商品。该文章在 Hacker News 上引发了大量讨论，获得 772 分和 476 条评论。 该分析揭示了推荐系统如何影响消费者行为和市场结果，引发了关于平台权力、消费者自主权和市场公平性的关注。它与电子商务、人工智能伦理和平台设计讨论尤为相关。 文章聚焦亚马逊的 item‑to‑item 协同过滤和搜索排名，优先考虑销量和赞助内容，实际上对消费者构成了隐形税。它并未提出技术解决方案，而是呼吁关注此类算法的伦理影响。

hackernews · herbertl · 8月18日 13:22 · [社区讨论](https://news.ycombinator.com/item?id=49345263)

**背景**: 推荐系统利用用户过去的交互来建议新商品。亚马逊的核心引擎依赖于 item‑to‑item 协同过滤，它通过匹配用户购买的商品与其他购物者的行为来寻找相似商品。亚马逊 Personalize 是一项托管服务，允许开发者使用类似技术构建自己的推荐模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.amazon.science/the-history-of-amazons-recommendation-algorithm">The history of Amazon&#x27;s recommendation algorithm - Amazon Science</a></li>
<li><a href="https://aws.amazon.com/personalize/">Recommender System – Amazon Personalize – Amazon Web Services</a></li>
<li><a href="https://en.wikipedia.org/wiki/Collaborative_filtering">Collaborative filtering - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认为亚马逊的搜索偏向销量和赞助结果，许多人觉得平台把他们推向自己想卖的商品，而非他们真正需要的。有人转向本地商店或其他在线平台，理由是质量下降和想避免隐形税。讨论还指出广告占据搜索结果主导地位，难以找到真正的优惠。

**标签**: `#e-commerce`, `#recommendation systems`, `#consumer behavior`, `#Amazon`, `#platform design`

---

<a id="item-4"></a>
## [Mojo 1.0 开源发布](https://simonwillison.net/2026/Aug/18/mojo-is-now-open-source/) ⭐️ 8.0/10

Mojo 1.0 已经开源，编译器和工具链现在以 Apache 2 许可证提供。 这使得 Mojo 的高性能、面向 AI 的语言向更广泛的社区开放，可能影响 AI/ML 和系统编程领域的语言设计与工具链。 该发布遵循 Modular 的早期承诺，并标志着从 Python 超集向使用 MLIR 优化 GPU 编程的独立语言的转变。

rss · Simon Willison · 8月18日 21:39

**背景**: Mojo 是 Modular Inc. 开发的系统编程语言。最初它被设想为 Python 的超集，但后来演变为自己的语言。Mojo 使用 MLIR 而非 LLVM，使其能够高效地针对 CPU、GPU、TPU 等加速器。该语言旨在以类似 Python 的语法提供高性能 AI 基础设施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mojo_%28programming_language%29">Mojo (programming language)</a></li>
<li><a href="https://mojolang.org/">Mojo</a></li>

</ul>
</details>

**社区讨论**: 该公告在 Lobste.rs 上分享，用户对开源发布及其对 AI 开发的潜在影响表示兴奋。

**标签**: `#Mojo`, `#open source`, `#programming languages`, `#AI/ML`, `#software engineering`

---

<a id="item-5"></a>
## [修复被砖化的 AMD 7040 Framework 13 笔记本](https://quantum5.ca/2026/08/16/fixing-bricked-amd-7040-series-framework-13-laptop-with-20-tools/) ⭐️ 8.0/10

本文详细列出了使用 20 种工具逐步修复被砖化的 AMD 7040 Framework 13 笔记本的方法，包括 BIOS 重新刷写、硬件检查和固件恢复。 该指南使用户和工程师能够拯救本来会成为电子废物的设备，凸显现代笔记本可靠固件和可维修性的意义。 恢复过程需要使用如 pogo‑pin 适配器、JTAG 调试器和 AMDVBFlash 工具等专业设备，并假设用户可以获取原始 BIOS 镜像和备用电源。

hackernews · jp\_sc · 8月18日 13:18 · [社区讨论](https://news.ycombinator.com/item?id=49345220)

**背景**: AMD Ryzen 7040 系列采用 4 nm 工艺的 Zen 4 Phoenix 架构，提供高性能和功耗效率。Framework 的 Laptop 13 是一款模块化、易于维修的设备，配备可通过 AMDVBFlash 等工具更新的 BIOS 固件。刷写失败会导致系统砖化，恢复通常需要低级刷写或硬件调试。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.amd.com/en/partner/articles/ryzen-pro-7040-series-processors.html">AMD Ryzen™ PRO 7040 Series Processors</a></li>
<li><a href="https://resources.frame.work/downloads/laptop-13/">Framework Laptop 13 — BIOS &amp; Drivers | Resources</a></li>
<li><a href="https://www.techpowerup.com/download/ati-atiflash/">AMDVBFlash / ATI ATIFlash 5.0.874 Download | TechPowerUp</a></li>

</ul>
</details>

**社区讨论**: 社区成员对制造商责任表示沮丧，指出固件缺陷会导致笔记本无法使用，并可能使保修失效。有人强调不同品牌 BIOS 砖化的普遍性以及缺乏透明的维修途径。还有人讨论法律责任，建议将受损消费者诉诸小额索赔法院。

**标签**: `#BIOS`, `#firmware`, `#hardware recovery`, `#embedded systems`, `#AMD`

---

<a id="item-6"></a>
## [司法部调查 Andreessen Horowitz 的董事会席位冲突](https://techcrunch.com/2026/08/18/dojs-probe-into-andreessen-horowitz-over-board-seats-baffles-vcs/) ⭐️ 8.0/10

美国司法部已对 Andreessen Horowitz 开始调查，重点关注该公司在其投资组合公司中的董事会席位安排所产生的利益冲突。 此调查表明监管机构正加强对风险投资实践的审查，可能改变 VC 公司管理董事会代表和利益冲突的方式。 调查聚焦 Andreessen Horowitz 的董事会席位策略是否违反反垄断或证券法规，但目前尚未提出指控。

rss · TechCrunch · 8月18日 20:36

**背景**: Andreessen Horowitz 是由 Marc Andreessen 和 Ben Horowitz 创立的硅谷最大、最具影响力的风险投资公司之一。风险投资公司通常会在其投资组合公司中占据董事会席位，以影响战略并保护投资。 但当公司在竞争业务中持有重叠董事会席位时，可能产生利益冲突。

**标签**: `#VC`, `#DOJ`, `#investigation`, `#board seats`, `#industry impact`

---

<a id="item-7"></a>
## [苹果将欧盟 App Store 费用降至 5%并放宽替代商店规则](https://techcrunch.com/2026/08/18/apple-overhauls-its-eu-app-store-fees-loosens-rules-for-alternative-app-stores/) ⭐️ 8.0/10

苹果已将欧盟 App Store 的按安装计费模式改为外部分发的应用统一 5%佣金，并放宽了此前限制开发者运营替代应用商店或网页分发的规则。 此举降低了希望通过替代渠道接触欧盟用户的开发者成本，可能刺激竞争并影响未来对苹果生态系统的反垄断审查。 5%费率仅适用于在苹果官方 App Store 之外分发的应用，App Store 内销售的应用仍保留 15%/30%的标准佣金；开发者还需在 12 个月内保持一致的支付选项以维护用户体验。

rss · TechCrunch · 8月18日 17:12

**背景**: 苹果的 App Store 历来对销售收取 15%佣金，对大型或订阅类应用收取 30%佣金。在欧盟，数字市场法（DMA）迫使苹果允许替代支付方式和应用分发渠道。新的费率模型取代了此前对欧盟分发应用的按安装计费模式，简化了定价结构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://9to5mac.com/2026/08/18/apple-overhauls-app-store-fees-in-the-eu-with-new-unified-terms/">Apple overhauls App Store fees in the EU with new unified... - 9to5Mac</a></li>
<li><a href="https://artikls.com/article/apple-overhauls-eu-app-store-fees-alternative-marketplaces">Apple Overhauls EU App Store Fees to Ease Payments Dispute | Artikls</a></li>
<li><a href="https://techcrunch.com/2026/02/22/move-over-apple-meet-the-alternative-app-stores-available-in-the-eu-and-elsewhere/">Move over, Apple: Meet the alternative app stores available in the EU and elsewhere | TechCrunch</a></li>
<li><a href="https://www.macrumors.com/2026/08/18/eu-app-store-fee-change/">Apple Overhauls EU App Store Fees to Settle Digital Markets Act Dispute - MacRumors</a></li>

</ul>
</details>

**社区讨论**: 开发者普遍欢迎更低的费用和更大的灵活性，但也有人担心 12 个月支付一致性要求。监管机构将此举视为符合 DMA 的步骤，行业分析师则警告这可能无法完全解决竞争问题。

**标签**: `#Apple`, `#App Store`, `#EU regulations`, `#developer policy`, `#competition`

---

<a id="item-8"></a>
## [TikTok explores peer-to-peer payments via DMs, report says](https://techcrunch.com/2026/08/18/tiktok-explores-peer-to-peer-payments-via-dms-report-says/) ⭐️ 7.0/10

TikTok is investigating the possibility of enabling peer‑to‑peer payments through direct messages using its existing TikTok Pay system.

rss · TechCrunch · 8月18日 20:03

**标签**: `#TikTok`, `#payments`, `#peer-to-peer`, `#social media`, `#fintech`

---

<a id="item-9"></a>
## [OpenAI institutes new safeguards after Hugging Face breach](https://techcrunch.com/2026/08/18/openai-institutes-new-safeguards-after-hugging-face-breach/) ⭐️ 7.0/10

OpenAI announced new monitoring and alignment safeguards in response to a Hugging Face data breach.

rss · TechCrunch · 8月18日 18:00

**标签**: `#AI Security`, `#Model Safeguards`, `#OpenAI`, `#Data Breach`, `#Alignment`

---

<a id="item-10"></a>
## [OpenAI president urges enterprises to hasten AI security defences](https://www.artificialintelligence-news.com/news/openai-president-urges-enterprises-hasten-ai-security-defences/) ⭐️ 7.0/10

OpenAI president Greg Brockman urges enterprises to speed up AI security defenses amid a compressed timeline, citing the OpenAI‑Hugging Face incident as a catalyst.

rss · AI News · 8月18日 14:58

**标签**: `#AI security`, `#enterprise security`, `#OpenAI`, `#cybersecurity`, `#AI governance`

---