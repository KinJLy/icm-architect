# Senate Accountability Brief — Template v2

*Based on the Gallagher ACT brief (most polished output produced so far), with sections restored from the original `Senate_Accountability_Brief_Template.docx` that the Gallagher example had dropped: Male Electors, the economic "what happens to" questions, the post-vote Accountability-after-the-vote section, the regional-communities question, and the sustainability closing lines. The Gallagher-only "Minister for Women" portfolio lens has been generalised into an optional block.*

---

## Field legend

Every `[BRACKET]` below is a field to fill in. This table is the single source of truth for what each one means and where its value comes from.

| Field | What it should contain | Source |
|---|---|---|
| `[SENATOR NAME]` | Full senator name as used in the contact list (e.g. "Katherine Gallagher") | Senate contact list |
| `[PORTFOLIO/MINISTERIAL ROLE]` | Ministerial/shadow portfolio — only include it (and the accountability-lens block below) if relevant per [portfolio-relevance.md](portfolio-relevance.md). Omit entirely otherwise. | Manual / public record |
| `[STATE/TERRITORY]` | Full state or territory name (e.g. "Australian Capital Territory") | NDIS Data Workbook |
| `[STATE ABBR]` | Short state/territory code (e.g. "ACT") | NDIS Data Workbook |
| `[PARTY]` | Full party name or "Independent" | Senate contact list |
| `[EMAIL ADDRESS]` | Senator's office email | Senate contact list |
| `[VOTE POSITION]` | Expected vote position | [vote-position-rules.md](vote-position-rules.md) |
| `[IMMEDIATE ASK]` | The specific ask for this senator | [vote-position-rules.md](vote-position-rules.md) — fixed text unless overridden |
| `[PREPARED BY]` | Name, role/organisation of whoever is sending the brief | Manual |
| `[TOTAL ELECTORS]` | Total state/territory electors | NDIS Data Workbook: `State Electors` |
| `[FEMALE ELECTORS]` | Female electors | NDIS Data Workbook: `State Female Electors` |
| `[MALE ELECTORS]` | Male electors | NDIS Data Workbook: `State Male Electors` |
| `[NDIS PARTICIPANTS]` | Active NDIS participants | NDIS Data Workbook: `Active Participants` |
| `[CHILDREN 0-14]` | Participants aged 0–14 | NDIS Data Workbook: `0-14 Years` |
| `[AUTISM PARTICIPANTS]` | Autism participants | NDIS Data Workbook: `Autism` |
| `[PSYCHOSOCIAL PARTICIPANTS]` | Psychosocial disability participants | NDIS Data Workbook: `Psychosocial Disability` |
| `[FIRST NATIONS PARTICIPANTS]` | First Nations participants | NDIS Data Workbook: `First Nations` |
| `[CALD PARTICIPANTS]` | CALD participants | NDIS Data Workbook: `CALD` |
| `[ACTIVE PROVIDERS]` | Active NDIS providers | NDIS Data Workbook: `Active Providers` |
| `[ANNUAL FUNDING]` | Annual NDIS funding exposure, in $ billions (e.g. "0.494") | NDIS Data Workbook: `Estimated Annual Funding Flow` ÷ 1,000,000,000 |
| `[1% REDUCTION]` / `[5% REDUCTION]` / `[10% REDUCTION]` | Funding at risk under a 1/5/10% cut, in $ millions | `Estimated Annual Funding Flow` × 0.01 / 0.05 / 0.10 ÷ 1,000,000 |
| `[FEMALE SHARE]` | Female electors as % of total electors | Computed: `FEMALE ELECTORS / TOTAL ELECTORS × 100` |
| `[CHILD SHARE]` | Children (0–14) as % of participants | Computed: `CHILDREN 0-14 / NDIS PARTICIPANTS × 100` |
| `[AUTISM SHARE]` | Autism participants as % of participants | Computed: `AUTISM PARTICIPANTS / NDIS PARTICIPANTS × 100` |
| `[CARERS ESTIMATE]` | Parents/carers estimate | Computed: `NDIS PARTICIPANTS × 2` |
| `[FAMILY ESTIMATE]` | Family members impacted estimate | Computed: `NDIS PARTICIPANTS × 4` |
| `[COMMUNITY ESTIMATE]` | Broader community impact estimate | Computed: `NDIS PARTICIPANTS × 6` |
| `[TOTAL FOOTPRINT ESTIMATE]` | Potential voter footprint estimate | Computed: sum of participants + carers + family + providers + community |
| `[PORTFOLIO-SPECIFIC RISK PARAGRAPH]` / `[PORTFOLIO-SPECIFIC ACCOUNTABILITY QUESTION]` / `[PORTFOLIO RISK LABEL]` / `[PORTFOLIO RISK DESCRIPTION]` | Only used in the optional Portfolio accountability lens block (see below) | Manual — only for senators holding a relevant portfolio |
| `[YOUR NAME]` / `[YOUR ROLE/TITLE]` / `[YOUR EMAIL]` | Sign-off identity | [sender-profile.md](sender-profile.md) — factory config, same for every senator, filled at the send-prep stage |
| `[PERSONAL STORY - optional, delete this whole box if none]` | A short first-person note on why the bill matters to you — makes the numbers land as human impact, not just data | Written per-senator (or reused) at the send-prep stage, in `records/{slug}/personal-note.md` |

