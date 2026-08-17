# 72 · Unmatched GPF / AdBlue / EV — still Step 6

Not a second SKILL. If this file disagrees with `SKILL.md`, `references/prognosis.md`, `references/prognosis-cards.md`, or `references/boards.md`, those four win. Do not diagnose. Do not invent pounds. Do not print a plate.

The lamp menu is a **fixed set of 13 ids**. GPF, AdBlue, and unmatched EV are **paths**, not a fourteenth id. Do not add `gpf`, `adblue`, or `ev-turtle` to the picker. Do not force the nearest of the 13.

Unmatched is still Path A. Write a **thinner** Step 5 statement, then Step 6 in the **same turn** — unless Step 5 already ended as **not-a-fault**.

---

## When

They described a warning that is **not** one of the 13 circled shapes, **or** they picked an empty ghost slot that this fuel maps to an unmatched path.

| Path | How they get here | Not this |
|---|---|---|
| **Petrol / hybrid GPF** | Exhaust-dots, “particulate filter” on petrol / petrol-hybrid, or **pick of 9** on the petrol or hybrid picture | Diesel pick of 9 (`dpf`). Hybrid + diesel / Electric Diesel / heavy oil in `fuel_raw` (diesel board; 9 is DPF). Electric pick of 9 (empty slot, not GPF). Engine outline 6 / 7 |
| **AdBlue / urea / DEF** | They **say** AdBlue, urea, or DEF (diesel). Not on any picture | Mapping to 9 or 6. Petrol GPF. Diesel DPF regen copy |
| **Unmatched EV** | Turtle / tortoise / limited power; **car-with-!** and **no** skid lines; charge plug; HV on-screen text. Tesla: accept pasted alert text | Lamp **12** (skid-lines). Lamp **8** on the electric board (12V rectangle). Opening the ICE unknown board |

Keep **this** board. Off-board 9 on petrol / hybrid: say it is not printed; ask the circle on the shape that is lit. Widen to `unknown` only if they say **none of these shapes** and they have not already described exhaust-dots. Never shrink toward electric. Never default electric.

Vans: same paths. Say **your Transit**. Not a van board. Downtime is “a day off the road,” not a made-up day-rate.

If they also named wrap / service / value: **[Drive advice]** and this outlook first, then a separate **[Value]** block. A wrap does not close an unmatched warning.

---

## Skip Step 6 (not-a-fault)

Skip outlook only when Step 5 already ended as **not a fault**. Unmatched does **not** by itself skip Step 6.

| Facts | Step 6 |
|---|---|
| GPF / AdBlue / EV **key-on bulb check** that then **went out** | **Skip.** Short “not a fault” note. No garage card |
| Blue / green status (main beam, indicators, cruise, fog, engine-cold blue thermometer) | **Skip.** Name the status function. Ask if any **circled** lamp is also on. Not GPF / AdBlue / EV |
| Glow 13 went out after start; parking-brake brake lamp (pedal normal); ESC flashing while driving | **Skip** on those **13-id** cards. Do not dump them into this file |
| AdBlue **level low**, car **still starts** | **Run** Step 6 — `owner` close (correct fluid). This is a real warning |
| AdBlue **remaining-starts** / will not start | **Run** Step 6 — `poor` |
| GPF still showing (exhaust-dots or petrol 9) | **Run** Step 6 — `device` then `garage` |
| EV turtle / car-with-! / HV or charge-plug text still showing | **Run** Step 6 — `garage` (or `poor` only if they already hold a written traction-pack quote) |

Do not skip because the shape is missing from the PNG. Do not skip because lookup was thin. Do not skip because you cannot invent an id.

---

## Thinner statement, then outlook

Unmatched still uses the Step 5 headings. It is **thinner**: no circled id, no DPF / engine / ESC padding, no fusion dump (these paths have **no** same-system allowlist — one negative History line). Lookup 404 / owner-stated make: say so once in **[History]**; do not invent MOT.

Spoken statement first, then **[Outlook]** in the **same turn**. Do not ask if they are driving. Stop / recovery lives in **[Drive advice]**, not as a flow lock.

```
[Vehicle]      year, make, model, fuel · mileage · MOT expiry (omit invented MOT)
[Showing]      unmatched path in plain English — not a circled id, not “lamp 14”
[Since]        when it started; remaining-starts count; pasted Tesla / HV text
[History]      one negative line. End any quoted note: this does not show the cause of today’s lamp
[Drive advice] see table below
[Ask the garage] readings or process — not a parts shortlist
[Book]         only if MOT expired or due within 30 days
```

Then:

