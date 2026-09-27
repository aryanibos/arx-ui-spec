# Implementation Guidance

ARX UI Spec describes implementation intent without forcing a frontend stack.

## Prefer semantic layout

Recommend layout concepts such as:

- constrained page container
- centered max-width card
- grid columns
- flex rows/stacks
- consistent gap tokens
- sticky/fixed navigation only when visually supported
- fluid width with min/max constraints

Avoid copying screenshot coordinates into production layout unless the composition is intentionally fixed.

## Existing projects

When a repository is available, inspect and respect:

- existing component library
- design tokens / CSS variables
- typography setup
- styling approach
- responsive breakpoints
- accessibility primitives
- icon library
- route/page conventions

Prefer reuse over creating visually duplicate components.

## New implementations

If no project conventions exist, provide framework-neutral guidance first.

Example:

```text
Use a centered container with max-width ~496px (ESTIMATED), horizontal viewport padding ~24px (ESTIMATED), and vertical centering via normal layout rather than absolute coordinates.
```

## Accessibility boundary

Visual analysis can identify visible contrast or state concerns, but it cannot prove semantic accessibility.

Recommend validating separately:

- keyboard navigation
- focus visibility
- labels and accessible names
- semantic controls
- contrast ratios using actual color values
- reduced motion
- screen reader behavior

## Assets

Distinguish between:

- content imagery
- brand assets
- icons
- decorative background
- data visualization

Do not recommend recreating a logo or proprietary illustration with CSS when an approved source asset should be used.

## Responsive implementation

Translate visual intent into constraints rather than arbitrary per-device coordinates.

Example:

```text
Desktop: centered card, max-width ~496px.
Tablet: preserve max-width; reduce outer whitespace.
Mobile: likely full available width with safe page padding; exact mobile treatment UNKNOWN because no mobile reference was supplied.
```

## Avoid

- fake precision
- unnecessary absolute positioning
- adding libraries solely to reproduce simple layout
- inventing hidden states
- inventing breakpoints
- replacing project tokens with new values without evidence
- generating code before the user asks when the task is specification-only
