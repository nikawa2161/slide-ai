# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## プロジェクト概要

Claude CodeのAIアシスタントを使用して、MarkdownファイルからMarpスライドを生成するリポジトリです。

## 必須の前提条件

1. VS Code拡張機能「Marp for VS Code」が必要
2. プロジェクト設定（`.vscode/settings.json`）でカスタムテーマを自動読み込み
   - デフォルトテーマ：`slide-ai` (themes/theme.css)
   - パステルカラーで明るく親しみやすいデザイン

## スライド生成ワークフロー

### 入力ファイル
- `decks/<deck>/input.md`に変換対象のMarkdownファイルを配置
- デッキフォルダ名は`YYYYMMDD_タイトル`形式を推奨
- 各デッキは独立したディレクトリで管理される

### スライド生成ルール（shared/rules/slide.md）
Claude Codeで`@slide.md`と`@input.md`をメンションしてスライド生成を指示すると、以下の制約が自動適用される：

**文字数・行数制限**
- タイトル：最大40文字
- 本文：1行あたり最大50文字
- 1スライドあたり総文字数：最大500文字
- 1スライドあたり最大行数：15行
- コードブロック：最大20行/ブロック

**画像ルール**
- 1スライドあたり最大2枚
- 幅最大800px
- 共通画像：`shared/.images/`に配置
- デッキ固有画像：`decks/<deck>/.images/`に配置
- ロゴ画像は必須
- 配置は中央揃えを基本とする

**フォーマット制限**
- 見出しレベル：h1からh3まで
- リスト：最大3階層
- 表：1スライドあたり最大1つ

### スライド生成コマンド
Claude Codeで`shared/rules/slide.md`と`decks/<deck>/input.md`を開き、AIチャットで以下のように指示：
```
@slide.md @input.md を元にスライド生成
```

### 出力ファイル
- 出力先：`decks/<deck>/deck.md`
- テンプレート：`shared/templates/default.md`を基に生成
- PDF出力：`decks/<deck>/deck.pdf`（Git管理外）

### PDF生成

スライドをPDFにエクスポートする方法が3つあります：

1. **Claude Codeカスタムコマンド** (推奨)
   ```
   /export-pdf decks/20260112_sample
   ```

   Marp CLIを使用して自動でPDFを生成します。
   引数なしで実行すると利用可能なデッキ一覧が表示されます。

2. **Marp CLIを直接使用**
   ```bash
   # Marp CLIのインストール（初回のみ）
   npm install -g @marp-team/marp-cli

   # PDF生成
   marp decks/<deck>/deck.md -o decks/<deck>/deck.pdf --pdf --allow-local-files
   ```

3. **VS Code拡張機能（手動）**
   - VS Codeで`deck.md`を開く
   - コマンドパレット（Cmd+Shift+P）→「Marp: Export slide deck」
   - PDF形式を選択して保存

## アーキテクチャとディレクトリ構造

```
.
├── themes/
│   └── theme.css             # カスタムMarpテーマ
├── shared/
│   ├── rules/
│   │   └── slide.md          # スライド生成ルール
│   ├── templates/
│   │   └── default.md        # デフォルトテンプレート
│   └── .images/              # 共通画像（ロゴ、背景など）
│       ├── logo.png
│       └── background.png
├── decks/
│   └── YYYYMMDD_タイトル/     # デッキ単位のフォルダ
│       ├── input.md          # 入力Markdown
│       ├── deck.md           # 生成されたスライド
│       ├── deck.pdf          # 生成されたPDF（Git管理外）
│       └── .images/          # デッキ固有の画像
├── .vscode/
│   └── settings.json         # VS Code設定（テーマ登録）
├── .gitignore                # PDFファイルを除外
├── README.md                 # 使い方ドキュメント
└── CLAUDE.md                 # このファイル
```

## 日本語フォント設定

スライドは以下のフォントを使用：
- 'Hiragino Sans'
- 'Noto Sans CJK JP'

文字化けが発生する場合はシステムのフォント設定を確認すること。

## カスタムテーマ

### テーマの特徴

プロジェクト固有のカスタムテーマ `slide-ai` (themes/theme.css) を使用します：

- **ベース**: Marp defaultテーマ
- **カラースキーム**: パステルカラーで明るく親しみやすい配色
  - プライマリ: スカイブルー (#87ceeb)
  - セカンダリ: ライトピンク (#ffb6c1)
  - アクセント: ゴールド (#ffd700)
  - 背景: フローラルホワイト (#fffaf0)
- **フォント**: Hiragino Sans, Noto Sans CJK JP
- **特殊スタイル**:
  - `<!-- _class: title -->` でタイトルスライド（グラデーション背景）
  - `<!-- _class: section -->` でセクション区切りスライド
  - `.info-box` でインフォメーションボックス
  - `.warning-box` で警告ボックス
  - `.columns` で2カラムレイアウト

### テーマの使用方法

スライド冒頭のfront matterで指定：
```markdown
---
marp: true
theme: slide-ai
---
```

### テンプレートのカスタマイズ

スライドのスタイルをカスタマイズする場合は`themes/theme.css`を編集する。
ただし、`shared/rules/slide.md`で定義された制限を遵守すること。

## 運用ルール

日常的な運用方法や管理手順については、`shared/rules/operations.md`を参照してください。

### 主な運用項目

- デッキの作成と管理方法
- 共通資産（画像、テンプレート）の管理
- Git管理とブランチ戦略
- スライド生成ワークフロー
- トラブルシューティング
- チーム運用のベストプラクティス

詳細は `@shared/rules/operations.md` を参照してください。
