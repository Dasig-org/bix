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
| `Attachment` | `contentType`, `url`, `hash` (SHA-256), `size`, `title`, `capturedAt`, `showsMinors` | As FHIR. Photos, receipts and attendance sheets. The file lives in the implementation's storage; the record holds its address and fingerprint. |

**Media.** Images are Attachments on `Person.photo`, `Organization.image`, `Initiative.image`, `Task.output[].attachment[]` and `Report.attachment[]`. A photo is shared no more widely than the record that holds it. Link previews and public pages may show only an `Initiative.image` or `Organization.image` whose record is `public`, never a Task's photos, because those often show beneficiaries, including children.

**Proof** is not a separate resource. It is a Task's `output[]` and attachments, confirmed by a verifier who is not the performer.

## Value sets

| Value set | Codes in v0.1 |
|---|---|
| `bayanihan:permission` | `org.manage` · `member.manage` · `initiative.plan` · `task.assign` · `task.confirm` · `report.submit` · `view.organization` (see all of the group's work; see "Seeing other committees' work") |
| Default permissions by role | officer: all seven · core-member: `initiative.plan`, `task.assign`, `task.confirm`, `view.organization` · member, volunteer-regular, volunteer-episodic, service-learning: none beyond claiming open work · partner-representative, donor: none |
| `bayanihan:requirement` | `can-drive` · `has-vehicle` · `adult` · `first-aid` · `can-tutor` (organizations add local codes in their own namespace) |
| `bayanihan:figure-rule` | `sum-task-hours` counts as in "Planned and given time" · `count-tasks` {`taskCode`} · `count-participants` {`taskCode`, `attended`} (distinct people active on done work; with `attended`, only those checked in) · `sum-task-hours` {`taskCode`} · `sum-task-output` {`outputCode`} · `sum-received` {`needCategory`} · `sum-part-reports` {`figureCode`} |
| `bayanihan:report-figure` | `sessions-held` · `volunteer-hours` · `volunteers-active` · `households-served` · `learners-served` · `goods-received` · `waste-collected` · `people-served` (a count recorded as a Task output, never names) |
| `bayanihan:assist-area` | `break-down` (smaller steps for a project, task or step) · `review-plan` (what a plan needs a second look at) · `who-to-ask` (people who could take a step, with the reason) · `newcomers` (good first steps) · `roster` (who's active, new, free, or not yet asked) · `slipping` (unclaimed steps, dates coming up, empty teams) · `report-draft` (a narrative draft; figures stay derived) · `memory` (compare a project with the group's Practices: match steps, filter usual steps, suggest lessons; see "Project memory: Practices"). Modules may add codes in their own namespace. |
| `bayanihan:practice-source` | `own` (learned from the group's projects) · `starter` (published by Dasig, a federation or a module) · `adopted` (a copy of a starter or shared Practice, now the group's own) |

Any confirmed Task counts toward a figure only if its `executionPeriod` lies inside the Report's `period`.

## Resources in v0.1

| Resource | Closest FHIR resource | Purpose | Key elements |
|---|---|---|---|
| `Person` | Person / Practitioner | One human, one record across organizations | `name` {`text`, `use`: nickname · full} (a nickname alone is enough), `photo` (Attachment, optional, set only by the person), `contact` (optional), `managedBy` (the Organization that created the record until the person claims it, then the person) |
| `Organization` | Organization | Any group, registered or informal | `name`, `image` (Attachment: logo or group photo), `kind` (registered-npo · faith-based · civic-club · community · event-team · sk-council · school-org · cooperative · informal · lgu-unit…), `partOf` (e.g. a chapter's national body, a ministry's parish), `registration[]`, `assist[]` (areas where the group turned on assistance; see "Proposed edits and assistance") |
| `Role` | PractitionerRole | A Person's relationship to an Organization | `person`, `organization`, `code` (officer · member · core-member · volunteer-regular · volunteer-episodic · service-learning · partner-representative · donor), `status` (requested · active · ended), `period`, `permissions[]` (codes from `bayanihan:permission`; defaults come from `code`), `qualification[]` (codes from `bayanihan:requirement`, e.g. `can-drive`) |
| `Location` | Location | A place | `name`, `description` (the landmark text), `psgc` (barangay level or above), `position` (optional lat/lon), `partOf` |
| `Initiative` | PlanDefinition / CarePlan | Any organized effort. Can be nested: a year's plan holds programs and projects; a recurring program holds one session per occurrence. | `title`, `kind` (plan · program · project · session), `image` (Attachment: the cover; sessions use their program's unless they set one), `status`, `organization`, `partOf`, `period`, `recurrence`, `category[]`, `location[]`, `target[]` {`code`, `value`, `unit`} (same codes as Report figures), `taskDefinition[]`, `partner[]` (co-hosting Organizations; display and credit only in v0.1), `note[]` {`author`, `time`, `text`} (updates on the project, newest last, as on a Task) |
| `Need` | SupplyRequest (generalized) · Schema.org `Demand` | What an initiative is short of: people, goods, money, skills, transport or a venue. Can recur with the initiative. | `initiative`, `category`, `quantity` {value, unit}, `received`, `neededBy`, `recurrence`, `location`, `priority` (routine · urgent), `status` |
| `Offer` | *No FHIR equivalent* · Schema.org `Offer` | What someone has and will give: goods, time, a skill, a vehicle, a venue | `offeredBy` (a Person or an Organization), `category`, `quantity`, `location`, `availableFrom`, `availableUntil`, `recurrence`, `matchedTo` (a Need), `status` |
| `TaskDefinition` | ActivityDefinition | The reusable template for a kind of work. Examples: `session-staffing` (serve, check in, close), `goods-transfer` (collect, deliver, confirm receipt), `expense-claim` (buy, file receipt, approve), `report-owed` (gather, draft, submit). | `appliesTo` (Initiative, Offer or Need categories), `steps[]` {`code`, `dependsOn`, `requires[]`, `evidence`, `confirmerRole`, `autoConfirm`}, `status`, `author`, `ratifiedBy` |
| `Task` | Task | One claimable step | `intent` (proposal · plan · order), `status`, `code`, `focus` (any resource: an Offer, a Need, or a module's type such as an Animal), `practice` (the kind of step it is; see "Project memory: Practices"), `priority` (routine · urgent), `definition`, `requester` (an Organization), `owner` (the Person who claimed it or was asked), `restriction` {`period`, `location`}, `requires[]` (codes from `bayanihan:requirement`), `executionPeriod` {`start`, `end`} (when the work actually happened), `output[]` {`code`, `value`, `unit`, `attachment[]`}, `note[]` {`author`, `time`, `text`} (including thanks), `verification` |
| `Provenance` | Provenance | Who did what, and who confirmed it | `target[]`, `activity` (propose · create · update · claim · assign · accept · decline · release · complete · reopen · confirm · invite · dispute · cancel · submit · return · acknowledge · claim-identity · merge), `agent[]` {`type`: author · performer · verifier · model, `who`, `onBehalfOf`}, `occurredAt` (client time), `recorded`, `offline`, `via` {`kind`: direct · hub · replayed, `endpoint`}, `model` {name, version} |
| `SharingPolicy` | Consent | One organization's default sharing rules per category | `organization`, `rules[]` {`category`, `sharing`}, `approvedBy` |
| `Report` | MeasureReport (loosely) | A report one organization owes another (a chapter to its national body, a ministry to its parish, a group to its LGU or a donor), with figures derived from confirmed records | `owedBy` (Organization), `owedTo` (Organization), `period`, `due`, `recurrence`, `scope` {`initiative[]`, `includeParts`}, `figures[]` {`code`, `value`, `unit`, `rule` {`code`, `params`}, `derivedFrom[]`, `derivedAt`}, `missingParts[]`, `narrative`, `attachment[]` (photos and documents chosen from the confirmed Tasks' outputs), `replaces`, `submittedBy`, `status` |
| `Practice` | *No FHIR equivalent* (its figures follow FHIR Observation: measured values kept apart from what they measure) | One kind of step as this group does it, and how it has gone across its finished projects: the group's project memory | `title`, `organization`, `appliesTo[]`, `team`, `partOf`, `after[]`, `source`, `lesson[]`, `observed` (calculated by rule), `status` |
| `ChangeProposal` | *No FHIR equivalent* (closest: a FHIR Task with `intent: proposal` whose `focus` is the record) | A proposed edit to a record that already exists, waiting for someone allowed to make it | `target`, `basedOn` (the target's `meta.version`), `organization`, `change[]` {`op`: add · remove · replace, `path`, `value`}, `includes[]` (draft records accepted together with it), `area`, `reason`, `status` |
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

## Content every page has

Anything people open as a page carries the same content elements, so people always know what it's about and what to look at. **Page resources:** `Organization`, `Team`, `Initiative`, `Task`, `Need`, `Offer`, `Decision`, `Report`, `Position`.

| Element | What it is |
|---|---|
| `description` | Plain text, a few lines. Links and @mentions allowed. |
| `attachment[]` | **Reference material**: what to read or look at (a brief, last year's call, a deck, a moodboard). Stored by the group's own server, or an outside link labelled as such. |
| `note[]` {`author`, `time`, `text`} | **Updates**: a few words on how it's going, left on the record itself, with who wrote each and when. On `Task`, `Initiative` and `Team` (2026-11-16). Oldest first, append-only. See "Updates on a record" below. |
| *Outputs stay separate* | On a Task, `output[].attachment[]` is **what the work produced**. A page shows "Files" (reference) and "What came out of it" (outputs) as two groups. |
| `Decision.option[].attachment[]` | Each option may carry several files (the concept, its PDF, mockups), and the `Decision` itself has `description` and `attachment[]` for the context of the vote. |

Comments (`Communication`) and History (Provenance) attach to any page already.

### Updates on a record (`note[]`)

A group's words about its work should stay with the work, not in a chat somewhere else. `Task`, `Initiative` and `Team`
each carry `note[]`: short updates such as "Permit approved, route cleared from 5 to 8 AM" or "Supplier can only
deliver Friday".

| | |
|---|---|
| **Shape** | `author` (a Person), `time`, `text` (plain text; required). The same on all three, and the same as FHIR's `Annotation`, which FHIR puts on `Task`, `CarePlan` and `CareTeam`. |
| **Who may add one** | Whoever may edit that record under the group's rules: on a Task, the people on it and its leads; on a Team, its active participants and its lead; on an Initiative, its leads and the group's core team. No new permission. |
| **Who sees it** | Whoever can see the record. A note is part of it, so it follows the record's `sharing` and never appears in a public summary. |
| **Order and conflicts** | Oldest first. Append-only, like `output[]` and attachments ("Concurrency and conflicts"): two people adding at once both succeed. A correction is a new note. |
| **History** | Adding a note is a new version of the record, so Provenance says who added it and when, like any change. |
| **In an export** | Notes travel inside the record, in a group's export and in a person's own. |

**`note[]` or `Communication`?** A note is an update *on* a record, read by whoever opens it. A `Communication` is a
message *to* people *about* a record: it has a sender and recipients (@mentions), can carry attachments, and can be
answered. Use `note[]` for "how it's going"; use `Communication` for a conversation or a notice. An app may show both
on the same page.

**For apps.** Show a record's notes with their author and time, newest first, and let people who may edit the record
add one. Don't put anything a rule depends on in a note: figures, confirmations and attendance have their own elements.
Photos and files go in `attachment[]` (and, on a Task, what the work produced in `output[].attachment[]`), not in notes.

**Servers on an earlier v0.1.** Resources refuse elements they don't know, so a server that hasn't taken this addition
refuses an Initiative or Team that carries `note[]`. A client should say the update didn't save and keep the text, not
drop it. `GET /metadata` says which version a server speaks.

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
| `Position` | Instrument | From Popolo Post |
| `Group` | Observable | From FHIR Group: who is served, as counts |
| `Goal` | Instrument | From FHIR Goal: a shared target |
| `Consent` | Instrument | From FHIR Consent |
| `Endpoint` | *Transport, not a kind* | From FHIR Endpoint |
| `Follow` | *Relationship, not a kind* | |
| `Decision` | Instrument while open, Event once decided | From Popolo Motion and VoteEvent |
| `ChangeProposal` | Instrument | A request to change a record; the change itself is recorded by Provenance |
| `Practice` | Instrument | How a group does one kind of step; its `observed` figures are derived, like a Report's |
| `Vote` | Event | From Popolo Vote |
| `Bundle` | *Transport, not a kind* | Like CEP's record envelope |

### Usernames and invitations (decided 2026-11-13)

People can be invited to a group, team, project or task by username or by email, besides by link.

| Element | Meaning |
|---|---|
| **`Person.handle`** | `{value, findable}`. Optional. 3–20 characters: lowercase ASCII letters, digits, `.` and `_`; starts with a letter; no leading, trailing or repeated `.`; compared without case. Unique on the server that holds the Person (a network rule, like references); a self-hosted network has its own. A person on one phone or a hub has none until they're on a server. `findable: false` turns off invites by username. Servers also refuse handles that are all digits, emails, phone numbers or reserved words, allow a change at most every 30 days, and hold a released handle for 30 days for its previous owner. |
| **`Invitation`** | One invitation to one person: `target` (Organization, Team, Initiative or Task), `invitedBy`, `invitee` (the Person, when known), `role` (what accepting gives: `volunteer` or `member` of a group, `team-member`, `helper` on a task), `status`, `expires`, `message` (280 characters), `via` (`username` · `email` · `in-app`), `blockFuture` (set by the invitee on declining: no more invitations from that group). |
| **`Task.taking`** | `anyone` (default): anyone the Task is shared with may say "I'm in". `ask`: they ask, by adding themselves to `participant[]` as `requested`, and someone with `task.assign` (or the team's lead) chooses. |
| **`Organization.invitePolicy`** | Who may invite by username or email: `core-team` (default) or `members` (everyone in the group). Links keep their own rules. |

**Privacy rules (MUST):**

1. **An email address is never part of a BIX record.** A server keeps the address an invitation went to only as a salted hash, to deliver it when that address later signs in; it never appears in a record, an export or a response.
2. **Inviting by email reveals nothing**: the inviter gets the same answer, in the same time, whether or not the address belongs to anyone.
3. **A handle is found only by exact match**, never by browsing or partial search, and the lookup returns only the nickname and photo, never groups, teams or work.
4. **Invitation emails and notifications carry no detail** beyond the group's name and who invited; the rest shows after signing in.
5. **Every invitation can be declined, and blocked for the future**; servers limit invitations per inviter and per invitee.
6. **An Invitation is not a ShareLink.** A ShareLink is used by whoever holds it; an Invitation is addressed to one person and only they can accept it.

### Suggestions and their answers (decided 2026-11-14)

A suggestion (from Bayani or from a rule, for the `memory` area) worked out on a device is **not a record** until a
person answers it. Then:

| Answer | What is committed |
|---|---|
| **Accept** | The change itself, with Provenance agents: the person (`author`) and what suggested it: `model` (`name`, `version`, `question`, `confidence`, `onBehalfOf` the person) or `rule` (its name). Edited first: `model.edited: true` |
| **Not this time** | A `ChangeProposal` in `declined`, area `memory`, target the project or step, with `includes` (the record it would have added) or `change` (the edit it would have made), and the same Provenance agents |

- **Not again:** a suggestion matching a declined ChangeProposal for the same target, area and Practice is not shown again for that target.
- **Questions** (`model.question`): `applies` (does this usual step belong in this project), `same-practice` (is this
  step already in the plan under another name), `which-practice` (which usual step is this), `which-team`, `one-off`,
  `general-title` (a general name to keep a step for next time), `step-ideas` (a step the model thought of itself, for
  this project, with no usual step behind it; added 2026-11-21); and, for rules, `usually-needed`, `done-by-now`,
  `out-of-order`. A `step-ideas` suggestion has no `confidence`: it is an idea for a person to judge, not an answer.
- **Thresholds** (how confident an answer must be to show) are the app's, not BIX's.
- **The measure** (accepted unchanged, edited, declined, per question) is read from these records; nothing else is collected.
- **Starter Practices** (`source: starter`) are published by a network as read-only records without figures; a group using one adopts it (`source: adopted`, `adoptedFrom`).

## Lifecycles

| Resource | States | Notes |
|---|---|---|
| Need | `draft → open → partially-met → met`, plus `cancelled` | `partially-met` and `met` are calculated from `received` vs `quantity`. A recurring Need opens again with each session of its Initiative. |
| Offer | `draft → available → matched → fulfilled`, plus `expired`, `withdrawn` | `expired` is set by rule when `availableUntil` passes |
| Task | `draft → ready → accepted → in-progress → completed`, plus `requested`, `cancelled`, `failed`, `on-hold` | **Reopening** (2026-11-12): `completed`, `failed` or `cancelled` → `ready` (or `in-progress` when people stay on it), and needs `task.assign`. The earlier completion, its signature and any proof stay in the history and still verify as that version; hours and credit count only while the Task is `completed`, so a reopened Task stops counting until it is done again, and is signed again then. Follows FHIR's meaning of `requested`. **`ready`:** open, no owner, anyone eligible may claim. **Claiming** sets `owner` to oneself: `ready → accepted`. **Asking** a named person: `ready → requested` with `owner` set. They **accept** (`requested → accepted`) or **decline** (`requested → ready`, `owner` cleared). **Releasing** an accepted Task returns it to `ready`. `in-progress` is optional. |
| Task.verification | `pending → confirmed`, or `pending → disputed` | A BIX extension to FHIR. `confirmed` needs a `verifier` agent who is not the performer. |
| Initiative | `draft → planned → active → completed`, plus `cancelled` | `planned` needs a person with `initiative.plan`. A session moves to `active` when its period starts and `completed` when it ends, by rule. |
| Role | `requested → active → ended` | An invite creates an `active` Role. A request to join creates a `requested` one, which needs `member.manage` to activate. |
| TaskDefinition | `draft → active → retired` | A model-authored `draft` becomes `active` only with `ratifiedBy` |
| Report | `owed → in-preparation → submitted → acknowledged`, plus `returned`, `cancelled` | `owed` is created by rule from `recurrence`, or by hand. `returned` sends it back to `in-preparation` with a reason. A submitted report is never edited; a correction is a new submission that references it. |
| Invitation | `sent → accepted`, or `sent → declined` · `expired` · `withdrawn` | Accepting is done only by the invitee; it creates the Role, Team participant or Task participant the invitation names, through the usual permission rules. `expired` is set by rule after `expires`. See "Usernames and invitations". |
| ChangeProposal | `draft → accepted`, or `draft → declined` · `withdrawn` · `outdated` | `outdated` is set by rule when the target's `meta.version` moves past `basedOn`. An outdated proposal is never applied; a new one may be made against the current version. |
| Practice | `draft → active → retired` | A `draft` (from a model, or kept at close-out) becomes `active` only with a person holding `initiative.plan`. `observed` is recalculated by rule and never changes the lifecycle. |

## Conformance rules (MUST)

1. Every resource carries the common elements above.
2. Every state change produces exactly one `Provenance` record.
3. A record created by a model has `intent: proposal` (Task) or `status: draft` (everything else), and a `Provenance` agent of type `model` with the model's name and version. A model never edits an existing record directly: it proposes the edit as a `ChangeProposal` (rule 20).
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
20. **Proposed edits.** A change to an existing record that its author isn't allowed to make directly, and every change a model suggests, is a `ChangeProposal`. Accepting it applies its `change[]` as one change based on `basedOn` (rule 16), and moves its `includes[]` out of draft, together, with one `Provenance` per record. Accepting needs the same permission as making the change directly. Declining or withdrawing it cancels its `includes[]`.
21. **What a proposal may not touch.** A `ChangeProposal` never targets or changes a `Report` figure, a `Practice`'s `observed` figures, a `Decision` outcome, a `Vote`, `Task.participant.attended`, `Task.verification`, a `Role`, a `Consent`, a `SharingPolicy`, a `Provenance`, `Organization.assist`, or another person's `Person` record. It never sets `Task.owner` to a Person: asking someone stays with `task.assign`, and a proposal may only add to `Task.suggestedFor`.
22. **Assistance is opt-in per group.** `Organization.assist[]` lists the areas (`bayanihan:assist-area`) where the group turned on assistance; absent or empty means none. A model, or a deterministic assist rule, acts only in an area that is on, and every `ChangeProposal` it makes names that `area` and gives a `reason` a person can read. Changing `assist` needs `org.manage`. Turning an area off withdraws that area's open model proposals, by rule.
23. **Practice figures are calculated.** `Practice.observed` is calculated by rule from the organization's completed Initiatives, as set out in "Project memory: Practices", and recalculated when one of them completes or a `Task.practice` on one changes. Only the group's home server, or its hub phone when it runs without one, calculates it; other devices receive it. No person and no model sets it.
24. **Step identity.** `Task.practice` and `InitiativeTemplate.action[].practice` may point only to a Practice of the same organization. A model never sets them directly; it proposes them as a `ChangeProposal` in the `memory` area.
25. **Memory stays with the group.** A Practice names no one except the authors of its lessons. Shared outside its organization, it carries no `basis` and no lesson authors, and an adopted copy starts with no `observed` figures.
26. **Who sees a group's memory.** Inside its organization, a `Practice` is seen by the core team and anyone with `view.organization`, and by anyone else only through a Task they can see whose `practice` points to it. A model reads only what its person can see.

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
| **`Team`** (new resource, from FHIR CareTeam; CAE kind: Actor, a collective participant) | A committee, called a **team** in the app. `name` in the group's own words, `organization`, `initiative` (set for an event's committee, empty for a standing one), `kind` (standing · initiative), `participant[]` {`person`, `role` (lead · member), `status` (requested · active · ended), `period`}, `status`. Also `description`, `attachment[]` (the team's files) and `note[]` (updates inside the team, 2026-11-16), as every page has. A person may be in any number of Teams; being asked to lead or join is `requested` until they accept. |
| **`Task.team`** | The Team the work belongs to. Stays set when `owner` moves from the Team to a person who claimed or was asked, so the Team's lead keeps their permissions and the Task stays on the Team's page. |
| **`Task.owner`** may be a Team | Work lands with a committee first; its lead assigns it to a member or opens it up. |
| **`Task.dependsOn[]`** | Tasks that must be `completed` first, across Teams ("print shirts" waits on "confirm sponsor logos"). A Task can't move past `ready` until they are. |
| **`Task.partOf`** (from FHIR) | Decomposition: "Secure the venue" → "Shortlist 3 venues", "Visit", "Get a quote", "Pay the deposit". |
| **`Task.audience`** | How far down the funnel it reaches: `team` · `organization` · `open` (to outside volunteers). Only `open` Tasks appear in shared links and public lists. `goodFirstStep: true` marks work suited to newcomers, as WordPress marks "good first issue". |
| **Co-host participants** | A Team participant may hold their Role in an Organization listed in the Initiative's `partner[]`. They see only that Team's Tasks and the Initiative. |
| **Team-scoped permissions** | A Team lead holds `task.assign` and `task.confirm` for Tasks owned by their Team, without being an officer of the whole Organization. Money and beneficiary steps still need a confirmer who is not the performer. |
| **`InitiativeTemplate`** (new resource, from FHIR PlanDefinition; CAE kind: Instrument) | A group's saved way of running a kind of initiative: its Teams and their usual tasks. **Never shown as a noun in the app**, which says "Save these teams for next time" and "Start from last year's teams". `title` ("Our fun run", "Medical mission"), `organization` (or a federation or a module that publishes it), `team[]` (committee names and their default lead role), `action[]` {`title`, `team`, `taskDefinition`, `practice`, `audience`, `offset` (e.g. 42 days before the start), `partOf`}, `need[]`, `report[]`, `version`, `status`. |

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
6. **How each step went is remembered too.** A template keeps the plan; a `Practice` keeps how each kind of step has gone across the group's projects: how often it was needed, when it was done, what came before it, how often it was forgotten, and the lessons. See "Project memory: Practices".

## Volunteers belong to the structure

Outside helpers are part of the teams and the organization, not records kept beside them. WordPress shows how: anyone who contributes is a contributor, named in every release's credits, and can grow from a first patch to a team rep.

| Element | What it is |
|---|---|
| **`Team.participant.role`** adds `volunteer` | A helper is on the team's roster, alongside its lead and members, and sees the team's open work and updates. Joining a team through an invite or by finishing one of its Tasks makes them a `volunteer` participant, with their consent. |
| **A path, never a gate** | `volunteer → member → lead`, for a team and for the organization (`Role.code` volunteer-episodic → volunteer-regular → member). Core suggests a step up by declared rule, e.g. "Liza has helped Communications 5 times. Invite her to join the team?" A person always decides; nobody is promoted automatically. |
| **Credits** | Every Initiative has a credits list, derived from confirmed work and reviews, like a WordPress release's credits: everyone who helped, grouped by team, lead and volunteer alike. |
| **`Person.credit`** | How a person wants to be named in credits and on public pages: `nickname` · `full` · `anonymous`. Set by the person; `nickname` by default. Credits never show more than this. |
| **Asked back** | A team's past volunteers can be asked first when new open work appears (`Task.suggestedFor` from past participants), so a one-time helper becomes a regular without anyone keeping a list. |

### How volunteers take part in the work

Credit follows participation; participation comes first. Everything below applies equally to members and volunteers on a team.

| Element | What it is |
|---|---|
| **`Task.participant[]`** | People working on a Task together: {`person`, `role` (`owner` · `helper`), `status` (requested · active · ended)}. The `owner` is accountable; `helpers` join with "I'll help". Everyone active on a confirmed Task is credited as having performed it. `Task.owner` remains the single accountable person or Team. |
| **Joining a team creates a Role** | Joining a Team as a volunteer, with consent, creates a `Role` (`volunteer-episodic`) in the Organization (or keeps the Role they hold in a partner Organization). No one is on a team without a relationship to the group. |
| **Anyone on a team may propose work** | Any active Team participant may propose Tasks, Needs and Offers for that Team. They are `draft` until the Team lead (or anyone with `task.assign` for the Team) accepts them. Leads see proposals in "Waiting on you". |

**Who may change what on a Task:**

| Action | Owner | Helper | Other team participants | Team lead |
|---|---|---|---|---|
| Update checklist, output, attachments, notes | Yes | Yes | Propose | Yes |
| Add subtasks under it (`partOf`) | Yes | Propose | Propose | Yes |
| Edit title, due date, audience | Propose | Propose | Propose | Yes |
| Mark done | Yes | No | No | Yes |
| Confirm or review | Only if not the performer | Only if not the performer | If `reviewer` | Yes, if not the performer |
| Invite a helper | Yes | No | No | Yes |

"Propose" means the change is a draft until the owner or lead accepts it, recorded in History.

**Honouring, in the record:** credit by kind (performed, reviewed, verified, proposed, commented), thanks attached to confirmations, the person's own story across every group, the project's credits, and later, signed credentials they can show anyone.

### Core team and volunteers (decided 2026-11-06)

Everyone in a group may call themselves a volunteer, but organizationally there are two kinds of people, told apart by `Role.code`:

- **Core team:** `officer`, `core-member`, `member`. They run the group.
- **Outside the core team:** `volunteer-regular`, `volunteer-episodic`, `service-learning`, `partner-representative`, `donor`. They help with parts of it.

On a Team, `participant.role` says what a person does on that team (`lead` · `member` · `volunteer`); `Role.code` says who they are to the group. Apps label the two kinds "Core team" and "Volunteers".

### Seeing other committees' work (decided 2026-11-06)

For records shared at `organization` that belong to a project or a team. Records that don't (the Organization, Roles, Positions) are seen by every member, as before.

| Who | Sees by default | Can be changed by the group to |
|---|---|---|
| Officers, core members (`view.organization`) | All of the group's work | — |
| Members | Every team in the projects they're on, and every project's own record | Not a team that sets `Team.visibility: team` |
| Volunteers and others outside the core team | Their own teams, the projects those teams belong to, the other Teams in those projects (the Team record only: name, lead, who is on it; added 2026-11-12, so they can ask to join), and Tasks with `audience` `organization` or `open` | The whole project (`Team.access: initiative` on their team), or everything (`view.organization` in `Role.permissions[]`) |
| Anyone | What they're on (`owner`, `participant[]`) | — |

Editing is unchanged: the people on a record, a team's lead for that team, and holders of `task.assign` or `org.manage`. Sharing levels still apply first: `public` stays public and `private` stays private.

## One person, many groups, and work of your own

- **One `Person`, many `Role`s.** A person can lead one organization and volunteer in others at the same time. Teams and Tasks reference the Person.
- **Permissions come from the group that owns the record.** Bayanihan Core resolves them from the person's active Role, Positions and Team leadership in *that* Organization only. Leading one group grants nothing in another.
- **Personal work.** An `Initiative` belongs to an `organization` **or** a `person` (exactly one). Personal projects work like any other; only the person (and people they add) can change them. A personal project can later be moved into a group the person starts, as a recorded change.
- **One story.** Signed records from every group, and from personal work, are copied to the person's device and shown together. Records from different groups never merge; each keeps its own signature.

## Organization structure: positions and terms

Teams belong to a project (`Team.initiative`); a group may also keep a few standing teams (no `initiative`). The **organization's own structure** is separate: its board and officers, who hold them, and for how long.

**Lesson from Popolo:** a **Post** is a position in an organization ("President") that people hold through a **Membership** for a period. It keeps the office separate from the person, so the July handover is a new holder of the same Post. BIX takes the same split.

| Element | What it is |
|---|---|
| **`Position`** (new resource, from Popolo Post; CAE kind: Instrument) | `organization`, `title` in the group's words, `kind` (`board` · `officer` · `committee-chair` · `other`), `seats` (e.g. 11 trustees), `term` (e.g. 1 year), `permissions[]`, `requiredBy` (a law or a parent body's rules, as text), `status` |
| **`Role.position`** | The Position a Role holds, with `period` as the term. Several people may hold a Position up to its `seats`. |
| **Elections** | A `Decision` whose options are candidates for a Position. The winner's Role is created by rule from the outcome. Open ballots only in v0.1 (see "Decisions and voting"). |
| **Saved structures** | Like saved teams: a group starts from a structure for its kind (below), then changes titles, seats and terms. Stored as `Position` resources it owns. |

**Common starting structures** (for the app to offer; *not legal advice; groups and their advisers confirm their own bylaws*):

| Kind of group | Usual positions | Source of the requirement |
|---|---|---|
| SEC-registered non-stock corporation | Board of trustees; president (who must be a trustee), treasurer, corporate secretary, and any others the bylaws set | Revised Corporation Code (RA 11232). As we understand it, the president may not also be secretary or treasurer, the secretary must be a Philippine citizen and resident, and the treasurer a resident. To confirm with an adviser. |
| Cooperative | Board of directors with chair and vice chair, secretary, treasurer, general manager; audit, election, mediation and conciliation, and ethics committees | Cooperative Code (RA 9520). To confirm. |
| Rotaract or Interact club | President, president-elect, vice president, secretary, treasurer, sergeant-at-arms, directors of avenues of service, immediate past president | Rotary International's club constitution |
| JCI local organization | President, executive vice presidents, vice presidents, secretary general, treasurer, general legal counsel | JCI Philippines' constitution |
| Community or meetup (e.g. a WordPress community) | Organizers and co-organizers | The community's own norms |
| Informal group | Whatever the group calls its people | — |

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
| **`Team.access`** | What this team may read. `own-tasks` (default) · `initiative`: read everything in the Initiative, as a Communications team needs | FHIR `CareTeam` |
| **`Team.visibility`** | Who may read this team's work. `initiative` (default): the core team members on the project · `team`: only the team, its lead, and people with `view.organization` | Added 2026-11-06 |
| **`Task.checklist[]`** | Small steps without owners: {`text`, `done`, `doneBy`} | Trello and GitHub task lists |
| **`Task.category[]`** | Optional tags in the group's namespace | GitHub labels |
| **Credit by kind** | A person's record counts work they **performed, reviewed, verified, proposed** and **commented on**, each separately | WordPress props credit reviewers and reporters |

**Left out on purpose:** size, estimate and iteration fields; required fields beyond a title; custom field builders. They are what made project boards feel like paperwork.

## Decisions and voting

Groups decide some things together: the leads of a fun run vote on the overall design concept from the Design team; a club votes on its next project. A vote is part of the record, and every BIX implementation must count it the same way, so it is defined here and counted by Bayanihan Core.

**Lessons.** From **Popolo** (the civic standard for legislatures, which CEP maps to): a Motion, a VoteEvent and individual Votes. From **Loomio** (open-source group decisions, AGPL): the methods groups actually use, a closing time, and an outcome statement written by a person.

| Element | What it is |
|---|---|
| **`Decision`** (new resource, from Popolo Motion + VoteEvent; CAE kind: Instrument while open, Event once decided) | `about` (any resource, e.g. Task LU-7), `question`, `method` (`approve` · `choose-one` · `choose-many` · `ranked` · `consent`), `option[]` {`id`, `label`, `description`, `attachment[]`}, `voters` (a Team, the leads of every Team in an Initiative, a Role, or named Persons), `eligible[]` (the voters, fixed when it opens), `opens`, `closes`, `quorum`, `threshold` (`majority` · `two-thirds` · `unanimous`; for `consent`: no objections), `showResults` (`after-voting` · `after-close`), `status`, `outcome` {`option[]`, `tally`, `decidedAt`}, `statement` (written by a person) |
| **`Vote`** (new resource, from Popolo Vote; CAE kind: Event) | `decision`, `voter`, `choice[]` (option ids, in order for `ranked`), `objection` (for `consent`), `reason`, `cast`. A voter may change their vote until `closes`; the last one counts. |

**Lifecycle:** `draft → open → closed → decided`, plus `no-quorum` and `cancelled`.

**Rules (conformance):**

- **The outcome is calculated, never set.** Core counts the Votes by the declared `method` and `threshold`. No person and no model sets `outcome`; a person writes the `statement`.
- **Eligibility is fixed when voting opens,** so changing a Team's members mid-vote changes nothing.
- **A model never votes,** and never proposes a Vote on anyone's behalf.
- **Offline votes count only if they reach the server before `closes`.**
- **A decided Decision can be the approval for a Task:** `Task.reviewer` may be a Decision, so "the leads approved the design concept" is a confirmation like any other, with the tally as its evidence.
- **Open ballots only in v0.1.** Secret ballots need cryptography to stay countable without revealing voters; they come later, with signatures.
- **Visibility follows `sharing`.** By default a vote is visible to the people who may vote.

## Recorded when done, kept by each person (decided 2026-10-28)

No confirmation back-and-forth for ordinary work. **"Done" is the record.**

1. **Done counts immediately.** When a Task is marked `completed`, its participants are credited at once. `verification` is needed only where it matters: steps involving money or beneficiaries (always a second person), and kinds of work a group chooses to review (`TaskDefinition.review: true`, or `Task.reviewer` set). Review is off by default.
2. **Signed on completion.** The group's home server or hub signs the completed record at that moment with the group's key, over its RFC 8785 canonical form, offline too. The signature is the group's stamp; no person has to approve it.
3. **A copy for each person.** The signed record is copied to the device of every participant the next time their app syncs with the hub or the cloud.
4. **Tamper-evident, not tamper-proof.** A device's owner can always edit what's on their device, but any change to a signed record breaks its signature, and every BIX app and profile that checks it shows it as altered.
5. **Published by choice.** When a person goes online, their Dasig profile shows only the signed records they choose to show, named the way they choose (`Person.credit`).
6. **Claiming.** Records a group made for a nickname join someone's profile only through that group's invite link or from the group's own server, never by name matching.

This replaces the earlier rule that credit counts only after confirmation. Conformance rule 5 (a second person for money and beneficiary steps) is unchanged.

## Who it's for, and the goals groups share

Bayanihan's larger proposition: organizations, governments and communities working toward the **same goals for a community**, each seeing how their work adds up. Three things make that possible: a shared way to say *what cause*, *who is served*, and *which goal* the work serves.

**Lessons.** FHIR **`Group`** describes a population by its characteristics and size without naming anyone; FHIR **`Goal`** is a target with measures and a due date. The **UN Sustainable Development Goals** give causes a shared code that governments, NGOs and funders already use. The collective-impact approach (shared goals, shared measures, separate work) is the model; OCHA's 3W (who does what, where) is the precedent for adding up many groups' work in one place.

| Element | What it is |
|---|---|
| **`cause[]`** on Organization and Initiative | What the work is for, as Codings: an SDG code (e.g. `sdg:4` quality education, `sdg:14` life below water) plus the group's own words ("coastal cleanup", "learning for kids") |
| **`Group`** (new resource, from FHIR Group; CAE kind: Observable) | **Who is served**, without naming anyone: `characteristic[]` (e.g. `bayanihan:population` codes: children, youth, students, senior citizens, PWDs, fisherfolk, Indigenous peoples, women, households), `location` (PSGC), `quantity` (estimated size). Referenced by `Initiative.servesGroup[]`. |
| **Reach** | How many were actually served is a Report figure (`households-served`, `learners-served`, …), counted from completed work as before. Never a list of names. |
| **`Goal`** (new resource, from FHIR Goal; CAE kind: Instrument) | **A shared target for a community**: `title` ("Every child in Barangay Pajo reads at grade level by 2028"), `owner` (an LGU, a coalition or any Organization), `cause[]`, `servesGroup[]`, `location`, `target[]` {`figure` code, `value`, `due`}, `sharing` (usually `public`). |
| **`Initiative.contributesTo[]`** | {`goal`, `status`}: the Goals a project is enrolled in. Any group may ask to enroll; the Goal's owner accepts (see below). |
| **Goal progress** | Calculated, never typed: the sum of matching figures from **accepted** contributing Initiatives' submitted Reports that are shared with the Goal's owner (`network` or `public`). Groups that contribute are listed; groups that haven't reported are listed, not estimated. |

### Publish as you are, find each other, join a goal if you want (decided 2026-10-28)

Bottom-up first. Nobody is made to work with anyone.

0. **What publishing means.** Sending a project's public summary to the public directory on the Dasig-hosted Bayanihan Server. It is separate from creating a project or running a hub: an offline group creates projects as usual, and its summaries publish when the hub next syncs online. **On by default** (decided 2026-10-28), with a clear note ("Your project's summary is public. Turn off any time"); groups whose served group includes children or patients are asked explicitly instead.
1. **Publish as you are.** A group publishes a project the way it already runs it. Publishing shows a **public summary** only: title, group, place (barangay or above, never an address), causes, who it's for (as a description), status and dates. Tasks, people, files and figures stay as shared as they were. Offered when a project is created, one tap, and can be turned off.
2. **Tag when ready.** `cause[]` and `servesGroup[]` are optional at first. The app suggests them from the project's words; the group confirms.
3. **Find who's already working here.** Bayanihan Server answers **"who's working on what, for whom, where"** from published summaries: by place (PSGC), by cause, by who's served. When a group creates a project, it sees *"3 groups also work on learning in Barangay Pajo"*, as information, never a requirement.
4. **Self-synchronise.** From a published project, others can follow it, offer help, message the group, or invite it as a partner (`Initiative.partner[]`). Groups decide; nothing links automatically.
5. **Join a larger effort.** When a foundation, a city or a national agency sets a **Goal**, any group can **enroll** a project in it. Enrollment is `Initiative.contributesTo[]` {`goal`, `status`: `requested → accepted`, or `declined`}; the Goal's owner accepts, so a goal's list of contributors can be trusted. Only accepted enrollments count toward the Goal's progress.

**Default categories.** BIX ships two value sets so groups don't start from a blank list, each mapped to the SDGs with SKOS-style mappings:

| `bayanihan:cause` | Maps to | | `bayanihan:population` |
|---|---|---|---|
| Education and learning | SDG 4 | | Children |
| Health | SDG 3 | | Youth |
| Food and nutrition | SDG 2 | | Students |
| Environment and coasts | SDG 13, 14, 15 | | Senior citizens |
| Disaster readiness | SDG 11, 13 | | Persons with disability |
| Livelihood and work | SDG 1, 8 | | Women |
| Water and sanitation | SDG 6 | | Indigenous peoples |
| Housing and communities | SDG 11 | | Fisherfolk and farmers |
| Youth leadership | SDG 4, 16 | | Families and households |
| Civic participation | SDG 16 | | Out-of-school youth |
| Digital skills and tech | SDG 4, 9 | | Patients and caregivers |
| Arts, culture and heritage | SDG 11 | | Communities (everyone in a place) |
| Faith and community care | SDG 1, 3 | | |
| Animal welfare | SDG 15 | | |

Groups add their own words in their namespace; a module (e.g. animal welfare) adds its own codes. Codes are never redefined.

**Privacy rules for beneficiaries:**

- People served are **counts and descriptions**, never named records, unless a module with its own consent design says otherwise (e.g. scholarship monitoring, later).
- **Small numbers are hidden in public views.** Any public figure below 5 for one place and group shows as "fewer than 5", so nobody can be identified.
- Health, disability and similar characteristics are sensitive under the Data Privacy Act; groups record them only as counts, and only when the work needs it.

**Where shared goals live.** A Goal is an ordinary BIX record with a global address, so it can live on any Bayanihan Server (an LGU's, a federation's) and be linked from anywhere. In practice, finding goals and adding up many groups' work needs a server that many groups use. For v0 that is the **Dasig-hosted Bayanihan Server**, which also publishes public Goal pages. Later, servers can federate and a Goal's owner can host it themselves.

## Files, home servers and hubs

**Files (decided 2026-10-28).** An `Attachment` is stored by the group's own Bayanihan Server, in S3-compatible storage that self-hosters can run themselves (e.g. MinIO), so no outside cloud account is required. A link to an outside file (Google Drive and similar) is allowed as an Attachment with `url` only and is shown as "kept outside the group": the group doesn't control its sharing or its future.

**Home server.** Every Organization has exactly one **home server** at a time: the Bayanihan Server that decides exclusive changes (claims, asks, confirmations, votes). Other copies replicate. This keeps "first come, first served" true when copies are apart.

**Hubs (in v0, decided 2026-10-29).** A group may dedicate a phone or Android tablet as its **hub**: a Bayanihan Server running on the device, reachable over its Wi-Fi hotspot or the local network.

| Question | Design |
|---|---|
| Who talks to it | Members' and volunteers' Android apps nearby. They find it on the local network and pair once by scanning a QR code on the hub, which also carries the hub's key so the connection can be verified. NFC is optional (iPhones and browsers can't rely on it). |
| What it holds | The group's BIX records and files, so photos and documents can be added with no internet at all |
| Online too | When the hub has internet, it syncs with the group's cloud server as BIX Bundles |
| Who decides | If the hub is the home server, it decides claims for its group; the cloud copy follows. If the cloud is home, the hub queues exclusive changes as pending. Moving "home" is an explicit, recorded act. |
| Losing the hub | Its storage is encrypted, and it backs up to the cloud whenever it can |
| Web users | Use the cloud server. Browsers can't reliably install an app that talks to a local device. |
| Standalone | A single phone with no hub and no cloud runs Bayanihan Server inside the app, on its own storage. Same API and rules. (v0, 2026-10-29) |

**Taking a group to a hub and back (decided 2026-11-28).** For a group that usually works online and goes somewhere
without signal: an event venue, a barangay, an evacuation center.

1. **Hand over.** While there is still signal, someone with `org.manage` makes a phone the group's hub. The cloud
   server records an `Endpoint` (`kind: hub`, the hub's `publicKey`) and points `Organization.homeServer` to it, as one
   recorded change. The hub then copies the group's records as they are, versions and signatures included.
2. **Away.** The hub is home: it decides exclusive changes and signs completed work. Members pair with it and work
   there. The cloud copy is read-only for the group's records; a change sent to it is refused with "your group is
   working on its hub", and the phone keeps it to send again later.
3. **Hand back.** When the hub has signal again, it sends every record that changed while it was home, with their
   Provenance, as one `Bundle` (`type: sync`, from the hub's Endpoint). The cloud server accepts them as they are,
   because nothing changed there while the hub was home, marks their Provenance `via: {kind: hub, endpoint}`, and
   points `homeServer` back to itself. Then phones send what they kept (step 2) and it is replayed as usual.
4. **Only the hub that is home** may hand back, and only once. A hub that never comes back can be released by someone
   with `org.manage`; its records are lost unless it returns, so the app warns before releasing.

**Your own facts win (decided 2026-11-28).** A change that arrives stale (rule 16) is refused, except when everything it
changes is the person's own: their own entry in `Task.participant` (releasing their place, their check-in, their
hours, their period) or their own `Person` record. Then the server re-applies those fields on top of the current
version and checks the result like any change. Exclusive changes (claiming a place, asking, confirming, voting) stay
first come, first served at the home server. Additions never conflict.

**How a change travelled.** `Provenance.via` says how a change reached the home server: `direct`, through a `hub`
(with its `endpoint`), or `replayed` from a phone's queue after being offline. Reports and History may show it
("recorded at the venue hub, synced 6:40 PM").

**Not in v0:** phone-to-phone mesh without a hub (store-and-forward like Briar), which needs signed Bundles first.

**Lessons:** Kolibri (Learning Equality) runs offline on local devices and syncs between them and the cloud; ODK and CommCare collect data offline in the field; Briar relays messages over Wi-Fi and Bluetooth; CouchDB and PouchDB replicate offline-first databases.

## Privacy and safety in v0.1 (decided 2026-10-28)

Trust is in v0, and hardened in later versions. Not legal advice; the Data Privacy Act wording is to be checked by an adviser.

| Rule | What it means |
|---|---|
| **Deleting an account** | The person's profile, contact, photo and the photos they added are removed after a 14-day grace period. Groups keep the work they recorded, with the person shown as "a former volunteer", so histories and report figures still add up. |
| **Removing someone** | Ending a Team participation or a Role never erases past work; it stays in the group's history and in the person's own story. |
| **Blocking** | A group may stop a person joining through its links (`ShareLink` refuses them). Separate from removing, and deliberate. |
| **Links are revocable** | Every `ShareLink` can be revoked at once. Revoking a link can also clear every draft that arrived through it. |
| **Spam can't reach anyone** | Anything proposed through a public link is `draft` and `private` until a member accepts it (rule 19). |
| **Photos with children** | An `Attachment` may be marked `showsMinors`. A group setting, on by default, keeps such photos from ever leaving the group: no previews, no public pages, no profiles. |
| **Messages for Bayani** | Raw messages stay on the phone (rule 11). Sharing a message to improve Bayani is opt-in, per message, with names removed first, and can be withdrawn at any time. |
| **Seeing your data** | A person can see counts of what is kept about them, download all of it as BIX (rule 18), choose what their profile shows, and delete their account. |

## Filling the gaps found in the 2026-10-28 audit

Everything decided for Dasig that another BIX app would also need belongs in BIX. These close the gaps between what the screens assume and what the language could say.

| Element | What it is | Lesson |
|---|---|---|
| **`Signature`** data type, on `Provenance.signature` | {`who` (the group's server or hub), `when`, `algorithm`, `keyId`, `value`} over the record's RFC 8785 canonical form. Required on completed work (see "Recorded when done"). | FHIR `Signature`; W3C Data Integrity |
| **`Endpoint`** (new resource, from FHIR Endpoint; *transport, not a CAE kind*) | A Bayanihan Server or hub that holds a group's records: `address`, `kind` (`cloud` · `hub` · `self-hosted`), `publicKey`, `status`. **`Organization.homeServer`** references the one Endpoint that decides exclusive changes. | FHIR `Endpoint` |
| **`Consent`** (new resource, from FHIR Consent; CAE kind: Instrument) | What a **person** agreed to, recorded once and withdrawable: `person`, `scope` (`share-messages-for-bayani` · `appear-in-credits` · `photo-of-me` · `contact-by-group`), `status` (`active` · `withdrawn`), `dateTime`. `SharingPolicy` stays for a group's defaults. | FHIR `Consent` |
| **`Follow`** (new resource; *a relationship*) | A Person or Organization following a published Initiative, Organization or Goal, to see its updates. Ends at any time. Never grants access beyond the public summary. | ActivityPub `Follow`; FHIR `Subscription` for delivery later |
| **`Offer.matchedTo`** widened | May reference a `Need`, a `Task` or an `Initiative`, so "offer help" works from any published project | — |
| **`Communication.recipient`** widened | May be a Person, a Team or an Organization, so "message this group" from a public page and "@Speakers" both fit | FHIR `Communication.recipient` |
| **`Task.due`** | The date work is due, separate from `restriction.period` (when it may be done) | FHIR `Task.restriction` vs due dates |
| **`Organization.kind`** adds | `foundation` · `national-agency` · `school` · `university`, the bodies most likely to set Goals | — |
| **`Organization.vocabulary[]`** | A group's own words for core terms {`term`, `label`}: "exhibitors" for sponsors, "committee" for team. Every BIX app shows them. | Popolo's labels; an event team's editorial styleguide |
| **Public summary** for Organizations | The same "publish as you are" summary as projects: name, kind, place, causes, logo. On by default. | — |
| **`InitiativeTemplate` on wrap-up** | Saving a project's teams back records which Tasks and offsets to keep, as a new version | FHIR `PlanDefinition` versions |

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

## Shifts, showing up and time (decided 2026-11-09)

Event work is mostly shifts: "4 marshals at km 4, 5:00 to 7:30". These elements let one Task stand for a shift, record
who actually came and for how long, and let a person hand their place to someone else. They come from walking a club's
fun run end to end (coordinator and volunteer, side by side).

| Element | What it is | Rules |
|---|---|---|
| **`Task.slots`** | How many people the work needs. Default 1 (one owner, as before). | With `slots` > 1, "I'm in" adds the person as an active `participant` (`role: helper`) and the Task stays `ready` with the Team as `owner` until active participants equal `slots`; then it becomes `accepted`. Releasing a place reopens it. "I'm in" fills *any* open place, so two people never collide. When full, a person may offer to be a backup (an `Offer` of time matched to the work's `Need`); a released place goes to the backup first. |
| **`Task.participant.attended`** | `{at, by}`: the person showed up. `by` is the person themselves (self check-in) or anyone with `task.assign` for the Task. | Separate from saying yes. Figures may count attended participants (`volunteers-active`). Never set by a model. |
| **`Task.participant.period`** | The person's own start and end, when it differs from the Task's `executionPeriod`. | `sum-task-hours` uses each participant's `period` when present, otherwise the Task's. |
| **`Task.participant.replaces`** | A proposed swap: a new participant with `status: requested` and `replaces` pointing to the person they'd take over from. | The named person accepts (their entry becomes `active`, the replaced one `ended`) or declines (the proposal is removed). Only the replaced person or the Team lead may propose it. |
| **`Task.restriction.arrival`** | `{at, location, note}`: when and where to arrive, if different from the work itself ("4:30 at gate 2, bring water"). | Shown to participants and in reminders. |
| **`Person.skill[]`** | Skills the person says they have, as codings (e.g. `first-aid`, `driving`, `writing`). | Set only by the person. Groups record what they've checked in `Role.qualification`; matching against `Task.requires` may use either, and says which. |

### Planned and given time (decided 2026-11-11)

Volunteer hours are what schools, employers and funders ask for, so they must be honest. A coordinator plans how long
work should take; each person confirms or changes it; the group's signature stands behind the result. (After ClickUp
and Monday.com time estimates, without their timers: volunteers don't run stopwatches at a cleanup.)

| Element | What it is | Rules |
|---|---|---|
| **`Task.estimate`** | `{value, unit, per}`: how long the work should take, e.g. `{2.5, "h", "person"}`. `per` is `person` (default) or `task` (shared by everyone on it). | Set by whoever plans the work. Shown to volunteers before they say yes ("about 2.5 h"). |
| **`TaskDefinition.step.estimate`** | The same, on a saved way of working, so every event made from it starts with durations. | |
| **`Task.participant.hours`** | `{value, source}`: the time one person gave, when there's no exact start and end. `source` is `planned` (accepted from the estimate), `stated` (the person said so), or `measured` (from a check-in or the shift's period). | Set by the person, or by a lead with `task.assign`. Never by a model. A `stated` value is the person's claim until the Task is confirmed or signed; reports may show confirmed and stated hours separately. |

**How hours are counted** (`sum-task-hours`, and anywhere an app shows a person's hours), per active participant on
completed work, first match wins:

1. `participant.period` (their own start and end);
2. `participant.hours.value`;
3. `restriction.period`, the shift's window, when the work was a shift;
4. `estimate` (divided among participants when `per` is `task`);
5. nothing: 0 hours.

`executionPeriod` (when the work was taken and when it was marked done) is **not** time given, and is never counted
as hours: a task taken on Monday and finished on Saturday is not 120 hours.

Deferred, to be decided with the pilot groups: signed credentials about a person, an emergency contact seen only by
officers, and guardian consent for volunteers under 18.

## Proposed edits and assistance (decided 2026-11-11)

BIX could already propose *new* things: a Task with `intent: proposal`, a Need or Offer in `draft`. It had no way to
propose an *edit* to a record that already exists, such as "move this step to Logistics" or "this has to happen after
that". Without one, an app would either let a model edit records directly, which breaks propose-then-commit, or invent
its own suggestion store that no other app can read. Bayani, the small model in development, needs this for reviewing a
plan; so does a member who spots a mistake but can't fix it themselves.

**Lessons.** GitHub's suggested changes in a review and GlotPress's suggestions (an edit waits beside the original until
someone with the right to approve it does) are the model for the workflow. JSON Patch (RFC 6902) is the model for the
change itself: a short list of `add`, `remove` and `replace` operations on paths, which any implementation can apply
and show as a before-and-after. FHIR has no separate resource for this; its nearest pattern is a Task with
`intent: proposal` whose `focus` is the record, but in BIX a Task is a claimable step, so a separate resource keeps the
two from being confused.

| Element | What it is | Rules |
|---|---|---|
| **`ChangeProposal`** (new resource; CAE kind: Instrument) | One proposed edit to one existing record (`target`), made against a known version (`basedOn`, the target's `meta.version`) | Starts `draft`. Someone allowed to make the change directly accepts or declines it (rule 20). If the target changes first, it becomes `outdated` by rule and is never applied, so a stale suggestion can't overwrite newer work. |
| **`change[]`** | JSON Patch operations: `op` (`add` · `remove` · `replace`), `path` (an element of the target, e.g. `/owner`, `/dependsOn/-`, `/goodFirstStep`), `value` | The result must still be a valid record and a valid lifecycle transition, checked by Core exactly as if it were made directly. Some elements are off limits to any proposal (rule 21). |
| **`includes[]`** | New draft records that belong to the same suggestion, e.g. the smaller steps of a split | Accepted or cancelled together with the proposal, in one change. A proposal needs `change[]`, `includes[]`, or both. |
| **`area`** | The assistance area it came from (`bayanihan:assist-area`) | Required for proposals from a model or an assist rule (rule 22). Lets a group see, and switch off, one kind of help. |
| **`reason`** | Plain words a lead reads before deciding: "Projects like this put water stations under Logistics" | Required for proposals from a model or an assist rule. Never a score, and never a ranking of people. |
| **`Organization.assist[]`** | The areas where this group turned on assistance, from `bayanihan:assist-area` | Per group. Absent or empty means none: nothing is on until an officer turns it on. Changing it needs `org.manage`. Applies to model and rule-based assistance alike, so a group chooses the help it wants, not the technology behind it. |

**Who can propose.** Any person with an active Role in the organization may make a `ChangeProposal` for a record they
can see, the same way any team participant may propose Tasks (see "Volunteers belong to the structure"). A model makes one
only on behalf of a person, in an area that is on. Proposals from someone without a Role go through public proposals
(rule 19), which cover only new Needs, Offers and Persons.

**Common suggestions, written as proposals.**

| Suggestion | `target` | `change[]` | `includes[]` |
|---|---|---|---|
| Split a step into smaller ones | The step | none | New Tasks with `intent: proposal` and `partOf` the step |
| Add a step projects like this usually include | The Initiative | none | One new Task with `intent: proposal` |
| Move a step to another team | The step | `replace /owner` with the Team | none |
| This must happen after that | The later step | `add /dependsOn/-` | none |
| Mark a good first step | The step | `replace /goodFirstStep` with `true` | none |
| These two are duplicates | The duplicate | `replace /status` with `cancelled`, `add /note/-` naming the other | none |
| Someone who could take this step | The step | `add /suggestedFor/-` with the Person | none |

**Example.** Bayani, reviewing a fun run plan for the person who asked it to, suggests moving the water stations step to
Logistics. A lead taps yes; the Task's `owner` changes, the proposal becomes `accepted`, and both changes carry
Provenance naming the model and the lead.

```json
{
  "resourceType": "ChangeProposal",
  "id": "7c1e2f4a-3b5d-4e8f-9a01-2b3c4d5e6f70",
  "meta": { "version": 1 },
  "target": { "reference": "Task/water-stations" },
  "basedOn": 4,
  "organization": { "reference": "Organization/runners-club" },
  "area": { "system": "bayanihan:assist-area", "code": "review-plan" },
  "reason": "Projects like this put water stations under Logistics, and Logistics already has the table and coolers.",
  "change": [ { "op": "replace", "path": "/owner", "value": { "reference": "Team/logistics" } } ],
  "status": "draft"
}
```

```json
{
  "resourceType": "Provenance",
  "id": "0d9b8a7c-6e5f-4a3b-8c2d-1e0f9a8b7c6d",
  "meta": { "version": 1 },
  "target": [ { "reference": "ChangeProposal/7c1e2f4a-3b5d-4e8f-9a01-2b3c4d5e6f70" } ],
  "activity": "propose",
  "agent": [
    { "type": "model", "model": { "name": "Bayani-1-1B", "version": "<version>" } },
    { "type": "author", "who": { "reference": "Person/ana" } }
  ],
  "occurredAt": "2026-11-20T21:14:00+08:00"
}
```

**Not in v0.1.** Proposals that change several existing records at once (make one per record, and accept them side by
side), proposals from outside the organization other than rule 19, and per-team or per-person assistance settings
(per group only, to keep it simple).

## Project memory: Practices (decided 2026-11-13)

A coordinator running a project has to remember everything it needs, and most of that knowledge sits with whoever ran
it last time. Officers change every year, committee leads are often doing it for the first time, and what went wrong
lives in group chats. Copying last year's plan carries the steps over but not how they went: which step was forgotten
and added in the last week, which one always slips, which was a one-off.

A **`Practice`** is one kind of step as this group does it ("Get the barangay permit", "Confirm marshals"), with how it
has gone across the group's finished projects. Each step in a project can say which Practice it is (`Task.practice`).
From those two things, rules can count and compare, and a small model only has to make the judgments rules can't:
whether a step is the same as a known Practice, whether a Practice applies here, whether a step was a one-off. That
split is deliberate. The structured record and the rules are the memory; the model reads it.

**Lessons.** FHIR's `PlanDefinition` is a reusable plan (BIX's `InitiativeTemplate`) and FHIR keeps measured values
separate from the things they measure (`Observation`); a Practice's `observed` figures follow that, and BIX rule 12's
"derived, not typed in". Project retrospectives ("what would we do differently?") are where groups already write
lessons. GitHub Projects, which many volunteer conference teams use, shows the gap: copying a project copies its items and
fields, not what was learned running it. FHIR `Task.basedOn` means "the request this task fulfils", so BIX names the
link `Task.practice` to avoid a different meaning under a familiar name.

| Element | What it is | Rules |
|---|---|---|
| **`Practice`** (new resource; CAE kind: Instrument) | One kind of step as this organization does it: `title` (general, e.g. "Book the venue", not "Book Mactan Expo"), `organization`, `appliesTo[]` (the kinds of project it belongs to, as `Initiative.category` codes), `team` (the team name that usually owns it), `partOf` (a broader Practice it is a step of), `after[]` (Practices that usually come before it), `taskDefinition` (optional: the detailed way of doing it), `source` (`own` · `starter` · `adopted`), `adoptedFrom`, `description`, `lesson[]`, `observed`, `status` | `draft → active → retired`. A Practice proposed by a model, or made at close-out, starts `draft`; a person with `initiative.plan` makes it `active` (rule 4). |
| **`Practice.observed`** | Figures about how it has gone, calculated by rule (rule 23): `ofProjects` (the group's completed projects of these kinds), `included` (how many of them had this step), `addedLate` (how many added it in the last 7 days before the start, or after), `dayFromStart` {`median`, `earliest`, `latest`} (the day it was done, relative to the project's start; negative is before), `lastSeen`, `basis[]` (the projects counted), `calculated` | Never set by a person or a model, and no `ChangeProposal` may change it (rule 21). |
| **`Practice.lesson[]`** | `{text, author, time, initiative}`: what someone learned ("Ask the barangay a month ahead; it took three weeks last time") | Written by a person, or drafted by a model as a proposal that a person accepts. Inside the group every lesson names its `author`; a copy shared outside drops `author` and `initiative` (rule 25). |
| **`Task.practice`** | The Practice this step is an instance of | Set like any change to the Task (`task.assign` or `initiative.plan`). A model proposes it as a `ChangeProposal` (rule 24). |
| **`InitiativeTemplate.action[].practice`** | The Practice a saved step stands for | A project started from the template gets `Task.practice` on each step, so matching is needed only for new steps. |

**How the figures are calculated** (rule 23), for one Practice:

1. `ofProjects`: the organization's Initiatives with `status: completed` whose `category` shares a code with
   `appliesTo`. `basis[]` lists them.
2. `included`: how many of those have at least one Task, not `cancelled`, with `practice` set to this Practice.
3. `addedLate`: how many of the included projects first recorded that Task (its earliest `Provenance.occurredAt`) less
   than 7 days before the Initiative's `period.start`, or later.
4. `dayFromStart`: for each included project, the day the step was done (`executionPeriod.end`, else
   `executionPeriod.start`) minus the Initiative's `period.start`, in whole days. `median`, `earliest` and `latest`
   over the projects that have one.
5. `lastSeen`: the latest `period.start` among the included projects.

**What rules do, and what the model does.**

| Question | Who answers | How |
|---|---|---|
| What does this project usually need that it doesn't have yet? | Rule | Active Practices that apply to its categories, `included` in at least half of `ofProjects` (or `starter` Practices with no figures yet), with no Task pointing to them |
| Is anything usually done by now? | Rule | Practices whose `dayFromStart.median` has passed, with a Task that isn't `completed` |
| Is anything out of order? | Rule | A Task whose Practice lists another in `after[]`, where that Practice's Task exists and isn't in `dependsOn` |
| Is this step the same as a known Practice? | Model | A proposal to set `Task.practice` |
| Does this usual step apply to this project? | Model | Filters the rule's list before it is shown |
| Was this step a one-off? | Model | At close-out: keep it as a new Practice, or not |
| What did we learn? | Model drafts, a person writes | A proposed `lesson` |

All of these appear to the coordinator as suggestions with their evidence ("in 2 of your 3 fun runs"), never as
requirements. A group turns the model's part on with the `memory` assistance area (`bayanihan:assist-area`).

**Closing a project.** When an Initiative becomes `completed`:

1. By rule, the `observed` figures of the organization's Practices that apply to it are recalculated.
2. Steps with no `practice` are offered for review: match each to an existing Practice, keep it as a new Practice
   (`draft`, then a lead confirms), or leave it as a one-off. The model may propose all three.
3. A lead may add lessons. Saving the project's steps back into its `InitiativeTemplate` stays a separate choice
   ("How a group's way of working is remembered", point 3).

**One memory for the whole group (decided 2026-11-14).** Bayani runs separately on each member's phone, but the memory
is not in the model: it is the group's `Practice` records, which sync like any other record. Every phone runs the same
model and reads the same records, so every member's Bayani works from the same memory. Two rules keep it that way:

1. **Figures are calculated in one place.** A volunteer's phone holds only the work they can see, so figures
   calculated there would disagree with an officer's. `observed` is calculated only by the group's home Bayanihan
   Server, or by the hub phone when the group runs without one, where all of the group's records are (rule 23). Other
   devices receive the figures and never recalculate them. The suggestions built from them (what a project usually
   needs, what is usually done by now, what comes first) may be worked out on any phone, from the figures it holds.
2. **Bayani sees what its person sees.** There is no separate access for the model: what Bayani reads on a phone is
   built from the records that person may see, so its suggestions and evidence never reveal more than they could
   open themselves. Inside the group (rule 26), the core team and anyone with `view.organization` see all of the
   group's Practices, with their lessons. A volunteer sees a Practice, and its lessons, only when a step they can see
   points to it, so "Ask a month ahead" appears on the permit step for whoever is on it. Changing a Practice still
   needs `initiative.plan`.

**Starting points and sharing.** Dasig, a federation or a module may publish `starter` Practices for common kinds of
project, so a new group's first project has something to compare against. Adopting one copies it into the group as
`adopted`, with `adoptedFrom` and empty figures; from then on it is the group's own. A Practice shared outside its
organization carries no `basis` and no lesson authors (rule 25), so a group can share how it works without sharing
who did it.

**Example.** A running club's permit step, after three fun runs, and the step in this year's plan that points to it.

```json
{
  "resourceType": "Practice",
  "id": "5b6c7d8e-9f0a-4b1c-8d2e-3f4a5b6c7d8e",
  "meta": { "version": 3 },
  "title": "Get the barangay permit",
  "organization": { "reference": "Organization/2a3b4c5d-6e7f-4a8b-9c0d-1e2f3a4b5c6d" },
  "status": "active",
  "appliesTo": [ { "system": "bayanihan:initiative-category", "code": "fun-run" } ],
  "team": "Logistics",
  "after": [ { "reference": "Practice/9e8d7c6b-5a4f-4e3d-8c2b-1a0f9e8d7c6b" } ],
  "source": "own",
  "lesson": [ { "text": "Ask the barangay a month ahead. It took three weeks last time.", "author": { "reference": "Person/4f5e6d7c-8b9a-4c0d-9e1f-2a3b4c5d6e7f" }, "time": "2026-03-10T20:00:00+08:00" } ],
  "observed": {
    "included": 3, "ofProjects": 3, "addedLate": 1,
    "dayFromStart": { "median": -21, "earliest": -30, "latest": -4 },
    "lastSeen": "2026-03-07T05:00:00+08:00",
    "basis": [
      { "reference": "Initiative/0a1b2c3d-4e5f-4a6b-8c7d-8e9f0a1b2c3d" },
      { "reference": "Initiative/1b2c3d4e-5f6a-4b7c-9d8e-9f0a1b2c3d4e" },
      { "reference": "Initiative/2c3d4e5f-6a7b-4c8d-8e9f-0a1b2c3d4e5f" }
    ],
    "calculated": "2026-03-10T20:00:00+08:00"
  }
}
```

```json
{
  "resourceType": "Task",
  "id": "6c7d8e9f-0a1b-4c2d-9e3f-4a5b6c7d8e9f",
  "meta": { "version": 2 },
  "intent": "plan",
  "status": "ready",
  "title": "Barangay permit for the 2027 run",
  "practice": { "reference": "Practice/5b6c7d8e-9f0a-4b1c-8d2e-3f4a5b6c7d8e" },
  "partOf": { "reference": "Initiative/3d4e5f6a-7b8c-4d9e-8f0a-1b2c3d4e5f6a" },
  "team": { "reference": "Team/7d8e9f0a-1b2c-4d3e-8f4a-5b6c7d8e9f0a" },
  "owner": { "reference": "Team/7d8e9f0a-1b2c-4d3e-8f4a-5b6c7d8e9f0a" }
}
```

With the run 30 days away and this Task still `ready`, the rule says it is usually done by now (median 21 days
before), and the app shows the lesson beside it.

**Not in v0.1.** The organization-wide view built from all of a group's Practices (it follows from these records and
needs no new resource), loose ends inside a live project's notes, and comparing Practices across groups.

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
| Signed records | The group's home server or hub signs each completed record automatically (see "Recorded when done"), so anyone can check it without trusting any server | **v0, on the cloud server and on phone hubs** |
| Public anchoring | Periodically publish one combined fingerprint (a Merkle root) of confirmed records, so later tampering can be proven. Maps to CEP's `anchorUri`. Never publishes the records themselves. | Designed; built after the pilot |
| Verifiable credentials | A Person's contribution record can be issued as W3C Verifiable Credentials they hold and anyone can verify | Designed; built after the pilot |
| Portable personal records | A Person's records can move between BIX servers with them, as Bluesky's AT Protocol does for posts | Export now (rule 18); moving between servers later |

Personal data is never anchored, signed into anything public, or made impossible to delete.

### A person's own key (in v0.1 since 2026-10-30), and statements a host signs (proposed for v0.2)

Two gaps stood between the records and contributions that are truly portable. **The person's own key moved into v0.1 on 2026-10-30**, so pilot phones have keys from the start and members can join a group's online server later without codes. Host-signed statements stay proposed for v0.2.

**1. A person's own key.** Today a person is an account on one server, so nothing proves that "Mia" on a group's hub and "Mia" on the Dasig Ecosystem are the same person. Groups sign work, but no one signs as the person.

- Each phone creates a key pair for its person the first time Dasig opens. The private key never leaves the phone (or the person's chosen backup).
- `Person.publicKey[]` entries are {`kid` (first 16 hex of the key's SHA-256), `alg`: `Ed25519`, `key` (hex), `created`, `status`: `active` · `revoked`}. Only the person may add or change them; a server refuses anyone else, officers included.
- Pairing with a server as a Person that has keys needs proof: the phone signs the server's one-time challenge (for hub pairing, the pairing code), bound to the person and the server, so a signature can't be replayed elsewhere.
- `Person.publicKey[]` lists the person's current keys. A new phone adds a key, signed by an existing one; a lost phone's key is marked revoked.
- Linking accounts is a `Provenance` with activity `claim-identity`, signed with the person's key, naming both `Person` records. Each server accepts it only from the key holder. Records are never merged; a person's story shows both, each with its group's signature.
- Verifiable Credentials for contributions are issued **to** this key, so the person can show them anywhere without asking any server.

**2. Statements a host signs.** A group can write anything in `Organization.registration[]`, so the field alone proves nothing. When a host checks something, it signs a statement instead:

- A host attestation is a `Provenance` with activity `confirm`, a `verifier` agent that is the host's `Endpoint`, the target (e.g. `Organization/…/_history/3`, the version checked), what was checked (`bayanihan:attestation` codes: `registration-reviewed`, `contact-confirmed`, `carried-over`), and the host's signature.
- The group cannot edit or delete it. A host withdraws an attestation with a later `Provenance` of activity `cancel`.
- Any app shows the badge only when the signature checks against the host's published key, so a badge can't be copied to another server.
- `carried-over` records that a host accepted another system's check (for the Dasig Ecosystem: verification already done by Dasig Fundraising), naming that system as `onBehalfOf`.

Hosts also **publish each group's public signing key** in their directory, so work a hub signed stays checkable after the hub's phone is lost.

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

**Today.** BIX is a draft developed and maintained by Dasig Inc., shaped by the organizations taking part in co-design. Changes that came from conversations are recorded in the change log, citing how many groups they came from. Groups that shape it are credited as contributors, with their permission. Nothing more formal exists yet, and this section says only what exists.

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
| 2026-10-27 | Decisions and voting: `Decision` and `Vote` (from Popolo, with methods from Loomio), outcomes calculated by Core, eligibility fixed at opening, no model voting, a decided Decision can approve a Task, open ballots only in v0.1. |
| 2026-10-27 | From the onboarding walk (`docs/architecture/ONBOARDING_FLOW.md`): `Team.participant.status` (asked to lead or join is `requested` until accepted); `Organization.kind` adds `community` and `event-team`. |
| 2026-10-27 | Organization structure: `Position` (from Popolo Post), `Role.position` with terms, elections as Decisions, saved structures, and common starting structures by kind of group (not legal advice). Teams confirmed as per project, with optional standing teams. |
| 2026-10-27 | Volunteers belong to the structure: `volunteer` as a Team participant role, a suggested path volunteer → member → lead (never automatic), derived project credits, `Person.credit` naming preference, past volunteers asked back first. |
| 2026-10-27 | How volunteers take part: `Task.participant[]` (owner and helpers working together, all credited), joining a team creates a volunteer Role, any team participant may propose work, and a table of who may change what on a Task. |
| 2026-10-28 | Files, home servers and hubs: Attachments stored by the group's own server (S3-compatible, self-hostable); outside links allowed and labelled; one home server per Organization; an organization hub on a dedicated phone or tablet, designed now and built after v0. |
| 2026-10-28 | Recorded when done: completed work counts immediately; review only for money, beneficiaries, or work a group chooses to review; records signed automatically by the group's server or hub; copied to each participant's device; tamper-evident; published by the person's choice; claiming only through the group. |
| 2026-10-28 | Privacy and safety in v0.1: account deletion with grace period and unnamed work kept by groups, removing never erases work, blocking, revocable links that can clear their drafts, `Attachment.showsMinors`, opt-in message sharing for Bayani, seeing your data. |
| 2026-10-28 | Content every page has: `description` and `attachment[]` (reference material) on Organization, Team, Initiative, Task, Need, Offer, Decision, Report and Position; Task outputs kept separate; Decision options carry several attachments. |
| 2026-10-28 | Who it's for and shared goals: `cause[]` with SDG codes, `Group` (from FHIR) for who is served as counts, `Goal` (from FHIR) for shared community targets, `Initiative.contributesTo[]`, calculated goal progress, small-number hiding in public views, sensitive characteristics as counts only. |
| 2026-10-28 | Publish as you are: public project summaries, optional tagging, "who's working on what, for whom, where" from Bayanihan Server, self-synchronising without forced links, goal enrollment accepted by the goal's owner, default `bayanihan:cause` and `bayanihan:population` value sets mapped to the SDGs. |
| 2026-10-28 | Audit fill-ins: `Signature` on Provenance, `Endpoint` and `Organization.homeServer`, person-level `Consent`, `Follow`, wider `Offer.matchedTo` and `Communication.recipient`, `Task.due`, more Organization kinds, `Organization.vocabulary[]`, public summaries for Organizations, saving teams back on wrap-up. |
| 2026-10-28 | One person, many groups: permissions resolved per owning Organization; personal Initiatives (`person` instead of `organization`); one story across groups with separate signatures. |
| 2026-10-28 | `Task.team`: the Team a Task belongs to, kept when its owner becomes a person (found while building the app). |
| 2026-10-29 | Standalone phone and phone hub moved into v0: Bayanihan Server runs inside the Dasig app on the phone's own storage; other phones pair by QR over the hub's hotspot. |
| 2026-10-29 | `Offer.partOf` and `Decision.partOf` (the project they belong to), so permissions resolve from the owning group. Found while building. |
| 2026-10-29 | `Person.description`: a line about yourself, set only by the person. |
| 2026-10-29 | Signing on phone hubs built in v0 (it was listed as after v0). Proposed for v0.2: a person-held key (`Person.publicKey[]`, `claim-identity` signed by the person) and host-signed attestations for verification, with published group keys. |
| 2026-10-30 | A person's own key moved into v0.1: `Person.publicKey[]`, set only by the person; pairing as a Person with keys needs a signed challenge. Built in Core (`generatePersonKey`, `signChallenge`, `verifyChallenge`), the server and the app (Android Keystore through expo-secure-store). |
| 2026-10-31 | Named the steward: BIX is developed and maintained by Dasig Inc. ("Contribution, governance and modules"). No change to the direction of shared governance. |
| 2026-11-06 | Core team and volunteers made explicit (`Role.code`). "Seeing other committees' work": members see the projects they're on, volunteers their own teams; `Team.visibility` (`initiative` · `team`) and the `view.organization` permission let a group widen or narrow it. Built in Core (`seesWithinGroup`). |
| 2026-11-09 | Shifts, showing up and time: `Task.slots` (shift places, fill any open place, backups), `Task.participant.attended` (check-in), `participant.period` (own hours, used by `sum-task-hours`), `participant.replaces` (swap to a named person), `Task.restriction.arrival` (call time and meeting point), `Person.skill[]` (self-declared). Deferred: credentials, emergency contact, guardian consent. |
| 2026-11-11 | Proposed edits and assistance: new `ChangeProposal` resource (an edit to an existing record, as JSON Patch operations against a known `meta.version`, with `includes[]` for drafts accepted together, `area` and `reason`; becomes `outdated` if the target changes first), `Organization.assist[]` (per-group opt-in areas from the new `bayanihan:assist-area` value set, for model and rule-based assistance alike). Rule 3 now says a model never edits an existing record directly; new rules 20–22. |
| 2026-11-11 | Value sets: figure rule `count-participants` (distinct people on done work, optionally only those checked in) and report figure `people-served` (a count, recorded on the work). For the event report. |
| 2026-11-11 | Planned and given time: `Task.estimate` and `TaskDefinition.step.estimate` (planned, per person or per task), `Task.participant.hours` {value, source: planned · stated · measured}; `sum-task-hours` counts period, then hours, then the shift window, then the estimate, and never `executionPeriod`. |
| 2026-11-12 | Lifecycles: a `completed`, `failed` or `cancelled` Task may be reopened to `ready` or `in-progress`, with `task.assign`, recorded as Provenance activity `reopen`. Earlier versions, signatures and proofs stay as they were; hours and credit count only while `completed`. |
| 2026-11-13 | Seeing other committees' work: volunteers also see the other Teams in the projects they're on (the Team record only, not its Tasks), so they can ask to join one; a Team with `visibility: team` stays hidden. Joining a Team: anyone in the group may add only themselves to `Team.participant` as `requested`, cancel it, or leave (`ended`); a lead, or with no lead the core team, accepts. Only `active` participants count as being on a record for editing. |
| 2026-11-13 | Usernames and invitations: `Person.handle` (optional, unique per server), the `Invitation` resource and lifecycle (one invitation to one person, accepted only by them; email never in a record), `Task.taking` (`anyone` · `ask`), `Organization.invitePolicy` (`core-team` · `members`), Provenance activity `invite`, and six privacy rules. |
| 2026-11-13 | Project memory: new `Practice` resource (one kind of step as the group does it, with `observed` figures calculated by rule from completed projects, `after[]`, `lesson[]`, `source`), `Task.practice` and `InitiativeTemplate.action[].practice` for step identity, the `memory` assistance area, `bayanihan:practice-source`, closing a project. New rules 23–25; rule 21 now covers Practice figures. |
| 2026-11-14 | One memory for the whole group: Practice figures are calculated only by the group's home server or hub (rule 23); who sees Practices inside a group (rule 26: core team and `view.organization`, others through steps they can see); a model reads only what its person can see. |
| 2026-11-14 | Suggestions and their answers: Provenance `agent.model` gains `question`, `confidence` and `edited`, and rule agents a `rule` name; accept records the person and the suggester; "Not this time" is a declined ChangeProposal; not suggesting again; starter Practices published read-only. |
| 2026-11-16 | `Initiative.note[]` and `Team.note[]` (author, time, text): updates on a project and on a team (committee), the same shape as `Task.note[]`, so people can say how it's going where the work is. Additive |
| 2026-11-21 | Provenance `agent.model.question` gains `same-practice` (already used by apps, now listed) and `step-ideas` (a model's own idea for a step, for a person to add or not; no confidence). Additive |
