# OpenAI

## Format

- **Stages:** Application → Resume screen → Coding/technical assessment → 4–6 final-round interviews (one or two days, 4–6 interviewers)
- **Coding tools:** HackerRank or CoderPad for the initial assessment
- **Coding style:** **Not LeetCode-style.** The assessment is typically a sequential, multi-part challenge — debugging or extending an existing piece of code, optimizing it, adding a feature — where you must pass each part before the next unlocks. You may see an algorithmic problem, but it's more common to be asked to reason about a realistic system than to solve a puzzle from scratch.
- **Lookups allowed:** Varies by stage — assessment is usually closed-book; live interviews may allow docs
- **AI usage:** Not officially published as of this writing. Treat live interviews as no-AI unless told otherwise; the assessment instructions will say explicitly if a stage permits it.

## Focus areas

- Practical engineering judgment over raw algorithm speed — code quality, clarity, and tradeoff reasoning are scored alongside correctness
- Systems programming: performance optimization, efficient data handling
- API design: building robust, scalable interfaces
- Data structures for ML workloads: efficient handling of large datasets, tokenization
- Distributed systems fundamentals: parallelism, fault tolerance
- Python is the primary language; Rust and Go show up in infrastructure-adjacent roles

## Behavioral

Core themes:
- **Impact** — what you built and what changed because of it
- **Collaboration** — working across teams and disciplines
- **Technical depth** — going beyond the surface in technical decisions
- **Safety awareness** — understanding of AI risks and tradeoffs (especially for technical/research-adjacent roles)

Suggested STAR stories:
1. A project where you had to make a fast technical decision under uncertainty
2. A collaboration that required navigating disagreement
3. A time you caught a reliability, correctness, or safety issue before it shipped

## Recommended prep

**Coding:**
- Don't over-index on pure LeetCode grinding — practice reading and modifying unfamiliar code under time pressure, not just solving from a blank file
- Still worth covering: graphs, DP, trees (these do show up)
- Practice explaining tradeoffs out loud as you code, not just narrating syntax
- Timed practice: treat each "level" of a multi-part problem as its own checkpoint — budget time so you don't burn it all on level 1

**Systems:**
- For SWE roles: review system design fundamentals (rate limiting, caching, queues)
- For ML/infra-adjacent roles: review model training pipeline and data infrastructure concepts

## Sources

- [OpenAI interview process & timeline — IGotAnOffer](https://igotanoffer.com/en/advice/openai-interview-process)
- [OpenAI software engineer interview guide — Exponent](https://www.tryexponent.com/guides/openai-software-engineer-interview)
- [OpenAI's interview process & questions — interviewing.io](https://interviewing.io/openai-interview-questions)
- Note: OpenAI has not published a single official candidate-process page as detailed as Anthropic's; the above are third-party prep sites aggregating reported candidate experiences, same tier of sourcing as the Google/Meta/Stripe packs in this repo. Verify against `openai.com/careers` before your interview — formats change.
