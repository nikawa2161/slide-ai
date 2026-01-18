# Design Tokens

Marpコンポーネント用のデザイントークン定義

## Color Tokens

### Primary Colors
- `--color-primary`: スカイブルー (#87ceeb)
- `--color-secondary`: ライトピンク (#ffb6c1)
- `--color-accent`: ゴールド (#ffd700)

### Neutral Colors
- `--color-background`: フローラルホワイト (#fffaf0)
- `--color-text`: ダークグレー (#333333)
- `--color-text-muted`: ミディアムグレー (#666666)

### Semantic Colors
- `--color-success`: ミントグリーン (#98d8c8)
- `--color-warning`: ピーチ (#ffcba4)
- `--color-error`: コーラル (#ff6b6b)
- `--color-info`: ライトブルー (#a8dadc)

## Spacing Tokens

- `--space-xs`: 0.25rem (4px)
- `--space-sm`: 0.5rem (8px)
- `--space-md`: 1rem (16px)
- `--space-lg`: 1.5rem (24px)
- `--space-xl`: 2rem (32px)
- `--space-2xl`: 3rem (48px)

## Typography Tokens

### Font Families
- `--font-primary`: 'Hiragino Sans', 'Noto Sans CJK JP', sans-serif

### Font Sizes
- `--font-size-xs`: 0.75rem (12px)
- `--font-size-sm`: 0.875rem (14px)
- `--font-size-base`: 1rem (16px)
- `--font-size-lg`: 1.25rem (20px)
- `--font-size-xl`: 1.5rem (24px)
- `--font-size-2xl`: 2rem (32px)
- `--font-size-3xl`: 2.5rem (40px)

### Font Weights
- `--font-weight-normal`: 400
- `--font-weight-medium`: 500
- `--font-weight-bold`: 700

## Border Radius Tokens

- `--radius-sm`: 0.25rem (4px)
- `--radius-md`: 0.5rem (8px)
- `--radius-lg`: 1rem (16px)
- `--radius-full`: 9999px

## Shadow Tokens

- `--shadow-sm`: 0 1px 2px rgba(0, 0, 0, 0.05)
- `--shadow-md`: 0 4px 6px rgba(0, 0, 0, 0.1)
- `--shadow-lg`: 0 10px 15px rgba(0, 0, 0, 0.1)
- `--shadow-xl`: 0 20px 25px rgba(0, 0, 0, 0.15)

## Usage in Components

コンポーネントCSSでは、これらのトークンを使用してください：

```css
.my-component {
  color: var(--color-text);
  background: var(--color-background);
  padding: var(--space-md);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-md);
  font-family: var(--font-primary);
}
```
