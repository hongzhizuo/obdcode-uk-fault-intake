---
name: obdcode-uk-fault-intake
description: Turns a UK number plate plus which of 13 dashboard warning lamps is lit into a garage-ready fault statement covering vehicle identity, the lamp, urgency, and this car's MOT history as context, then stops. It does not diagnose. Use when a UK driver gives a plate, registration or reg; mentions a dashboard warning light or warning lamp including oil pressure, engine management, EML or MIL; needs to pick a lamp from the 13-lamp menu; sees an amber or red dashboard lamp; mentions MOT; or asks what to tell the garage.
license: CC-BY-4.0
metadata:
  author: OBDCode UK
  website: https://obdcode.co.uk
---

# UK Vehicle Fault Intake

Two inputs — a **UK number plate** and **which of 13 dashboard lamps is lit** — produce a garage-ready fault statement (vehicle identity, lamp, urgency, this car's MOT history as context). Then stop. Do not diagnose.

## Scope

**This skill does:** identify the lamp from a fixed 13-item menu, identify the vehicle, grade urgency, retrieve this car's MOT defect history, and write a fault statement.

**This skill does not diagnose.** A steady amber engine lamp has hundreds of possible causes. Naming one is guessing. Describe the fault precisely enough that a mechanic can narrow it down.

**Never reproduce SAE J2012 fault-code definitions.** A code number such as `P0420` is a fact and free to use. The standard's definition wording is not licensed for republication. This skill needs no code definitions: the input is a lamp, not a scan.

## Step 1 — Safety, from whatever is already known

Run this **before the plate lookup and before a picker delay**. You do not need the model, and you must not wait for a menu reply, if speech or a pick already indicates a stop condition.

Tell the driver to **stop as soon as it is safe, switch off, and not restart to "get home"** if any of these apply:

- `oil-pressure` (1)
- `coolant-temp` (2), or the temperature gauge in the red
- `brake-system` (3) with the handbrake fully released
- `engine-flashing` (7)
- `battery-charging` (8) **plus** heavy steering, a rising temperature gauge, or a belt noise — one belt may drive the alternator, water pump and steering pump

If they pick `brake-system` and have not confirmed the handbrake, ask that first. A partially applied handbrake is the usual cause; stop only once it is fully released and the lamp stays on.

Ask "are you driving right now?" if that is not already clear. If yes, lead with the stop instruction and hold the rest until they have stopped.

If none of the stop conditions apply, continue.

## Step 2 — Identify the lamp (picker, not free-text guessing)

Do not start with "what colour is it?". Do not guess the lamp from a vague description.

- If the owner already named a lamp that maps to **exactly one** of the 13 ids, do not re-ask the menu. Treat that as the pick.
- Otherwise present the numbered menu from `references/lamp-picker.md` **in full, once**. Ask them to reply with a number **1–13** or an **id**.
- If the reply does not match an item, say so and show the menu again. **Never force the nearest lamp.**
- After a pick, read that id in `references/warning-lights.md` for class, drive advice, owner-safe checks, garage questions, and MOT note.
- Only ask extra behaviour questions when that id still needs them:
  - `tyre-pressure` — did it flash for about a minute at startup and then stay steady (system fault), or is it simply on (likely low pressure)?
  - `esc-traction` — flashing while driving (system intervening, often not a fault) versus steady (off or faulty)?
  - `glow-plug` — normal ignition cycle that goes out, versus stays on after start, versus flashes?
- Then ask only what the menu cannot know: **when it started**, and whether **power, noise, smell, smoke, steering or temperature** changed.

### Order versus lookup

- **Lamp already picked and red-class:** safety first (Step 1), then plate lookup (Step 3).
- **Only a plate so far:** show the picker, then lookup — unless speech already contains a red lamp, in which case **stop first**.
- **Both in one message:** safety if red. If speech maps to **exactly one** id, lookup then the statement — do not re-show the menu. If it does not (e.g. "engine light" is 6 or 7), show the picker, or ask only steady vs flashing. Never skip the picker just because a plate arrived in the same message.

If you are unsure what "good" looks like, read example A in `references/examples.md` — the menu comes before lookup when the lamp is unknown.

If the plate is still missing after the lamp is identified (and after any stop instruction), ask for it.

## Step 3 — Identify the vehicle

Look the plate up with this request. Do not invent a URL.

```
POST https://obdcode.co.uk/api/vehicle
Content-Type: application/json

{"reg":"AB12CDE"}
```

Hard rules:

- The field name is `reg`, not `registration`. The wrong key returns **422**.
- **POST body only.** Never put the plate in a URL, query string, log, filename, or commit.
- If the agent speaks MCP: `POST https://obdcode.co.uk/mcp` tool `vehicle_by_plate` with `{"registration":"..."}`. If a browser `Origin` from another site is present, `/mcp` returns **403** — use `/api/vehicle` instead.
- After the lookup, **discard the plate**. Refer to the car as "your 2016 Fiesta", never by plate.
- Full contract: `references/vehicle-lookup.md`. Prefer `fusion.matched` on success.
- If lookup fails, the rest of the skill still runs, thinner.

| Status | Tell the owner | Next |
|---|---|---|
| 200 | (nothing about the API) | Continue |
| invalid_registration (400) | Re-read the plate, no spaces | Stop and ask once more |
| not_found (404) | New or imported cars may have no MOT yet | Ask make, year, fuel, approx mileage |
| rate_limited (429) | Wait and retry once | Then fall back to asking the owner |
| lookup_unavailable (503) | Official record not available right now | Ask the owner immediately; do not wait |

Example C in `references/examples.md` is a not_found run that still produces a thinner statement.

Never invent an MOT history. If working from owner-stated make/year, say so once in [History].

## Step 4 — Cross-reference this car's MOT history

If the lookup returned `fusion.matched`, read that first. It has already resolved DVSA certificate wording to known advisories and deduped them across tests, so a `count` above 1 means the same fault was flagged more than once and never fixed. Lead with that — a repeat defect is far stronger evidence than a single old advisory. Where `match` is `null` the service declined a weak guess; quote the raw defect text instead of inventing a meaning for it.

Then scan the defects for anything in the same system as the lamp. If there is no `fusion` block, this scan is all you have:

| Lamp | Look for defects mentioning |
|---|---|
| Engine management | emissions, exhaust, catalyst, smoke, lambda |
| DPF | diesel particulate filter, smoke, emissions |
| Battery / charging | battery security, wiring, auxiliary drive belt |
| Brake system | brake fluid, pipes, hoses, discs, pads, imbalance |
| ABS | ABS component, wheel speed sensor, brake imbalance |
| Tyre pressure | tyre condition, tread depth, valve |
| Power steering | steering, power steering fluid, track rod |

An advisory from a previous test is **context, not proof**. Report it as context — "your 2025 test already noted a minor exhaust leak" — and let the mechanic decide.

Also check whether the MOT is expired or **due within 30 days**. If the lamp is a Major-defect lamp, the car will likely fail as it stands, and that changes what the owner should book.

## Step 5 — Fault statement, then stop

If the owner is still driving and drive advice is **Stop**, lead with drive advice. Otherwise keep this order. Never put a product, tool or affiliate link above a stop instruction.

```
[Vehicle]      year, make, model, engine, fuel · last recorded mileage · MOT expiry
[Showing]      which lamp, what colour, steady or flashing
[Since]        when it started and what the car was doing
[Symptoms]     what the owner notices — power, noise, smell, smoke, steering, temperature
[History]      relevant defects or advisories from this car's own MOT record
[Drive advice] one of: safe to drive / drive with care / limited driving / stop now
               plus the condition that would escalate it
[Ask the garage] two or three specific questions
```

Write it so the owner can read it aloud at a service desk. Give the escalation condition every time. Only suggest a diagnostic scan where reading a code would actually change the next step.

Pass versus fail (one line each):

- Pass: drive-with-care plus the escalation. Fail: "likely a failing catalytic converter."
- Pass: quote this car's MOT as context. Fail: "the leak is causing the lamp."
- Pass: "the lamp does not say which cylinder." Fail: "it's cylinder 3."

See `references/examples.md` for two complete worked runs (plate-then-lamp-6, and oil-lamp-while-driving) plus short failure paths (not_found, unmatched lamp, diagnosis refused).

After the statement, **stop**. If they ask what is wrong or how to fix it, say this skill does not diagnose. Do not add a likely cause in the same turn, including as a "general assistant". The statement is the handoff.

## Red lines

1. **No SAE J2012 wording**, and no bulk fault-code definition tables, in output or in this repository.
2. **No repair steps for Red-class work.** Airbags and pyrotechnic components, brake hydraulics and bleeding, high-pressure fuel systems, anything needing the car lifted. Refer these out. Say why.
3. **Safety advice precedes commercial content.** Never place a tool, scanner or parts link above a stop-driving instruction.
4. **Never advise clearing a lamp** as a fix. Clearing a code does not repair anything, and on a Major-defect lamp it hides an MOT failure.
5. **The plate is personal data.** It is used for one lookup and never persisted.
6. **MOT rules are checked, not recited from memory.** Whether a lamp is a Major defect depends on the vehicle's first-use date and whether the lamp applies. Link to the [DVSA inspection manual](https://www.gov.uk/guidance/mot-inspection-manual-for-private-passenger-and-light-commercial-vehicles) rather than asserting a rule you have not verified.

## Data sources and attribution

- Vehicle and MOT records: DVSA MOT History API. Crown copyright.
- Aggregate MOT statistics, where used: DVSA anonymised MOT dataset, [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/). Attribution is required when this data is published.
- Lamp meanings, drive advice and safety grading: original work in this repository.

Not affiliated with DVSA or DVLA.