```
[Outlook]  Close it yourself / A garage can usually handle this / Repair may cost more than the car
[Repair]   verified headline, or: we publish no figure — two written estimates
[Sell]     weak outlook only
[Close it] close-it-yourself branches only
```

**[Showing]** lines (plain English):

- GPF: amber exhaust-dots / petrol particulate-filter mark. Circled 9 is empty on this petrol or hybrid picture — not a diesel filter.
- AdBlue: AdBlue / urea / DEF message. Not on the picture. Not the exhaust-dots lamp. Not the engine outline.
- EV: turtle / limited power, or a car-with-! with no skid lines, or a charge-plug / high-voltage message. Not the 12-volt rectangle. Not the skid-lines mark.

Drive advice in the statement:

| Path | [Drive advice] |
|---|---|
| GPF | Drive with care. Scan next. No motorway regen copy |
| AdBlue, low, still starts | Limited. Drive directly to the handbook filler if they are going anywhere; no extra journeys |
| AdBlue remaining-starts / no-start | **Stop.** Do not drive it in. Collect or recovery |
| EV unmatched | **Limited.** Drive directly there, no extra journeys — unless a **red** lamp or a **Stop** lamp is also on, then do not drive it in; arrange recovery |

Ask the garage:

- GPF: stored codes and freeze frame before replacing anything. Not soot-versus-ash. Not a diesel regen fork.
- AdBlue: **SCR / reagent status**, not a parts fork (not injector / pump / NOx as a shortlist).
- EV: what the cluster or pasted alert says. Not a 12V-versus-pack fork you invent. Tesla text is an owner fact, not a named part.

