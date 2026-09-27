# Compare Mode

Use `compare` mode when a reference design and a current implementation are both available.

## Goal

Produce actionable visual QA findings that prioritize material differences over meaningless pixel noise.

## Required roles

Identify inputs as:

- `reference` — approved design or intended visual target
- `implementation` — current browser/app output

If the role of each image is ambiguous, infer from context when safe; otherwise state the assumption.

## Comparison order

Compare in this order:

1. overall page composition
2. shell/container geometry
3. major component placement and sizing
4. typography hierarchy
5. spacing and alignment
6. controls and component variants
7. colors/borders/radii/effects
8. assets/icons
9. minor cosmetic rendering differences

## Priority model

### Critical

Use only when the screen structure/state is fundamentally wrong or unusable.

Examples:

- missing primary form or content area
- wrong page/state rendered
- severe overlap/clipping

### High

Major mismatch that strongly changes visual fidelity or hierarchy.

Examples:

- wrong primary font family
- substantially wrong content/container width
- missing major panel
- incorrect sidebar/header geometry
- wrong primary brand color

### Medium

Noticeable but localized mismatch.

Examples:

- button/input height
- section spacing
- card radius
- secondary text sizing
- shadow intensity

### Low

Small cosmetic difference with limited perceptual or UX impact.

Examples:

- tiny icon offset
- subtle border-tone variance
- negligible raster antialiasing difference

## Finding format

Each material finding should contain:

- area/component
- expected/reference observation
- implementation observation
- delta or qualitative difference
- confidence
- priority
- recommended correction

Example:

```text
Component: AuthCard
Reference: width ~496px
Implementation: width ~540px
Delta: +44px
Confidence: ESTIMATED
Priority: High
Correction: reduce max-width to approximately the reference range and verify at the same viewport.
```

## False precision rule

When both sources are raster screenshots, do not report arbitrary one-pixel differences as exact unless the image dimensions and measurement method truly support it.

Prefer:

```text
~24px reference gap vs ~32px implementation gap
```

over:

```text
23px vs 31px
```

when the source is visually estimated.

## Verdict

The final verdict should summarize whether the implementation is:

- `MATCH` — no material differences found
- `CLOSE` — minor/medium differences remain
- `NEEDS_ADJUSTMENT` — one or more high-impact differences remain
- `MAJOR_MISMATCH` — composition or screen identity is materially wrong

The verdict is visual QA guidance, not a substitute for accessibility, functional, or browser compatibility testing.
