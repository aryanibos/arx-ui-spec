# ARX UI Spec

[![Version](https://img.shields.io/badge/version-1.0.0-111827)](https://github.com/aryanibos/arx-ui-spec/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-16a34a.svg)](LICENSE)
[![skills.sh](https://skills.sh/b/aryanibos/arx-ui-spec)](https://skills.sh/aryanibos/arx-ui-spec)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-cross--agent-7c3aed)](https://skills.sh/)
[![Codex Plugin](https://img.shields.io/badge/Codex-plugin-111827)](https://developers.openai.com/plugins/)
[![UI Specification](https://img.shields.io/badge/focus-UI%20specification-2563eb)](#what-arx-ui-spec-does)

> **From visual reference to implementation-ready UI specification.**

**ARX UI Spec** is a cross-agent UI specification skill that turns **Figma exports, PNG/JPG screenshots, product mockups, and implementation screenshots** into structured design specifications that developers and AI coding agents can actually use.

The skill is named **`arx-ui-spec`**.

It extracts and documents layout structure, spacing, typography, colors, radii, component hierarchy, responsive intent, design-system patterns, and visual differences — while clearly separating what is **exact** from what is only **inferred or estimated**.

---

## Why this exists

A PNG can show how a design looks, but it does not directly tell a developer:

- whether a gap is `20px` or `24px`
- whether a card uses Auto Layout
- the actual font family and weight
- the design token behind a color
- whether two similar elements are the same component
- the intended responsive behavior
- whether a browser implementation is visually close enough

`arx-ui-spec` converts that visual evidence into an implementation contract without pretending that screenshot-derived values are exact Figma metadata.

---

## Install

### Global cross-agent install

Install globally so the skill is available across projects:

```bash
npx skills add -g aryanibos/arx-ui-spec
```

This is the recommended install for compatible agent environments such as **Codex, Claude Code, Cursor, OpenCode, Windsurf**, and other Agent Skills-compatible clients.

### Project-only install

```bash
npx skills add aryanibos/arx-ui-spec
```

### Codex plugin marketplace

Add this repository as a Codex marketplace source:

```bash
codex plugin marketplace add aryanibos/arx-ui-spec
```

Then install **ARX UI Spec** from the marketplace/plugin browser.

Useful commands:

```bash
codex plugin marketplace list
codex plugin marketplace upgrade
```

---

## What ARX UI Spec does

ARX UI Spec supports three stable modes.

### 1. `screen` — Single-screen extraction

Analyze one visual reference and produce an implementation-ready specification.

```text
Use arx-ui-spec in screen mode to analyze login.png.
Generate both JSON and Markdown specs.
```

Typical output:

- viewport and canvas
- page layout
- component tree
- dimensions and spacing
- typography hierarchy
- colors and effects
- borders and radii
- icon/image placement
- responsive guidance
- implementation notes
- confidence for every uncertain value

### 2. `system` — Multi-screen design-system inference

Analyze multiple related screens and infer repeated design patterns.

```text
Use arx-ui-spec in system mode on these 8 exported screens.
Infer the shared design system and reusable components.
```

Typical output:

- color tokens
- typography scale
- spacing scale
- radius scale
- shadow/elevation patterns
- repeated components
- layout primitives
- sidebar/header patterns
- form controls
- table/card/tag/button variants
- inconsistent visual patterns that may need designer confirmation

### 3. `compare` — Design vs implementation visual QA

Compare a design reference with a browser/app screenshot.

```text
Use arx-ui-spec in compare mode.
Image A is the design reference.
Image B is the current frontend implementation.
```

Typical output:

- alignment differences
- padding/gap differences
- card/input/button size differences
- typography differences
- color/effect differences
- missing/extra elements
- severity/prioritization
- visual QA verdict

---

## Confidence model

Screenshot analysis is evidence-based estimation, not access to hidden Figma properties.

Every meaningful value should be classified as:

| Confidence | Meaning |
| --- | --- |
| **EXACT** | Directly available from source metadata or explicitly supplied data |
| **INFERRED** | Strongly supported by repeated patterns or visual/system evidence |
| **ESTIMATED** | Approximate value measured or judged from a raster image |
| **UNKNOWN** | The source does not support a reliable value |

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

ARX UI Spec must never silently upgrade an estimate into an exact design fact.

---

## Source priority

When richer source data exists, use it before raster estimation:

```text
Figma node / design metadata
        ↓
Design tokens / variables
        ↓
Existing design-system source
        ↓
CSS / frontend implementation metadata
        ↓
Exported PNG / JPG / screenshot
        ↓
Visual estimation
```

A PNG is a useful fallback, not a substitute for original design metadata.

---

## Output contract

By default, produce both:

```text
design-spec.json
design-spec.md
```

### JSON

The JSON file is the machine-readable contract for coding agents and tooling.

It includes:

```text
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
```

A JSON Schema is included at:

```text
schemas/design-spec.schema.json
```

### Markdown

The Markdown output is optimized for developers, designers, reviewers, and handoff discussions.

It explains:

- screen structure
- major measurements
- reusable patterns
- uncertain values
- implementation guidance
- responsive assumptions
- confirmation questions when source evidence is insufficient

---

## Example component tree

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

ARX UI Spec should describe **semantic layout**, not encourage brittle screenshot tracing with absolute coordinates.

Avoid implementation guidance like:

```css
position: absolute;
left: 457px;
top: 238px;
```

when the same composition should instead be expressed through grid, flexbox, container constraints, gaps, and responsive rules.

---

## Example design tokens

```json
{
  "colors": {
    "primary": {
      "value": "#67AD48",
      "confidence": "ESTIMATED"
    },
    "surface": {
      "value": "#FFFFFF",
      "confidence": "ESTIMATED"
    }
  },
  "spacing": {
    "baseUnit": {
      "value": 8,
      "unit": "px",
      "confidence": "INFERRED"
    },
    "scale": [4, 8, 12, 16, 24, 32, 48, 64]
  }
}
```

---

## Compare-mode example

```text
Visual QA — Login Screen

Card width
Reference: ~496px
Implementation: ~540px
Delta: +44px
Confidence: ESTIMATED
Priority: High

Primary button height
Reference: ~52px
Implementation: ~40px
Delta: -12px
Confidence: ESTIMATED
Priority: Medium

Headline family
Reference: likely Inter / similar grotesk sans
Implementation: Arial
Confidence: INFERRED
Priority: High
```

The goal is not pixel-perfect theater. The goal is to identify the differences that materially affect visual fidelity and UX.

---

## Responsive reasoning

A desktop screenshot does not reveal every breakpoint.

ARX UI Spec may infer likely responsive behavior, but it must label those rules accordingly.

Good:

```text
INFERRED: The centered auth card likely keeps a max-width around 480–520px.
ESTIMATED: Desktop page horizontal padding appears to be about 24px.
UNKNOWN: The source does not show how the illustration behaves below tablet width.
```

Bad:

```text
The mobile breakpoint is exactly 768px.
```

unless the source actually proves it.

---

## Usage examples

### Analyze a Figma PNG export

```text
Use arx-ui-spec in screen mode.
Analyze this Figma export and produce design-spec.json and design-spec.md.
Clearly mark estimated values.
```

### Extract a design system

```text
Use arx-ui-spec in system mode across all attached product screens.
Identify repeated tokens and components, and separate consistent patterns from one-off values.
```

### Compare frontend with design

```text
Use arx-ui-spec in compare mode.
Reference A is the approved design.
Reference B is the current implementation.
Prioritize the mismatches that most affect visual fidelity.
```

### Prepare a handoff for another coding agent

```text
Use arx-ui-spec to turn these screenshots into an implementation contract for another frontend agent.
Do not generate frontend code yet.
```

---

## Repository structure

```text
.
├── skills/
│   └── arx-ui-spec/
│       ├── SKILL.md
│       └── references/
│           ├── confidence-model.md
│           ├── screen-mode.md
│           ├── system-mode.md
│           ├── compare-mode.md
│           ├── output-contract.md
│           └── implementation-guidance.md
│
├── schemas/
│   └── design-spec.schema.json
│
├── examples/
│   └── login-screen/
│       ├── design-spec.json
│       └── design-spec.md
│
├── .agents/
│   └── plugins/
│       └── marketplace.json
│
├── plugins/
│   └── arx-ui-spec/
│       ├── .codex-plugin/
│       │   └── plugin.json
│       └── skills/
│           └── arx-ui-spec/
│               ├── SKILL.md
│               └── references/
│
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── SECURITY.md
└── README.md
```

The root `skills/arx-ui-spec/` path is the cross-agent Agent Skills entrypoint.

The `plugins/arx-ui-spec/` path packages the same behavior as a Codex plugin.

---

## Design principles

**Evidence before confidence.** If the source cannot prove it, do not call it exact.

**Semantic structure before coordinates.** Describe layout systems and components, not screenshot tracing hacks.

**Patterns before one-offs.** Multi-screen analysis should infer tokens only when repetition supports them.

**Implementation-ready output.** Specs should be useful to a developer or coding agent without requiring them to reinterpret the image from scratch.

**Design intent over fake precision.** `~24px ESTIMATED` is better than confidently inventing `23px`.

**Visual QA should prioritize impact.** A wrong primary font or container width matters more than a one-pixel icon offset.

---

## Versioning

Current stable version: **`1.0.0`**

```text
v1.0.x  Backward-compatible fixes and clarifications
v1.x.0  New compatible modes, fields, or analysis capabilities
v2.0.0  Breaking output-contract or behavior changes
```

See [CHANGELOG.md](CHANGELOG.md).

---

## Security & privacy

Screenshots can contain private product information, user data, or credentials.

ARX UI Spec should inspect only the material needed for the task and should never encourage publishing private screenshots or extracted secrets into public repositories.

See [SECURITY.md](SECURITY.md).

---

## Contributing

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

The public contract of `arx-ui-spec` is intentionally strict: contributions should preserve confidence labeling, source precedence, structured outputs, and project-agnostic behavior.

---

## License

MIT © 2026 Arya Isnaidi
