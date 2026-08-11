---
name: status
last-updated: 2026-08-11
---

# Status — where the pipeline is up to

Read this first in a new session before scanning folders — it captures open items that aren't obvious from file presence alone. See `decisions.md` for the reasoning behind how things got here.

## Current state
- **Accounts**: all 4 confirmed and registered in `_shared/accounts.md` — `0259`, `1844` (Active, long-running), `1836` (Active, uniform sales — discovered 2026-08-11), `5443` (Dormant since 09/12/2024 — discovered 2026-08-11).
- **Ledgers**: all 4 accounts have ledger files in `03_Ledger/`. `ledger-0259.md`/`ledger-1844.md` are the original migration; `ledger-1836.md`/`ledger-5443.md` were posted 2026-08-11 as a historical catch-up import, balances confirmed against the bank same night.
- **Reporting**: `04_Report/CONTEXT.md` scoped to cash-basis (no balance sheet) — see decision in `decisions.md`. No board report has been generated yet (`04_Report/output/` is empty).
- **Chart of accounts**: `_shared/chart-of-accounts.md` populated with real categories matching this org's actual cash cycle (event stalls, school program subsidies, insurance, low-value equipment). No longer a stub.

## Open items (next session should pick these up)
1. **Categories uncoded on `ledger-1836.md` and `ledger-5443.md`** — every row has a blank Category. Worth prioritising 1836's larger/unusual amounts first (the $38,280 credit, the $20,000 "music program" transfer, recurring LW Reid Pty Ltd payments) since it's the active account most likely to feature in a report soon.
2. **1836's balance needs rechecking before any report** — confirmed at $36,795.74 as of 05/05/2026 when imported, but it's an active account and may have moved since.
3. **Committee disclosure on account 1836** — the treasurer has reported its total balance in two prior meetings, but at the time didn't know it had substantial ongoing activity rather than being quiet like 5443. Treasurer's current call is that no further formal acknowledgment is needed (see `_shared/accounts.md` for full context) — not a task, just something the treasurer may revisit.
4. **Term deposit proposal for account 5443** — treasurer's own idea, not yet raised with the committee. Not a pipeline task; noted in `_shared/accounts.md` so it isn't lost.
5. **No board report generated yet** — `04_Report/output/` is empty. First run will exercise the new cash-basis scope for the first time.

## Not yet built
Budget pipeline (propose → approve → track vs. actuals) — deferred until reporting/ledger are stable, per root `CONTEXT.md`.
