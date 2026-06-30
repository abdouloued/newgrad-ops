#!/usr/bin/env python3
"""
Search the local problem maps (NeetCode 150, Blind 75, Monster 50) by slug,
title, pattern, or difficulty. Local-only, read-only, no network calls.

Usage:
    python search_problems.py --slug two-sum
    python search_problems.py --title "binary tree"
    python search_problems.py --pattern "Sliding Window" --difficulty Medium
    python search_problems.py --pattern Graphs --pattern "Dynamic Programming" --list neetcode150
    python search_problems.py --list monster50
"""

import sys
import json
import argparse
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "interview"

LIST_FILES = {
    "neetcode150": DATA_DIR / "neetcode150-map.json",
    "blind75": DATA_DIR / "blind75-map.json",
    "monster50": DATA_DIR / "monster50-map.json",
}


def load_all(lists_filter):
    entries = []
    for name, path in LIST_FILES.items():
        if lists_filter and name not in lists_filter:
            continue
        if not path.exists():
            print(f"Warning: missing data file {path}", file=sys.stderr)
            continue
        data = json.loads(path.read_text())
        for entry in data:
            entry = dict(entry)
            entry["_source_list"] = name
            entries.append(entry)
    return entries


def matches(entry, args):
    if args.slug and entry.get("slug", "").lower() != args.slug.lower():
        return False
    if args.title and args.title.lower() not in entry.get("title", "").lower():
        return False
    if args.pattern:
        entry_pattern = entry.get("pattern", "").lower()
        if not any(p.lower() == entry_pattern for p in args.pattern):
            return False
    if args.difficulty and entry.get("difficulty", "").lower() != args.difficulty.lower():
        return False
    return True


DIFFICULTY_ORDER = {"easy": 0, "medium": 1, "hard": 2}


def main():
    parser = argparse.ArgumentParser(description="Search local DSA problem maps")
    parser.add_argument("--slug", help="Exact slug match, e.g. two-sum")
    parser.add_argument("--title", help="Case-insensitive substring match on title")
    parser.add_argument("--pattern", action="append", help="Pattern name (repeatable)")
    parser.add_argument("--difficulty", choices=["Easy", "Medium", "Hard", "easy", "medium", "hard"])
    parser.add_argument(
        "--list",
        action="append",
        choices=list(LIST_FILES.keys()),
        help="Restrict to one or more lists (repeatable). Default: all three.",
    )
    args = parser.parse_args()

    entries = load_all(set(args.list) if args.list else None)
    results = [e for e in entries if matches(e, args)]

    # de-duplicate by slug (a problem can appear in multiple lists)
    by_slug = {}
    for e in results:
        if e["slug"] not in by_slug:
            by_slug[e["slug"]] = {**e, "_lists": {e["_source_list"]}}
        else:
            by_slug[e["slug"]]["_lists"].add(e["_source_list"])
    deduped = sorted(
        by_slug.values(),
        key=lambda e: (DIFFICULTY_ORDER.get(e.get("difficulty", "").lower(), 99), e.get("pattern", ""), e.get("title", "")),
    )

    if not deduped:
        print("No matching problems found.")
        sys.exit(0)

    print(f"\n{len(deduped)} matching problem(s):\n")
    current_pattern = None
    for e in deduped:
        if e.get("pattern") != current_pattern:
            current_pattern = e.get("pattern")
            print(f"{current_pattern}:")
        url = e.get("neetcode_url") or e.get("algomonster_url", "")
        lists = ", ".join(sorted(e["_lists"]))
        print(f"  - {e['title']} ({e.get('difficulty', '?')}) — {url}  [{lists}]")
        traps = e.get("traps") or []
        if traps:
            print(f"      trap: {traps[0]}")
    print()


if __name__ == "__main__":
    main()
