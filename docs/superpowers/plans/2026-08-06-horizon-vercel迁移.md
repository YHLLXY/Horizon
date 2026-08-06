# Horizon 日报 Vercel 镜像部署 · 实施计划

> 日期：2026-08-06 ｜ 状态：调研完成，待实施
> 背景：站点 https://yhllxy.github.io/Horizon/（Jekyll）在大陆网络直连被阻断，用户手机（无代理）打不开日报。已确认方案：**Vercel 镜像部署 gh-pages 分支**（用户 Vercel 账号已验证可达——工作台就在 vercel.app）。

---

## 一、网上调研结论（2026-08-06，已查证）

| 问题 | 结论 | 来源 |
|------|------|------|
| Vercel 对 Jekyll 的支持 | **原生支持、零配置检测**（官方 KB 2026-06 更新）：检测 `_config.yml` 自动启用 Jekyll preset，默认构建 `jekyll build`，输出 `_site` | [Vercel KB: Deploying Jekyll](https://vercel.com/kb/guide/deploying-jekyll-with-vercel) |
| 已知构建坑 | ① Ruby 3.4/Jekyll 4.4 编码错误 → 需 `LANG=C.UTF-8 LC_ALL=C.UTF-8`；② 无 Gemfile 时主题 gem 缺失（GitHub Pages 预装的主题 Vercel 环境没有）→ **必须提交 Gemfile**；③ Bundler 2.2.3+ 平台差异 → 建议提交 Gemfile.lock（或用 bundle install 现解析） | [Jekyll 部署踩坑总结](https://delusion.uno/posts/Vercel-filed-reason/) |
| gh-pages 分支作为部署源 | **可行**：Vercel Git 集成支持任意分支作生产分支；peaceiris 推 gh-pages → Vercel webhook 自动部署；`keep_files: true` 保留分支上非 publish_dir 文件 | [jzero 双部署模式](https://deepwiki.com/jzero-io/jzero/10.2-documentation-deployment) |
| baseurl 覆盖 | 无环境变量机制；**Jekyll 支持多 config 合并**（`jekyll build --config a.yml,b.yml` 后者覆盖前者）→ 用 `_config.vercel.yml` 覆盖 `baseurl: ""`（Vercel 站点在域名根路径）；`url` 建议部署后按实际域名补 | [Jekyll baseurl 讨论](https://talk.jekyllrb.com/t/need-a-quick-help-with-my-new-jekyll-static-website/6535/5) |
| 替代方案对比 | ① **amondnet/vercel-action 在 CI 部署**：需 VERCEL_TOKEN/ORG_ID/PROJECT_ID 三个 secrets（用户生成 token 步骤多，备选）；② Cloudflare Pages：大陆可达性无实证、用户无账号；③ 静态产物分支（CI 构建后推 _site）：多一个分支 + CI 改动，构建仍要环境 | [vercel-action 迁移案例](https://github.com/kingyx3/puzzlepals/commit/1c7cc5bedee7b2b4bda80a6dfccd77a8867bd1e3) |

**推荐**：Vercel Git 集成直连 gh-pages 分支（零 CI 改动、零 token），构建配置全部版本化进 `docs/`（peaceiris 自动推送到 gh-pages 根），用户在控制台只需 Import + 选分支 + Deploy 三步。

## 二、架构（改后）

```
daily-summary CI（master）
  └─ peaceiris 推 docs/ → gh-pages 分支（含 Gemfile/_config.vercel.yml/vercel.json）
       ├─ GitHub Actions pages-build-deployment → GitHub Pages（保留，原样）
       └─ Vercel webhook → jekyll build（bundle install + LANG 覆盖 + 双 config）
            └─ <项目>.vercel.app（国内可达镜像，手机电脑都能开）
```

- GitHub Pages 与 Vercel **并行不冲突**（同一份 gh-pages 源，两处构建）
- 日报更新（每天早 7 点）→ 两边自动同步

## 三、改动清单（全部在 master 的 docs/，peaceiris 自动同步 gh-pages）

| 文件 | 内容 | 作用 |
|------|------|------|
| `docs/Gemfile`（新） | jekyll + jekyll-theme-cayman + jekyll-feed | Vercel 构建环境声明主题依赖（GitHub Pages 预装但 Vercel 没有） |
| `docs/_config.vercel.yml`（新） | `baseurl: ""` | 覆盖 baseurl（Vercel 站点在根路径；Jekyll 多 config 后者覆盖前者） |
| `docs/vercel.json`（新） | framework=jekyll + 构建命令（bundle install && LANG=C.UTF-8 LC_ALL=C.UTF-8 bundle exec jekyll build --config ...）+ outputDirectory=_site | 构建配置版本化，规避编码坑，用户在控制台零配置 |
| `docs/vercel-deploy.md`（新） | 部署步骤 + 架构 + FAQ + 部署后检查项 | 交付文档 |
| 本计划文档 | — | 留档 |

**不动**：`_config.yml`（GitHub Pages 仍用）、CI workflow、日报生成逻辑、_posts 内容。

## 四、验证方式

1. 本地：JSON/YAML 语法校验（`python -c yaml/json`）；本机无 Ruby，Jekyll 构建无法本地跑 → 依赖 Vercel 首次部署验证
2. Vercel 部署后：访问 `<项目>.vercel.app` 确认日报渲染、导航/样式正常、feed 可用
3. 回归：GitHub Pages 站点不变（代理下可对比）
4. 待用户确认项：日报文件名「当天日期」改造（本次不做，另议）

## 五、风险与对策

| 风险 | 对策 |
|------|------|
| Vercel 构建环境 Ruby 版本与 Gemfile.lock 不兼容 | 不提交 lock（bundle install 现解析）；如失败在 vercel.json 加 `"installCommand"` |
| jekyll-theme-cayman 依赖的 GitHub Pages 特有 gem | cayman 已在 rubygems.org 发布，Gemfile 声明即可；构建失败会有明确报错可迭代 |
| feed 中 absolute_url 指向 github.io | 部署后把实际 Vercel 域名补进 `_config.vercel.yml` 的 `url` 字段（FAQ 已记录） |
| peaceiris 推送覆盖 docs 内新文件 | 新文件就在 publish_dir 内，每次推送自动带上 ✓ |
