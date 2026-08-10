# 04_Report — ledger to board report

One job: turn the ledger, as of a chosen date, into a board-ready financial report.

## Inputs
- Working (this run): `../03_Ledger/ledger.md`, as of the report date.
- Reference (every run): `../_shared/treasurer-principles.md` (what a report must cover and how to explain variance), `../_shared/chart-of-accounts.md`.

Do NOT load: `../01_Import/inbox/` or `../02_Reconcile/output/` directly — reporting works from the ledger, the single reconciled source of truth, not from raw or in-progress reconciliation data.

## Process
1. Summarise the ledger as of the report date into a Statement of Financial Position (balance sheet) and Statement of Financial Performance (income/expenditure vs. budget, period and year-to-date).
2. Add a cash summary sufficient to answer whether the organisation can pay what's coming due.
3. Write plain-language commentary on any variance past the board's agreed threshold — the story behind the number, not just the number.
4. Run the solvency check from `../_shared/treasurer-principles.md` and note the answer explicitly.

## Outputs
- `{period}-board-report.md` → `output/`

## Human check
Read the report end to end before it goes to the board — confirm the numbers tie back to the ledger and that every flagged variance has an explanation a non-financial board member could follow.
