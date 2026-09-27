# Login UI Specification

## Source

- Mode: `screen`
- Source: `login.png`
- Source quality: raster export
- Hidden Figma metadata: unavailable

## Summary

Minimal centered authentication layout with a light neutral canvas, subtle background decoration, and a single elevated authentication card.

## Component Tree

```text
LoginPage
├── BackgroundDecoration
└── AuthCard
    ├── BrandLogo
    ├── EmailField
    ├── PasswordField
    ├── RememberMe
    └── SubmitButton
```

## Layout

- Viewport: `1440 × 1080` — **EXACT**
- Composition: centered card
- Auth card width: `~496px` — **ESTIMATED**
- Card radius: `~16px` — **ESTIMATED**
- Background: near-white / soft gray — **ESTIMATED**

## Typography

- Primary family: likely Inter or a visually similar grotesk sans — **INFERRED**
- Labels: compact medium-weight UI labels
- Input/button text: regular/medium UI text

The PNG alone does not prove the exact font file or Figma text style.

## Colors

- Primary green: `~#67AD48` — **ESTIMATED**
- Surface: `~#FFFFFF` — **ESTIMATED**
- Primary text: `~#2C3440` — **ESTIMATED**

## Spacing

Repeated visual rhythm is consistent with an approximately 8px-based spacing system — **INFERRED**.

Likely scale:

```text
4 / 8 / 12 / 16 / 24 / 32 / 48 / 64
```

## Responsive Behavior

- Keep the form/card constrained rather than allowing it to stretch full desktop width — **INFERRED**.
- Preserve safe horizontal page padding on narrow viewports — **INFERRED**.
- Exact mobile breakpoint and decorative-background behavior — **UNKNOWN**.

## Implementation Guidance

Use grid/flex centering and max-width constraints. Do not reproduce the screenshot with page-level `left/top` coordinates.

Confirm the exact font, tokens, and mobile behavior from Figma metadata or the product design system when available.
