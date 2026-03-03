# kaizen-dx-lab

ExcelシフトデータをCSV形式に自動変換するツール。

## 機能

- Excelシフト表（.xlsx）を読み取り、フラットなCSVに変換
- 日付ヘッダー行・従業員名列の自動検出
- 複数の日付形式に対応（`3/1(月)`, `2026/3/1`, `3月1日`, datetime型）
- 複数シートの一括変換
- BOM付きUTF-8出力（Excelでの文字化け防止）

## セットアップ

```bash
pip install -r requirements.txt
```

## 使い方

```bash
# 基本的な使い方
python -m src.excel_to_csv input.xlsx

# 出力先を指定
python -m src.excel_to_csv input.xlsx -o output.csv

# 特定シートのみ変換
python -m src.excel_to_csv input.xlsx -s "3月シフト表"

# 年を明示指定（ヘッダーに年が無い場合）
python -m src.excel_to_csv input.xlsx -y 2026
```

### オプション

| オプション | 説明 | デフォルト |
|---|---|---|
| `-o, --output` | 出力CSVファイルパス | 入力ファイル名.csv |
| `-s, --sheet` | 変換対象シート名 | 全シート |
| `-y, --year` | 日付の年 | 今年 |
| `-e, --encoding` | 出力エンコーディング | utf-8-sig |

### 出力CSV形式

```csv
date,employee,shift
2026-03-01,田中太郎,早番
2026-03-01,鈴木花子,遅番
```

## サンプルデータの生成

```bash
python scripts/create_sample_data.py
```

## テスト

```bash
python -m pytest tests/ -v
```
