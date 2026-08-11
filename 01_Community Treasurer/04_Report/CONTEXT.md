# 04_Report — ledger to board report

One job: turn the ledger, as of a chosen date, into a board-ready financial report.

## Inputs
- Working (this run): each **active** account's ledger in `../03_Ledger/` per `../_shared/accounts.md`, as of the report date. Dormant accounts (per the registry) are excluded from cash summaries and solvency checks — note their existence and balance separately if material.
- Reference (every run): `../_shared/treasurer-principles.md` (what a report must cover and how to explain variance), `../_shared/chart-of-accounts.md`.

Do NOT load: `../01_Import/inbox/` or `../02_Reconcile/output/` directly — reporting works from the ledger, the single reconciled source of truth, not from raw or in-progress reconciliation data.

## Scope: cash-basis, not full balance sheet
`../_shared/treasurer-principles.md` calls for a full Statement of Financial Position (assets/liabilities/equity). This organisation doesn't hold funds on behalf of others, doesn't carry inventory or prepayments, and expenses equipment when bought — so there's no material balance-sheet structure to report. Reporting instead runs cash-basis: cash at bank, income/expenditure, and a manual check for anything currently owed. Revisit this scope if that changes (e.g. the organisation starts holding grant money in advance, or collecting funds on behalf of a class/program that aren't yet spent).

## Process
1. Summarise the active-account ledgers as of the report date into a Statement of Financial Performance (income/expenditure vs. budget, period and year-to-date), by category from `../_shared/chart-of-accounts.md`.
2. State current cash at bank for each active account, and the combined net cash position. List dormant accounts and their last-known balance separately, not folded into the active total.
3. Ask whether any bills are currently unpaid or cheques uncashed as of the report date — if so, list them and subtract from cash to give a true "free cash" figure. This is the closest thing to a liabilities check this organisation needs.
4. Write plain-language commentary on any variance past the board's agreed threshold — the story behind the number, not just the number.
5. Run the solvency check from `../_shared/treasurer-principles.md` (adapted: current assets = cash at bank; current liabilities = unpaid bills/uncashed cheques per step 3) and note the answer explicitly.

## Outputs
- `{period}-board-report.md` → `output/`

## Human check
Read the report end to end before it goes to the board — confirm the numbers tie back to the ledger and that every flagged variance has an explanation a non-financial board member could follow.
