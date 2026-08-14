---
layout: default
title: "Horizon Summary: 2026-08-14 (EN)"
date: 2026-08-14
lang: en
---

> From 51 items, 10 important content pieces were selected

---

1. [AI‑Powered Human Tissue Lab Could Replace Animal Testing](#item-1) ⭐️ 9.0/10
2. [Google Makes Homomorphic Encryption Practical for Private AI](#item-2) ⭐️ 9.0/10
3. [Apple Seeks 15% Commission on External App Purchases](#item-3) ⭐️ 9.0/10
4. [Qwen 3.8 27B Released – New Reasoning Power](#item-4) ⭐️ 8.0/10
5. [HN Digest 2026-08-13 · Gemini 3.7 Flash：原生多模态推理新迭代](#item-5) ⭐️ 8.0/10
6. [Uber and Pony.ai Expand Robotaxi Fleet to 2,000 Units in Europe](#item-6) ⭐️ 8.0/10
7. [California Grants Permits for Aurora and Kodiak Truck Tests](#item-7) ⭐️ 7.0/10
8. [What we know about the alleged Iranian hacks on US water utilities](#item-8) ⭐️ 7.0/10
9. [Does Mark Zuckerberg really believe AI is ‘for everyone’?](#item-9) ⭐️ 7.0/10
10. [Samsung health AI models analyse wearable biosignal data](#item-10) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [AI‑Powered Human Tissue Lab Could Replace Animal Testing](https://www.fastcompany.com/91589344/the-worlds-largest-biological-datacenter-could-help-make-animal-testing-obsolete) ⭐️ 9.0/10

Vivodyne’s AI‑driven platform now operates 12 robotic “honeycomb” labs that can test over 3 million human tissue samples per year, doubling the total capacity of all U.S. clinical trials combined. With 90 % of drugs failing after animal tests, this scalable human‑tissue approach could dramatically improve safety predictions and reduce reliance on animal models, accelerating drug development. The system uses fully automated robotics and AI‑designed experiments to control variables, but it currently focuses on in‑vitro organoids and does not yet replace all in‑vivo validation steps.

telegram · zaihuapd · Aug 14, 01:48

**Background**: Traditional drug discovery relies heavily on animal testing to assess efficacy and toxicity, yet many compounds fail in later human trials. Advances in tissue engineering allow scientists to grow human organoids that mimic real tissues, and AI can optimize experimental designs and interpret complex data. Vivodyne combines these technologies to create a high‑throughput platform that tests drugs directly on human tissues.

<details><summary>References</summary>
<ul>
<li><a href="https://www.vivodyne.com/">Vivodyne | Make biology computable</a></li>
<li><a href="https://www.genengnews.com/topics/artificial-intelligence/vivodynes-lab-grown-human-tissue-platform-gets-real-with-38-million-seed-financing/">Vivodyne&#x27;s Lab Grown Human Tissue Platform Gets Real with $38 Million Seed Financing</a></li>
<li><a href="https://www.vivodyne.com/platform">Vivodyne - Our Platform</a></li>

</ul>
</details>

**Tags**: `#AI`, `#drug testing`, `#tissue engineering`, `#animal testing`, `#biomedical research`

---

<a id="item-2"></a>
## [Google Makes Homomorphic Encryption Practical for Private AI](https://blog.google/security/how-google-is-making-private-ai-practical-with-homomorphic-encryption/) ⭐️ 9.0/10

Google announced that it has reduced the computational overhead of homomorphic encryption to the point where private AI inference is now practical. The company demonstrated the technique on its Gemma4 model, enabling inference on encrypted data without revealing inputs or outputs. This breakthrough allows organizations to run sensitive AI workloads in the cloud while keeping data encrypted, addressing privacy concerns and regulatory compliance. It could reduce the need for costly hardware enclaves and make privacy-preserving AI more accessible. The optimization leverages specialized arithmetic libraries and batching techniques, cutting overhead from ~1000× to a few dozen times compared to plaintext inference. However, the approach still requires careful key management and may not yet support all model architectures.

hackernews · u1hcw9nx · Aug 14, 15:43 · [Discussion](https://news.ycombinator.com/item?id=49300314)

**Background**: Homomorphic encryption allows computation on ciphertexts, producing ciphertext outputs that decrypt to the same result as if computed on plaintext. It has long been considered too slow for practical use, especially for large neural networks. Google’s recent work demonstrates that with algorithmic and hardware optimizations, the overhead can be reduced enough for real-world inference workloads.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Homomorphic_encryption">Homomorphic encryption</a></li>
<li><a href="https://www.splunk.com/en_us/blog/learn/homomorphic-encryption.html">Homomorphic Encryption: How It Works | Splunk</a></li>

</ul>
</details>

**Discussion**: Users expressed skepticism about the claimed performance gains, noting that HE still incurs high overhead and may not be commercially viable. Some pointed out that private AI could be achieved locally without cloud reliance, while others questioned Google&\#x27;s privacy claims given past product shortcomings.

**Tags**: `#homomorphic encryption`, `#privacy‑preserving AI`, `#Google`, `#machine learning security`, `#AI privacy`

---

<a id="item-3"></a>
## [Apple Seeks 15% Commission on External App Purchases](https://techcrunch.com/2026/08/14/apple-proposes-to-take-a-15-cut-of-purchases-made-outside-the-app-store/) ⭐️ 9.0/10

Apple has petitioned a federal judge to allow it to charge up to a 15% commission on purchases made through external links embedded in iOS apps. This would extend its existing App Store fee structure to transactions that occur outside the App Store but are initiated from within an app. If approved, developers would face higher costs for any in-app purchases routed through external links, potentially reshaping monetization strategies and prompting a shift toward alternative payment methods. The move could also intensify antitrust scrutiny of Apple&\#x27;s control over the iOS ecosystem. The commission applies only to transactions that are initiated via deep links or universal links that open a third‑party site, not to purchases made directly within the App Store. Apple argues the fee is necessary to maintain the security and privacy guarantees of the iOS platform.

rss · TechCrunch · Aug 14, 14:54

**Background**: Universal links are a feature of iOS that allow a URL to open an app directly if it is installed, otherwise it falls back to a web page. Deep linking extends this by directing users to specific content or screens within the app. Apple traditionally charges a 15% or 30% commission on sales made through the App Store, but has not previously taken a cut on purchases that leave the App Store ecosystem.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.apple.com/documentation/xcode/supporting-universal-links-in-your-app">Supporting universal links in your app | Apple Developer Documentation</a></li>
<li><a href="https://orufy.com/blog/webtonative/deep-linking-in-ios">Deep Linking in iOS —A Complete Guide of 2026</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#App Store`, `#commissions`, `#app development`, `#antitrust`

---

<a id="item-4"></a>
## [Qwen 3.8 27B Released – New Reasoning Power](https://huggingface.co/Qwen/Qwen3.8-27B-FP8) ⭐️ 8.0/10

Alibaba’s Qwen team has released the 27‑parameter Qwen 3.8 model on Hugging Face, featuring a dense 27B architecture with a vision encoder, 262,144‑token native context and support for up to 1M tokens via RoPE scaling. The launch sparked a lively Hacker News thread where users benchmarked its explicit reasoning against models such as Opus, Gemma 4, and Claude. The model demonstrates that a 27B‑parameter LLM can achieve competitive reasoning scores while remaining deployable on consumer hardware, addressing the community’s demand for efficient, local inference. Its performance against larger or more expensive models highlights a shift toward practical, high‑quality reasoning in the LLM ecosystem. Qwen 3.8 contains 27 B parameters and a hidden dimension of 5120, uses FP8 quantization for efficient inference, and requires roughly 32 GB VRAM for full precision. While it outperforms Opus on certain reasoning benchmarks, its VRAM usage is higher than Gemma 4, and it relies on a dense architecture rather than a mixture‑of‑experts design.

hackernews · erdaltoprak · Aug 14, 15:00 · [Discussion](https://news.ycombinator.com/item?id=49299605)

**Background**: Large language models \(LLMs\) scale performance with parameter count and training data, but practical deployment often hinges on model size and inference efficiency. Reasoning benchmarks, such as mathematical or logical problem sets, evaluate a model’s ability to perform multi‑step inference rather than just generate fluent text. Multimodal extensions, like vision encoders, allow LLMs to process images alongside text, broadening application scope.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-27B">Qwen / Qwen 3 . 8 -27B · Hugging Face</a></li>
<li><a href="https://benchlm.ai/models/qwen3-8-27b">Qwen 3 . 8 -27B Benchmarks &amp; Context (August 2026) | BenchLM.ai</a></li>
<li><a href="https://lmstudio.ai/models/qwen3.8">Qwen 3 . 8</a></li>

</ul>
</details>

**Discussion**: Users praised Qwen 3.8’s explicit reasoning and local performance, noting it beat Opus on certain tasks while remaining cheaper to run. Some commenters compared it to Gemma 4, highlighting higher VRAM demands but clearer reasoning steps. Overall sentiment was positive, with a call for larger or MoE variants to push the boundary further.

**Tags**: `#Large Language Models`, `#Qwen`, `#Model Release`, `#AI Research`, `#Hugging Face`

---

<a id="item-5"></a>
## [HN Digest 2026-08-13 · Gemini 3.7 Flash：原生多模态推理新迭代](https://zeli.app/zh/digest/2026-08-13) ⭐️ 8.0/10

A Hacker News digest summarizing the launch of Gemini 3.7 Flash, a multimodal LLM, and DeepSeek Harness, an open‑source agent framework, both generating significant community discussion.

rss · Zeli · Aug 13, 23:59

**Tags**: `#AI`, `#LLM`, `#multimodal`, `#agent framework`, `#open-source`

---

<a id="item-6"></a>
## [Uber and Pony.ai Expand Robotaxi Fleet to 2,000 Units in Europe](https://techcrunch.com/2026/08/14/uber-and-pony-ai-plan-to-bring-2000-robotaxis-to-europe/) ⭐️ 8.0/10

Uber and autonomous‑vehicle startup Pony.ai announced that they will deploy 2,000 robotaxis across five European cities, expanding beyond their original launch in Zagreb, Croatia. This expansion signals a significant scaling of autonomous mobility services in Europe, potentially reshaping urban transportation, creating new competition for traditional taxi operators, and accelerating the adoption of self‑driving technology. The partnership will deploy 2,000 robotaxis, but the article does not specify the exact models, software versions, or regulatory approvals required for each city.

rss · TechCrunch · Aug 14, 10:44

**Background**: Robotaxis are autonomous vehicles that provide on‑demand rides without a human driver, typically operated by companies like Uber, Waymo, or Pony.ai. Deploying them in cities requires meeting local safety regulations, testing protocols, and infrastructure support. Uber has previously tested robotaxis in Zagreb, Croatia, and is now expanding to additional European markets.

**Tags**: `#autonomous vehicles`, `#robotaxi`, `#Uber`, `#Pony.ai`, `#Europe`

---

<a id="item-7"></a>
## [California Grants Permits for Aurora and Kodiak Truck Tests](https://techcrunch.com/2026/08/14/self-driving-trucks-are-officially-testing-on-california-highways/) ⭐️ 7.0/10

The California Department of Motor Vehicles has issued official testing permits to Aurora Innovation and Kodiak AI, allowing their autonomous trucks to operate on state highways under the safety‑driver and driverless categories. This regulatory milestone signals a shift toward commercial deployment of autonomous freight, potentially reducing labor shortages and improving logistics efficiency across the U.S. trucking industry. Both companies will operate under California&\#x27;s Level 4 autonomy framework; Aurora&\#x27;s trucks already run revenue‑generating freight, while Kodiak&\#x27;s platform is designed for integration into existing fleets.

rss · TechCrunch · Aug 14, 20:37

**Background**: Autonomous trucks use sensors, AI, and mapping to navigate without human input. California has historically been a testing ground for self‑driving vehicles, offering permits that specify safety‑driver or driverless categories and operational limits.

<details><summary>References</summary>
<ul>
<li><a href="https://www.dmv.ca.gov/portal/vehicle-industry-services/autonomous-vehicles/autonomous-vehicle-testing-permit-holders/">Autonomous Vehicle Permit Holders - California DMV - California ...</a></li>
<li><a href="https://aurora.tech/">aurora . tech</a></li>
<li><a href="https://kodiak.ai/?gad=1">Kodiak AI | Autonomous Trucking &amp; AI -Powered Ground Autonomy ...</a></li>

</ul>
</details>

**Tags**: `#autonomous vehicles`, `#self‑driving trucks`, `#California`, `#AI`, `#industry regulation`

---

<a id="item-8"></a>
## [What we know about the alleged Iranian hacks on US water utilities](https://techcrunch.com/2026/08/14/what-we-know-about-the-alleged-iranian-hacks-on-u-s-water-utilities/) ⭐️ 7.0/10

TechCrunch reports on alleged Iranian cyberattacks targeting U.S. water utilities, outlining what is known and what remains uncertain.

rss · TechCrunch · Aug 14, 19:04

**Tags**: `#cybersecurity`, `#critical infrastructure`, `#cyberwarfare`, `#water utilities`, `#Iran`

---

<a id="item-9"></a>
## [Does Mark Zuckerberg really believe AI is ‘for everyone’?](https://techcrunch.com/video/does-mark-zuckerberg-really-believe-ai-is-for-everyone/) ⭐️ 7.0/10

Meta launched the open-weight AI model Glimmer, contrasting with its locked Muse Spark, while Zuckerberg promoted the idea that AI should be accessible to everyone.

rss · TechCrunch · Aug 14, 15:43

**Tags**: `#AI`, `#OpenAI`, `#Meta`, `#Democratization`, `#Machine Learning`

---

<a id="item-10"></a>
## [Samsung health AI models analyse wearable biosignal data](https://www.artificialintelligence-news.com/news/samsung-health-ai-models-analyse-wearable-biosignal-data/) ⭐️ 7.0/10

Samsung Research America unveiled two AI foundation models that learn from smartwatch biosignals to advance digital health capabilities.

rss · AI News · Aug 14, 13:30

**Tags**: `#AI`, `#Wearable Technology`, `#Biosignals`, `#Digital Health`, `#Foundation Models`

---