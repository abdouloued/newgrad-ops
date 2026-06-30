# Anthropic

## Format

- **Application:** Standard resume + cover letter optional
- **Stages:** Application → OA (if applicable) → Phone/Video Screen → Technical Interviews → Final Round
- **Video tool:** Google Meet (per careers page)
- **Coding tools:** Colab, CodeSignal, or Replit — a shared live Python environment, not a LeetCode-style judge
- **Coding style:** **Not classic LeetCode.** Reported format is a single problem that escalates across 3–4 tiers, each building on the code you already wrote (e.g. build a web crawler → make it multi-threaded → filter/aggregate results). The CodeSignal take-home version is similarly leveled: pass tests at one level to unlock the next.
- **Lookups allowed:** Yes — candidates may look things up, but should be comfortable with basic syntax and standard library usage
- **AI usage:** Only when explicitly permitted by Anthropic for that specific assessment. The company's candidate guidance states they will be clear when AI is allowed (e.g. "you may use Claude for this coding challenge"). Do not assume AI is allowed.

## AI policy

From anthropic.com/candidate-ai-guidance (public):
> During live interviews: this is all you — no AI assistance unless we indicate otherwise. We're curious to see how you think through problems in real time.
> For take-home assessments: complete these without Claude unless we indicate otherwise.

**What this means for prep:**
- Practice solving problems without autocomplete first
- Be able to explain your solution out loud, step by step
- If a CodeSignal OA allows lookups, use docs — not AI generation
- Prepare to think aloud and discuss tradeoffs

## Focus areas

- Python fluency (primary language for most technical roles)
- Data structures and algorithms (standard DSA depth)
- Systems thinking and reliability
- Debugging under time pressure
- Product and mission motivation (AI safety, helpful/harmless/honest)
- Judgment and reasoning about ambiguous situations

## Behavioral

Reportedly (per community accounts, not an officially published process detail) there's a dedicated ~45-minute "Culture Interview" every candidate goes through regardless of role or level — not a standard FAANG-style behavioral round, and relying on pre-packaged STAR answers is described as a common way to fail it. Treat this as anecdotal, but worth knowing going in.

Core themes Anthropic looks for:
- **Ownership** — taking a project from idea to shipped without being asked
- **Judgment under ambiguity** — making good calls with incomplete information
- **Intellectual curiosity** — digging into how things work, not just using them
- **Mission alignment** — genuine interest in safe and beneficial AI

Suggested STAR stories:
1. A time you shipped something without clear requirements
2. A time you disagreed with a decision and how you handled it
3. A time you debugged a hard problem you didn't understand at first

## Recommended prep

**Coding (OA and technical):**
- Practice in Colab or a plain Python notebook (no IDE autocomplete)
- Focus: sliding window, trees, graphs, intervals, DP basics
- Timed runs: 30–45 min per problem, explain aloud

**Portfolio:**
- Projects involving reliability, tooling, or AI are strong signals
- Tests, docs, and architecture writeups matter

**Company knowledge:**
- Read Anthropic's public research papers (at least abstracts)
- Understand Claude's product positioning vs. competitors
- Have a genuine, specific answer to "why Anthropic"

## Community reports

Individually-cited candidate write-ups, not scraped aggregate data:

- ["I failed my Anthropic interview and came to tell you all about it so you don't have to" — blog.goncharov.page](https://blog.goncharov.page/i-failed-my-anthropic-interview-and-came-to-tell-you-all-about-it-so-you-dont-have-to) — a failure-mode account, useful precisely because most public write-ups survive past the rejection stage.
- ["Inside Anthropic's Culture Interview" — Ridhima Khurana, Substack](https://ridhimakhurana.substack.com/p/inside-anthropics-culture-interview) — first-person detail on the ~45-minute Culture Interview every candidate goes through regardless of role/level; reports that pre-packaged STAR answers are a common failure mode there specifically.

## Sources

- https://www.anthropic.com/careers (interview process, tools)
- https://www.anthropic.com/candidate-ai-guidance (AI usage policy)
