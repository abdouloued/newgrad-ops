# Company Ops

Generates company-specific prep packs that combine application guidance, interview format, OA prep, and behavioral story angles.

Data source: `data/companies/<name>.md`

---

## Command

### `/student company <name>`

Generate a full prep pack for the named company.

**Steps:**
1. Load `data/companies/<name>.md`
2. If the company file does not exist, generate a best-effort pack using public information and flag it as unverified
3. Cross-reference OA patterns with `data/interview/` maps
4. Output the prep pack

**Output format:**
```
────────────────────────────────────────
[Company] Prep Pack
────────────────────────────────────────

APPLICATION
  Role types to target: [new grad / intern roles]
  Resume focus: [what to emphasize]
  Portfolio signal: [what projects matter]
  Fit score tip: [highest-leverage resume change]

INTERVIEW FORMAT
  [sourced from public careers page / candidate guidance]
  Stages: [e.g. OA → phone screen → technical → final]
  Tools used: [e.g. Colab, CodeSignal, HackerRank]
  Coding style: [LeetCode-style algorithmic / live escalating challenge / practical-debugging / take-home production code — pull straight from the company file's "Coding style" line, don't assume every company runs a LeetCode grind]
  AI policy: [what the company says publicly]
  Lookups allowed: [yes/no/context-dependent]

OA PREP
  Focus patterns: [top 3 patterns to drill]
  Time pressure: [typical time limits if known]
  Recommended problems from NeetCode 150 / Monster 50:
    - [problem] ([pattern]) — [link]
    - [problem] ([pattern]) — [link]

BEHAVIORAL
  Core themes the company looks for: [e.g. judgment, ownership, ambiguity]
  Suggested STAR stories to prepare: [3 story prompts]

WEEKLY PLAN
  Mon: [coding drill]
  Tue: [resume/portfolio task]
  Wed: [coding drill]
  Thu: [mock or timed practice]
  Fri: [outreach / application task]

Sources: [public URLs cited for interview format and AI policy]
Note: Interview formats change. Verify against the current careers page.
────────────────────────────────────────
```

---

## Company files

Company data lives in `data/companies/`. Each file is a markdown document with:

- `## Format` — interview stages, tools, and a **Coding style** line (from public careers page). Companies differ a lot here — Google and Meta run classic closed-book LeetCode-style algorithmic rounds; Anthropic runs a live, escalating multi-tier challenge in a shared Python environment; OpenAI leans practical (debug/extend existing code over blank-file algorithm puzzles); Stripe's take-home is closer to a small production feature than a DSA problem. Don't assume "coding interview" means "LeetCode" — read this line before recommending a prep plan.
- `## AI policy` — what the company says publicly about candidate AI use
- `## Focus areas` — technical emphasis for this company
- `## Behavioral` — themes, culture signals
- `## Sources` — public URLs

Covered companies: Anthropic · OpenAI · Google · Meta · Stripe

To request a new company pack, add a file at `data/companies/<name>.md` following the same structure.
