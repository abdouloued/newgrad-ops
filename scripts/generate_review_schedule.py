#!/usr/bin/env python3
"""
Generate a spaced repetition review schedule from a list of solved problems.
Reads a JSON file with solve history, outputs review schedule to stdout.

Input format (JSON file or stdin):
    [
      {"slug": "two-sum", "solved_date": "2026-06-25"},
      {"slug": "merge-intervals", "solved_date": "2026-06-28"},
      ...
    ]

Output: problems due for review today and upcoming, grouped by date.

Usage:
    python generate_review_schedule.py solved.json
    python generate_review_schedule.py solved.json --from 2026-07-01
"""

import sys
import json
import argparse
from datetime import date, timedelta
from pathlib import Path

REVIEW_INTERVALS = [1, 3, 7, 14, 30]


def load_solved(path_or_stdin: str) -> list:
    if path_or_stdin == "-":
        text = sys.stdin.read()
    else:
        p = Path(path_or_stdin)
        if not p.exists():
            print(f"Error: file not found: {path_or_stdin}", file=sys.stderr)
            sys.exit(1)
        text = p.read_text()
    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        print(f"Error: invalid JSON — {e}", file=sys.stderr)
        sys.exit(1)


def generate_schedule(solved: list, from_date: date) -> dict:
    schedule = {}

    for entry in solved:
        slug = entry.get("slug", "unknown")
        solved_date_str = entry.get("solved_date", "")
        try:
            solved_date = date.fromisoformat(solved_date_str)
        except ValueError:
            print(f"Warning: skipping '{slug}' — invalid date '{solved_date_str}'", file=sys.stderr)
            continue

        for interval in REVIEW_INTERVALS:
            review_date = solved_date + timedelta(days=interval)
            if review_date >= from_date:
                key = review_date.isoformat()
                schedule.setdefault(key, []).append({
                    "slug": slug,
                    "solved_date": solved_date_str,
                    "days_since_solved": interval,
                })

    return dict(sorted(schedule.items()))


def main():
    parser = argparse.ArgumentParser(description="Generate spaced repetition schedule")
    parser.add_argument("input", nargs="?", default="-", help="JSON file with solved problems (default: stdin)")
    parser.add_argument("--from", dest="from_date", default=None, help="Start date YYYY-MM-DD (default: today)")
    parser.add_argument("--days", type=int, default=14, help="How many days ahead to show (default: 14)")
    args = parser.parse_args()

    from_date = date.today()
    if args.from_date:
        try:
            from_date = date.fromisoformat(args.from_date)
        except ValueError:
            print(f"Error: invalid --from date '{args.from_date}'", file=sys.stderr)
            sys.exit(1)

    solved = load_solved(args.input)
    schedule = generate_schedule(solved, from_date)

    cutoff = from_date + timedelta(days=args.days)
    upcoming = {k: v for k, v in schedule.items() if date.fromisoformat(k) <= cutoff}

    if not upcoming:
        print(f"\nNo reviews due between {from_date} and {cutoff}.\n")
        return

    print(f"\nSpaced Repetition Schedule — {from_date} to {cutoff}\n")

    today_str = from_date.isoformat()
    for review_date_str, problems in upcoming.items():
        label = ""
        if review_date_str == today_str:
            label = " ← TODAY"
        elif review_date_str == (from_date + timedelta(days=1)).isoformat():
            label = " ← TOMORROW"

        print(f"{review_date_str}{label}  ({len(problems)} problems)")
        for p in problems:
            days_label = f"{p['days_since_solved']}-day review"
            print(f"  - {p['slug']}  [{days_label}, solved {p['solved_date']}]")
        print()

    total = sum(len(v) for v in upcoming.values())
    print(f"Total reviews in next {args.days} days: {total}")
    print()


if __name__ == "__main__":
    main()
