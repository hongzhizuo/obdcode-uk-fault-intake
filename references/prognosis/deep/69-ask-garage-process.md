# 69 · Ask the garage = readings / process, not a parts shortlist

Not a second SKILL. If this note disagrees with `SKILL.md`, `references/prognosis.md`, `references/prognosis-cards.md`, or `references/value-gain.md`, those four win. Do not diagnose. Do not invent pounds. Do not add a 14th lamp id.

The Step 5 field **[Ask the garage]** is **readings or process rules**. It is not a candidate-parts menu. Spoken **[Outlook]** / **[Repair]** must not smuggle that same menu through `repair_cost` slugs. Owner-facing copy is **UK English**. Live slug rules: `73-when-to-call-repair-cost.md`. Live outlook scoring: `75-pass-fail-outlook.md`.

## When

Write **[Ask the garage]** on every Path A **real-fault** statement (Step 5), in the same turn as **[Drive advice]**, then Step 6.

Skip the field (and skip Step 6) on not-a-fault endings: glow 13 went out, blue thermometer that went out, parking-brake brake lamp, ESC flashing while driving, key-on bulb check.

Path B with no lamp has no garage card. Do not invent an **[Ask the garage]** parts list for wrap / remap / service.

Do not ask if they are driving. Do not hold the statement for a “have you stopped” confirmation.

## What the field is

From SKILL Step 5:

```
[Ask the garage] readings or process rules, not a parts shortlist
```

A reading is a number or a stored record the workshop takes **before replacing anything**: freeze frame, charging voltage, soot load, differential pressure, which wheel a scan reports, SCR / reagent status.

A process rule is an order of work: read first; do not sell a battery until voltage is known; do not replace on a code alone; ask whether the diagnostic fee comes off the repair.

A parts shortlist is a closed list of failed components (pump / sender / bearing; sensor / reluctor / wiring; soot vs ash; battery vs alternator; lambda / cat / coil). That is a diagnosis. This skill does not diagnose.

Owner facts they already know (how long the lamp was on, noise, last oil change) go in **[Since]**, or as a **Tell the garage** fact line. They are not questions to the mechanic, and they are not a parts fork.

## Spoken field (English)

UK English. Garage / workshop, recovery, freeze frame, handbook, tyre, petrol, colour, MOT. Not CEL, not “auto shop,” not a Chinese gloss, not “prognosis.”

Inside the statement: no ids, no fusion slugs, no URLs, no plates, no cost-slug names.

**Pass sketch** (engine-steady, from `references/examples.md`):

**[Ask the garage]** Read the stored code and the freeze frame before replacing anything. Does the diagnostic fee come off the repair?

**Pass sketch** (diesel DPF):

**[Ask the garage]** Soot load and differential pressure. Not a soot-vs-ash fork.

**Fail sketch:**

**[Ask the garage]** Sensor, reluctor, or wiring. Or the cat. Here’s clutch and converter prices.

## Process lines by path

Use the **left** column in **[Ask the garage]**. The **right** column is a parts shortlist — a fail even when it sounds helpful.

