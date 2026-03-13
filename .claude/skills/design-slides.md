# /design-slides - プレミアム クライアント向けスライド生成

クライアントプレゼンテーション用の高品質でデザイン重視のHTMLスライドデッキを生成する。

## 使い方

```
/design-slides [トピックまたは簡単な説明]
```

## スキル手順

このスキルが呼び出されたら、以下のルールに厳密に従い、完全な自己完結型HTMLスライドデッキを生成する。

### ステップ 1: ブリーフの理解

ユーザーが十分なコンテキストを提供していない場合は確認する。一行の簡単な説明のみの場合は、妥当なデフォルトを推測して進める。

```yaml
確認項目:
  - 項目: トピック / 提案テーマ
    例: "小売業クライアント向けDX変革提案"
  - 項目: 対象者
    例: "CTO、取締役、マーケティングチーム"
  - 項目: トーン
    例: "大胆＆ビジョナリー、落ち着き＆プロフェッショナル、データドリブン"
  - 項目: おおよそのスライド枚数
    デフォルト: 12〜18枚
  - 項目: テーマ選択
    選択肢:
      - midnight-indigo
      - arctic-frost
      - obsidian-ember
```

### ステップ 2: テーマ選択とテンプレート参照

ベーステンプレートと選択したテーマを読み込む。生成するデッキは、すべてのCSS（ベースデザインシステムとテーマの両方）をインラインで含む**単一の自己完結型HTMLファイル**でなければならない。外部CSS `<link>` 参照は使用せず、すべてを `<style>` タグ内にインラインで記述すること。

```yaml
テンプレート:
  ベース: templates/slide-base.html     # HTMLスケルトンとCSSデザインシステム
  テーマ: templates/themes/{theme}.css   # カラー/スタイルテーマ

出力ルール:
  形式: 単一の自己完結型HTMLファイル
  CSS: すべてインライン（<style>タグ内）
  外部参照: 禁止
```

### ステップ 3: スライド構成

すべてのデッキは以下の構成に従うこと。

```yaml
デッキ構成:
  - 順番: 1
    種別: カバースライド
    内容: タイトル + サブタイトル + 企業名/日付
    目的: 視覚的インパクト最大

  - 順番: 2
    種別: アジェンダ / 概要
    内容: 3〜5つの主要トピック
    目的: ビジュアルロードマップとして表示

  - 順番: 3〜N
    種別: コンテンツスライド
    内容: 本題（スライドタイプカタログ参照）
    目的: 提案の実質的な内容

  - 順番: N+1
    種別: サマリー
    内容: 3〜5つの箇条書き
    目的: 重要なポイントのまとめ

  - 順番: N+2
    種別: ネクストステップ
    内容: タイムラインまたはアクションアイテム
    目的: 次の行動の明確化

  - 順番: N+3
    種別: クロージング
    内容: お礼 / 連絡先 / CTA
    目的: 締めくくり
```

### ステップ 4: スライドタイプカタログ

デッキ全体でこれらのスライドタイプを多様に使い分けること。**連続するスライドで同じレイアウトを使用してはならない。**

```yaml
スライドタイプ:
  - 名前: カバー
    CSSクラス: slide-cover
    使用場面: ヒーロータイポグラフィのオープニングスライド

  - 名前: セクション区切り
    CSSクラス: slide-section
    使用場面: トピック間のアクセントグラデーション区切り

  - 名前: 2カラム
    CSSクラス: grid-2
    使用場面: 比較、ビフォー/アフター、テキスト+ビジュアル

  - 名前: 3カード
    CSSクラス: grid-3
    使用場面: 機能、柱、オプション

  - 名前: 4カード
    CSSクラス: grid-4
    使用場面: メトリクスダッシュボード、複数KPI

  - 名前: 2:1 分割
    CSSクラス: grid-2-1
    使用場面: メインコンテンツ + サイドバー

  - 名前: 1:2 分割
    CSSクラス: grid-1-2
    使用場面: サイドバー + メインコンテンツ

  - 名前: 大きな数値 / KPI
    CSSクラス: .metric コンポーネント使用
    使用場面: インパクトメトリクス、ROI

  - 名前: タイムライン
    CSSクラス: .timeline コンポーネント使用
    使用場面: ロードマップ、フェーズ分け

  - 名前: 番号付きリスト
    CSSクラス: .numbered-list 使用
    使用場面: プロセス、ステップ

  - 名前: 引用 / コールアウト
    CSSクラス: 中央揃えの大きなテキスト
    使用場面: インパクトのある一文

  - 名前: クロージング
    CSSクラス: slide-closing
    使用場面: CTAを含む最終スライド
```

