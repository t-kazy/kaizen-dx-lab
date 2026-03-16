# kaizen-dx-lab

社内ナレッジを管理するリポジトリです。`docs/` 配下の Markdown ファイルを Dify ナレッジベースへ自動同期します。

## Dify 連携セットアップ

### 1. Dify API キーの取得

1. [Dify](https://cloud.dify.ai/) にログイン
2. 対象のナレッジベース（Knowledge）を開く
3. 左メニュー「API」からデータセット API キーを作成
4. データセット ID は URL から取得: `https://cloud.dify.ai/datasets/{dataset_id}/...`

### 2. GitHub Secrets の設定

リポジトリの **Settings > Secrets and variables > Actions** で以下を登録:

| Secret 名 | 値 |
|---|---|
| `DIFY_API_KEY` | Dify Dataset API キー |
| `DIFY_DATASET_ID` | 同期先データセットの ID |

### 3. 動作の仕組み

- `main` ブランチへ `docs/` 配下のファイルが push されると GitHub Actions が自動実行
- `scripts/sync_to_dify.py` が各 Markdown ファイルを Dify ナレッジベースへ同期
  - ファイル名で既存ドキュメントを照合し、あれば更新・なければ新規作成
- 手動実行も可能（Actions タブ > "Sync docs to Dify Knowledge" > Run workflow）
