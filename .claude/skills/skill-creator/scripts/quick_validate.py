#!/usr/bin/env python3
"""
スキルのクイックバリデーションスクリプト - 最小バージョン
"""

import sys
import os
import re
import yaml
from pathlib import Path

def validate_skill(skill_path):
    """スキルの基本的なバリデーション"""
    skill_path = Path(skill_path)

    # SKILL.mdが存在するか確認
    skill_md = skill_path / 'SKILL.md'
    if not skill_md.exists():
        return False, "SKILL.mdが見つかりません"

    # frontmatterを読み取り、検証
    content = skill_md.read_text()
    if not content.startswith('---'):
        return False, "YAMLフロントマターが見つかりません"

    # frontmatterを抽出
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return False, "フロントマター形式が無効です"

    frontmatter_text = match.group(1)

    # YAMLフロントマターをパース
    try:
        frontmatter = yaml.safe_load(frontmatter_text)
        if not isinstance(frontmatter, dict):
            return False, "フロントマターはYAML辞書でなければなりません"
    except yaml.YAMLError as e:
        return False, f"フロントマター内のYAMLが無効です: {e}"

    # 許可されたプロパティを定義
    ALLOWED_PROPERTIES = {'name', 'description', 'allowed-tools', 'metadata'}

    # 予期しないプロパティをチェック（metadata配下のネストされたキーは除外）
    unexpected_keys = set(frontmatter.keys()) - ALLOWED_PROPERTIES
    if unexpected_keys:
        return False, (
            f"SKILL.mdフロントマター内に予期しないキー: {', '.join(sorted(unexpected_keys))}。"
            f"許可されているプロパティ: {', '.join(sorted(ALLOWED_PROPERTIES))}"
        )

    # 必須フィールドをチェック
    if 'name' not in frontmatter:
        return False, "フロントマターに'name'がありません"
    if 'description' not in frontmatter:
        return False, "フロントマターに'description'がありません"

    # nameを抽出して検証
    name = frontmatter.get('name', '')
    if not isinstance(name, str):
        return False, f"nameは文字列でなければなりません（{type(name).__name__}が指定されています）"
    name = name.strip()
    if name:
        # 命名規則をチェック（ハイフンケース：小文字とハイフン）
        if not re.match(r'^[a-z0-9-]+$', name):
            return False, f"name '{name}'はハイフンケース（小文字、数字、ハイフンのみ）である必要があります"
        if name.startswith('-') or name.endswith('-') or '--' in name:
            return False, f"name '{name}'はハイフンで始まる/終わる、または連続したハイフンを含むことはできません"
        # name長をチェック（仕様上の最大64文字）
        if len(name) > 64:
            return False, f"nameが長すぎます（{len(name)}文字）。最大は64文字です。"

    # descriptionを抽出して検証
    description = frontmatter.get('description', '')
    if not isinstance(description, str):
        return False, f"descriptionは文字列でなければなりません（{type(description).__name__}が指定されています）"
    description = description.strip()
    if description:
        # 山括弧をチェック
        if '<' in description or '>' in description:
            return False, "descriptionには山括弧（<または>）を含めることはできません"
        # description長をチェック（仕様上の最大1024文字）
        if len(description) > 1024:
            return False, f"descriptionが長すぎます（{len(description)}文字）。最大は1024文字です。"

    return True, "スキルは有効です！"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使用方法: python quick_validate.py <skill_directory>")
        sys.exit(1)

    valid, message = validate_skill(sys.argv[1])
    print(message)
    sys.exit(0 if valid else 1)
