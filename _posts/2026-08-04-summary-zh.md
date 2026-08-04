---
layout: default
title: "Horizon Summary: 2026-08-04 (ZH)"
date: 2026-08-04
lang: zh
---

> 从 88 条内容中筛选出 8 条重要资讯。

---

1. [Anthropic 与 AI 云初创公司签署 100 亿美元算力协议](#item-1) ⭐️ 9.0/10
2. [白宫完成机密 AI 模型评估框架](#item-2) ⭐️ 8.0/10
3. [DeepSeek V4 Flash 在单块 AMD MI300X 上运行](#item-3) ⭐️ 8.0/10
4. [Keyv 及相关包遭受 Shai‑Hulud 供应链攻击](#item-4) ⭐️ 8.0/10
5. [IcPower 将电源签核周期从周缩至天](#item-5) ⭐️ 8.0/10
6. [韩国启动国家 AI 算力中心](#item-6) ⭐️ 8.0/10
7. [车企自研电池品牌，挑战宁德时代](#item-7) ⭐️ 7.0/10
8. [清华博士联合创业公司获数千万天使+轮融资](#item-8) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Anthropic 与 AI 云初创公司签署 100 亿美元算力协议](https://36kr.com/newsflashes/3925172170324099?f=rss) ⭐️ 9.0/10

Anthropic 与一家人工智能云初创公司签署了一项价值 100 亿美元的算力协议，承诺为其提供大规模 GPU 和 TPU 资源，用于训练和推理。 此交易表明对 AI 基础设施的重大投资，使 Anthropic 能更快扩展其模型，并可能重塑 AI 云服务的竞争格局。 该协议可能包含多年承诺、性能 SLA 以及对 NVIDIA 最新 GPU 等专业硬件的访问，但具体条款尚未公开。

rss · 36氪 · 8月4日 12:11

**背景**: Anthropic 是一家由前 OpenAI 员工创立的 AI 安全与研究公司，致力于构建可靠且可控的 AI 系统。AI 领域的算力协议是长期合同，确保获取大规模 GPU 或 TPU 资源，通常来自超大规模云服务商或专业云提供商。此类协议对训练大型语言模型至关重要，因为训练可能需要数百亿亿次浮点运算。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anthropic">Anthropic - Wikipedia</a></li>
<li><a href="https://computelaw.blog/deals/cloud-hosting-agreements-slas-ai-workloads/">Cloud and hosting agreements and SLAs for AI workloads · Compute Law Blog</a></li>
<li><a href="https://investors.coreweave.com/news/news-details/2026/Jane-Street-Signs-6-Billion-AI-Cloud-Agreement-With-CoreWeave/default.aspx">CoreWeave - Jane Street Signs $6 Billion AI Cloud Agreement With CoreWeave</a></li>

</ul>
</details>

**标签**: `#AI`, `#Cloud Computing`, `#Compute`, `#Business Deal`, `#Infrastructure`

---

<a id="item-2"></a>
## [白宫完成机密 AI 模型评估框架](https://www.axios.com/2026/08/03/white-house-finalizes-ai-framework-behind-closed-doors) ⭐️ 8.0/10

白宫在 8 月 3 日宣布已完成先进 AI 模型的自愿评估框架，但将不公开框架内容、审阅者名单或企业何时开始使用。该框架规定企业在模型公开发布前最多 30 天内向政府开放访问，并要求保密、网络安全、知识产权保护和保密协议。 该政策为联邦政府提供了在模型上市前评估前沿 AI 的结构化方式，可能影响行业合规并塑造未来 AI 监管。缺乏透明度限制了行业的准备能力，也可能引发关于隐私和竞争优势的担忧。 行政令规定了 30 天的预发布访问窗口，并将模型网络能力基准测试列为机密。已定义可信伙伴，但合格伙伴名单和详细评估标准仍未公开。

telegram · zaihuapd · 8月4日 02:31

**背景**: 2026 年 6 月，拜登总统签署了行政命令 14365，建立了前沿 AI 模型的自愿早期访问框架。该命令要求开发者在模型发布前最多 30 天向政府开放访问，以评估安全、网络安全和政策影响。白宫一直与主要 AI 实验室——OpenAI、Anthropic、Google 等合作，完成了该框架，但仍保持机密。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/08/03/white-house-ai-companies-voluntary-framework-meeting.html">White House to host AI companies Tuesday to review new model-testing framework</a></li>
<li><a href="https://thenextweb.com/news/white-house-ai-framework-secret-voluntary-classified">The White House says its AI framework is done. It will not say what is in it.</a></li>
<li><a href="https://www.nortonrosefulbright.com/en/knowledge/publications/900af3cf/executive-order-establishes-voluntary-early-access-framework-to-frontier-ai-models">EO sets voluntary ‘early access’ framework for AI models | Global law firm | Norton Rose Fulbright</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#AI regulation`, `#AI governance`, `#U.S. government`, `#AI industry`

---

<a id="item-3"></a>
## [DeepSeek V4 Flash 在单块 AMD MI300X 上运行](https://github.com/ryanzhou/deepseek-v4-flash-mi300x) ⭐️ 8.0/10

该 GitHub 仓库演示了如何在单块 AMD MI300X GPU 上运行 DeepSeek V4 Flash，详细说明了内存使用、原生 MXFP4 量化以及性能权衡。它表明 284 B Mixture‑of‑Experts 模型可以在 144 GB HBM3 内存中运行，并在 256k 上下文窗口下实现约 150 tokens/秒。 在单块加速器上运行 284 B LLM 降低了硬件成本，并证明了在更实惠的系统上实现高性能推理的可行性。它还为社区提供了关于大模型量化和内存策略的实用见解。 实现依赖于 256 MoE 导出的原生 MXFP4 量化，使 13 B 活跃参数模型能够适配 144 GB HBM3。性能受限于 256k 上下文窗口（相较于完整模型的 1M），但单块 MI300X 仍能超过 150 tokens/秒。

hackernews · zhoutong · 8月4日 10:00 · [社区讨论](https://news.ycombinator.com/item?id=49166386)

**背景**: DeepSeek V4 Flash 是一个 284 B 的 Mixture‑of‑Experts 语言模型，拥有 13 B 活跃参数和 1M‑token 上下文窗口，专为编码和代理工作流程优化。AMD MI300X 是一款高端离散 GPU，配备 192 GB HBM3 内存和 304 个计算单元，专为生成式 AI 工作负载设计。MXFP4 等量化技术通过降低内存占用同时保持推理精度，使大型模型能够在有限硬件上运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lmstudio.ai/models/deepseek-v4-flash">DeepSeek V4 Flash - lmstudio.ai</a></li>
<li><a href="https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/data-sheets/amd-instinct-mi300x-data-sheet.pdf">AMD Instinct MI300X Accelerator</a></li>
<li><a href="https://cast.ai/blog/demystifying-quantizations-llms/">LLM Quantization Methods: GPTQ, AWQ, GGUF - Cast AI</a></li>

</ul>
</details>

**社区讨论**: 评论者指出单块 MI300X 并非独立单元，MI350P PCIe 卡提供更实用的单 GPU 选项，拥有 144 GB 内存。他们讨论了 MI300X 更高 HBM 的优势、将上下文窗口降至 256k 的权衡，并将量化方法与 DwarfStar 等其他模型进行比较。

**标签**: `#AI/ML`, `#LLM inference`, `#AMD MI300X`, `#quantization`, `#hardware acceleration`

---

<a id="item-4"></a>
## [Keyv 及相关包遭受 Shai‑Hulud 供应链攻击](https://www.aikido.dev/blog/keyv-and-friends-compromised-in-npm-supply-chain-attack) ⭐️ 8.0/10

npm 包 keyv 及其相关包在 Shai‑Hulud 供应链攻击中被入侵，攻击通过 pre‑install 钩子注入恶意代码。此事件促使社区重新评估 pre‑install 钩子的使用，并采取更严格的安全措施。 此攻击揭示了广泛使用的 Node.js 库在供应链中的脆弱性，突显了 pre‑install 钩子被恶意利用的风险。依赖 keyv 或其生态系统的开发者和组织可能无意中安装了恶意代码，可能影响生产环境。 恶意负载通过在 npm 安装期间执行任意代码的 pre‑install 钩子传递，这一功能因安全风险而备受争议。此次攻击影响了 170 多个包，keyv 便是其中使用了被利用的 pre‑install 钩子的包之一。

hackernews · cimi\_ · 8月4日 11:01 · [社区讨论](https://news.ycombinator.com/item?id=49166874)

**背景**: npm 是 Node.js 的默认包管理器，包通过 npm 注册表分发。包可以包含生命周期脚本，例如在包安装前运行的 pre‑install 钩子。Shai‑Hulud 攻击是一种自我传播的供应链蠕虫，针对 npm 和 PyPI 包，通过向合法包注入恶意代码，导致 170 多个项目被入侵。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.npmjs.com/package/keyv">keyv - npm</a></li>
<li><a href="https://nodered.org/docs/api/hooks/install/">Node Install Hooks : Node-RED</a></li>
<li><a href="https://www.wiz.io/blog/shai-hulud-npm-supply-chain-attack">Shai - Hulud npm Supply Chain Attack | Wiz Blog</a></li>

</ul>
</details>

**社区讨论**: 社区成员对 pre‑install 钩子的使用表示担忧，呼吁暂停新增钩子并加强对现有钩子的审查。有人指出清理受损依赖的难度以及连锁攻击的持续性。还有人建议实用的缓解措施，例如在 .npmrc 中设置最小发布年龄，并使用工具扫描 node\_modules 以查找恶意模式。

**标签**: `#supply-chain-security`, `#nodejs`, `#npm`, `#pre-install-hooks`, `#software-security`

---

<a id="item-5"></a>
## [IcPower 将电源签核周期从周缩至天](https://36kr.com/p/3925067918227591?f=rss) ⭐️ 8.0/10

芯晓科技推出的 IcPower 分布式矩阵求解器，将先进工艺芯片的电源签核速度提升 4.5–8.5 倍，签核周期从几周缩短到几天。 更快的电源签核加速芯片设计周期，降低工程成本，使国内厂商在高性能半导体市场与国外 EDA 工具竞争。 该求解器采用区域分解和图论分区，将数十亿节点的电源网络拆分为子矩阵，在分布式环境下通过优化通信拓扑和数值稳定性控制，保证与单机精度一致。

rss · 36氪 · 8月4日 10:27

**背景**: 在先进工艺芯片设计中，电源签核通过求解包含数十亿节点的稀疏矩阵方程来验证电源网络的功耗、电压降和电迁移等指标。传统上，这一分析需要数周时间，尤其随着晶体管数量的增长。分布式计算和区域分解技术（源自大规模逆问题）可将问题拆分为子问题并行求解，从而缩短总耗时。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://36kr.com/p/3925067918227591">36kr.com/p/3925067918227591</a></li>
<li><a href="https://www.163.com/dy/article/L3GPHUNM05118DFD.html">163.com/dy/article/L3GPHUNM05118DFD.html</a></li>

</ul>
</details>

**标签**: `#EDA`, `#Power Integrity`, `#Distributed Computing`, `#Semiconductor Design`, `#Matrix Solver`

---

<a id="item-6"></a>
## [韩国启动国家 AI 算力中心](https://36kr.com/newsflashes/3925199434611072?f=rss) ⭐️ 8.0/10

韩国国家人工智能算力中心建设工作已于 2024 年 8 月 3 日正式启动，由三星 SDS 牵头，项目总投资 2.5 万亿韩元，预计 2028 年竣工投用。 该中心将为韩国提供专用的高性能 AI 算力基础设施，提升在 AI 研发和商业服务方面的竞争力，支持国家 AI 战略，助力成为全球 AI 中心。 该设施占地约 4.8 万平方米，规划为两层建筑，三星 SDS、NAVER 云、三星物产、三星电子、Kakao、KT、光州市政府等联合体通过公开招标获得项目。

rss · 36氪 · 8月4日 12:39

**背景**: 人工智能算力中心是大型数据设施，提供 GPU/TPU 集群用于训练和推理大模型等 AI 工作负载。中国已在西安、北京、天津等地建设类似中心，以支持国家 AI 计划。三星 SDS 作为全球 IT 服务提供商，拥有构建和运营大规模云与 AI 基础设施的经验，NAVER 云则为韩国企业提供定制化云服务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://h5.ifeng.com/c/vivoArticle/v002VZAnOg--6YRZK9K18vJKhoXogOxEAJZpaKBaC1Kb8GQM__?isNews=1&amp;showComments=0">探访西北首个大规模AI 算 力 集群：大模型背后是大生态</a></li>
<li><a href="https://3w.huanqiu.com/a/c36dc8/4BhG0q1Cv4u">北京昇腾 人 工 智 能 计 算 中 心 上线，首批签约47家单位</a></li>
<li><a href="https://www.ncloud.com/policy/infou/infou?language=zh-CN">NAVER CLOUD PLATFORM NAVER 云 平台</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#South Korea`, `#Samsung SDS`, `#national AI strategy`, `#cloud computing`

---

<a id="item-7"></a>
## [车企自研电池品牌，挑战宁德时代](https://36kr.com/p/3925382191708552?f=rss) ⭐️ 7.0/10

华为鸿蒙智行、理想汽车、小米等多家车企相继推出自有电池品牌——巨鲸、理想牌、龙甲，分别针对全温度热防护、2000 次循环和 500 J 撞击等性能指标。 车企通过掌控电池技术与供应链，既能降低成本、保障供给，又能在产品差异化上获得竞争优势，可能重塑以宁德时代为主导的市场格局。 这些品牌采用“穿透式管理”，从电芯到电池包制定技术标准，参与材料研发，甚至参与核心岗位招聘，但仍需与宁德时代的生产一致性竞争。

rss · 36氪 · 8月4日 15:46

**背景**: 动力电池是电动车的核心部件，约占整车成本的 30%。传统上，宁德时代等领先供应商提供成熟的系统级方案，车企定制空间有限。随着电芯技术与制造工艺的进步，门槛下降，车企开始考虑自研电池。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.autohome.com.cn/tech/202512/1310838.html">【图】不起火不爆炸的 电 池 真的有吗？ 华为用“ 巨 鲸 ”给出答案_汽车之家</a></li>
<li><a href="https://post.smzdm.com/p/ad73n8zn/">电 池 健 康 度 低于80...</a></li>
<li><a href="https://post.smzdm.com/p/a70kwle9/">智能可变大空间增程SUV：小米澎程N70 Max、N90 Max...</a></li>

</ul>
</details>

**标签**: `#Automotive`, `#Battery`, `#EV`, `#SupplyChain`, `#CATL`

---

<a id="item-8"></a>
## [清华博士联合创业公司获数千万天使+轮融资](https://36kr.com/p/3924634192673153?f=rss) ⭐️ 7.0/10

清博空天完成数千万元天使+轮融资，主要用于空间目标监测网络建设、算法平台迭代、核心技术团队扩充及重点客户开拓。 随着低轨卫星和碎片数量激增，空间态势感知成为卫星运营的基础能力，商业公司提供此类服务可提升轨道安全。 公司创始人均为清华“三清”博士，拥有航天动力学与空间态势感知研究经验，正在构建光学、无线电、雷达多源监测体系并布局 AI 算法。

rss · 36氪 · 8月4日 03:05

**背景**: 空间态势感知（SSA）指跟踪轨道物体并预测其位置，以预防碰撞。近地轨道物体数量已达数万，碎片风险持续上升。商业卫星数量激增导致对 SSA 服务需求快速增长。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.spacefoundation.org/space_brief/space-situational-awareness/">Space Situational Awareness</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0094576524006726">Space situational awareness systems: Bridging traditional ...</a></li>

</ul>
</details>

**标签**: `#Space Situational Awareness`, `#Startup Funding`, `#Commercial Space`, `#Satellite Collision Avoidance`, `#Tsinghua University`

---