---
layout: default
title: "Horizon Summary: 2026-08-14 (ZH)"
date: 2026-08-14
lang: zh
---

> 从 51 条内容中筛选出 10 条重要资讯。

---

1. [AI 人体组织实验有望取代动物测试](#item-1) ⭐️ 9.0/10
2. [谷歌实现同态加密在私有 AI 中的实用化](#item-2) ⭐️ 9.0/10
3. [苹果拟对外部链接购买收取 15%佣金](#item-3) ⭐️ 9.0/10
4. [Qwen 3.8 27B 发布 – 新推理能力](#item-4) ⭐️ 8.0/10
5. [HN 摘要 2026-08-13 · Gemini 3.7 Flash：原生多模态推理新迭代](#item-5) ⭐️ 8.0/10
6. [优步与 Pony.ai 计划在欧洲投放 2000 辆机器人出租车](#item-6) ⭐️ 8.0/10
7. [加州批准 Aurora 与 Kodiak 货运卡车测试许可](#item-7) ⭐️ 7.0/10
8. [What we know about the alleged Iranian hacks on US water utilities](#item-8) ⭐️ 7.0/10
9. [Does Mark Zuckerberg really believe AI is ‘for everyone’?](#item-9) ⭐️ 7.0/10
10. [Samsung health AI models analyse wearable biosignal data](#item-10) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [AI 人体组织实验有望取代动物测试](https://www.fastcompany.com/91589344/the-worlds-largest-biological-datacenter-could-help-make-animal-testing-obsolete) ⭐️ 9.0/10

Vivodyne 的 AI 驱动平台已在旧金山运营 12 台机器人“蜂巢”实验室，年可测试超过 300 万个人体组织样本，容量是美国所有临床试验总和的两倍。 由于 90% 的药物在动物测试后仍失败，规模化的人体组织测试方法可显著提升安全性预测，减少对动物模型的依赖，加速药物研发。 该系统采用全自动机器人和 AI 设计实验来控制变量，但目前主要针对体外类器官，并未完全取代所有体内验证步骤。

telegram · zaihuapd · 8月14日 01:48

**背景**: 传统药物研发高度依赖动物测试来评估疗效和毒性，但许多化合物在后期人类试验中失败。组织工程的进步使科学家能够培养类似真实组织的类器官，AI 可优化实验设计并解释复杂数据。Vivodyne 将这些技术结合，创建了一个高通量平台，可直接在人体组织上测试药物。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.vivodyne.com/">Vivodyne | Make biology computable</a></li>
<li><a href="https://www.genengnews.com/topics/artificial-intelligence/vivodynes-lab-grown-human-tissue-platform-gets-real-with-38-million-seed-financing/">Vivodyne&#x27;s Lab Grown Human Tissue Platform Gets Real with $38 Million Seed Financing</a></li>
<li><a href="https://www.vivodyne.com/platform">Vivodyne - Our Platform</a></li>

</ul>
</details>

**标签**: `#AI`, `#drug testing`, `#tissue engineering`, `#animal testing`, `#biomedical research`

---

<a id="item-2"></a>
## [谷歌实现同态加密在私有 AI 中的实用化](https://blog.google/security/how-google-is-making-private-ai-practical-with-homomorphic-encryption/) ⭐️ 9.0/10

谷歌宣布已将同态加密的计算开销降低到足以实现私有 AI 推理的程度，并在 Gemma4 模型上演示了该技术，使得在不泄露输入或输出的情况下可对加密数据进行推理。 这一突破使组织能够在云端运行敏感 AI 工作负载，同时保持数据加密，解决隐私和合规性问题，并可能降低昂贵硬件隔离的需求，使隐私保护 AI 更易获取。 该优化利用专门的算术库和批处理技术，将开销从约 1000 倍降低到仅几十倍相较于明文推理。然而，该方法仍需细致的密钥管理，并且可能尚未支持所有模型架构。

hackernews · u1hcw9nx · 8月14日 15:43 · [社区讨论](https://news.ycombinator.com/item?id=49300314)

**背景**: 同态加密允许在密文上进行计算，产生的密文结果解密后与在明文上计算得到的结果相同。长期以来，它被认为过于缓慢，尤其是对大型神经网络而言。谷歌最近的工作表明，通过算法和硬件优化，开销可以降低到足以满足实际推理工作负载。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Homomorphic_encryption">Homomorphic encryption</a></li>
<li><a href="https://www.splunk.com/en_us/blog/learn/homomorphic-encryption.html">Homomorphic Encryption: How It Works | Splunk</a></li>

</ul>
</details>

**社区讨论**: 用户对所声称的性能提升持怀疑态度，指出同态加密仍然存在高开销，可能不具备商业可行性。有人认为私有 AI 可以在本地实现而不依赖云端，另一些人则质疑谷歌的隐私声明，因其过去产品存在缺陷。

**标签**: `#homomorphic encryption`, `#privacy‑preserving AI`, `#Google`, `#machine learning security`, `#AI privacy`

---

<a id="item-3"></a>
## [苹果拟对外部链接购买收取 15%佣金](https://techcrunch.com/2026/08/14/apple-proposes-to-take-a-15-cut-of-purchases-made-outside-the-app-store/) ⭐️ 9.0/10

苹果已向联邦法官提请允许其对通过 iOS 应用内嵌外部链接完成的购买收取最高 15% 的佣金。此举将把现有 App Store 费用结构扩展到在应用内发起但在 App Store 之外完成的交易。 若获批准，开发者将为通过外部链接完成的任何内购支付更高费用，可能改变其盈利模式并促使更多使用替代支付方式。此举还可能加剧对苹果在 iOS 生态系统中控制力的反垄断审查。 该佣金仅适用于通过深链接或通用链接打开第三方站点后发起的交易，而不适用于直接在 App Store 内完成的购买。苹果认为此费用有助于维持 iOS 平台的安全与隐私保障。

rss · TechCrunch · 8月14日 14:54

**背景**: 通用链接是 iOS 的一项功能，允许 URL 直接打开已安装的应用，否则回退到网页。深链接则进一步把用户定向到应用内的特定内容或页面。苹果传统上对 App Store 内的销售收取 15% 或 30% 的佣金，但此前并未对离开 App Store 生态系统的购买收取费用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.apple.com/documentation/xcode/supporting-universal-links-in-your-app">Supporting universal links in your app | Apple Developer Documentation</a></li>
<li><a href="https://orufy.com/blog/webtonative/deep-linking-in-ios">Deep Linking in iOS —A Complete Guide of 2026</a></li>

</ul>
</details>

**标签**: `#Apple`, `#App Store`, `#commissions`, `#app development`, `#antitrust`

---

<a id="item-4"></a>
## [Qwen 3.8 27B 发布 – 新推理能力](https://huggingface.co/Qwen/Qwen3.8-27B-FP8) ⭐️ 8.0/10

阿里巴巴 Qwen 团队在 Hugging Face 上发布了 27 B 参数的 Qwen 3.8 模型，采用稠密 27 B 架构并配备视觉编码器，原生上下文窗口为 262,144 令牌，并通过 RoPE 扩展至 1M 令牌。发布后在 Hacker News 上引发热烈讨论，用户将其显式推理能力与 Opus、Gemma 4、Claude 等模型进行对比。 该模型表明 27 B 参数的 LLM 能在保持竞争性推理分数的同时，在消费级硬件上部署，满足社区对高效本地推理的需求。其与更大或更昂贵模型的表现对比，凸显了 LLM 生态向实用高质量推理的转变。 Qwen 3.8 拥有 27 B 参数，隐藏维度 5120，采用 FP8 量化以提升推理效率，完整精度下大约需要 32 GB VRAM。虽然在某些推理基准上优于 Opus，但其 VRAM 使用高于 Gemma 4，并且采用稠密架构而非混合专家设计。

hackernews · erdaltoprak · 8月14日 15:00 · [社区讨论](https://news.ycombinator.com/item?id=49299605)

**背景**: 大型语言模型（LLM）通过参数规模和训练数据提升性能，但实际部署往往取决于模型大小和推理效率。推理基准（如数学或逻辑问题集）评估模型执行多步推理的能力，而非仅生成流畅文本。多模态扩展（如视觉编码器）使 LLM 能同时处理图像和文本，扩大应用范围。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-27B">Qwen / Qwen 3 . 8 -27B · Hugging Face</a></li>
<li><a href="https://benchlm.ai/models/qwen3-8-27b">Qwen 3 . 8 -27B Benchmarks &amp; Context (August 2026) | BenchLM.ai</a></li>
<li><a href="https://lmstudio.ai/models/qwen3.8">Qwen 3 . 8</a></li>

</ul>
</details>

**社区讨论**: 社区成员赞扬 Qwen 3.8 的显式推理和本地性能，指出其在某些任务上优于 Opus，同时运行成本更低。有人将其与 Gemma 4 对比，指出 VRAM 需求更高但推理步骤更清晰。总体情绪积极，呼吁推出更大或 MoE 版本以进一步突破。

**标签**: `#Large Language Models`, `#Qwen`, `#Model Release`, `#AI Research`, `#Hugging Face`

---

<a id="item-5"></a>
## [HN 摘要 2026-08-13 · Gemini 3.7 Flash：原生多模态推理新迭代](https://zeli.app/zh/digest/2026-08-13) ⭐️ 8.0/10

一份 Hacker News 摘要，概述了 Gemini 3.7 Flash（一个多模态 LLM）和 DeepSeek Harness（一个开源代理框架）的发布，两者都引发了社区的热烈讨论。

rss · Zeli · 8月13日 23:59

**标签**: `#AI`, `#LLM`, `#multimodal`, `#agent framework`, `#open-source`

---

<a id="item-6"></a>
## [优步与 Pony.ai 计划在欧洲投放 2000 辆机器人出租车](https://techcrunch.com/2026/08/14/uber-and-pony-ai-plan-to-bring-2000-robotaxis-to-europe/) ⭐️ 8.0/10

优步与自动驾驶初创公司 Pony.ai 宣布，将在五个欧洲城市投放 2000 辆机器人出租车，扩展至原先在克罗地亚萨格勒布的市场之外。 此举标志着欧洲自动驾驶出行服务的显著扩张，可能重塑城市交通，给传统出租车行业带来竞争，并加速自驾技术的普及。 该合作伙伴计划投放 2000 辆机器人出租车，但文章未说明具体车型、软件版本或各城市所需的监管批准。

rss · TechCrunch · 8月14日 10:44

**背景**: 机器人出租车是无需人工驾驶员即可提供按需乘车服务的自动驾驶车辆，通常由 Uber、Waymo 或 Pony.ai 等公司运营。将其投放到城市需要满足当地安全法规、测试协议和基础设施支持。Uber 此前已在克罗地亚萨格勒布测试机器人出租车，现在正向其他欧洲市场扩张。

**标签**: `#autonomous vehicles`, `#robotaxi`, `#Uber`, `#Pony.ai`, `#Europe`

---

<a id="item-7"></a>
## [加州批准 Aurora 与 Kodiak 货运卡车测试许可](https://techcrunch.com/2026/08/14/self-driving-trucks-are-officially-testing-on-california-highways/) ⭐️ 7.0/10

加州机动车辆管理局已向 Aurora Innovation 和 Kodiak AI 颁发正式测试许可，使其自动驾驶卡车能够在州高速公路上进行安全驾驶员和无人驾驶测试。 这一监管里程碑表明自动化货运正迈向商业化部署，可能缓解劳动力短缺并提升美国卡车行业的物流效率。 两家公司均将在加州 Level 4 自动化框架下运营；Aurora 的卡车已在营收生成的货运中运行，而 Kodiak 的平台则专为与现有车队集成而设计。

rss · TechCrunch · 8月14日 20:37

**背景**: 自动驾驶卡车利用传感器、人工智能和地图实现无人工输入的导航。加州长期以来一直是自动驾驶车辆的试验场，提供安全驾驶员或无人驾驶类别及运营限制的许可。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.dmv.ca.gov/portal/vehicle-industry-services/autonomous-vehicles/autonomous-vehicle-testing-permit-holders/">Autonomous Vehicle Permit Holders - California DMV - California ...</a></li>
<li><a href="https://aurora.tech/">aurora . tech</a></li>
<li><a href="https://kodiak.ai/?gad=1">Kodiak AI | Autonomous Trucking &amp; AI -Powered Ground Autonomy ...</a></li>

</ul>
</details>

**标签**: `#autonomous vehicles`, `#self‑driving trucks`, `#California`, `#AI`, `#industry regulation`

---

<a id="item-8"></a>
## [What we know about the alleged Iranian hacks on US water utilities](https://techcrunch.com/2026/08/14/what-we-know-about-the-alleged-iranian-hacks-on-u-s-water-utilities/) ⭐️ 7.0/10

TechCrunch reports on alleged Iranian cyberattacks targeting U.S. water utilities, outlining what is known and what remains uncertain.

rss · TechCrunch · 8月14日 19:04

**标签**: `#cybersecurity`, `#critical infrastructure`, `#cyberwarfare`, `#water utilities`, `#Iran`

---

<a id="item-9"></a>
## [Does Mark Zuckerberg really believe AI is ‘for everyone’?](https://techcrunch.com/video/does-mark-zuckerberg-really-believe-ai-is-for-everyone/) ⭐️ 7.0/10

Meta launched the open-weight AI model Glimmer, contrasting with its locked Muse Spark, while Zuckerberg promoted the idea that AI should be accessible to everyone.

rss · TechCrunch · 8月14日 15:43

**标签**: `#AI`, `#OpenAI`, `#Meta`, `#Democratization`, `#Machine Learning`

---

<a id="item-10"></a>
## [Samsung health AI models analyse wearable biosignal data](https://www.artificialintelligence-news.com/news/samsung-health-ai-models-analyse-wearable-biosignal-data/) ⭐️ 7.0/10

Samsung Research America unveiled two AI foundation models that learn from smartwatch biosignals to advance digital health capabilities.

rss · AI News · 8月14日 13:30

**标签**: `#AI`, `#Wearable Technology`, `#Biosignals`, `#Digital Health`, `#Foundation Models`

---