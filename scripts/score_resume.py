#!/usr/bin/env python3
"""
Score a markdown resume and return a 0–100 score with a gap list.
Reads resume from a file path or stdin. Prints to stdout only — no file writes.

Usage:
    python score_resume.py resume.md
    cat resume.md | python score_resume.py
    python score_resume.py resume.md --roast    # same scoring, blunter delivery
"""

import sys
import re
import argparse
from pathlib import Path

# Each gap is tagged with a category so --roast can pair a one-liner with the
# same underlying fix instruction — roast mode changes tone, not substance.
ROASTS = {
    "no_projects": '"Projects" section is empty. Did you only do homework for four years?',
    "no_summary": "No summary line. The recruiter has to guess what you even want.",
    "weak_impact": "Every bullet reads like a job description, not something you actually did. Where are the numbers?",
    "few_keywords": "Your skills section could describe three different people. Be the one with substance.",
    "weak_verbs": '"Responsible for" is not an action verb. Neither is "helped with."',
    "few_links": "No GitHub, no LinkedIn, no proof of life. How is anyone supposed to check your work?",
    "too_short": "This resume has less content than a tweet. Pad it with substance, not adjectives.",
    "too_long": "Two pages for zero years of experience. Nobody is reading page 2.",
}

TECH_KEYWORDS = {
    "python", "javascript", "typescript", "java", "go", "rust", "c++",
    "sql", "postgresql", "mysql", "redis", "docker", "kubernetes",
    "aws", "gcp", "azure", "api", "rest", "graphql", "fastapi", "django",
    "react", "node", "distributed systems", "machine learning", "ml",
    "testing", "pytest", "jest", "ci/cd", "git", "linux",
}

IMPACT_PATTERNS = [
    r'\d+[%x]',               # percentages or multipliers: 40%, 3x
    r'\d[\d,]*\s*(users|requests|customers|daily|monthly)',
    r'(reduced|improved|increased|decreased|optimized|saved|cut)\b',
    r'\$\d',                   # dollar amounts
    r'\d+\s*(ms|seconds|hours|days)\b',
]

SECTION_HEADERS = [
    "experience", "education", "projects", "skills",
    "summary", "objective", "awards", "activities",
]


def load_text(path_or_stdin: str) -> str:
    if path_or_stdin == "-":
        return sys.stdin.read()
    p = Path(path_or_stdin)
    if not p.exists():
        print(f"Error: file not found: {path_or_stdin}", file=sys.stderr)
        sys.exit(1)
    return p.read_text()


def score_resume(text: str) -> dict:
    text_lower = text.lower()
    score = 0
    gaps = []
    details = {}

    # 1. Sections present (20 pts)
    found_sections = [s for s in SECTION_HEADERS if s in text_lower]
    section_score = min(20, len(found_sections) * 4)
    score += section_score
    details["sections"] = f"{len(found_sections)}/{len(SECTION_HEADERS)} key sections found"
    if "projects" not in text_lower:
        gaps.append({"category": "no_projects", "message": "No projects section — add 2–3 projects with links"})
    if "summary" not in text_lower and "objective" not in text_lower:
        gaps.append({"category": "no_summary", "message": "No summary/objective — add a 2-sentence targeted summary"})

    # 2. Quantified impact (25 pts)
    impact_hits = sum(
        1 for pattern in IMPACT_PATTERNS
        if re.search(pattern, text_lower)
    )
    impact_score = min(25, impact_hits * 5)
    score += impact_score
    details["impact"] = f"{impact_hits} quantified impact signals found"
    if impact_hits < 3:
        gaps.append({"category": "weak_impact", "message": "Weak impact quantification — add numbers (%, users, latency, req/s) to bullets"})

    # 3. Technical keywords (20 pts)
    found_keywords = [kw for kw in TECH_KEYWORDS if kw in text_lower]
    keyword_score = min(20, len(found_keywords) * 2)
    score += keyword_score
    details["keywords"] = f"{len(found_keywords)} tech keywords found"
    if len(found_keywords) < 6:
        gaps.append({"category": "few_keywords", "message": "Few technical keywords — expand skills section with languages, frameworks, tools"})

    # 4. Action verbs (15 pts)
    action_verbs = [
        "built", "designed", "implemented", "developed", "led", "created",
        "architected", "optimized", "reduced", "improved", "shipped", "launched",
        "wrote", "refactored", "automated", "integrated", "deployed",
    ]
    verb_hits = sum(1 for v in action_verbs if v in text_lower)
    verb_score = min(15, verb_hits * 2)
    score += verb_score
    details["action_verbs"] = f"{verb_hits} action verbs found"
    if verb_hits < 5:
        gaps.append({"category": "weak_verbs", "message": "Bullet points lack action verbs — start each bullet with a strong verb (Built, Designed, Reduced…)"})

    # 5. Links present (10 pts)
    links = re.findall(r'https?://\S+|github\.com/\S+|linkedin\.com/\S+', text_lower)
    link_score = min(10, len(links) * 3)
    score += link_score
    details["links"] = f"{len(links)} links found"
    if len(links) < 2:
        gaps.append({"category": "few_links", "message": "Add links: GitHub profile, LinkedIn, and project repos/demos"})

    # 6. Length check (10 pts)
    word_count = len(text.split())
    if 300 <= word_count <= 700:
        score += 10
        details["length"] = f"{word_count} words (good range: 300–700)"
    elif word_count < 300:
        score += 3
        details["length"] = f"{word_count} words — too short, needs more content"
        gaps.append({"category": "too_short", "message": "Resume is too sparse — add more detail to experience and projects sections"})
    else:
        score += 5
        details["length"] = f"{word_count} words — may be too long for new grad (aim for 1 page)"
        gaps.append({"category": "too_long", "message": "Resume may be too long — condense to 1 page for new grad roles"})

    return {"score": score, "gaps": gaps, "details": details}


def score_band_comment(score: int) -> str:
    if score < 40:
        return "This resume would lose to a templated one. Start over on the bullets."
    if score < 60:
        return "Readable, but it won't survive a 30-second recruiter skim. Fix the top 3 gaps."
    if score < 80:
        return "Solid bones. A couple targeted fixes and this clears most screens."
    return "Actually good. Stop fiddling with it and go apply."


def main():
    parser = argparse.ArgumentParser(description="Score a markdown resume (0-100) with a gap list")
    parser.add_argument("path", nargs="?", default="-", help="Resume file path (default: stdin)")
    parser.add_argument("--roast", action="store_true", help="Same scoring, blunter delivery — still ends in the real fix")
    args = parser.parse_args()

    text = load_text(args.path)
    result = score_resume(text)

    if args.roast:
        print(f"\nResume Roast — {result['score']}/100 (be glad this isn't live)\n")
        print(score_band_comment(result["score"]))
        if result["gaps"]:
            print("\nWhat's actually wrong, in order:")
            for i, gap in enumerate(result["gaps"], 1):
                roast = ROASTS.get(gap["category"], gap["message"])
                print(f"  {i}. {roast}")
                print(f"     fix: {gap['message']}")
        else:
            print("\nNo major gaps found. Annoyingly, this one's fine.")
        print()
        return

    print(f"\nResume Score: {result['score']}/100\n")
    print("Details:")
    for key, val in result["details"].items():
        print(f"  {key}: {val}")

    if result["gaps"]:
        print(f"\nGaps (fix in this order):")
        for i, gap in enumerate(result["gaps"], 1):
            print(f"  {i}. {gap['message']}")
    else:
        print("\nNo major gaps found.")

    print()


if __name__ == "__main__":
    main()
