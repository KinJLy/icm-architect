---
custom-width: 100
---
# Community Treasurer

Reconciles bank/receipt transactions into a ledger, and turns the ledger into board-ready financial reports.

Built on ICM: folders carry sequencing, hierarchy carries context, files carry state. The structure is the documentation — if something needs explaining, the explanation goes in that folder's CONTEXT.md, not in your head.

## Where things live

| Folder | What it holds |
|---|---|
| `01_Import/` → `02_Reconcile/` → `03_Ledger/` → `04_Report/` | the pipeline, in execution order |
| `_shared/` | factory: treasurer principles, chart of accounts — stable across runs |
| `Community Treasurer resources/` | raw source material (guides, webinar transcript) the factory was distilled from |

## Route by what just happened

| If | Go to | Then stop at |
|---|---|---|
| a new bank statement (CSV or XLSX) has arrived | `01_Import/CONTEXT.md` | human confirms the file landed in `inbox/` |
| import is sitting in `01_Import/inbox/` | `02_Reconcile/CONTEXT.md` | human resolves flagged discrepancies before posting |
| reconciled entries are ready to post | `03_Ledger/CONTEXT.md` | human confirms `ledger.md` looks right |
| a board report is due | `04_Report/CONTEXT.md` | human reads the report before it goes to the board |
| asked for status | scan `01_Import/inbox/`, `02_Reconcile/output/`, `04_Report/output/` | report what exists and what's still pending |
| chart of accounts or treasurer rules need updating | `_shared/CONTEXT.md` | human confirms the change |

## Not yet built

A budget pipeline (propose → approve → track vs. actuals) is a known next step once reporting and the ledger are stable — see `CONTEXT.md` for why it's deferred.

## The one rule

Nothing moves to the next stage until a person has read the output of the last one.
