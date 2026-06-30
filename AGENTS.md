# AGENTS.md

Instructions for AI coding assistants (Claude Code, Codex CLI, Gemini CLI, Cursor,
or any agent) operating in this repository.

## What this repo is

`newgrad-ops` is a local, file-based job-search toolkit for students. The agent's
job is to read the skill files in `skills/student-career/` and the data in
`data/` to produce **draft documents** — prep packs, tailored resumes, outreach
messages, review schedules. It is not a service, it has no backend, and it
should never act on the student's behalf outside the repo.

## How to load the skill

1. Read [skills/student-career/SKILL.md](skills/student-career/SKILL.md) first — it indexes every
   `/student` command and points to the relevant `*_OPS.md` module.
2. Before executing a command, read the specific `*_OPS.md` file it belongs to.
3. Pull supporting data from `data/companies/`, `data/interview/`, and
   `data/recruiting/` as needed — do not invent company interview formats or
   problem metadata that isn't in those files.
4. If a company isn't in `data/companies/`, say so and offer to draft a new
   file from public sources rather than guessing.

## Hard rules

- **Never send anything.** No emails, no DMs, no form submissions, no API
  calls to job boards or ATSs. All outreach and application content is
  written to a file or the chat for the student to copy and send themselves.
- **Never auto-apply.** Application plans and tracker updates are proposals;
  the student decides what to submit and when.
- **Never fabricate a referral or contact.** Referral and alumni-outreach
  templates require a real name/connection supplied by the student. If none
  exists, say so instead of inventing one.
- **Never scrape or reproduce paywalled content.** Interview problem links
  must point to public pages (e.g. `neetcode.io/problems/*`,
  `algo.monster/practice`, public LeetCode problem statements). Do not copy
  premium company-tag lists or paid course content into this repo.
- **Cite sources for company data.** Any claim about a company's interview
  process, tools, or AI policy in `data/companies/*.md` must trace to a
  public careers page or candidate-guidance doc. Don't state hiring-process
  details from memory without a citation.
- **Scripts in `scripts/` are local-only.** They must not make network
  requests and must not write files without the user explicitly asking —
  default to printing results to stdout.

## When extending the repo

- New company pack: add `data/companies/<name>.md` following the structure
  of `data/companies/anthropic.md` (interview format, AI-usage policy, focus
  areas, behavioral angles), each claim cited.
- New problems: add entries to the relevant JSON map in `data/interview/`
  with `pattern`, `difficulty`, a public URL, and at least one trap.
- New template: keep it plain markdown, no placeholders that silently imply
  fabricated info (use explicit `[FILL IN: ...]` markers instead).
