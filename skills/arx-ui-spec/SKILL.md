---
name: arx-ui-spec
description: Cross-agent UI specification skill for analyzing Figma links, Figma exports, screenshots, and visual references into implementation-ready UI specs, design tokens, component maps, and visual QA guidance. Use when the user asks to specify one UI screen, infer a shared design system from multiple screens, or compare an approved design against an implementation.
---

# ARX UI Spec

ARX UI Spec converts visual UI evidence into structured, implementation-ready specifications without pretending that screenshot-derived values are exact source metadata.

## Stable modes

Use exactly one primary mode unless the user explicitly asks for a combined workflow.

### `screen`
Analyze one UI reference and produce a screen-level implementation contract.

### `system`
Analyze multiple related screens and infer repeated design-system patterns.

### `compare`
Compare an approved design reference against an implementation screenshot and report material visual mismatches.

If the user does not name a mode, infer it from the task:

- one design image or one target Figma node → `screen`
- multiple related design screens/frames → `system`
- design/reference + implementation → `compare`

## Supported input sources

Accept whichever source the user already has when the environment can access it safely:

- Figma share URL
- Figma node/frame URL
- Figma connector/MCP/design-context source
- Figma export (`PNG`, `JPG`, or similar)
- product screenshot or mockup
- implementation screenshot
- existing design-token or frontend source in the repository

Do not force a manual PNG export when a Figma link or richer source is already accessible.

## Figma URL ingestion

When the user supplies a Figma link, parse the file key and `node-id` when available and resolve the design through the richest legitimate source available.

Use this access order:

1. native Figma connector/MCP/design-context tooling available to the agent
2. authenticated Figma REST API access available in the environment
3. directly viewable public Figma share link
4. user-provided export/screenshot as fallback

A public Figma link may be viewable without a manual export, but browser visibility is not anonymous REST API access. Do not claim hidden Figma metadata unless the environment actually returns it.

If only the rendered public view is accessible, classify values using the normal confidence model rather than marking them `EXACT`.

When a link is restricted, password-protected, organization-only, expired, or otherwise inaccessible, report the limitation and use another already-available source. Do not bypass Figma access controls.

Follow `references/figma-link-input.md` for detailed URL behavior.

## Source precedence

Use the richest trustworthy source available, in this order:

1. Figma node/design metadata or equivalent source-design metadata
2. design tokens or variables
3. existing project design-system source
4. CSS/frontend implementation metadata
5. directly viewable rendered design
6. exported PNG/JPG/screenshot
7. visual estimation

Never use visual estimation to overwrite richer exact metadata.

## Confidence contract

Classify uncertain design facts using only:

- `EXACT` — directly supported by metadata, explicit source values, or known dimensions
- `INFERRED` — strongly supported by repeated patterns or system evidence
- `ESTIMATED` — approximate value derived from raster/visual measurement
- `UNKNOWN` — insufficient evidence for a reliable value

Do not silently convert an inferred or estimated value into an exact value.

A source may contain mixed confidence. For example, a Figma connector may provide exact frame dimensions while leaving responsive behavior unknown.

## Analysis priorities

Prioritize information that materially helps implementation:

1. screen composition and layout model
2. semantic component hierarchy
3. container widths, alignment, padding, gaps, and density
4. typography hierarchy and likely font attributes
5. colors, borders, radii, shadows, opacity, and effects
6. repeated components and likely variants
7. assets, icons, and imagery placement
8. responsive behavior that is actually supported by evidence
9. implementation constraints and avoidances
10. unresolved ambiguities that require designer confirmation

## Semantic layout rule

Prefer semantic layout descriptions over screenshot tracing.

Recommend grid, flexbox, container constraints, max-widths, gaps, and responsive rules when appropriate.

Do not encourage brittle implementation patterns such as hard-coded absolute screen coordinates unless the source clearly represents an intentionally fixed-position visual composition.

## Component tree

Represent the screen as a semantic component hierarchy whenever useful.

Example:

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

Component names should describe product/UI responsibility rather than arbitrary visual fragments.

## Token inference

In `system` mode, infer a token only when repeated evidence supports it.

Good candidates:

- primary/secondary/surface/text colors
- spacing scale
- typography scale
- radius scale
- shadows/elevation
- control heights
- page/container widths
- recurring component variants

If screens conflict, report the conflict rather than averaging values into a fake standard.

## Responsive reasoning

A single desktop screenshot or Figma frame does not prove mobile behavior or exact breakpoints.

When responsive behavior is not directly shown:

- label plausible behavior as `INFERRED`
- label approximate measurements as `ESTIMATED`
- use `UNKNOWN` when the source does not support a reliable conclusion

Never invent an exact breakpoint from a single raster image or single fixed-size Figma frame.

## Compare mode

In `compare` mode:

