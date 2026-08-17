# Unmatched EV (turtle / car-with-! / HV or charge-plug)

Not a 14th lamp id. Live defaults: `SKILL.md`, `references/prognosis.md`, `references/prognosis-cards.md`. This file is not a second SKILL. If they disagree, those win.

**Path:** electric + tortoise / limited power / car-with-! and **no** skid lines / charge-plug symbol / high-voltage on-screen text.  
**Bucket:** `garage` (owner hears: a garage can usually handle this). Upgrade to `poor` only if they **already** have a traction-pack quote.  
**Not this file:** lamp **12** (skid-lines only); lamp **8** on the electric board (that rectangle is **12V**, not the pack).  
**Drive advice (statement):** Limited — drive directly there, no extra journeys — unless the message is **red** or another Stop lamp is also on, then Stop: do not drive it in; arrange collection.

Do not diagnose. Do not invent pounds. Do not print a plate.

---

## When

Run Step 6 in the **same turn** as the thinner Step 5 statement when **all** of these are true:

1. The car is **electric** (`fuel_type` electric, electric board).
2. They described a **turtle / tortoise / limited power**, a **car-with-!** with **no** wavy tracks, a **charge-plug** mark, or **HV / high-voltage** text (Tesla: accept pasted alert text as owner fact, not a diagnosis).

Skip this file when:

- They picked **12**, or the shape has **skid lines** — that is `esc-traction`, not this path.
- They picked **8** on the electric picture — that is the **12V rectangle**. Leave this file. Do not retell 12V / DC-DC / belt copy here.
- The board is petrol, diesel, hybrid, or unknown. Do **not** open the ICE unknown cluster. Do **not** shrink an ICE board toward electric on owner talk.
- Lookup failed and fuel is unknown — ask fuel; never default electric.
- Key-on bulb check on a **circled** electric-board lamp that then went out — that is not this unmatched path.
- They asked only about wrap / service / value and **no** lamp — `value-gain.md`, not this path.

Do not force the nearest circled number. Do not add a lamp id. Age does not change the bucket. Do not upgrade to `poor` because the car is old or because an EV “might need a pack.”

Vans: same bucket. Say **your Transit**. Downtime may be “a day off the road.” Do not invent a day-rate. A Leaf is not a van.

History: this path has **no** same-system MOT allowlist. One negative line. Do not dump fusion slugs. Do not call an engine MIL an MOT fail item on a pure EV. Never say “Expect a fail.”

---

## Owner copy

Spoken **[Outlook]** after the statement. ≤120 words. No ids, no fusion slugs, no URLs, no plates, no pounds. Stop / Limited already sits in **[Drive advice]** — no shop or scanner link above a Stop line.

**Garage** (default, ~100 words):

A garage can usually handle this. This is not the skid-lines lamp and not the 12-volt rectangle. A tortoise, a car with an exclamation and no tracks, a charge-plug symbol, or high-voltage text is a power-limit or high-voltage message. Drive only to a workshop that can read this electric car, no extra journeys. If the message is red or another stop lamp is also on, do not drive it in — arrange collection. We publish no figure for this class of job. Ask two specialists for a written estimate. A consumer reader does not close this. Do not clear the message.

**Poor** — they already have a traction-pack quote (~59 words):

Repair may cost more than a buyer will pay as it sits. We publish no pack price. Put that written quote next to one bid as the car sits before you authorise the work. If the message is red or another stop lamp is on, collection is part of the sell cost. A consumer reader does not close this.

Spoken labels: **[Outlook]** then **[Repair]** (no figure). **[Sell]** only on the poor branch. No **[Close it]** block.

---

## Slugs

Allowlist: **none**. No ICE slugs. Do not call `repair_cost`. Do not hunt a nearby job because it has a number.

Do **not** call:

- `car-diagnostic-test-cost`
- `car-battery-replacement-cost` (that “if invoiced” 12V slug belongs on **electric lamp 8**, not here)
- `alternator-replacement-cost` (no belt / alternator story on an EV)
- `head-gasket-repair-cost`, `clutch-replacement-cost`, `dpf-cleaning-cost`, `catalytic-converter-replacement-cost`, or any other published ICE job

