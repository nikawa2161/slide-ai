---
name: pr
description: 現在のブランチ名からGitHub ISSUEの情報を取得し、PRを作成します。コミット完了後に自動的に提案します。
---

現在のブランチ名からGitHub ISSUEの情報を取得し、PRを作成してください。

対象リポジトリ: https://github.com/nikawa2161/<リポジトリ名>

## 実行手順

### 1. ブランチとISSUE番号の確認

以下を並列実行してください:
- `git branch --show-current` で現在のブランチ名を確認
- ブランチ名からISSUE番号を抽出（例: `feature/13` → `13`）

### 2. GitHub ISSUE情報の取得

`gh issue view {ISSUE番号} --json title,body,url` でISSUE情報を取得:
- タイトル: PRのタイトルに使用
- 本文: PRの説明に含める
- URL: PRにリンクを記載

### 3. リモートへのプッシュ

`git push -u origin {ブランチ名}` で最新の変更をリモートリポジトリにプッシュ

### 4. PRテンプレートの準備

`.github/PULL_REQUEST_TEMPLATE.md` を読み込んで、テンプレートの形式を確認してください。

以下の内容でテンプレートを埋める:

- **ISSUEへのリンク**: GitHub ISSUE URL
- **やったこと**: `git log main..HEAD --format="%B"` から取得したコミットメッセージ（絵文字を除いた説明部分）を箇条書き
- **確認手順**: 変更されたファイルタイプに基づいて推奨される確認手順を提案
- **その他**: 必要に応じて特記事項を記載

テンプレートが存在しない場合は、以下の形式で作成:
```
Closes #{ISSUE番号}

## やったこと
- [コミットメッセージから生成]

## 確認手順
- [推奨される確認手順]
```

**重要**: テンプレートファイルが更新された場合は、常に最新の内容を参照すること

### 5. PRの作成

`gh pr create` コマンドを使用してPRを作成:
- **ベースブランチ**: `main`
- **タイトル**: GitHub ISSUEのタイトル
- **本文**: テンプレートに基づいて生成した内容（HEREDOCを使用）

```bash
gh pr create --title "タイトル" --body "$(cat <<'EOF'
[PR本文]
EOF
)" --base main
```

### 6. PR URLの表示

作成されたPR URLをユーザーに表示

## エラーハンドリング

- **ブランチ名にISSUE番号がない場合**: 手動でISSUE番号の入力を求める
- **GitHub ISSUEが取得できない場合**: コミット履歴からPRタイトルを生成して続行
- **プッシュが必要な場合**: プッシュを実行してから再試行
- **PRが既に存在する場合**: 既存PRのURLを表示

## 注意事項

- PRは必ずOpenで作成
- コミットメッセージは絵文字を除いた部分のみを使用
- `git log main..HEAD --format="%B"` で全コミットメッセージ（詳細含む）を取得
- `gh pr create` のHEREDOCでは `'EOF'` とシングルクォートで囲む
- **必ず** `.github/PULL_REQUEST_TEMPLATE.md` を読み込んでテンプレート形式を確認すること
- **重要**: コミットメッセージから `Co-Authored-By:` の行を除外する
- コミット規約は `.claude/skills/commit/SKILL.md` を参照
