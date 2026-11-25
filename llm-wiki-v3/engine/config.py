"""Paths, schema access, and small I/O helpers shared by the engine."""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any, Iterable

WIKI_ROOT = Path(__file__).resolve().parent.parent
REPO_ROOT = WIKI_ROOT.parent
SCHEMA_PATH = WIKI_ROOT / "schema.json"

RAW_DIR = WIKI_ROOT / "raw"
INBOX_DIR = RAW_DIR / "inbox"
PRIVATE_RAW_DIR = RAW_DIR / "private"
OBS_DIR = WIKI_ROOT / "observations"
PRIVATE_OBS_DIR = OBS_DIR / "private"
STATE_DIR = WIKI_ROOT / "state"
PRIVATE_CLAIMS_PATH = STATE_DIR / "private_claims.jsonl"
PRIVATE_QUESTIONS_PATH = STATE_DIR / "private_questions.jsonl"
TRANS_DIR = WIKI_ROOT / "transitions"
GRAPH_DIR = WIKI_ROOT / "graph"
WIKI_DIR = WIKI_ROOT / "wiki"
RETRIEVAL_DIR = WIKI_ROOT / "retrieval"
EVALS_DIR = WIKI_ROOT / "evals"
EXPORTS_DIR = WIKI_ROOT / "exports"
REPORTS_DIR = WIKI_ROOT / "reports"
PROMPTS_DIR = WIKI_ROOT / "prompts"

TEXT_SUFFIXES = {".md", ".txt", ".py", ".ipynb", ".yml", ".yaml", ".json", ".toml", ".cfg"}
SKIP_DIRS = {
    ".git", ".venv", "venv", "__pycache__", ".ipynb_checkpoints", "node_modules",
    "teacher", "data", "kafka-data", "spark-warehouse", "metastore_db", ".devcontainer",
}
SKIP_NAME_PREFIXES = ("kafka_2.13-",)
MAX_SOURCE_BYTES = 8 * 1024 * 1024


def load_schema() -> dict[str, Any]:
    with SCHEMA_PATH.open(encoding="utf-8") as fh:
        schema = json.load(fh)
    topic_ids = {t["id"] for t in schema["topics"]}
    if "unfiled" not in topic_ids:
        raise SystemExit("schema.json: topics must include an 'unfiled' fallback topic")
    for name in ("source_types", "decay_profiles", "thresholds", "entities"):
        if name not in schema:
            raise SystemExit(f"schema.json: missing section '{name}'")
    return schema


def topic_index(schema: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {t["id"]: t for t in schema["topics"]}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def short_hash(text: str, length: int = 10) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:length]


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def parse_iso(value: str | None) -> dt.datetime | None:
    if not value:
        return None
    text = value.replace("Z", "+00:00")
    try:
        parsed = dt.datetime.fromisoformat(text)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=dt.timezone.utc)
    return parsed


def days_between(a: dt.datetime, b: dt.datetime) -> float:
    return (b - a).total_seconds() / 86400.0


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def write_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
    tmp.replace(path)


def append_jsonl(path: Path, row: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tmp.replace(path)


def read_json(path: Path, default: Any = None) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def _git(args: list[str], cwd: Path) -> str:
    try:
        out = subprocess.run(
            ["git", *args], cwd=str(cwd), capture_output=True, text=True, timeout=20
        )
    except (OSError, subprocess.SubprocessError):
        return ""
    return out.stdout.strip() if out.returncode == 0 else ""


def git_metadata(rel_path: str) -> dict[str, str]:
    """Last commit date and author for a repository path, if git knows it."""
    date = _git(["log", "-1", "--format=%cI", "--", rel_path], REPO_ROOT)
    author = _git(["log", "-1", "--format=%an", "--", rel_path], REPO_ROOT)
    return {"created_at": date, "author": author}


def relative_to_repo(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path.resolve())


def resolve_source_path(rel_path: str) -> Path:
    """Relative source paths are against the repo root, or the wiki root for raw/ drops."""
    for base in (REPO_ROOT, WIKI_ROOT):
        candidate = base / rel_path
        if candidate.exists():
            return candidate
    return REPO_ROOT / rel_path


def ensure_dirs() -> None:
    for directory in (
        WIKI_ROOT, RAW_DIR, INBOX_DIR, PRIVATE_RAW_DIR, OBS_DIR, STATE_DIR, TRANS_DIR, GRAPH_DIR,
        WIKI_DIR, RETRIEVAL_DIR, EVALS_DIR, EXPORTS_DIR, REPORTS_DIR, PROMPTS_DIR,
        OBS_DIR / "pending", OBS_DIR / "accepted", OBS_DIR / "rejected", OBS_DIR / "archived",
        PRIVATE_OBS_DIR,
    ):
        directory.mkdir(parents=True, exist_ok=True)


def is_private_sensitivity(sensitivity: str) -> bool:
    return sensitivity in {"private", "secret"}
