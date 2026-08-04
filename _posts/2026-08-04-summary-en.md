---
layout: default
title: "Horizon Summary: 2026-08-04 (EN)"
date: 2026-08-04
lang: en
---

> From 88 items, 8 important content pieces were selected

---

1. [Anthropic Secures $10B Compute Deal with AI Cloud Startup](#item-1) ⭐️ 9.0/10
2. [White House Finalizes Secret AI Model Assessment Framework](#item-2) ⭐️ 8.0/10
3. [DeepSeek V4 Flash Runs on Single AMD MI300X](#item-3) ⭐️ 8.0/10
4. [Keyv and Related Packages Hit by Shai‑Hulud Supply‑Chain Breach](#item-4) ⭐️ 8.0/10
5. [IcPower Cuts Power Sign‑Off Cycle from Weeks to Days](#item-5) ⭐️ 8.0/10
6. [South Korea Launches National AI Computing Center Project](#item-6) ⭐️ 8.0/10
7. [Automakers Launch Own Battery Brands, Challenging CATL](#item-7) ⭐️ 7.0/10
8. [Tsinghua PhDs Secure Multi-Million Yuan Funding for Space Situational Awareness Startup](#item-8) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Anthropic Secures $10B Compute Deal with AI Cloud Startup](https://36kr.com/newsflashes/3925172170324099?f=rss) ⭐️ 9.0/10

Anthropic has entered into a $10 billion compute agreement with an unnamed AI cloud startup, committing the startup to deliver large‑scale GPU and TPU resources for training and inference. This deal signals a major investment in AI infrastructure, positioning Anthropic to scale its models faster and potentially reshaping the competitive landscape of AI cloud services. The agreement likely includes multi‑year commitments, performance SLAs, and access to specialized hardware such as NVIDIA’s latest GPUs, though specific terms remain undisclosed.

rss · 36氪 · Aug 4, 12:11

**Background**: Anthropic is an AI safety and research company founded by former OpenAI employees, focused on building reliable and steerable AI systems. Compute agreements in the AI sector are long‑term contracts that secure access to large‑scale GPU or TPU resources, often from hyperscalers or specialized cloud providers. Such deals are critical for training large language models, which can require hundreds of petaflop‑seconds of compute.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anthropic">Anthropic - Wikipedia</a></li>
<li><a href="https://computelaw.blog/deals/cloud-hosting-agreements-slas-ai-workloads/">Cloud and hosting agreements and SLAs for AI workloads · Compute Law Blog</a></li>
<li><a href="https://investors.coreweave.com/news/news-details/2026/Jane-Street-Signs-6-Billion-AI-Cloud-Agreement-With-CoreWeave/default.aspx">CoreWeave - Jane Street Signs $6 Billion AI Cloud Agreement With CoreWeave</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Cloud Computing`, `#Compute`, `#Business Deal`, `#Infrastructure`

---

<a id="item-2"></a>
## [White House Finalizes Secret AI Model Assessment Framework](https://www.axios.com/2026/08/03/white-house-finalizes-ai-framework-behind-closed-doors) ⭐️ 8.0/10

On August 3, the White House announced that it has finished a voluntary assessment framework for advanced AI models, but it will not disclose the framework’s contents, the list of reviewers, or when companies can begin using it. The framework requires firms to grant the government access to models up to 30 days before public release and imposes confidentiality, cybersecurity, intellectual‑property, and NDA requirements. The policy gives the federal government a structured way to evaluate frontier AI models before they reach the market, potentially influencing industry compliance and shaping future AI regulation. The lack of transparency limits the industry’s ability to prepare and may raise concerns about privacy and competitive advantage. The executive order mandates a 30‑day pre‑release access window and classifies model network‑capability benchmark testing as confidential. Trusted partners are defined, but the list of eligible partners and detailed assessment criteria remain undisclosed.

telegram · zaihuapd · Aug 4, 02:31

**Background**: In June 2026, President Biden signed Executive Order 14365, establishing a voluntary early‑access framework for frontier AI models. The order requires developers to provide the government with access to models up to 30 days before release, allowing assessment of safety, security, and policy impacts. The White House has been working with major AI labs—OpenAI, Anthropic, Google, and others—to finalize the framework, which is now complete but remains classified.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/08/03/white-house-ai-companies-voluntary-framework-meeting.html">White House to host AI companies Tuesday to review new model-testing framework</a></li>
<li><a href="https://thenextweb.com/news/white-house-ai-framework-secret-voluntary-classified">The White House says its AI framework is done. It will not say what is in it.</a></li>
<li><a href="https://www.nortonrosefulbright.com/en/knowledge/publications/900af3cf/executive-order-establishes-voluntary-early-access-framework-to-frontier-ai-models">EO sets voluntary ‘early access’ framework for AI models | Global law firm | Norton Rose Fulbright</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#AI regulation`, `#AI governance`, `#U.S. government`, `#AI industry`

---

<a id="item-3"></a>
## [DeepSeek V4 Flash Runs on Single AMD MI300X](https://github.com/ryanzhou/deepseek-v4-flash-mi300x) ⭐️ 8.0/10

The GitHub repository demonstrates how to run DeepSeek V4 Flash on a single AMD MI300X GPU, detailing memory usage, native MXFP4 quantization, and performance trade‑offs. It shows that the 284 B Mixture‑of‑Experts model can fit within 144 GB of HBM3 and achieve roughly 150 tokens per second with a 256k context window. Running a 284 B LLM on a single accelerator lowers hardware cost and proves that high‑performance inference is achievable on more affordable systems. It also provides the community with practical insights into quantization and memory strategies for large models. The implementation relies on native MXFP4 quantization of the 256 MoE exports, allowing the 13 B active‑parameter model to fit within 144 GB HBM3. Performance is limited by the reduced 256k context window \(vs. the 1M window of the full model\) but still exceeds 150 tokens per second on a single MI300X.

hackernews · zhoutong · Aug 4, 10:00 · [Discussion](https://news.ycombinator.com/item?id=49166386)

**Background**: DeepSeek V4 Flash is a 284 B Mixture‑of‑Experts language model with 13 B active parameters and a 1M‑token context window, optimized for coding and agentic workflows. The AMD MI300X is a high‑end discrete GPU featuring 192 GB of HBM3 memory and a 304‑unit compute architecture, designed for generative AI workloads. Quantization techniques such as MXFP4 reduce memory footprint while preserving inference accuracy, enabling large models to run on limited hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://lmstudio.ai/models/deepseek-v4-flash">DeepSeek V4 Flash - lmstudio.ai</a></li>
<li><a href="https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/data-sheets/amd-instinct-mi300x-data-sheet.pdf">AMD Instinct MI300X Accelerator</a></li>
<li><a href="https://cast.ai/blog/demystifying-quantizations-llms/">LLM Quantization Methods: GPTQ, AWQ, GGUF - Cast AI</a></li>

</ul>
</details>

**Discussion**: Commenters note that a single MI300X is not a standalone unit and that the MI350P PCIe card offers a more realistic single‑GPU option with 144 GB memory. They discuss the benefits of higher HBM on the MI300X, the trade‑offs of reducing the context window to 256k, and compare the quantization approach to other models like DwarfStar.

**Tags**: `#AI/ML`, `#LLM inference`, `#AMD MI300X`, `#quantization`, `#hardware acceleration`

---

<a id="item-4"></a>
## [Keyv and Related Packages Hit by Shai‑Hulud Supply‑Chain Breach](https://www.aikido.dev/blog/keyv-and-friends-compromised-in-npm-supply-chain-attack) ⭐️ 8.0/10

The npm package keyv and several of its related packages were compromised in the Shai‑Hulud supply‑chain attack, which injected malicious code via pre‑install hooks. The breach forced the community to re‑evaluate the use of pre‑install hooks and to adopt stricter security practices. This attack exposed the vulnerability of widely used Node.js libraries to supply‑chain compromise, highlighting how pre‑install hooks can be weaponized. Developers and organizations that depend on keyv or its ecosystem may have inadvertently installed malicious code, potentially affecting production systems. The malicious payload was delivered through a pre‑install hook that executed arbitrary code during npm install, a feature that has been debated for its security risks. The attack affected more than 170 packages, and the keyv package was among those with an active pre‑install hook that was exploited.

hackernews · cimi\_ · Aug 4, 11:01 · [Discussion](https://news.ycombinator.com/item?id=49166874)

**Background**: npm is the default package manager for Node.js, and packages are distributed via the npm registry. Packages can include lifecycle scripts such as pre‑install hooks that run before the package is installed. The Shai‑Hulud attack was a self‑propagating supply‑chain worm that targeted npm and PyPI packages, compromising over 170 projects by inserting malicious code into legitimate packages.

<details><summary>References</summary>
<ul>
<li><a href="https://www.npmjs.com/package/keyv">keyv - npm</a></li>
<li><a href="https://nodered.org/docs/api/hooks/install/">Node Install Hooks : Node-RED</a></li>
<li><a href="https://www.wiz.io/blog/shai-hulud-npm-supply-chain-attack">Shai - Hulud npm Supply Chain Attack | Wiz Blog</a></li>

</ul>
</details>

**Discussion**: Community members expressed alarm over the use of pre‑install hooks, calling for a moratorium on new hooks and stricter scrutiny of existing ones. Some commenters noted the difficulty of cleaning up compromised dependencies and the persistence of knock‑on attacks. Others suggested practical mitigation steps, such as setting a minimum release age in .npmrc and using tools to scan node\_modules for malicious patterns.

**Tags**: `#supply-chain-security`, `#nodejs`, `#npm`, `#pre-install-hooks`, `#software-security`

---

<a id="item-5"></a>
## [IcPower Cuts Power Sign‑Off Cycle from Weeks to Days](https://36kr.com/p/3925067918227591?f=rss) ⭐️ 8.0/10

ChipXiao Tech released the IcPower distributed matrix solver, which speeds up power sign‑off for advanced‑process chips by 4.5–8.5×, reducing the cycle from several weeks to just a few days. Faster power sign‑off accelerates chip design cycles, cuts engineering costs, and enables domestic vendors to compete with foreign EDA tools in the high‑performance semiconductor market. The solver applies region‑decomposition and graph‑based partitioning to split the billion‑node power network into sub‑matrices, then runs distributed computations with optimized communication topology and numerical‑stability controls to match single‑machine precision.

rss · 36氪 · Aug 4, 10:27

**Background**: In advanced‑process chip design, power sign‑off verifies that the power network meets power, voltage drop, and electromigration requirements by solving a sparse matrix equation with billions of nodes. Traditionally, this analysis takes weeks, especially as transistor counts grow. Distributed computing and region‑decomposition techniques, originally developed for large‑scale inverse problems, enable parallel solving of sub‑problems to reduce overall time.

<details><summary>References</summary>
<ul>
<li><a href="https://36kr.com/p/3925067918227591">36kr.com/p/3925067918227591</a></li>
<li><a href="https://www.163.com/dy/article/L3GPHUNM05118DFD.html">163.com/dy/article/L3GPHUNM05118DFD.html</a></li>

</ul>
</details>

**Tags**: `#EDA`, `#Power Integrity`, `#Distributed Computing`, `#Semiconductor Design`, `#Matrix Solver`

---

<a id="item-6"></a>
## [South Korea Launches National AI Computing Center Project](https://36kr.com/newsflashes/3925199434611072?f=rss) ⭐️ 8.0/10

Construction of South Korea’s national AI computing center, led by Samsung SDS, officially began on August 3, 2024, with a total investment of 2.5 trillion KRW and a projected completion in 2028. The center will provide a dedicated high‑performance AI infrastructure, boosting Korea’s competitiveness in AI research, development, and commercial services, and supporting the national AI strategy to become a global AI hub. The facility will occupy about 48,000 square meters and consist of a two‑storey building, with a consortium of Samsung SDS, NAVER Cloud, Samsung C&amp;T, Samsung Electronics, Kakao, KT, and local governments securing the contract through open bidding.

rss · 36氪 · Aug 4, 12:39

**Background**: AI computing centers are large‑scale data facilities that provide GPU/TPU clusters for training and inference of large language models and other AI workloads. Countries such as China have built similar centers in Xi&\#x27;an, Beijing, and Tianjin to support national AI initiatives. Samsung SDS, a global IT services provider, has experience building and operating large‑scale cloud and AI infrastructure, while NAVER Cloud offers cloud services tailored to Korean enterprises.

<details><summary>References</summary>
<ul>
<li><a href="https://h5.ifeng.com/c/vivoArticle/v002VZAnOg--6YRZK9K18vJKhoXogOxEAJZpaKBaC1Kb8GQM__?isNews=1&amp;showComments=0">探访西北首个大规模AI 算 力 集群：大模型背后是大生态</a></li>
<li><a href="https://3w.huanqiu.com/a/c36dc8/4BhG0q1Cv4u">北京昇腾 人 工 智 能 计 算 中 心 上线，首批签约47家单位</a></li>
<li><a href="https://www.ncloud.com/policy/infou/infou?language=zh-CN">NAVER CLOUD PLATFORM NAVER 云 平台</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#South Korea`, `#Samsung SDS`, `#national AI strategy`, `#cloud computing`

---

<a id="item-7"></a>
## [Automakers Launch Own Battery Brands, Challenging CATL](https://36kr.com/p/3925382191708552?f=rss) ⭐️ 7.0/10

Several automakers, including Huawei&\#x27;s 鸿蒙智行, Li Auto, and Xiaomi, have introduced proprietary battery brands—巨鲸, 理想牌, and 龙甲—each with distinct performance targets such as full‑temperature thermal protection, 2000 cycles, and 500 J impact resistance. By controlling battery design, production, and supply chain, automakers aim to reduce costs, secure supply, and differentiate their vehicles, potentially reshaping the competitive landscape dominated by CATL. These brands employ ‘penetrative management,’ defining cell and pack standards, participating in material development, and even hiring for battery‑factory roles, while still facing CATL’s superior production consistency.

rss · 36氪 · Aug 4, 15:46

**Background**: Battery packs are the heart of electric vehicles, typically accounting for about 30% of vehicle cost. Traditionally, leading suppliers like CATL provide mature system‑level solutions, leaving automakers with limited customization. Recent advances in cell chemistry and manufacturing have lowered entry barriers, enabling automakers to consider in‑house battery development.

<details><summary>References</summary>
<ul>
<li><a href="https://www.autohome.com.cn/tech/202512/1310838.html">【图】不起火不爆炸的 电 池 真的有吗？ 华为用“ 巨 鲸 ”给出答案_汽车之家</a></li>
<li><a href="https://post.smzdm.com/p/ad73n8zn/">电 池 健 康 度 低于80...</a></li>
<li><a href="https://post.smzdm.com/p/a70kwle9/">智能可变大空间增程SUV：小米澎程N70 Max、N90 Max...</a></li>

</ul>
</details>

**Tags**: `#Automotive`, `#Battery`, `#EV`, `#SupplyChain`, `#CATL`

---

<a id="item-8"></a>
## [Tsinghua PhDs Secure Multi-Million Yuan Funding for Space Situational Awareness Startup](https://36kr.com/p/3924634192673153?f=rss) ⭐️ 7.0/10

The startup Qingbo Kuan Tian has closed a multi‑million yuan angel+ round led by Minghui Investment, with participation from Xingxiang and Taiya Investments, and Maple Pledge as private equity advisor. The capital will fund the construction of a space target monitoring network, iteration of the SSA algorithm platform, core team expansion, and key customer development. As low‑Earth‑orbit congestion grows, collision risk for commercial satellites rises sharply, making space situational awareness a critical capability for operators. Commercial SSA providers can offer flexible, cost‑effective services that complement national‑level systems. Both founders are Tsinghua University “Three‑Clear” PhDs with deep expertise in orbital dynamics and SSA, and the company is building a multi‑source monitoring system that includes optical telescopes, radio receivers, and phased‑array radar, while also developing AI‑driven risk analysis algorithms.

rss · 36氪 · Aug 4, 03:05

**Background**: Space situational awareness \(SSA\) refers to tracking and predicting the positions of objects in Earth orbit to prevent collisions. The number of resident space objects has reached tens of thousands, and debris risk continues to rise. The rapid growth of commercial satellite constellations has created a strong demand for SSA services.

<details><summary>References</summary>
<ul>
<li><a href="https://www.spacefoundation.org/space_brief/space-situational-awareness/">Space Situational Awareness</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0094576524006726">Space situational awareness systems: Bridging traditional ...</a></li>

</ul>
</details>

**Tags**: `#Space Situational Awareness`, `#Startup Funding`, `#Commercial Space`, `#Satellite Collision Avoidance`, `#Tsinghua University`

---