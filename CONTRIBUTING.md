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
`data/companies/anthropic.md` (`## Format` — including a `Coding style` line,
`## Focus areas`, `## Behavioral`, `## Recommended prep`, optionally
`## Community reports`, and `## Sources`). Every factual claim about
interview process needs a cited public source.

File by current legal/brand name, not historical ones — Meta's file is
`meta.md`, not `facebook.md`, since Facebook the company was renamed to Meta
in 2021. If a rename happens again, rename the file in the same PR as the
update rather than adding a duplicate.

**On `## Community reports`:** individual candidates write detailed, public
posts about their interview experience all the time (Medium, personal blogs,
named Reddit/LinkedIn posts) and these are genuinely useful — they're often
more current and specific than aggregator sites. You can cite a few, by name,
with a one-line note on what each adds. What you can't do: bulk-scrape
Glassdoor/Blind/LeetCode Discuss into this file. Those sites gate that data
behind login/ToS specifically to prevent scraping, and AGENTS.md's "no
scraped content" rule applies here too. One contributor manually citing one
post they actually read is the model — not an automated aggregator.

### Fix a template or OPS module

`skills/student-career/*_OPS.md` define the `/student` commands. If you
change a command's behavior, update both the OPS file and the command index
in `skills/student-career/SKILL.md` — they must stay in sync.

## Good first issues

- **Add more company packs.** Apple, Netflix, Nvidia, and most mid-size
  AI/infra startups aren't covered yet. Amazon, Microsoft, Anthropic, OpenAI,
  Google, Meta, and Stripe are.
- **Add `## Community reports` to the older company files.** Anthropic,
  OpenAI, Google, Meta, and Stripe don't have one yet — Amazon and Microsoft
  do, use those as the reference format.
- **Build the CI Action mentioned below** — currently nothing blocks a PR
  from merging broken JSON or a dead link.
- NeetCode 150 is exactly 150, Monster 50 is exactly 50, and Blind 75 has 76
  (the canonical list is 75, but we picked up a duplicate-flagging fix that
  left one extra real problem in — not worth removing a correct entry just
  to hit a round number). If NeetCode revises its official list, that's the
  next thing to reconcile.

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
