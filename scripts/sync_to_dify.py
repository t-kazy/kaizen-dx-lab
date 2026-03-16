#!/usr/bin/env python3
"""docs/ 配下の Markdown ファイルを Dify ナレッジベースへ同期するスクリプト。

環境変数:
  DIFY_API_KEY    : Dify Dataset API キー（必須）
  DIFY_DATASET_ID : 同期先のデータセット ID（必須）
  DIFY_BASE_URL   : API ベース URL（省略時 https://api.dify.ai/v1）
"""

import json
import os
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

DIFY_API_KEY = os.environ.get("DIFY_API_KEY", "")
DIFY_DATASET_ID = os.environ.get("DIFY_DATASET_ID", "")
DIFY_BASE_URL = os.environ.get("DIFY_BASE_URL", "https://api.dify.ai/v1").rstrip("/")

DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"

# デフォルトの処理ルール（automatic モード）
PROCESS_RULE = {"mode": "automatic"}


def api_request(method: str, path: str, body: dict | None = None) -> dict:
    """Dify API へリクエストを送信する。"""
    url = f"{DIFY_BASE_URL}{path}"
    headers = {
        "Authorization": f"Bearer {DIFY_API_KEY}",
        "Content-Type": "application/json",
    }
    data = json.dumps(body).encode() if body else None
    req = urllib.request.Request(url, data=data, headers=headers, method=method)

    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        error_body = e.read().decode()
        print(f"  API Error {e.code}: {error_body}", file=sys.stderr)
        raise


def list_documents() -> dict[str, str]:
    """データセット内の既存ドキュメント一覧を取得し {name: id} の dict を返す。"""
    docs: dict[str, str] = {}
    page = 1
    while True:
        resp = api_request(
            "GET",
            f"/datasets/{DIFY_DATASET_ID}/documents?page={page}&limit=100",
        )
        for doc in resp.get("data", []):
            docs[doc["name"]] = doc["id"]
        if not resp.get("has_more", False):
            break
        page += 1
    return docs


def create_document(name: str, text: str) -> str:
    """新規ドキュメントを作成し、ドキュメント ID を返す。"""
    body = {
        "name": name,
        "text": text,
        "indexing_technique": "high_quality",
        "process_rule": PROCESS_RULE,
    }
    resp = api_request(
        "POST",
        f"/datasets/{DIFY_DATASET_ID}/document/create_by_text",
        body,
    )
    return resp["document"]["id"]


def update_document(doc_id: str, name: str, text: str) -> None:
    """既存ドキュメントをテキストで更新する。"""
    body = {
        "name": name,
        "text": text,
        "process_rule": PROCESS_RULE,
    }
    api_request(
        "POST",
        f"/datasets/{DIFY_DATASET_ID}/documents/{doc_id}/update_by_text",
        body,
    )


def main() -> None:
    if not DIFY_API_KEY or not DIFY_DATASET_ID:
        print("Error: DIFY_API_KEY and DIFY_DATASET_ID must be set.", file=sys.stderr)
        sys.exit(1)

    md_files = sorted(DOCS_DIR.glob("*.md"))
    if not md_files:
        print("No markdown files found in docs/.")
        return

    print(f"Found {len(md_files)} markdown file(s) in docs/")

    existing = list_documents()
    print(f"Existing documents in dataset: {len(existing)}")

    created = 0
    updated = 0

    for md_path in md_files:
        name = md_path.name
        text = md_path.read_text(encoding="utf-8")
        if not text.strip():
            print(f"  Skip (empty): {name}")
            continue

        if name in existing:
            print(f"  Update: {name}")
            update_document(existing[name], name, text)
            updated += 1
        else:
            print(f"  Create: {name}")
            create_document(name, text)
            created += 1

        # レート制限対策
        time.sleep(0.5)

    print(f"\nDone! Created: {created}, Updated: {updated}")


if __name__ == "__main__":
    main()
