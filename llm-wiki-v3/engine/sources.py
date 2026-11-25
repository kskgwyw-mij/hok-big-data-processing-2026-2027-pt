"""Source discovery, classification, registration and the immutable raw copy."""

from __future__ import annotations

import datetime as dt
import fnmatch
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


def discover_dropzone(schema: dict[str, Any]) -> list[Path]:
    """Files dropped anywhere under raw/ except the registered type folders.

    The drop zone is the only place large files (lecture decks) may live: they are
    not copied, so the size cap that protects the repository scan does not apply.
    """
    if not config.RAW_DIR.exists():
        return []
    reserved = set(schema["source_types"]) | {"inbox"}
    found: list[Path] = []
    for path in sorted(config.RAW_DIR.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(config.RAW_DIR)
        if len(rel.parts) > 1 and rel.parts[0] in reserved:
            continue
        found.append(path)
    return found


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


def classify_sensitivity(path: Path, schema: dict[str, Any]) -> str:
    """Teacher material (solutions, answer keys) is private: queryable, never published."""
    privacy = schema.get("privacy") or {}
    patterns = [p.lower() for p in privacy.get("private_patterns", [])]
    if not patterns:
        return privacy.get("public_sensitivity", "internal")
    try:
        in_wiki = path.resolve().is_relative_to(config.WIKI_ROOT)
    except OSError:
        in_wiki = False
    rel = str(path.resolve().relative_to(config.WIKI_ROOT)).lower() if in_wiki else ""
    name = path.name.lower()
    for pattern in patterns:
        if fnmatch.fnmatch(name, pattern) or (rel and fnmatch.fnmatch(rel, pattern)):
            return privacy.get("private_sensitivity", "private")
    return privacy.get("public_sensitivity", "internal")


def make_source(
    path: Path, schema: dict[str, Any], raw_dir: Path | None = None, dropzone: bool = False
) -> Source:
    """Build the source record. `dropzone` files already live under raw/ and are not copied."""
    rel = config.relative_to_repo(path)
    raw_rel: str | None = None
    if dropzone:
        try:
            raw_rel = str(path.resolve().relative_to(config.WIKI_ROOT))
        except ValueError:
            dropzone = False
        else:
            rel = raw_rel
    if raw_dir is not None:
        rel = f"inbox/{path.name}"
    source_type = classify(path)
    source_type_spec = schema["source_types"].get(source_type, {"authority": 0.6})
    sensitivity = classify_sensitivity(path, schema)
    if sensitivity != "internal" and path.suffix.lower() == ".md" and source_type == "readme":
        source_type = "exam"
        source_type_spec = schema["source_types"].get(source_type, source_type_spec)
    meta = config.git_metadata(str(path)) if raw_dir is None and not dropzone else {}
    created = meta.get("created_at") or ""
    if not created:
        created = (
            dt.datetime.fromtimestamp(path.stat().st_mtime, dt.timezone.utc)
            .replace(microsecond=0)
            .isoformat()
            .replace("+00:00", "Z")
        )
    return Source(
        source_id="src_" + config.short_hash(rel, 8),
        rel_path=rel,
        abs_path=path,
        type=source_type,
        authority=float(source_type_spec["authority"]),
        created_at=created,
        author=meta.get("author") or "unknown",
        scope="shared" if sensitivity == "internal" else "private",
        sensitivity=sensitivity,
        title=path.stem.replace("_", " "),
        content_hash=config.sha256_file(path),
        raw_rel_path=raw_rel,
    )


def register_raw(source: Source, raw_dir: Path) -> Path:
    """Immutable copy of the source under raw/<type>/.

    A file that already lives under raw/ is its own preserved copy: copying it again
    would duplicate data and, for teacher material, spread it further.
    """
    if source.raw_rel_path:
        return config.WIKI_ROOT / source.raw_rel_path
    target = raw_dir / source.type / f"{source.source_id}__{source.abs_path.name}"
    target.parent.mkdir(parents=True, exist_ok=True)
    if not target.exists() or config.sha256_file(target) != source.content_hash:
        shutil.copy2(source.abs_path, target)
    return target
