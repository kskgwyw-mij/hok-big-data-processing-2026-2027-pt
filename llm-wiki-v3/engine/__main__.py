"""Command line entry point: python3 -m engine <command>."""

from __future__ import annotations

import argparse
import json
import sys

from . import config, evals, llm, ops, render, state


def _print_ingest(report: ops.IngestReport) -> None:
    mode = "rebuild" if report.rebuilt else "ingest"
    print(f"\n{mode} complete")
    print(f"  sources       {report.sources}")
    print(f"  observations  {report.observations}")
    print(f"  rejected      {report.rejected}")
    print(f"  questions     {report.questions}")
    print(f"  claims new    {report.new_claims}")
    print(f"  supported     {report.support_updates}")
    print(f"  contradicted  {report.contradiction_updates}")
    print(f"  superseded    {report.supersessions}")
    print(f"  pages written {report.pages}")
    if report.changed_sources:
        print("  changed sources: " + ", ".join(report.changed_sources[:6]))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="engine",
        description="LLM Wiki v3 engine: observe -> update state -> render the wiki.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    ingest_parser = sub.add_parser("ingest", help="register new or changed sources and update the state")
    ingest_parser.add_argument("--no-inbox", action="store_true", help="skip raw/inbox")
    ingest_parser.add_argument("--quiet", action="store_true")

    sub.add_parser("rebuild", help="wipe derived state and re-derive everything from the sources")
    sub.add_parser("render", help="re-render the wiki from the current state")
    sub.add_parser("decay", help="apply time decay to every claim")
    sub.add_parser("stats", help="print state statistics")
    sub.add_parser("lint", help="run health checks and write reports/lint_latest.md")

    query_parser = sub.add_parser("query", help="answer a question from the current state")
    query_parser.add_argument("text", nargs="+")
    query_parser.add_argument("--limit", type=int, default=8)
    query_parser.add_argument("--json", action="store_true")

    review_parser = sub.add_parser("review", help="human override of a claim")
    review_parser.add_argument("action", choices=["approve", "reject", "obsolete", "restore", "merge", "resolve"])
    review_parser.add_argument("claim_id")
    review_parser.add_argument("--second", default="", help="target claim id for merge")
    review_parser.add_argument("--note", default="")

    eval_parser = sub.add_parser("eval", help="run retrieval, state and faithfulness evals")
    eval_parser.add_argument("--write", action="store_true", help="write evals/report.md")

    batch_parser = sub.add_parser("llm-batch", help="export chunks for LLM extraction (prompt contract 13.1)")
    batch_parser.add_argument("--size", type=int, default=6000, help="characters per chunk")
    batch_parser.add_argument("--limit", type=int, default=0, help="max chunks (0 = all)")

    apply_parser = sub.add_parser("llm-apply", help="validate and apply LLM observations from a JSONL file")
    apply_parser.add_argument("path")

    args = parser.parse_args(argv)

    if args.command == "ingest":
        _print_ingest(ops.ingest(include_inbox=not args.no_inbox, quiet=args.quiet))
        return 0
    if args.command == "rebuild":
        _print_ingest(ops.rebuild())
        return 0
    if args.command == "render":
        store = ops._store()
        questions = config.read_jsonl(config.STATE_DIR / "questions.jsonl")
        report = render.render_all(store, questions)
        print(f"pages written {len(report.pages)}, unchanged {report.skipped_unchanged}")
        return 0
    if args.command == "decay":
        changed = ops.decay()
        print(f"decay applied, {changed} claims moved")
        return 0
    if args.command == "stats":
        store = ops._store()
        print(json.dumps(store.stats(), indent=2))
        return 0
    if args.command == "lint":
        findings, report_text = ops.lint()
        errors = sum(1 for finding in findings if finding.severity == "error")
        warnings = sum(1 for finding in findings if finding.severity == "warning")
        print(report_text)
        print(f"\n{errors} errors, {warnings} warnings · full report: reports/lint_latest.md")
        return 1 if errors else 0
    if args.command == "query":
        print(ops.query(" ".join(args.text), limit=args.limit, as_json=args.json))
        return 0
    if args.command == "review":
        print(ops.review(args.action, args.claim_id, second=args.second, note=args.note))
        return 0
    if args.command == "eval":
        report = evals.run_all(write=args.write)
        print(report)
        return 0
    if args.command == "llm-batch":
        path = llm.export_batch(size=args.size, limit=args.limit)
        print(f"wrote {path}")
        return 0
    if args.command == "llm-apply":
        result = llm.apply_file(args.path)
        print(result)
        return 0
    parser.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
