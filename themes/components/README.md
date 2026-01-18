# Marp Component Catalog

Marpスライドで使用できるCSSコンポーネントのカタログです。

## 使用方法

各コンポーネントは独立したディレクトリで管理されています：

```
themes/components/
├── metric-card/
│   ├── index.css      # CSSファイル
│   └── index.html     # プレビュー用HTML
└── comparison-table/
    ├── index.css      # CSSファイル
    └── index.html     # プレビュー用HTML
```

### スライドでの使用

1. コンポーネントのCSSは`themes/theme.css`に自動的にインポートされています
2. スライドMarkdownでHTMLとクラスを直接使用できます
3. プレビューは各コンポーネントの`index.html`をブラウザで開いて確認できます

---

## コンポーネント一覧

### 1. Metric Card

**パス**: [metric-card/](./metric-card/)

数値やメトリクスを強調して表示する3カラムのカードコンポーネント。

**ユースケース**:
- KPI（重要業績評価指標）の表示
- プロジェクトの実績数値
- サービスの統計情報
- パフォーマンス指標

**使用例**:
```html
<div class="metric-cards">
  <div class="metric-card">
    <div class="metric-card__value">30<span class="metric-card__unit">種類</span></div>
    <div class="metric-card__title">CSSコンポーネント</div>
    <div class="metric-card__description">再利用可能なレイアウト</div>
  </div>
  <div class="metric-card">
    <div class="metric-card__value">100<span class="metric-card__unit">%</span></div>
    <div class="metric-card__title">会社ブランド準拠</div>
    <div class="metric-card__description">ロゴ・カラー完全対応</div>
  </div>
  <div class="metric-card">
    <div class="metric-card__value">15<span class="metric-card__unit">分</span></div>
    <div class="metric-card__title">生成時間</div>
    <div class="metric-card__description">電車移動で完成</div>
  </div>
</div>
```

**特徴**:
- 3カラムグリッドレイアウト
- 大きく読みやすい数値表示
- 単位、タイトル、説明文の階層構造
- 淡いグレー背景とシャドウ

**カスタマイズ可能**:
- 数値（`metric-card__value`）
- 単位（`metric-card__unit`）
- タイトル（`metric-card__title`）
- 説明文（`metric-card__description`）

---

### 2. Comparison Table

**パス**: [comparison-table/](./comparison-table/)

複数項目を横並びで比較するテーブルコンポーネント。

**ユースケース**:
- AIモデルの機能比較
- 製品スペック比較
- 料金プランの比較
- 機能の有無チェックリスト

**使用例**:
```html
<div class="comparison-table">
  <div class="comparison-table__row comparison-table__row--header">
    <div class="comparison-table__cell comparison-table__cell--label">特徴</div>
    <div class="comparison-table__cell">GPT-4.5</div>
    <div class="comparison-table__cell">Claude 3.7</div>
    <div class="comparison-table__cell">Gemini 2.0</div>
  </div>
  <div class="comparison-table__row">
    <div class="comparison-table__cell comparison-table__cell--label">感情知能</div>
    <div class="comparison-table__cell comparison-table__cell--check">✓</div>
    <div class="comparison-table__cell comparison-table__cell--cross">✗</div>
    <div class="comparison-table__cell comparison-table__cell--cross">✗</div>
  </div>
</div>
```

**特徴**:
- グラデーション背景のヘッダー行
- 左端のラベル列（200px）+ 3つの比較列
- チェックマーク（✓）とバツマーク（✗）の色分け
- 偶数行の背景色で縞模様
- シャドウとボーダーで視認性向上

**モディファイアクラス**:
- `comparison-table__row--header`: ヘッダー行
- `comparison-table__cell--label`: 左端のラベルセル
- `comparison-table__cell--check`: チェックマーク（緑）
- `comparison-table__cell--cross`: バツマーク（赤）

**カスタマイズ可能**:
- ヘッダーのタイトル
- 行のラベル
- セルの内容（テキスト、チェックマーク、バツマーク）

---

## 新しいコンポーネントの追加

新しいコンポーネントを追加する場合は、以下の構成で作成してください：

1. **ディレクトリ作成**: `themes/components/<component-name>/`
2. **CSSファイル**: `themes/components/<component-name>/index.css`
3. **プレビューHTML**: `themes/components/<component-name>/index.html`
4. **テーマ統合**: `themes/theme.css`に`@import`を追加
5. **このREADME更新**: コンポーネント一覧に説明を追加

### テンプレート構造

```
themes/components/
└── <component-name>/
    ├── index.css      # コンポーネントのCSS
    └── index.html     # プレビュー用HTML（複数パターン推奨）
```

## デザインガイドライン

### スライド制約

コンポーネント設計時は以下の制約を考慮してください：

- **文字数制限**: タイトル最大40文字、本文1行最大50文字
- **行数制限**: 1スライドあたり最大15行
- **画像制限**: 1スライドあたり最大2枚、幅最大800px

### 命名規則

BEM（Block Element Modifier）命名規則を使用：

- **Block**: `.component-name`
- **Element**: `.component-name__element`
- **Modifier**: `.component-name--modifier`

### デザイントークン

プロジェクトのカラーパレット（`themes/theme.css`参照）：

- `--color-primary`: #87ceeb (スカイブルー)
- `--color-secondary`: #ffb6c1 (ライトピンク)
- `--color-accent`: #ffd700 (ゴールド)
- `--color-background`: #fffaf0 (フローラルホワイト)

## プレビュー方法

各コンポーネントのプレビューを確認するには：

```bash
# ブラウザで直接開く
open themes/components/metric-card/index.html
open themes/components/comparison-table/index.html
```

または、VS Codeの「Live Server」拡張機能を使用してプレビューできます。
