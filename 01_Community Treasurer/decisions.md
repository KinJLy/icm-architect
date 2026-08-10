# Decisions and Learnings

This file tracks key architectural decisions, mistakes, and technical learnings during the setup and migration of the Community Treasurer project.

## Decisions

### Account Separation
- **Decision**: Split the bank ledger into two separate files: `03_Ledger/ledger-0259.md` and `03_Ledger/ledger-1844.md`.
- **Reasoning**: The source Excel file contained transactions for two distinct accounts (General Account ending in 0259 and Single Sign Account ending in 1844). Combining them into a single ledger would result in incorrect running balances and make it impossible to reconcile either account accurately.
- **Impact**: All future reconciliations and reports must now reference the specific ledger corresponding to the account being processed.

### Migration Strategy
- **Decision**: Use a script-based migration for historical data from Excel to Markdown.
- **Reasoning**: Manual entry of years of historical data is error-prone. A script ensures that dates, descriptions, categories, and balances are preserved exactly as they appear in the source.

## Mistakes & Corrections

### Mixed Ledger (Corrected)
- **Mistake**: Initially migrated all transactions from the Excel file into a single `03_Ledger/ledger.md`.
- **Correction**: Identified that this mixed the running balances of two different accounts. Corrected by creating separate ledger files and re-running the migration script with account-specific column mapping.

### Column Mapping Collision (Corrected)
- **Mistake**: The migration script picked the *last* occurrence of headers like "Date" and "Balance" in sheets that contained both accounts side-by-side (2025 and 2026). This caused data from Account 1844 to be incorrectly assigned to the Account 0259 ledger.
- **Correction**: Updated `migrate_ledger.py` to dynamically select the first occurrence of headers for Account 0259 and the second occurrence for Account 1844.

## Technical Learnings

### Excel Processing (`openpyxl`)
- **Formulas**: Must use `data_only=True` when loading workbooks to extract the calculated values instead of the underlying Excel formulas (e.g., `=F5+E6`).
- **Iterators**: `ws.iter_rows(values_only=True)` returns a generator. Accessing indices (e.g., `[0]`) requires either converting the result to a list or using `next()` to retrieve the first row.

### Data Mapping & Robustness
- **Robustness**: When migrating data from multi-account sheets, it is safer to dynamically find column indices by searching for keywords (e.g., "Date", "Balance") rather than relying on hardcoded column numbers, as sheet structures can vary.

### Date & Ledger Integrity
- **Date Consistency**: Ensure dates are consistently formatted as `DD/MM/YYYY`. Found a case where months were leading (e.g., `07/01/2026` for July 1st) and corrected it to `01/07/2026`.
- **Ledger Status**: Differentiate between "Historical" and "Current" records. Data from 2026 and onwards should be marked as "Current" until the current year changes.

### Project Pipeline
- **Naming Conventions**: Reinforce the use of `{account}-{period}.xlsx` in the `01_Import/inbox/` folder to maintain consistency in the pipeline.
- **Human-in-the-loop**: Reconfirmed the "one rule": no data moves to the next stage until a human has verified the output of the previous stage.
