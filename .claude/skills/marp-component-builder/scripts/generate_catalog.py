#!/usr/bin/env python3
"""
Marpコンポーネントカタログ生成スクリプト

コンポーネントのテスト用HTMLカタログを生成し、スクリーンショットを撮影します。
"""

import sys
import subprocess
import argparse
from pathlib import Path


def generate_catalog_markdown(component_name: str, css_content: str, output_path: Path) -> Path:
    """コンポーネントカタログ用のMarkdownファイルを生成"""

    catalog_content = f"""---
marp: true
theme: slide-ai
---

<!-- _class: title -->

# Component Catalog
## {component_name}

---

# {component_name} Example

<!--
ここにコンポーネントの使用例を追加
例: <div class="{component_name}">...</div>
-->

<div class="{component_name}">
  <p>Sample content</p>
</div>

---

# Variations

<!-- コンポーネントのバリエーション例 -->

"""

    output_path.write_text(catalog_content, encoding='utf-8')
    return output_path


def generate_html(markdown_path: Path, output_path: Path) -> bool:
    """Marp CLIでHTMLを生成"""
    try:
        cmd = [
            'marp',
            str(markdown_path),
            '-o', str(output_path),
            '--html',
            '--allow-local-files'
        ]

        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"✅ HTML生成完了: {output_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ HTML生成エラー: {e.stderr}", file=sys.stderr)
        return False
    except FileNotFoundError:
        print("❌ Marp CLIが見つかりません。npm install -g @marp-team/marp-cli でインストールしてください。", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(description='Marpコンポーネントカタログを生成')
    parser.add_argument('component_name', help='コンポーネント名（例: metric-card）')
    parser.add_argument('--css', help='CSSファイルパス', required=False)
    parser.add_argument('--output-dir', help='出力ディレクトリ', default='./catalog')

    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Markdownファイル生成
    md_path = output_dir / f"{args.component_name}_catalog.md"
    css_content = Path(args.css).read_text() if args.css else ""

    generate_catalog_markdown(args.component_name, css_content, md_path)

    # HTML生成
    html_path = output_dir / f"{args.component_name}_catalog.html"
    if generate_html(md_path, html_path):
        print(f"\n📄 カタログが生成されました:")
        print(f"  Markdown: {md_path}")
        print(f"  HTML: {html_path}")
        print(f"\nブラウザで開く: file://{html_path.absolute()}")
    else:
        sys.exit(1)


if __name__ == '__main__':
    main()
