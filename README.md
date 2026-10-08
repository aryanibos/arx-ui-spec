<div align="center">

# ARX UI SPEC

### Visual Specification Engine

**A precise, confidence-aware specification layer for agentic UI development.**

From visual reference to implementation-ready UI specification.

[![Version](https://img.shields.io/badge/version-2.0.0-111827)](https://github.com/aryanibos/arx-ui-spec/releases)
[![commit activity](https://img.shields.io/github/commit-activity/m/aryanibos/arx-ui-spec?label=commit%20activity)](https://github.com/aryanibos/arx-ui-spec/commits/main)
[![issues](https://img.shields.io/github/issues/aryanibos/arx-ui-spec?label=issues)](https://github.com/aryanibos/arx-ui-spec/issues)
[![pull requests](https://img.shields.io/github/issues-pr/aryanibos/arx-ui-spec?label=pull%20requests)](https://github.com/aryanibos/arx-ui-spec/pulls)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-cross--agent-7c3aed)](https://skills.sh/)
[![License](https://img.shields.io/badge/license-ARX%20Source%20Available%201.0-f59e0b.svg)](LICENSE)

</div>

---

**ARX UI Spec** is a cross-agent UI specification skill that turns **direct Figma links, Figma exports, screenshots, product mockups, and implementation screenshots** into structured design specifications that developers and AI coding agents can actually use.

It extracts layout structure, spacing, typography, colors, radii, component hierarchy, responsive intent, design-system patterns, and visual differences while clearly separating what is **exact** from what is only **inferred or estimated**.

---

## Why ARX UI Spec exists

A screenshot can show how a design looks, but it does not directly tell a developer:

- whether a gap is `20px` or `24px`
- whether a frame uses Auto Layout
- the real typography values
- which color comes from a reusable token
- whether repeated elements are the same component
- the intended responsive behavior
- whether the frontend implementation is visually close enough

ARX UI Spec turns visual evidence into an implementation contract without pretending that screenshot-derived values are exact Figma metadata.

---

## Install

### Global cross-agent install

```bash
npx skills add -g aryanibos/arx-ui-spec
```

### Project-only install

```bash
npx skills add aryanibos/arx-ui-spec
```

### Codex plugin marketplace

```bash
codex plugin marketplace add aryanibos/arx-ui-spec
```

Then install **ARX UI Spec** from the Codex plugin browser.

---

## Direct Figma link support

You do **not** have to manually export a PNG first when the agent environment can access the Figma source.

Give the agent a Figma share link or node/frame link directly:

```text
Use arx-ui-spec in screen mode.
Analyze this Figma design directly:
https://www.figma.com/design/FILE_KEY/Product?node-id=123-456

Generate the UI specification for the selected frame.
```

ARX UI Spec resolves a Figma source in this order:

```text
Native Figma connector / MCP / design context
        ↓
Authenticated Figma REST API
        ↓
Directly viewable public Figma share link
        ↓
Figma PNG/JPG export or screenshot
        ↓
Visual estimation
```

A public Figma link may be viewable without a manual export, but public browser visibility does **not** mean the Figma REST API is anonymous. Exact source metadata is only marked `EXACT` when the execution environment actually returns it.

If the environment can only see the rendered public design, values are classified normally as `INFERRED`, `ESTIMATED`, or `UNKNOWN`.

ARX UI Spec never attempts to bypass password protection, organization-only access, invitations, expired links, or other Figma security controls.

---

## Stable modes

### `screen`

Analyze one design screen, Figma node, screenshot, or export.

```text
Use arx-ui-spec in screen mode to analyze this Figma frame.
Generate design-spec.json and design-spec.md.
```

Produces information such as:

- viewport and layout model
- semantic component tree
- dimensions and spacing
- typography hierarchy
- colors and effects
- borders and radii
- assets and icon placement
- responsive guidance
- implementation notes
- confidence per uncertain value

### `system`

Analyze multiple related screens and infer the shared design system.

```text
Use arx-ui-spec in system mode across these product screens.
Infer shared design tokens and reusable components.
```

Typical output includes:

- color tokens
- typography scale
- spacing scale
- radius scale
- shadow/elevation patterns
- control sizes
- layout primitives
- navigation patterns
- form controls
- card/table/tag/button variants
- design inconsistencies requiring confirmation

### `compare`

Compare an approved design against the current implementation.

```text
Use arx-ui-spec in compare mode.
Reference A is the approved design.
Reference B is the current frontend implementation.
```

Typical findings include:

- composition differences
- alignment and spacing mismatch
- incorrect container sizes
- typography mismatch
- component sizing differences
- color/effect mismatch
- missing or extra elements
- visual QA priority and verdict

---

## Confidence model

Every design value must preserve uncertainty.

| Confidence | Meaning |
| --- | --- |
| **EXACT** | Directly available from source metadata or an explicitly supplied value |
| **INFERRED** | Strongly supported by repeated visual/system evidence |
| **ESTIMATED** | Approximate value derived from rendered/raster evidence |
| **UNKNOWN** | Not enough evidence for a reliable value |

Example:

```json
{
  "fontFamily": {
    "value": "Inter",
    "confidence": "INFERRED"
  },
  "cardRadius": {
    "value": 16,
    "unit": "px",
    "confidence": "ESTIMATED"
  }
}
```

A screen can contain mixed confidence. Exact Figma frame dimensions do not automatically make responsive assumptions exact.

---

## Output contract

By default ARX UI Spec produces:

```text
design-spec.json
design-spec.md
```

`design-spec.json` is the machine-readable implementation contract for coding agents and tooling.

`design-spec.md` is the human-readable design handoff for developers, designers, and reviewers.

The repository also includes:

```text
schemas/design-spec.schema.json
```

for machine-readable validation.

---

## Project output location

When a repository already has a UI/design documentation convention, ARX UI Spec follows it.

Otherwise the default is:

```text
docs/ui-specs/{feature-name}/
```

Example:

```text
docs/
└── ui-specs/
    ├── login/
    │   ├── design-spec.json
    │   ├── design-spec.md
    │   └── qa/
    │       ├── round-1.md
    │       └── round-2.md
    │
    └── design-system/
        ├── design-system.json
        └── design-system.md
```

Feature directories use semantic `kebab-case` names such as:

```text
login
document-upload
document-preview
access-permissions
audit-trail
```

not export names such as `US-01` or `png-2`.

---

## Git hygiene

UI specifications are engineering/design contracts and should be committed by default.

Do **not** ignore the entire `docs/ui-specs/` directory.

Temporary visual artifacts belong under:

```text
.arx-ui-spec/
docs/ui-specs/{feature-name}/artifacts/
```

When appropriate, ARX UI Spec may preserve the project's existing `.gitignore` and append:

```gitignore
# ARX UI Spec — generated local artifacts
.arx-ui-spec/
docs/ui-specs/**/artifacts/
```

That means:

```text
design-spec.json   → versioned
design-spec.md     → versioned
qa/round-*.md      → versioned
screenshots/diffs  → local/ignored by default
cache/temp files   → local/ignored by default
```

---

## Semantic component mapping

ARX UI Spec describes the design as product/UI structure rather than screenshot fragments.

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

Implementation guidance should favor grid, flexbox, container constraints, gaps, and reusable components instead of brittle screenshot tracing such as hard-coded absolute coordinates.

---

## Figma metadata behavior

When source tooling exposes Figma metadata, ARX UI Spec can use exact information such as:

- frame/node dimensions
- node hierarchy
- explicit padding and gap
- layout mode or constraints when surfaced
- text properties
- fills, strokes, and effects
- component/instance relationships
- variables/styles/tokens when surfaced

If only part of the metadata is available, unsupported properties keep their own lower confidence instead of inheriting `EXACT` from the entire source.

When a URL contains `node-id`, that node/frame becomes the primary analysis target unless the requested mode requires broader context.

---

## Responsive reasoning

A single desktop screenshot or fixed Figma frame does not prove mobile behavior.

Good:

```text
INFERRED: The auth card likely uses a max-width around 480–520px.
ESTIMATED: Desktop horizontal page padding appears to be about 24px.
UNKNOWN: No source demonstrates behavior below tablet width.
```

Bad:

```text
The mobile breakpoint is exactly 768px.
```

unless source metadata or project code actually supports that claim.

---

## Visual QA priorities

Compare mode uses:

```text
Critical  broken structure or unusable state
High      major layout, typography, component, or brand mismatch
Medium    noticeable spacing, size, color, or effect mismatch
Low       minor cosmetic difference
```

The purpose is not fake pixel-perfect precision. It is to identify differences that materially affect fidelity and UX.

---

## Example workflows

### Figma link → implementation spec

```text
Figma URL
   ↓
ARX UI Spec
   ↓
docs/ui-specs/login/design-spec.json
docs/ui-specs/login/design-spec.md
```

### Multiple screens → design system

```text
Figma screens / exports
   ↓
ARX UI Spec system mode
   ↓
docs/ui-specs/design-system/
```

### Design → frontend → visual QA

```text
Approved design
       ↓
ARX UI Spec
       ↓
Frontend implementation
       ↓
Browser screenshot
       ↓
ARX UI Spec compare
       ↓
docs/ui-specs/{feature}/qa/round-N.md
```

---

## Repository structure

```text
.
├── skills/arx-ui-spec/
│   ├── SKILL.md
│   └── references/
│       ├── confidence-model.md
│       ├── figma-link-input.md
│       ├── screen-mode.md
│       ├── system-mode.md
│       ├── compare-mode.md
│       ├── output-contract.md
│       ├── output-location.md
│       └── implementation-guidance.md
│
├── schemas/
│   └── design-spec.schema.json
│
├── examples/login-screen/
│   ├── design-spec.json
│   └── design-spec.md
│
├── plugins/arx-ui-spec/
│   ├── .codex-plugin/plugin.json
│   └── skills/arx-ui-spec/
│
├── .agents/plugins/marketplace.json
├── .github/workflows/validate.yml
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── NOTICE.md
├── TRADEMARKS.md
├── SECURITY.md
└── README.md
```

The root `skills/arx-ui-spec/` directory is the canonical cross-agent skill.

The Codex plugin packages an intentionally mirrored copy and CI verifies that the canonical and Codex skill definitions stay synchronized.

---

## Design principles

**Evidence before confidence.** If the source cannot prove it, do not call it exact.

**Use richer sources first.** A direct accessible Figma source is better than reconstructing the same screen from a PNG.

**Semantic structure before coordinates.** Describe layout systems and components, not screenshot tracing hacks.

**Patterns before one-offs.** Infer design-system tokens only when repeated evidence supports them.

**Implementation-ready output.** Another developer or coding agent should not need to reinterpret the source from scratch.

**Design intent over fake precision.** `~24px ESTIMATED` is more useful than confidently inventing `23px`.

---

## Versioning

Current stable version: **`2.0.0`**

```text
v2.0.x  Backward-compatible fixes and clarifications
v2.x.0  New compatible inputs, modes, fields, or analysis capabilities
v3.0.0  Breaking behavior, schema, architecture, or distribution changes
```

`2.0.0` is a major release because the project distribution contract changed from MIT to the ARX Source Available License 1.0.

See [CHANGELOG.md](CHANGELOG.md).

---

## License & brand protection

ARX UI Spec `2.0.0` and later is distributed under the **ARX Source Available License 1.0** (`LicenseRef-ARX-Source-Available-1.0`).

You may install and use ARX UI Spec for personal work, education, internal business use, commercial projects, and client work. Generated `design-spec.json`, `design-spec.md`, and visual-QA outputs are not claimed by the ARX license merely because they were produced with ARX UI Spec.

Without written permission, the distributed source may **not** be resold, republished as another standalone skill/plugin, white-labeled, rebranded, or used substantially to create a competing standalone derivative. The **ARX** and **ARX UI Spec** names and associated branding are reserved.

Versions distributed before `2.0.0` remain governed by the license that shipped with those versions.

Read [LICENSE](LICENSE), [NOTICE.md](NOTICE.md), and [TRADEMARKS.md](TRADEMARKS.md) for the complete terms.

> This is a source-available license, not an OSI-approved open-source license.

---

## Security & privacy

Figma URLs and screenshots can point to confidential product work.

ARX UI Spec never stores OAuth tokens, personal access tokens, cookies, or secret query parameters in generated specifications and does not attempt to bypass source permissions.

See [SECURITY.md](SECURITY.md).

---

## Contributing

Contributions are welcome under the project contribution terms. See [CONTRIBUTING.md](CONTRIBUTING.md).

The public contract should preserve source precedence, confidence labeling, structured output, project awareness, provider-neutral behavior, and the project's licensing/brand requirements.

---

## License

**ARX Source Available License 1.0**  
`LicenseRef-ARX-Source-Available-1.0`

Copyright © 2026 Arya Isnaidi.
