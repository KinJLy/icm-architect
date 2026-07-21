# 05_report-draft — assemble the High Cost AT report

One job: write the full report body from everything collected so far.

## Inputs
- Working (this run): ../01_intake-assessment/output/, ../03_community-trial/output/, ../04_washout/output/ (whichever exist for this case)
- Reference (every run): ../../../references/report-block-structure.md
- Reference (every run): ../../../references/justification-banks/<condition>.md
- Reference (every run): ../../../references/evidence-summary-<condition>.md
- Reference (every run): ../../../references/ndis-phrasebook.md

## Process
1. Follow the block/section structure in `report-block-structure.md` — don't reinvent section order per case.
2. Pull condition-specific justification language from the matching `justification-banks/` file; customise, don't restate boilerplate.
3. Cite from `evidence-summary-*.md` with inline author/year — every quantitative claim needs a source (see `submission-compliance-checklist.md`).
4. Lead with demonstrated benefit (trial + washout data) over projected benefit wherever both are available — this is what NDIS delegates weight most heavily.

## Outputs
- report.md → output/ (one file, one source of truth — not a new "Branch ·" fork per revision; use git history for versions)

## Human check
Clinician reads the full draft end to end before it moves to submission. This is the heaviest editing gate in the pipeline — expect it.
