---
allowed-tools: Bash(marp:*), Bash(ls:*), Bash(find:*), Read
argument-hint: [deck-path]
description: Marp CLIを使用してスライドをPDFにエクスポート
---

# MarpスライドをPDFにエクスポート

## 目的

Marpスライド（deck.md）をMarp CLIを使用してPDF形式に変換します。

## コンテキスト

- 利用可能なデッキ: !`find decks -name "deck.md" -type f 2>/dev/null | sed 's|/deck.md||'`
- Marp CLIの確認: !`command -v marp >/dev/null 2>&1 && echo "インストール済み" || echo "未インストール"`

## タスク

1. **デッキパスの決定**
   - 引数が指定された場合: `$1` をデッキパスとして使用
   - 引数がない場合: 利用可能なデッキを一覧表示し、ユーザーに選択肢で求める

2. **デッキの検証**
   - `$1/deck.md` が存在するか確認

3. **PDFへエクスポート**
   以下のコマンドを実行:
   ```bash
   marp $1/deck.md -o $1/deck.pdf --pdf --allow-local-files
   ```

4. **確認と報告**
   - PDFが正常に作成されたことを確認
   - 出力パスとファイルサイズを報告

## エラーハンドリング

- デッキパスが無効な場合: 利用可能なデッキを表示
- deck.mdが存在しない場合: 先にスライドを生成するよう提案
- Marp CLIの実行が失敗した場合: トラブルシューティング手順を提供

## 使用例

```
/export-pdf decks/20260112_sample
```

## 注意事項

- 生成されたPDFは.gitignoreによりGit管理外となります
- ローカル画像を読み込むために `--allow-local-files` フラグが必要です
- 大きなスライドデッキの場合、PDF生成に数秒かかることがあります
