# Contributing to newgrad-ops

Thanks for considering a contribution. This repo lives or dies on the accuracy
of its data — a wrong interview format or a dead link costs a real student
real prep time. Read this before opening a PR.

## Ground rules (non-negotiable)

These mirror [AGENTS.md](AGENTS.md) — they apply to humans too:

1. **Cite public sources only.** Company interview format, AI-usage policy, and
   focus areas in `data/companies/*.md` must trace to a public careers page or
   candidate-guidance doc. Link it in the `## Sources` section.
2. **No paywalled or scraped content.** Problem links go to free pages —
   `neetcode.io/problems/*`, `algo.monster/practice`, public LeetCode problem
   statements. Don't add LeetCode Premium company-tag data or paid course
   content.
3. **No fabricated referrals or contacts.** Templates in `templates/outreach/`
   stay generic placeholders — don't add real names or scraped contact lists.
4. **Scripts stay local-only.** Anything in `scripts/` must not make network
   calls and must not write files without being asked — print to stdout.
5. **Verify URLs before adding them.** A dead or wrong link is worse than no
   link. If you're adding a NeetCode URL, load the page (or search for it) and
   confirm the slug — don't guess from the problem title.

## Ways to contribute

### Add or fix a problem entry

Each entry in `data/interview/*.json` needs: `slug`, `title`, `difficulty`,
`pattern` (must match a key in `data/interview/patterns.json`), a public URL,
and at least one real `traps` entry. Run the search script to sanity-check
your addition doesn't already exist and that the pattern name matches
existing usage:

```bash
python scripts/search_problems.py --title "your problem title"
```

### Add a company prep pack

Create `data/companies/<name>.md` following the structure of
`data/companies/anthropic.md` (`## Format`, `## AI policy`, `## Focus areas`,
`## Behavioral`, `## Recommended prep`, `## Sources`). Every factual claim
about interview process needs a cited public source.

### Fix a template or OPS module

`skills/student-career/*_OPS.md` define the `/student` commands. If you
change a command's behavior, update both the OPS file and the command index
in `skills/student-career/SKILL.md` — they must stay in sync.

## Good first issues

- **Fill the Blind 75 gap.** `data/interview/blind75-map.json` currently has
  67 of the canonical 75 problems. Missing: the 5 Bit Manipulation problems
  (Sum of Two Integers, Number of 1 Bits, Counting Bits, Missing Number,
  Reverse Bits), 3 Matrix problems (Set Matrix Zeroes, Spiral Matrix, Rotate
  Image), and Valid Anagram. Adding these also means adding `Bit
  Manipulation` and `Matrix` pattern entries to `data/interview/patterns.json`
  (cue + common traps + review interval) since neither category exists there
  yet.
- **Expand NeetCode 150.** `data/interview/neetcode150-map.json` has 128 of
  150. Cross-check against the official NeetCode 150 list and fill gaps with
  verified URLs.
- **Add a company pack.** Amazon, Microsoft, Apple, and most mid-size
  AI/infra startups aren't covered yet.

## Testing your change

```bash
# JSON must parse
python3 -c "import json; json.load(open('data/interview/your-file.json'))"

# search script should surface your new entries
python scripts/search_problems.py --pattern "Your Pattern"

# resume/readme scorers should still run clean
python scripts/score_resume.py templates/resumes/new-grad-template.md
python scripts/score_readme.py templates/github-readmes/project-readme-template.md
```

There's no CI yet (also a good first issue — a GitHub Action that runs the
checks above on every PR would be welcome).

## Pull requests

- Keep PRs scoped to one company/problem-set/template at a time — easier to
  review, easier to merge.
- Explain *why* in the PR description if you're changing behavior, not just
  what changed.
- Link your sources for any factual claim.
