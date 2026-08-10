---
custom-width: 99
---
# Community Treasurer — the pipeline

The flow in one line: import the bank statement, reconcile it against receipts, post it to the ledger, report it to the board.

| Stage | Job | Input | Output | Human check |
|---|---|---|---|---|
| `01_Import` | drop the raw bank export for a period | bank CSV/XLSX export | `inbox/{period}.csv` (or `.xlsx`) | confirm the right period, right account |
| `02_Reconcile` | match imports + receipts against the ledger, flag diffs | 01's output, `receipts/`, `03_Ledger/ledger.md` | `output/{period}-reconciliation.md` | resolve every flagged discrepancy before it's posted |
| `03_Ledger` | post reconciled entries; the running record | 02's approved output | `ledger.md` (appended) | spot-check balances match the bank statement |
| `04_Report` | turn the ledger as-of-date into a board report | `03_Ledger/ledger.md`, `_shared/*` | `output/{period}-board-report.md` | read it before it goes to the board |

Factory (stable, every run): `_shared/treasurer-principles.md`, `_shared/chart-of-accounts.md`.
Product (new each run): `01_Import/inbox/`, `02_Reconcile/output/`, `04_Report/output/`; `03_Ledger/ledger.md` accumulates rather than resetting.

Status is whatever exists: a stage is COMPLETE for a period when its output folder holds a file for that period other than `.gitkeep`.

## Not yet built: the budget pipeline

The role also needs a budget cycle (propose → board approval → track budget vs. actuals through the year). It isn't scaffolded yet — reporting and the ledger need to be running reliably first, per the "don't build stages that don't exist yet" rule. When it's added, it will sit alongside `04_Report` (both read the ledger) as `05_Budget/`, sharing the same `_shared/` factory.

## Source material

`Community Treasurer resources/` holds the raw guides `_shared/treasurer-principles.md` was distilled from — the ICDA/Beyond Bank "Damn Good Advice for Treasurers" guide and webinar transcript. Left in place, untouched; link back to it rather than copying passages forward.
