# Order Desk Demo

架空の注文照会・通知テンプレート用の Python 演示リポジトリです。
サンプル値と履歴はすべて人工データです。演示ブランチには、レビュー対象の不具合を含みます。

基準ブランチのテストは `python3 -m unittest discover -s tests -v` で実行できます。
演示ブランチと期待結果は [演示シナリオ](docs/演示シナリオ.md) を参照してください。

## GitHub PR 自动审查

将工作流和配置合入 `main`。在本仓库的 **Settings → Secrets and variables → Actions** 中配置以下各项。

| 类型 | 名称 | 值 |
|---|---|---|
| Variable | `REVIEW_LLM_MODEL` | 已获准使用的网关固定模型 ID |
| Secret | `REVIEW_LLM_API_KEY` | 网关凭据 |
| Secret | `REVIEW_SCM_TOKEN` | `linxichong` 的细粒度 GitHub PAT，限定本仓库并授予 Pull requests 读权限 |

同仓库的非草稿 PR 以 `main` 为目标时，创建、重新打开、推送提交或标记为待审会触发审查。
工作流从 PR 的基准提交读取项目配置、提示词和规则，PR 的头部提交只用于取差异。
通过安全检查的审查输入会发送至配置的外部模型。成功后在 **Actions → AI 审查 → Artifacts** 下载对应提交的结果 JSON。
本流程是试运行，GitHub 评论和反馈同步均关闭。SQLite 随 runner 退出而丢弃。
试点期间关闭网关重试。审查失败时，步骤日志仅输出 CLI 退出码和可用的结构化错误类别，成功结果才会上传。
