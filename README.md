# BIX · Bayanihan Information Exchange

The open language for the everyday work of volunteer clubs and nonprofits: people and their roles, the efforts they run, what those efforts need, what others offer, the steps that get the work done, and proof of who did each step and who confirmed it.

Inspired by HL7® FHIR®. FHIR® is the registered trademark of HL7 and is used with the permission of HL7. BIX is not affiliated with or endorsed by HL7.

- **Spec:** [`spec/BIX_v0.1.md`](spec/BIX_v0.1.md). Part A is the conversation guide for organizations; Part B is the technical v0.1.
- **Coming in this folder:** JSON Schemas. The engine that follows them is **Bayanihan Core**, a separate package (see `apps/bayanihan/`).

**Name.** Always write "Bayanihan Information Exchange" before "BIX". "BIX" is also IATA's Baggage Information eXchange and the ISO 639-3 code for Bijori. For the same reason, `bix` is never used as a code value or namespace inside records; use `bayanihan:` or a full URL.

**Licence:** permissive (MIT or Apache-2.0, picked before publishing). Decided 2026-10-26.
