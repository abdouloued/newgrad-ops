# student-career

**Skill for:** Claude Code · Codex · Gemini CLI · Cursor · any AI coding assistant

Turn your AI coding assistant into a new-grad job-search command center.
Track applications, tailor resumes, prep for OAs, grind company-specific LeetCode,
audit your GitHub portfolio, manage referrals, and build a weekly recruiting plan.

---

## Trigger keywords

internship, new-grad, job search, application, resume, OA, online assessment,
LeetCode, interview prep, company prep, portfolio audit, referral, recruiting

---

## Module index

| Module | File | What it does |
|---|---|---|
| Apply Ops | `APPLY_OPS.md` | Application tracking, fit scoring, resume tailoring, follow-ups |
| Interview Ops | `INTERVIEW_OPS.md` | LeetCode diagnosis, pattern drills, spaced review, company problems |
| Company Ops | `COMPANY_OPS.md` | Company-specific prep packs (format, focus, weekly plan) |
| Portfolio Ops | `PORTFOLIO_OPS.md` | GitHub audit, README upgrade, project-role matching |
| Referral Ops | `REFERRAL_OPS.md` | Alumni maps, referral DMs, recruiter outreach drafts |

---

## Command index

```
/student apply-plan                  Build a weekly application plan
/student fit-score <job-url>         Score role fit vs current resume
/student tailor-resume <job-url>     Generate targeted resume diff
/student roast-resume <resume>       Blunt version of fit-score — same checks, no sugar-coating
/student track <company>             Log application status
/student follow-up                   Draft a follow-up email

/student interview diagnose <problem>  Explain pattern, cue, traps for a problem
/student interview company <name>      List problems matching that company's documented focus areas
/student interview weak-patterns       Identify your lowest-solved patterns
/student interview review-today        Show problems due for spaced review
/student interview explain-with-links <problem>  Explain + link public resources

/student company <name>              Full company prep pack (apply + interview + behavioral)

/student portfolio-audit             Score GitHub profile and top repos
/student github-readme <repo>        Generate upgraded project README draft
/student project-match <job-url>     Map projects to role requirements
/student project-upgrade-plan        Prioritized list of project improvements

/student referral-map <company>      Find alumni and potential referrers
/student alumni-message <company>    Draft a LinkedIn alumni outreach message
/student recruiter-dm <role>         Draft a recruiter cold DM
/student follow-up-referral          Draft a referral follow-up message
```

---

## Data files

- `data/companies/*.md` — company interview format and prep guidance
- `data/interview/neetcode150-map.json` — NeetCode 150 problems with patterns and traps
- `data/interview/blind75-map.json` — Blind 75 subset
- `data/interview/monster50-map.json` — AlgoMonster Monster 50
- `data/interview/patterns.json` — pattern cues, traps, spaced-review intervals
- `data/recruiting/` — application statuses and recruiting calendar

## Templates

- `templates/resumes/new-grad-template.md`
- `templates/outreach/referral-dm.md`
- `templates/outreach/recruiter-cold.md`
- `templates/followups/`
- `templates/behavioral-stories/star-template.md`
- `templates/github-readmes/project-readme-template.md`

## Scripts

- `scripts/score_resume.py` — local resume scorer (0–100 + gap list); `--roast` for blunt delivery of the same checks
- `scripts/score_readme.py` — GitHub README quality scorer
- `scripts/generate_review_schedule.py` — spaced repetition schedule from solved list
- `scripts/search_problems.py` — search the problem maps by slug, title, pattern, or difficulty; backs `interview diagnose`, `interview company`, and `interview explain-with-links`
- `scripts/validate_repo.py` — repo-wide consistency check (JSON schema, duplicate slugs, broken links, script smoke tests); same checks CI runs on every PR

---

## Safety principles

- No auto-apply, no auto-email, no automated outreach
- No scraping paid content (LeetCode Premium, AlgoMonster Pro)
- All generated resumes and messages are **drafts** — review before sending
- Company prep packs cite public sources only
- No destructive file writes — scripts print to stdout
