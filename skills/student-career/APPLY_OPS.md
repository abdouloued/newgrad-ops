# Apply Ops

Handles the full application workflow: planning, fit scoring, resume tailoring, status tracking, and follow-ups.

---

## Commands

### `/student apply-plan`

Build a weekly application plan based on the student's target roles and current resume.

**Steps:**
1. Ask for target role type (SWE intern, new-grad SWE, PM, data, etc.) if not stated
2. Ask for graduation date or timeline
3. Read current resume from context or ask for paste
4. Generate a prioritized list of 5–10 companies to target this week
5. For each: fit estimate, resume gap, and one action item
6. Output a day-by-day plan (Mon–Fri)

**Output format:**
```
Weekly Application Plan — [date]

Target: New-Grad SWE | Timeline: May 2026

Priority applications this week:
1. Anthropic — fit 74/100 | gap: ML infra, evals | action: tailor projects section
2. Stripe — fit 81/100 | gap: distributed systems | action: add scale numbers to resume
3. Linear — fit 68/100 | gap: TypeScript, product sense | action: add frontend project

Day-by-day:
Mon: tailor resume for Anthropic + apply
Tue: tailor resume for Stripe + apply
Wed: 5 sliding window problems (Anthropic OA prep)
Thu: portfolio README upgrade
Fri: referral outreach to 2 alumni
```

---

### `/student fit-score <job-url>`

Score how well the student's current resume matches a job posting.

**Steps:**
1. Fetch or receive the job description
2. Extract required skills, preferred skills, and role signals
3. Compare against resume (provided in context or pasted)
4. Score 0–100
5. List gaps in priority order

**Output format:**
```
Fit Score: 74/100

Company: Anthropic
Role: Software Engineer, New Grad

Matched: Python ✓, distributed systems ✓, API design ✓
Gaps (high priority):
  - ML infrastructure / evals experience
  - LLM tooling (mentioned 3x in JD)
  - Reliability and observability

Resume sections to update:
  - Projects: reframe toward AI tooling / infra
  - Skills: add any relevant ML frameworks
  - Summary: add AI safety motivation
```

---

### `/student tailor-resume <job-url>`

Generate a targeted diff of resume changes for a specific role.

**Steps:**
1. Read current resume
2. Fetch job description
3. Generate a rewrite of the most impactful 2–3 bullet points per section
4. Output as a diff (before / after), not a full resume rewrite

**Output format:**
```
Resume Tailoring — Anthropic SWE New Grad

Projects > [Your project name]
  Before: Built a REST API for user data management
  After:  Built a reliability-focused REST API handling 50k req/day; added structured logging and alerting

Summary
  Before: Software engineer with experience in backend and APIs
  After:  Software engineer interested in building reliable AI infrastructure and developer tools

Note: These are draft suggestions. Review for accuracy before applying.
```

---

### `/student track <company>`

Log an application status update.

**Steps:**
1. Ask for: company, role, date applied, current status
2. Output a formatted log entry to paste into a tracking file
3. Suggest next action based on status

**Statuses:** applied · OA sent · OA completed · phone screen · technical · final round · offer · rejected · ghosted

---

### `/student follow-up`

Draft a professional follow-up email after applying or after an interview.

**Steps:**
1. Ask: company, role, what happened last (applied / interviewed / OA)
2. Ask: recruiter or interviewer name if known
3. Generate a short, non-pushy follow-up email draft
4. Note: output is a draft — do not auto-send

**Output format:**
```
Subject: Following up — [Role] at [Company]

Hi [Name],

I wanted to follow up on my application for the [Role] position. I'm very excited about [specific thing about the company/role] and would love to continue the conversation.

Please let me know if there's anything else I can provide.

Best,
[Your name]

Note: This is a draft. Review and personalize before sending.
```
