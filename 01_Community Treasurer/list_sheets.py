import openpyxl
wb = openpyxl.load_workbook('01_Import/inbox/Lidcombe P&C General Ledger - 2026.xlsx')
for sheet in wb.worksheets:
    print(sheet.title)
