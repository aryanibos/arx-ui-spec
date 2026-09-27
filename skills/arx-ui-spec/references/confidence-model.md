# Confidence Model

ARX UI Spec uses four confidence levels to prevent screenshot-derived assumptions from being presented as source truth.

## EXACT

Use `EXACT` only when the value is directly available from trustworthy source data.

Examples:

- Figma node width from source metadata
- explicit `font-size: 16px` in project CSS
- viewport dimensions supplied by the user
- token value read from a design token file

Do not use `EXACT` merely because a screenshot measurement looks obvious.

## INFERRED

Use `INFERRED` when multiple pieces of evidence strongly support a conclusion, but the original source value is not available.

Examples:

- repeated 8px-like spacing suggests an 8px base unit
- the same green appears across buttons, active states, and links and is likely the primary color
- repeated card geometry suggests a shared component
- typography closely matches a project font already declared in the codebase

An inference should be explainable.

## ESTIMATED

Use `ESTIMATED` for approximate values measured or visually judged from raster images.

Examples:

- card width around 496px
- input height around 48px
- border radius around 12px
- approximate color sampled from an exported PNG

Prefer useful rounded values or ranges over fake single-pixel precision.

## UNKNOWN

Use `UNKNOWN` when the source cannot support a reliable conclusion.

Examples:

- exact mobile breakpoint when only a desktop screenshot exists
- hidden Auto Layout direction when visual structure is ambiguous
- exact font family with no source metadata and several plausible matches
- hover state not shown in any source

Unknown is a valid engineering result.

## Confidence rules

1. Richer source metadata always outranks visual estimation.
2. Repeated evidence may upgrade `ESTIMATED` to `INFERRED`, but not to `EXACT` without source proof.
3. Do not average conflicting screens into a false token.
4. When precision is uncertain, prefer a range such as `~20–24px`.
5. If a value is implementation-critical and uncertain, surface it for designer confirmation.
