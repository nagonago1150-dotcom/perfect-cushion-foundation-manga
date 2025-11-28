#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LP派生リンクプロジェクト: クッションファンデ（漫画型）
販売リンク置換スクリプト

目的: 各派生LPフォルダのindex.htmlに、それぞれ異なる販売リンクを埋め込む
"""

import os
import shutil
from pathlib import Path

# プロジェクト設定
PROJECT_NAME = "cushion-manga"
BASE_DIR = Path(__file__).parent
XSERVER_UPLOAD_DIR = BASE_DIR / "xserver-upload"
MASTER_HTML = BASE_DIR / "index.html"

# 現在のマスターリンク（置換対象）
MASTER_LINK = "https://www.shinnihonseiyaku.co.jp/lp/promotion/cosme/2375b_19/"

# 派生URLと販売リンクの対応
DERIVATIVE_LINKS = {
    "cushion-manga-1": "https://greatasp.com/link.php?i=pi7o66ridb7f&m=mi6f5xl5wn0u",
    "cushion-manga-2": "https://greatasp.com/link.php?i=pi7o6beemjrm&m=mi73szi7s9zb",
}


def replace_links_in_file(file_path, old_link, new_link):
    """
    HTMLファイル内のリンクを置換

    Args:
        file_path: 対象ファイルのパス
        old_link: 置換前のリンク
        new_link: 置換後のリンク
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # リンクを置換
        updated_content = content.replace(old_link, new_link)

        # 置換回数をカウント
        count = content.count(old_link)

        # ファイルに書き込み
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)

        print(f"✓ {file_path.name}: {count}箇所のリンクを置換しました")
        return count

    except Exception as e:
        print(f"✗ エラー: {file_path} - {e}")
        return 0


def main():
    """メイン処理"""
    print("=" * 60)
    print(f"LP派生リンクプロジェクト: {PROJECT_NAME}")
    print("=" * 60)
    print()

    total_replacements = 0

    # 各派生フォルダのindex.htmlを処理
    for folder_name, new_link in DERIVATIVE_LINKS.items():
        folder_path = XSERVER_UPLOAD_DIR / folder_name
        index_html = folder_path / "index.html"

        if not index_html.exists():
            print(f"⚠ 警告: {index_html} が見つかりません")
            continue

        print(f"\n処理中: {folder_name}/index.html")
        print(f"  置換前: {MASTER_LINK}")
        print(f"  置換後: {new_link}")

        count = replace_links_in_file(index_html, MASTER_LINK, new_link)
        total_replacements += count

    print()
    print("=" * 60)
    print(f"完了: 合計 {total_replacements} 箇所のリンクを置換しました")
    print("=" * 60)
    print()
    print("次のステップ:")
    print(f"1. ローカル確認: python3 -m http.server 8000")
    print(f"   - http://localhost:8000/xserver-upload/cushion-manga-1/")
    print(f"   - http://localhost:8000/xserver-upload/cushion-manga-2/")
    print(f"2. Git コミット & プッシュ")
    print(f"3. Xserver FTPアップロード: xserver-upload/ -> public_html/")
    print()


if __name__ == "__main__":
    main()
