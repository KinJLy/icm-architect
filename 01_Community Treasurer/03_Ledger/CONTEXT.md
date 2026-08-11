# 03_Ledger — the running transaction records

One job: hold the accumulating, reconciled records for each account. This is a record library, not a per-run stage — it never resets.

## Inputs
- Working (each run): the approved output of `../02_Reconcile/output/{account}-{period}-reconciliation.md`, once every flagged discrepancy has been resolved by a human.
- Reference (every run): `../_shared/accounts.md` (which ledger file this account maps to, or whether one needs creating), `../_shared/chart-of-accounts.md`, and the relevant historical ledger for the previous balance.

Do NOT load: `../01_Import/inbox/` directly — the ledger only receives entries that have passed through reconciliation, never raw bank data.

## Process
1. Once a period's reconciliation is approved, append its matched entries to that account's ledger file per `../_shared/accounts.md` (creating `ledger-{account}.md` if this is the account's first posting): date, description, category, amount, running balance, source (bank/receipt reference), reconciled period.
2. Never edit or delete a posted entry to "fix" a mistake — post a correcting entry instead, so the ledgers stay an honest history (per treasurer principles: no forced edits after the fact).
3. If this is a new ledger file, update `../_shared/accounts.md` with its filename and mark the account's status accordingly.

## Outputs
- One ledger file per account in `../_shared/accounts.md` (currently `ledger-0259.md` and `ledger-1844.md`) — appended, never overwritten.

## Human check
Spot-check the new running balance against the actual current bank balance after posting. If they diverge, the reconciliation that fed this entry needs to be revisited, not the ledger patched directly.
