"""
Build folder-free exports of this ICM's reference material (rules, template,
method, plain-text data), for LLM platforms that can't take a zip or a nested
folder upload. Four outputs, covering different real constraints:

  _system/portable/flat-files/       every included file, original extension,
                                      flattened filename (path separators ->
                                      "__"), no subfolders - for platforms
                                      that accept multiple individual file
                                      uploads but not folder structure.

  _system/portable/flat-files-txt/   the same, but every file renamed to
                                      .txt - for platforms whose upload
                                      dialog filters by extension and won't
                                      accept .md/.csv even though the content
                                      is plain text. Markdown notation is
                                      NOT stripped - the consumer is an LLM,
                                      which reads markdown structure fine as
                                      plain text; only the extension changes.

  _system/portable/bundle.md         every included file concatenated into
  _system/portable/bundle.txt        ONE document with clear <<<FILE: path>>>
                                      markers, identical content in both -
                                      for platforms that only take one
                                      upload, or where you'd just paste the
                                      text directly. bundle.txt exists for
                                      the same extension-filter reason as
                                      flat-files-txt/.

Most binary files (.xlsx/.pdf) are deliberately excluded - they can't be
usefully flattened into text. Their plain-text equivalents (brief-template.md,
the source-data CSVs) are included instead. Two exceptions (see BINARY_INCLUDE
below): brief-template.docx and the Gallagher example stay as real .docx files
in flat-files/ only, for the "ask a code-capable chat LLM to fill in the real
docx" workflow documented in chat-only-workflow.md's Path B+ - a markdown
mirror isn't enough for that, it needs the actual template file. They're
skipped in flat-files-txt/ and both bundles, since a docx can't usefully
become .txt or get pasted into a text bundle.

  _system/portable/start-here/       the "silly-proof" minimum: bundle.md,
                                      bundle.txt, brief-template.docx, the
                                      Gallagher example docx, and one plain
                                      instructions file - 5 files, clean
                                      names, no flattening needed since
                                      there's no collision risk at this size.
                                      For someone who just wants the smallest
                                      possible thing to drop into a chat
                                      window without first understanding the
                                      other three exports.

This is a generated artifact, like _index/log.md - don't hand-edit the output,
re-run this script instead. Re-run whenever a reference file changes.

Usage:
    python build_portable_bundle.py
"""
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent  # _system/tools -> _system -> workspace root
PORTABLE_DIR = BASE / "_system" / "portable"

# Curated, not a blind directory walk - keeps the bundle to what a chat-only
# user actually needs to get started (method + rules + template + data),
# not the whole working instance (records/, 02_output/, etc.).
INCLUDE = [
    "CLAUDE.md",
    "README.md",
    "01_reference/brief-template.md",
    "01_reference/campaign-brief.md",
    "01_reference/chat-only-workflow.md",
    "01_reference/decisions-and-lessons.md",
    "01_reference/portfolio-relevance.md",
    "01_reference/sender-profile.md",
    "01_reference/senator-portfolios.md",
    "01_reference/vote-position-rules.md",
    "01_reference/source-data/senate-ndis-table.csv",
    "01_reference/source-data/senate-contact-list.csv",
    "_templates/senator-record.md",
    "_templates/personal-note.md",
    "_system/icm-method/SKILL.md",
    "_system/icm-method/README.md",
    "_system/icm-method/ABOUT-THIS-COPY.md",
    "_system/icm-method/references/core.md",
    "_system/icm-method/references/forms.md",
    "_system/icm-method/assets/templates/CLAUDE.md",
    "_system/icm-method/assets/templates/CONTEXT.md",
    "_system/icm-method/assets/templates/node.md",
    "_system/icm-method/assets/templates/questionnaire.md",
    "_system/icm-method/assets/templates/schema.md",
    "_system/icm-method/assets/templates/stage-CONTEXT.md",
]

# Real .docx files, flat-files/ only (see the note above on why).
BINARY_INCLUDE = [
    "01_reference/brief-template.docx",
    "01_reference/examples/Gallagher ACT Accountability Brief.docx",
]


def flatten_name(rel_path: str, force_txt: bool) -> str:
    flat = rel_path.replace("/", "__")
    if force_txt:
        flat = Path(flat).with_suffix(".txt").name
    return flat


