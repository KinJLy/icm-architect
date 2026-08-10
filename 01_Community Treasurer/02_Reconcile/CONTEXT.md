# 02_Reconcile — match imports and receipts, flag discrepancies

One job: match the imported bank lines against receipts/invoices and the existing ledger, and produce a reconciliation report that flags anything that doesn't match.

## Inputs
- Working (this run): `../01_Import/inbox/{account}-{period}.csv`, any receipts/invoices in `receipts/` for the period.
- Reference (every run): `../03_Ledger/ledger.md` (existing balance and entries to reconcile against), `../_shared/treasurer-principles.md` (reconciliation rules), `../_shared/chart-of-accounts.md` (category coding).

Do NOT load: prior periods' `output/` files, `04_Report/output/` — reporting reads the ledger, not this stage's history.

## Process
1. Read the imported CSV line by line; for each transaction, find its matching receipt/invoice (if one exists) and category from the chart of accounts.
2. Compare against `ledger.md`'s existing entries for the same period to catch anything already recorded, duplicated, or missing.
3. Anything that doesn't cleanly match — no receipt, wrong amount, timing difference, unexplained fee — gets flagged, not resolved automatically. See `../_shared/treasurer-principles.md` for common causes to check first.
4. Confirm book balance vs. bank balance reconciles once all flags are resolved.

## Outputs
- `{account}-{period}-reconciliation.md` → `output/` — matched entries ready to post, plus a list of flagged discrepancies with a recommended resolution for each.

## Human check
Resolve every flagged discrepancy — approve, correct, or explain it — before anything from this period is posted to `03_Ledger/ledger.md`. Do not post a reconciliation with unresolved flags.
