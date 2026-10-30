"""Generate BIX v0.1 JSON Schemas from one compact definition.
Edit RES below, then run: python3 bix/tools/build_schemas.py
Each resource schema = common Resource elements + its own properties."""
import json, pathlib
OUT = pathlib.Path(__file__).resolve().parent.parent / "schemas"
BASE = "https://bix.dasig.org/v0.1/"
DT = "datatypes.schema.json#/$defs/"
def ref(t): return {"$ref": DT + t}
def arr(x): return {"type": "array", "items": x}
def enum(*v): return {"enum": list(v)}
S = {"type": "string"}; T = ref("dateTime"); R = ref("Reference"); C = ref("Coding"); Q = ref("Quantity"); P = ref("Period"); A = ref("Attachment")
txt = {"type": "string", "maxLength": 4000}
page = {"description": txt, "attachment": arr(A)}           # content every page has
summary = {"publicSummary": {"type": "boolean", "default": True}}
RES = {
 "Person": ({"name": {"type": "object", "properties": {"text": S, "use": enum("nickname", "full")}, "required": ["text"], "additionalProperties": False},
             "photo": A, "contact": arr({"type": "object", "properties": {"system": enum("phone", "email", "messenger", "other"), "value": S}, "required": ["system", "value"], "additionalProperties": False}),
             "managedBy": R, "credit": enum("nickname", "full", "anonymous"), "description": txt,
             # The person's own keys (one per phone). Only the person may add or revoke them; a server never holds the private key.
             "publicKey": arr({"type": "object", "properties": {"kid": S, "alg": enum("Ed25519"), "key": {"type": "string", "pattern": "^[0-9a-f]{64}$"},
                 "created": {"type": "string"}, "status": enum("active", "revoked")}, "required": ["kid", "alg", "key", "status"], "additionalProperties": False})}, ["name"]),
 "Organization": ({"name": S, "kind": enum("registered-npo", "faith-based", "civic-club", "community", "event-team", "sk-council", "school-org", "school", "university", "cooperative", "informal", "lgu-unit", "national-agency", "foundation"),
                   "partOf": R, "registration": arr({"type": "object", "properties": {"system": S, "value": S}, "required": ["value"]}), "image": A,
                   "cause": arr(C), "location": arr(R), "homeServer": R, "vocabulary": arr({"type": "object", "properties": {"term": S, "label": S}, "required": ["term", "label"]}), **page, **summary}, ["name"]),
 "Role": ({"person": R, "organization": R, "code": C, "status": enum("requested", "active", "ended"), "position": R, "period": P,
           "permissions": arr(C), "qualification": arr(C)}, ["person", "organization", "code", "status"]),
 "Position": ({"organization": R, "title": S, "kind": enum("board", "officer", "committee-chair", "other"), "seats": {"type": "integer", "minimum": 1},
               "term": {"type": "string", "description": "ISO 8601 duration, e.g. P1Y"}, "permissions": arr(C), "requiredBy": S, "status": enum("active", "retired"), **page}, ["organization", "title"]),
 "Team": ({"name": S, "organization": R, "initiative": R, "kind": enum("standing", "initiative"), "access": enum("own-tasks", "initiative"),
           "participant": arr({"type": "object", "properties": {"person": R, "role": enum("lead", "member", "volunteer"), "status": enum("requested", "active", "ended"), "period": P}, "required": ["person", "role", "status"], "additionalProperties": False}),
           "status": enum("active", "ended"), **page}, ["name", "organization"]),
 "Location": ({"name": S, "description": S, "psgc": {"type": "string", "pattern": "^[0-9]{9,10}$"}, "position": {"type": "object", "properties": {"lat": {"type": "number"}, "lon": {"type": "number"}}}, "partOf": R}, ["name"]),
 "Initiative": ({"title": S, "kind": enum("plan", "program", "project", "session"), "status": enum("draft", "planned", "active", "completed", "cancelled"),
                 "organization": R, "person": R, "partOf": R, "period": P, "recurrence": ref("Recurrence"), "category": arr(C), "cause": arr(C), "location": arr(R), "image": A,
                 "target": arr({"type": "object", "properties": {"code": C, "value": {"type": "number"}, "unit": S}, "required": ["code", "value"]}),
                 "taskDefinition": arr(R), "partner": arr(R), "servesGroup": arr(R),
                 "contributesTo": arr({"type": "object", "properties": {"goal": R, "status": enum("requested", "accepted", "declined")}, "required": ["goal", "status"]}), **page, **summary}, ["title", "kind", "status"]),
 "InitiativeTemplate": ({"title": S, "organization": R, "version": {"type": "integer", "minimum": 1}, "status": enum("draft", "active", "retired"),
                         "team": arr({"type": "object", "properties": {"name": S, "leadRole": S}, "required": ["name"]}),
                         "action": arr({"type": "object", "properties": {"title": S, "team": S, "taskDefinition": R, "audience": enum("team", "organization", "open"), "offset": S, "partOf": S, "dependsOn": arr(S)}, "required": ["title"]}),
                         "need": arr(Q), "report": arr(C)}, ["title", "organization", "version", "status"]),
 "Group": ({"characteristic": arr(C), "location": R, "quantity": {"type": "integer", "minimum": 0}, "description": S}, ["characteristic"]),
 "Goal": ({"title": S, "owner": R, "cause": arr(C), "servesGroup": arr(R), "location": R, "status": enum("draft", "active", "achieved", "cancelled"),
           "target": arr({"type": "object", "properties": {"figure": C, "value": {"type": "number"}, "due": T}, "required": ["figure", "value"]}), **page}, ["title", "owner", "status"]),
 "Need": ({"initiative": R, "category": C, "quantity": Q, "received": Q, "neededBy": T, "recurrence": ref("Recurrence"), "location": R, "priority": enum("routine", "urgent"),
           "status": enum("draft", "open", "partially-met", "met", "cancelled"), **page}, ["category", "status"]),
 "Offer": ({"offeredBy": R, "partOf": R, "category": C, "quantity": Q, "location": R, "availableFrom": T, "availableUntil": T, "recurrence": ref("Recurrence"), "matchedTo": R,
            "status": enum("draft", "available", "matched", "fulfilled", "expired", "withdrawn"), **page}, ["offeredBy", "category", "status"]),
 "TaskDefinition": ({"title": S, "appliesTo": arr(C), "review": {"type": "boolean", "default": False}, "status": enum("draft", "active", "retired"), "author": R, "ratifiedBy": R,
                     "step": arr({"type": "object", "properties": {"code": S, "dependsOn": arr(S), "requires": arr(C), "evidence": S, "confirmerRole": C, "autoConfirm": {"type": "boolean"}, "involvesMoney": {"type": "boolean"}, "involvesBeneficiaries": {"type": "boolean"}}, "required": ["code"]})}, ["title", "status"]),
 "Task": ({"intent": enum("proposal", "plan", "order"), "status": enum("draft", "ready", "requested", "accepted", "in-progress", "completed", "cancelled", "failed", "on-hold"),
           "code": C, "title": S, "focus": R, "definition": R, "partOf": R, "team": R, "dependsOn": arr(R), "milestone": {"type": "boolean"}, "requester": R, "owner": R,
           "participant": arr({"type": "object", "properties": {"person": R, "role": enum("owner", "helper"), "status": enum("requested", "active", "ended")}, "required": ["person", "role", "status"], "additionalProperties": False}),
           "suggestedFor": arr(R), "reviewer": R, "audience": enum("team", "organization", "open"), "goodFirstStep": {"type": "boolean"},
           "priority": enum("routine", "urgent"), "due": T, "restriction": {"type": "object", "properties": {"period": P, "location": R}}, "requires": arr(C), "executionPeriod": P,
           "checklist": arr({"type": "object", "properties": {"text": S, "done": {"type": "boolean"}, "doneBy": R}, "required": ["text", "done"]}),
           "output": arr({"type": "object", "properties": {"code": C, "value": {}, "unit": S, "attachment": arr(A)}}),
           "note": arr({"type": "object", "properties": {"author": R, "time": T, "text": S}, "required": ["text"]}), "category": arr(C),
           "verification": enum("not-required", "pending", "confirmed", "changes-requested", "disputed"), **page}, ["intent", "status"]),
 "Provenance": ({"target": arr(R), "activity": enum("propose", "create", "update", "claim", "assign", "accept", "decline", "release", "complete", "confirm", "dispute", "cancel", "submit", "return", "acknowledge", "claim-identity", "merge", "vote", "publish", "revoke"),
                 "agent": arr({"type": "object", "properties": {"type": enum("author", "performer", "verifier", "model", "rule"), "who": R, "onBehalfOf": R, "model": {"type": "object", "properties": {"name": S, "version": S}, "required": ["name", "version"]}}, "required": ["type"]}),
                 "occurredAt": T, "recorded": T, "offline": {"type": "boolean"}, "signature": arr(ref("Signature"))}, ["target", "activity", "agent", "occurredAt"]),
 "Communication": ({"about": R, "sender": R, "recipient": arr(R), "payload": {"type": "object", "properties": {"text": S, "attachment": arr(A)}}, "sent": T}, ["about", "sender", "sent"]),
 "ShareLink": ({"target": R, "grants": arr(enum("view", "claim", "join-team", "join-org", "propose", "comment")), "audience": enum("anyone-with-link", "signed-in", "members"),
                "preview": enum("full", "title-only", "generic"), "expires": T, "createdBy": R, "status": enum("active", "revoked"), "blocked": arr(R)}, ["target", "grants", "audience", "createdBy", "status"]),
 "Decision": ({"about": R, "partOf": R, "question": S, "method": enum("approve", "choose-one", "choose-many", "ranked", "consent"),
               "option": arr({"type": "object", "properties": {"id": S, "label": S, "description": S, "attachment": arr(A)}, "required": ["id", "label"]}),
               "voters": R, "eligible": arr(R), "opens": T, "closes": T, "quorum": {"type": "integer", "minimum": 0}, "threshold": enum("majority", "two-thirds", "unanimous", "no-objection"),
               "showResults": enum("after-voting", "after-close"), "status": enum("draft", "open", "closed", "decided", "no-quorum", "cancelled"),
               "outcome": {"type": "object", "properties": {"option": arr(S), "tally": {"type": "object"}, "decidedAt": T}}, "statement": S, **page}, ["question", "method", "status"]),
 "Vote": ({"decision": R, "voter": R, "choice": arr(S), "objection": {"type": "boolean"}, "reason": S, "cast": T}, ["decision", "voter", "cast"]),
 "Report": ({"owedBy": R, "owedTo": R, "period": P, "due": T, "recurrence": ref("Recurrence"), "scope": {"type": "object", "properties": {"initiative": arr(R), "includeParts": {"type": "boolean"}}},
             "figures": arr({"type": "object", "properties": {"code": C, "value": {"type": "number"}, "unit": S, "rule": {"type": "object", "properties": {"code": S, "params": {"type": "object"}}, "required": ["code"]}, "derivedFrom": arr(R), "derivedAt": T}, "required": ["code", "rule"]}),
             "missingParts": arr(R), "narrative": S, "replaces": R, "submittedBy": R,
             "status": enum("owed", "in-preparation", "submitted", "acknowledged", "returned", "cancelled"), **page}, ["owedBy", "owedTo", "period", "status"]),
 "SharingPolicy": ({"organization": R, "rules": arr({"type": "object", "properties": {"category": C, "sharing": ref("Sharing")}, "required": ["sharing"]}), "approvedBy": R, "minorsStayInGroup": {"type": "boolean", "default": True}}, ["organization"]),
 "Consent": ({"person": R, "scope": enum("share-messages-for-bayani", "appear-in-credits", "photo-of-me", "contact-by-group"), "status": enum("active", "withdrawn"), "dateTime": T, "organization": R}, ["person", "scope", "status", "dateTime"]),
 "Endpoint": ({"address": S, "kind": enum("cloud", "hub", "self-hosted"), "publicKey": S, "organization": R, "status": enum("active", "off", "retired")}, ["address", "kind", "status"]),
 "Follow": ({"follower": R, "target": R, "since": T, "status": enum("active", "ended")}, ["follower", "target", "status"]),
}
CAE = {"Person": "Actor", "Organization": "Actor", "Team": "Actor", "Location": "Site", "Initiative": "Instrument", "InitiativeTemplate": "Instrument", "TaskDefinition": "Instrument",
       "SharingPolicy": "Instrument", "Need": "Instrument", "Offer": "Instrument", "Report": "Instrument", "Position": "Instrument", "Goal": "Instrument", "Consent": "Instrument",
       "ShareLink": "Instrument", "Decision": "Instrument", "Vote": "Event", "Task": "Event-when-completed", "Group": "Observable",
       "Role": "relationship", "Communication": "relationship", "Follow": "relationship", "Provenance": "attestation", "Endpoint": "transport"}
