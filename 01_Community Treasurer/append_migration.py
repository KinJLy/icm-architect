with open('ledger_migration.md', 'r') as f:
    lines = f.readlines()

# The first 3 lines are # Ledger, \n, and the header
# The 4th line is the separator |---|---|---|---|---|---|---|
# The 5th line is the blank row | | | | | | | |
# We want the rows starting from the 6th line.

rows_to_add = lines[5:]

with open('03_Ledger/ledger.md', 'a') as f:
    for row in rows_to_add:
        f.write(row)