| Path | Ask (readings / process) | Do not ask (parts shortlist) |
|---|---|---|
| `oil-pressure` (1) | Hand over **[Since]** facts: how long it was on, any noise, last oil change. Cold dipstick is information, not a close | Pump, sender, or bearing. DIY switch or pressure-test |
| `coolant-temp` red (2) | **[Since]** facts: climbed or spiked, heater hot or cold, topping-up, steam or sweet smell. Cold tank / floor glance is information | Head gasket, thermostat, water pump as today’s failed part |
| `brake-system` hydraulic (3) | **[Since]** facts: spongy pedal, pull, fluid at a wheel. Recovery, not a driveway bleed | Pads, discs, master cylinder, ABS module as the cause |
| `airbag-srs` (4) | **[Since]** facts: when it started, collision, seat / belt / trim work. No under-seat look | Clock spring, module, under-seat connector as a closed list |
| `power-steering` (5) | **[Since]** facts: heavy both ways or one, whine, whether charging or temperature also changed | Pump, rack, motor, or belt as the named part |
| `engine-steady` (6) | Stored code **and freeze frame** before replacing anything. Diagnostic fee off the repair? | Lambda, cat, coil, clutch. “It’s cylinder 3.” |
| `engine-flashing` (7) | Read the stored code before ordering parts. The lamp does not name the cylinder | Failed cat, misfire on cylinder *n*, coil pack |
| `battery-charging` (8) ICE / hybrid | Charging voltage at idle **and** at raised revs **before any battery is sold** | Battery vs alternator vs belt vs wiring |
| Electric board lamp 8 | 12V / DC-DC health **before** any battery is sold | Traction pack, alternator, belt, “fit a battery” |
| Diesel `dpf` (9) | Soot load and differential pressure, not just a code | Soot-loaded vs ash-loaded; blocked filter; named sensor |
| Unmatched petrol / hybrid GPF | Stored codes and freeze frame. No diesel regen copy | Blocked GPF, soot vs ash, failed cat |
| `tyre-pressure` (10) flash-then-steady | After correct placard pressures: read the system (sensor IDs / status). Do not guess a dead sensor | Dead TPMS sensor, pairing, valve stem as the cause |
| `abs` (11) | Which wheel the scan reports | Sensor, reluctor, or wiring |
| `esc-traction` (12) steady | Whether ABS is also lit; whether it started after a wheel, tyre, or suspension job | Shared wheel-speed sensor as the named part |
| `glow-plug` (13) stays on / flashes | Read engine codes. Do not promise what a code will say | Set of four glow plugs; “it will say glow-plug” |
| AdBlue / urea / DEF | SCR / reagent status, not a parts fork | Injector, NOx, heater, crystals |
| Unmatched EV turtle / HV / charge-plug | A workshop that can **read this electric car**. No ICE scan story | Pack, inverter, DC-DC, lamp 8 or 12 as a forced id |

`tyre-pressure` simply on is Close it yourself (placard inflate). There is no parts ask. Flash-then-steady still checks pressures first, then process at the garage.

## Outlook must not smuggle a parts list via cost slugs

**[Ask the garage]** is the statement. **[Repair]** is planning money. A cost slug is an **invoice class**, not today’s failed part. SKILL red line 8: a cost slug is not a diagnosis.

Smuggling looks like this: you call one or more `repair_cost` jobs, then the owner hears a **menu of parts** — “battery or alternator,” “it’s the cat,” “pads and discs,” “sensor, reluctor, or wiring” — as if the slug list were the shortlist.

| What you called | Pass speech | Fail (smuggled shortlist) |
|---|---|---|
| `car-diagnostic-test-cost` | First invoice is a **scan**. The lamp does not name the part | “The scan will show the lambda / cat / coil.” |
| `car-battery-replacement-cost` and, on ICE, `alternator-replacement-cost` | **If later invoiced** — quote both as planning ranges. **Do not pick** which. Ask voltage / 12V health first | “It’s battery or alternator — here are both prices.” Calling battery because the pictogram is a battery |
| `catalytic-converter-replacement-cost` | **Flashing engine only**, **if the garage later invoices a converter** — weak-outlook upper bound | “You have a failed cat.” Calling it because a **steady** engine lamp is on |
| `head-gasket-repair-cost` | Red coolant, **if invoiced**. Often `gbp: null` — that is the answer | “It’s the head gasket.” |
| `dpf-cleaning-cost` | Call it (often null). Still ask soot load and differential pressure | “It needs a clean / it’s soot not ash” because the slug exists |
| `brake-pads-and-discs-cost` | Only if **they already named** that invoice. Never the cause of a hydraulic Stop lamp | Pads-and-discs as why the red brake lamp is on |
| `clutch-replacement-cost` / belt / chain / wet-belt | Step 7 named job, or they already named a clutch — **not** an engine lamp | Engine outline → clutch or cambelt page “so there is a number” |
| `wheel-bearing-replacement-cost` | Only if **they already named** that job, **if later invoiced** | ABS lamp → bearing |
| Empty allowlist (oil, airbag, PAS, ABS, TPMS, AdBlue, EV turtle) | **Do not call.** We publish no figure for this class of job | Hunting diagnostic-test, clutch, cat, or battery so a parts menu appears |

Never pick a slug because it is the only one with a number. Never put a slug name (`catalytic-converter-replacement-cost`) in **[Ask the garage]**. Never treat a cost page as the failed part.

