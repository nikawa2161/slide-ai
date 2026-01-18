---
name: marp-component-builder
description: "Marpスライド用のCSSコンポーネントを作成・管理するスキル。モック画像から再現性の高いコンポーネント（.metric-card, .comparison-matrixなど）を生成し、themes/components/で管理。デザイントークン、BEM命名規則、スライド制約（文字数・行数制限）を適用。反復改善ワークフロー（CSS生成→HTML出力→スクショ→画像比較）をサポート。ユーザーが「モック画像からメトリクスカードコンポーネントを作って」「コンポーネントカタログを作成して」などと依頼したときに使用。"
---

# Marp Component Builder

Marpスライド用のCSSコンポーネントライブラリを体系的に管理・生成するスキル。

## 概要

このスキルは、Marpスライドで使用するCSSコンポーネント（例: `.metric-card`, `.comparison-matrix`）を、モック画像から再現性高く生成し、管理することを可能にします。Loglass記事の思想に基づき、`theme.css`を「コンポーネントライブラリ」として育てます。

**主な機能:**
- モック画像からコンポーネントを再現
- デザイントークン（色・余白・影など）に基づく設計
- BEM命名規則の適用
- スライド制約（文字数・行数制限）の遵守
- 反復改善ワークフロー（CSS→HTML→スクショ→比較）
- コンポーネントカタログの自動生成

## ワークフロー決定ツリー

ユーザーのリクエストに応じて、以下のワークフローを選択してください：

1. **新規コンポーネント作成（モック画像から）** → 「モック画像からコンポーネントを作成」セクションへ
2. **既存コンポーネントの改善** → 「反復改善ワークフロー」セクションへ
3. **コンポーネントカタログ生成** → 「カタログ生成」セクションへ
4. **新しいコンポーネントをゼロから設計** → 「ゼロからコンポーネントを設計」セクションへ

## モック画像からコンポーネントを作成

ユーザーが提供したモック画像から、CSSコンポーネントを再現します。

### ステップ1: モック画像の分析

1. ユーザーが提供したモック画像を確認
2. 視覚的要素を分析：
   - レイアウト構造（フレックスボックス、グリッドなど）
   - 色使い（背景色、テキスト色、アクセントカラー）
   - タイポグラフィ（フォントサイズ、太さ、行間）
   - 間隔（padding, margin）
   - ボーダー、影、角丸
3. コンポーネント名を決定（BEM命名規則に従う）

### ステップ2: CSS生成

1. `references/design-tokens.md`のトークンを使用
2. `assets/component-template.css`を参考にCSS構造を作成
3. `references/component-guidelines.md`のガイドラインに従う
4. CSSファイルを`themes/components/[component-name]/index.css`に保存
5. `themes/components/index.html`に新しいコンポーネントのセクションを追加
6. `themes/components/README.md`にコンポーネント説明を追加

**ディレクトリ構造:**
```
themes/components/
├── index.html                    # 統合カタログ（全コンポーネントのプレビュー）
├── [component-name]/
│   ├── index.html                # コンポーネント個別プレビュー
│   ├── style.css                 # CSSファイル
│   └── README.md                 # コンポーネントドキュメント
└── [component-name-2]/
    ├── index.html
    ├── style.css
    └── README.md
```

**ファイル命名規則:**
- **CSSファイル**: `style.css`（従来の`index.css`から変更）
- **プレビューHTML**: `index.html`（各コンポーネントディレクトリ内）
- **ドキュメント**: `README.md`（各コンポーネントディレクトリ内）

**カタログについて:**
- `themes/components/index.html`: 全コンポーネントの実際のデザインをブラウザで確認できる統合カタログ
- `themes/components/[component-name]/index.html`: 個別コンポーネントのプレビュー
- `themes/components/[component-name]/README.md`: コンポーネント個別ドキュメント
- 新しいコンポーネントを追加したら、統合カタログ(`themes/components/index.html`)に追加すること

**CSS生成の原則:**
- デザイントークン（CSS変数）を使用
- BEM命名規則に準拠
- スライド制約を考慮（文字数・行数制限）
- 再利用可能な設計

### ステップ3: 反復改善ワークフロー

1. **カタログMarkdown生成**: `assets/catalog-template.md`を使用してコンポーネントのテストページを作成
2. **HTML生成**: `scripts/generate_catalog.py`でMarp HTMLを出力
3. **スクリーンショット撮影**: `scripts/capture_screenshot.py`でHTMLをキャプチャ
4. **画像比較**: `scripts/compare_images.py`でモック画像と比較
5. **差分確認**: 一致率が95%未満の場合、CSSを調整して再実行

**自動ワークフロー実行:**

```bash
python3 scripts/iterate_component.py [component-name] \
  --css themes/components/[component-name]/index.css \
  --reference [path-to-mock-image] \
  --output-dir catalog
```

これにより、HTML生成→スクショ→比較が一度に実行されます。

### ステップ4: theme.cssへの統合

1. 生成したコンポーネントCSSを`themes/components/[component-name]/`に保存
2. `themes/theme.css`に以下を追加（まだ存在しない場合）:

```css
/* Component imports */
@import 'components/[component-name]/index.css';
```

3. コンポーネントが正しく読み込まれることを確認

## 反復改善ワークフロー

既存のコンポーネントを改善する場合：

1. 現在のCSSファイル（`themes/components/[component-name]/index.css`）を読み込み
2. 改善点を特定（ユーザーフィードバック、参照画像との差分など）
3. CSSを修正
4. 反復ワークフローを実行（ステップ3参照）
5. 一致率が95%以上になるまで繰り返し

