---
custom-width: 100
---
# Architectural Review — the pipeline

The flow in one line: new Masterton revision in, compared against the RKJ baseline and Pajic's costing, change requests out.

| Stage | Job | Input | Output | Human check |
|---|---|---|---|---|
| `01_compare` | table the differences RKJ → Masterton, with cost deltas | RKJ baseline + Pajic costing (ref), this round's Masterton plans (working) | `output/round-NN-comparison.md` | table matches the plans; costs read sane |
| `02_change-requests` | turn the table into a written ask for Masterton | 01's output | `output/round-NN-change-requests.md` | matches what you actually want changed, before it's sent |

Factory (stable, every round): `_reference/83 Brixton Rd/` (RKJ baseline = the CC-approved Architectural Plans within it), `_reference/pajic-costing.md`, `_reference/voice.md`
Product (new each round): each stage's `output/`, numbered by round

Status is whatever exists: round count = number of files in `01_compare/output/`. A round is COMPLETE when both stages have a file for that round number.