ONE_OF = {"Initiative": [{"required": ["organization"]}, {"required": ["person"]}]}
def build(name, props, req):
    extra = {"oneOf": ONE_OF[name]} if name in ONE_OF else {}
    return {**extra, "$schema": "https://json-schema.org/draft/2020-12/schema", "$id": f"{BASE}{name}.schema.json", "title": f"BIX v0.1 {name}",
            "x-bix-cae-kind": CAE[name], "type": "object",
            "allOf": [{"$ref": DT + "Resource"}],
            "properties": {"resourceType": {"const": name}, "id": True, "meta": True, "identifier": True, "sharing": True, "language": True, "extension": True, **props},
            "required": ["resourceType", "id", "meta", *req], "additionalProperties": False}
for n, (props, req) in RES.items():
    (OUT / f"{n}.schema.json").write_text(json.dumps(build(n, props, req), indent=2) + "\n")
bundle = {"$schema": "https://json-schema.org/draft/2020-12/schema", "$id": f"{BASE}Bundle.schema.json", "title": "BIX v0.1 Bundle", "x-bix-cae-kind": "transport", "type": "object",
          "properties": {"resourceType": {"const": "Bundle"}, "id": ref("id"), "type": enum("sync", "transaction", "export"), "timestamp": T,
                         "entry": arr({"type": "object", "properties": {"fullUrl": S, "resource": {"type": "object", "required": ["resourceType"]}}, "required": ["fullUrl", "resource"]})},
          "required": ["resourceType", "id", "type", "entry"], "additionalProperties": False}
(OUT / "Bundle.schema.json").write_text(json.dumps(bundle, indent=2) + "\n")
allfiles = sorted(OUT.glob("*.schema.json"))
(OUT / "all.json").write_text(json.dumps([json.loads(f.read_text()) for f in allfiles], indent=1) + "\n")
print(len(RES) + 1, "schemas written, plus all.json")
import subprocess; subprocess.run(["node", str(pathlib.Path(__file__).parent / "build_validators.mjs")], check=True)
