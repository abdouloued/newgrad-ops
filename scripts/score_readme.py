#!/usr/bin/env python3
"""
Score a GitHub project README for hiring signal quality.
Reads from a file path or stdin. Prints to stdout only — no file writes.

Usage:
    python score_readme.py README.md
    cat README.md | python score_readme.py
"""

import sys
import re
from pathlib import Path


SECTIONS = {
    "why": {
        "patterns": [r"why i built", r"motivation", r"why this", r"problem", r"background"],
        "weight": 20,
        "label": "Why / Motivation",
        "tip": "Add a 'Why I built this' section — 3 sentences about the problem you solved",
    },
    "demo": {
        "patterns": [r"live demo", r"demo", r"try it", r"deployed at", r"https://", r"screenshot"],
        "weight": 20,
        "label": "Demo / Live link",
        "tip": "Add a deployed demo link or a screenshot showing the project working",
    },
    "tests": {
        "patterns": [r"test", r"pytest", r"jest", r"coverage", r"ci", r"badge.*test", r"test.*badge"],
        "weight": 20,
        "label": "Tests",
        "tip": "Add a tests section or CI badge showing tests pass",
    },
    "architecture": {
        "patterns": [r"architect", r"design", r"how it works", r"overview", r"structure", r"components", r"diagram"],
        "weight": 20,
        "label": "Architecture / Design",
        "tip": "Add an architecture section — even a short text diagram explains your system design choices",
    },
    "metrics": {
        "patterns": [r"\d+[%x]\b", r"\d[\d,]*\s*(req|request|user|ms|second)", r"benchmark", r"performance", r"latency", r"throughput"],
        "weight": 20,
        "label": "Performance / Metrics",
        "tip": "Add one concrete metric: requests/sec, latency, test coverage %, or user count",
    },
}


def load_text(path_or_stdin: str) -> str:
    if path_or_stdin == "-":
        return sys.stdin.read()
    p = Path(path_or_stdin)
    if not p.exists():
        print(f"Error: file not found: {path_or_stdin}", file=sys.stderr)
        sys.exit(1)
    return p.read_text()


def score_readme(text: str) -> dict:
    text_lower = text.lower()
    score = 0
    present = []
    missing = []

    for key, section in SECTIONS.items():
        found = any(re.search(pat, text_lower) for pat in section["patterns"])
        if found:
            score += section["weight"]
            present.append(section["label"])
        else:
            missing.append((section["label"], section["tip"]))

    return {"score": score, "present": present, "missing": missing}


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "-"
    text = load_text(path)
    result = score_readme(text)

    print(f"\nREADME Score: {result['score']}/100\n")

    if result["present"]:
        print("Present:")
        for item in result["present"]:
            print(f"  ✓ {item}")

    if result["missing"]:
        print(f"\nMissing (add these for +{20 * len(result['missing'])} pts):")
        for i, (label, tip) in enumerate(result["missing"], 1):
            print(f"  {i}. {label}")
            print(f"     → {tip}")

    if result["score"] >= 80:
        print("\nStrong README — good hiring signal.")
    elif result["score"] >= 60:
        print("\nDecent README — a few fixes would significantly improve hiring signal.")
    else:
        print("\nWeak README — projects may appear like coursework. Fix missing sections.")

    print()


if __name__ == "__main__":
    main()
