---
custom-width: 100
---
# Architectural Review

Round-by-round comparison of Masterton's revised house plans against the RKJ baseline, ending in change requests sent back to Masterton.

Built on ICM: folders carry sequencing, hierarchy carries context, files carry state. The structure is the documentation — if something needs explaining, the explanation goes in that folder's CONTEXT.md.

## Where things live

| Folder | What it holds |
|---|---|
| `01_compare/` | compares this round's Masterton plans against the RKJ baseline + Pajic costing |
| `02_change-requests/` | turns the comparison into a written list of changes to send Masterton |
| `_reference/` | factory: RKJ baseline plans, Pajic costing, voice/format rules — stable across rounds |

## Route by what just happened

| If | Go to | Then stop at |
|---|---|---|
| a new Masterton plan revision arrived | drop it in `01_compare/input/`, then `01_compare/CONTEXT.md` | human reads the comparison table |
| a comparison table was just produced | `02_change-requests/CONTEXT.md` | human reads the change requests before sending |
| asked for status / how many rounds so far | scan `01_compare/output/` and `02_change-requests/output/` | report what exists |
| Pajic sends updated costing | update `_reference/pajic-costing.md` directly | — |

## The one rule

Nothing goes to Masterton until a person has read the change requests.
