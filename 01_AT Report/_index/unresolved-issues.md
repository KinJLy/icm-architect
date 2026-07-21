# Unresolved issues

Consolidated from the restructure of `markdown_files/` into this ICM workspace. Nothing here was silently resolved — each item needs a human decision or missing source material before the affected case/reference can be treated as final. Grouped by scope; check the linked file for full context before acting.

## Workspace-level

- [x] ~~`01_AT Report/Original Text files.zip`~~ — checked: it's the same 19 chat transcripts as plain `.txt`, byte-for-byte equivalent in content to what's already in `_archive/chat-transcripts/` (verified by line-count diff on `Bioness L300 Go 보고서`). Moved into `_archive/chat-transcripts/`. No new information — does not resolve the missing logbook weeks below.
- [ ] **`markdown_files/PDFs/`** — rendered PDF exports of the *old* file structure; not regenerated or reconciled against the new `references/` + `records/` layout. Treat as stale once the underlying `.md` content changes.
- [ ] **`01_AT Report/Documentation/`** (added later) holds real source files — the actual v3(5)–v3(11) Word draft series, factory templates (`KOrthotics_NDIS_High_Cost_AT_Master_Submission_Template.docx`, `NDIS_High_Cost_AT_Report_Template.docx`, `NDIS_High_Cost_AT_Report_Cover_Executive_Summary.docx`), and raw evidence PDFs. The report draft has been mined (see M's section below); **the factory templates have not been** — they may refine or replace `references/report-block-structure.md` and `references/org-info.md` further. Left in place, not reorganised into `records/`/`references/`, since that means moving several large binaries and hasn't been asked for.
- [ ] **`Re_ Megan Hollway.eml`** — per instruction, not opened. Still sitting in `Documentation/` whenever it's wanted.

## M / Megan Hollway — Bioness L300 Go (records/m-bioness-l300go/)

**Resolved by finding the actual v3(11) Word draft in `Documentation/`** (previously the top items in this section): report body reconciliation, NDIS goal wording (the "reviewer's rewrite" version was confirmed as what's actually in the final draft — see `05_report-draft/output/draft-participant-goals-section.md`), appendix structure (A–F confirmed, no separate goals appendix), trial/washout exact dates, full outcome-measure tables including mid-trial values, participant's real name, and confirmation that device-usage-analytics (B3) was addressed in the appendix list (even though the file itself still isn't located).

**Resolved by a second Documentation/ update:** Attachment E1 (`Letter from Neurologist.pdf` — Dr Colin Mahoney, Liverpool Hospital, 20 April 2026, verified against §13.2's DF 3/5→4-/5 claim), Megan's DOB (19 Jan 1990, now in `report.md`'s cover table), and — after a follow-up addition — **every community-trial week (1–8) and every washout week (1–3) is now present as a raw PDF.**

New items surfaced by the same update:

- [ ] **New raw evidence found but not yet cited in the report:** `03_community-trial/output/balance-confidence-measures.md` — ABC Scale, Falls Efficacy Scale, and Fear of Falling Avoidance Questionnaire, dated 6 Feb 2026 (genuinely pre-community-trial). None of these three instruments appear in `report.md` §9.5's outcome-measures list. The Fear of Falling Avoidance Questionnaire shows avoidance ("Agree"/"Completely agree") on 13 of 14 items — strong, dated, signed evidence for a claim the report already makes qualitatively. Whether to add this is a clinical/editorial call, not made here.
- [ ] **New clinical fact surfaced, not yet reflected in the report:** the neurologist's letter documents two prior courses of Mavenclad (a high-efficacy MS disease-modifying therapy) with continued significant symptoms despite it — strengthens the existing-supports-are-insufficient argument in `report.md` §4/§6 but isn't mentioned there currently.
- [ ] **Some illegible handwriting on the Falls Efficacy Scale** (one item under "Walk around the house") — flagged in `balance-confidence-measures.md`, don't compute or cite a total score from the rough transcription without getting the original re-read.

Remaining, unrelated to the above:

- [ ] **Attachment F1 (supplier quotation) is missing entirely** — not in `Documentation/`, not anywhere in the workspace. Blocks a quantified value-for-money argument in `report.md` §17.
- [ ] **NDIS number is still a placeholder** in the source document — not fixable from within this workspace.
- [ ] **Attachment A3 (PSFS) and D1 (carer feedback) are located but not yet opened/verified** — only FSS and the neurologist letter have actually been cross-checked so far.
- [ ] **Attachment B3 (Bioness Clinician Programmer usage analytics)** not located as a standalone file — may or may not overlap with the training-graph tables already in `03_community-trial/output/logbook.md`.
- [ ] **No compliance-checklist pass has been run against `report.md` specifically.** One data anomaly is already flagged inline (§10.3, TUG mid-trial reading goes up before improving, unexplained in the source text) — there may be others; `references/submission-compliance-checklist.md` hasn't been checked item-by-item against this exact document yet.
- [ ] **Appendix C1 (participant feedback) not drafted as its own 1-page document** — quotes exist in `report.md` §11–12 but no standalone summary file.
- [ ] **Goal wording is still a paraphrase**, not confirmed against Megan's actual NDIS plan text (caveat noted inline in `report.md` §3.1).
- [ ] **QA line-edit correspondence in `_archive/chat-transcripts/Bioness L300 Go 보고서.md` not fully triaged** — the *general* patterns are in `references/submission-compliance-checklist.md`, but case-specific line edits from that back-and-forth (which may or may not already be reflected in v3(11) — not checked) were never compared against the final draft.
- [ ] **"NDIS Goals Alignment" narrative** in `_archive/chat-transcripts/NDIS AT 레포트 작성.md` and `Bioness L300 Go 보고서.md` — largely superseded by `report.md` §18.3, but not explicitly diffed against it to confirm nothing case-relevant was dropped.

## P — Custom AFO / CP (records/p-custom-afo-cp/)

- [ ] **No full clinical assessment on file** — only the funding-justification Q&A (`01_intake-assessment/output/clinical-justification.md`). ROM, tone, and gait findings needed for Block 3/5 of the report haven't been captured in this workspace; check whether they exist elsewhere before drafting.
- [ ] **Living situation and NDIS goals not on file** — needed for Block 2 (Participant Story).
- [ ] **Cost/quote for the custom AFO not on file.**
- [ ] **Report body not started** (`05_report-draft` empty).

## How to use this file

Work through a section, resolve or source the missing piece, then delete that line and update the relevant case's `CONTEXT.md` "Outstanding" list to match. This file is hand-maintained, not generated — if it drifts from the case `CONTEXT.md` files, they're the more detailed source; reconcile this file to match them, not the other way round.
