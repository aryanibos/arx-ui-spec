# Contributing to ARX UI Spec

Thanks for helping improve ARX UI Spec.

## Public contract

Contributions must preserve these guarantees unless a major version intentionally changes them:

1. visual estimates are never presented as exact source metadata
2. confidence uses `EXACT`, `INFERRED`, `ESTIMATED`, or `UNKNOWN`
3. richer source metadata outranks screenshot estimation
4. screen, system, and compare modes remain project-agnostic
5. outputs favor semantic layout over brittle coordinate tracing
6. JSON output remains machine-readable and compatible with the published schema for the current major version
7. existing project conventions are respected when available

## Changes

For non-trivial behavior changes, include:

- problem being solved
- expected behavior
- examples
- compatibility impact
- schema impact, if any

## Versioning

- patch: fixes/clarifications without contract changes
- minor: backward-compatible capabilities or fields
- major: breaking behavior/schema/output changes

## Skill mirror

`skills/arx-ui-spec/` is the canonical skill source.

The Codex plugin mirror under `plugins/arx-ui-spec/skills/arx-ui-spec/` must remain byte-for-byte equivalent for `SKILL.md` and reference files.

## Style

Keep instructions explicit, evidence-oriented, and tool/framework-neutral unless a task provides project-specific context.
