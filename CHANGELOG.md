# Changelog

BIX is versioned by its spec (`v0.1`, `v0.2`). While v0.1 is a draft, additions that don't break existing records
land in v0.1 and are listed here. The full decision log is at the end of `spec/BIX_v0.1.md`.

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

- **2026-11-13 · Joining teams.** Volunteers now see the other Teams in the projects they're on (the Team record only:
  name, lead, who's on it; never the team's Tasks), so they can ask to join one. Anyone in the group may add only
  themselves to `Team.participant` as `requested`, cancel that, or leave (`ended`); the team's lead accepts, or the
  core team when there's no lead. A `requested` or `ended` participant no longer counts as being on a record for
  editing. A Team with `visibility: team` stays hidden.
- **2026-11-12 · Reopening a Task.** `completed`, `failed` and `cancelled` were final. Real work gets reopened (a
  website marked done too early, a cancelled shift brought back), so they may now go to `ready`, or `in-progress`
  when people stay on it. Reopening needs `task.assign`. Earlier versions, signatures and proofs are unchanged and
  still verify; hours and credit count only while the Task is `completed`.
