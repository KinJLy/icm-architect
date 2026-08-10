# 03_Ledger — the running transaction record

One job: hold the single, accumulating, reconciled record of every transaction. This is a record library, not a per-run stage — it never resets.

## Inputs
- Working (each run): the approved output of `../02_Reconcile/output/{account}-{period}-reconciliation.md`, once every flagged discrepancy has been resolved by a human.
- Reference (every run): `../_shared/chart-of-accounts.md`.

Do NOT load: `../01_Import/inbox/` directly — the ledger only receives entries that have passed through reconciliation, never raw bank data.

## Process
1. Once a period's reconciliation is approved, append its matched entries to `ledger.md`: date, description, category, amount, running balance, source (bank/receipt reference), reconciled period.
2. Never edit or delete a posted entry to "fix" a mistake — post a correcting entry instead, so the ledger stays an honest history (per treasurer principles: no forced edits after the fact).

## Outputs
- `ledger.md` — appended, never overwritten.

## Human check
Spot-check the new running balance against the actual current bank balance after posting. If they diverge, the reconciliation that fed this entry needs to be revisited, not the ledger patched directly.