1. establish which image/source is the approved reference
2. establish which image/source is the implementation
3. compare major composition before minor details
4. report material mismatches with evidence
5. prioritize by visual/UX impact
6. avoid overstating pixel precision when working from screenshots

Use priorities:

- `Critical` — broken/incorrect screen structure or unusable state
- `High` — major layout, typography, component, or brand mismatch
- `Medium` — noticeable spacing, sizing, control, color, or effect mismatch
- `Low` — small cosmetic difference with limited perceptual impact

Do not fail a screen solely for negligible raster/rendering differences.

## Output

By default, produce both:

- `design-spec.json` — machine-readable implementation contract
- `design-spec.md` — human-readable handoff

Follow `references/output-contract.md` and the repository schema when available.

If the environment cannot create files, present equivalent structured content in the response.

## Output location & repository hygiene

When writing artifacts into a repository, inspect the project's existing documentation convention first.

If no relevant convention exists, use:

```text
docs/ui-specs/{feature-name}/
```

Use semantic `kebab-case` feature names such as `login`, `document-upload`, or `access-permissions` rather than source-export names such as `US-01` or `png-1`.

Default screen output:

```text
docs/ui-specs/{feature-name}/
├── design-spec.json
└── design-spec.md
```

Default system output:

```text
docs/ui-specs/design-system/
├── design-system.json
└── design-system.md
```

Keep compare history under the feature. Each comparison round should preserve both a machine-readable JSON result and a human-readable Markdown report, for example `qa/round-1.json` + `qa/round-1.md`, then `qa/round-2.json` + `qa/round-2.md`. Do not overwrite prior rounds when history is useful.

The specification is an engineering/design contract and should be version-controlled by default. Do not ignore the entire `docs/ui-specs/` directory.

Put temporary or reproducible visual artifacts under `.arx-ui-spec/` or `docs/ui-specs/{feature-name}/artifacts/` and ignore only those local artifacts.

When the repository is writable and no project rule conflicts, preserve the existing `.gitignore` and append this block only if equivalent rules are not already present:

```gitignore
# ARX UI Spec — generated local artifacts
.arx-ui-spec/
docs/ui-specs/**/artifacts/
```

Do not duplicate rules, do not remove existing ignore entries, and do not attempt to untrack already tracked files unless explicitly requested.

Follow `references/output-location.md` for the complete location and Git policy.

## JSON behavior

Prefer stable field names and explicit confidence fields.

Do not store unsupported claims as plain facts.

Apply confidence to extracted or inferred design facts where uncertainty is material. Semantic identifiers such as component names or role labels do not need confidence wrappers unless the identifier itself is uncertain.

For uncertain measurements, include confidence and optionally a note or range.

Example:

```json
{
  "width": {
    "value": 496,
    "unit": "px",
    "confidence": "ESTIMATED",
    "note": "Measured from the raster export."
  }
}
```

When the source is a Figma URL, record only non-secret source identifiers that are useful for traceability. Never store OAuth tokens, personal access tokens, cookies, or secret query parameters in generated specs.

## Markdown behavior

The Markdown output should be concise enough for implementation but complete enough that another developer or coding agent does not need to reinterpret the visual reference from scratch.

Include:

- source and mode
- screen summary
- component tree
- layout specification
- typography
- colors/effects
- spacing/sizing
- reusable components/tokens where relevant
- responsive notes
- implementation guidance
- confidence/ambiguity notes
- designer confirmation questions only where materially useful

## Project awareness

When analyzing an existing repository, inspect its established design system, component library, styling conventions, framework, and tokens before recommending implementation details.

Project conventions override generic preferences when they are intentional and safe.

Do not impose React, Tailwind, CSS Modules, shadcn, Material UI, or any other framework/library unless the project or user chooses it.

## Visual evidence limitations

Raster images and rendered public views cannot reliably reveal every hidden source property, including:

- hidden Auto Layout configuration when metadata is unavailable
- true Figma constraints when metadata is unavailable
- component properties/variants when metadata is unavailable
- exact font family if visually ambiguous
- invisible spacing tokens
- exact breakpoints not shown
- interactions, hover/focus states, or animation not depicted

Report those limitations when they materially affect implementation.

## Privacy

Treat UI screenshots and Figma links as potentially confidential.

Do not copy private screenshots, Figma URLs/file keys/node IDs, credentials, personal information, internal URLs, access tokens, or proprietary assets into public outputs unless explicitly authorized and necessary.

## Reference files

Use these repository references when present:

- `references/confidence-model.md`
- `references/figma-link-input.md`
- `references/screen-mode.md`
- `references/system-mode.md`
- `references/compare-mode.md`
- `references/output-contract.md`
- `references/output-location.md`
- `references/implementation-guidance.md`

## Core principle

Turn visual evidence into a useful engineering contract while preserving uncertainty. Accuracy is not pretending to know more than the source can prove.