MOT: never “Expect a fail.” Do not copy diesel-DPF MOT copy onto GPF. Pure EV: do not call an engine lamp an MOT fail item. Link the [DVSA inspection manual](https://www.gov.uk/guidance/mot-inspection-manual-for-private-passenger-and-light-commercial-vehicles) if scope is in play.

---

## Buckets (Step 6)

| Path | Default | Repair slugs | Close-it-yourself |
|---|---|---|---|
| Petrol / hybrid GPF | `device` then `garage` | `car-diagnostic-test-cost` **only** | Scan + freeze frame, do not clear. **No** diesel regen. Fuel cap is engine-steady only — it does not close GPF |
| AdBlue, level low, still starts | `owner` | **none** | Correct fluid, handbook filler. Not water. No tank-reset DIY |
| AdBlue remaining-starts / no-start | `poor` | **none** | **No.** Top-up does not close a lockout |
| EV turtle / car-with-! / HV text | `garage` | **none** (no ICE slugs) | **No.** Not 12, not 8 |
| EV + **written** traction-pack quote they already have | `poor` | **none** | **No.** Compare **that** quote with one bid as it sits |
| Electric board lamp 8 (12V rectangle) | **Not this file** | `car-battery-replacement-cost` as “if invoiced” on lamp 8 | No belt combo |

Do not upgrade GPF or EV-garage to `poor` because the car is old. EV `poor` only on a written pack quote. GPF weak-outlook speech only after a **later large written estimate**. AdBlue remaining-starts is already `poor` on a new diesel.

Device scan steps (GPF): `references/prognosis/deep/21-device-scan-steps.md`. Remaining-starts sell: `95-adblue-remaining-starts.md`. EV pack quote: `96-ev-pack-quote-vs-bid.md`. GPF card: `14-gpf-unmatched.md`. This file is the **routing**: thinner statement, then the matching row.

---

## Owner copy

Each branch ≤120 words. After the thinner statement. No ids, no fusion slugs, no plates, no pounds except a live `repair_cost` headline (GPF garage path only). Labels are for the agent.

### Skip — key-on check that went out

That mark came on with the ignition and went out. Not a fault. No garage card. No repair-or-sell outlook.

(~22 words.)

### GPF — device then garage (~95 words)

Circled 9 is empty on this petrol or hybrid picture. That is not a diesel filter. Drive with care. Close the next step yourself if you have a reader: stored codes and freeze frame, write them down, do not clear. No motorway loops and no handbook regen — that copy is diesel only. No reader: a garage diagnostic is next. We publish a planning figure for that test when the cost tool returns one; otherwise we publish no figure — two written estimates. The lamp does not name the part.

Spoken: **[Outlook]** Close it yourself (reader) / a garage can usually handle this. **[Close it]** the scan. **[Repair]** `car-diagnostic-test-cost`. No **[Sell]** on the default path.

### AdBlue — low, still starts (~58 words)

Close it yourself. Use the correct AdBlue (urea / DEF) at the filler the handbook shows. Do not add water or screenwash. Do not reset the tank with a reader. Limited driving until it is filled. If a remaining-starts countdown or a no-start appears, stop this top-up close — that is a different outlook. We publish no figure for AdBlue-system work.

Spoken: **[Outlook]** Close it yourself. **[Close it]** handbook filler. No **[Sell]**.

### AdBlue — remaining-starts / will not start (~88 words)

Stop. Do not drive it in. Ask the garage to collect, or call recovery. This is not a low-level top-up. Repair may cost more than the car. We publish no figure for this class of work. Get one bid as it sits — it is not a runner — and one written estimate. Recovery is part of the sell cost. Compare those two before you authorise work. Ask the garage for SCR and reagent status, not a parts guess.

Spoken: **[Outlook]** Repair may cost more than the car. **[Repair]** no figure. **[Sell]** bid vs estimate. No **[Close it]**.

### EV — no pack quote (~72 words)

A garage can usually handle this. We publish no figure for this class of high-voltage work — two written estimates. The message does not name the part. Drive directly there, no extra journeys, unless a red or stop lamp is also on — then do not drive it in. This is not the 12-volt rectangle and not the skid-lines lamp. Not a driveway job. Do not clear it.

Spoken: **[Outlook]** A garage can usually handle this. **[Repair]** no figure. No **[Sell]**. No **[Close it]**.

### EV — written traction-pack quote already in hand (~70 words)

Repair may cost more than the car. We publish no pack price and no used-car price. Compare the traction-pack quote you already have with one bid as the car sits. If that quote is larger than the bid, selling is often the better outlook. Recovery is part of the sell cost if you must not drive it in. Repeat their quoted figure as what they were given. Do not invent another pack number.

---

## Slugs

Call `repair_cost` only from **this path’s** allowlist. Never pick a job because it is the only slug with a number. A cost page is not a diagnosis.

| Path | Call |
|---|---|
| GPF | **Always** `car-diagnostic-test-cost` on the garage path (no reader, or the lamp stays). Headline if verified; `gbp: null` / `no_verified_price` / `no_published_job` → we publish no figure; two written estimates |
| AdBlue (either branch) | **None.** No published AdBlue-system slug |
| EV unmatched (either branch) | **None.** No ICE slugs. No invented HV pack price |
| Not-a-fault skip | Do not call |

Do **not** call on these unmatched paths:

- `dpf-cleaning-cost` on petrol / hybrid GPF
- `catalytic-converter-replacement-cost`, clutch, belts, pads, head gasket, MOT, wheel-bearing because the mark is on
- `car-battery-replacement-cost` or `alternator-replacement-cost` on unmatched EV (12V invoice class is **lamp 8** only)
- `car-diagnostic-test-cost` on AdBlue or unmatched EV so there is a number

There is no published GPF-replace or AdBlue-system or traction-pack slug. Do not invent those prices.

---

## Sell

Only on **weak outlook**.

- GPF default: **no** sell block. Later large written estimate → then bid as it sits vs that estimate. Drive with care is not Stop, so recovery is not a default sell cost.
- AdBlue low / still starts: **no** sell.
- AdBlue remaining-starts / no-start: **yes.** Bid as it sits (not a runner). One written estimate. Recovery is part of sell cost. Do not tell them to use remaining starts to reach a buyer.
- EV, no pack quote: **no** sell.
- EV, written pack quote: **yes.** Compare **that** quote with one bid as it sits. Repeat their number. Do not invent the bid or a second pack price. Recovery in sell cost only when **[Drive advice]** is Stop.

No sell-price tool. No Parkers / WeBuyAnyCar / trade-in pounds. Do not say write-off. A missing pound is not a missing outlook: still give the compare rule on `poor`.

Do not suggest DPF / GPF / cat / SCR delete as a cheap fix. Deletion is **Negative** sale-price effect (`value-gain.md`) after this outlook — no how-to.

---

## DIY

| Path | Close-it-yourself |
|---|---|
| GPF | Reader: handbook ignition, engine off unless the reader says otherwise; stored codes **and** freeze frame; write down; **do not clear**. How-to-choose links **below** drive advice. Category may be off the shelf — not a fake SKU. No diesel regen. No scan-tool forced regen. No fuel-cap close |
| AdBlue low, still starts | Correct ISO / handbook reagent at the **handbook** filler only |
| AdBlue remaining-starts / no-start | **No.** Do not keep cranking. Do not drive the countdown to zero |
| EV unmatched | **No.** No HV / orange-cable / BMS-reset / “just plug it in” as a close. A 12V reader does not close this |
| Skip / not-a-fault | No owner repair. Status lamps: name the function |

Never clear a lamp or message as a fix. Never “just add water.” Never tank-reset DIY.

Scanner links (GPF device path only), below **[Drive advice]**:

- https://obdcode.co.uk/guides/best-obd2-scanner-uk/
- https://obdcode.co.uk/tools/scanners/

---

## Red lines

1. **Not a 14th lamp id.** Do not add `gpf` / `adblue` / `ev-turtle` to the menu. Do not pick the closest of the 13.
2. **Unmatched still gets a statement and Step 6** unless not-a-fault. Do not drop the garage card because the PNG has no matching shape.
3. Keep this board. Do not switch petrol 9 to the diesel picture. Do not open the ICE unknown board for EV turtle / HV text.
4. AdBlue is not 9 and not 6. GPF is not diesel DPF. EV turtle / car-with-! / HV is not 12 and not 8.
5. No diagnosis. Not blocked GPF, not soot-versus-ash, not AdBlue injector / NOx, not traction pack / BMS / cell.
6. No invented pounds. Empty allowlist means we publish no figure. Do not hunt a nearby slug.
7. No SAE J2012 wording. A code they write down is a fact; the standard’s definition is not.
8. Never clear the lamp. No scan-tool forced regen. No GPF motorway-regen copy. No filter / SCR delete how-to.
9. No real registration. Illustrative plate only `AB12CDE`, then **your 2016 Fiesta** / **your Transit** / **your 2016 Leaf**.
10. Safety before commerce. No shop or scanner link above Stop / recovery.
11. Never “Expect a fail.”
12. Do not ask if they are driving.
13. Ask the garage for **process** (scan / SCR status / what the message said), not a parts shortlist.
14. If they ask what is wrong: this skill does not diagnose. If they ask recovery, scan, keep-driving, or repair-vs-sell: restate **[Drive advice]** and **[Outlook]**. Do not say “continue as a normal assistant.”

---

## Pass / fail

**Pass**

- Menu stays 13. Unmatched GPF / AdBlue / EV spoken as a path, not as lamp 14.
- Thinner statement (no circled id, one negative History line), then Step 6 in the same turn.
- Petrol / hybrid: keep that picture. “9 is not printed. Not DPF.” Drive with care. Scan. `car-diagnostic-test-cost` only. No regen copy.
- AdBlue: not on the picture; not 9; not 6. Low and still starts → close it yourself with the correct fluid. Remaining-starts / no-start → Stop, `poor`, no slug, bid vs estimate, recovery in sell cost.
- EV turtle / car-with-! / HV text: not 12, not 8, no ICE unknown board. Limited unless red or Stop. `garage` and no figure — or `poor` only with **their** written pack quote versus one bid.
- Key-on unmatched mark that went out → not a fault; **skip** Step 6.
- “A scan is the next step; the lamp does not name the part” (GPF). “Ask SCR / reagent status, not a parts fork” (AdBlue). “The message does not name the part” (EV).
- `gbp: null` spoken as we publish no figure. Two written estimates where the card says so.
- Restate drive advice and outlook if they ask keep-driving or repair-vs-sell.
- Your 2016 Fiesta / your Transit / your 2016 Leaf.

**Fail**

- Inventing id 14, or forcing GPF → 9-as-DPF, AdBlue → 6 or 9, EV turtle / car-with-! → 12 or 8.
- Switching the petrol board to diesel for exhaust-dots, or opening the ICE unknown board for an EV HV message.
- Skipping the statement or Step 6 **only because** the shape is unmatched (while the warning is still on).
- Running Step 6 on a key-on check that went out, or on a blue/green status lamp.
- Diesel regen / motorway loops / `dpf-cleaning-cost` on petrol GPF.
- “Pop a bottle in and use the remaining starts to get there.” / “Add water.” / tank-reset DIY.
- “It’s a blocked GPF / the NOx sensor / the traction pack.”
- Calling `car-diagnostic-test-cost` on AdBlue or unmatched EV so there is a number. Calling battery / alternator on unmatched EV.
- “About £400–£800” / invented pack or AdBlue-system pounds / Parkers bid / “it’s a write-off.”
- Clear the message; scan-tool regen; “just cut it out.”
- Shop or scanner link above Stop. Fake in-stock scanner SKU.
- “Expect a fail.” A real plate. “Continue as a normal assistant” then a parts guess.

**Pass sketch** (illustrative; no live pounds): Your 2016 Fiesta, petrol, exhaust-dots. Keep the petrol picture; 9 is empty, not DPF. Drive with care. Thinner statement, then: scan stored codes and freeze frame, do not clear; or a garage diagnostic — published figure or we publish no figure.

**Fail sketch:** “That’s basically a DPF — pick 9, do a regen. If you’re electric, that’s traction control (12) or the battery (8). AdBlue is the engine light. New lamp id 14.”
