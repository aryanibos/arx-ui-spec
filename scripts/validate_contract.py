#!/usr/bin/env python3
"""Repository contract checks for ARX UI Spec v2.0.0."""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SKILL_VERSION = "2.0.0"
CONFIDENCE_VALUES = {"EXACT", "INFERRED", "ESTIMATED", "UNKNOWN"}


def load_json(path: Path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def count_confidence(node) -> Counter:
    counts: Counter = Counter()
    if isinstance(node, dict):
        for key, value in node.items():
            if key == "confidence" and value in CONFIDENCE_VALUES:
                counts[value.lower()] += 1
            elif key != "confidenceSummary":
                counts.update(count_confidence(value))
    elif isinstance(node, list):
        for value in node:
            counts.update(count_confidence(value))
    return counts


def validate_json_files() -> None:
    for path in sorted(ROOT.rglob("*.json")):
        load_json(path)
        print(f"valid json: {path.relative_to(ROOT)}")


def validate_schema_and_examples() -> None:
    schema_path = ROOT / "schemas/design-spec.schema.json"
    schema = load_json(schema_path)
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)

    source_types = schema["properties"]["source"]["properties"]["type"]["enum"]
    if "figma-url" not in source_types:
        fail("schema source.type must include figma-url")

    default_version = schema["properties"]["metadata"]["properties"]["skillVersion"].get("default")
    if default_version != EXPECTED_SKILL_VERSION:
        fail(f"schema skillVersion default is {default_version!r}, expected {EXPECTED_SKILL_VERSION!r}")

    examples = sorted((ROOT / "examples").glob("*/design-spec.json"))
    if not examples:
        fail("no design-spec.json examples found")

    for path in examples:
        document = load_json(path)
        errors = sorted(validator.iter_errors(document), key=lambda error: list(error.path))
        if errors:
            for error in errors:
                location = ".".join(str(part) for part in error.path) or "<root>"
                print(f"SCHEMA ERROR {path.relative_to(ROOT)} {location}: {error.message}", file=sys.stderr)
            raise SystemExit(1)

        actual_version = document.get("metadata", {}).get("skillVersion")
        if actual_version != EXPECTED_SKILL_VERSION:
            fail(f"{path.relative_to(ROOT)} skillVersion is {actual_version!r}")

        expected_summary = {name: 0 for name in ("exact", "inferred", "estimated", "unknown")}
        expected_summary.update(count_confidence(document))
        actual_summary = document.get("confidenceSummary", {})
        if actual_summary != expected_summary:
            fail(
                f"{path.relative_to(ROOT)} confidenceSummary mismatch: "
                f"declared={actual_summary}, counted={expected_summary}"
            )
        print(f"schema-valid example: {path.relative_to(ROOT)}")


def validate_version_consistency() -> None:
    plugin = load_json(ROOT / "plugins/arx-ui-spec/.codex-plugin/plugin.json")
    version = plugin.get("version")
    if version != EXPECTED_SKILL_VERSION:
        fail(f"Codex plugin version is {version!r}, expected {EXPECTED_SKILL_VERSION!r}")


def validate_skill_entrypoint() -> None:
    skill_path = ROOT / "skills/arx-ui-spec/SKILL.md"
    text = skill_path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, flags=re.DOTALL)
    if not match:
        fail("SKILL.md is missing YAML frontmatter")

    frontmatter = match.group(1)
    if not re.search(r"^name:\s*arx-ui-spec\s*$", frontmatter, flags=re.MULTILINE):
        fail("SKILL.md frontmatter name must be arx-ui-spec")
    description_match = re.search(r"^description:\s*(.+)$", frontmatter, flags=re.MULTILINE)
    if not description_match or "Use when" not in description_match.group(1):
        fail("SKILL.md description must explain when to use the skill")

    references = re.findall(r"`(references/[^\`]+\.md)`", text)
    for relative in sorted(set(references)):
        if not (skill_path.parent / relative).is_file():
            fail(f"SKILL.md references missing file: {relative}")


def main() -> None:
    validate_json_files()
    validate_schema_and_examples()
    validate_version_consistency()
    validate_skill_entrypoint()
    print("ARX UI Spec contract validation passed.")


if __name__ == "__main__":
    main()
