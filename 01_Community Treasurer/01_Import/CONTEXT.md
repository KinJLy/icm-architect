# 01_Import — bank export drop point

One job: receive a raw bank CSV/statement export for a period and stage it for reconciliation.

## Inputs
- Working (this run): the bank CSV/statement the human downloads from online banking.

Do NOT load: other periods' imports, `02_Reconcile/output/`, `03_Ledger/ledger.md` — this stage doesn't reconcile or interpret, only receives.

## Process
1. Human exports a CSV (or statement) from the bank for the period being processed.
2. Save it into `inbox/` as `{account}-{period}.csv` (e.g. `main-2026-08.csv`).
3. Confirm the account and date range in the file match what was intended.

## Outputs
- `{account}-{period}.csv` → `inbox/`

## Human check
Open the file and confirm it's the right account and the right date range before moving to `02_Reconcile`. A wrong-period import here means every discrepancy downstream is a false one.
