"""Gold continuity checks; deliberately conservative and CI-friendly."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATUSES = {"source_canon", "accepted_extension", "proposal", "alternate", "contradicted"}


def front_matter(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end < 0:
        return {}
    # Minimal YAML subset intentionally keeps CI dependency-free.
    result: dict[str, object] = {}
    for line in text[4:end].splitlines():
        match = re.match(r"^([\w-]+):\s*(.*)$", line)
        if match:
            result[match.group(1)] = match.group(2).strip().strip('"')
    return result


def main() -> None:
    errors: list[str] = []
    ids: set[str] = set()
    bronze = ROOT / "bronze" / "manifests" / "pages.json"
    page_ids = {str(page["page_id"]) for page in json.loads(bronze.read_text(encoding="utf-8"))} if bronze.exists() else set()
    for path in (ROOT / "gold").rglob("*.md"):
        if path.name == "README.md":
            continue
        data = front_matter(path)
        for key in ("id", "kind", "status", "title"):
            if not data.get(key): errors.append(f"{path}: missing {key}")
        identifier = str(data.get("id", ""))
        if identifier in ids: errors.append(f"{path}: duplicate id {identifier}")
        ids.add(identifier)
        if data.get("status") not in STATUSES: errors.append(f"{path}: invalid status {data.get('status')}")
        if data.get("status") == "accepted_extension" and "rationale:" not in path.read_text(encoding="utf-8") and "page_id:" not in path.read_text(encoding="utf-8"):
            errors.append(f"{path}: accepted extension needs a rationale or source page_id")
        for matched in re.findall(r"page_id:\s*(\d+)", path.read_text(encoding="utf-8")):
            if page_ids and matched not in page_ids: errors.append(f"{path}: unknown Bronze page_id {matched}")
    if errors:
        print("Continuity validation failed:\n- " + "\n- ".join(errors), file=sys.stderr); raise SystemExit(1)
    print("Continuity validation passed.")


if __name__ == "__main__":
    main()
