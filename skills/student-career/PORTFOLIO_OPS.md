# Portfolio Ops

Audits GitHub profile and projects, generates upgraded READMEs, matches projects to job requirements, and produces a prioritized improvement plan.

---

## Commands

### `/student portfolio-audit`

Score the student's GitHub portfolio and return a prioritized fix list.

**Steps:**
1. Ask for GitHub username or ask student to paste top 3 project READMEs
2. Score each repo on: deployed demo, tests, architecture docs, "why this matters" section, code quality signals
3. Score overall profile on: pinned repos, contribution graph, profile README
4. Output score + ranked fix list

**Scoring rubric:**

Up to 3 repos, scored 0–20 each (max 60):
- Demo / live link present: +4
- Tests present (any test file): +4
- Architecture or design section in README: +4
- "Why this matters" / motivation section: +4
- Benchmark, eval, or performance data: +4

Profile-level, scored out of 40:
- Pinned repos showcase real projects, not forks/coursework: 0–15
- Active contribution graph (recent, consistent activity): 0–10
- Profile README present and informative: 0–15

Overall score = repo subtotal (/60) + profile-level (/40) = /100

**Output format:**
```
Portfolio Audit

Overall score: 58/100

Top repo — [project name]: 9/20
  ✓ Has live demo link
  ✗ No tests
  ✗ No architecture section
  ✗ No "why this matters" section
  ✗ No performance data

Fixes (prioritized by hiring signal):
  1. Add tests — the #1 signal engineers look for in new-grad projects
  2. Write a "Why I built this" section (3 sentences)
  3. Add architecture diagram (even a text ASCII one)
  4. Deploy and link a live demo
  5. Add one benchmark or metric

Before → After estimate: 58/100 → 82/100 with these 5 fixes
```

---

### `/student github-readme <repo>`

Generate an upgraded project README draft.

**Steps:**
1. Ask for current README content or repo name
2. Generate a full improved README using the template in `templates/github-readmes/project-readme-template.md`
3. Flag all [PLACEHOLDER] sections that need real content

**Output:** full markdown README draft — review and fill in placeholders before pushing.

---

### `/student project-match <job-url>`

Map existing projects to a job description's requirements.

**Steps:**
1. Fetch or receive the job description
2. Extract required and preferred technical areas
3. Map each of the student's projects to job requirements
4. Identify coverage gaps (requirements with no matching project)

**Output format:**
```
Project-Role Match — Anthropic SWE New Grad

Your projects vs. role requirements:

  [API project] → covers: REST, reliability, Python ✓
  [CLI tool] → covers: developer tooling, OSS contribution ✓
  [ML course project] → covers: ML basics (weak signal for infra roles)

Gaps (no project coverage):
  - Distributed systems / multi-service architecture
  - Evaluation / evals pipeline
  - Observability and monitoring

Recommendation:
  Build or document one project that shows distributed systems or evals work.
  Even a small load-testing or benchmarking writeup raises your signal significantly.
```

---

### `/student project-upgrade-plan`

Produce a prioritized plan to improve existing projects for a target role.

**Steps:**
1. Ask for target role type and current projects
2. Score each project against role signals
3. Output a ranked upgrade plan (highest ROI first)

**Output format:**
```
Project Upgrade Plan — Target: AI/infra new-grad roles

Priority 1 (high ROI, 2–4 hours):
  [API project] — add structured logging + error metrics
  Why: infra/reliability roles look for observability

Priority 2 (medium ROI, 1–2 hours):
  [CLI tool] — add a README demo GIF and install instructions
  Why: OSS polish signals attention to user experience

Priority 3 (low ROI but visible):
  [ML project] — reframe README toward "evaluation" rather than "training"
  Why: evals vocabulary resonates with AI-adjacent roles
```
