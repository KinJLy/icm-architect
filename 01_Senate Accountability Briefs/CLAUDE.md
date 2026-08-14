---
custom-width: 77
---
# Senate Accountability Briefs — NDIS Amendment Bill

A record library of 76 senators. Each senator gets a record that accumulates data, gets checked, and reaches a validated state — then gets personalized and finalized into a Word brief and a cover email, ready to send. Nothing "runs" to completion here; records get created, filled in, and looked up.

Built on ICM: folders carry sequencing, hierarchy carries context, files carry state. The structure is the documentation — if something needs explaining, the explanation goes in that folder's own file, not in your head.

## Works with any LLM — read this before assuming you're stuck

This ICM does not require Claude or Claude Code specifically. It has two paths:

- **Scripted path** (this session, or any agent with Python + code execution): the `_system/tools/*.py` scripts do the data lookup, maths, and Word formatting. Needs `openpyxl`, `pypdf`, `python-docx`, `PyYAML` installed.
- **Chat-only path** (a plain chat window — ChatGPT, Claude.ai chat, Gemini, etc. — with no code execution): see [`01_reference/chat-only-workflow.md`](01_reference/chat-only-workflow.md). The binary source files (`.xlsx`, `.pdf`, `.docx`) are the actual blocker for this path — a chat window can't open them without running code — so `01_reference/source-data/senate-ndis-table.csv` and `senate-contact-list.csv` exist as plain-text exports specifically so they can be pasted into any chat. Everything else in this ICM is already plain markdown.

Don't assume a user is on Claude Code just because this file is named `CLAUDE.md` — check what they actually have access to before picking a path.

## Where things live

| Folder | What it holds |
|---|---|
| `01_reference/` | factory — the brief template + field legend, vote-position rules, portfolio-relevance rules, a dated senator-portfolios snapshot, source data (binary + plain-text CSV exports), the bill text, campaign context, the chat-only workflow guide, sender profile, and one polished example |
| `_templates/` | blank stamps: `senator-record.md`, `personal-note.md` — new work is a copy, not a blank page |
| `_index/log.md` | one line per senator: slug, party, state, vote position, status — generated/rebuilt, never hand-edited |
| `records/` | one folder per senator: `record.md` (data + validation) and, later, `personal-note.md` (optional) |
| `_system/tools/` | the pipeline scripts (below) plus `_selection.py` (shared `--party`/`--state`/`--all`/name filtering) |
| `02_output/` | rendered Word briefs from validated-or-not records — regenerate any time, sign-off stays blank |
| `03_ready-to-send/` | finalized output: Word brief + plain-text cover email, per senator, with sender identity and personal story filled in |
| `_archive/` | superseded template, the old AI-instructions doc, and draft briefs generated before this record/validation workflow existed |

## The pipeline

1. **Extract** — `python _system/tools/extract_senator_data.py "Senator Name"` (or `--party ALP` / `--state QLD` / `--all`) pulls workbook + contact list + vote-position rule + portfolio check into `records/{slug}/record.md`.
2. **Validate** — a human opens the record, checks the data, actively runs the portfolio-relevance check (don't default to skipping it), confirms the vote position, ticks the checklist, sets `validated: true`.
3. **Render (optional review step)** — `python _system/tools/render_brief_docx.py {slug}` (or `--party`/`--state`/`--all`) produces a docx in `02_output/` from whatever's in the record right now, validated or not — useful for reviewing before the record is fully signed off. Sign-off/personal-note stay blank at this stage.
4. **Finalize** — once `validated: true`: fill in `01_reference/sender-profile.md` (your name/role/email — one-time, factory-level) and optionally `records/{slug}/personal-note.md` (per-senator, see `_templates/personal-note.md` for the "dump it in or ask the LLM to help you draft it" options). Then `python _system/tools/finalize_send_pack.py {slug}` (or `--party`/`--state`/`--all`) writes both the final Word brief **and** a ready-to-paste plain-text cover email to `03_ready-to-send/`. This step **refuses to run on an unvalidated record** — that's the real gate, not step 3.
5. **Send** — open the cover email `.txt`, copy it into your email client, drag in the matching docx as an attachment, send.

## Route by what just happened

| If | Go to |
|---|---|
| starting a new senator | `python _system/tools/extract_senator_data.py "Senator Name"` |
| checking a senator's data | `records/{slug}/record.md` — tick the checklist, set `validated: true` |
| writing a personal story | copy `_templates/personal-note.md` → `records/{slug}/personal-note.md` |
| the field legend or a rule looks wrong | `01_reference/brief-template.md`, `vote-position-rules.md`, `portfolio-relevance.md` — confirm the fix before it's applied to any record |
| a record is validated, ready to send | `python _system/tools/finalize_send_pack.py {slug}` → `03_ready-to-send/` |
| asked "what's left to do" | scan `_index/log.md` (or `records/*/record.md` frontmatter) |
| no code execution available | [`01_reference/chat-only-workflow.md`](01_reference/chat-only-workflow.md) |
| the source workbook/contact-list PDF changed | `python _system/tools/export_plaintext_sources.py` to refresh the CSV exports |

## The one rule

A record isn't done because the data was pulled — it's done when a human has ticked its validation checklist and set `validated: true`. `finalize_send_pack.py` enforces this: it will not produce a send-ready brief or cover email for an unvalidated record. Don't bypass that gate.
