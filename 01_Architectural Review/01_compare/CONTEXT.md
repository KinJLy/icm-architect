# 01_compare — table RKJ baseline vs Masterton's latest revision

One job: produce a side-by-side comparison of this round's Masterton plans against the RKJ baseline, with likely reasons and cost deltas.

## Inputs
- Working (this round): `input/` — this round's Masterton plan documents
- Reference (every round): `../_reference/83 Brixton Rd/fwd83brixtonapprovedccdocuments/83 Brixton Road Berala - APPROVED Architectural Plans.pdf` — the RKJ baseline
- Reference (every round): `../_reference/pajic-costing.md`
- Reference (every round): `../_reference/voice.md`

Do NOT load: the rest of `../_reference/83 Brixton Rd/` (Sydney Water docs, DA docs, engineering/stormwater/landscape plans) — the CC-approved Architectural Plans is the baseline; only pull another file from that folder if the human asks for something the architectural plans don't cover. Do NOT load previous rounds' output — compare only against the RKJ baseline and the newest Masterton set, unless explicitly asked for a round-over-round diff.

## Process
1. Read the RKJ baseline (CC-approved Architectural Plans) and the newest Masterton plans in `input/`.
2. For every difference: identify the item, where to find it in the plans, what RKJ shows, what Masterton shows, what changed, and a likely reason.
3. Estimate the cost difference each change makes, anchored to `pajic-costing.md`.
4. Follow `voice.md` for tone, table format, and the no-fluff constraint. If nothing changed, say so plainly.

## Outputs
- `round-NN-comparison.md` → `output/` (NN = next round number)

## Human check
Read the table against the actual plan sets. Confirm the cost deltas look sane before moving to `02_change-requests`. Edit the file in place — the next stage reads whatever is here.