### ステップ 5: デザイン原則（重要）

スライドがプレミアムに見え、ありきたりにならないよう、以下のルールを厳守する。

```yaml
デザイン原則:
  タイポグラフィ:
    - heading-hero（120px）はカバースライドのみで使用
    - スライドタイトルには heading-1 または heading-2 を使用
    - タイトルは短くインパクトのあるものに（最大6〜8単語）
    - 本文テキストは body-lg または body-base を使用（body-sm より小さくしない）
    - .text-gradient はヒーロー数値やキーフレーズに控えめに使用
    - ラベル、カテゴリ、メタデータには .caption クラスを使用

  視覚的階層:
    - すべてのスライドに明確なフォーカルポイントを1つ設ける
    - 余白を積極的に活用（スライド面積の60%以上を埋めない）
    - カードの内容は簡潔に（1カードあたり最大2〜3行）
    - 見出しとコンテンツの区切りには .divider-gradient を使用

  色とコントラスト:
    - アクセントカラーは強調に使い、全面的には使わない
    - テキストは背景に対して明確なコントラストを確保
    - 二次的な情報には .text-muted を使用
    - 三次的/メタデータには .text-subtle を使用

  装飾要素:
    - スライドの30〜40%に '<div class="bg-grid"></div>' を追加してテクスチャを出す
    - すべてのスライドに '<div class="bg-noise"></div>' を追加して奥行きを出す
    - 主要スライド（カバー、セクション、クロージング）に .bg-blob 要素を使用（1スライドあたり最大2つ）
    - 装飾はやりすぎない（感じられるが目立たない程度に）

  データとメトリクス:
    - 数値には必ず .metric コンポーネントを使用（プレーンテキストは禁止）
    - パーセンテージには .progress-bar を使用
    - ステータス/カテゴリラベルには .badge または .chip を使用
    - 長文の段落よりも大きな数値の方がインパクトがある

  カードデザイン:
    - .card / .card-glass / .card-elevated / .card-outline を交互に使い分ける
    - カードヘッダーに .icon-circle と絵文字アイコンを追加して視覚的なアンカーにする
    - カードの内容は見出し + 1〜2行の説明に留める
```

### ステップ 6: コンテンツ品質

```yaml
コンテンツルール:
  見出し:
    方針: レポート作成者ではなくデザイナーのように書く
    良い例: "出荷方法を変革する"
    悪い例: "デジタルトランスフォーメーション提案"

  箇条書き:
    最大数: 1スライドあたり4つ
    文字数: 各12単語以内

  数値:
    方針: 必ず文脈を付ける
    良い例: "デプロイが3.2倍高速化"
    悪い例: "3.2倍"

  言葉遣い:
    方針: クライアントの業界用語を適切に合わせる

  流れ:
    方針: 各スライドが論理的に次のスライドにつながるようにする
```

### ステップ 7: ページ番号

カバー以外のすべてのスライドに追加：

```html
<span class="page-number">02</span>
```

### ステップ 8: 出力

```yaml
出力先: examples/{説明的な名前}.html

ファイル要件:
  - 単一の自己完結型HTMLファイル（すべてのCSSをインライン）
  - モダンブラウザで正しく表示される
  - キーボードナビゲーション対応（矢印キー、スペース）
  - クリック/タップナビゲーション対応
  - モバイルでのタッチスワイプ対応
  - 上部にプログレスバーを表示
  - ページカウンターを表示（右下、ホバー時に表示）
```

### ステップ 9: 完了報告

```yaml
報告内容:
  - ファイルパス
  - スライド枚数
  - 使用テーマ
  - 改善提案やバリエーション
```

---

## スライドHTMLパターン例

### カバースライド

