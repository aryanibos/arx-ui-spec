# Changelog

All notable changes to ARX UI Spec are documented here.

The project follows Semantic Versioning.

## [1.1.0] - 2026-09-27

### Added

- Direct Figma share URL input without requiring users to manually export PNG/JPG first.
- Figma file-key and `node-id` aware source handling.
- Source resolution order that prefers native Figma connector/MCP/design-context tooling, then authenticated Figma REST API, then directly viewable public links, with raster exports as fallback.
- Explicit distinction between public browser visibility and authenticated Figma REST API access.
- Figma URL privacy rules that prevent credentials, tokens, cookies, or secret query parameters from being written into generated specs.
- Project-aware default output location under `docs/ui-specs/{feature-name}/`.
- Repository hygiene rules that version design specifications while ignoring only temporary generated visual artifacts.

### Changed

- Source precedence now includes directly viewable rendered designs before raster-export fallback.
- Skill descriptions and Codex plugin metadata now advertise Figma-link input support.

## [1.0.0] - 2026-09-27

### Added

- Initial stable public release of `arx-ui-spec`.
- Cross-agent Agent Skills packaging.
- Codex plugin and marketplace packaging.
- `screen` mode for single-screen UI specification extraction.
- `system` mode for multi-screen design-system inference.
- `compare` mode for design-vs-implementation visual QA.
- Four-level confidence model: `EXACT`, `INFERRED`, `ESTIMATED`, `UNKNOWN`.
- Source-precedence rules favoring source metadata over raster estimation.
- Machine-readable `design-spec.json` output contract.
- Human-readable `design-spec.md` handoff contract.
- JSON Schema for stable machine-readable output.
- Reference implementation guidance and example login specification.
- Privacy and contribution guidelines.
