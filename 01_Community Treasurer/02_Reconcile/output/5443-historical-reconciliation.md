# Reconciliation - Account 5443 (historical catch-up)

Source: `01_Import/inbox/5443-historical.csv`. Full historical export from the bank, not a single period statement -- being imported as a one-off catch-up since this account was missing from the source "General Ledger" spreadsheet that ledger-0259.md / ledger-1844.md were migrated from.

This account has been quiet since 09/12/2024 (its last transaction) -- see ` _shared/accounts.md` for the linked-transfer history with account 1836.

## Matched entries (ready to post)

| Date | Description | Category | Amount | Running Balance | Source | Reconciled Period |
|---|---|---|---|---|---|---|
| 09/09/2024 | DEPOSIT CASH $1200.00 CHEQUE $0.00 Branch EASTWOOD |  | 1200.00 | 9877.46 | Bank CSV export (historical) | Historical |
| 12/09/2024 | Transfer from NetBank Sqr PMT transfer |  | 3600.00 | 13477.46 | Bank CSV export (historical) | Historical |
| 22/10/2024 | Transfer from NetBank Sqr payment transf |  | 3000.00 | 16477.46 | Bank CSV export (historical) | Historical |
| 22/11/2024 | DEPOSIT CASH $550.00 CHEQUE $0.00 Branch LIDCOMBE |  | 550.00 | 17027.46 | Bank CSV export (historical) | Historical |
| 09/12/2024 | Transfer to other Bank NetBank LIDPR |  | -1537.36 | 15490.10 | Bank CSV export (historical) | Historical |
| 09/12/2024 | Transfer to other Bank NetBank LIDPR |  | -7593.61 | 7896.49 | Bank CSV export (historical) | Historical |

## Flagged discrepancies

- No receipts/invoices available for these historical transactions (import is 8-20 months after the fact) -- categories are left blank for the treasurer to code against `_shared/chart-of-accounts.md`, not auto-assigned.
- Running balances above are the bank's own post-transaction balances from the CSV export, not recalculated -- verified internally consistent (each row's balance = next row's balance +/- that row's amount) across the full export.

## Human check
Confirm the most recent running balance above against the current actual bank balance for this account before posting to ` 03_Ledger/ledger-5443.md`. Assign categories where practical before or after posting.
