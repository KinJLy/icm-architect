---
custom-width: 100
---
# 01_AT Report — Korthotics NDIS AT reporting workspace

Record library. Each **record** in `records/` is one participant's assistive-technology funding case; it accumulates evidence over months and internally runs the pipeline defined in `_templates/case-template/`.

## Where things live

| Need                                                       | Go to |
|---|---|
| Start a new case                                           | Copy `_templates/case-template/` into `records/<id>/`, fill in `CONTEXT.md`, add a line to `_index/log.md` |
| Check what cases exist and their status                    | `_index/log.md` |
| See everything still unresolved across all cases            | `_index/unresolved-issues.md` |
| Report structure, block/section numbering, appendix rules  | `references/report-block-structure.md` |
| Outcome measure definitions (TUG, 6MWT, PSFS, FSS, etc.)   | `references/outcome-measures.md` |
| Reusable Section 34 justification language                 | `references/justification-banks/` (one file per condition) |
| Research citations to cite in a report                     | `references/evidence-summary-*.md` (one file per condition) |
| Support letter templates (physio / orthotist / generic)    | `references/support-letter-templates.md` |
| 8-week community trial protocol + washout logbook template | `references/community-trial-protocol.md` |
| Clinical note → NDIS-ready phrasing conversions            | `references/ndis-phrasebook.md` |
| Pre-submission QA checklist                                | `references/submission-compliance-checklist.md` |
| Korthotics letterhead / ABN / contact details              | `references/org-info.md` |
| A specific participant's case files                        | `records/<case-id>/` |
| Raw source chat exports this workspace was built from      | `_archive/chat-transcripts/` (superseded — kept for provenance, not for reuse) |

## The pipeline every case record runs

`01_intake-assessment → 02_trial-request → 03_community-trial → 04_washout → 05_report-draft → 06_submission`

Not every case needs every stage — a straight custom-AFO case (no device trial) may only need `01_intake-assessment` before `05_report-draft`. See each record's own `CONTEXT.md` for which stages apply.

## Conventions

- Case id = `<initial-or-name>-<device-or-AT-type>-<condition>` (e.g. `m-bioness-l300go`, `p-custom-afo-cp`) — matches `_index/log.md`.
- Factory (`references/`, `_templates/`) is condition/device-general and stable across cases. Product (`records/*/`) is case-specific and changes every run.
- Everything here is real NDIS disability-funding documentation. Where a source draft was ambiguous or unreconciled, the file says so explicitly rather than presenting a guess as final — treat those notes as a required human check before submission, not a formatting quirk.
