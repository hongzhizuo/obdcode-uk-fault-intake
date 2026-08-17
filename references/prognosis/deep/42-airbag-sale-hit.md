# Airbag / SRS: sale hit if they will not repair

Not a second SKILL. Live rules: `SKILL.md`, `references/prognosis.md`, `references/prognosis-cards.md`. If this file disagrees, those win. Do not diagnose. Do not invent pounds. Do not print a plate.

Lamp 4 `airbag-srs`. Red seated-person-and-circle. **`safety_class: Red`**, **[Drive advice] Limited** (not Stop). Default bucket **`garage`**. Close-it-yourself: **no**.

This note is the **sell** line only. Garage speech comes first. Do not load this as a write-off script.

---

## When

After the Step 5 statement when the showing lamp is airbag / SRS (named, or circled **4**).

**Garage first.** Owner hears: a workshop can usually put this right. Controllable on many cars. Still no DIY.

Do **not** open with sell. Do **not** upgrade to `poor` because the car is old.

Upgrade to weak outlook (`poor`) **only** if:

- they already have a **large SRS quote**, or
- they are **choosing not to repair** a safety system, or
- the car is otherwise **not worth a safety repair**

Skip this sell file when they are booking the garage and have not refused the job. Then there is no **[Sell]** block.

Key-on bulb check that then went out: not a fault; no outlook; no sale talk.

Vans: same order. Say **your Transit**. Downtime is “a day off the road,” not a made-up day-rate.

---

## Owner copy

≤120 words. Spoken **[Outlook]** after the statement. Limited drive advice already sits in the statement — they may drive **directly** there, no extra journeys. No ids, no fusion slugs, no plates, no pounds.

**Garage (default):**

A garage can usually handle this. We publish no figure for this class of job — two written estimates. Drive directly there; no extra journeys. Airbags and pretensioners are not driveway work. Do not clear the lamp. Do not probe wiring or work under the seats. The lamp does not name the part.

(58 words.)

**If they will not repair, or they already have a large SRS quote:**

A lamp-on airbag car is worth less and may not be legal to sell as a safe runner. Repair may cost more than a buyer will pay as it sits. We publish no used-car price. Get one bid as it sits and one written estimate. Compare them before you authorise work, or before you advertise it as a runner. Still no invented bid.

(73 words. Use this **instead of** pushing a first-line sell. Do not stack both blocks as if garage and write-off were the same.)

Spoken labels:

```
[Outlook]  A garage can usually handle this
           (or, on the poor branch only: Repair may cost more than the car)
[Repair]   we publish no figure — two written estimates
[Sell]     poor branch only — worth less; may not be a safe runner; one bid as it sits; no invented pounds
```

No **[Close it]** block.

---

## Slugs

Allowlist for this lamp: **none**. There is **no** published SRS job.

Do not call `repair_cost`. Do not hunt a nearby slug. Empty allowlist means: **we publish no figure** — two written estimates. That is the answer.

Do **not** call diagnostic-test, battery, clutch, cat, pads, belt, or any other published job because this lamp is on. A cost page is not a diagnosis. Never pick a slug because it is the only one with a number.

---

## Sell

There is **no** sell-price tool. Do not invent Parkers / WeBuyAnyCar / “typical trade-in” pounds.

On the **garage** default: do not push selling.

On the **poor** branch only (large quote, they refuse a safety repair, or the car is not worth that repair):

1. Repair: no published figure. Two written estimates if a workshop is quoting.
2. Sell: we publish no used-car price. Get **one** instant-sale or dealer bid **as the car sits**, and **one** written garage estimate.
3. If the estimate is larger than the bid, selling is often the better outlook.
4. Say the **sale hit in words, not pounds**: a lamp-on airbag car is **worth less** and **may not be legal to sell as a safe runner**. That is speech, not a valuation.
5. **[Drive advice]** is Limited, not Stop. Do not copy oil-can / hydraulic **collection** speech. Do not tell them to drive it to a buyer **as a safe runner**. Recovery is part of sell cost **only** if they later cannot or must not drive it; do not invent that fee.

Do not say the car is a write-off. Do not advertise “drives fine, light on” as a safe runner.

---

## DIY

**No.** Red-class. A reader does not close an airbag lamp.

- No scan-clear as a fix.
- No clock-spring DIY.
- No probing SRS wiring, modules, pretensioners, or connectors under seats.
- Seat moved / cover fitted / object in a footwell is **[Since]** or **[Ask the garage]** — information, not a repair.
- Owner-safe: drive directly to the workshop. Nothing else.

Device and shop links stay below drive advice. This path has no device close.

---

## Red lines

1. Garage first. Do not lead with sell on a default airbag lamp.
2. Do not diagnose (not clock spring, occupancy mat, crash sensor, module, wiring).
3. No invented pounds for repair, sell, recovery, or “typical SRS jobs.”
4. No SAE J2012 wording. No real registration in this file or in speech. Illustrative plate only: `AB12CDE`; then **your 2016 Fiesta**.
5. Never advise clearing the lamp. No pyrotechnic or under-seat how-to.
6. Do not say “Expect a fail.” An SRS lamp indicating a fault may be a listed Major where that check applies — link the [DVSA inspection manual](https://www.gov.uk/guidance/mot-inspection-manual-for-private-passenger-and-light-commercial-vehicles); do not recite a verdict.
7. Do not treat Limited as Stop, and do not treat Limited as permission to ignore it or to sell it as a safe runner.
8. Do not mix this card with 44 Stop-lamp “not a runner / collect it” copy unless drive advice has already become Stop for another lamp.
9. A cost slug is not a diagnosis. Do not call one.

---

## Pass / fail

**Pass**

- “A garage can usually handle this.” Two written estimates. We publish no figure.
- Limited: drive directly there, no extra journeys. Not a driveway job.
- Sell only after they refuse a safety repair or already have a large SRS quote.
- “A lamp-on airbag car is worth less and may not be legal to sell as a safe runner.”
- “We publish no used-car price. Get one bid as it sits and compare it with the estimate.”
- “The lamp does not name the part. This skill does not diagnose.”
- Restating Limited and the garage (or poor) outlook if they ask repair vs sell.

**Fail**

- Leading with sell, trade-in, or “just scrap it” while they have not refused the garage.
- “Typical SRS repair is £400–£800.” Any guessed GBP. Invented Parkers / WeBuyAnyCar / trade-in pounds.
- “It’s the clock spring / crash sensor / under-seat connector.”
- “Clear the code and the lamp will go out.” Clock-spring DIY. Probing SRS wiring.
- “Drive it to WeBuyAnyCar” as a safe runner. “Drives fine, light on — advertise as a runner.”
- “It’s a write-off.”
- “Expect a fail.”
- Calling `repair_cost` (any slug) because the airbag lamp is on.
- Copying Stop / recovery / “not a runner” from oil, red coolant, flashing engine, or hydraulic brakes onto this Limited lamp.
- A real plate in git or speech.
