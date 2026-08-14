"""
Stage 3 (personalize + finalize): take a VALIDATED senator record, add the
sender's identity (01_reference/sender-profile.md) and an optional per-senator
personal story (records/{slug}/personal-note.md), and produce the final
send-ready docx in 03_ready-to-send/.

Refuses to finalize a record that isn't validated (`validated: true` in its
frontmatter) - that's the actual "ready to send" gate. Validate the data
first (stage 1/2), personalize and finalize last (this stage).

Usage (choose exactly one selection mode; names are record slugs):
    python finalize_send_pack.py katherine-gallagher pauline-hanson ...
    python finalize_send_pack.py --party ALP
    python finalize_send_pack.py --state QLD
    python finalize_send_pack.py --all
"""
import re
import sys
from pathlib import Path

import docx
import yaml

sys.path.insert(0, str(Path(__file__).parent))
from render_brief_docx import (
    TEMPLATE, RECORDS_DIR, BASE, REF,
    parse_record, build_replacements, apply_replacements,
    strip_prepared_for_clause, strip_lens_optional_note,
    remove_portfolio_row, remove_portfolio_lens_section,
    set_checklist_checked, load_immediate_ask, scan_existing_records,
)
from _selection import parse_selection_args

SENDER_PROFILE = REF / "sender-profile.md"
OUT_DIR = BASE / "03_ready-to-send"

PERSONAL_STORY_MARKER = (
    "[PERSONAL STORY - optional, delete this whole box if none. A short "
    "first-person note on why this bill matters to you personally makes "
    "the numbers land as human impact, not just data.]"
)


def load_sender_profile():
    text = SENDER_PROFILE.read_text(encoding="utf-8")
    fm = yaml.safe_load(text.split("---", 2)[1])
    missing = [k for k in ("name", "role", "email") if not fm.get(k)]
    if missing:
        raise SystemExit(
            f"01_reference/sender-profile.md is missing: {', '.join(missing)}. "
            "Fill in your name/role/email there before finalizing any brief."
        )
    return fm


def load_personal_note(slug: str):
    """The template (_templates/personal-note.md) puts instructions above a
    '---' divider and the actual story below it - only that part counts."""
    path = RECORDS_DIR / slug / "personal-note.md"
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8")
    story = text.rsplit("---", 1)[-1].strip() if "---" in text else text.strip()
    return story or None


def finalize(slug: str, immediate_ask: str, sender: dict):
    record_path = RECORDS_DIR / slug / "record.md"
    if not record_path.exists():
        print(f"SKIP (no record): {slug}")
        return
    fm, bullets, mechanism = parse_record(record_path)
    if not fm.get("validated"):
        print(f"SKIP (not validated - finish the checklist in records/{slug}/record.md first): {slug}")
        return

    replacements, relevant = build_replacements(fm, bullets, mechanism, immediate_ask)
    replacements["[YOUR NAME]"] = sender["name"]
    replacements["[YOUR ROLE/TITLE]"] = sender["role"]
    replacements["[YOUR EMAIL]"] = sender["email"]
    replacements["[PREPARED BY - name, role/organisation]"] = f"{sender['name']}, {sender['role']}"

    story = load_personal_note(slug)
    if story:
        replacements[PERSONAL_STORY_MARKER] = story

    doc = docx.Document(str(TEMPLATE))
    strip_prepared_for_clause(doc, relevant, fm.get("portfolio"))
    if not relevant:
        remove_portfolio_row(doc)
        remove_portfolio_lens_section(doc)
    else:
        strip_lens_optional_note(doc)
    if not story:
        remove_personal_note_box(doc)
    apply_replacements(doc, replacements)
    set_checklist_checked(doc, True)  # finalize only runs on validated records

    OUT_DIR.mkdir(exist_ok=True)
    out_path = OUT_DIR / f"{fm['senator_name']} Senate Impact Pack.docx"
    doc.save(str(out_path))

    email_text = build_cover_email(fm, bullets, story, sender, immediate_ask)
    email_path = OUT_DIR / f"{fm['senator_name']} Cover Email.txt"
    email_path.write_text(email_text, encoding="utf-8")

    print(f"Wrote {out_path}  [{'with personal note' if story else 'no personal note'}]")
    print(f"Wrote {email_path}")


def remove_personal_note_box(doc):
    for t in doc.tables:
        cell = t.rows[0].cells[0]
        if cell.text.startswith("A personal note from"):
            t._tbl.getparent().remove(t._tbl)
            return


def build_cover_email(fm, bullets, story, sender, immediate_ask):
    """Plain, unformatted text (no markdown) - meant to be copied straight
    into an email client's compose box, so no characters that would show up
    literally (*, #, etc.)."""
    greeting = f"Dear Senator {fm['senator_name']},"

    context = (
        f"I'm writing ahead of the Senate vote on the National Disability Insurance Scheme "
        f"Amendment (Securing the NDIS for Future Generations) Bill 2026, with a short brief on "
        f"what it could mean in {fm['state']} specifically: {bullets['Active NDIS Participants']} "
        f"active NDIS participants, an estimated {bullets['Total Footprint Estimate']} people "
        f"directly or indirectly affected, and up to ${bullets['Annual NDIS Funding Exposure ($ billion)']} "
        f"billion in funding exposure."
    )

    ask_para = (
        f"This isn't a request for a meeting, and it isn't an argument against reforming the NDIS. "
        f"Before you vote, I'd ask that you: {immediate_ask.lower()}"
    )

    closing = (
        "The attached brief sets out the full picture, including the questions constituents are "
        "likely to be asking after the vote if implementation causes harm in ways that weren't intended."
    )

    sign_off = f"Kind regards,\n{sender['name']}\n{sender['role']}\n{sender['email']}"

    parts = [greeting, "", context]
    if story:
        parts += ["", story]
    parts += ["", ask_para, "", closing, "", sign_off]
    return "\n".join(parts)


if __name__ == "__main__":
    immediate_ask = load_immediate_ask()
    sender = load_sender_profile()
    available = scan_existing_records()
    selection, _ = parse_selection_args(sys.argv[1:], default_names=[])
    slugs = selection.resolve(available, default_keys=list(available.keys()))
    print(f"Selected {len(slugs)} record(s)")

    for slug in slugs:
        finalize(slug, immediate_ask, sender)
