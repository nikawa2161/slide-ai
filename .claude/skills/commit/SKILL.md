---
name: commit
description: 変更を適切な粒度に分割してコミットします。コード変更完了時に自動的に提案します。
---

現在の変更を適切な粒度に分割してコミットしてください。

対象リポジトリ: https://github.com/nikawa2161/blog

## コミットメッセージ規約

### 基本形式

```
<type>: <subject>

[本文]
```

### Type（プレフィックス）

- `feat`: 新機能の追加
- `fix`: バグ修正
- `docs`: ドキュメントのみの変更
- `style`: コードの意味に影響しない変更（空白、フォーマットなど）
- `refactor`: バグ修正や機能追加ではないコードの変更
- `perf`: パフォーマンス改善
- `test`: テストの追加・修正
- `chore`: ビルドプロセスやツールの変更

### Subject（件名）

- 変更の目的を簡潔に記述
- 日本語で記述
- 最大50文字

###　本文

- 変更の理由や背景を説明
- 箇条書きで具体的な変更内容を記載

### 例

```
feat: GitHub ISSUE対応のPRコマンドを追加

- ブランチ名からGitHub ISSUEを取得してPRを作成
- Jira/MCP依存を削除し、gh CLIのみで完結
```


## 実行手順

### 1. 変更内容の確認

以下を並列実行してください:
- `git status` で変更されたファイルを確認
- `git diff` で変更内容を確認

### 2. 変更の分類

変更されたファイルを以下の基準で分類:

#### 関連性による分類
- 同じ機能・目的に関連する変更は1つのコミットにまとめる
- 異なる目的の変更は別々のコミットに分ける

### 3. コミットの実行

各グループごとに以下の形式でコミット:

```bash
git add [ファイル1] [ファイル2] ... && git commit -m "$(cat <<'EOF'
<type>: <subject>

- 変更内容1
- 変更内容2

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
EOF
)"
```

### 4. コミット履歴の表示

完了後、最近のコミットを表示:
```bash
git log --oneline -5
```

## コミット分割の例

### 例1: 新機能とドキュメント更新

**変更ファイル**:
- `.claude/commands/issue.md` (新規)
- `doc/tree-command.md` (更新)
- `CLAUDE.md` (更新)

**分割**:
1. `feat: GitHub ISSUE作成コマンドを追加`
   - `.claude/commands/issue.md`
2. `docs: treeコマンドドキュメントを更新`
   - `doc/tree-command.md`
   - `CLAUDE.md`

### 例2: 複数の独立した修正

**変更ファイル**:
- `src/components/Header.tsx` (バグ修正)
- `src/utils/format.ts` (バグ修正)
- `README.md` (ドキュメント更新)

**分割**:
1. `fix: Headerコンポーネントのレイアウト崩れを修正`
   - `src/components/Header.tsx`
2. `fix: 日付フォーマット関数のタイムゾーン処理を修正`
   - `src/utils/format.ts`
3. `docs: README.mdのセットアップ手順を更新`
   - `README.md`

## 注意事項

- コミットメッセージは日本語で記述
- 1コミットは1つの論理的な変更単位
- 関連する変更は1つのコミットにまとめる
- 無関係な変更は別々のコミットに分ける
- `git commit` のHEREDOCでは `'EOF'` とシングルクォートで囲む
- コミット履歴を確認してから次の作業に進む
