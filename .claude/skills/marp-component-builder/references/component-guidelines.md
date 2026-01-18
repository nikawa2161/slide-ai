# Component Guidelines

Marpスライドコンポーネントの設計ガイドライン

## 命名規則

### BEM (Block Element Modifier) に準拠

- **Block**: `.metric-card`
- **Element**: `.metric-card__title`, `.metric-card__value`
- **Modifier**: `.metric-card--large`, `.metric-card--highlighted`

### 命名パターン

- ケバブケース（kebab-case）を使用
- 意味のある、説明的な名前を付ける
- 略語は避ける（`btn` ではなく `button`）

## コンポーネント構造

### 基本構造

```css
.component-name {
  /* Layout */
  display: flex;
  flex-direction: column;

  /* Spacing */
  padding: var(--space-md);
  margin: var(--space-sm);

  /* Visual */
  background: var(--color-background);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-md);

  /* Typography */
  font-family: var(--font-primary);
  color: var(--color-text);
}
```

### 要素とモディファイア

```css
/* Element */
.component-name__title {
  font-size: var(--font-size-lg);
  font-weight: var(--font-weight-bold);
  margin-bottom: var(--space-sm);
}

/* Modifier */
.component-name--highlighted {
  background: var(--color-accent);
  border: 2px solid var(--color-primary);
}
```

## スライド制約

### 文字数制限

- タイトル: 最大40文字
- 本文: 1行あたり最大50文字
- 1スライドあたり総文字数: 最大500文字

### 行数制限

- 1スライドあたり最大15行

### 画像制限

- 1スライドあたり最大2枚
- 幅最大800px

### レイアウト制限

- 見出しレベル: h1からh3まで
- リスト: 最大3階層
- 表: 1スライドあたり最大1つ

## コンポーネント設計原則

### 1. 再利用性

- 特定のコンテンツに依存しない
- 汎用的なクラス名を使用
- バリエーションはモディファイアで対応

### 2. レスポンシブ

- Marpスライドサイズ（通常16:9）に最適化
- 相対単位（rem, em, %）を使用
- 固定サイズは避ける

### 3. アクセシビリティ

- 十分なコントラスト比を確保
- 読みやすいフォントサイズ
- 色だけに依存しない情報伝達

### 4. パフォーマンス

- 不要なネストを避ける
- セレクタを簡潔に保つ
- CSS変数を活用

## バリエーション設計

### サイズバリエーション

```css
.component--small { /* ... */ }
.component--medium { /* ... */ }
.component--large { /* ... */ }
```

### カラーバリエーション

```css
.component--primary { background: var(--color-primary); }
.component--secondary { background: var(--color-secondary); }
.component--accent { background: var(--color-accent); }
```

### 状態バリエーション

```css
.component--active { /* ... */ }
.component--disabled { /* ... */ }
.component--error { /* ... */ }
```

## 禁則事項

- `!important` の乱用を避ける
- インラインスタイルを使用しない
- ID セレクタの使用を避ける
- 要素セレクタの過度な使用を避ける
- 深いネスト（3階層以上）を避ける
- ブラウザ固有のプレフィックスは最小限に

## テストチェックリスト

- [ ] デザイントークンを使用しているか
- [ ] BEM命名規則に準拠しているか
- [ ] スライド制約を満たしているか
- [ ] 再利用可能な設計になっているか
- [ ] バリエーションが適切に定義されているか
- [ ] 参照画像と一致するか（視覚的テスト）