## Marpスライドでのコンポーネント使用方法

各コンポーネントをMarpスライドで使用する際の手順：

1. **CSSの読み込み**:
   スライドのfront matterで以下のように指定:
   ```markdown
   ---
   marp: true
   theme: slide-ai
   style: |
     @import url('./themes/components/[component-name]/style.css');
   ---
   ```

2. **HTMLタグの使用**:
   各コンポーネントのREADME.mdに記載されているHTML構造を使用

**例: Vertical Cardコンポーネント**
```html
<div class="vertical-cards">
  <div class="vertical-card">
    <div class="vertical-card__number">01</div>
    <div class="vertical-card__content">
      <div class="vertical-card__label">ラベル</div>
      <div class="vertical-card__title">タイトル</div>
      <div class="vertical-card__description">説明文</div>
    </div>
  </div>
</div>
```

## カタログ管理

全コンポーネントのカタログは`themes/components/`に統合されています。

### カタログファイル

1. **統合HTMLカタログ** (`themes/components/index.html`)
   - 全コンポーネントの実際のデザインをブラウザで確認
   - CSSは直接埋め込み（`:where(section)`を通常のクラスセレクタに変換）
   - 各コンポーネントのセクション構成:
     - 説明とユースケース
     - 複数の実例
     - HTMLコード例
     - カスタマイズ可能な要素

2. **README** (`themes/components/README.md`)
   - テキスト版のコンポーネントドキュメント
   - 使用方法、特徴、デザインガイドラインを記載

### 新しいコンポーネントの追加手順

1. コンポーネントディレクトリを作成: `themes/components/[component-name]/`
2. 以下のファイルを作成:
   - `style.css`: コンポーネントのCSSスタイル
   - `index.html`: プレビューHTML（CSSを読み込み、実例を表示）
   - `README.md`: コンポーネントドキュメント（使い方、特徴、カスタマイズ方法）
3. `themes/components/index.html`（統合カタログ）に新しいセクションを追加:
   - 目次にリンクを追加
   - コンポーネントCSSを`<style>`タグ内に追加
   - HTMLセクション（説明、実例、コード例）を追加

### カタログの確認

```bash
open themes/components/index.html
```

## ゼロからコンポーネントを設計

モック画像がない場合、ゼロからコンポーネントを設計します。

### ステップ1: 要件定義

ユーザーに以下を確認：
- コンポーネントの目的（何を表示するか）
- 必要な要素（タイトル、値、アイコンなど）
- 望ましいスタイル（シンプル、華やか、ミニマルなど）
- バリエーション（サイズ、色など）

### ステップ2: デザイントークンの選択

`references/design-tokens.md`から適切なトークンを選択：
- カラー（primary, secondary, accentなど）
- スペーシング（sm, md, lgなど）
- タイポグラフィ（font-size, font-weightなど）

### ステップ3: CSS実装

`assets/component-template.css`をベースに実装：

1. 基本構造（Block）
2. 子要素（Elements）
3. バリエーション（Modifiers）

### ステップ4: テストとレビュー

1. カタログMarkdownを作成
2. HTMLを生成してプレビュー
3. 必要に応じて調整

## スライド制約の確認

コンポーネント設計時、以下の制約を遵守してください（`shared/rules/slide.md`参照）：

**文字数制限:**
- タイトル: 最大40文字
- 本文: 1行あたり最大50文字
- 1スライドあたり総文字数: 最大500文字

**行数制限:**
- 1スライドあたり最大15行

**画像制限:**
- 1スライドあたり最大2枚
- 幅最大800px

**フォーマット制限:**
- 見出しレベル: h1からh3まで
- リスト: 最大3階層
- 表: 1スライドあたり最大1つ

## ベストプラクティス

1. **デザイントークンの一貫性**: 常に`references/design-tokens.md`のトークンを使用
2. **BEM命名規則**: `.block__element--modifier`の形式を厳守
3. **再利用性**: 特定のコンテンツに依存しない汎用的な設計
4. **レスポンシブ**: 相対単位（rem, em, %）を使用
5. **アクセシビリティ**: 十分なコントラスト比と読みやすいフォントサイズ
6. **反復テスト**: 参照画像との一致率95%以上を目指す

## トラブルシューティング

### Marp CLIが見つからない

```bash
npm install -g @marp-team/marp-cli
```

### Playwrightが見つからない

```bash
pip install playwright
playwright install chromium
```

### 画像比較ツールが見つからない

```bash
pip install Pillow
```

### CSS変数が適用されない

`themes/theme.css`に変数定義があることを確認してください。存在しない場合、`references/design-tokens.md`の定義をCSS変数として追加してください。

## リソース

### scripts/

コンポーネント生成ワークフローを自動化するスクリプト：

- `generate_catalog.py` - カタログMarkdownとHTMLを生成
- `capture_screenshot.py` - HTMLのスクリーンショットを撮影
- `compare_images.py` - 参照画像と生成画像を比較
- `iterate_component.py` - 全ワークフローを一括実行

### references/

コンポーネント設計の指針となるドキュメント：

- `design-tokens.md` - デザイントークン定義（色、スペーシング、タイポグラフィなど）
- `component-guidelines.md` - コンポーネント設計ガイドライン（BEM、制約、禁則事項など）

### assets/

コンポーネント作成のテンプレート：

- `component-template.css` - 新規コンポーネントのCSSテンプレート
- `catalog-template.md` - カタログページのMarkdownテンプレート
