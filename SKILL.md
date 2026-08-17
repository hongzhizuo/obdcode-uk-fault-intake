---
name: obdcode-uk-fault-intake
description: UK car outlook (愈后): plate plus a lit dashboard lamp become a garage-ready fault statement, then a repair-or-sell outlook — close it yourself only when a small OBD device or owner-safe action can, garage approximate cost when a workshop can, repair cost and how to get a sell bid when the outlook is weak. Does not diagnose. When they have no lamp and are modifying, servicing, or presenting the car, state only the sale-price effect of that work and point them to a vehicle card on obdcode.co.uk — no how-to. When the owner gives a plate and has not picked a lamp, look the vehicle up first, classify petrol/diesel/hybrid/electric from fuel_type and fuel_raw, then open that still dashboard PNG (MCP show_dashboard with required board= then open_resource on the file:// preview) and ask which circled number on the picture is lit — do not list lamp names. Do not ask if they are driving. Use when a UK driver gives a plate, registration or reg; mentions a dashboard warning light; needs to pick a lamp from the dashboard cluster picture; mentions MOT; asks repair or sell, worth fixing, diagnostic or repair cost; asks wrap, remap, service history, cambelt, clutch, vehicle card, or what a modification does to sale price; or asks what to tell the garage.
license: CC-BY-4.0
metadata:
  author: OBDCode UK
  website: https://obdcode.co.uk
---

# UK vehicle outlook (愈后)

OBDCode is an **outlook** skill: what happens after the lamp, or after work on the car — not a fault-code dictionary.

**Path A — lamp on.** Plate + which lamp is lit → garage-ready fault statement → **repair or sell** (`references/prognosis.md`). Then stop diagnosing.

**Path B — no lamp.** They are modifying, servicing, or presenting the car → **sale-price effect only** (`references/value-gain.md`). No dashboard picker. No how-to.

**Both.** Statement + outlook first (safety). Then a separate **[Value]** block for the work they named.

They are using this skill on a computer or a phone. Do **not** ask if they are driving. Do **not** hold lookup, the picture, or the statement for a "have you stopped" confirmation. Stop / recovery belongs in **[Drive advice]**, not as a flow lock.

The lamp menu is a fixed set of 13 ids. The **picture** depends on the car. Numbers stay global — 9 is always DPF even when a petrol board leaves that slot empty. 7 is not a second drawing: one engine cell is **6**, flashing is spoken (**7**). Classify the board from the plate lookup (`references/boards.md`) before showing a PNG.

## Scope

**This skill does:** identify the vehicle (including fuel), show the matching lamp board, identify the lamp, grade urgency, retrieve this car's MOT defect history as context, write a fault statement, then give a repair-or-sell outlook. With no lamp, it states only what the named work usually does to sale price.

**This skill does not diagnose.** A steady amber engine lamp has hundreds of possible causes. Naming one is guessing. A cost slug is not a diagnosis.

**Never reproduce SAE J2012 fault-code definitions.** A code number such as `P0420` is a fact. The standard's definition wording is not licensed for republication.

### Entry

- Plate or lamp / warning light / MOT / garage card → Path A (Steps 1–6).
- Wrap, wheels, exhaust, remap, paint, PPF, service, cambelt, clutch, tyres, vehicle card, “does this add value?” and **no** lamp → Path B (Step 7 only). Lookup the plate if they gave one, for year/make/model in the value line — still no picker.
- “Is it worth repairing?” after a lamp → Path A through Step 6.

## Step 1 — Drive advice lives in the statement

Do not gate Steps 2–6 on whether they have parked.

When you write **[Drive advice]**, use **Stop** (do not drive it in; arrange recovery) for:

- `oil-pressure` (1)
- `coolant-temp` (2) when the lamp is **red** (not the blue cold-engine twin — ask colour if they named a thermometer)
- `brake-system` (3) only if the parking brake / EPB / Auto Hold is fully off and the lamp stays on, **or** they already reported a spongy pedal, a pull, or a leak
- `engine-flashing` (7)
- `battery-charging` (8) **plus** heavy steering, a rising temperature gauge, or a belt noise — skip the belt combo on an electric car

`safety_class: Red` is not Stop. Airbag is Red and **Limited**. Power steering is Stop only if the steering has gone heavy.

If they pick `brake-system` and have not mentioned the parking brake, ask whether it is fully off. That is classification, not a driving quiz.

## Step 2 — Identify the lamp (show the cluster picture, do not describe it)

Owners match **shapes**, not names. A list of "oil-can / engine-block outline" is a fail.

- If speech maps to **exactly one** id, treat that as the pick — except the specials below.
- **Engine family** ("engine light", EML, MIL, check engine): ask only **steady or flashing**. Do not open the cluster unless they are unsure. Flashing → 7. Do not treat a bare 6 as steady until they have said it is not flashing.
- **Thermometer / coolant / temp light:** ask **blue or red** before id 2. Blue after a short run that then goes out is engine-cold, not a fault.
- **AdBlue / urea / DEF:** not on any picture. Do not map to 9 or 6. Unmatched AdBlue path in `references/boards.md`.
- **Petrol or hybrid + exhaust-dots / "particulate filter" / pick of 9:** unmatched GPF. Do not run diesel DPF copy. Do not switch board.
- **Electric + turtle / tortoise / limited power / car-with-! and no skid lines / charge plug / HV on-screen text:** unmatched EV. Do not pick 12 or 8. Do not open the ICE unknown board.
- Otherwise follow `references/lamp-picker.md`. Look the plate up first if you do not yet know the fuel. Call `show_dashboard` with **required** `board=`. Empty args is a fail. Then `open_resource` the `file://` preview **in the same turn**. If the picture did not open, say so. Do not list names. Do not ask for a number.
- Ask for the **circled number on the matching shape**, not a left-to-right count. Empty grey slots are not on this car.
- Off-board number (9 on petrol, 1 on electric): **keep the same board**. Say that number is not printed. Ask them to read the circle on the shape that is lit. Widen to `unknown` only if they say **none of these shapes**. Never shrink toward electric on owner talk. Never force the nearest lamp.
- After a valid pick: one sentence to confirm the shape. Skip `show_lamp` unless they hesitate. Give **drive advice in that same turn**. Then one optional "anything feel different?" Default since/symptoms to "just now / drives normally" if they do not add more.
- Extra behaviour questions only when needed:
  - `tyre-pressure` — flash-then-steady at startup (system) vs simply on (likely low pressure)
  - `esc-traction` — flashing (intervening) vs steady (off or faulty)
  - `glow-plug` — went out after start (**not a fault**, no garage card, no Step 6) vs stays on vs flashes
- 12 is skid-lines only.

### Order versus lookup

- **Only a plate, and they are asking about a lamp or have not said they are modifying:** look it up now (Step 3). Do not print the plate. Classify from `fuel_type` **and** `fuel_raw` (`references/boards.md`). Then show that PNG.
- **Only a plate, and they named modification / service / value:** Step 7. No PNG.
- **Lookup 404:** ask make, year, fuel, mileage. Then the matching board. Do not show unknown first. Never default electric.
- **Lookup 503 / 429 after retry:** ask fuel. Matching board if they know; `unknown` only if they do not. Never default electric.
- **Both in one message:** unique id → skip picker (except the specials). Engine family → steady vs flashing. Else lookup then the matching board.
- **No plate, lamp unnamed:** ask plate or fuel. Do not open the unknown 13-lamp picture as the first screen.
- **Named lamp, no plate:** write the lamp + drive advice. Ask plate (or make/year/fuel) for MOT history. Do not gate the advice on the plate.

Example A in `references/examples.md` is lookup then the matching board, not a name list.

## Step 3 — Identify the vehicle

```
POST https://obdcode.co.uk/api/vehicle
Content-Type: application/json

{"reg":"<the plate from this turn — do not print it>"}
```

Hard rules:

- The field name is `reg`, not `registration`. The wrong key returns **422**.
- **POST body only.** Never put the plate in a URL, query string, log, filename, commit, or spoken reply.
- If the agent speaks MCP: `POST https://obdcode.co.uk/mcp` tool `vehicle_by_plate` with `{"registration":"..."}`. A foreign `Origin` on `/mcp` is **403** — use `/api/vehicle`.
- They already typed the plate. Do not ask consent again. Do not echo it. Refer to "your 2016 Fiesta". The chat still holds it; "discard" is output hygiene, not deletion.
- Full contract: `references/vehicle-lookup.md`. Prefer `fusion.matched` on success. If the lamp is still unknown, show the matching board in this step.
- Classify with `fuel_raw`, not `fuel_type` alone. Hybrid + missing raw → `unknown` (or ask petrol vs diesel hybrid). Hybrid + diesel / Electric Diesel / heavy oil → diesel board. Never upgrade `fuel_type=diesel` to hybrid from a marketing name.
- If lookup fails, the rest still runs, thinner.

| Status | Tell the owner | Next |
|---|---|---|
| 200 | (nothing about the API) | Continue |
| invalid_registration (400) | That registration was not accepted. Type it again with no spaces. | Do not repeat the value |
| not_found (404) | New or imported cars may have no MOT yet | Ask make, year, fuel, mileage, then the matching board |
| rate_limited (429) | Wait and retry once | Then ask the owner |
| lookup_unavailable (503) | Official record not available right now | Ask fuel immediately |

Never invent an MOT history. If working from owner-stated make/year, say so once in [History].

## Step 4 — This car's MOT history (context, not a cause)

`fusion.matched` `count` above 1 means the **same slug appeared on more than one certificate**. It does not mean "never fixed" and it is not evidence that today's lamp is that fault.

Do not substring-scan raw defect text for `smoke` / `steering` / `valve`. If fusion exists, include a slug only when it is on the same-system allowlist for this lamp. Quote date and `type`. No causal verbs (`causing`, `explains`, `related fault`).

| Lamp | Allowlist family |
|---|---|
| Engine management | emissions, exhaust, catalyst, lambda (not a diagnosis) |
| DPF | diesel particulate filter |
| Battery / charging | battery security, auxiliary drive belt |
| Brake system | brake fluid, pipes, hoses, discs, pads |
| ABS | ABS, wheel speed sensor |
| Tyre pressure | tyre condition, tread, valve |
| Power steering | steering, power steering fluid |

Every History line that names a prior note must end: **this does not show the cause of today's lamp.** If nothing in-family, one negative line is enough. Do not dump unrelated fusion slugs into speech.

**MOT outcome talk is gated on `first_used` + fuel**, not copied from `warning-lights.md`:

- Engine MIL as a listed fail item: petrol cars first used on or after 1 July 2003; diesel (including diesel hybrid) on or after 1 July 2008. Pure EV: do not call the engine lamp an MOT fail item.
- TPMS as a listed fail item: M1 first used on or after 1 January 2012, and only a **malfunction** (often flash-then-steady), not a lamp that only means inflate the tyre.
- Never say "Expect a fail" or "will likely fail as it stands." In scope: the tester may record a Major if the lamp still indicates a malfunction — check the [DVSA inspection manual](https://www.gov.uk/guidance/mot-inspection-manual-for-private-passenger-and-light-commercial-vehicles). Out of scope: this lamp is not an automatic fail item on this car.

If MOT is expired or due within 30 days, add an owner booking line in the statement, not a verdict.

## Step 5 — Fault statement

Spoken card first (~60–80 words). Same facts as a written hand-over, without ids, fusion slugs, or URLs.

```
[Vehicle]      year, make, model, engine, fuel · mileage · MOT expiry
[Showing]      lamp in plain English, colour, steady or flashing
[Since]        when it started (one line; merge with symptoms if short)
[History]      same-system MOT notes only, or one negative line
[Drive advice] safe to drive / drive with care / limited driving / stop now
               + escalation
               Stop → do not drive it in; ask the garage to collect, or call recovery
               Limited → they may drive directly there, no extra journeys
[Ask the garage] readings or process rules, not a parts shortlist
[Book]         only if MOT expired, due within 30 days, or an in-scope Major lamp
```

Pass versus fail:

- Pass: drive-with-care plus the escalation. Fail: "likely a failing catalytic converter."
- Pass: quote this car's MOT as prior notes. Fail: "the leak is causing the lamp."
- Pass: "the lamp does not say which cylinder." Fail: "it's cylinder 3."
- Pass: restating recovery / scan / keep-driving from the statement. Fail: naming a likely part.
- Pass: "read the freeze frame before replacing anything." Fail: "sensor, reluctor, or wiring" / "soot-loaded or ash-loaded."

Owner facts (how long the lamp was on) go in **[Since]** or a **Tell the garage** line, not as questions to the mechanic.

Not-a-fault endings (glow 13 went out, blue thermometer that went out, parking-brake brake lamp, ESC flashing while driving) **skip Step 6**.

Otherwise continue to Step 6 in the **same turn** as the statement.

## Step 6 — Repair or sell (outlook)

Read `references/prognosis.md` and the matching card in `references/prognosis-cards.md`. Do not diagnose.

The owner hears one of three buckets:

1. **Close it yourself** — outlook is good **and** either an owner-safe action or a **small OBD device** (on the shelf at obdcode.co.uk, or one they already own) changes the next step. Then tell them how to close it. Green inflate / AdBlue top-up / one handbook DPF regen count. Red-class work never does. A reader does not fix oil, hot coolant, hydraulic brakes, airbags, or a flashing engine lamp. Do not clear codes. Do not force a DPF regen with a scan tool.
2. **Garage, cost in range** — a workshop can usually put it right. Call `repair_cost` with a slug **on that lamp’s allowlist**. Say the headline if verified. `gbp: null` means we publish **no** figure — two written estimates, not a guess.
3. **Weak outlook** — the job may be large, and a repair often leaves a car that is hard to sell. Give **repair** (verified or no figure) **and** **sell**: we publish no used-car price; get one bid as it sits and compare it with the estimate. Recovery is part of sell cost when **[Drive advice]** is Stop.

Spoken outlook (~40–60 words) after the statement:

```
[Outlook]  Close it yourself / A garage can usually handle this / Repair may cost more than the car
[Repair]   repair_cost headline, or: we publish no figure — two written estimates
[Sell]     weak outlook only — get a bid as it sits; do not invent pounds
[Close it] close-it-yourself only — driveway or scan steps
```

Call `repair_cost` via `POST https://obdcode.co.uk/mcp` tool `repair_cost` `{"job":"<slug>"}`. Never pick a slug because it is the only one with a number. Never treat a cost page as the failed part.

Device and shop links stay **below** Stop / recovery. Scanner category may be off the shelf — link `https://obdcode.co.uk/guides/best-obd2-scanner-uk/` and `https://obdcode.co.uk/tools/scanners/` as how to choose, not as a fake SKU.

After the outlook: if they ask what is wrong, this skill does not diagnose. If they ask recovery, a scan, keep-driving, or repair-vs-sell, **restate [Drive advice] and [Outlook]**. Do not say "continue as a normal assistant" to the owner.

## Step 7 — Sale-price effect (no lamp, or extra work)

Read `references/value-gain.md`. Skill mode states **only** the price effect of the named work. No wrap/remap/delete how-to. No invented “adds £800.”

```
[Value]   band: Strong / Modest / Little-mixed / Negative — typical buyer reaction, not a valuation
[Record]  date, mileage, invoice they paid, on a vehicle card at obdcode.co.uk
```

Illegal or MOT-hostile work (DPF/GPF/cat delete, emissions cheat) is **Negative**. Do not instruct. Documented cambelt / wet belt / clutch / service history is usually **Strong**. Cosmetic wrap / wheels / stereo is usually **Little / mixed**.

`repair_cost` may describe a **job** they asked about (cambelt, clutch). It still does not become a **gain** in pounds.

## Red lines

1. **No SAE J2012 wording**, and no bulk fault-code definition tables, in output or in this repository.
2. **No repair steps for Red-class work.** Airbags and pyrotechnic components, brake hydraulics and bleeding, high-pressure fuel systems, anything needing the car lifted. Refer these out. Say why.
3. **Safety advice precedes commercial content.** Never place a tool, scanner or parts link above a stop-driving instruction in the statement.
4. **Never advise clearing a lamp** as a fix.
5. **The plate is personal data.** Do not print, file, URL, or commit it.
6. **MOT rules are gated on first-use and fuel**, then linked to the DVSA manual — not recited as "Expect a fail."
7. **Never invent pounds** for repair, sell, or modification gain. `gbp: null` and a missing used-car API are answers.
8. **A cost slug is not a diagnosis.** Do not call clutch or cat cost because an engine lamp is on unless that card allows it as “if later invoiced.”
9. **No how-to for wrap, remap, filter delete, or lift.** Step 7 is price effect only.
10. **Close-it-yourself never covers Red-class work.** Oil, hot coolant, hydraulic brakes, airbags, flashing engine: outlook may be sell; it is not a driveway job.

## Data sources and attribution

- Vehicle and MOT records: DVSA MOT History API. Crown copyright.
- Aggregate MOT statistics, where used: DVSA anonymised MOT dataset, [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/). Attribution is required when this data is published.
- Lamp meanings, drive advice, safety grading, repair-or-sell outlook, and sale-price bands: original work in this repository.
- Repair planning figures: `repair_cost` on obdcode.co.uk, only where a named dated UK source exists.
- Lamp pictograms: Material Design Icons (Apache-2.0, Pictogrammers) plus original OBDCode UK drawings for oil-pressure, DPF and glow-plug. Not ISO 2575 official artwork. Sources in `assets/svg/`.

Not affiliated with DVSA or DVLA.
