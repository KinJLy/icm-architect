---
custom-width: 85
---
# AT Report record library — schema

**Unit:** one participant's assistive-technology NDIS funding case. **Form:** record library whose records each run a pipeline (see `_templates/case-template/`).

## Record lifecycle (status values used in `_index/log.md`)

`intake → trial-requested → trialling → washout → report-drafting → submitted → approved | rejected | withdrawn`

A case can skip `trial-requested`/`trialling`/`washout` if there's no device trial (e.g. straight custom orthotic provision) — go `intake → report-drafting`.

## Record shape

```
records/<case-id>/
├─ CONTEXT.md                     participant, condition, device/AT, current stage, what's still needed
├─ 01_intake-assessment/output/   MMT, ROM, tone, gait, functional impact — captured in NDIS-ready language
├─ 02_trial-request/output/       support letter requesting trial funding (human gate: clinician sign-off)
├─ 03_community-trial/output/     logbook + outcome measures collected during the trial
├─ 04_washout/output/             withdrawal-period logbook + deterioration findings
├─ 05_report-draft/output/        the assembled High Cost AT report body (human gate: clinical review)
└─ 06_submission/output/          appendix manifest + compliance check (human gate: final sign-off before lodging)
```

Each stage folder that's in use gets its own `CONTEXT.md` (copied from `_templates/case-template/`) stating what it reads from `references/`, what it produces, and the human check before the next stage reads it.

## Factory vs product

- `references/` and `_templates/` = factory. Edited rarely; a change here should improve every future case, not just one.
- `records/*/` = product. New every case; nothing here should be needed by another case except by explicit link.

## Human gates

Support-letter sign-off (stage 02), report clinical review (stage 05), and the pre-submission compliance check (stage 06, checklist in `references/submission-compliance-checklist.md`) are non-negotiable — none of these documents leave the workspace without a human reading the last output first.
