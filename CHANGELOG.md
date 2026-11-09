# Changelog

BIX is versioned by its spec (`v0.1`, `v0.2`). While v0.1 is a draft, additions that don't break existing records
land in v0.1 and are listed here. The full decision log is at the end of `spec/BIX_v0.1.md`.

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