### Rules referenced by this template

These live in their own files so they can be updated independently of the content structure — don't duplicate them here:

- **Portfolio relevance check** (do this for every senator, before deciding whether to include the accountability-lens block) → [portfolio-relevance.md](portfolio-relevance.md)
- **Vote-position rule + known overrides** (how to fill `[VOTE POSITION]`) → [vote-position-rules.md](vote-position-rules.md)
- **Fixed immediate ask** text → see [vote-position-rules.md](vote-position-rules.md)

---

## Document body

```
SENATE ACCOUNTABILITY BRIEF
[STATE/TERRITORY] | Pre-vote NDIS Amendment Bill Impact Brief
Prepared for [SENATOR NAME][, PORTFOLIO/MINISTERIAL ROLE - optional, delete if none]
```

> **Purpose of this brief**
> This is not a meeting request. It is a rapid pre-vote accountability brief focused on implementation risk, [STATE ABBR] impact, political accountability and the consequences senators may be asked to own if unintended harms emerge.

> **A personal note from [YOUR NAME]**
> [PERSONAL STORY - optional, delete this whole box if none. A short first-person note on why this bill matters to you personally makes the numbers land as human impact, not just data.]

### Senator snapshot

| Field | Details |
|---|---|
| Senator | [SENATOR NAME] |
| Portfolio relevance | [PORTFOLIO/MINISTERIAL RESPONSIBILITY - optional, delete row if none] |
| Party | [PARTY] |
| State/Territory | [STATE/TERRITORY] |
| Email | [EMAIL ADDRESS] |
| Expected vote position | [VOTE POSITION] |
| Immediate ask | [IMMEDIATE ASK] |
| Brief prepared by | [PREPARED BY - name, role/organisation] |

> **The question before the vote**
> The question is not only: Will the Bill pass? The question is: If unintended harms emerge, who will [STATE ABBR] constituents hold responsible?

### [STATE ABBR] impact snapshot

| Measure | [STATE ABBR] |
|---|---|
| Total Electors | [TOTAL ELECTORS] |
| Female Electors | [FEMALE ELECTORS] |
| Male Electors | [MALE ELECTORS] |
| Active NDIS Participants | [NDIS PARTICIPANTS] |
| Children (0-14 Years) | [CHILDREN 0-14] |
| Autism Participants | [AUTISM PARTICIPANTS] |
| Psychosocial Participants | [PSYCHOSOCIAL PARTICIPANTS] |
| First Nations Participants | [FIRST NATIONS PARTICIPANTS] |
| CALD Participants | [CALD PARTICIPANTS] |
| Active Providers | [ACTIVE PROVIDERS] |
| Annual NDIS funding exposure | $[ANNUAL FUNDING] billion |

**Key read:** The [STATE ABBR] has [NDIS PARTICIPANTS] active NDIS participants, including [CHILDREN 0-14] children and [AUTISM PARTICIPANTS] autistic participants. Women make up approximately [FEMALE SHARE]% of [STATE ABBR] electors. Children represent approximately [CHILD SHARE]% of [STATE ABBR] participants and autistic participants represent approximately [AUTISM SHARE]% of [STATE ABBR] participants.

### [PORTFOLIO] accountability lens
*(OPTIONAL — include only if the senator holds a relevant portfolio; delete this whole section otherwise)*

