---
name: obdcode-uk-dashboard-lamps
description: >-
  Turns a UK number plate and a lit dashboard warning light into a garage-ready
  statement, then a repair-or-sell next step. Does not diagnose, does not
  republish SAE J2012 definitions, and does not invent prices. Use when a UK
  driver gives a UK number plate or registration together with a dashboard
  warning light, oil light, engine management light, EML, MIL, check engine, or
  DPF light, or asks what to tell the garage about a lamp that is on. Do not use
  for VIN lookup, US plates, NHTSA, Carfax, smog checks, or dollar repair quotes.
disable-model-invocation: true
license: CC-BY-4.0 AND Apache-2.0
metadata:
  author: OBDCode UK
  website: https://obdcode.co.uk
---

# UK dashboard lamp to garage card

One job: **UK plate + which lamp is lit** → garage-ready statement → repair or sell. Not a P-code dictionary.

Do not ask if they are driving. Do not diagnose. Do not invent pounds. Load only files linked here.

**Do not use when:** a 17-character VIN, a US plate, NHTSA / Carfax / smog / state inspection, or a USD quote. Refuse and stop.

## Lamps (stable — do not rename)

| # | id | First drive advice |
|---|---|---|
| 1 | `oil-pressure` | **Stop** |
| 2 | `coolant-temp` | **Stop** if **red**; blue cold-engine that goes out is not this id |
| 3 | `brake-system` | **Stop** if parking brake / EPB is off and the lamp stays, or pedal/leak |
| 4 | `airbag-srs` | **Limited** (Red class, not Stop) |
| 5 | `power-steering` | **Stop** only if steering is heavy |
| 6 | `engine-steady` | Drive with care |
| 7 | `engine-flashing` | **Stop** — spoken flashing of cell **6**, no second drawing |
| 8 | `battery-charging` | **Stop** on ICE if heavy steering, rising temp, or belt noise; EV 12V is Limited |
| 9 | `dpf` | Limited on diesel; petrol/hybrid pick of 9 = path `unmatched-gpf` (not DPF, not pick-again) |
| 10 | `tyre-pressure` | Inflate / investigate |
| 11 | `abs` | Drive with care — brakes still work |
| 12 | `esc-traction` | Skid-lines only |
| 13 | `glow-plug` | Not a fault if it went out after start; stays/flashes = garage, **never treat as 7** |

Paths, not ids 14+: `unmatched-gpf` · `unmatched-adblue` · `unmatched-ev`.

**Board** (MCP `show_dashboard` **requires** `board=`): `petrol` \| `diesel` \| `hybrid` \| `electric` \| `unknown`. Empty args is a fail.

Two different “slugs”: MOT `fusion.matched` slugs are prior notes. `repair_cost` job names are invoice classes. Neither is a diagnosis.

## Steps (this order)

1. **Drive advice now** if they already named a lamp — same turn, even with no plate. Colour does **not** set Stop. Read [drive-advice.md](references/drive-advice.md).
2. **UK plate only.** VIN / non-UK identifier → refuse. Else ask once: send this registration to obdcode.co.uk (DVSA MOT History)? If no, Tier 3. If yes, `POST https://obdcode.co.uk/api/vehicle` `{"reg":"..."}` — never print the plate. Transport miss = 503. Named Stop lamp + outage → still write Stop this turn; omit MOT expiry. Read [vehicle-lookup.md](references/vehicle-lookup.md) and [boards.md](references/boards.md).
3. **If the lamp is unnamed:** classify board from `fuel_type` **and** `fuel_raw`, then `show_dashboard` with that `board`. The tool returns the PNG. Ask which **circled** number matches the lit shape. Do not list names. If they cannot see it, say so; Cursor may open the `file://` preview the tool printed; otherwise last-resort ASCII in [lamp-picker.md](references/lamp-picker.md).
4. **Statement** then **outlook** in the **same turn**. Templates: [output.md](references/output.md). Outlook: [prognosis.md](references/prognosis.md) + the matching card in [prognosis-cards.md](references/prognosis-cards.md). `gbp: null` or unreachable `repair_cost` → we publish no figure. No scanner is promised in stock. No shop link above Stop.
5. **No lamp**, and they named service or modification work: sale-price **band** only — [value-gain.md](references/value-gain.md). No picker, no how-to.

Pass/fail and a second “what part is it?” push: [output.md](references/output.md). Worked turns: [examples.md](references/examples.md).

## Red lines

1. No SAE J2012 wording. A code number is a fact; the definition is not.
2. No driveway repair for oil, hot coolant, hydraulic brakes, airbags, flashing engine.
3. Never clear a lamp as a fix. Never forced DPF regen with a scan tool.
4. Plate is personal data: POST body only, never URL / log / commit / speech.
5. Do not quote MOT certificate text. History = fusion slug + date + type + **Source: DVSA MOT History, Crown copyright.**
6. Never invent pounds for repair, sell, or modification gain.
7. A cost job name is not the failed part. Do not speak invoice-class part names on the first reply.
