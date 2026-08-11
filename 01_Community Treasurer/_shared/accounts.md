---
name: accounts
status: all 4 accounts posted to 03_Ledger/ as of 2026-08-11. Categories still blank on 5443/1836 — see finding below.
---

# Accounts

The organisation's bank accounts. Every stage that names a specific ledger file should instead say "the active accounts in this registry" — add or retire an account here, not by editing every stage's `CONTEXT.md`.

| Account | Number | Status | Ledger file | Notes |
|---|---|---|---|---|
| General Account | 0259 | Active | `03_Ledger/ledger-0259.md` | |
| Single Sign Account | 1844 | Active | `03_Ledger/ledger-1844.md` | |
| Uniform holding/sweep account | 5443 | Dormant | `03_Ledger/ledger-5443.md` | Posted 2026-08-11, confirmed against the bank same night. Last activity 09/12/2024, closing balance **$7,896.49**. Received transfer-linked deposits from 1836 through 2024, then swept almost everything out to another bank account ("LIDPR") on 09/12/2024. Quiet since. Categories not yet coded. |
| Uniform (Square/POS) account | 1836 | **Active** | `03_Ledger/ledger-1836.md` | Posted 2026-08-11, confirmed against the bank same night, closing balance **$36,795.74** as of 05/05/2026 (may have moved since — recheck before reporting). Continuous activity: recurring Square terminal deposits, payments to "LW Reid Pty Ltd" (uniform supplier), transactions labelled "Uniform sales" and "Uniform shop", plus a $38,280 credit and transfers for a music program and bulk library order. **This is the account still running uniform sales, not a dormant leftover** — outsourcing changed who runs the shop day-to-day, not whether this account is in use. It did not appear in the source "General Ledger" spreadsheet that `ledger-0259.md`/`ledger-1844.md` were migrated from. Categories not yet coded. |

## Status meanings
- **Active** — reconciled and reported on every run; has a ledger file in `03_Ledger/`.
- **Dormant** — account is open but has no ongoing transaction activity. Excluded from `04_Report` cash summaries and solvency checks until reactivated. Gets a ledger file once historical data is imported, even with no current activity, so the balance is on record.

## Open finding: account 1836
An account with over a year of substantial, ongoing transaction activity was not part of the organisation's recorded ledger before this CSV was dropped into `01_Import/inbox/`.

**Likely explanation (2026-08-11, per current treasurer):** the current treasurer is new this year; the president appears to have run this account together with the previous treasurer last year, and it wasn't included in the handover. Reads as a handover gap, not a control irregularity.
- Account count confirmed closed: the bank-side handover from the previous treasurer surfaced only these four accounts, so no further accounts are expected.
- **Disclosure status (2026-08-11):** the treasurer has reported this account's total balance to the committee across two meetings, alongside account 5443's, as one of the two lower-movement accounts. At the time, the treasurer didn't yet know 1836 had substantial ongoing transaction activity (Square sales deposits, a $38,280 credit, program transfers) rather than being genuinely quiet like 5443. The treasurer's current view is that no further formal acknowledgment is needed. Worth the treasurer's own judgement call on whether the committee's understanding from those meetings still matches the fuller picture now known — noted here, not escalated further.
- This is still a catch-up import once the treasurer is comfortable: bring the account's history into the books, since it was missing from the source "General Ledger" spreadsheet.

## Known open question (not a pipeline task)
The current treasurer is considering proposing that the dormant uniform account (5443) balance be moved into a term deposit for interest — an idea drawn from practice at larger NFPs, not yet raised with or discussed by the committee. This is a future committee/banking decision, not something this pipeline does — noted here so it isn't lost, not because reporting should act on it.

## Human check
Resolve the account 1836 finding above before treating it as routine. Confirm account 5443's name/details before creating its ledger file.
