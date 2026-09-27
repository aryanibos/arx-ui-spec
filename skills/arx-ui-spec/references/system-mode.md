# System Mode

Use `system` mode when analyzing multiple related screens from the same product or design language.

## Goal

Infer a reusable design system from repeated visual evidence while preserving inconsistencies and uncertainty.

## Workflow

1. Inventory all supplied screens and their viewport classes.
2. Identify shared shell patterns such as sidebar, topbar, page container, content grid, and footer.
3. Cluster repeated colors, spacing values, radii, type roles, control heights, shadows, and icon treatments.
4. Identify repeated semantic components.
5. Separate global patterns from screen-specific exceptions.
6. Detect inconsistencies rather than silently normalizing them.
7. Generate reusable token/component recommendations with confidence.

## Token candidates

### Color

- primary / accent
- primary hover/pressed when shown
- background
- surface
- elevated surface
- border/divider
- text primary/secondary/muted
- success/warning/error/info

### Spacing

Infer a scale only when values cluster meaningfully.

Example:

```text
4 / 8 / 12 / 16 / 24 / 32 / 48 / 64
```

Do not force every measured gap onto a perfect mathematical scale.

### Typography

Look for recurring roles:

- display
- h1/h2/h3
- body large/default/small
- label
- caption
- button
- table header/cell

### Shape and elevation

- border radii
- border widths
- shadows
- overlays
- blur/glass effects

### Controls

- button heights and variants
- input/select/search heights
- checkbox/radio/toggle sizing
- chips/tags
- table rows
- cards
- modals/drawers
- navigation items

## Reusable component rule

A repeated visual pattern is a component candidate when it shares structure and behavior, not merely color.

Good candidates:

- `SidebarNavItem`
- `SearchInput`
- `StatCard`
- `DataTableRow`
- `StatusTag`
- `PrimaryButton`

Avoid meaningless fragmentation such as `GreenRectangle` or `GrayTextBlock`.

## Inconsistency handling

If similar screens show conflicting values:

```text
Input radius appears as ~8px on 6 screens and ~12px on 2 screens.
Status: INCONSISTENT
Likely canonical value: 8px (INFERRED)
Action: confirm whether the 12px examples are intentional variants or design drift.
```

Do not silently rewrite outliers into the majority value.

## Output

System-mode output should include:

- screen inventory
- inferred global tokens
- reusable component catalog
- layout primitives
- component variants
- confidence per token/pattern
- inconsistencies and outliers
- recommended canonicalization only when clearly marked as recommendation, not source fact
