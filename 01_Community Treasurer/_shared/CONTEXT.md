# _shared — the factory

One job: hold the rules and reference data that stay the same every reconciliation and report run, so stage contracts can point here instead of restating them.

## Inputs
- Reference (one-time, human-supplied): `../Community Treasurer resources/` — the source guides these files were distilled from.

## Contents
- `treasurer-principles.md` — distilled reconciliation, controls, and reporting rules from the source guides. Read by `02_Reconcile` and `04_Report`.
- `chart-of-accounts.md` — the category list transactions get coded to. Read by `02_Reconcile` and `03_Ledger`. **Stub** — confirm/edit against your organisation's actual categories before first use.

## Human check
Both files are editable at any time. If a category or rule stops matching how the organisation actually operates, edit here — never restate a corrected version inside a stage contract.
