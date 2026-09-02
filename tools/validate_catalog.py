#!/usr/bin/env python3
"""Verificações estruturais leves do catálogo e dos manifestos.

Não substitui validação YAML completa, revisão factual, QA ou aprovação humana.
Mantido sem dependências para funcionar no MVP. Aceita a convenção YAML simples deste
repositório e verifica campos de primeira linha usados na navegação editorial.
"""
from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "content" / "catalog.yml"
VALID_STATES = {
    "IDEA", "RESEARCH", "OUTLINE", "SCRIPT", "SCRIPT_REVIEW", "SCRIPT_APPROVED",
    "VOICE", "ASSETS", "EDITING", "QA", "HUMAN_REVIEW", "APPROVED", "PUBLISHED",
    "ANALYZING",
}


def scalar_after(text: str, key: str) -> str | None:
    pattern = rf"(?m)^\s*{re.escape(key)}:\s*(.+?)\s*$"
    match = re.search(pattern, text)
    if not match:
        return None
    return match.group(1).strip().strip("'\"")


def catalog_entries(text: str) -> list[dict[str, str]]:
    """Read only flat list entries shaped as '- content_id: ...' from catalog.yml."""
    entries: list[dict[str, str]] = []
    chunks = re.split(r"(?m)^\s{2}- content_id:\s*", text)
    for chunk in chunks[1:]:
        lines = chunk.splitlines()
        if not lines:
            continue
        entry = {"content_id": lines[0].strip().strip("'\"")}
        for line in lines[1:]:
            match = re.match(r"^\s{4}([a-z_]+):\s*(.*?)\s*$", line)
            if match:
                entry[match.group(1)] = match.group(2).strip().strip("'\"")
        entries.append(entry)
    return entries


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    if not CATALOG.exists():
        print(f"ERROR: catalog not found: {CATALOG.relative_to(ROOT)}")
        return 1

    catalog_text = CATALOG.read_text(encoding="utf-8")
    policy = scalar_after(catalog_text, "publication_policy")
    if policy != "human_explicit_approval_required":
        errors.append("catalog publication_policy must be human_explicit_approval_required")

    entries = catalog_entries(catalog_text)
    if not entries:
        errors.append("catalog has no content entries")

    seen: set[str] = set()
    for entry in entries:
        content_id = entry.get("content_id", "")
        if not re.fullmatch(r"[A-Z0-9-]+", content_id):
            errors.append(f"invalid content_id: {content_id!r}")
            continue
        if content_id in seen:
            errors.append(f"duplicate content_id: {content_id}")
        seen.add(content_id)
        for key in ("type", "language", "state", "package", "script", "research"):
            if not entry.get(key):
                errors.append(f"{content_id}: missing catalog field {key}")
        if entry.get("state") not in VALID_STATES:
            errors.append(f"{content_id}: invalid state {entry.get('state')!r}")
        if entry.get("owner_approval_required") != "true":
            errors.append(f"{content_id}: owner_approval_required must be true")

        manifest = ROOT / entry.get("package", "") / "manifest.yaml"
        if not manifest.exists():
            errors.append(f"{content_id}: manifest not found at {manifest.relative_to(ROOT)}")
            continue
        manifest_text = manifest.read_text(encoding="utf-8")
        for key in ("content_id", "type", "language", "state"):
            value = scalar_after(manifest_text, key)
            if not value:
                errors.append(f"{content_id}: manifest missing {key}")
            elif key in entry and value != entry[key]:
                errors.append(f"{content_id}: catalog {key}={entry[key]!r} differs from manifest {value!r}")
        if scalar_after(manifest_text, "publish_owner_approval") not in {"pending", "approved", "rejected"}:
            errors.append(f"{content_id}: manifest requires publish_owner_approval status")
        for required_file in (entry.get("script", ""), entry.get("research", "")):
            if required_file and not (ROOT / required_file).exists():
                errors.append(f"{content_id}: referenced file not found: {required_file}")

    for error in errors:
        print(f"ERROR: {error}")
    for warning in warnings:
        print(f"WARNING: {warning}")
    if errors:
        print(f"Validation failed: {len(errors)} error(s), {len(warnings)} warning(s).")
        return 1
    print(f"Validation passed: {len(entries)} content item(s) checked, {len(warnings)} warning(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