def build_flat_files(force_txt: bool):
    out_dir = PORTABLE_DIR / ("flat-files-txt" if force_txt else "flat-files")
    out_dir.mkdir(parents=True, exist_ok=True)
    for existing in out_dir.glob("*"):
        existing.unlink()

    files = INCLUDE if force_txt else INCLUDE + BINARY_INCLUDE
    for rel in files:
        src = BASE / rel
        if not src.exists():
            print(f"WARN: missing, skipped: {rel}")
            continue
        dest = out_dir / flatten_name(rel, force_txt)
        dest.write_bytes(src.read_bytes())
    print(f"Wrote {len(list(out_dir.glob('*')))} flat files to {out_dir}")


def build_bundle_text() -> tuple[str, int]:
    parts = [
        "# Senate Accountability Briefs — portable ICM bundle",
        "",
        "Every reference file this ICM needs to work from, concatenated into one document",
        "for platforms that only take a single file upload (or plain paste). Each section",
        "below is one file from the workspace, marked with its original path so an LLM can",
        "still reason about the folder structure even though there isn't one here.",
        "",
        "Generated by `_system/tools/build_portable_bundle.py` - don't hand-edit this file,",
        "re-run that script instead if a source file changes.",
        "",
        "---",
    ]
    included = 0
    for rel in INCLUDE:
        src = BASE / rel
        if not src.exists():
            print(f"WARN: missing, skipped: {rel}")
            continue
        parts.append(f"\n<<<FILE: {rel}>>>\n")
        parts.append(src.read_text(encoding="utf-8"))
        parts.append(f"\n<<<END FILE: {rel}>>>\n")
        parts.append("---")
        included += 1
    return "\n".join(parts), included


def build_bundle_files():
    text, included = build_bundle_text()
    for name in ("bundle.md", "bundle.txt"):
        out_path = PORTABLE_DIR / name
        out_path.write_text(text, encoding="utf-8")
        print(f"Wrote {out_path} ({included} files, {out_path.stat().st_size:,} bytes)")


START_HERE_INSTRUCTIONS = """START HERE
==========

You have 5 files in this folder:

1. bundle.md  OR  bundle.txt  -  pick ONE of these two (they're identical content,
   just two file types in case your chat rejects one of them). This has everything:
   the brief template, the rules for vote position and portfolios, and every
   senator's data.
2. brief-template.docx  -  the blank Word document itself.
3. Gallagher example brief.docx  -  a real filled-in example, so you (or the AI)
   can check the result looks right.
4. This file.

WHAT TO DO
----------
1. Open a chat with any AI (ChatGPT, Claude, Gemini, etc).
2. Drop in bundle.md (or bundle.txt) and brief-template.docx. Add the Gallagher
   example too if you want the AI to compare its output against a real one.
3. Type something like this, filling in the senator's name:

   "I've attached reference material for the NDIS Senate Accountability Briefs
   project, plus a blank Word template (brief-template.docx). I want a completed
   brief for Senator [SENATOR NAME]. Find that senator's data in the attached
   material, check whether they hold a relevant portfolio and what their expected
   vote position is (the rules for both are in the attached material), then fill
   in brief-template.docx with everything using python-docx if you're able to run
   code. If you can't run code, just give me the completed brief as text and I'll
   paste it into Word myself."

4. Want to add your own story? Mention it in that same message, or paste it in
   separately, or ask the AI to help you write one with a few questions.

That's it. Everything else in this workspace (the full folder structure, the
individual reference files, the automated scripts) is for when you want more
control, or you're working with an AI that has direct file/code access to the
whole thing rather than just a chat window.
"""


def build_start_here():
    out_dir = PORTABLE_DIR / "start-here"
    out_dir.mkdir(parents=True, exist_ok=True)
    for existing in out_dir.glob("*"):
        existing.unlink()

    (out_dir / "bundle.md").write_bytes((PORTABLE_DIR / "bundle.md").read_bytes())
    (out_dir / "bundle.txt").write_bytes((PORTABLE_DIR / "bundle.txt").read_bytes())
    (out_dir / "brief-template.docx").write_bytes((BASE / "01_reference/brief-template.docx").read_bytes())
    (out_dir / "Gallagher example brief.docx").write_bytes(
        (BASE / "01_reference/examples/Gallagher ACT Accountability Brief.docx").read_bytes()
    )
    (out_dir / "START HERE.txt").write_text(START_HERE_INSTRUCTIONS, encoding="utf-8")
    print(f"Wrote {len(list(out_dir.glob('*')))} files to {out_dir}")


if __name__ == "__main__":
    PORTABLE_DIR.mkdir(parents=True, exist_ok=True)
    build_flat_files(force_txt=False)
    build_flat_files(force_txt=True)
    build_bundle_files()
    build_start_here()
