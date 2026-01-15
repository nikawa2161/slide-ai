# Claude Code to Marp

Claude CodeのAIアシスタントを使用して、MarkdownファイルからMarpスライドを簡単に生成するリポジトリです。

## 前提条件

1. Claude Codeのインストール
2. VS Codeの拡張機能「Marp for VS Code」の追加
3. カスタムテーマ
   - プロジェクト固有のテーマ `slide-ai` を使用
   - `.vscode/settings.json` で自動的に読み込まれます
   - パステルカラーで明るく親しみやすいデザイン
   - 詳細は `themes/theme.css` を参照

## ディレクトリ構造

```
slide-ai/
├── themes/                    # カスタムテーマ
│   └── theme.css             # slide-aiテーマ定義
├── shared/                    # 共通資産
│   ├── rules/
│   │   └── slide.md          # スライド生成ルール
│   ├── templates/
│   │   └── default.md        # デフォルトテンプレート
│   └── .images/              # 共通画像（ロゴ、背景など）
│       ├── logo.png
│       └── background.png
├── decks/                     # スライドデッキ
│   └── YYYYMMDD_タイトル/     # デッキ単位のフォルダ
│       ├── input.md          # 入力Markdown
│       ├── deck.md           # 生成されたスライド
│       ├── deck.pdf          # 生成されたPDF（Git管理外）
│       └── .images/          # デッキ固有の画像
└── .vscode/
    └── settings.json         # VS Code設定（テーマ登録）
```

## 基本的な使い方

1. 入力ファイルの準備
   - `decks/<deck>/input.md`に変換したいMarkdownファイルを配置
   - デッキフォルダ名は`YYYYMMDD_タイトル`形式を推奨

2. スライドの生成
   - Claude Codeで`shared/rules/slide.md`と`decks/<deck>/input.md`を開く
   - Claude CodeのAIチャットに「@slide.md @input.md を元にスライド生成」と指示
   - `shared/rules/slide.md`のルールと`shared/templates/default.md`のテンプレートを参照してスライドが生成されます
   - 出力は`decks/<deck>/deck.md`に保存されます

3. PDFの生成

   **方法1: Claude Codeカスタムコマンド（推奨）**
   ```
   /export-pdf decks/20260112_sample
   ```

   Marp CLIを使用してPDFを自動生成します。
   Marp CLIがインストールされていない場合は、インストール方法が表示されます。

   **方法2: Marp CLI を直接使用**
   ```bash
   marp decks/20260112_sample/deck.md -o decks/20260112_sample/deck.pdf --pdf --allow-local-files
   ```

   **方法3: VS Code拡張機能を手動で使用**
   - Marp for VS Codeで生成された`deck.md`を開く
   - VS Codeのコマンドパレット（Cmd+Shift+P）から「Marp: Export slide deck」を選択
   - PDFは自動的に`.gitignore`で除外されます

## 注意事項

1. 画像の配置
   - 共通画像（ロゴ、背景など）：`shared/.images/`に配置
   - デッキ固有の画像：`decks/<deck>/.images/`に配置

2. スライドのスタイル
   - `shared/templates/default.md`で定義
   - カスタマイズする場合はテンプレートを編集

3. 日本語対応
   - フォントは'Hiragino Sans'と'Noto Sans CJK JP'を使用
   - 文字化けが発生する場合はフォントの確認を

4. Git管理
   - PDFファイルは`.gitignore`で除外されています
   - Markdownファイル（input.md, deck.md）はGit管理されます

## 運用ルール

より詳細な運用方法については、[運用ルール](shared/rules/operations.md)を参照してください。

以下のような情報が含まれています：
- デッキの作成と管理方法
- 共通資産の管理
- Git管理とブランチ戦略
- スライド生成の詳細ワークフロー
- トラブルシューティング
- チーム運用のガイドライン
