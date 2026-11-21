# Changelog

BIX is versioned by its spec (`v0.1`, `v0.2`). While v0.1 is a draft, additions that don't break existing records
land in v0.1 and are listed here. The full decision log is at the end of `spec/BIX_v0.1.md`.

## v0.1, 2026-11-21: two more suggestion questions

No new resource types or elements. `Provenance.agent.model.question` (spec, "Suggestions and their answers") accepts
two more values, nothing changed or removed:

| Value | What the model was asked |
|---|---|
| `same-practice` | Is this step already in the plan under another name? (Apps already asked it; it wasn't listed.) |
| `step-ideas` | What steps might this project still need? The model's own idea, not one of the group's usual steps |

A `step-ideas` suggestion carries no `confidence`: it's an idea for a person to judge, and a person always commits it.
Why: a new group has no past projects for project memory to learn from, so Bayani suggests steps from the project's
own details, and the group's measure of suggestions (accepted, edited, declined, per question) should count these
separately.

For implementers: regenerate from `tools/build_schemas.py`; a server that keeps only known questions should add both.

## v0.1, 2026-11-16: updates on a project and a team

No new resource types. Two new elements on existing ones, nothing changed or removed:

| Element | On | What it is |
|---|---|---|
| `note[]` {`author`, `time`, `text`} | `Initiative` | Updates on a project: how it's going, said where the work is |
| `note[]` {`author`, `time`, `text`} | `Team` | Updates inside a team (committee) |

`Task.note[]` has had this shape since 2026-10-27; the three are now defined once in the schemas, with descriptions.

How it behaves (spec, "Content every page has" → "Updates on a record"):

- **Who may add one:** whoever may edit the record. No new permission.
- **Who sees it:** whoever can see the record. Never in a public summary.
- **Append-only**, oldest first, so two people adding at once both succeed. A correction is a new note.
- **Not a message.** `Communication` is still how you write *to* people about a record, with recipients and replies.
  A note is an update *on* the record.

Why: a group's photos, files and words about a project should live with the project, not in a chat somewhere else.
Tasks had notes; projects and teams had files (`attachment[]`) and a description, but nowhere to say how it's going.
The project report in the Dasig app now quotes the latest updates, and a team's page shows them.

For implementers:

- Schemas changed: `Initiative.schema.json`, `Team.schema.json` (new property), `Task.schema.json` (descriptions
  only), `all.json`, `validators.js`. Regenerate with `python3 tools/build_schemas.py`.
- Compatibility: additive. Records without `note[]` are unchanged. A server still on the earlier schemas refuses an
  Initiative or Team that carries `note[]` (resources don't accept unknown elements), so update servers before
  clients start writing it; a client should tell the person the update didn't save rather than drop it.
- FHIR: the same idea as `Annotation` on `Task`, `CarePlan` and `CareTeam`.

## v0.1, 2026-11-14: one memory for the whole group

Changed rules, no new elements:

- Rule 23: a Practice's `observed` figures are calculated only by the group's home Bayanihan Server, or its hub phone
  when it runs without one, so a phone holding part of the group's work never produces different figures. Other
  devices receive them.
- Rule 26 (new): inside a group, the core team and anyone with `view.organization` see all Practices and their
  lessons; anyone else sees a Practice only through a step they can see that points to it. A model reads only what its
  person can see.

Why: Bayani runs on each member's phone, but the memory is the group's records. These two rules make every member's
Bayani work from the same memory without showing anyone more than they could open themselves. See spec section
"Project memory: Practices", "One memory for the whole group".

## v0.1, 2026-11-13: project memory (Practices)

Added, all optional, so existing records stay valid:

- `Practice`, a new resource: one kind of step as a group does it ("Get the barangay permit"), with `appliesTo[]` (kinds
  of project, as `Initiative.category` codes), the usual `team`, `partOf`, `after[]` (what usually comes before it),
  `source` (`own`, `starter`, `adopted`), `lesson[]` written by people, and `observed` figures calculated by rule from
  the group's completed projects: how many had the step, how many added it late, and the day it was usually done.
  Lifecycle `draft → active → retired`.
- `Task.practice`: the Practice a step is an instance of. `InitiativeTemplate.action[].practice`: the same for a saved
  step, so projects started from a template are linked from the start.
- The `memory` assistance area, and the value set `bayanihan:practice-source`.

Changed rules:

- Rule 21: no proposal may change a Practice's `observed` figures.
- Rule 23: `observed` is calculated by rule, recalculated when a project completes; no person or model sets it.
- Rule 24: `practice` links stay inside the organization; a model only proposes them.
- Rule 25: a Practice names no one but its lesson authors, and shared outside the group it carries neither those nor
  the projects counted.

Why: copying last year's plan carries the steps but not how they went. Practices give a group a memory of each kind
of step that builds up with every finished project, so a coordinator can see what a project usually needs, what is
usually done by now and what usually comes first. Rules do the counting; a small model only matches steps and
judges what applies. See spec section "Project memory: Practices".

## v0.1, 2026-11-11: proposed edits and assistance

Added, all optional, so existing records stay valid:

- `ChangeProposal`, a new resource: a proposed edit to a record that already exists. It names the `target` and the
  version it was made against (`basedOn`), lists the edit as JSON Patch operations (`change[]`: `add`, `remove`,
  `replace`), and can carry new draft records accepted with it (`includes[]`, e.g. the smaller steps of a split).
  Lifecycle: `draft → accepted`, or `declined`, `withdrawn`, `outdated` (set by rule when the target changes first).
- `Organization.assist[]`: the areas where a group turned on assistance, from the new value set
  `bayanihan:assist-area` (`break-down`, `review-plan`, `who-to-ask`, `newcomers`, `roster`, `slipping`,
  `report-draft`). Per group; nothing is on until an officer (`org.manage`) turns it on.

Changed rules:

- Rule 3: a model never edits an existing record directly; it makes a `ChangeProposal`.
- Rule 20: accepting a proposal needs the same permission as making the change directly, and applies it as one change.
- Rule 21: what no proposal may touch (figures, votes and outcomes, attendance, verification, roles, consent, sharing
  policy, provenance, `assist`, other people's Person records), and a proposal never makes a Person a Task's owner.
- Rule 22: a model or an assist rule acts only in an area the group turned on, and every proposal it makes names the
  `area` and gives a `reason`.

Why: BIX could propose new records but not edits to existing ones, so reviewing a plan ("move this step to
Logistics", "this has to happen after that") had no home, and every app, or every model, would invent its own. See
spec section "Proposed edits and assistance".

## v0.1, 2026-11-11: planned and given time

- `Task.estimate {value, unit: min|h, per: person|task}` and `TaskDefinition.step.estimate`: how long work should take.
- `Task.participant.hours {value, source: planned|stated|measured}`: time one person gave, without exact clock times.
- `sum-task-hours` now counts, per person: their `period`, else their `hours`, else the shift's `restriction.period`,
  else the `estimate`. **Changed:** it no longer uses `executionPeriod` (taken → marked done), which overstated hours
  for work done over days and undercounted shifts.

Why: hours are what schools, employers and funders ask for. A coordinator plans them, each person confirms or
changes theirs, and the group's signature stands behind them. See spec section "Planned and given time".

## v0.1, 2026-11-11: report figures

- Figure rule `count-participants` {taskCode, attended}: distinct people on done work.
- Report figure `people-served`: a count recorded as a Task output, never names.

## v0.1, 2026-11-09: shifts, showing up and time

Added, all optional, so existing records stay valid:

- `Task.slots`: how many people the work needs (default 1). Places fill in any order; full work can take backups.
- `Task.participant.attended {at, by}`: the person showed up, recorded by them or a lead.
- `Task.participant.period`: a person's own start and end; hours figures use it when present.
- `Task.participant.replaces`: a proposed swap to a named person, who accepts or declines.
- `Task.restriction.arrival {at, location, note}`: call time and meeting point.
- `Person.skill[]`: skills a person declares themselves.

Why: walking a volunteer-run event end to end showed that shift sign-ups, check-in, per-person hours and swaps had no
home in the format, so every app would invent its own. See spec section "Shifts, showing up and time".

Deferred: signed credentials about a person, an officer-only emergency contact, guardian consent for minors.

- **2026-11-14 · Suggestions and their answers.** Provenance `agent.model` gains `question`, `confidence` (0–1) and
  `edited`; rule agents gain `rule`. A suggestion is a record only once a person answers: accepting records the person
  and the model or rule that suggested it; "Not this time" is a `ChangeProposal` in `declined`, so it isn't suggested
  again. Starter Practices are published read-only and adopted on use.
- **2026-11-13 · Usernames and invitations.** `Person.handle` (optional username, unique on the server holding the
  Person, found only by exact match), a new `Invitation` resource (one invitation to one person, to a group, team,
  project or task; `sent → accepted · declined · expired · withdrawn`; only the invitee accepts; can block future
  ones), `Task.taking` (`anyone` by default, or `ask`: people ask and a lead chooses), and
  `Organization.invitePolicy` (`core-team` by default, or `members`). Provenance activity `invite`. Privacy rules:
  email addresses never appear in a record, inviting by email reveals nothing about whether an account exists, and
  invitation messages carry no detail. Schemas rebuilt from `tools/build_schemas.py` (`reopen` now lives there too).
- **2026-11-13 · Joining teams.** Volunteers now see the other Teams in the projects they're on (the Team record only:
  name, lead, who's on it; never the team's Tasks), so they can ask to join one. Anyone in the group may add only
  themselves to `Team.participant` as `requested`, cancel that, or leave (`ended`); the team's lead accepts, or the
  core team when there's no lead. A `requested` or `ended` participant no longer counts as being on a record for
  editing. A Team with `visibility: team` stays hidden.
- **2026-11-12 · Reopening a Task.** `completed`, `failed` and `cancelled` were final. Real work gets reopened (a
  website marked done too early, a cancelled shift brought back), so they may now go to `ready`, or `in-progress`
  when people stay on it. Reopening needs `task.assign`. Earlier versions, signatures and proofs are unchanged and
  still verify; hours and credit count only while the Task is `completed`.
