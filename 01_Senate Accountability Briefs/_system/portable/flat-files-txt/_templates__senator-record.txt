---
type: senator-record
slug: ""
senator_name:
party:
party_abbr:
state:
state_abbr:
email:
portfolio:
vote_position:
vote_position_source: rule
status: new
validated: false
custom-width: 100
---

<!-- slug: kebab-case-name, e.g. katherine-gallagher. Left as a quoted empty
     string above (not a {bracket}) because curly braces in YAML frontmatter
     get parsed as a flow-map and silently mangle the field. -->

# {Senator Name} — record

Field meanings and sources: [../01_reference/brief-template.md](../01_reference/brief-template.md)

## Pulled data
*(from `01_reference/source-data/` — regenerate via `_system/tools/extract_senator_data.py`, don't hand-edit these)*

- Total Electors:
- Female Electors:
- Male Electors:
- Active NDIS Participants:
- Children (0-14 Years):
- Autism Participants:
- Psychosocial Participants:
- First Nations Participants:
- CALD Participants:
- Active Providers:
- Annual NDIS Funding Exposure ($ billion):

## Computed fields
*(formulas: [../01_reference/brief-template.md](../01_reference/brief-template.md) field legend)*

- Female Share (%):
- Child Share (%):
- Autism Share (%):
- 1% Reduction ($ million):
- 5% Reduction ($ million):
- 10% Reduction ($ million):
- Carers Estimate:
- Family Estimate:
- Community Estimate:
- Total Footprint Estimate:

## Portfolio relevance check
*(rule: [../01_reference/portfolio-relevance.md](../01_reference/portfolio-relevance.md); snapshot lookup: [../01_reference/senator-portfolios.md](../01_reference/senator-portfolios.md) — confirm currency, don't trust the snapshot blindly)*

- Full title on public record (context only, not what goes in the brief):
- Matched portfolio (used as `[PORTFOLIO/MINISTERIAL ROLE]` if relevant):
- Relevant to this bill? Y/N —
- If yes, the specific mechanism (not a generic paragraph):

## Vote position
*(rule: [../01_reference/vote-position-rules.md](../01_reference/vote-position-rules.md))*

- Position:
- Source: rule | override — {cite if override}

## Validation checklist

- [ ] Elector data matches `01_reference/source-data/Senate ndis table completed.xlsx`
- [ ] NDIS participant data matches the workbook
- [ ] Party/email match `01_reference/source-data/senate contact list.pdf`
- [ ] Portfolio relevance actively checked (not defaulted to blank)
- [ ] Vote position checked against the rule + any known override
- [ ] Immediate ask correct (fixed text, unless a reason to override)
- [ ] No leftover `[BRACKET]` placeholders

## Human notes

