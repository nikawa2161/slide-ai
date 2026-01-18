# Vertical Card Component

番号付きで縦に並ぶカードコンポーネント。取り組み事例やステップの説明に最適です。

## ユースケース

- 取り組み事例の紹介
- プロセスのステップ説明
- 実績やアプローチの説明
- 段階的な説明が必要な内容

## 特徴

- グラデーション背景で視認性向上
- 番号バッジ（グラデーション付き）
- ラベル、タイトル、説明文の3階層構造
- 縦方向のフレキシブルレイアウト
- 柔らかい影とボーダー半径

## Marpスライドでの使い方

1. スライドのfront matterでCSSを読み込む:

```markdown
---
marp: true
theme: slide-ai
style: |
  @import url('./themes/components/vertical-card/style.css');
---
```

2. HTMLタグを使用してコンポーネントを配置:

```html
<div class="vertical-cards">
  <div class="vertical-card">
    <div class="vertical-card__number">01</div>
    <div class="vertical-card__content">
      <div class="vertical-card__label">取り組み例</div>
      <div class="vertical-card__title">フィードバックを求めブラッシュアップする</div>
      <div class="vertical-card__description">スクラムを導入し、デザイナー以外のステークホルダーを巻き込みながら、レビュー/フィードバックのサイクルを定着させてきました。</div>
    </div>
  </div>
  <div class="vertical-card">
    <div class="vertical-card__number">02</div>
    <div class="vertical-card__content">
      <div class="vertical-card__label">取り組み例</div>
      <div class="vertical-card__title">本質的な課題やニーズの発見</div>
      <div class="vertical-card__description">ドメインエキスパートや顧客へのヒアリングを通して、現場を知り現実的な課題と課題解決された理想像をつかみます。</div>
    </div>
  </div>
  <div class="vertical-card">
    <div class="vertical-card__number">03</div>
    <div class="vertical-card__content">
      <div class="vertical-card__label">取り組み例</div>
      <div class="vertical-card__title">よりシンプルで無駄をなくしたデザイン制作</div>
      <div class="vertical-card__description">各プロセスのアンチパターンをクリアにし、価値を届けるために必要があるかを考え続けます。</div>
    </div>
  </div>
</div>
```

## カスタマイズ可能な要素

- `vertical-card__number`: 番号バッジ
- `vertical-card__label`: ラベル（小見出し）
- `vertical-card__title`: タイトル
- `vertical-card__description`: 説明文

## デザインのカスタマイズ

CSS変数を使用して色やサイズを調整できます:

```css
.vertical-card {
  --card-bg-start: #f0f4ff;
  --card-bg-end: #fdf5ff;
  --number-bg-start: #667eea;
  --number-bg-end: #764ba2;
  --label-color: #667eea;
  --title-color: #2d3748;
  --description-color: #4a5568;
}
```

## スライド制約への適合

- タイトル: 最大40文字を推奨
- 説明文: 1行あたり最大50文字
- 1スライドあたり最大3つのカードを推奨（視認性の確保）

## プレビュー

コンポーネントの実際の見た目を確認するには:
- 個別プレビュー: `themes/components/vertical-card/index.html`
- 統合カタログ: `themes/components/index.html`

をブラウザで開いてください。
