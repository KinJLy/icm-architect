# 01_intake-assessment — capture the clinical picture in NDIS-ready language

One job: turn the clinical assessment into a structured, NDIS-ready findings record.

## Inputs
- Working (this run): raw assessment notes (from wherever they were taken — paper, EMR export, dictation)
- Reference (every run): ../../../references/outcome-measures.md
- Reference (every run): ../../../references/ndis-phrasebook.md

## Process
1. Record strength (MMT), ROM, tone/spasticity, gait deviations, and functional impact under the headings in `outcome-measures.md`.
2. Write findings directly in NDIS language per `ndis-phrasebook.md` — not "foot drop present" but "foot drop resulting in reduced toe clearance, increasing falls risk and limiting safe community ambulation." This is the single biggest time-saver in the whole pipeline.
3. If any measurement conflicts across assessors (e.g. two different MMT scores), record both plus the explanation — see `../../../references/justification-banks/assessment-discrepancy-reasoning.md` — never silently pick one.

## Outputs
- assessment-findings.md → output/

## Human check
Clinician reviews the findings record for accuracy before it's used to justify any trial request or report section.
