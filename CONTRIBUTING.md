# Contributing to BIX

Salamat for helping. BIX is a young, draft format, shaped with the volunteer groups in the Dasig pilot. Comments
from people who build systems, who run groups, or who know other standards (FHIR, Open Referral, schema.org) all make
it better.

By taking part you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## Ways to help

- **Read the spec and say what's unclear.** [`spec/BIX_v0.1.md`](spec/BIX_v0.1.md). An issue saying "I read this
  three times and still don't know what `Task.claim` means" is a real contribution.
- **Tell us what the format can't express.** A situation from a real group (described with made-up names) that BIX has
  no place for.
- **Fix the schemas or validators,** or the descriptions inside them.
- **Build something on BIX** and tell us where it hurt.
- **Pick up an issue** labelled [`good first issue`](https://github.com/Dasig-org/bix/labels/good%20first%20issue) or
  [`help wanted`](https://github.com/Dasig-org/bix/labels/help%20wanted).

## Before you start

- **Small fixes** (typos, broken links, a wrong description): open a pull request straight away.
- **Anything that changes the format** (a new element, a new resource, a changed meaning): open an issue first with the
  "BIX spec change" template, and wait until a maintainer agrees on the approach. Format changes affect every app
  built on BIX, so they're decided in the open, and the reason goes in the spec's decision log.
- **To work on an issue,** comment on it so it can be assigned to you. If there's no news after two weeks, it goes
  back to the pool so someone else can take it. No hard feelings.

## Set up

You need Node.js 22 and Python 3.

```sh
git clone https://github.com/<you>/bix.git     # your fork
cd bix
npm install
```

## How the pieces fit

The schemas are **generated**, so don't edit `schemas/*.json` by hand.

| To change | Edit | Then run |
|---|---|---|
| A resource, an element or its description | `RES` in [`tools/build_schemas.py`](tools/build_schemas.py) | `python3 tools/build_schemas.py` |
| The compiled validators | nothing to edit | `node tools/build_validators.mjs` |
| The meaning, rules or examples | [`spec/BIX_v0.1.md`](spec/BIX_v0.1.md) | |

Commit the regenerated `schemas/` with your change. A format change also needs:

1. the spec text updated in the same pull request,
2. an entry in [`CHANGELOG.md`](CHANGELOG.md): what changed, why, and what implementers need to do,
3. a line in the spec's decision log,
4. examples with **fictional** groups and people only.

## Rules the format keeps

- **Plain language.** Element descriptions are read by people building apps for volunteers. Short sentences.
- **Privacy by design.** People served are counts, never names. Small numbers are hidden in public summaries. Photos of
  children never leave the group. Changes that weaken this won't be merged.
- **Never break existing records in v0.1.** Add, don't rename or remove. Breaking changes wait for v0.2.
- **"BIX" is never a code value or namespace** inside records (it's also IATA's Baggage Information eXchange). Use
  `bayanihan:` or a full URL.

## Open a pull request

1. Branch from `main` in your fork: `git switch -c fix-task-claim-description`.
2. Keep it to one change. Two unrelated fixes are two pull requests.
3. Fill in the pull request template: what, why, and how you checked it.

## What happens next

- A maintainer reviews it, usually **within a week**. Only maintainers can merge; every change to `main` needs an
  approving review.
- You may be asked for changes. That's normal, not a rejection.
- We squash-merge, so your pull request becomes one commit on `main`, and you're credited in it and in the changelog.

## Your contribution's licence

By contributing you agree that your contribution is licensed under this repository's licences: spec text under
**CC BY 4.0** ([`LICENSE-spec`](LICENSE-spec)), everything else under **Apache-2.0** ([`LICENSE`](LICENSE)).

Sign off each commit (`git commit -s`), which adds a `Signed-off-by:` line. It certifies the
[Developer Certificate of Origin](https://developercertificate.org/): that you wrote the change, or otherwise have the
right to submit it under these licences.

## Questions

[Dasig-org Discussions](https://github.com/orgs/Dasig-org/discussions), or hello@dasig.org. Security and privacy
problems: see [`SECURITY.md`](SECURITY.md), never a public issue.
