# Screen Mode

Use `screen` mode when analyzing one design screen, mockup, exported Figma frame, screenshot, or UI reference.

## Goal

Produce an implementation-ready specification for one screen without inventing hidden design metadata.

## Workflow

1. Identify the screen type and purpose.
2. Record known viewport/canvas dimensions.
3. Determine the major layout model.
4. Build a semantic component tree.
5. Estimate or read container sizes, alignment, padding, gaps, and control dimensions.
6. Capture typography hierarchy.
7. Capture colors, borders, radii, shadows, opacity, and decorative effects.
8. Identify assets and icons.
9. Infer only defensible responsive behavior.
10. Generate `design-spec.json` and `design-spec.md`.

## Layout questions

Determine, where evidence supports it:

- centered, split, sidebar, dashboard, grid, stacked, overlay, modal, or shell layout
- primary container width/max-width
- page padding
- column ratios
- alignment anchors
- vertical rhythm
- repeated gaps
- fixed vs fluid regions

## Component questions

For each major component, capture:

- semantic name
- role/type
- parent relationship
- approximate dimensions
- padding/gap
- border/radius
- background/text colors
- typography role
- visible state
- reusable/one-off assessment
- confidence

## Typography

Capture hierarchy rather than guessing only a font name:

- display/hero
- page title
- section title
- body
- label
- input text
- helper text
- button text
- caption

If font family cannot be reliably established, use `UNKNOWN` or a family category such as `grotesk sans-serif`, clearly labeled as inferred.

## Responsive output

When only one viewport exists, describe likely behavior conservatively.

Example:

```text
INFERRED: The authentication card should retain a max-width and center within the viewport.
ESTIMATED: Minimum horizontal page padding appears to be ~24px.
UNKNOWN: Mobile treatment for the decorative background is not shown.
```

## Completion standard

A screen-mode result is complete when another competent frontend developer or coding agent can implement the screen structure and visual system without needing to re-interpret the original screenshot for every decision.