```html
<section class="slide slide-cover">
  <div class="bg-blob" style="width:600px;height:600px;background:var(--accent-primary);top:-200px;right:-100px;"></div>
  <div class="bg-blob" style="width:500px;height:500px;background:#ec4899;bottom:-150px;left:-100px;"></div>
  <div class="bg-noise"></div>
  <div class="slide-inner text-center">
    <div class="badge" style="margin-bottom:var(--space-md);">PROPOSAL 2026</div>
    <h1 class="heading-hero text-gradient" style="margin-bottom:var(--space-md);">Reimagine Your<br>Digital Experience</h1>
    <p class="body-lg text-muted" style="max-width:680px;margin:0 auto;">A strategic roadmap to transform customer engagement<br>and accelerate growth through technology.</p>
    <div style="margin-top:var(--space-xl);">
      <p class="caption text-subtle">CLIENT NAME | MARCH 2026</p>
    </div>
  </div>
</section>
```

### KPI / メトリクススライド

```html
<section class="slide">
  <div class="bg-noise"></div>
  <div class="slide-inner">
    <div class="caption text-accent" style="margin-bottom:var(--space-sm);">インパクトメトリクス</div>
    <h2 class="heading-2" style="margin-bottom:var(--space-lg);">成長を促進する<br>測定可能な成果</h2>
    <div class="divider-gradient" style="margin-bottom:var(--space-xl);"></div>
    <div class="grid-4">
      <div class="card-glass" style="text-align:center;">
        <div class="metric">
          <span class="metric-value">3.2x</span>
          <span class="metric-label">デプロイ高速化</span>
          <span class="metric-delta positive">+220%</span>
        </div>
      </div>
      <!-- 他のメトリクスも同様に繰り返す -->
    </div>
  </div>
  <span class="page-number">05</span>
</section>
```

### 3カード機能スライド

```html
<section class="slide">
  <div class="bg-grid"></div>
  <div class="bg-noise"></div>
  <div class="slide-inner">
    <div class="caption text-accent" style="margin-bottom:var(--space-sm);">アプローチ</div>
    <h2 class="heading-2" style="margin-bottom:var(--space-xl);">変革を支える<br>3つの柱</h2>
    <div class="grid-3">
      <div class="card">
        <div class="icon-circle" style="margin-bottom:var(--space-md);">&#9889;</div>
        <h3 class="heading-4" style="margin-bottom:var(--space-sm);">スピード</h3>
        <p class="body-base text-muted">主要なデリバリーパイプラインの自動化でタイム・トゥ・マーケットを短縮。</p>
      </div>
      <!-- 繰り返す -->
    </div>
  </div>
  <span class="page-number">06</span>
</section>
```

### タイムラインスライド

```html
<section class="slide">
  <div class="bg-noise"></div>
  <div class="slide-inner">
    <div class="caption text-accent" style="margin-bottom:var(--space-sm);">ロードマップ</div>
    <h2 class="heading-2" style="margin-bottom:var(--space-xl);">実行<br>タイムライン</h2>
    <div class="grid-2">
      <div class="timeline">
        <div class="timeline-item">
          <div class="caption text-accent">フェーズ 01 — 2026年 Q2</div>
          <h3 class="heading-4" style="margin-top:var(--space-xs);">ディスカバリーとアセスメント</h3>
          <p class="body-sm text-muted" style="margin-top:var(--space-xs);">現状分析と機会のマッピング。</p>
        </div>
        <!-- 繰り返す -->
      </div>
      <div class="card-glass" style="padding:var(--space-lg);">
        <!-- サマリーまたはビジュアル -->
      </div>
    </div>
  </div>
  <span class="page-number">10</span>
</section>
```

### セクション区切り

```html
<section class="slide slide-section">
  <div class="bg-noise"></div>
  <div class="slide-inner text-center">
    <div class="badge" style="background:rgba(255,255,255,0.15);color:#fff;margin-bottom:var(--space-md);">SECTION 02</div>
    <h2 class="heading-1">ソリューション</h2>
    <p class="text-muted body-lg" style="margin-top:var(--space-md);max-width:600px;margin-left:auto;margin-right:auto;">エンドツーエンドで業務を変革する方法。</p>
  </div>
</section>
```
