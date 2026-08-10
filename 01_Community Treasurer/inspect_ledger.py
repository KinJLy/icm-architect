import openpyxl
import sys

def main():
    try:
        wb = openpyxl.load_workbook('01_Import/inbox/Lidcombe P&C General Ledger - 2026.xlsx')
        ws = wb.active
        for row in ws.iter_rows(values_only=True):
            print(row)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
