# Horizon 日报 Vercel 镜像部署

> 背景：GitHub Pages（yhllxy.github.io）在大陆网络直连被阻断，手机端（无代理）打不开日报。
> 方案：用 Vercel（国内可达）镜像部署同一份 gh-pages 分支，GitHub Pages 保留并行运行。

## 架构

```
daily-summary CI（每天 UTC 22:00）
  └─ peaceiris/actions-gh-pages 推送 docs/ → gh-pages 分支
       ├─ GitHub Actions 自动构建 → GitHub Pages（原样保留）
       └─ Vercel Git 集成 webhook → 自动构建部署 → <项目>.vercel.app
```

日报更新后两边自动同步；构建配置全部版本化在 `docs/` 下（`Gemfile`、`_config.vercel.yml`、`vercel.json`），由 peaceiris 自动带上 gh-pages 分支。

## 部署步骤（Vercel 控制台，一次性，约 3 分钟）

1. 打开 <https://vercel.com> → **Add New Project** → **Import** 选择 GitHub 仓库 `YHLLXY/Horizon`（首次需授权 GitHub）
2. **生产分支（Production Branch）选 `gh-pages`** ← 关键，日报都在这个分支
3. Framework Preset 会自动识别为 **Jekyll**（`docs/vercel.json` 已锁定构建命令，无需手动配置）
4. 点 **Deploy**，等构建完成（约 1-2 分钟）
5. 部署后访问 `<项目>.vercel.app`（可在 Settings → Domains 绑定自定义域名）

## 部署后检查项

- [ ] 首页正常渲染（莫兰迪风格、导航、样式）
- [ ] 打开最新一期日报（`_posts` 下 8/5 起应有 7-17KB 真实内容）
- [ ] feed 可用：`<项目>.vercel.app/feed-zh.xml`
- [ ] 手机浏览器打开（无代理）正常
- [ ] 次日早 7 点日报更新后，Vercel 自动重新部署（无需手动）

## FAQ

**Q: feed 里的链接指向 yhllxy.github.io 怎么办？**
把 `docs/_config.vercel.yml` 里的 `url` 改成实际 Vercel 域名（如 `https://horizon-daily.vercel.app`），改后推送 master 即可（下个 CI 周期自动同步部署）。不影响阅读。

**Q: 构建失败怎么办？**
在 Vercel 项目 → Deployments → 失败记录查看日志。已知坑：Ruby 编码错误（构建命令已带 `LANG=C.UTF-8 LC_ALL=C.UTF-8` 规避）、gem 版本冲突（改 `docs/Gemfile` 版本号）。

**Q: 想完全停掉 GitHub Pages？**
保留即可，零成本；或到仓库 Settings → Pages 关闭。

**Q: 为什么不用 vercel-action 在 CI 里部署？**
需要额外生成 VERCEL_TOKEN 等 secrets；Git 集成方案零 token、控制台一次配置永久生效。
