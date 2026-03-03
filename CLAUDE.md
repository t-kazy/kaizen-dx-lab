# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## Project Overview

ExcelシフトデータをCSV形式に自動変換するPythonツール。openpyxlでExcelを読み取り、日付・従業員・シフト種別のフラットCSVに変換する。

## Repository Structure

```
.
├── CLAUDE.md
├── README.md
├── requirements.txt          # Python依存パッケージ (openpyxl)
├── src/
│   ├── __init__.py
│   └── excel_to_csv.py       # メイン変換ロジック
├── tests/
│   ├── __init__.py
│   └── test_excel_to_csv.py  # pytest テスト
├── scripts/
│   └── create_sample_data.py # サンプルExcel生成
└── sample_data/              # サンプルデータ
```

## Development

- **Language**: Python 3.11+
- **Dependencies**: `pip install -r requirements.txt`
- **Test**: `python -m pytest tests/ -v`
- **Run**: `python -m src.excel_to_csv <input.xlsx>`
