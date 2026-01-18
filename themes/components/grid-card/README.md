# Grid Card Component

2カラムのグリッドレイアウトで情報を整理するカードコンポーネント。福利厚生や機能一覧の表示に最適です。

## ユースケース

- 福利厚生・制度の一覧
- 機能・サービスの紹介
- 複数項目の並列表示
- カテゴリ別の情報整理

## 特徴

- 2カラムのレスポンシブグリッドレイアウト
- アイコン絵文字とタイトルのヘッダー
- 箇条書きリストによる詳細説明
- 3〜6枚のカードに対応
- シンプルで読みやすいデザイン

## Marpスライドでの使い方

1. スライドのfront matterでCSSを読み込む:

```markdown
---
marp: true
theme: slide-ai
style: |
  @import url('./themes/components/grid-card/style.css');
---
```

2. HTMLタグを使用してコンポーネントを配置:

```html
<div class="grid-cards">
  <div class="grid-card">
    <div class="grid-card__header">
      <span class="grid-card__icon">👨‍💼</span>
      <h3 class="grid-card__title">オフィスワーク補助</h3>
    </div>
    <div class="grid-card__content">
      <ul>
        <li>業務中の労働環境を整え、生産性を高めるために補助手当を支給</li>
        <li>オフィス用品について経費精算が可能</li>
      </ul>
    </div>
  </div>
  <div class="grid-card">
    <div class="grid-card__header">
      <span class="grid-card__icon">👶</span>
      <h3 class="grid-card__title">ベビーシッター補助制度</h3>
    </div>
    <div class="grid-card__content">
      <ul>
        <li>仕事と子育てを両立するための支援制度</li>
        <li>ベビーシッター利用時、割引チケットを提供</li>
      </ul>
    </div>
  </div>
</div>
```

## カスタマイズ可能な要素

- `grid-card__icon`: アイコン絵文字
- `grid-card__title`: タイトル
- `grid-card__content`: コンテンツ（箇条書きリスト）

## 枚数による表示

- 3枚: 左列2枚、右列1枚
- 4枚: 左右2枚ずつ
- 5枚: 左列3枚、右列2枚
- 6枚: 左右3枚ずつ

## デザインのカスタマイズ

CSS変数を使用して色やサイズを調整できます:

```css
.grid-card {
  --card-bg: #f0f4f8;
  --title-color: #2d3748;
  --text-color: #4a5568;
  --icon-size: 1.8em;
}
```

## スライド制約への適合

- タイトル: 最大40文字を推奨
- 箇条書き: 1項目あたり最大50文字
- 1カードあたり最大5項目を推奨
- 1スライドあたり最大6枚のカードを推奨

## アイコンの選び方

効果的な絵文字アイコンの例:

- ビジネス: 👨‍💼 💼 📊 📈 💰
- サポート: 👶 🏠 🍽️ 👥 🤝
- 技術: 🔒 🤖 📱 🔗 💬
- 成果: ⚡ 😊 🎯 🏆 ✨

## プレビュー

コンポーネントの実際の見た目を確認するには:
- 個別プレビュー: `themes/components/grid-card/index.html`
- 統合カタログ: `themes/components/index.html`

をブラウザで開いてください。
