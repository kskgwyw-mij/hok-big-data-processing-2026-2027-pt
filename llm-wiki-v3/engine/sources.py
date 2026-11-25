"""Source discovery, classification, registration and the immutable raw copy."""

from __future__ import annotations

import shutil
from pathlib import Path
from typing import Any

from . import config
from .readers import Source

TYPE_BY_SUFFIX = {
    ".pdf": "lecture_note",
    ".ipynb": "notebook",
    ".py": "code",
    ".yml": "config",
    ".yaml": "config",
    ".toml": "config",
    ".cfg": "config",
}

EXAM_MARKERS = ("exam_circuit", "mock_exam", "exam")


def discover(repo_root: Path = config.REPO_ROOT) -> list[Path]:
    found: list[Path] = []
    for path in sorted(repo_root.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(repo_root)
        if any(part in config.SKIP_DIRS for part in rel.parts[:-1]):
            continue
        if rel.parts and rel.parts[0] == config.WIKI_ROOT.name:
            continue
        if path.name.startswith(config.SKIP_NAME_PREFIXES):
            continue
        if path.suffix.lower() not in config.TEXT_SUFFIXES | {".pdf"}:
            continue
        try:
            if path.stat().st_size > config.MAX_SOURCE_BYTES:
                continue
        except OSError:
            continue
        found.append(path)
    return found


def discover_inbox() -> list[Path]:
    if not config.INBOX_DIR.exists():
        return []
    return sorted(p for p in config.INBOX_DIR.rglob("*") if p.is_file())


def classify(path: Path) -> str:
    suffix = path.suffix.lower()
    name = path.name.lower()
    rel = config.relative_to_repo(path) if path.is_absolute() else str(path)
    if suffix in TYPE_BY_SUFFIX:
        return TYPE_BY_SUFFIX[suffix]
    if suffix == ".md":
        if any(marker in name for marker in EXAM_MARKERS) or "exam" in rel.lower():
            return "exam"
        try:
            head = path.read_text(encoding="utf-8", errors="replace")[:400]
        except OSError:
            head = ""
        first_heading = head.lstrip().splitlines()[:1]
        heading = first_heading[0] if first_heading else ""
        if heading.startswith(("# Lab", "# Block", "## Lab", "## Block")):
            return "lab_guide"
        return "readme"
    if suffix == ".ipynb":
        return "notebook"
    if suffix == ".py":
        return "code"
    if suffix in {".yml", ".yaml", ".json", ".toml", ".cfg"} or name.startswith("requirements"):
        return "config"
    if suffix == ".txt":
        try:
            size = path.stat().st_size
        except OSError:
            size = 0
        return "session_stub" if size < 400 else "readme"
    return "readme"


def make_source(path: Path, schema: dict[str, Any], raw_dir: Path | None = None) -> Source:
    rel = config.relative_to_repo(path)
    if raw_dir is not None:
        rel = f"inbox/{path.name}"
    source_type = classify(path)
    source_type_spec = schema["source_types"].get(source_type, {"authority": 0.6})
    meta = config.git_metadata(str(path)) if raw_dir is None else {}
    created = meta.get("created_at") or ""
    if not created:
        import datetime as dt
        created = dt.datetime.fromtimestamp(path.stat().st_mtime, dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    return Source(
        source_id="src_" + config.short_hash(rel, 8),
        rel_path=rel,
        abs_path=path,
        type=source_type,
        authority=float(source_type_spec["authority"]),
        created_at=created,
        author=meta.get("author") or "unknown",
        scope="shared",
        sensitivity="internal",
        title=path.stem.replace("_", " "),
        content_hash=config.sha256_file(path),
    )


def register_raw(source: Source, raw_dir: Path) -> Path:
    """Copy the source into raw/<type>/ unchanged; the copy is the immutability proof."""
    target = raw_dir / source.type / f"{source.source_id}__{source.abs_path.name}"
    target.parent.mkdir(parents=True, exist_ok=True)
    if not target.exists() or config.sha256_file(target) != source.content_hash:
        shutil.copy2(source.abs_path, target)
    return target
