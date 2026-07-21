# Case index

One line per case. Status values: `intake → trial-requested → trialling → washout → report-drafting → submitted → approved | rejected | withdrawn`.

| id | participant | condition | device/AT                                           | status | notes |
|---|---|---|---|---|---|
| `m-bioness-l300go` | Megan Hollway (referred to as "M" in most workspace files) | Multiple Sclerosis, right foot drop | Bioness L300 Go (FES), Lower Leg + Thigh components | report-drafting | Report body reconciled (`records/m-bioness-l300go/05_report-draft/output/report.md`, from the real v3(11) draft). All 8 community-trial weeks + all 3 washout weeks now on file; neurologist letter and DOB confirmed. Still missing: supplier quote, PSFS/carer-feedback verification, usage-analytics attachment. Two new evidence sources (Mavenclad history, fear-of-falling questionnaire) found but not yet folded into the report — clinician call. See `records/m-bioness-l300go/CONTEXT.md`. |
| `p-custom-afo-cp` | P | Cerebral Palsy, foot deformity with bony prominences | Custom-made AFO (Korthotics)                        | report-drafting | Current AFO fitted 04/2024 (replaced cracked pair from 11/2021); wearing AFOs since ~age 5. No trial/washout stages — off-the-shelf ruled out on anatomical grounds, not by trial. Clinical justification Q&A captured; full report body not yet drafted. |

This table is hand-maintained today. If the number of cases grows past a handful, script it from each record's `CONTEXT.md` frontmatter instead.
