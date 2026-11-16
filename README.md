# BIX · Bayanihan Information Exchange

**An open format for the everyday work of volunteer groups and civic organizations.**

> **Early and open.** BIX v0.1 is a draft, shaped with the volunteer groups in the Dasig pilot. Expect changes, and
> please argue with it: comments on the spec are welcome as [issues](https://github.com/Dasig-org/bix/issues/new/choose).

## Why a shared format

A barangay can have five groups running feeding programmes on the same street, each with its own spreadsheet and
group chat, none of them able to see that the others are short of rice or have three spare volunteers. When a
coordinator steps down, the plan goes with them. When a group reports to its parish, its national body or a donor,
someone retypes everything.

Health systems solved a version of this with [HL7® FHIR®](https://hl7.org/fhir/): a shared format, so records can move
between systems without retyping. **BIX does the same for civic work.** Any app that speaks BIX can read a group's
projects, steps and records, and a group can take its history with it when it changes apps.

## What it describes

People and their roles, the projects groups run, the teams that run them, the steps anyone can take, what a project
needs and what others offer, decisions made together, how each kind of step has gone across a group's projects (its
memory), and a signed record of who did the work.

| Area | Resources |
|---|---|
| People and groups | `Person`, `Organization`, `Role`, `Position`, `Group`, `Invitation` |
| The work | `Initiative` (plan, program, project, session), `Team`, `Task`, `TaskDefinition`, `InitiativeTemplate`, `Goal` |
| Needs and offers | `Need`, `Offer`, `Location` |
| Deciding together | `Decision`, `Vote`, `ChangeProposal` |
| Record and memory | `Provenance` (who did what, and who confirmed it), `Practice` (project memory), `Report` |
| Sharing and consent | `SharingPolicy`, `ShareLink`, `Consent`, `Follow`, `Communication`, `Endpoint` |
| Exchange | `Bundle` (sync and transactions) |

A volunteer says they can't come on Saturday but has two sacks of rice for the feeding. In BIX that's an `Offer`
matched to the project's `Need`, and a `Task` for someone to receive it:

```json
{
  "resourceType": "Offer",
  "status": "draft",
  "offeredBy": { "reference": "Person/3c9a…volunteer" },
  "category": { "system": "bayanihan:category", "code": "goods.food.rice" },
  "quantity": { "value": 2, "unit": "sack" },
  "location": { "display": "Parish hall", "psgc": "<barangay code>" },
  "matchedTo": { "reference": "Need/1d77…saturday-rice" }
}
```

The full worked example is in the spec, under "Worked example: a volunteer can't come, and offers rice instead".

## Design choices

- **Privacy by design.** People served are counts, never names. Small numbers are hidden in public summaries. Photos of
  children never leave the group.
- **Offline first.** Phones work without internet and sync later. Conflicts follow clear rules: the first valid
  claim wins, a stale change is refused and shown to the person, never silently merged.
- **Signed records.** Finished work is signed by the group (Ed25519), so anyone can check who did what, and the record
  goes with the volunteer.
- **Built for a small model.** BIX keeps the structure and the rules, so the AI working with it can be small enough for
  a phone. A model only proposes: new records as drafts, edits as a `ChangeProposal`, which a person accepts. A group's
  memory is structured too: each kind of step is a `Practice`, whose figures are calculated by rule.
- **FHIR's patterns where they fit.** Resources, references, Bundles and REST, so people who know FHIR feel at home.

## What's here

| Path | What |
|---|---|
| [`spec/BIX_v0.1.md`](spec/BIX_v0.1.md) | The specification. Part A is a conversation guide for co-designing with groups; Part B is the technical v0.1. |
| [`schemas/`](schemas) | JSON Schemas (2020-12) for every resource, a Bundle, and `all.json` |
| `schemas/validators.js` | Validators compiled ahead of time, so they run anywhere JavaScript runs, including phones (no `eval`) |
| [`tools/`](tools) | The generators for the schemas and validators |
| [`CHANGELOG.md`](CHANGELOG.md) | What changed, why, and what implementers need to do |

Schemas are published at `https://bix.dasig.org/v0.1/`.

## Use it

It isn't on npm yet. Until then, clone this repository beside your project and point to it:

```sh
git clone https://github.com/Dasig-org/bix.git
cd bix && npm install
```

```jsonc
// your package.json
"dependencies": { "@bayanihan/bix": "file:../bix" }
```

```js
import { Task } from "@bayanihan/bix/validators";
if (!Task(record)) console.log(Task.errors);
```

Once published, it will be `npm install @bayanihan/bix`. Any language with a JSON Schema 2020-12 validator can use
the schemas directly.

**Building something on BIX?** You don't have to start from zero:
[Bayanihan Core and Server](https://github.com/Dasig-org/bayanihan) implement the rules and the API, and the
[Dasig app](https://github.com/Dasig-org/dasig-app) is the reference app.

## Get involved

- **Read the spec and open an issue** where it's wrong, unclear or missing something. Use the "BIX spec change"
  template.
- **Tell us what your group does that BIX can't say,** with made-up names.
- **Pick up an issue** labelled [`good first issue`](https://github.com/Dasig-org/bix/labels/good%20first%20issue) or
  [`help wanted`](https://github.com/Dasig-org/bix/labels/help%20wanted).
- **Questions:** [Dasig-org Discussions](https://github.com/orgs/Dasig-org/discussions).

Read [`CONTRIBUTING.md`](CONTRIBUTING.md) before your first pull request. Everyone taking part follows the
[Code of Conduct](CODE_OF_CONDUCT.md).

## Status

**v0.1 is a draft.** Additions that don't break existing records land in v0.1 and are listed in
[`CHANGELOG.md`](CHANGELOG.md), newest first; breaking changes wait for v0.2. The full decision log is at the end of
the spec.

**Latest (2026-11-16):** updates on a project and a team (`Initiative.note[]`, `Team.note[]`), the same shape as
`Task.note[]`.

**Name:** always write "Bayanihan Information Exchange" before "BIX" on first use. "BIX" is also IATA's Baggage
Information eXchange, so `bix` is never used as a code value or namespace inside records; use `bayanihan:` or a full
URL.

## Part of Bayanihan

BIX is the foundation of [Bayanihan, an open initiative by Dasig](https://bayanihan.dasig.org):
**BIX** (the open format) · [Bayanihan Core and Server](https://github.com/Dasig-org/bayanihan) (rules and storage) ·
[Bayani](https://github.com/Dasig-org/bayani) (a small on-phone model) · [Dasig](https://github.com/Dasig-org/dasig-app)
(the app).

## Licence

- The specification text (`spec/`): **CC BY 4.0**, see [`LICENSE-spec`](LICENSE-spec).
- Schemas, validators and tools: **Apache-2.0**, see [`LICENSE`](LICENSE).

Inspired by HL7® FHIR®. FHIR® is the registered trademark of HL7 and is used with the permission of HL7. BIX is not
affiliated with or endorsed by HL7.

Maintained by Dasig Inc. Questions: hello@dasig.org. Security and privacy problems: [`SECURITY.md`](SECURITY.md).
