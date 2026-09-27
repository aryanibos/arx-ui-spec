# Figma Link Input

ARX UI Spec may accept a Figma share URL directly so users do not have to manually export a PNG before analysis.

## Goal

Prefer source design information over raster estimation whenever the execution environment can access it.

A Figma URL can point to:

- a whole Figma Design file
- a specific frame or node through `node-id`
- a prototype/share view

Typical file/node URL shape:

```text
https://www.figma.com/design/{file-key}/{file-name}?node-id={node-id}
```

Older or alternate Figma URL forms may use another file-type segment. Parse the file key and node ID from the URL when available instead of depending on the human-readable file name.

## Access order

When given a Figma URL, resolve it using the strongest available source in this order:

1. native Figma connector/MCP/design-context tool available to the agent
2. authenticated Figma REST API access available in the environment
3. directly viewable public Figma share link
4. user-provided export/screenshot as fallback

Do not ask the user to export a PNG when a richer Figma source can already be accessed safely.

## Public links are not authenticated API access

A file shared as `Anyone` / `Anyone with the link` may be viewable in a browser by people outside the owner's organization, subject to the file's sharing/security settings.

However, public browser visibility does **not** mean that the Figma REST API is anonymous. REST API requests require supported authentication.

Therefore:

- use connector/API metadata as `EXACT` only when the environment actually returns that metadata
- do not claim that a public share URL alone exposes hidden Auto Layout, variables, component properties, or other source metadata
- when only the rendered public view is available, apply normal visual confidence rules (`INFERRED`, `ESTIMATED`, `UNKNOWN`)

## Node-targeted links

When `node-id` is present:

- treat that node/frame as the primary analysis target
- preserve the node ID in source metadata when useful
- avoid analyzing unrelated pages/frames unless the selected mode requires broader context

When no node is specified:

- in `screen` mode, identify the most relevant requested frame by name/context when possible
- in `system` mode, inspect the relevant top-level screens/frames that belong to the same product/design system
- if the file contains unrelated work, do not infer a shared system across unrelated sections

## Metadata confidence

Examples of values that may be `EXACT` when returned by Figma source tooling:

- node/frame dimensions
- node hierarchy
- explicit padding/gap values
- layout mode/constraints when surfaced
- text properties
- fill/stroke/effect values
- component/instance relationships
- variables/styles/tokens when surfaced

If a tool returns only part of the metadata, classify unsupported fields independently instead of promoting the entire screen to `EXACT`.

## Restricted or inaccessible links

A Figma URL may still be inaccessible because of:

- `Only invited people` access
- organization-only access
- password protection
- expired/revoked public link
- disabled public sharing
- viewer restrictions
- missing authentication in the execution environment

When blocked:

1. report the access limitation precisely
2. do not attempt to bypass Figma permissions or security controls
3. use another already-available source if one exists
4. otherwise request a viewable link, authorized connector access, or an export/screenshot

## Privacy

Treat Figma URLs as potentially sensitive project resources.

Do not publish private Figma URLs, file keys, node IDs, internal names, screenshots, or extracted proprietary assets into public repositories unless explicitly authorized and necessary.

## Source record

When a Figma URL is the input, record source information in the spec without leaking unnecessary credentials or tokens.

Recommended shape:

```json
{
  "source": {
    "type": "figma-url",
    "access": "connector",
    "fileKey": "<file-key>",
    "nodeId": "<node-id-or-null>",
    "confidence": "EXACT"
  }
}
```

Never store OAuth tokens, personal access tokens, cookies, or secret query parameters in generated specs.

## Core rule

A Figma link is a source pointer, not proof of exact metadata. Use the richest data the environment can legitimately access, and preserve uncertainty for everything else.
