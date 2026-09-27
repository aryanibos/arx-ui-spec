# Output Contract

ARX UI Spec produces two complementary artifacts by default.

## `design-spec.json`

Machine-readable contract for coding agents, automation, and validation.

Recommended top-level fields:

```text
schemaVersion
mode
metadata
source
viewport
layout
componentTree
components
tokens
responsive
implementationGuidance
confidenceSummary
compare
```

Only include `compare` in compare mode.

### Measurement shape

Use this shape when uncertainty matters:

```json
{
  "value": 496,
  "unit": "px",
  "confidence": "ESTIMATED",
  "note": "Measured from the raster export."
}
```

For exact source values, a note is optional.

### Stable values

Use uppercase confidence values:

```text
EXACT
INFERRED
ESTIMATED
UNKNOWN
```

Compare priorities:

```text
Critical
High
Medium
Low
```

Compare verdicts:

```text
MATCH
CLOSE
NEEDS_ADJUSTMENT
MAJOR_MISMATCH
```

## `design-spec.md`

Human-readable handoff.

Recommended structure:

```text
# <Screen/System> UI Specification

## Source
## Summary
## Component Tree
## Layout
## Components
## Typography
## Colors & Effects
## Spacing & Sizing
## Responsive Behavior
## Implementation Guidance
## Confidence & Ambiguities
## Designer Confirmation
```

For compare mode, replace component implementation sections with:

```text
## Visual QA Summary
## Findings
## Priority Breakdown
## Recommended Corrections
## Verdict
```

## Output quality rules

1. Keep JSON valid and parseable.
2. Do not use comments inside JSON.
3. Keep field naming stable across screens.
4. Record uncertainty near the value it affects.
5. Avoid excessive one-off fields when a reusable structure works.
6. Markdown should explain the design, not simply duplicate every JSON field.
7. If a field cannot be established, use `UNKNOWN` or omit it when truly irrelevant; never fabricate a value to fill the schema.
