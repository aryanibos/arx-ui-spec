# Output Location & Git Hygiene

ARX UI Spec should keep generated specifications predictable, reviewable, and repository-friendly.

## Project convention wins

Before creating files, inspect the repository for an established documentation or design-spec convention.

Prefer an intentional existing location such as:

```text
docs/design-specs/
docs/design/
product/ui/
specs/ui/
```

when the project already uses it consistently.

Do not create a competing documentation hierarchy without a clear reason.

## Default location

When the project has no relevant convention, use:

```text
docs/ui-specs/{feature-name}/
```

Use semantic `kebab-case` feature names.

Good:

```text
docs/ui-specs/login/
docs/ui-specs/document-upload/
docs/ui-specs/document-preview/
docs/ui-specs/access-permissions/
docs/ui-specs/audit-trail/
```

Avoid source-export naming such as:

```text
docs/ui-specs/US-01/
docs/ui-specs/png-1/
docs/ui-specs/Screen Final 2/
```

The folder should describe product intent, not the original image filename.

## Screen mode

Default:

```text
docs/ui-specs/{feature-name}/
├── design-spec.json
└── design-spec.md
```

## System mode

Default:

```text
docs/ui-specs/design-system/
├── design-system.json
└── design-system.md
```

If the project already has a canonical design-system documentation location, use that instead.

## Compare mode

Keep human-readable QA history near the feature specification:

```text
docs/ui-specs/{feature-name}/
├── design-spec.json
├── design-spec.md
└── qa/
    ├── round-1.md
    ├── round-2.md
    └── round-3.md
```

For a single comparison, `qa/visual-qa.md` is acceptable.

Do not overwrite prior QA rounds when history is useful to the team.

## Generated visual artifacts

Large or reproducible raster artifacts should not pollute normal source history by default.

Put temporary or generated visual artifacts under:

```text
.arx-ui-spec/
```

or, when they belong to a specific feature:

```text
docs/ui-specs/{feature-name}/artifacts/
```

Examples:

- temporary crops
- measurement overlays
- generated diff images
- browser screenshots captured only for comparison
- intermediate visual-analysis files

Do not move or duplicate a user's original tracked design assets into an ignored folder unless necessary.

## Git policy

The specification itself is an engineering/design contract and should be version-controlled by default.

Track:

```text
docs/ui-specs/**/design-spec.json
docs/ui-specs/**/design-spec.md
docs/ui-specs/**/design-system.json
docs/ui-specs/**/design-system.md
docs/ui-specs/**/qa/*.md
```

Ignore only local/reproducible visual artifacts by default:

```gitignore
# ARX UI Spec — generated local artifacts
.arx-ui-spec/
docs/ui-specs/**/artifacts/
```

Do **not** ignore the entire `docs/ui-specs/` directory unless the user or project explicitly treats all generated specifications as disposable local output.

## Automatic `.gitignore` behavior

When ARX UI Spec creates files inside a writable repository and no project rule conflicts:

1. inspect the existing `.gitignore`
2. preserve all existing entries and comments
3. append the managed ARX UI Spec block only when equivalent rules are not already present
4. never duplicate the block
5. never add `docs/ui-specs/` itself to `.gitignore` by default
6. if `.gitignore` does not exist, it may be created with only the narrow generated-artifact rules
7. do not attempt to untrack files that Git already tracks unless the user explicitly asks

Managed block:

```gitignore
# ARX UI Spec — generated local artifacts
.arx-ui-spec/
docs/ui-specs/**/artifacts/
```

If the repository uses a different output root, adapt the artifact ignore rule to that root rather than forcing `docs/ui-specs/`.

## Principle

Version the specification. Ignore the disposable evidence used to derive or verify it.
