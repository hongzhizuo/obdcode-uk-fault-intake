# Vehicle lookup

A UK number plate can resolve to make, model, fuel, first-use date, MOT expiry, and MOT test history. This file is the **vehicle** lookup. Lamp identification is [lamp-picker.md](lamp-picker.md).

This skill is **UK plates only**. A 17-character VIN, a US plate, or a NHTSA / Carfax / smog request: refuse, explain this is UK MOT only, and **stop**. Do not 400-retry a VIN as a plate.

## Consent (before the first POST)

Typing a plate into chat is not consent to send it to a third party.

Ask once, in plain English: you will send this registration to obdcode.co.uk, which looks up MOT History at DVSA; the plate is personal data; shall I look it up?

- If they already said “look this plate up” / “check MOT” / “yes”, that is consent.
- If they say no: Tier 3 (ask make, year, fuel, mileage). Do not POST.
- Do not claim the thread has discarded the plate. The chat still holds it.

Controller for the hosted lookup is the operator of obdcode.co.uk. Recipients: that host, then DVSA. This skill cannot delete copies from Cursor logs or the host.

## Privacy after consent

- Field name on `POST /api/vehicle` is `reg`, not `registration`. Wrong key → 422.
- **POST body only.** Never put the plate in a URL, query string, log, filename, commit, or spoken reply.
- Refer to “your 2016 Fiesta”, never by plate.
- For 400: “That registration was not accepted. Type it again with no spaces.” Never repeat the value.
- Prefer `/api/vehicle`. Do not call `/api/v1/mot` (FastAPI `detail[].input` can echo the plate).
- If the agent speaks MCP: `POST https://obdcode.co.uk/mcp` tool `vehicle_by_plate` with `{"registration":"..."}`. A foreign `Origin` on `/mcp` is **403** — treat as 503 and use `/api/vehicle`, or fall back to Tier 3. Do not retry a 403 in a loop.

## Tier 1 — Hosted lookup (no key)

```
POST https://obdcode.co.uk/api/vehicle
Content-Type: application/json

{"reg":"<the plate — do not print it>"}
```

No account. Daily DVSA ceiling is shared. Do not burst plates.

### Status

| Status | Tell the owner | Next |
|---|---|---|
| 200 | (nothing about the API) | Continue. Prefer `fusion.matched`. Classify board from `fuel_type` **and** `fuel_raw`. |
| invalid_registration (400) | That registration was not accepted. Type it again with no spaces. | Do not repeat the value. If it is a VIN, refuse UK-only and stop. |
| not_found (404) | New or imported cars may have no MOT yet | Ask make, year, fuel, mileage, then the matching board **if the lamp is still unknown** |
| rate_limited (429) | Wait and retry once | Then Tier 3. Do not delay a named Stop lamp for a retry |
| lookup_unavailable (503) | Official record not available right now | Tier 3. Named Stop lamp: write Stop **this turn**; omit MOT expiry |

Map **any transport miss** (timeout, 502/504, DNS, empty body, MCP 403 Origin) to **503**. Do not hang the statement.

A DVSA 429 arrives as **503**. A 429 means *this client* was too fast.

Never invent MOT history. If working from owner-stated make/year, say so once in [History].

## repair_cost (same host, not a diagnosis)

Call only with a job name from the allowlist in [prognosis.md](prognosis.md) for **this lamp**.

```
POST https://obdcode.co.uk/mcp
{"jsonrpc":"2.0","id":1,"method":"tools/call",
 "params":{"name":"repair_cost","arguments":{"job":"<slug>"}}}
```

- `gbp: null` / `no_verified_price` → that is the answer.
- Unreachable (timeout, 5xx, 403) → speak **we publish no figure**. Do not invent. Skipping the tool because it failed is allowed; inventing pounds is not.
- Do not call `fault_code`. This skill does not diagnose from codes.
- Do not call `decode_mot_advisory` in order to quote certificate wording.
- Do not call `model_mot_stats` as a stand-in for this car’s history.

There is no sell-price or modification-gain tool.

## Tier 2 — Do not collect DVSA credentials in this chat

Do not ask the owner for MOT History API client secrets. If hosted lookup is down, use Tier 3. Operators who run their own DVSA integration do that **outside** this skill.

## Tier 3 — Ask the owner

Make, model, year, fuel, mileage. Say once that you could not pull the MOT record. Carry on thinner.

## Response shape (abridged)

The plate appears nowhere in a success body. Do not quote `defects[].text`. Use `fusion.matched` slugs only.

```json
{
  "vehicle": {
    "make": "FORD", "model": "FIESTA",
    "fuel_type": "petrol", "fuel_raw": "Petrol",
    "year": 2016, "engine_cc": "998",
    "mot_due": "2027-03-01", "first_used": "2016-03-14"
  },
  "fusion": {
    "matched": [{"slug": "brake-pads-wearing-thin", "count": 1, "latest": "2026-03-02"}],
    "unmatched_count": 1, "threshold": 0.75, "enabled": true
  },
  "sources": {"dvsa": true}
}
```

`fuel_type` is `petrol` / `diesel` / `hybrid` / `electric` / `unknown`. Classify the picture from **both** fields ([boards.md](boards.md)).

`fusion.matched` count > 1 means the same MOT slug appeared on more than one certificate — a prior note, not proof of today’s lamp.

If `match` is null, skip that defect. Do **not** quote raw certificate `text`.

## History speech

Same-system allowlist (include a slug only if it is in-family for this lamp):

| Lamp / path | Allowlist family |
|---|---|
| Engine management | emissions, exhaust, catalyst, lambda (not a diagnosis) |
| DPF | diesel particulate filter |
| Battery / charging | battery security, auxiliary drive belt |
| Brake system | brake fluid, pipes, hoses, discs, pads |
| ABS | ABS, wheel speed sensor |
| Tyre pressure | tyre condition, tread, valve |
| Power steering | steering, power steering fluid |

Quote **slug, date, type** only. End with: **Source: DVSA MOT History, Crown copyright. This does not show the cause of today’s lamp.**

If nothing in-family, one negative line is enough.

## Terms

Vehicle and MOT records are Crown copyright. State the source when displaying them. This skill does not relicense Crown records as CC-BY-4.0.

Aggregate MOT statistics behind `model_mot_stats` are OGL v3.0. This skill should not quote them on the spoken card.
