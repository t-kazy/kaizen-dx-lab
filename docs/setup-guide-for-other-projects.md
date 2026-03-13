# 他プロジェクトでスライド作成スキルを使うためのセットアップガイド

## 必要なファイル構成

他プロジェクトのルートに以下のファイルをコピーしてください。

```
your-project/
├── CLAUDE.md                          # ← オートルーティング設定を追記
├── .claude/
│   └── skills/
│       ├── design-slides.md           # ← コピー元: kaizen-dx-lab/.claude/skills/design-slides.md
│       └── refine-slides.md           # ← コピー元: kaizen-dx-lab/.claude/skills/refine-slides.md
└── templates/
    ├── slide-base.html                # ← コピー元: kaizen-dx-lab/templates/slide-base.html
    └── themes/
        ├── midnight-indigo.css        # ← コピー元: kaizen-dx-lab/templates/themes/midnight-indigo.css
        ├── arctic-frost.css           # ← コピー元: kaizen-dx-lab/templates/themes/arctic-frost.css
        └── obsidian-ember.css         # ← コピー元: kaizen-dx-lab/templates/themes/obsidian-ember.css
```

## セットアップ手順

### 1. ファイルをコピー

```bash
# スキルファイル
mkdir -p your-project/.claude/skills
cp kaizen-dx-lab/.claude/skills/design-slides.md your-project/.claude/skills/
cp kaizen-dx-lab/.claude/skills/refine-slides.md your-project/.claude/skills/

# テンプレート
mkdir -p your-project/templates/themes
cp kaizen-dx-lab/templates/slide-base.html your-project/templates/
cp kaizen-dx-lab/templates/themes/*.css your-project/templates/themes/
```

### 2. CLAUDE.md にオートルーティング設定を追記

既存の `CLAUDE.md` に以下を追記してください（なければ新規作成）:

```markdown
## スライド生成スキル

### Auto-routing Rules

ユーザーのリクエスト内容に応じて、以下のスキルを自動的に適用する。

| トリガー | 適用スキル | スキルファイル |
|---|---|---|
| スライド作成、プレゼン資料作成、提案書作成 | `/design-slides` | `.claude/skills/design-slides.md` |
| スライドの改善、デザインレビュー、スライド修正 | `/refine-slides` | `.claude/skills/refine-slides.md` |

### ルーティング手順
1. ユーザーのメッセージが上記のいずれかに該当するか判定する
2. 該当する場合、対応するスキルファイルを **必ず Read で読み込んで** から作業を開始する
3. スキルファイルに記載された全てのステップ・デザイン原則・ルールに厳密に従う
```

## 使い方

### スラッシュコマンドで呼ぶ（確実）

```
/design-slides SaaS導入提案 - ターゲット: CTO、テーマ: midnight-indigo
```

```
/refine-slides ./examples/proposal.html
```

### 自然言語で呼ぶ（オートルーティング設定済みの場合）

```
クライアント向けのDX推進提案スライドを作って。対象は経営企画部、15枚程度。
```

```
このスライドのデザインをレビューして改善して: ./examples/proposal.html
```

### より詳細に指示する場合

```
/design-slides
- トピック: AI活用による業務効率化提案
- 対象: 経営企画部
- トーン: データドリブン、堅実
- スライド数: 15枚
- テーマ: arctic-frost（ライト系の企業向けテーマ）
```

## 利用可能なテーマ

| テーマ名 | 特徴 | 適したシーン |
|---|---|---|
| `midnight-indigo` | ダーク × ブルー | テック、SaaS、DX |
| `arctic-frost` | ライト × クリーン | コンサル、企業向け |
| `obsidian-ember` | ダーク × 暖色 | クリエイティブ、スタートアップ |

## 注意事項

- `templates/` ディレクトリはスキルがテンプレートを参照するために必要です
- 生成されたスライドは `examples/` ディレクトリに出力されます
- 出力は単一の自己完結型HTMLファイル（CSS全てインライン）なので、ブラウザで直接開けます
