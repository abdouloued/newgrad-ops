# Referral Ops

Helps students find alumni connections, draft ethical outreach messages, and follow up on referral requests.

**Safety note:** All outputs are drafts for manual sending. No auto-outreach. No mass messaging. Every message should be reviewed, personalized with real context, and sent one at a time.

---

## Commands

### `/student referral-map <company>`

Find where to look for alumni and potential referrers at a target company.

**Steps:**
1. Ask for student's school (for alumni filtering)
2. Output a structured guide on where and how to find connections — not a scraped list

**Output format:**
```
Referral Map — Anthropic

Where to find connections:
  1. LinkedIn: search "[Your School] Anthropic" — filter by 2nd connections
  2. LinkedIn: search "Anthropic engineer" → filter by alumni
  3. School career portal / alumni directory (check if your school has one)
  4. Handshake (if your school uses it) — Anthropic may have a presence
  5. Discord servers (AI/ML communities, Anthropic public channels if any)
  6. GitHub: contributors to Anthropic public repos

Warm leads first: prioritize anyone who went to your school or worked at a shared past company.

Note: Do not use any service that requires scraping or paying for contact data.
```

---

### `/student alumni-message <company>`

Draft a LinkedIn message to an alumnus at the target company.

**Steps:**
1. Ask for: alumnus name, company, role, shared connection (school / past job)
2. Generate a short, genuine, non-pushy message (under 300 characters for LinkedIn connection request, under 800 for InMail)

**Output format:**
```
LinkedIn Connection Request Draft — Anthropic

Hi [Name],

I'm a [year] [School] [Major] student interested in [role type] roles at Anthropic.
I saw you went to [School] too — would love to connect and hear about your path
if you have a few minutes.

[Your name]

— 247 characters. Review and personalize before sending.
Note: This is a draft. Do not send to multiple people with the same text.
```

---

### `/student recruiter-dm <role>`

Draft a cold message to a recruiter for a specific role.

**Steps:**
1. Ask for: recruiter name, company, role title, one specific thing about the role or company
2. Generate a short, specific, non-generic message

**Output format:**
```
LinkedIn Message Draft — Recruiter at Anthropic

Hi [Name],

I applied for the [Role] position at Anthropic last week and am very excited
about the opportunity to work on [specific team/product area].
I'd love to connect if you have availability.

[Your name]

Note: This is a draft. Personalize the specific detail before sending.
```

---

### `/student follow-up-referral`

Draft a follow-up message to someone who agreed to refer you.

**Steps:**
1. Ask for: referrer name, company, role, how long since they agreed

**Output format:**
```
Follow-Up Draft — Referral

Hi [Name],

Just wanted to follow up — I submitted my application for [Role] at [Company]
on [date]. Wanted to let you know in case there's anything you need from my end
to complete the referral. Really appreciate your help!

[Your name]

Note: This is a draft. Keep it short and grateful.
```
