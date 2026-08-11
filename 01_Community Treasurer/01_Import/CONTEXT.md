# 01_Import — bank export drop point

One job: receive a raw bank export (CSV or XLSX) for a period and stage it for reconciliation.

## Inputs
- Working (this run): the bank CSV or XLSX export the human downloads from online banking.

Do NOT load: other periods' imports, `02_Reconcile/output/`, `03_Ledger/` — this stage doesn't reconcile or interpret, only receives.

## Process
1. Human exports a CSV or XLSX from the bank for the period being processed.
2. Save it into `inbox/` as `{account}-{period}.csv` or `{account}-{period}.xlsx`, where `{account}` matches an entry in `../_shared/accounts.md` (e.g. `0259-2026-08.xlsx`).
3. Confirm the account and date range in the file match what was intended.
4. If this is the first import for an account not yet in `../_shared/accounts.md` (e.g. one of the dormant uniform accounts), add it to the registry first.

## Outputs
- `{account}-{period}.csv` or `{account}-{period}.xlsx` → `inbox/`

## Human check
Open the file and confirm it's the right account and the right date range before moving to `02_Reconcile`. A wrong-period import here means every discrepancy downstream is a false one.