Empty allowlist means: **we publish no figure** for this class of job — two written estimates. That is the answer. `gbp: null` / `no_verified_price` / `no_published_job` is not a gap to fill.

Do not invent a traction-pack, inverter, charger, or “typical EV” price. A cost page is not the failed part.

---

## Sell

Not first-line. Garage bucket: do not push selling.

Sell talk only on the `poor` branch — they **already** have a traction-pack quote:

1. Repair: we publish **no** pack price and no other figure. Use their written quote, or two specialist estimates.
2. Sell: we publish no used-car price. Get **one** bid **as the car sits** (runner if Limited; for parts if Stop) and compare it with that estimate before they authorise the job.
3. Recovery / collection is part of sell cost when **[Drive advice]** is Stop. Limited driving is still a runner unless a red or Stop lamp took it off the road.
4. Do not say write-off. Do not invent Parkers / WeBuyAnyCar / trade-in / pack pounds.

---

## DIY

**No.** Close-it-yourself is not allowed on this path. Outlook is `garage` or `poor`, never `owner` or `device`.

- No HV isolation, orange-cable, pack, inverter, or charge-port work. No lifting.
- A consumer OBD reader does **not** close this. Do not clear the message or any codes.
- Pasted Tesla / maker alert text is **[Since]** / tell-the-garage fact, not a driveway decode and not a close.
- Trying another charge post, “resetting” the car, or unplugging as a fix is not a close. Charge-plug **text** is why this path ran; it is not a 12V job.
- Owner-safe notes only: exact on-screen wording, whether power is limited, whether a red or Stop lamp is also showing. That is information, not a repair.

This path has no `[Close it]` block. Device and shop links stay below Stop / recovery if they appear at all — they do not close this.

---

## Red lines

1. Do not diagnose. Not the pack, inverter, motor, charger, DC-DC, contactor, or a cable — even as a shortlist.
2. Do not pick **12** or **8**. Lamp 8 on the electric board is **12V** — say that only to send them off this card.
3. Do not open the ICE unknown board. Do not add a 14th lamp id. Do not shrink toward electric on ICE talk.
4. No ICE slugs. No invented pack price or any other GBP.
5. No HV or lift how-to. No scan-clear as a fix.
6. Do not run the ICE belt / heavy-steering / rising-temp combo. That is not this path.
7. Do not print, file, or speak a real registration. Illustrative only: `AB12CDE`, then “your 2019 Leaf” / “your Transit.”
8. Do not say “Expect a fail.” Do not treat a prior MOT note as today’s cause.
9. Safety before commerce. No tool or parts link above a Stop line.
10. A cost slug is not a diagnosis. Do not call the 12V battery slug because they said charge plug or HV.

---

## Pass / fail

**Pass**

- “A garage can usually handle this.”
- “This is not the skid-lines lamp and not the 12-volt rectangle.”
- “We publish no figure — two written estimates.”
- Limited: drive directly to a workshop that can read this electric car. Red or another Stop lamp: do not drive it in; arrange collection.
- “A scan at that workshop is the next step; the message does not name the part.”
- They already have a pack quote → weak outlook: that quote next to one bid as it sits. Still no invented bid or pack price.
- Restating Limited / Stop and the outlook when they ask keep-driving or repair-vs-sell.
- “This skill does not diagnose” when they ask which part.
- Tesla alert text repeated to the garage as owner wording, not decoded as a failed part.

**Fail**

- Picking 12 or 8, or opening the ICE unknown cluster.
- “It’s the traction battery / inverter / charger.”
- “A pack is about £…” / any invented GBP, Parkers, or trade-in.
- Calling `car-battery-replacement-cost`, `alternator-replacement-cost`, `car-diagnostic-test-cost`, or any ICE slug.
- “Clear it with a reader” / HV DIY / “try another post and it should go out.”
- Belt-noise or alternator speech on this path.
- “Expect a fail.” / “It’s a write-off.”
- A real plate in git or speech.
- Naming a likely part when they ask what is wrong.
