#!/usr/bin/env python3
"""
画像比較スクリプト

参照画像と生成画像を比較し、差分を可視化します。
"""

import sys
import argparse
from pathlib import Path


def compare_images_pillow(reference_path: Path, generated_path: Path, diff_output: Path) -> dict:
    """PILで画像を比較（基本的な差分検出）"""
    try:
        from PIL import Image, ImageChops, ImageStat

        # 画像を読み込み
        ref_img = Image.open(reference_path).convert('RGB')
        gen_img = Image.open(generated_path).convert('RGB')

        # サイズを合わせる
        if ref_img.size != gen_img.size:
            print(f"⚠️  画像サイズが異なります: {ref_img.size} vs {gen_img.size}")
            gen_img = gen_img.resize(ref_img.size, Image.LANCZOS)

        # 差分を計算
        diff = ImageChops.difference(ref_img, gen_img)

        # 差分を保存
        diff.save(diff_output)

        # 統計情報
        stat = ImageStat.Stat(diff)
        avg_diff = sum(stat.mean) / len(stat.mean)

        result = {
            'average_difference': avg_diff,
            'diff_image': str(diff_output),
            'match_percentage': max(0, 100 - (avg_diff / 255 * 100))
        }

        return result

    except ImportError:
        print("❌ Pillowがインストールされていません", file=sys.stderr)
        print("インストール: pip install Pillow", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"❌ 画像比較エラー: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description='参照画像と生成画像を比較')
    parser.add_argument('reference', type=Path, help='参照画像（モック）')
    parser.add_argument('generated', type=Path, help='生成画像（スクリーンショット）')
    parser.add_argument('--diff-output', '-o', type=Path, help='差分画像の出力パス', required=True)

    args = parser.parse_args()

    # ファイルの存在確認
    if not args.reference.exists():
        print(f"❌ 参照画像が見つかりません: {args.reference}", file=sys.stderr)
        sys.exit(1)

    if not args.generated.exists():
        print(f"❌ 生成画像が見つかりません: {args.generated}", file=sys.stderr)
        sys.exit(1)

    # 出力ディレクトリを作成
    args.diff_output.parent.mkdir(parents=True, exist_ok=True)

    # 画像比較
    print(f"🔍 画像を比較中...")
    result = compare_images_pillow(args.reference, args.generated, args.diff_output)

    print(f"\n📊 比較結果:")
    print(f"  一致率: {result['match_percentage']:.2f}%")
    print(f"  平均差分: {result['average_difference']:.2f}")
    print(f"  差分画像: {result['diff_image']}")

    if result['match_percentage'] >= 95:
        print("\n✅ 高い一致率です！")
    elif result['match_percentage'] >= 80:
        print("\n⚠️  改善の余地があります")
    else:
        print("\n❌ 大きな差分があります。CSS調整が必要です")


if __name__ == '__main__':
    main()
