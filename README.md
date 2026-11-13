# BIX · Bayanihan Information Exchange

> **Private preview.** The three repos aren't on npm yet, so they're used side by side. Clone all three into one folder:
>
> ```sh
> mkdir dasig && cd dasig
> git clone https://github.com/Dasig-org/bix.git
> git clone https://github.com/Dasig-org/bayanihan.git
> git clone https://github.com/Dasig-org/dasig-app.git
> ```
>
> Then `npm install` inside `bayanihan/`, and inside `dasig-app/app/`. Please don't share the code outside the preview yet.

An open format for the everyday work of volunteer groups and civic organizations: people and their roles, the projects they run, the teams that run them, the steps anyone can take, what a project needs and what others offer, decisions made together, how each kind of step has gone across a group's projects (its memory), and a signed record of who did the work.

Inspired by HL7® FHIR®. FHIR® is the registered trademark of HL7 and is used with the permission of HL7. BIX is not affiliated with or endorsed by HL7.

## What's here

| Path | What |
|---|---|
| [`spec/BIX_v0.1.md`](spec/BIX_v0.1.md) | The specification. Part A is a conversation guide for co-designing with groups; Part B is the technical v0.1. |
| `schemas/` | JSON Schemas (2020-12) for every resource, a Bundle, and `all.json` |
| `schemas/validators.js` | Validators compiled ahead of time, so they run anywhere JavaScript runs, including phones (no `eval`) |
| `tools/` | The generators for the schemas and validators |

Schemas are published at `https://bix.dasig.org/v0.1/`.

## Use it

```sh
npm install @bayanihan/bix
```
```js
import { Task } from "@bayanihan/bix/validators";
if (!Task(record)) console.log(Task.errors);
```

The reference engine and server are [Bayanihan Core and Bayanihan Server](https://github.com/Dasig-org/bayanihan). The first app built on BIX is [Dasig](https://github.com/Dasig-org/dasig-app).

## Built for a small model

BIX keeps the structure and the rules, so the AI working with it can be small enough for a phone. A model only proposes: new records as drafts, and edits to existing ones as a `ChangeProposal`, which a person accepts. A group's memory is structured too: each kind of step is a `Practice`, whose figures (how often it was needed, when it was done, how often it was forgotten) are calculated by rule from finished projects. The model's part is the judgment rules can't make, such as whether two steps are the same. Spec sections: "Proposed edits and assistance" and "Project memory: Practices".

## Status

**v0.1 is a draft**, shaped with the groups taking part in the pilot. Expect changes; the change log at the end of the spec records them.

**Name:** always write "Bayanihan Information Exchange" before "BIX" on first use. "BIX" is also IATA's Baggage Information eXchange, so `bix` is never used as a code value or namespace inside records; use `bayanihan:` or a full URL.

## Licence

- The specification text (`spec/`): **CC BY 4.0**, see [`LICENSE-spec`](LICENSE-spec).
- Schemas, validators and tools: **Apache-2.0**, see [`LICENSE`](LICENSE).

Maintained by Dasig Inc. Questions: hello@dasig.org.
