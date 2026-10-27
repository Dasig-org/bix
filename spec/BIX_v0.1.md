# Bayanihan Information Exchange (BIX) · v0.1 draft for co-design

**Status:** working draft, 2026-10-24. Nothing here is final until organizations have shaped it.
**Name:** Bayanihan Information Exchange (BIX). Write the full name before the abbreviation, because "BIX" is also IATA's Baggage Information eXchange and the ISO 639-3 code for Bijori. For the same reason, "bix" is never used as a code value or namespace inside records; namespaces use `bayanihan:` or a full URL.
**Lineage:** BIX stands on two references, each with a different job.

- **HL7® FHIR®** gives the resource pattern: resources, references, lifecycles, extensions and bundles. FHIR® is the registered trademark of HL7 and is used with the permission of HL7. BIX is not affiliated with or endorsed by HL7.
- **Civic Accountable Entities (CAE)**, part of [Civic Interconnect](https://github.com/civic-interconnect/civic-interconnect), gives the ontology: every BIX resource type is one of CAE's six kinds of civic thing. Civic Interconnect's Civic Exchange Protocol (CEP) is where confirmed BIX work can be exported. BIX is not affiliated with or endorsed by Civic Interconnect.

**What BIX adds.** Civic Interconnect records what has happened, for accountability afterwards, and leaves "operational layers" outside its scope. BIX is an operational layer: it coordinates work that hasn't happened yet (plans, needs, offers, open steps, reports owed), with rules for who may move it forward, and produces accountable records once it has.

**Scope: the everyday work of volunteer clubs and nonprofits.** BIX is designed first for the ordinary week: a parish feeding program, a youth club's tutoring sessions, a Rotary or JCI chapter's project cycle, a scholarship program's monitoring, a monthly coastal cleanup. Disaster response is one profile of the same model, not its premise. If a resource only makes sense in a crisis, it doesn't belong in the core.

The draft has two parts:

- **Part A** is the conversation with organizations. The first conversation is about them: their story, their advocacy, their community. It ends with an invitation, not a list of questions. Making sense of what they share is our job, done afterwards.
- **Part B** is the technical v0.1. It's the contract the engine and the model have to follow.

Part A changes Part B, not the other way round.

---

# Part A · The conversation

## A1 · The first conversation

**What it's for.** Three things, in this order:

1. Getting to know the group: their story, what they stand for, and the community they serve.
2. Understanding their work from their own experience. Disaster response may be part of that story, but it's rarely all of it.
3. Getting one message across: they can help develop something bigger, alongside other groups, that also helps them work better in their own organization and community.

It isn't for collecting specifics. Nothing in the first conversation should feel like a form being filled in.

**Before.** Learn about them first: their page, their recent posts, what they've run, the cause they keep coming back to. Open with something specific to them, so it's clear this conversation is about their group and not a script.

**During.**

- **Start with them.** Say what you noticed and appreciate about their work.
- **Share why you're doing this, in your own words.** Keep it short. It gives them permission to share their own story.
- **Invite their story,** then mostly listen. Something as open as "I'd love to hear how your group started, and what keeps you going." Follow where they take it.
- **Reflect back what you heard,** in their words, so they know it landed.
- **Then make the invitation.** *(Placeholder, to be said in your own words:)* groups like yours do important work that rarely gets recorded or recognized. We want to build something bigger, together with a few groups, that helps each group run its work more easily and shows what it achieves. Nothing is built yet, and we'd love you to help shape it.
- **Close warmly.** Ask if they'd like to keep talking, and whether there's another group they think should be part of this.

**Keep it light.**

- No screens, no spec and no checklist.
- Ask if it's alright to jot a few notes. Write the fuller notes right after, while it's fresh.
- If they're comfortable, ask whether you may quote them later without naming them.

**Our responsibility.** Making sense of what they shared is our job, not theirs. Section A2 is how we do it afterwards.

**What success looks like.** They want to talk again, or they introduce another group. Specifics come later.

## A2 · Making sense of it afterwards

| When they talk about… | It shapes |
|---|---|
| Who helps: the core team, the regulars, the people who show up once | **Person, Role** |
| Their group, and who they answer to: parish, chapter, national office, LGU | **Organization** |
| Where things happen and how they give directions | **Location** |
| Their programs, and what repeats versus what happens once | **Initiative** |
| What they're always short of | **Need** |
| People and businesses offering things, and offers that got lost | **Offer** |
| How work gets handed out and who follows up | **Task, TaskDefinition** |
| Reports, receipts, photos, and who asks for them | **Provenance** |
| What they'd never want shared, and who they already share with | **SharingPolicy** |
| Which languages they write in, their phones, their signal | **Model and device constraints** |

If something in the table didn't come up, leave it blank. Don't go back to ask for it. It may come up naturally in a later conversation, or it may not matter to this group.

**Signs of real buy-in, over time:** they agree to keep talking, introduce another group, and eventually offer one real activity to try something on. Interest alone isn't buy-in.

## A3 · Follow-up questions for later conversations

These aren't for the first conversation. Use them in later conversations, and only when a specific part of their work needs understanding and the conversation is already heading there. Pick one or two, never the list.

**Their work**

- How did your group start, and what keeps you going?
- Tell me about the last thing you ran, from the first message to after it was over.
- Who made it happen?
- What does an ordinary month look like for your group?
- *Gentle follow-ups:* Who else was involved? What happened next? How did you know it went well?

**What's hard**

- What part of running your group takes more out of you than it should?
- Tell me about a time something fell through the cracks.
- After an activity, what do you wish you didn't have to do?
- When people want to help, what makes it hard to take them up on it?

**Being part of it**

- Would helping shape it be worth your time?
- What would it have to do for you to be glad you joined?
- Who else should we be talking to?

**Two habits for any follow-up.** Ask about a real, recent time rather than a hypothetical: "the last one you ran" gets a truer answer than "would you use…?" And write down their words as they say them, including the Filipino. Their vocabulary becomes the spec's vocabulary.

---

# Part B · Technical v0.1

## Design principles

1. **Resources and references.** Every record is a self-contained resource with a permanent ID, and it links to other resources by reference. *(Same as FHIR.)*
2. **Roles, not person types.** There is one `Person` resource. "Volunteer", "officer" and "beneficiary representative" are `Role`s held by a Person, for a period, relative to an Organization. *(Same pattern as FHIR's `Practitioner` vs `PractitionerRole`.)*
3. **Program the type, not the instance.** A `TaskDefinition` defines, once, which steps a kind of Offer or Need requires. `Task`s are generated from it. Nobody breaks down an individual need by hand.
4. **Propose, then commit.** Anything a model produces has `intent: proposal` and `status: draft`. Only a person, or a deterministic rule, can move it forward. *(FHIR's `Task.intent` already includes `proposal`.)*
5. **Provenance on every change.** Every state change writes a `Provenance` record saying who did it, whether a person or a model proposed it, and who confirmed it.
6. **Minimal data about people.** Beneficiaries are recorded as counts or households by default, not as named individuals.
7. **Local first.** Records are created offline and synced as `Bundle`s. The rules for which state can follow which are enforced the same way on the device and on the server.
8. **Roll up, don't compete.** Locations carry PSGC codes, and categories map to existing sector lists. That way BIX records can be summarized into 3W-style figures (who, what, where) for HDX-style systems.
9. **An ordinary week first.** Every resource and every lifecycle must make sense for routine work: a weekly session, a monthly meeting, an annual report. Disaster response is a profile that adds categories and urgency. It doesn't add new core resources.
10. **Every resource type has a CAE kind.** Each type is one of CAE's six kinds: Actor, Site, Instrument, Event, Jurisdiction or Observable (see "CAE kinds" below). The kind belongs to the type, so records carry no extra field for it. A new resource type, including one added by a module, must declare its kind. Roles are relationships, never a kind. *(From CAE.)*
11. **Reports are derived, not typed in.** A report's figures are calculated from confirmed records by a declared rule, so the same records always give the same numbers. A model may draft a report's narrative; it never sets a figure. *(CAE treats measured values as Observations, separate from the events they measure.)*

## Elements every resource has

| Element | Rule |
|---|---|
| `resourceType` | One of the resources below |
| `id` | UUID, assigned where the record is created (including offline). Never reused. |
| `meta.version` | Integer, goes up on every change |
| `meta.lastUpdated` | Server time once synced. Client time goes in `Provenance`. |
| `meta.previousHash` | SHA-256 of the previous version's canonical form, so the revision history is tamper-evident. Borrowed from CEP's `previousRecordHash`. Optional in v0.1. Computed over the record's canonical form under **RFC 8785** (JSON Canonicalization Scheme), decided 2026-10-27; CEP's own encoding (CEC) is used only by the CEP export adapter. |
| `meta.profile` | The versioned type URL, e.g. `https://bix.example/v0.1/Offer` (domain to be decided) |
| `sharing` | `private` · `organization` · `partners` · `network` · `public` |
| `language` | BCP 47 code for any free text, e.g. `fil`, `en`. Mixed Filipino-English text is tagged `fil`. |
| `extension[]` | Namespaced additions. An extension may never redefine a core element. |

## Data types

| Type | Elements | Notes |
|---|---|---|
| `Reference` | `reference` (`{type}/{id}` or a full URL), `display` | As FHIR |
| `Quantity` | `value`, `unit` (BIX unit list) | Rule 6 |
| `Period` | `start`, `end` | ISO 8601 with offset |
| `Coding` | `system`, `code`, `display` | `system` is `bayanihan:{value-set}` or a module's namespace |
| `Attachment` | `contentType`, `url`, `hash` (SHA-256), `size`, `title`, `capturedAt` | As FHIR. Photos, receipts and attendance sheets. The file lives in the implementation's storage; the record holds its address and fingerprint. |

**Media.** Images are Attachments on `Person.photo`, `Organization.image`, `Initiative.image`, `Task.output[].attachment[]` and `Report.attachment[]`. A photo is shared no more widely than the record that holds it. Link previews and public pages may show only an `Initiative.image` or `Organization.image` whose record is `public`, never a Task's photos, because those often show beneficiaries, including children.

**Proof** is not a separate resource. It is a Task's `output[]` and attachments, confirmed by a verifier who is not the performer.

## Value sets

| Value set | Codes in v0.1 |
|---|---|
| `bayanihan:permission` | `org.manage` · `member.manage` · `initiative.plan` · `task.assign` · `task.confirm` · `report.submit` |
| Default permissions by role | officer: all six · core-member: `initiative.plan`, `task.assign`, `task.confirm` · member, volunteer-regular, volunteer-episodic, service-learning: none beyond claiming open work · partner-representative, donor: none |
| `bayanihan:requirement` | `can-drive` · `has-vehicle` · `adult` · `first-aid` · `can-tutor` (organizations add local codes in their own namespace) |
| `bayanihan:figure-rule` | `count-tasks` {`taskCode`} · `sum-task-hours` {`taskCode`} · `sum-task-output` {`outputCode`} · `sum-received` {`needCategory`} · `sum-part-reports` {`figureCode`} |
| `bayanihan:report-figure` | `sessions-held` · `volunteer-hours` · `volunteers-active` · `households-served` · `learners-served` · `goods-received` · `waste-collected` |

Any confirmed Task counts toward a figure only if its `executionPeriod` lies inside the Report's `period`.

## Resources in v0.1

| Resource | Closest FHIR resource | Purpose | Key elements |
|---|---|---|---|
| `Person` | Person / Practitioner | One human, one record across organizations | `name` {`text`, `use`: nickname · full} (a nickname alone is enough), `photo` (Attachment, optional, set only by the person), `contact` (optional), `managedBy` (the Organization that created the record until the person claims it, then the person) |
| `Organization` | Organization | Any group, registered or informal | `name`, `image` (Attachment: logo or group photo), `kind` (registered-npo · faith-based · civic-club · sk-council · school-org · cooperative · informal · lgu-unit…), `partOf` (e.g. a chapter's national body, a ministry's parish), `registration[]` |
| `Role` | PractitionerRole | A Person's relationship to an Organization | `person`, `organization`, `code` (officer · member · core-member · volunteer-regular · volunteer-episodic · service-learning · partner-representative · donor), `status` (requested · active · ended), `period`, `permissions[]` (codes from `bayanihan:permission`; defaults come from `code`), `qualification[]` (codes from `bayanihan:requirement`, e.g. `can-drive`) |
| `Location` | Location | A place | `name`, `description` (the landmark text), `psgc` (barangay level or above), `position` (optional lat/lon), `partOf` |
| `Initiative` | PlanDefinition / CarePlan | Any organized effort. Can be nested: a year's plan holds programs and projects; a recurring program holds one session per occurrence. | `title`, `kind` (plan · program · project · session), `image` (Attachment: the cover; sessions use their program's unless they set one), `status`, `organization`, `partOf`, `period`, `recurrence`, `category[]`, `location[]`, `target[]` {`code`, `value`, `unit`} (same codes as Report figures), `taskDefinition[]`, `partner[]` (co-hosting Organizations; display and credit only in v0.1) |
| `Need` | SupplyRequest (generalized) · Schema.org `Demand` | What an initiative is short of: people, goods, money, skills, transport or a venue. Can recur with the initiative. | `initiative`, `category`, `quantity` {value, unit}, `received`, `neededBy`, `recurrence`, `location`, `priority` (routine · urgent), `status` |
| `Offer` | *No FHIR equivalent* · Schema.org `Offer` | What someone has and will give: goods, time, a skill, a vehicle, a venue | `offeredBy` (a Person or an Organization), `category`, `quantity`, `location`, `availableFrom`, `availableUntil`, `recurrence`, `matchedTo` (a Need), `status` |
| `TaskDefinition` | ActivityDefinition | The reusable template for a kind of work. Examples: `session-staffing` (serve, check in, close), `goods-transfer` (collect, deliver, confirm receipt), `expense-claim` (buy, file receipt, approve), `report-owed` (gather, draft, submit). | `appliesTo` (Initiative, Offer or Need categories), `steps[]` {`code`, `dependsOn`, `requires[]`, `evidence`, `confirmerRole`, `autoConfirm`}, `status`, `author`, `ratifiedBy` |
| `Task` | Task | One claimable step | `intent` (proposal · plan · order), `status`, `code`, `focus` (any resource: an Offer, a Need, or a module's type such as an Animal), `priority` (routine · urgent), `definition`, `requester` (an Organization), `owner` (the Person who claimed it or was asked), `restriction` {`period`, `location`}, `requires[]` (codes from `bayanihan:requirement`), `executionPeriod` {`start`, `end`} (when the work actually happened), `output[]` {`code`, `value`, `unit`, `attachment[]`}, `note[]` {`author`, `time`, `text`} (including thanks), `verification` |
| `Provenance` | Provenance | Who did what, and who confirmed it | `target[]`, `activity` (propose · create · update · claim · assign · accept · decline · release · complete · confirm · dispute · cancel · submit · return · acknowledge · claim-identity · merge), `agent[]` {`type`: author · performer · verifier · model, `who`, `onBehalfOf`}, `occurredAt` (client time), `recorded`, `offline`, `model` {name, version} |
| `SharingPolicy` | Consent | One organization's default sharing rules per category | `organization`, `rules[]` {`category`, `sharing`}, `approvedBy` |
| `Report` | MeasureReport (loosely) | A report one organization owes another (a chapter to its national body, a ministry to its parish, a group to its LGU or a donor), with figures derived from confirmed records | `owedBy` (Organization), `owedTo` (Organization), `period`, `due`, `recurrence`, `scope` {`initiative[]`, `includeParts`}, `figures[]` {`code`, `value`, `unit`, `rule` {`code`, `params`}, `derivedFrom[]`, `derivedAt`}, `missingParts[]`, `narrative`, `attachment[]` (photos and documents chosen from the confirmed Tasks' outputs), `replaces`, `submittedBy`, `status` |
| `Bundle` | Bundle | The sync and exchange envelope | `type` (sync · transaction), `entry[]` {`fullUrl`: `urn:uuid:…`, `resource`} |

### Report, in more detail

A `Report` is an obligation first and a document second. It exists as soon as it is owed, so a coordinator can see what is due before anyone starts writing.

- **Figures.** Each figure has a `code` from `bayanihan:report-figure`, a `rule` from `bayanihan:figure-rule` with its parameters, and `derivedFrom[]`, the confirmed records it counts. Figures are recalculated, never edited.
- **Which part reports count.** `sum-part-reports` adds only parts' Reports that are `submitted` or `acknowledged`, carry the same figure code, and whose `period` lies inside the reporting period. Parts that haven't reported are listed in `missingParts[]`, never estimated.
- **Corrections.** A correction is a new Report with `replaces` pointing at the one it corrects.
- **Federated organizations.** With `scope.includeParts: true`, a report also counts the work of every organization that is `partOf` the one that owes it. A national body's figures can come from its chapters in two ways:
  - from the chapters' own **submitted** `Report`s, summed figure by figure (the usual case, because each chapter submits and stands behind its own numbers);
  - from the chapters' confirmed records directly, where they share them with the national body.
  Either way, a figure can only count records the reporting organization is allowed to see under the chapters' `SharingPolicy`.
- **Narrative.** Free text. A model may draft it as a proposal from the figures and the period's Provenance; a person edits and submits it.
- **The work.** The steps (gather, draft, submit) come from the `report-owed` TaskDefinition, like any other kind of work.

## CAE kinds

Every resource type is one of CAE's six kinds. The kind is fixed by the type.

| BIX resource | CAE kind | Why |
|---|---|---|
| `Person`, `Organization` | Actor | They take part in civic work and can be held to account |
| `Location` | Site | A place. Its PSGC code identifies the barangay or municipality, which is a Jurisdiction in CAE terms. |
| `Initiative` | Instrument | A program or plan that structures what happens |
| `TaskDefinition` | Instrument | Defines what a kind of work requires |
| `SharingPolicy` | Instrument | A rule about what may be shared |
| `Need` | Instrument | An open ask. *Provisional; see the CEP section.* |
| `Offer` | Instrument | An open commitment. *Provisional; see the CEP section.* |
| `Report` | Instrument | An obligation owed to someone |
| `Report.figures[]` | Observable | Measured values, derived by a rule |
| `Task` | Event, **once completed and confirmed** | Until then it is planned work, which CAE has no kind for. That gap is what BIX exists to fill. |
| `Role` | *Relationship, not a kind* | A Person's relationship to an Organization |
| `Provenance` | *Attestation, not a kind* | Who did what and who confirmed it |
| `Team` | Actor | A collective participant |
| `InitiativeTemplate`, `ShareLink` | Instrument | |
| `Communication` | *Relationship, not a kind* | |
| `Bundle` | *Transport, not a kind* | Like CEP's record envelope |

## Lifecycles

| Resource | States | Notes |
|---|---|---|
| Need | `draft → open → partially-met → met`, plus `cancelled` | `partially-met` and `met` are calculated from `received` vs `quantity`. A recurring Need opens again with each session of its Initiative. |
| Offer | `draft → available → matched → fulfilled`, plus `expired`, `withdrawn` | `expired` is set by rule when `availableUntil` passes |
| Task | `draft → ready → accepted → in-progress → completed`, plus `requested`, `cancelled`, `failed`, `on-hold` | Follows FHIR's meaning of `requested`. **`ready`:** open, no owner, anyone eligible may claim. **Claiming** sets `owner` to oneself: `ready → accepted`. **Asking** a named person: `ready → requested` with `owner` set. They **accept** (`requested → accepted`) or **decline** (`requested → ready`, `owner` cleared). **Releasing** an accepted Task returns it to `ready`. `in-progress` is optional. |
| Task.verification | `pending → confirmed`, or `pending → disputed` | A BIX extension to FHIR. `confirmed` needs a `verifier` agent who is not the performer. |
| Initiative | `draft → planned → active → completed`, plus `cancelled` | `planned` needs a person with `initiative.plan`. A session moves to `active` when its period starts and `completed` when it ends, by rule. |
| Role | `requested → active → ended` | An invite creates an `active` Role. A request to join creates a `requested` one, which needs `member.manage` to activate. |
| TaskDefinition | `draft → active → retired` | A model-authored `draft` becomes `active` only with `ratifiedBy` |
| Report | `owed → in-preparation → submitted → acknowledged`, plus `returned`, `cancelled` | `owed` is created by rule from `recurrence`, or by hand. `returned` sends it back to `in-preparation` with a reason. A submitted report is never edited; a correction is a new submission that references it. |

## Conformance rules (MUST)

1. Every resource carries the common elements above.
2. Every state change produces exactly one `Provenance` record.
3. A record created or edited by a model has `intent: proposal` (Task) or `status: draft` (everything else), and a `Provenance` agent of type `model` with the model's name and version.
4. Only a Person holding an `active` Role with the right permission, or a declared deterministic rule, may move a record out of `draft` or `proposal`. Planning needs `initiative.plan`, asking someone needs `task.assign`, confirming needs `task.confirm`, submitting a Report needs `report.submit`.
5. `Task.verification = confirmed` requires a verifier who is not the performer, except where the TaskDefinition sets `autoConfirm` for that step. Steps involving money or beneficiaries may never auto-confirm.
6. Quantities always have a unit from the BIX unit list (box · pack · sack · kg · L · piece · person · person-hour · PHP), using UCUM codes where one exists.
7. Every `Location` at barangay level or above carries a PSGC code. Free text is allowed, but only alongside the code.
8. Categories come from BIX value sets. Organizations can add local codes in their own namespace, but never redefine shared codes.
9. A record's `sharing` can never be wider than its organization's `SharingPolicy` allows for its category.
10. Offline edits are replayed in `occurredAt` order. A transition that isn't allowed is rejected, never silently merged.
11. The raw message a model read is never stored in a shared record. If it's kept at all, it stays on the device or under `private`.
12. Every `Report` figure is calculated by its declared `rule` from confirmed records, or from submitted Reports of organizations that are `partOf` the reporting one. No person and no model sets a figure's value directly.
13. A figure may count only records the reporting organization is allowed to see under the source organization's `SharingPolicy`.
14. A resource type added by a module declares its CAE kind, or declares that it is a relationship.
15. **A module's data is BIX data.** A module stores everything as BIX resources or `extension[]` elements, never in private tables or formats that other implementations can't read.
16. Every change to an existing resource names the `meta.version` it was based on. A server refuses a change based on an older version. Exclusive Task transitions are decided only by the server.
17. Only a Task's `owner` can move it to `accepted`. Work can be offered to someone; it can't be accepted on their behalf.
18. A Person can export every record that names them, and an Organization every record it owns, as BIX Bundles, at any time and without asking anyone.
19. **Public proposals.** Someone without a Role may propose a `Need`, an `Offer` or a `Person` (such as an applicant) through an organization's public link. It is always `draft` and `private` until a member with the right permission confirms it.

## Everyday scenarios the model must handle

Each scenario below has to be representable with the v0.1 resources, without a special case. All of them are routine.

| Scenario | What happens | Resources and templates involved |
|---|---|---|
| **Weekly feeding program** at a parish | Every Saturday: six volunteers serve, someone buys goods and keeps the receipt, around forty households get a pack. | Recurring `Initiative` with one session per Saturday · recurring `Need` (6 people, 2 sacks of rice) · `session-staffing` and `expense-claim` steps · households recorded as counts |
| **Volunteer can't come, offers something else** | A regular volunteer messages that she can't serve this Saturday but will drop off rice on Friday. | Her `serve` Task is released back to `ready` · a new goods `Offer` · a `receive` step at the parish hall |
| **Tutoring club** at a school | Volunteer tutors cover Tuesday and Thursday sessions. Students doing NSTP log their service hours. | `Role` = `service-learning` · `Offer` of time with `recurrence` · completed `serve` Tasks become service hours |
| **Civic club project cycle** (Rotary, JCI) | A chapter runs a project, tracks member participation, and owes a quarterly report to its national body, which consolidates every chapter's report. | `Organization.partOf` the national body · `Role` = `member` · each chapter's `Report` owed to the national body, figures derived from confirmed Tasks · the national `Report` with `includeParts`, summing the chapters' submitted Reports |
| **Scholarship monitoring** | Sixty scholars. Quarterly grade slips, home visits by volunteer mentors. | Recurring `Need` per scholar group, recorded as counts · `upload` and `visit` steps with evidence · mentor confirmation |
| **Monthly coastal cleanup** | Volunteers sign up, a partner lends sacks and gloves, someone reports the kilos collected to the LGU. | `Offer` from a partner `Organization` · `session-staffing` steps · Task output in `kg` · `report-owed` step |
| **Rotaract or JCI year** | Officers change each year; meetings with attendance; projects co-hosted with a sponsoring club; monthly reports to the district or national body | `Role.period` for terms, so records stay with the club · `meeting-attendance` template · `Initiative.partner[]` · recurring `Report` |
| **Animal shelter** | Daily care shifts, named animals with medical steps, public rescue reports, fosters and adoptions | `session-staffing` · the animal welfare module's `Animal` as `Task.focus` · public proposals (rule 19) with `priority: urgent` · `foster` and `adoption` templates |
| **Disaster response** *(a profile, not the premise)* | An offer of bottled water at the town plaza, available until 3PM, gets matched to an evacuation center. | Same resources. Adds urgent categories and a short `availableUntil`. No new resource types. |

## Worked example: a volunteer can't come, and offers rice instead

A regular volunteer posts in the group chat, in Filipino mixed with English, the way most group chats are written: *"Ate, di ako makakapunta this Saturday pero may 2 sacks of rice ako para sa feeding. Dadalhin ko na lang sa parish hall Friday night."* ("I can't come this Saturday, but I have 2 sacks of rice for the feeding. I'll bring them to the parish hall on Friday evening.")

*Sample data.*

The model proposes two changes in one Bundle. The first is a new Offer and a step for someone to receive the rice:

```json
{
  "resourceType": "Bundle",
  "type": "sync",
  "entry": [
    {
      "fullUrl": "urn:uuid:7b1e…offer",
      "resource": {
        "resourceType": "Offer",
        "id": "7b1e…offer",
        "status": "draft",
        "sharing": "organization",
        "language": "fil",
        "offeredBy": { "reference": "Person/3c9a…volunteer" },
        "category": { "system": "bayanihan:category", "code": "goods.food.rice" },
        "quantity": { "value": 2, "unit": "sack" },
        "location": { "display": "Parish hall", "psgc": "<barangay code>" },
        "availableFrom": "2026-10-30T18:00:00+08:00",
        "matchedTo": { "reference": "Need/1d77…saturday-rice" }
      }
    },
    {
      "fullUrl": "urn:uuid:a41d…task",
      "resource": {
        "resourceType": "Task",
        "id": "a41d…task",
        "intent": "proposal",
        "status": "draft",
        "code": { "system": "bayanihan:step", "code": "receive" },
        "focus": { "reference": "Offer/7b1e…offer" },
        "definition": { "reference": "TaskDefinition/goods-transfer|0.1" },
        "requester": { "reference": "Organization/91f2…parish-ministry" },
        "restriction": { "period": { "start": "2026-10-30T18:00:00+08:00", "end": "2026-10-30T21:00:00+08:00" } },
        "verification": "pending"
      }
    },
    {
      "fullUrl": "urn:uuid:e0c3…prov",
      "resource": {
        "resourceType": "Provenance",
        "id": "e0c3…prov",
        "target": [{ "reference": "Offer/7b1e…offer" }, { "reference": "Task/a41d…task" }],
        "activity": "propose",
        "occurredAt": "2026-10-27T20:14:05+08:00",
        "offline": false,
        "agent": [
          { "type": "model", "model": { "name": "<small model>", "version": "<version>" } },
          { "type": "author", "who": { "reference": "Person/55aa…coordinator" } }
        ]
      }
    }
  ]
}
```

The second change: it proposes releasing her Saturday `serve` Task, so the slot moves back to `ready`.

**What happens next.**

1. The coordinator checks both proposals and confirms them in one tap.
2. Her Saturday slot goes back to `ready` and is posted to the group chat for someone else to claim.
3. The Offer becomes `available`. The receive step becomes `intent: plan` and `status: ready`.
4. On Friday evening, whoever receives the rice completes the step. She confirms the handover, so performer and verifier are different people.
5. The Saturday rice Need moves toward `met`. Her record shows a contribution that week, even though she didn't serve.

The same structure handles the disaster-response profile. In the Catmon example, an offer of 5 boxes of bottled water at the plaza until 3PM, the template is the same `goods-transfer`, with `collect` and `deliver` steps instead of `receive`.

## Teams (committees) and how a group remembers its way of working

> **Priority (2026-10-27).** This is first-hand cultural context: Philippine groups run projects and events through **committees**, each with a **lead**: volunteers, venue, creatives and design, sponsors and partners, finance, and so on. Leads break the work down into tasks for themselves, their members and outside volunteers. A person often sits on several committees. Implement this in BIX, Bayanihan Core and Dasig before generic task features.

**Lessons from FHIR.** `CareTeam` is a team with roles around one plan of care, and a FHIR `Task` may be owned by a team before it is handed to a person. `PlanDefinition` is a reusable plan: its actions, who takes part, and when each action happens relative to the start. BIX takes both.

### New and changed elements

| Element | What it is |
|---|---|
| **`Team`** (new resource, from FHIR CareTeam; CAE kind: Actor, a collective participant) | A committee, called a **team** in the app. `name` in the group's own words, `organization`, `initiative` (set for an event's committee, empty for a standing one), `kind` (standing · initiative), `participant[]` {`person`, `role` (lead · member), `period`}, `status`. A person may be in any number of Teams. |
| **`Task.owner`** may be a Team | Work lands with a committee first; its lead assigns it to a member or opens it up. |
| **`Task.dependsOn[]`** | Tasks that must be `completed` first, across Teams ("print shirts" waits on "confirm sponsor logos"). A Task can't move past `ready` until they are. |
| **`Task.partOf`** (from FHIR) | Decomposition: "Secure the venue" → "Shortlist 3 venues", "Visit", "Get a quote", "Pay the deposit". |
| **`Task.audience`** | How far down the funnel it reaches: `team` · `organization` · `open` (to outside volunteers). Only `open` Tasks appear in shared links and public lists. `goodFirstStep: true` marks work suited to newcomers, as WordPress marks "good first issue". |
| **Co-host participants** | A Team participant may hold their Role in an Organization listed in the Initiative's `partner[]`. They see only that Team's Tasks and the Initiative. |
| **Team-scoped permissions** | A Team lead holds `task.assign` and `task.confirm` for Tasks owned by their Team, without being an officer of the whole Organization. Money and beneficiary steps still need a confirmer who is not the performer. |
| **`InitiativeTemplate`** (new resource, from FHIR PlanDefinition; CAE kind: Instrument) | A group's saved way of running a kind of initiative: its Teams and their usual tasks. **Never shown as a noun in the app**, which says "Save these teams for next time" and "Start from last year's teams". `title` ("Our fun run", "Medical mission"), `organization` (or a federation or a module that publishes it), `team[]` (committee names and their default lead role), `action[]` {`title`, `team`, `taskDefinition`, `audience`, `offset` (e.g. 42 days before the start), `partOf`}, `need[]`, `report[]`, `version`, `status`. |

### What is programmable, and what is not

| Layer | Programmable by the organization | Saved as |
|---|---|---|
| Kinds of work (steps, evidence, who confirms) | Yes | `TaskDefinition` |
| Committees: the standing set, and each event's | Yes: add, rename, remove, set leads | `Team` |
| How a kind of event is usually run: its teams, their usual tasks and timing | Yes | `InitiativeTemplate` |
| Recurring programs and their needs | Yes | `Initiative.recurrence`, `Need` |
| Role names in the group's own words, mapped to BIX permissions | Yes | `Role.code` + `permissions[]` |
| Reports owed, to whom, how often, which figures | Yes | `Report` recurrence and figure codes |
| Sharing defaults | Yes | `SharingPolicy` |
| **Lifecycles, propose-then-commit, provenance, performer ≠ verifier for money and beneficiaries** | **No.** These are BIX's constitution; every group gets the same guarantees. | Core |

### How a group's way of working is remembered

1. **It lives in the group's own records**, as `Team`, `InitiativeTemplate` and `TaskDefinition` resources owned by the Organization. It exports with everything else (rule 18), and survives officer handover.
2. **Learned from use, not set up in advance.** After an event, the app offers: "Save these teams for next time?" The next event starts from them. Groups with five teams and groups with fifteen just have their own saved teams.
3. **Changing one event never silently changes the saved teams.** Saving back is a choice, recorded with Provenance, and templates are versioned.
4. **Saved teams travel.** A national body or district can publish a set of teams its chapters adopt; a module can ship them for a sector. An adopted set is copied and then belongs to the group.
5. **Starting points, not rules.** Dasig ships a few sets of teams (club project, event, recurring program) so a new group isn't facing a blank page.

## Working together on a project (lessons from GitHub Projects)

From a study of project tools and a large volunteer-run event. GitHub Projects showed what helps (history, previews, mentions, drafts, views) and what makes it bureaucratic (accounts to take part, many fields, triage on one person). BIX takes the first and leaves out the second.

| Element | What it is | Lesson |
|---|---|---|
| **`identifier[]`** on every resource | A short reference people can say and type, scoped to the group: `LU-24`. Allocated by the server. | FHIR `identifier`; GitHub `#8` |
| **`Communication`** (new resource, from FHIR; *a relationship, not a CAE kind*) | A comment or message about anything: `about` (any resource), `sender`, `recipient[]` (people @mentioned), `payload` {`text`, `attachment[]`}, `sent`. Shared no wider than what it's about. `Task.note[]` stays for short notes and thanks. | FHIR `Communication` |
| **`ShareLink`** (new resource; *an Instrument*) | A link that grants access: `target`, `grants[]` (`view` · `claim` · `join-team` · `propose` · `comment`), `audience` (`anyone-with-link` · `signed-in` · `members`), `preview` (`full` · `title-only` · `generic`), `expires`, `createdBy`, `status` (`active` · `revoked`). The token is never stored in the record. A link can't grant more than its creator has, nor more than the target's `sharing` allows. | Capability links; FHIR R5 `Permission` |
| **`Task.suggestedFor[]`** | People anyone has suggested for a Task. A suggestion is a proposal; asking (`requested`) still needs `task.assign`. | Propose-then-commit |
| **`Task.milestone`** and **`Task.owner`** = an outside Organization | A gate many Tasks `dependsOn`, possibly owned by an outside body ("Central approves the venue"). Shown once, not on every blocked Task. | FHIR `Task.owner`; GitHub milestones |
| **`Task.reviewer`** | A Team or Person whose approval is the `verification`, across Teams. Approval or "changes requested" is recorded as an attestation. | GlotPress; CEP attestations; review before merge |
| **`Team.access`** | `own-tasks` (default) · `initiative`: read everything in the Initiative, as a Communications team needs | FHIR `CareTeam` |
| **`Task.checklist[]`** | Small steps without owners: {`text`, `done`, `doneBy`} | Trello and GitHub task lists |
| **`Task.category[]`** | Optional tags in the group's namespace | GitHub labels |
| **Credit by kind** | A person's record counts work they **performed, reviewed, verified, proposed** and **commented on**, each separately | WordPress props credit reviewers and reporters |

**Left out on purpose:** size, estimate and iteration fields; required fields beyond a title; custom field builders. They are what made project boards feel like paperwork.

## Concurrency and conflicts

Many people act on the same open work, sometimes offline. BIX follows the patterns WordPress contribution and FHIR already use:

| Pattern | Where it comes from | In BIX |
|---|---|---|
| **Exclusive changes go through the server, first come first served** | FHIR versioned updates: a change carries the version it was based on (`If-Match` on `meta.version`) and is refused if the record changed since | Claiming, asking, accepting, releasing, cancelling and confirming a Task. The server applies the first valid change and refuses the others with the current state. |
| **Many proposals, one approval** | GlotPress: several suggestions for one string wait side by side until a validator approves one | Model proposals, public proposals and competing matches stay `draft` together. Confirming one closes the others as superseded, with Provenance. |
| **Show who's working on it** | WordPress post locking: "Ana is currently editing", expiring if they go quiet, with an option to take over | Editing a plan or a report narrative. App-level presence, not part of BIX. Saves still use the version check. |
| **Additions never conflict** | Comments and translations accumulate | `note[]`, `output[]` and attachments are append-only, so two people adding at once both succeed. |
| **Calculated values can't conflict** | | Report figures, `partially-met`/`met`, hours and credit are derived, never edited. |

**Offline.** A change made offline is a request until the server accepts it. The app shows it as pending ("We'll confirm your spot when you're back online"). On replay (rule 10), a change whose base version is stale is refused, never merged, and shown to the person with the current state.

**Fewer collisions by design.** Slots for the same session are interchangeable, so "I'm in" claims *any* open slot of that session, not a particular one. When none are left, the person can offer to be a backup, recorded as an `Offer` of time matched to the session's `Need`, so a released slot can go to them first.

## Open work and credit

BIX is built for contribution the way WordPress contribution works: teams keep lists of open work, and contributors pick up what fits them. Here, an open `Task` is the unit of work, and volunteers matter as much as coordinators.

- **Open work is visible, within sharing rules.** A Person sees `ready` Tasks from every organization they hold a `Role` in, and from any organization that shares them at `network` or `public`.
- **Claim or be asked.** Anyone with a suitable Role can claim open work. A coordinator can offer work to a specific person, who accepts or declines (conformance rule 17).
- **Credit, derived.** A Person's contribution record is the set of confirmed Tasks they performed or verified, and Offers they fulfilled, calculated like Report figures and never typed in. It belongs to the Person and leaves with them (rule 18). This is BIX's equivalent of WordPress "props".

## Interoperability (lessons from FHIR)

FHIR's data model alone didn't make health data move. What did was a standard API, global addresses for records, servers that declare what they support, country-level implementation guides, public conformance tests, and people's right to get their own data. BIX takes all of them. Without them, every installation would share BIX's shapes and still keep its data to itself.

| Lesson | In BIX | v0.1 |
|---|---|---|
| A standard API | Every BIX server answers the same way: `GET /{type}/{id}`, search with `GET /{type}?param=value`, history with `GET /{type}/{id}/_history`, and `POST /` with a `transaction` Bundle | Required |
| Global addresses | A record's canonical address is the server's base URL + `/{type}/{id}`. References may point at another server's address. | Required |
| Servers declare what they support | `GET /metadata` returns the BIX version, resource types, profiles and modules the server supports | Required |
| Export | `GET /Person/{id}/$export` and `GET /Organization/{id}/$export` return Bundles (rule 18) | Required |
| Implementation guides | Modules and profiles (see "Contribution, governance and modules") | Mechanism defined |
| Conformance tests | Published test cases any implementation can run | Before other implementations exist |
| Identity matching is hard | A Person record created by a coordinator can be claimed by that person when they sign in. Merging two Person records is a confirmed, provenance-recorded action, never automatic. | Required |

How a person signs in is up to each implementation. BIX records refer to Persons; accounts are not part of the language.

## Integrity and portability (lessons from blockchain, without one)

BIX takes the cryptography that blockchains popularized and leaves out the chain. A public blockchain can't delete data, which conflicts with the Data Privacy Act's right to erasure. It also spends energy and compute on consensus between strangers, which civic groups with coordinators and relationships don't need.

| Technique | In BIX | When |
|---|---|---|
| Hash-chained revisions | `meta.previousHash`, over the RFC 8785 canonical form | Designed; built after the pilot |
| Signed confirmations | The device of the person who confirms a step signs the confirmation, so anyone can check who confirmed it without trusting the server | Designed; built after the pilot |
| Public anchoring | Periodically publish one combined fingerprint (a Merkle root) of confirmed records, so later tampering can be proven. Maps to CEP's `anchorUri`. Never publishes the records themselves. | Designed; built after the pilot |
| Verifiable credentials | A Person's contribution record can be issued as W3C Verifiable Credentials they hold and anyone can verify | Designed; built after the pilot |
| Portable personal records | A Person's records can move between BIX servers with them, as Bluesky's AT Protocol does for posts | Export now (rule 18); moving between servers later |

Personal data is never anchored, signed into anything public, or made impossible to delete.

## Relationship to Civic Interconnect and CEP

Reviewed 2026-10-24 from the public site, and again on 2026-10-26 from the source repository ([civic-interconnect/civic-interconnect](https://github.com/civic-interconnect/civic-interconnect), v0.0.7, 2026-10-23), which is ten months ahead of the site. Full study: the Bayanihan workspace's research notes.

**What Civic Interconnect is.** A layered framework, with dependencies flowing upward only:

- **CAE**, Civic Accountable Entities: six kinds of civic thing (Actor, Site, Instrument, Event, Jurisdiction, Observable). Roles come from relationships.
- **CEP**, the Civic Exchange Protocol: Entity, Relationship and Exchange records in a shared envelope with revision hashes and attestations.
- **CEE**, Contextual Evidence and Explanations: observations and explanations over CEP records, with models treated as instruments, not authorities.

**Where BIX fits.** CEP leaves "user interfaces or workflows" out of scope, and CEE says outcomes "belong to governance, policy, or operational layers outside CEE." BIX is such an operational layer. CAE's Events are things that have occurred; nothing in the framework represents planned work, needs, offers, claimable steps, model proposals versus human commits, sharing defaults or offline records. BIX does, and hands confirmed work to CEP.

**What BIX takes:**

1. CAE's six kinds as BIX's top-level classification (design principle 10, "CAE kinds" above).
2. Observations as derived, reproducible values, as the model for `Report` figures (principle 11).
3. Hash-chained revisions (`meta.previousHash`).
4. Attestation fields aligned with W3C Verifiable Credentials.
5. CEP's vocabulary rules: stable term URIs, deprecated terms never reused, SKOS-style mappings (`exactMatch`, `broadMatch`, `narrowMatch`, `relatedMatch`).
6. CEP's context-tag field names for model proposals (`appliedBy`, `confidence`, `sourceRunId`), so a proposal exports without renaming.

**How BIX exports to CEP.** Through an adapter written to CEP's Adapter Architecture specification:

| Confirmed BIX work | CEP record |
|---|---|
| `Organization` | Entity |
| `Role` | Relationship (membership) |
| Goods received or delivered | Exchange, value type `in-kind` |
| Service performed | Exchange, value type `service-hours` |
| Money a volunteer spent for the group (a later module) | Exchange, value type `monetary` |
| Performer and verifier in `Provenance` | Envelope attestations |
| `Report` figures | CEE observations referencing the Exchanges they summarize |

Only completed, confirmed work exports, as `exchangeStatus: COMPLETED`. Timestamps convert to CEP's UTC format on export.

**What BIX does not take, and why:**

- **CEP's identity rules for people.** A CEP Entity requires a legal name, and its open identifier (SNFEI) is a hash of name and address, which anyone who knows a person could recompute. BIX uses random IDs for people and exports a Person only with consent, otherwise as a pseudonymous ID or as counts. SNFEI may be used for registered organizations.
- **US federal category codes** (CFDA, NAICS, GTAS). BIX exports its own `bayanihan:` codes through CEP's local category fields.
- **CEP's record status** (`ACTIVE`, `PENDING`…) as a substitute for work lifecycles. BIX lifecycles are unchanged.
- **"Disagreement is preserved"** as the default for current state. BIX needs one current state per record to coordinate work; disputes are a state (`verification: disputed`) with their history in Provenance.

**Open questions.** BIX decides these itself from CEP's published documents and code; nothing waits on CEP's maintainer (decided 2026-10-26). Contact is welcome but optional.

- Are `Need` and `Offer` best treated as CAE Instruments? Provisionally yes (see "CAE kinds").
- BIX's propose-then-commit rules could fill CEP's `CEP-AI-Constrained` profile, which is listed without content. An offer we may make, not a dependency.
- Canonical encoding: decided 2026-10-27. RFC 8785 for BIX's hashes and signatures; CEC only inside the CEP export adapter.

**Caveats:**

- CEP is at version 0.0.x with one maintainer. Its governance documents describe a standards board that has not yet formed. Describe it as an early-stage, single-maintainer framework.
- Its prose and schemas disagree in places (what an Exchange is; what "CTag" stands for). Cite the schemas.

## Contribution, governance and modules

**Today.** BIX is a draft maintained by Dasig, shaped by the organizations taking part in co-design. Changes that came from conversations are recorded in the change log, citing how many groups they came from. Groups that shape it are credited as contributors, with their permission. Nothing more formal exists yet, and this section says only what exists.

**Direction.** BIX is open to contribution, and is to be governed together with credible organizations as they join. How decisions are shared is itself something to design with them, not in advance.

**Modules.** Organizations and developers can extend BIX without changing its core, the way WordPress plugins extend WordPress. A module can add:

| What | How | Rule |
|---|---|---|
| Kinds of work | `TaskDefinition`s for a sector or program, e.g. scholarship monitoring | Uses core resources only |
| Vocabulary | Categories, role codes, report figures, in the module's own namespace | Never redefines a shared code |
| Fields | `extension[]` elements on core resources | Never redefines a core element |
| Resource types | A new type, such as `Expense` | Declares its CAE kind (conformance rule 14) |
| Profiles | Constraints for a context, e.g. disaster response | Narrows the core; adds nothing it would reject |
| Integrations | Adapters that publish to or read from another system | Respects `sharing` and `SharingPolicy` |

**First module: animal welfare** (`bayanihan-animal`), deferred until after v0 (decided 2026-10-27: these groups deserve dedicated design time). Sketched in `docs/architecture/SCENARIO_WALKS.md` §7: an `Animal` resource, `intake`, `vet-care`, `foster` and `adoption` templates, and figure codes such as `animals-rescued` and `animals-adopted`. It doubles as the worked example of how modules extend BIX.

**Integrations.** Dasig Fundraising (dasig.org) is one of the first: confirmed outcomes can be published to a public campaign page. A CEP adapter is another. Neither is part of the core, and the core depends on neither.

## Out of scope for v0.1

A module registry, a terminology server, conformance tests, formal governance, signatures and public anchoring (designed above), and mappings to 3W/HDX HAPI, IATI, Open Badges 3.0 / W3C Verifiable Credentials, Open Referral HSDS and CEP. All of these are on the roadmap. v0.1 only has to be implementable and not block any of them.

**Candidates for v0.2, if conversations show they matter:**

- **Expense:** money spent by a volunteer on the group's behalf. It could be exported to CEP as a monetary Exchange.
- **Field report:** an observation such as a blocked road.
- **Credential:** a certificate, mapped to Open Badges.

## What the conversations should settle

These are for us, answered over time from the stories organizations tell. We don't ask them directly, and none of them belong in a first conversation.

1. Which role codes match how groups actually describe their people?
2. Which steps should auto-confirm, and which always need a second person?
3. What's the smallest place description volunteers actually use?
4. Which categories of need and offer come up in a normal month, not just in a crisis?
5. What's the default sharing level groups are comfortable with?
6. Which reports do groups owe, to whom, and how often?
7. How do groups handle money a volunteer spends on the group's behalf?

## Related work

HL7 FHIR R4 (Task, Provenance, Consent, ActivityDefinition, the RESTful API, CapabilityStatement, Bulk Data `$export`), RFC 8785 JSON Canonicalization Scheme, W3C Verifiable Credentials, Certificate Transparency (RFC 9162) for public anchoring, the AT Protocol for portable personal repositories, WordPress contribution teams and props, Civic Interconnect's CAE, CEP and CEE (see the section above), W3C PROV, Schema.org (`Offer`, `Demand`), Open Referral HSDS 3.x, HDX HAPI and OCHA 3W, IATI, PSA's PSGC, and Open Badges 3.0 / W3C Verifiable Credentials.

## Change log

| Date | Change |
|---|---|
| 2026-10-24 | First working draft: conversation guide, 12 resources, lifecycles, 11 conformance rules |
| 2026-10-24 | Scope set to everyday operations, with disaster response as one profile. Added design principle 9, the everyday scenarios table, and the feeding-program worked example (replacing Catmon as the main example). Widened Need and Offer to cover people, time, skills and venues, with recurrence. Added `civic-club` and `cooperative` organization kinds and the `member` role. Added the CEP relationship section and `meta.previousHash`. Added Schema.org mappings and v0.2 candidates. |
| 2026-10-24 | Part A rewritten around the first conversation: relationship-led and personalized, about the group's story and advocacy, ending in an invitation. The earlier questions moved to A3 as follow-ups for later conversations. Making sense of what groups share is stated as our responsibility. |
| 2026-10-25 | Renamed from Civic Information Exchange (CIX) to Bayanihan Information Exchange (BIX), to follow the naming rule that open things carry the Bayanihan name. Namespaces changed from `cix:` to `bayanihan:`. |
| 2026-10-26 | Worked example rewritten in Filipino mixed with English, replacing the Cebuano draft. Language codes now `fil` and `en`. Interface language for implementations is English. |
| 2026-10-26 | Grounded in Civic Interconnect after a study of its source repository. Lineage now names CAE next to FHIR, and states what BIX adds. Added design principles 10 (every resource type has a CAE kind) and 11 (reports are derived), the "CAE kinds" table, and conformance rules 12–14. Brought a thin `Report` into v0.1 from the v0.2 candidates: an obligation with a due date and recipient, figures derived by rule, and roll-up for federated organizations through `partOf`. Rewrote the CEP section: the framework's layers, the export mapping, what BIX does not adopt (CEP's identity rules for people, US federal codes) and open questions. Added the section on contribution, governance and modules. |
| 2026-10-27 | Took FHIR's interoperability lessons, not just its data model: a standard API, global record addresses, `/metadata`, Person and Organization export, and careful Person claiming and merging. Took blockchain's cryptographic techniques without a blockchain: hash chains, signed confirmations, public anchoring, verifiable credentials and portable records, all designed now and built after the pilot. Decided RFC 8785 for canonical encoding. Added the "Open work and credit" section (claiming versus being asked, credit derived like report figures) and conformance rules 15–17, including "a module's data is BIX data" so modules can't recreate silos. |
| 2026-10-27 | Applied the fixes from the scenario walks (`docs/architecture/SCENARIO_WALKS.md`): Initiative `kind`, `status`, `target[]`, `taskDefinition[]` and lifecycle; Role `status`, `qualification[]` and lifecycle; Task `executionPeriod`, `requires[]` codes, `output[]` with attachments, and FHIR's meaning of `requested` for asking a named person; Person `managedBy` until claimed; new Provenance activities; Data types (including `Attachment`) and Value sets sections (permissions, requirements, figure rules, report figures); Report `rule` as a coded rule, `missingParts[]`, `replaces`, `submittedBy`. Proof defined as Task output plus attachments. |
| 2026-10-27 | Walked the likely pilot audiences: Rotaract/Interact, JCI and animal welfare. Added `Initiative.partner[]`, `Task.note[]` (thanks), `priority` on Need and Task, `Task.focus` widened to any resource, conformance rule 18 (public proposals are drafts until a member confirms), two scenario rows, and the first module, animal welfare, with an `Animal` resource. |
| 2026-10-27 | Added "Concurrency and conflicts": server-decided exclusive changes with FHIR-style version checks, GlotPress-style proposals side by side, append-only notes and outputs, offline changes as pending requests, "I'm in" claims any open slot, backups as Offers of time. New rule 16 (version checks); rules 16–18 renumbered to 17–19. `Person.name` may be a nickname alone. Animal welfare module deferred until after v0. |
| 2026-10-27 | Media fields for what the screens show: `Person.photo` (set only by the person), `Organization.image`, `Initiative.image`, `Report.attachment[]`. Rule: a photo is shared no more widely than its record, and public previews never use Task photos. |

| 2026-10-27 | Committees as a priority: new `Team` (from FHIR CareTeam) and `InitiativeTemplate` (from FHIR PlanDefinition) resources; `Task.owner` may be a Team; `Task.partOf`; `Task.audience` with `goodFirstStep`; team-scoped permissions; the list of what organizations can program and what is fixed; how a group's way of working is remembered and reused. |
| 2026-10-27 | Renamed `Kit` to `InitiativeTemplate`, never shown as a noun in the app. The app calls committees **teams** and speaks of saving and reusing teams. |
| 2026-10-27 | From the fun-run walk: `Task.dependsOn[]` across Teams, and Team participants from a co-host Organization. |
| 2026-10-27 | Working together on a project: `identifier[]` short references, `Communication` (comments and @mentions), `ShareLink` (configurable access through links), `Task.suggestedFor[]`, milestones and outside owners, `Task.reviewer` across Teams, `Team.access`, `Task.checklist[]`, `Task.category[]`, credit by kind. CAE kinds added for Team, InitiativeTemplate, ShareLink, Communication. |
