#!/usr/bin/env python3
"""
Validate the repo's data files and scripts. Local-only, read-only, no network
calls. Exits non-zero on any failure — used by CI and by contributors before
opening a PR (see CONTRIBUTING.md).

Usage:
    python scripts/validate_repo.py
"""

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []
warnings = []


def fail(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def check_json_parses():
    print("== JSON validity ==")
    json_files = sorted((ROOT / "data").rglob("*.json"))
    for path in json_files:
        rel = path.relative_to(ROOT)
        try:
            json.loads(path.read_text())
            print(f"  OK   {rel}")
        except json.JSONDecodeError as e:
            fail(f"{rel}: invalid JSON — {e}")
    return json_files


PROBLEM_FILES = ["neetcode150-map.json", "blind75-map.json", "monster50-map.json"]
DIFFICULTIES = {"Easy", "Medium", "Hard"}


def check_problem_schema():
    print("\n== Problem entry schema ==")
    patterns_path = ROOT / "data" / "interview" / "patterns.json"
    known_patterns = set(json.loads(patterns_path.read_text()).keys())

    for fname in PROBLEM_FILES:
        path = ROOT / "data" / "interview" / fname
        if not path.exists():
            fail(f"{fname}: file missing")
            continue
        entries = json.loads(path.read_text())
        seen_slugs = set()
        bad = 0
        for e in entries:
            slug = e.get("slug", "<no slug>")
            for field in ("slug", "title", "difficulty", "pattern"):
                if not e.get(field):
                    fail(f"{fname}/{slug}: missing required field '{field}'")
                    bad += 1
            if e.get("difficulty") not in DIFFICULTIES:
                fail(f"{fname}/{slug}: difficulty '{e.get('difficulty')}' not one of {DIFFICULTIES}")
                bad += 1
            if e.get("pattern") not in known_patterns:
                fail(f"{fname}/{slug}: pattern '{e.get('pattern')}' not in patterns.json")
                bad += 1
            url = e.get("neetcode_url") or e.get("algomonster_url")
            if not url or not url.startswith("https://"):
                fail(f"{fname}/{slug}: missing or invalid public URL")
                bad += 1
            if not e.get("traps"):
                warn(f"{fname}/{slug}: no traps listed")
            if slug in seen_slugs:
                fail(f"{fname}/{slug}: duplicate slug in this file")
                bad += 1
            seen_slugs.add(slug)
        status = "OK" if bad == 0 else f"{bad} issue(s)"
        print(f"  {status:12} {fname} ({len(entries)} entries, {len(seen_slugs)} unique slugs)")


def check_internal_links():
    print("\n== Internal markdown links ==")
    link_re = re.compile(r"\]\(([a-zA-Z0-9_./-]+\.md[^)]*)\)")
    md_files = [p for p in ROOT.rglob("*.md") if ".git" not in p.parts]
    checked = 0
    for path in md_files:
        text = path.read_text()
        for match in link_re.finditer(text):
            link = match.group(1).split("#")[0]
            if link.startswith("http"):
                continue
            resolved = (path.parent / link).resolve()
            checked += 1
            if not resolved.exists():
                fail(f"{path.relative_to(ROOT)}: broken link -> {link}")
    print(f"  checked {checked} relative links across {len(md_files)} markdown files")


def check_scripts_run():
    print("\n== Script smoke tests ==")
    tests = [
        (["python3", "scripts/score_resume.py", "templates/resumes/new-grad-template.md"], "score_resume.py"),
        (["python3", "scripts/score_resume.py", "templates/resumes/new-grad-template.md", "--roast"], "score_resume.py --roast"),
        (["python3", "scripts/score_readme.py", "templates/github-readmes/project-readme-template.md"], "score_readme.py"),
        (["python3", "scripts/search_problems.py", "--slug", "two-sum"], "search_problems.py"),
    ]
    for cmd, label in tests:
        result = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
        if result.returncode != 0:
            fail(f"{label} exited {result.returncode}: {result.stderr.strip()[:200]}")
        else:
            print(f"  OK   {label}")


def main():
    check_json_parses()
    check_problem_schema()
    check_internal_links()
    check_scripts_run()

    print()
    if warnings:
        print(f"{len(warnings)} warning(s):")
        for w in warnings:
            print(f"  - {w}")
        print()

    if errors:
        print(f"FAILED — {len(errors)} error(s):")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)

    print("All checks passed.")
    sys.exit(0)


if __name__ == "__main__":
    main()