As [PORTFOLIO], Senator [SENATOR NAME] is being asked to consider more than program expenditure. [PORTFOLIO-SPECIFIC RISK PARAGRAPH — explain how implementation risk connects to this portfolio's responsibilities].

[PORTFOLIO-SPECIFIC ACCOUNTABILITY QUESTION]

> **[PORTFOLIO RISK LABEL]**
> [PORTFOLIO RISK DESCRIPTION]

### Community footprint

*Indicative methodology: The footprint figures below are not official headcounts. They are conservative advocacy estimates to show the multiplier effect around each NDIS participant. They should be used as a political accountability frame, not as statistical prevalence data.*

| Group | Estimated [STATE ABBR] footprint |
|---|---|
| Active NDIS participants | [NDIS PARTICIPANTS] |
| Parents and carers estimate | [CARERS ESTIMATE] |
| Family members impacted estimate | [FAMILY ESTIMATE] |
| Providers and workforce proxy | [ACTIVE PROVIDERS] |
| Broader community impact estimate | [COMMUNITY ESTIMATE] |
| Potential voter footprint estimate | [TOTAL FOOTPRINT ESTIMATE] |

> **Total community footprint**
> Estimated people directly or indirectly affected in the [STATE ABBR]: [TOTAL FOOTPRINT ESTIMATE]

### Implementation risks to own if safeguards are absent

- Increased social isolation and reduced community participation
- Reduced independence and loss of informal peer networks
- Carer burnout and greater unpaid care burden
- Reduced parent and carer workforce participation
- Increased mental health presentations and crisis service pressure
- Longer waiting lists and longer travel times
- Reduced provider choice and possible program closures
- Higher long-term support needs if early intervention and participation supports are narrowed

### Economic exposure

| Scenario | Estimated [STATE ABBR] exposure |
|---|---|
| Annual NDIS funding | $[ANNUAL FUNDING] billion |
| 1% reduction | $[1% REDUCTION] million |
| 5% reduction | $[5% REDUCTION] million |
| 10% reduction | $[10% REDUCTION] million |

> **The economic risk**
> The Bill may save money in one budget line while increasing costs across health, crisis services, family stress, workforce disengagement and long-term support needs.

*(restored from base template — dropped in the Gallagher example)*
- What happens to parent and carer workforce participation?
- What happens to small providers and sole traders?
- What happens to regional service availability?
- What happens to allied health access?
- What happens to local jobs and community organisations?

### Accountability after the vote
*(restored from base template — dropped entirely in the Gallagher example)*

If implementation produces harm, constituents are unlikely to distinguish between Treasury advice, NDIA implementation, departmental administration and parliamentary votes. Many will remember which senators supported the legislation. History rarely remembers legislation by its intent — it remembers legislation by its outcomes.

- Who supported the Bill?
- Who spoke for participants and families?
- Who sought safeguards before the vote?
- Who required transparent monitoring of outcomes?
- Who responded when concerns were raised?

### Questions constituents may ask after the vote

- What safeguards existed if participants lost supports?
- How were implementation outcomes monitored?
- What evidence would trigger policy reconsideration?
- How were carers supported if service access reduced?
- How will regional communities be protected? *(restored from base template)*
- How were women and unpaid carers protected from cost shifting?
- Who should participants contact if implementation creates harm?

### Actions requested before the vote

| Action requested | Status |
|---|---|
| Review the potential impacts on [STATE ABBR] participants, families, carers and providers | ☐ |
| Consider implementation risks alongside sustainability objectives | ☐ |
| Require gender impact safeguards for unpaid carers and women affected by service reductions | ☐ |
| Support amendments, delay or safeguards where required | ☐ |
| Advocate for transparent monitoring of participant outcomes | ☐ |
| Publicly communicate how unintended harms will be addressed should they emerge | ☐ |
| Confirm who constituents should contact if implementation creates harm | ☐ |

*(restored from base template — dropped in the Gallagher example)*
> We support a sustainable NDIS. Success should be measured by outcomes, not savings alone. Participants do not exist in isolation. Families, carers and communities share the impact.

### One-page summary for covering email

| Snapshot item | [STATE ABBR] |
|---|---|
| Participants | [NDIS PARTICIPANTS] |
| Children | [CHILDREN 0-14] |
| Autistic participants | [AUTISM PARTICIPANTS] |
| Female electors | [FEMALE ELECTORS] |
| Families affected estimate | [FAMILY ESTIMATE] |
| Providers | [ACTIVE PROVIDERS] |
| Annual funding exposure | $[ANNUAL FUNDING] billion |
| Potential voter footprint estimate | [TOTAL FOOTPRINT ESTIMATE] |
| Expected vote position | [VOTE POSITION] |

> **The core question**
> If implementation creates increased isolation, carer burnout, reduced community participation and higher long-term costs, what responsibility will Senator [SENATOR NAME] accept for those outcomes?

### Sign off

[YOUR NAME]
[YOUR ROLE/TITLE]
[YOUR EMAIL]

### Data and completion checklist

| Field | Required value | Completed |
|---|---|---|
| Senator details | [SENATOR NAME], [PARTY], [EMAIL ADDRESS], [VOTE POSITION] | ☐ |
| Elector data | [TOTAL ELECTORS], [FEMALE ELECTORS], [MALE ELECTORS] | ☐ |
| NDIS participants | [NDIS PARTICIPANTS], [CHILDREN 0-14], [AUTISM PARTICIPANTS] | ☐ |
| Equity cohorts | [PSYCHOSOCIAL PARTICIPANTS], [FIRST NATIONS PARTICIPANTS], [CALD PARTICIPANTS] | ☐ |
| Provider and workforce data | [ACTIVE PROVIDERS] providers | ☐ |
| Funding exposure | $[ANNUAL FUNDING] billion, $[1% REDUCTION] million, $[5% REDUCTION] million, $[10% REDUCTION] million | ☐ |
| Community footprint | [CARERS ESTIMATE], [FAMILY ESTIMATE], [TOTAL FOOTPRINT ESTIMATE] | ☐ |
| Immediate ask | [IMMEDIATE ASK] | ☐ |
| Portfolio (if applicable) | [PORTFOLIO/MINISTERIAL RESPONSIBILITY] | ☐ |

*Source note: Prepared from the Senate Accountability Brief Template, the Senate NDIS Data Workbook and the Senate Contact List. Figures should be checked against final source data before distribution.*

---

*Footer (for the eventual Word/PDF output): "Replace all [square bracket] fields | Pre-vote senator brief" — left / "Prepared by [YOUR NAME] ([YOUR EMAIL]) | Pre-vote accountability brief" — right.*
