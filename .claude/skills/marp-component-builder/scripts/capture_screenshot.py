#!/usr/bin/env python3
"""
HTMLスクリーンショット撮影スクリプト

Playwright/Puppeteerを使用してHTMLファイルのスクリーンショットを撮影します。
参考: https://note.com/aoki_monpro/n/nd2a7266f0d5e
"""

import sys
import argparse
from pathlib import Path


def capture_with_playwright(html_path: Path, output_path: Path, width: int = 1280, height: int = 720) -> bool:
    """Playwrightでスクリーンショットを撮影"""
    try:
        from playwright.sync_api import sync_playwright

        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={'width': width, 'height': height})

            # ローカルHTMLファイルを開く
            page.goto(f'file://{html_path.absolute()}')

            # スクリーンショット撮影
            page.screenshot(path=str(output_path), full_page=True)

            browser.close()

        print(f"✅ スクリーンショット撮影完了: {output_path}")
        return True

    except ImportError:
        print("❌ Playwrightがインストールされていません", file=sys.stderr)
        print("インストール: pip install playwright && playwright install chromium", file=sys.stderr)
        return False
    except Exception as e:
        print(f"❌ スクリーンショット撮影エラー: {e}", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(description='HTMLファイルのスクリーンショットを撮影')
    parser.add_argument('html_path', type=Path, help='HTMLファイルパス')
    parser.add_argument('--output', '-o', type=Path, help='出力画像パス', required=True)
    parser.add_argument('--width', type=int, default=1280, help='ビューポート幅（デフォルト: 1280）')
    parser.add_argument('--height', type=int, default=720, help='ビューポート高さ（デフォルト: 720）')

    args = parser.parse_args()

    if not args.html_path.exists():
        print(f"❌ HTMLファイルが見つかりません: {args.html_path}", file=sys.stderr)
        sys.exit(1)

    # 出力ディレクトリを作成
    args.output.parent.mkdir(parents=True, exist_ok=True)

    # スクリーンショット撮影
    if capture_with_playwright(args.html_path, args.output, args.width, args.height):
        print(f"\n📸 スクリーンショット: {args.output}")
    else:
        sys.exit(1)


if __name__ == '__main__':
    main()
