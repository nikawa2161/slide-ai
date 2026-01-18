#!/usr/bin/env python3
"""
コンポーネント反復改善スクリプト

CSS生成 → HTML生成 → スクリーンショット → 画像比較のワークフローを実行します。
"""

import sys
import subprocess
import argparse
from pathlib import Path


def run_workflow(
    component_name: str,
    css_file: Path,
    reference_image: Path,
    output_dir: Path
) -> dict:
    """ワークフロー全体を実行"""

    results = {}

    # 1. カタログHTML生成
    print("\n📝 Step 1: カタログHTML生成")
    catalog_script = Path(__file__).parent / 'generate_catalog.py'
    catalog_cmd = [
        'python3', str(catalog_script),
        component_name,
        '--css', str(css_file),
        '--output-dir', str(output_dir)
    ]

    try:
        subprocess.run(catalog_cmd, check=True)
        results['catalog_generated'] = True
    except subprocess.CalledProcessError as e:
        print(f"❌ カタログ生成エラー", file=sys.stderr)
        results['catalog_generated'] = False
        return results

    # 2. スクリーンショット撮影
    print("\n📸 Step 2: スクリーンショット撮影")
    html_path = output_dir / f"{component_name}_catalog.html"
    screenshot_path = output_dir / f"{component_name}_current.png"

    screenshot_script = Path(__file__).parent / 'capture_screenshot.py'
    screenshot_cmd = [
        'python3', str(screenshot_script),
        str(html_path),
        '--output', str(screenshot_path)
    ]

    try:
        subprocess.run(screenshot_cmd, check=True)
        results['screenshot_captured'] = True
    except subprocess.CalledProcessError:
        print(f"❌ スクリーンショット撮影エラー", file=sys.stderr)
        results['screenshot_captured'] = False
        return results

    # 3. 画像比較
    print("\n🔍 Step 3: 画像比較")
    diff_path = output_dir / f"{component_name}_diff.png"

    compare_script = Path(__file__).parent / 'compare_images.py'
    compare_cmd = [
        'python3', str(compare_script),
        str(reference_image),
        str(screenshot_path),
        '--diff-output', str(diff_path)
    ]

    try:
        subprocess.run(compare_cmd, check=True)
        results['comparison_done'] = True
    except subprocess.CalledProcessError:
        print(f"❌ 画像比較エラー", file=sys.stderr)
        results['comparison_done'] = False
        return results

    results['success'] = True
    return results


def main():
    parser = argparse.ArgumentParser(
        description='コンポーネント反復改善ワークフローを実行'
    )
    parser.add_argument('component_name', help='コンポーネント名')
    parser.add_argument('--css', type=Path, required=True, help='CSSファイルパス')
    parser.add_argument('--reference', type=Path, required=True, help='参照画像（モック）')
    parser.add_argument('--output-dir', type=Path, default=Path('./catalog'), help='出力ディレクトリ')

    args = parser.parse_args()

    # 入力ファイルの存在確認
    if not args.css.exists():
        print(f"❌ CSSファイルが見つかりません: {args.css}", file=sys.stderr)
        sys.exit(1)

    if not args.reference.exists():
        print(f"❌ 参照画像が見つかりません: {args.reference}", file=sys.stderr)
        sys.exit(1)

    # 出力ディレクトリを作成
    args.output_dir.mkdir(parents=True, exist_ok=True)

    print(f"🚀 コンポーネント反復改善ワークフロー開始")
    print(f"  コンポーネント: {args.component_name}")
    print(f"  CSS: {args.css}")
    print(f"  参照画像: {args.reference}")

    # ワークフロー実行
    results = run_workflow(
        args.component_name,
        args.css,
        args.reference,
        args.output_dir
    )

    if results.get('success'):
        print("\n✅ ワークフロー完了")
        print(f"\n📂 出力ファイル:")
        print(f"  カタログHTML: {args.output_dir / f'{args.component_name}_catalog.html'}")
        print(f"  現在のスクショ: {args.output_dir / f'{args.component_name}_current.png'}")
        print(f"  差分画像: {args.output_dir / f'{args.component_name}_diff.png'}")
    else:
        print("\n❌ ワークフローが失敗しました", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
