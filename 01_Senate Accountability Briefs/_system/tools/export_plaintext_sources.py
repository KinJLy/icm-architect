"""
Export the binary source data (xlsx workbook, PDF contact list) to plain
CSV, so this ICM works for someone using a plain chat window with no code
execution - they can paste a CSV into any LLM chat, but can't open an .xlsx
or parse a .pdf without running code.

Re-run this whenever the source workbook or contact list PDF is updated -
these CSVs are generated, not hand-edited (same rule as _index/log.md).

Usage:
    python export_plaintext_sources.py
"""
import csv
import sys
from pathlib import Path

import openpyxl

sys.path.insert(0, str(Path(__file__).parent))
from extract_senator_data import load_contacts, WORKBOOK

REF = Path(__file__).parent.parent.parent / "01_reference"
SOURCE_DATA = REF / "source-data"


def export_workbook():
    wb = openpyxl.load_workbook(WORKBOOK, data_only=True)
    ws = wb.active
    out_path = SOURCE_DATA / "senate-ndis-table.csv"
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for row in ws.iter_rows(values_only=True):
            writer.writerow(row)
    print(f"Wrote {out_path}")


def export_contacts():
    contacts = load_contacts()
    out_path = SOURCE_DATA / "senate-contact-list.csv"
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["normalized_key", "state", "party", "email", "title"])
        for key, v in sorted(contacts.items()):
            writer.writerow([key, v["state"], v["party"], v["email"], v["title"]])
    print(f"Wrote {out_path} ({len(contacts)} rows)")


if __name__ == "__main__":
    export_workbook()
    export_contacts()
