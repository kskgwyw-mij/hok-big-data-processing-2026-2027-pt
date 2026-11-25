"""Turn a source file into locatable text segments.

Every segment remembers where it came from, so an observation can always point
at a verbatim evidence span instead of a paraphrase.
"""

from __future__ import annotations

import ast
import json
import os
import re
import subprocess
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

from . import config

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
BULLET_RE = re.compile(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$")
TABLE_SEP_RE = re.compile(r"^\s*\|?[\s:|-]*-[\s:|-]*\|?\s*$")
HTML_TAG_RE = re.compile(r"<[^>]{1,80}>")
LINK_RE = re.compile(r"!?\[([^\]]*)\]\(([^)]+)\)")
INLINE_CODE_RE = re.compile(r"`([^`]*)`")
BOLD_RE = re.compile(r"(\*\*\*|\*\*|__)(?=\S)(.+?)(?<=\S)\1")
ITALIC_RE = re.compile(r"(?<![\w*])\*(?=\S)([^*\n]+?)(?<=\S)\*(?![\w*])")
PLACEHOLDER_RE = re.compile(r"^[\s_\-–—.·|]*$")
NUMBERING_RE = re.compile(r"^\s*(?:\d+(?:\.\d+)*[.)]?|[A-Z]\.)\s+")
TIME_HINT_RE = re.compile(r"\s*\((?:≈\s*)?\d+\s*(?:min|minutes|minuten)\)\s*$", re.IGNORECASE)
DIFF_META_RE = re.compile(
    r"^(?:@@ [-+0-9, ]+ @@|diff --git |index [0-9a-f]{7,}|@@ |--- \S|\+\+\+ \S|\\ No newline)"
)
COMMAND_PREFIXES = (
    "docker", "git", "python", "python3", "py ", "pip", "uv ", "pyenv", "kafka-", "export ",
    "cd ", "source ", "spark-submit", "spark-shell", "curl ", "winget", "brew ", "sudo ",
    "powershell", "jupyter", "conda", "make ", "bash ", "sh ",
)


@dataclass
class Source:
    source_id: str
    rel_path: str
    abs_path: Path
    type: str
    authority: float
    created_at: str
    author: str
    scope: str
    sensitivity: str
    title: str
    content_hash: str
    raw_rel_path: str | None = None

    def record(self) -> dict:
        raw_path = self.raw_rel_path or f"raw/{self.type}/{self.source_id}__{Path(self.rel_path).name}"
        return {
            "source_id": self.source_id,
            "type": self.type,
            "path": self.rel_path,
            "raw_path": raw_path,
            "title": self.title,
            "created_at": self.created_at,
            "author": self.author,
            "source_authority": self.authority,
            "scope": self.scope,
            "sensitivity": self.sensitivity,
            "hash": f"sha256:{self.content_hash}",
        }


@dataclass
class Segment:
    rel_path: str
    locator: str
    block: str
    heading_path: tuple[str, ...]
    text: str
    raw: str
    header: tuple[str, ...] = ()
    cells: tuple[str, ...] = ()
    labels: tuple[str, ...] = field(default_factory=tuple)


CHECK_MARKS = {"✓": "yes", "✔": "yes", "✗": "no", "✘": "no", "×": "no"}


def strip_emoji(text: str) -> str:
    out = []
    for ch in text:
        cat = unicodedata.category(ch)
        if cat in {"So", "Sk"} and ch not in CHECK_MARKS:
            continue
        if ch in {"\ufe0f", "\u200d", "\u20e3"}:
            continue
        if ch == "\u00a0":
            out.append(" ")
            continue
        out.append(ch)
    return "".join(out)


def clean_inline(text: str) -> str:
    text = HTML_TAG_RE.sub(" ", text)
    text = LINK_RE.sub(lambda m: m.group(1) or m.group(2), text)
    text = INLINE_CODE_RE.sub(lambda m: m.group(1), text)
    text = BOLD_RE.sub(lambda m: m.group(2), text)
    text = ITALIC_RE.sub(lambda m: m.group(1), text)
    text = text.replace("~~", "")
    text = text.replace("&nbsp;", " ").replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    text = strip_emoji(text)
    text = text.replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')
    text = re.sub(r"\s+", " ", text)
    return text.strip()


TRAILING_GROUP_RE = re.compile(r"\s*\((?=[^()]*)(?=[^()]*(?:\d|min|Session|Block))[^()]*\)\s*$")


def clean_heading(text: str) -> str:
    text = clean_inline(text)
    text = NUMBERING_RE.sub("", text)
    text = TIME_HINT_RE.sub("", text)
    while TRAILING_GROUP_RE.search(text):
        text = TRAILING_GROUP_RE.sub("", text)
    text = re.sub(r"\s*[·|]\s*\d+\s*P\b.*$", "", text)
    return text.strip(" .-–—:")


def looks_like_diff(text: str) -> bool:
    head = text.splitlines()[:6]
    return any(line.startswith("@@ ") or line.startswith("diff --git") for line in head)


def prepare_lines(text: str) -> list[tuple[int, str]]:
    """Split into (original line number, content) pairs, unwrapping diff artifacts."""
    lines = text.splitlines()
    if not looks_like_diff(text):
        return list(enumerate(lines, start=1))
    body: list[tuple[int, str]] = []
    started = False
    for number, line in enumerate(lines, start=1):
        stripped = line.strip()
        if not started and (stripped.startswith("@@ ") or stripped.startswith("diff --git")):
            started = True
            continue
        if not started and (stripped.startswith("* ") or stripped.startswith("--- ")):
            continue
        if DIFF_META_RE.match(stripped):
            continue
        body.append((number, line))
    content = [line for _, line in body if line.strip()]
    if content:
        plus_ratio = sum(1 for line in content if line.startswith("+")) / len(content)
        if plus_ratio > 0.8:
            body = [(n, line[1:] if line.startswith("+") else line) for n, line in body]
    return body


def is_command(line: str) -> bool:
    stripped = line.strip().lstrip("$ ").strip()
    if not stripped or len(stripped) < 3:
        return False
    if stripped.startswith("#"):
        return True
    if "--" in stripped or stripped.startswith("./"):
        return True
    return stripped.lower().startswith(COMMAND_PREFIXES)


def meaningful_line(text: str) -> bool:
    if PLACEHOLDER_RE.match(text):
        return False
    if len(clean_inline(text)) < 3:
        return False
    return True


def read_markdown(
    text: str,
    rel_path: str,
    heading_stack: Iterable[str] = (),
    locator_prefix: str | None = None,
) -> list[Segment]:
    segments: list[Segment] = []
    stack: list[tuple[int, str]] = [(index + 1, title) for index, title in enumerate(heading_stack)]
    lines = prepare_lines(text)

    para: list[str] = []
    para_raw: list[str] = []
    para_line = 0
    bullet: list[str] = []
    bullet_raw: list[str] = []
    bullet_line = 0
    table: list[tuple[int, str]] = []
    in_fence = False
    fence_lines: list[str] = []

    def locator(line_number: int) -> str:
        base = locator_prefix or rel_path
        return f"{base}:{line_number}"

    def headings() -> tuple[str, ...]:
        return tuple(title for _, title in stack)

    def flush_para() -> None:
        nonlocal para, para_raw, para_line
        if para:
            text_joined = clean_inline(" ".join(para))
            raw_joined = " ".join(para_raw).strip()
            if len(text_joined) >= 12 and meaningful_line(text_joined):
                segments.append(Segment(rel_path, locator(para_line), "paragraph", headings(), text_joined, raw_joined))
        para, para_raw, para_line = [], [], 0

    def flush_bullet() -> None:
        nonlocal bullet, bullet_raw, bullet_line
        if bullet:
            text_joined = clean_inline(" ".join(bullet))
            raw_joined = " ".join(bullet_raw).strip()
            if len(text_joined) >= 8 and meaningful_line(text_joined):
                segments.append(Segment(rel_path, locator(bullet_line), "bullet", headings(), text_joined, raw_joined))
        bullet, bullet_raw, bullet_line = [], [], 0

    def flush_table() -> None:
        nonlocal table
        if len(table) >= 2:
            header_cells = [clean_inline(c) for c in table[0][1].strip().strip("|").split("|")]
            matrix = not header_cells or not header_cells[0]
            for number, row in table[1:]:
                if TABLE_SEP_RE.match(row):
                    continue
                cells = [clean_inline(c) for c in row.strip().strip("|").split("|")]
                cells = [
                    cell.replace("✓", "yes").replace("✔", "yes").replace("✗", "no").replace("✘", "no")
                    for cell in cells
                ]
                if matrix and len(cells) >= 2:
                    label = cells[0]
                    pairs = [
                        f"{header_cells[i] if i < len(header_cells) and header_cells[i] else f'column {i}'}: {cell}"
                        for i, cell in enumerate(cells[1:], start=1) if cell
                    ]
                    text = f"{label}: " + ", ".join(pairs) if label else ", ".join(pairs)
                    raw_joined = " | ".join(c.strip() for c in cells if c.strip())
                    if len(text) >= 12:
                        segments.append(
                            Segment(rel_path, locator(number), "table_row", headings(),
                                    text, raw_joined, tuple(header_cells), tuple(cells), ("matrix",))
                        )
                    continue
                pairs = [
                    f"{header_cells[i] if i < len(header_cells) and header_cells[i] else 'value'}: {cell}"
                    for i, cell in enumerate(cells) if cell
                ]
                if not pairs:
                    continue
                raw_joined = " | ".join(c.strip() for c in cells if c.strip())
                if len(raw_joined) < 6:
                    continue
                segments.append(
                    Segment(
                        rel_path, locator(number), "table_row", headings(),
                        "; ".join(pairs), raw_joined, tuple(header_cells), tuple(cells),
                    )
                )
        table = []

    def flush_fence() -> None:
        nonlocal fence_lines
        if fence_lines:
            comments = [line for line in fence_lines if line.strip().startswith("#")]
            commands = [line for line in fence_lines if is_command(line) and not line.strip().startswith("#")]
            for line in comments:
                cleaned = clean_inline(line.strip().lstrip("#").strip())
                if len(cleaned) >= 10:
                    segments.append(Segment(rel_path, locator(para_line or 1), "code_comment", headings(), cleaned, line.strip()))
            if commands:
                cleaned = clean_inline(" ; ".join(c.strip().lstrip("$").strip() for c in commands))
                if len(cleaned) >= 6:
                    segments.append(
                        Segment(rel_path, locator(para_line or 1), "code", headings(), cleaned,
                                " ; ".join(c.strip() for c in commands))
                    )
        fence_lines = []

    for number, line in lines:
        fence = FENCE_RE.match(line)
        if in_fence:
            if fence:
                in_fence = False
                flush_fence()
            else:
                fence_lines.append(line)
            continue
        if fence:
            flush_para()
            flush_bullet()
            flush_table()
            in_fence = True
            para_line = number
            fence_lines = []
            continue

        heading = HEADING_RE.match(line)
        if heading:
            flush_para()
            flush_bullet()
            flush_table()
            level = len(heading.group(1))
            title = clean_heading(heading.group(2))
            if title:
                stack = [entry for entry in stack if entry[0] < level] + [(level, title)]
            continue

        if not line.strip():
            flush_para()
            flush_bullet()
            flush_table()
            continue

        if line.lstrip().startswith("|") or ("|" in line and len(table) > 0 and line.strip().startswith("|")):
            flush_para()
            flush_bullet()
            table.append((number, line))
            continue

        bullet_match = BULLET_RE.match(line)
        if bullet_match and not line.lstrip().startswith("|"):
            flush_para()
            flush_bullet()
            flush_table()
            bullet_line = number
            bullet = [bullet_match.group(3)]
            bullet_raw = [line.strip()]
            continue

        if bullet:
            bullet.append(line.strip())
            bullet_raw.append(line.strip())
            continue

        if line.lstrip().startswith(">"):
            flush_table()
            para_line = para_line or number
            para.append(line.strip().lstrip(">").strip())
            para_raw.append(line.strip())
            continue

        flush_table()
        if not para:
            para_line = number
        para.append(line.strip())
        para_raw.append(line.strip())

    flush_para()
    flush_bullet()
    flush_table()
    if in_fence:
        flush_fence()
    return segments


def read_notebook(text: str, rel_path: str) -> list[Segment]:
    try:
        notebook = json.loads(text)
    except json.JSONDecodeError:
        return read_markdown(text, rel_path)
    segments: list[Segment] = []
    heading_stack: list[str] = []
    title = ""
    for index, cell in enumerate(notebook.get("cells", [])):
        kind = cell.get("cell_type")
        source = "".join(cell.get("source", []))
        locator = f"{rel_path}#cell-{index}"
        if kind == "markdown":
            cell_segments = read_markdown(source, rel_path, heading_stack, locator_prefix=locator)
            for segment in cell_segments:
                if segment.heading_path and segment.block == "paragraph":
                    heading_stack = list(segment.heading_path)
            if cell_segments:
                heading_stack = list(cell_segments[-1].heading_path)
            if not title:
                first_heading = re.search(r"^#\s+(.+)$", source, re.MULTILINE)
                if first_heading:
                    title = clean_heading(first_heading.group(1))
            segments.extend(cell_segments)
        elif kind == "code":
            comments = []
            for offset, line in enumerate(source.splitlines(), start=1):
                stripped = line.strip()
                if stripped.startswith("#") and len(stripped) > 3:
                    comments.append(clean_inline(stripped.lstrip("#").strip()))
            joined = " ".join(c for c in comments if len(c) > 8)
            if len(joined) >= 15:
                segments.append(
                    Segment(rel_path, locator, "code_comment", tuple(heading_stack), joined,
                            joined, labels=("notebook_code",))
                )
    return segments


def read_python(text: str, rel_path: str) -> list[Segment]:
    segments: list[Segment] = []
    heading_stack: list[str] = [Path(rel_path).stem]
    try:
        tree = ast.parse(text)
    except SyntaxError:
        tree = None
    if tree is not None:
        module_doc = ast.get_docstring(tree)
        if module_doc:
            for line_number, chunk in _docstring_paragraphs(module_doc):
                cleaned = clean_inline(chunk)
                if len(cleaned) >= 25:
                    segments.append(Segment(rel_path, f"{rel_path}:1", "docstring", tuple(heading_stack), cleaned, chunk.strip()))
        for node in tree.body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                doc = ast.get_docstring(node)
                stack = tuple(heading_stack + [node.name.replace("_", " ")])
                if doc:
                    for _, chunk in _docstring_paragraphs(doc):
                        cleaned = clean_inline(chunk)
                        if len(cleaned) >= 25:
                            segments.append(Segment(rel_path, f"{rel_path}:{node.lineno}", "docstring", stack, cleaned, chunk.strip()))
    for number, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if stripped.startswith("#") and not stripped.startswith("#!"):
            cleaned = clean_inline(stripped.lstrip("#").strip())
            if len(cleaned) >= 25 and not cleaned.lower().startswith(("todo", "type:", "noqa", "pragma")):
                segments.append(Segment(rel_path, f"{rel_path}:{number}", "code_comment", tuple(heading_stack), cleaned, stripped))
    return segments


def _docstring_paragraphs(doc: str) -> list[tuple[int, str]]:
    paragraphs = re.split(r"\n\s*\n", doc)
    return [(index, paragraph.replace("\n", " ").strip()) for index, paragraph in enumerate(paragraphs) if paragraph.strip()]


def read_config(text: str, rel_path: str) -> list[Segment]:
    segments: list[Segment] = []
    name = Path(rel_path).name
    heading = (name,)
    if name.startswith("requirements"):
        for number, line in enumerate(text.splitlines(), start=1):
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            if "==" in stripped or ">=" in stripped:
                package, _, version = re.split(r"(==|>=)", stripped, maxsplit=1)
                package = package.strip()
                version_text = (stripped[len(package):]).strip()
                segments.append(
                    Segment(rel_path, f"{rel_path}:{number}", "config", heading,
                            f"{package} is pinned as {version_text}", stripped)
                )
        return segments
    if name.endswith((".yml", ".yaml")):
        service = ""
        for number, line in enumerate(text.splitlines(), start=1):
            stripped = line.strip()
            match = re.match(r"^([A-Za-z0-9_.-]+):\s*(.*)$", stripped)
            if not match:
                continue
            key, value = match.group(1), match.group(2).strip().strip('"')
            indentation = len(line) - len(line.lstrip())
            if indentation <= 2 and not value:
                service = key
                continue
            if value:
                subject = f"{service} {key}".strip() if service else key
                segments.append(
                    Segment(rel_path, f"{rel_path}:{number}", "config", heading,
                            f"{subject} is {value}", stripped)
                )
        return segments
    if name.endswith(".json"):
        try:
            data = json.loads(text)
        except json.JSONDecodeError:
            return segments
        for key, value in _flatten_json(data):
            if isinstance(value, (str, int, float, bool)) and str(value).strip():
                segments.append(
                    Segment(rel_path, rel_path, "config", heading,
                            f"{key} is {value}", f'"{key}": "{value}"')
                )
        return segments
    return segments


def _flatten_json(data, prefix: str = "") -> list[tuple[str, object]]:
    out: list[tuple[str, object]] = []
    if isinstance(data, dict):
        for key, value in data.items():
            out.extend(_flatten_json(value, f"{prefix}.{key}".strip(".")))
    elif isinstance(data, list):
        for index, value in enumerate(data[:8]):
            out.extend(_flatten_json(value, f"{prefix}[{index}]"))
    else:
        out.append((prefix, data))
    return out


def read_pdf(path: Path, rel_path: str) -> list[Segment]:
    text = ""
    # System poppler must link against the system C++ runtime; an inherited
    # LD_LIBRARY_PATH (IDE bundles, conda) breaks it with GLIBCXX errors.
    environment = {key: value for key, value in os.environ.items() if key not in {"LD_LIBRARY_PATH", "LD_PRELOAD"}}
    try:
        out = subprocess.run(
            ["pdftotext", "-layout", "-enc", "UTF-8", str(path), "-"],
            capture_output=True, text=True, timeout=120, env=environment,
        )
        if out.returncode == 0:
            text = out.stdout
    except (OSError, subprocess.SubprocessError):
        text = ""
    if not text.strip():
        return [Segment(rel_path, f"{rel_path}:1", "notice", (Path(rel_path).stem,),
                        f"{rel_path} could not be read as text (no pdftotext or scanned pages); re-ingest after OCR.",
                        "", labels=("unreadable_pdf",))]
    segments: list[Segment] = []
    for page_number, page in enumerate(text.split("\f"), start=1):
        if not page.strip():
            continue
        page_segments = read_markdown(page, rel_path, locator_prefix=f"{rel_path}#p{page_number}")
        for segment in page_segments:
            segments.append(segment)
    return segments


def read_source(source: Source) -> list[Segment]:
    suffix = source.abs_path.suffix.lower()
    if suffix == ".pdf":
        return read_pdf(source.abs_path, source.rel_path)
    try:
        text = source.abs_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return []
    if suffix == ".ipynb":
        return read_notebook(text, source.rel_path)
    if suffix == ".py":
        return read_python(text, source.rel_path)
    if suffix in {".yml", ".yaml", ".json", ".txt"} and source.type == "config":
        return read_config(text, source.rel_path)
    if suffix in {".txt"} and source.type == "config":
        return read_config(text, source.rel_path)
    return read_markdown(text, source.rel_path)
