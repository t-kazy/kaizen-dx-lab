# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## Project Overview

kaizen-dx-lab は社内ナレッジを管理するリポジトリです。業務カテゴリごとの手順・ルールを Markdown ファイルで管理しています。

## Repository Structure

```
.
├── README.md
├── CLAUDE.md
├── scripts/
│   └── sync_to_dify.py     # Dify ナレッジベース同期スクリプト
├── .github/workflows/
│   └── sync-dify-knowledge.yml  # docs/ 変更時に Dify へ自動同期
└── docs/
    ├── README.md          # ナレッジ一覧(インデックス)
    ├── 全体.md
    ├── 送迎(行き).md
    ├── はじまりの会.md
    ├── 宿題.md
    ├── 活動準備.md
    ├── 活動.md
    ├── おやつ・食事提供.md
    ├── 遊び(自由時間).md
    ├── 掃除・点検.md
    ├── おわりの会.md
    ├── 送迎(帰り).md
    ├── 未所時.md
    ├── 活動記録.md
    └── 管理業務.md
```

## Development

- **Dify 同期**: `docs/` を main に push すると GitHub Actions が Dify ナレッジベースへ自動同期
- **手動同期**: `DIFY_API_KEY` と `DIFY_DATASET_ID` を環境変数にセットして `python scripts/sync_to_dify.py`

## ナレッジの追加・編集

- `docs/` ディレクトリ配下に Markdown ファイルを追加・編集してください
- 新しいカテゴリを追加した場合は `docs/README.md` の一覧も更新してください