Calling **both** allowed charging slugs on ICE lamp 8 is required as invoice class. That is **not** permission to say the failed part is battery or alternator. The process line stays: voltage at idle and raised revs **before any battery is sold**.

`gbp: null` is not a gap to fill with a guessed part. Two written estimates. No invented GBP.

## After they ask “so which part?”

This skill does not diagnose. Restate **[Drive advice]** and **[Outlook]**. Restate the **[Ask the garage]** reading. Do not fill the silence with a shortlist. Do not say “continue as a normal assistant.” Do not fetch a neighbour slug to name a part.

## Red lines

1. **[Ask the garage]** is readings / process. Not a parts shortlist. Not a closed “A, B, or C.”
2. Outlook / `repair_cost` must not smuggle that shortlist. Invoice class only, **if later invoiced** where the card says so.
3. Owner facts belong in **[Since]**, not as questions the mechanic must answer, and not as a diagnosis.
4. Never hunt a nearby slug. Empty allowlist = no call = no parts menu.
5. Never invent pounds. Never freeze a headline in this file.
6. UK English on the card. No Chinese. No CEL. No “prognosis.”
7. No SAE J2012 wording. A code number is a fact to hand over, not a named failed part.
8. Never advise clearing the lamp. Never print a plate. Illustrative car: **your 2016 Fiesta** / **your Transit**.
9. Safety before commercial: Stop / recovery above any cost line or shop link.
10. Do not diagnose. If they ask what is wrong, say the lamp does not name the part.

## Pass versus fail

**Pass**

- **[Ask the garage]** “Read the stored code and the freeze frame before replacing anything.”
- “Does the diagnostic fee come off the repair?”
- “Charging voltage at idle and at raised revs before they sell a battery.” / “12V or DC-DC health before any battery is sold.”
- “Soot load and differential pressure. Not a soot-vs-ash fork.”
- “Which wheel the scan reports.”
- “SCR / reagent status, not a parts fork.”
- “The lamp does not name the part” / “does not say which cylinder.”
- **[Repair]** “If the garage later invoices this job, published UK figures are …” — after a live allowlisted `repair_cost` result, not as today’s cause.
- ICE lamp 8: both invoice-class slugs spoken as **if invoiced**; do not pick battery vs alternator.
- Empty allowlist: no `repair_cost`; “we publish no figure for this class of job.”
- Owner facts (how long, noise, last oil) in **[Since]**.
- Restate drive advice, outlook, and the reading if they ask which part, keep-driving, or repair-vs-sell.
- UK English: garage, freeze frame, recovery, tyre, petrol, handbook, MOT.

**Fail**

- “Sensor, reluctor, or wiring.”
- “Soot-loaded or ash-loaded.” / soot-vs-ash as a closed repair path.
- “It’s the clutch / cat / head gasket / alternator / pump / sender / bearing.”
- “Likely a failing catalytic converter.” / “it’s cylinder 3.”
- “Battery or alternator — here are both prices” as the cause of lamp 8.
- Calling `catalytic-converter-replacement-cost` because a **steady** engine lamp is on, or without the **if later invoiced** frame.
- Calling `clutch-replacement-cost` (or a belt slug) because an engine lamp is on.
- Calling pads-and-discs as why a hydraulic Stop lamp is on.
- Calling wheel-bearing because the ABS lamp is on.
- Hunting diagnostic-test / cat / battery on oil, airbag, ABS, TPMS, AdBlue, or EV turtle “so there is a number.”
- Putting slug names or a parts menu in **[Ask the garage]**.
- “About £400–£800” with no tool result, or filling `gbp: null` with a guessed part.
- “Clear it and see.” / promising what a code will say.
- CEL / “auto shop” / 愈后 / “prognosis” on the garage card.
- “Continue as a normal assistant” and then name a part.

**Pass sketch** (illustrative; no live pounds): Your 2016 Fiesta, amber engine outline, steady. Drive with care. Ask the garage to read the stored code and the freeze frame before replacing anything. Outlook: close it yourself with a reader, or a garage diagnostic — published figure only if the live tool returns one. The lamp does not name the part.

**Fail sketch:** Ask them to check the lambda, cat, or coil. Converter replacement is about £500, or the clutch if that is cheaper.
