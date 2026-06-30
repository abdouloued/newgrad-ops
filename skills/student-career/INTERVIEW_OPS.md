# Interview Ops

Handles coding interview prep: pattern diagnosis, company-specific problems, spaced review, and structured explanations.

Data sources: `data/interview/neetcode150-map.json`, `blind75-map.json`, `monster50-map.json`, `patterns.json`

Lookups in every command below can be done with `python scripts/search_problems.py` (`--slug`, `--title`, `--pattern`, `--difficulty`, `--list`) instead of reading the JSON by hand.

---

## Commands

### `/student interview diagnose <problem>`

Explain the pattern, recognition cue, common trap, and review schedule for a problem.

**Steps:**
1. Look up problem in the JSON maps by slug or title: `python scripts/search_problems.py --slug <slug>` or `--title "<keyword>"`
2. Identify pattern from `patterns.json`
3. Output structured explanation

**Output format:**
```
Problem: Longest Substring Without Repeating Characters

Pattern: Sliding Window
Cue: longest contiguous subarray/substring with a uniqueness or budget constraint
Trap: moving the left pointer one step at a time instead of jumping past the duplicate
Difficulty: Medium

Text: solve it locally; LeetCode editorial is free if you're stuck
Video: https://neetcode.io/problems/longest-substring-without-duplicates (NeetCode free)
AlgoMonster: https://algo.monster/practice (Monster 50 list)

Appears in: NeetCode 150 · Monster 50 · Blind 75

Spaced review:
  Next: tomorrow
  Then: in 3 days
  Then: in 7 days
```

---

### `/student interview company <name>`

List problems matching a company's documented focus areas. The problem maps
have no per-problem company tags (that data is paywalled on most sites and
out of scope per [AGENTS.md](../../AGENTS.md) — we don't reproduce scraped
premium content). Instead this command cross-references public, named focus
areas with the pattern field already in the maps.

**Steps:**
1. Read `data/companies/<name>.md` → `## Focus areas` / `## Recommended prep` for the patterns it names (e.g. "graphs", "sliding window", "DP")
2. Query the problem maps for that pattern, e.g.:
   `python scripts/search_problems.py --pattern "Sliding Window" --pattern "Graphs" --difficulty Medium`
3. Group results by pattern, sorted easy → hard

**Output format:**
```
Company: Google
Focus areas (from data/companies/google.md — public sources):
  DSA depth: graphs, DP, trees. Big-O analysis always required.

Matching problems (pattern-matched, not official company lists):

Graphs:
  - Course Schedule (Medium) — NeetCode: https://neetcode.io/problems/course-schedule
  - Number of Islands (Medium) — NeetCode: https://neetcode.io/problems/count-number-of-islands

Dynamic Programming:
  - Longest Increasing Subsequence (Medium) — NeetCode: https://neetcode.io/problems/longest-increasing-subsequence

Note: these are pattern-matched recommendations based on Google's publicly
documented interview focus, not a leaked or scraped company question list.
```

---

### `/student interview weak-patterns`

Identify patterns with the lowest solve rate in the student's tracked history.

**Steps:**
1. Ask for solved problem list (slugs or titles) or read from a local file if provided
2. Map to patterns via the JSON data
3. Compute coverage per pattern
4. Rank weakest patterns first

**Output format:**
```
Pattern Coverage Report

Strong (>70% solved):
  Arrays / Hashing: 5/6 ✓
  Two Pointers: 3/4 ✓

Needs work (30–70%):
  Trees: 4/7 — missing: diameter, level order, serialization
  Graphs: 2/6 — missing: union-find, topological sort, course schedule

Weak (<30%):
  Dynamic Programming: 1/5 — missing: house robber, coin change, LCS, edit distance
  Backtracking: 0/3 — not started

Recommended drill order:
  1. DP (highest ROI for final rounds)
  2. Graphs (common in system design roles)
  3. Backtracking
```

---

### `/student interview review-today`

Show problems due for spaced repetition review.

**Steps:**
1. Read the solve log (provided in context or from a local file)
2. Check dates against review intervals from `patterns.json` (next-day, 3-day, 7-day)
3. List problems due today

**Output format:**
```
Review Due Today — 2026-07-01

3 problems:
  - Two Sum (Arrays) — last solved 2026-06-24 (7 days ago)
  - Valid Parentheses (Stack) — last solved 2026-06-28 (3 days ago)
  - Longest Substring Without Repeating Characters (Sliding Window) — last solved 2026-06-30 (1 day ago)

Tip: re-solve from scratch before checking the solution.
```

---

### `/student interview explain-with-links <problem>`

Explain a problem's pattern and link to free public resources.

**Steps:**
1. Look up problem in all three maps
2. Find its pattern entry in `patterns.json`
3. Output a structured explanation with links to public pages only

**Output format:**
```
Merge Intervals

Pattern: Intervals
Cue: given a list of intervals, merge overlapping ones
Trap: forgetting to sort by start time first; off-by-one on overlap condition

Approach:
  1. Sort intervals by start
  2. Initialize result with first interval
  3. For each next interval: if it overlaps last in result, extend end; else append

Key insight: two intervals [a,b] and [c,d] overlap iff c <= b

Free resources:
  NeetCode video: https://neetcode.io/problems/merge-intervals
  AlgoMonster (Monster 50): https://algo.monster/practice

Difficulty: Medium
Appears in: NeetCode 150 · Monster 50
```
