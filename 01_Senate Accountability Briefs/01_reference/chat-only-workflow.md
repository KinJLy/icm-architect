# Chat-only workflow (no code execution)

This ICM has two paths. Pick whichever matches what you actually have access to.

## Path A — Scripted (Claude Code, or any agent with code execution)

Needs: Python 3 + `openpyxl`, `pypdf`, `python-docx`, `PyYAML` installed, and file-system access to this folder.

```
python _system/tools/extract_senator_data.py "Senator Name"   # or --party/--state/--all
python _system/tools/render_brief_docx.py {slug}
python _system/tools/finalize_send_pack.py {slug}
```

This is the fast path — it does the data lookup, the maths, and the Word-doc formatting for you. Everything below is for when you don't have this.

## Path B — Chat-only (any plain LLM chat window, no code execution)

If you're working in a plain chat window (ChatGPT, Claude.ai chat, Gemini, etc. with no file-upload-and-run capability, or no code execution enabled), you can still produce a brief by hand. The binary source files (`.xlsx`, `.pdf`, `.docx`) are the actual blocker here — a chat window can't open them without running code. Everything else in this ICM is plain markdown, which any chat window can read if you paste it in.

**What to paste into the chat, in order:**

1. `01_reference/brief-template.md` — the structure and field legend
2. The **one relevant row** for your senator from `01_reference/source-data/senate-ndis-table.csv` and `01_reference/source-data/senate-contact-list.csv` (plain CSV, generated from the binary sources — don't paste the whole 76-row file if you can avoid it, just the row(s) you need, to keep the chat focused)
3. `01_reference/vote-position-rules.md`
4. `01_reference/portfolio-relevance.md` (and `01_reference/senator-portfolios.md` if you want the portfolio snapshot rather than looking it up live)

**What to ask the LLM to do:**

> Using the attached brief template, this senator's workbook row and contact row, the vote-position rule, and the portfolio-relevance rule: fill in every `[BRACKET]` field in the template. Compute the derived fields (shares, footprint estimates, funding reductions) using the formulas in the field legend. Apply the portfolio-relevance check explicitly - don't skip it. State which vote-position case applies and why. Output the fully filled brief as plain text/markdown.

Any capable LLM can do the arithmetic and the substitution from those four inputs - it doesn't require Claude specifically, and it doesn't require Python. What it can't do without the CSVs is know the senator's numbers or contact details, since those live in files a chat window can't open on its own.

**Formatting the result:** the LLM's output will be plain markdown, not a formatted Word doc (that part of the pipeline genuinely needs `python-docx`). Paste the filled markdown into Word yourself and format it to match `01_reference/examples/Gallagher ACT Accountability Brief.docx`, or send it as plain text/a PDF export from your word processor - a polished Word doc is nice to have, not the thing that makes the brief effective.

**Keep the CSVs current:** `01_reference/source-data/senate-ndis-table.csv` and `senate-contact-list.csv` are generated from the `.xlsx`/`.pdf` sources by `_system/tools/export_plaintext_sources.py`. If those source files change, someone with Path A access needs to re-run that script - the CSVs don't update themselves.

## Personal story and cover email - works either way

Whether you're on Path A or Path B: you can write your personal story yourself and drop it straight into `records/{slug}/personal-note.md` (or just paste it into the chat and tell the LLM to use it as-is), **or** you can ask the assisting LLM to help you draft it conversationally - e.g. *"ask me a few questions to help me write a short personal note for this brief."* Either is fine; there's no required format beyond "a short first-person paragraph."

See `_templates/personal-note.md` for the blank stamp, and `_system/tools/finalize_send_pack.py` / the chat-only equivalent above for how it gets folded into the final brief and the cover email.
