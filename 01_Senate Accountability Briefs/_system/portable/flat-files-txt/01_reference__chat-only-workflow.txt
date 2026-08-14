# Chat-only workflow (no code execution)

This ICM has three paths. Pick whichever matches what you actually have access to.

**In a hurry, or not sure where to start?** Skip straight to `_system/portable/start-here/` - 5 files, one plain-English instructions file, nothing else to understand first. Everything below explains the fuller set of options and the reasoning behind them, for when you want more control.

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

### Path B+ — getting a real Word doc back, if your chat platform runs code

Some chat platforms have code execution built in even without full agentic file-system access - ChatGPT's Code Interpreter/Advanced Data Analysis is the clearest example; some Claude.ai sessions can do this too. If yours can, you can skip the "paste markdown into Word yourself" step and get an actual formatted `.docx` back.

**The important part:** don't ask it to invent a Word document from scratch - that produces something that looks nothing like the real template. Instead, upload the actual `brief-template.docx` (found in `_system/portable/flat-files/` as `01_reference__brief-template.docx`, or at `01_reference/brief-template.docx` if you have folder access) and have it edit *that* file with `python-docx`.

**What to ask it to do**, after uploading `brief-template.docx` and giving it the senator's filled-in data (from the Path B step above, or directly from a `records/{slug}/record.md`):

> I've attached `brief-template.docx`, a Word document with `[BRACKET]` placeholder fields, plus one optional section headed "[PORTFOLIO] accountability lens" with a matching "Portfolio relevance" table row. Using Python (`python-docx`), open this document and:
>
> 1. Replace every `[BRACKET]` field with the corresponding value from the data below. Do this in paragraphs, table cells, **and the page header and footer** - not just the main body text (the header repeats the senator's name and state on every page).
> 2. If no portfolio value is given (or it's not relevant), delete the whole "[PORTFOLIO] ... accountability lens" section entirely - its heading, both paragraphs under the heading, and its callout table - plus the "Portfolio relevance" row in the Senator snapshot table. Don't leave placeholder text visible.
> 3. If a portfolio value *is* given, keep that section, but remove the "(OPTIONAL - include only if...)" instructional phrase from its heading - that note is for whoever fills the template in, not for the final reader.
> 4. Leave `[YOUR NAME]`, `[YOUR ROLE/TITLE]`, `[YOUR EMAIL]`, and `[PREPARED BY - name, role/organisation]` exactly as they are unless I've given you values for those too.
> 5. Save the result and give me the file to download.
>
> Here is the data: [paste the filled fields - either the plain-text brief the Path B prompt produced, or the record's Pulled data / Computed fields / Portfolio relevance / Vote position sections directly]

This mirrors what `_system/tools/render_brief_docx.py` actually does - the header/footer step and the "delete, don't blank out" handling of the optional section are the two easiest things to get wrong, which is why they're spelled out explicitly above rather than left for the model to guess.

**A worked example to sanity-check the result against:** `01_reference__examples__Gallagher ACT Accountability Brief.docx`, also in `_system/portable/flat-files/` - the real polished output this template is built to match (a `.docx` can't be usefully flattened to `.txt`, it's a binary/zipped format, so this one stays as an actual Word file in the flat-files export rather than in `flat-files-txt/` or `bundle.md`).

## Path C — no folders, no zip (single-file or multi-file-flat platforms only)

Some platforms won't take a zip, won't preserve folder structure on upload, or only accept a handful of individual files at once with no nesting. `_system/tools/build_portable_bundle.py` exists specifically for this - it produces four folder-free exports of everything Path B needs (plus the method itself), regenerated from source, in `_system/portable/`:

- **`_system/portable/flat-files/`** - every reference file, original extension, copied with a single flattened filename (e.g. `01_reference/brief-template.md` → `01_reference__brief-template.md`) and no subfolders. Select all of them and drag into any uploader that takes multiple individual files but not folders.
- **`_system/portable/flat-files-txt/`** - the same files, but every one renamed to `.txt`, for platforms whose upload dialog filters by file extension and rejects `.md`/`.csv` outright even though the content is plain text. The markdown notation inside (`#`, `**`, tables, `[links]`) is **not** stripped - only the extension changes. That's a deliberate choice: the consumer here is an LLM, which reads markdown structure fine as plain text regardless of extension, and stripping it would lose real information (table structure, emphasis) for no benefit. If a human is going to read one of these directly rather than feed it to an LLM, `.md` opened in something markdown-aware (Obsidian, VS Code) will look far better than either `.txt` version.
- **`_system/portable/bundle.md`** / **`bundle.txt`** - the same files concatenated into one document with `<<<FILE: path>>>` markers (byte-identical content, just two extensions), for platforms that only take a single upload, or where you'd rather just paste the whole thing into the chat box in one go. At time of writing it's roughly 130KB - well inside the context window of any current model, but check the platform's own upload/paste limit if it's an unusually small one.

All four are generated, not hand-maintained - if a reference file changes, re-run `python _system/tools/build_portable_bundle.py` to refresh them (this needs Path A access; if you don't have that either, ask whoever maintains this workspace to regenerate it for you).

Most binary files (`.xlsx`, `.pdf`) are deliberately left out of all four exports for the same reason as Path B - they can't be usefully flattened into text. Their plain-text equivalents are what's actually included. Two exceptions: `flat-files/` also includes `01_reference__brief-template.docx` and `01_reference__examples__Gallagher ACT Accountability Brief.docx` as real, unflattened `.docx` files - needed for the Path B+ "get a real Word doc back" workflow above, which requires the actual template file, not its markdown mirror. They're absent from `flat-files-txt/` and both bundles, since neither a renamed-to-`.txt` docx nor one pasted into a text bundle would be usable.

## Personal story and cover email - works on every path

Whether you're on Path A, B, or C: you can write your personal story yourself and drop it straight into `records/{slug}/personal-note.md` (or just paste it into the chat and tell the LLM to use it as-is), **or** you can ask the assisting LLM to help you draft it conversationally - e.g. *"ask me a few questions to help me write a short personal note for this brief."* Either is fine; there's no required format beyond "a short first-person paragraph."

See `_templates/personal-note.md` for the blank stamp, and `_system/tools/finalize_send_pack.py` / the chat-only equivalent above for how it gets folded into the final brief and the cover email.
