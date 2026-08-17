# 4 `airbag-srs`

Live defaults: `references/prognosis.md`, `references/prognosis-cards.md`. This file is not a second SKILL. If they disagree, those win.

Lamp 4. Red seated person with a circle in front. Bucket **`garage`**. Red-class. **Limited** driving — not Stop. Not diagnosis. Not a driveway close. No published SRS slug.

---

## When

Run Step 6 in the **same turn** as the Step 5 statement when this lamp is a **real fault**: it stayed on after the key-on bulb check.

Skip outlook when it was only the bulb check and then went out.

Stay on this card when they picked 4, or named airbag / SRS / supplementary restraint. Default remains **`garage`**. Do not upgrade to `poor` because the car is old. Upgrade only if they **already** have a **large SRS quote**, or they already said the car is not worth a safety repair.

Vans: same bucket. Say “your Transit”. A day off the road may be part of outlook speech. Do not invent a day-rate.

History (statement, not outlook): this lamp has **no** same-system MOT fusion allowlist. One negative History line. Do not dump unrelated slugs. Do not invent an SRS MOT note as today’s cause.

MOT talk is gated. An SRS lamp indicating a fault can be a listed Major where that check applies. Link the [DVSA inspection manual](https://www.gov.uk/guidance/mot-inspection-manual-for-private-passenger-and-light-commercial-vehicles). Never say “Expect a fail.”

Drive advice in the statement is **Limited**: they may drive **directly** to the garage, no extra journeys. `safety_class: Red` is not Stop. Do not recover this car unless some other Stop lamp or fact already applies.

If they have this lamp **and** named a modification, finish **[Drive advice]** and this outlook first, then a separate **[Value]** block. A wrap does not close an airbag lamp.

---

## Owner copy

Spoken outlook, ≤120 words. After the statement. No ids, no fusion slugs, no URLs, no plates, no pounds.

**Garage (default):**

A garage can usually handle this. Drive there directly — no extra journeys. Do not work on it yourself. We publish no figure for this class of job. Ask two workshops for a written estimate. The lamp does not name the part. Do not clear it. Airbags and seat-belt pretensioners are pyrotechnic. There is no driveway job.

(56 words.)

**Poor, or they are choosing not to repair this safety system:**

A written estimate may cost more than a buyer will pay as it sits. We publish no repair figure and no used-car price. Get one bid as it sits and compare it with the estimate. A car sold with the airbag lamp on is worth less and may not be legal to sell as a safe runner.

(57 words.)

Spoken labels: **[Outlook]** then **[Repair]** (no figure). **[Sell]** only on the second branch. No **[Close it]** block.

---

## Slugs

Allowlist for this lamp: **none**. There is **no** published SRS job.

Do not call `repair_cost`. Do not hunt a nearby slug. Empty allowlist means **we publish no figure** — two written estimates. That is the answer.

Do **not** call:

- any airbag / SRS / clock-spring / pretensioner / crash-sensor job (none is published)
- `car-diagnostic-test-cost` (not on this allowlist; a garage scan is still the next step in speech)
- `car-battery-replacement-cost` because a low 12V system can also light SRS lamps
- cat, clutch, pads, DPF, head gasket, alternator, belts, MOT, or wheel-bearing slugs because this lamp is on

Never pick a slug because it is the only one with a number. Never treat a cost page as the failed part. Never invent GBP. `gbp: null` / `no_verified_price` / `no_published_job` is not a gap to fill.

---

## Sell

Not first-line on the default **`garage`** bucket. Do not push selling as the plan.

Sell talk **only** if they are choosing not to repair this safety system, or the bucket has already upgraded to `poor` (large SRS quote, or they said it is not worth a safety repair):

1. Repair: no published figure (empty allowlist). Two written estimates if a workshop is quoting.
2. Sell: we publish no used-car price. Get **one** bid **as the car sits**. Get **one** written garage estimate. Compare before they authorise the job.
3. A lamp-on airbag car is a **safety and legal value hit**: it is worth less, and it may not be legal to sell as a safe runner. Still **no invented bid**. No Parkers / WeBuyAnyCar / trade-in pounds.
4. Limited driving still makes it a **runner** unless another Stop fact applies. Bid as it sits with the lamp disclosed — not “for parts” by default. Recovery / collection is part of sell cost **only** when **[Drive advice]** is Stop. Do not invent that fee either.

Do not say write-off. If they ask repair vs sell, restate **[Drive advice]** (Limited: drive directly there) and **[Outlook]**.

---

## DIY

**No.** Close-it-yourself is not allowed. Red-class work is never a driveway or scan-tool close. A reader does not fix an airbag.

- No clock-spring DIY. No steering-wheel, column, or squib how-to.
- No scan-clear as a fix. Do not clear codes. Do not “see if it comes back.”
- No probing SRS wiring. No disconnecting modules. No work under seats where an SRS connector lives. No pretensioner or airbag-module steps. These are pyrotechnic devices.
- Noting when the lamp started, and whether a seat was moved, a cover was fitted, or something was dropped in a footwell, is **information for the garage** — not a repair and not a named cause.
- Owner-safe: nothing beyond that note. There are no publishable owner steps for this system.

Device and shop links stay below Stop / recovery. This path has no `[Close it]` block and no scanner close.

---

## Red lines

1. Do not diagnose. Not the clock spring, crash sensor, occupancy mat, under-seat connector, module, or pretensioner — even as a shortlist.
2. No clock-spring DIY. No pyrotechnic how-to. No lifting for this job on the driveway.
3. Never advise clearing the lamp or the codes as a fix.
4. Do not invent pounds for repair, sell, recovery, or “typical airbag jobs.”
5. Do not print, file, or speak a real registration. Illustrative plate only: `AB12CDE`. After lookup: “your 2016 Fiesta”, never the plate.
6. Do not call `repair_cost` on an empty allowlist. Do not hunt `car-diagnostic-test-cost` for a number.
7. Do not treat Limited as Stop. Do not recover this car for the airbag lamp alone.
8. Do not say “Expect a fail.”
9. A cost slug is not a diagnosis. Empty allowlist is the answer.
10. No SAE J2012 wording. Safety before commerce: no tool or shop link above **[Drive advice]**.
11. Do not invent a used-car bid. Selling with the lamp on is a value and legal hit, not a made-up pound figure.

---

## Pass / fail

**Pass**

- “A garage can usually handle this.”
- “Drive directly there — no extra journeys.” (Limited, not Stop)
- “A scan is the next step; the lamp does not name the part.”
- “We publish no figure — two written estimates.”
- “Do not work on it yourself. Airbags are pyrotechnic.”
- Empty slug list. Do not call `repair_cost`.
- If they choose not to repair: lamp-on sale is worth less and may not be legal as a safe runner; get one bid as it sits; we publish no used-car price.
- “This skill does not diagnose” when they ask which part.
- Restating Limited and the garage outlook when they ask keep-driving or repair-vs-sell.

**Fail**

- “It’s the clock spring / crash sensor / under-seat connector / occupancy mat.”
- Clock-spring replacement steps, steering-wheel DIY, or “just unplug the yellow connector under the seat.”
- “Clear the code and see if it comes back.”
- “About £200–£400” / any guessed SRS price with no tool result.
- Calling `car-diagnostic-test-cost` (or any slug) because this lamp is on.
- Invented trade-in, Parkers, or “worth about …” pounds.
- “Expect a fail.”
- “Stop; recover it” for this lamp alone.
- “Plug in a reader” as the close.
- “It’s a write-off.”
- Naming a likely part when they ask what is wrong.
- A real plate in git or speech.
