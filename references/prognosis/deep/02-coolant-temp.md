# 2 `coolant-temp` — red thermometer

Not a second SKILL. If this file disagrees with `SKILL.md`, `references/prognosis.md`, `references/prognosis-cards.md`, or `references/value-gain.md`, those four win.

**Id:** `coolant-temp` (circled **2**)  
**Default bucket:** `poor`  
**Owner hears:** Repair may cost more than the car  
**Drive advice (statement):** Stop. Do not drive it in. Ask the garage to collect, or call recovery.

This file is the **red** thermometer only. Blue is skip — not this card.

## When

Ask **blue or red** before treating a thermometer / coolant / temp light as id 2.

Run Step 6 in the **same turn** as the fault statement when the showing lamp is the **red** thermometer in wavy liquid (named as red, or circled 2 after they said red). Petrol, diesel, hybrid, unknown ICE, and the electric board (slot 2 is printed) use this card.

Skip this file when:

- The thermometer was **blue** — engine-cold, not id 2. Blue after a short run that then goes out is not a fault; no garage card; no Step 6. Do not run this outlook on blue.
- The red thermometer was a **key-on bulb check** and then went out — not a fault; no outlook.
- They asked only about wrap / service / value and **no** lamp — that is `value-gain.md`, not this lamp.
- Unmatched EV turtle / car-with-! and no skid lines / HV or charge-plug text — not this id. Do not map those to 2.

If they have this **red** lamp **and** named a modification, finish **[Drive advice]** and this outlook first, then a separate **[Value]** block. A wrap does not close a hot engine.

Age does not change this bucket. The lamp is already `poor` on a new car. Do not upgrade to a driveway close because the cold tank looks full. A caught-early thermostat job does not change the spoken bucket or invent pounds.

Vans use the same bucket. Say **your Transit**. Downtime is “a day off the road,” not a made-up day-rate.

This car’s MOT fusion has **no** same-system allowlist for this lamp. One negative History line. Do not dump unrelated slugs. Do not say the lamp is an automatic MOT fail. A visible serious leak is a tester matter — link the [DVSA inspection manual](https://www.gov.uk/guidance/mot-inspection-manual-for-private-passenger-and-light-commercial-vehicles); never say “Expect a fail.”

Do not ask if they are driving. Stop / recovery lives in **[Drive advice]**.

## Owner copy

≤120 words. Spoken **[Outlook]** after the statement (~40–60 of these). Stop / recovery already sits in **[Drive advice]** — do not put a shop or scanner link above it.

Repair may cost more than the car. If a workshop later invoices a head-gasket job, we may quote that published planning range; the page is often empty. Empty means we publish no figure — two written estimates. That job name is not today’s fault. Get one bid as it sits — it is not a runner — and compare it with the estimate. Recovery is part of the sell cost. Never open a hot cap. Once fully cold, a look at the tank and the floor is information, not a close. The lamp does not name the part.

## Slugs

You **may** call `repair_cost` with this lamp’s allowlist slug. Never pick a job because it is the only one with a number. Never treat a cost page as the failed part. Never say the gasket failed.

| Slug | Call? |
|---|---|
| `head-gasket-repair-cost` | **May.** Coolant weak-outlook **if invoiced**. Often `gbp: null` / `no_verified_price` / `no_published_job` — that **is** the answer. Say we publish no figure. Two written local estimates. Do not fill the gap. Speak it only as “if the garage later invoices this job, published UK figures are …” — never as today’s diagnosis. |
| Thermostat, hose, water pump, radiator, or “flush” as a named cause | **No published slug** for a caught-early thermostat job. Still no invented pounds. Two written estimates. |
| `cambelt-and-water-pump-cost` | **No** as a lamp cause. Value-gain / due belt only. |
| `car-diagnostic-test-cost`, `catalytic-converter-replacement-cost`, `clutch-replacement-cost`, `alternator-replacement-cost`, or any other published job | **No.** A reader does not close a hot engine. Do not hunt a nearby slug. |

On an electric board, slot 2 is still this card. The gasket slug remains an **invoice class if later billed**, not a named failed part. Do not invent a pack, pump, or heater-matrix price.

## Sell

Weak outlook only — this is that case. There is no sell-price tool.

1. Repair: verified `head-gasket-repair-cost` headline **if** the tool returns one and you are speaking invoice class; otherwise **we publish no figure**.
2. Sell: we publish no used-car price. Get **one** instant-sale or dealer bid **as the car sits** (for parts if it must not be driven — usually not a runner). Get **one** written garage estimate.
3. If they kept driving after the red lamp, the estimate can exceed what a buyer will pay for it as it sits. Still do not invent that bid.
4. If the estimate is larger than the bid, selling is often the better outlook.
5. Recovery / collection is part of the sell cost because **[Drive advice]** is Stop. Do not invent that fee.

Do not say the car is a write-off. Do not invent Parkers / WeBuyAnyCar / trade-in pounds. If they ask repair vs sell, restate **[Drive advice]** and **[Outlook]**.

## DIY

**No.** Outlook is `poor`. Red-class work is never a driveway or scan-tool close. A reader does **not** fix a hot engine. Do not clear codes.

**Never open the expansion tank or radiator cap while the system is hot.** It is pressurised. Escaping coolant is above boiling point.

Once the engine is **fully cold** — an hour or more — looking at the tank (level, without opening a hot cap) and looking underneath for puddles is **information** for the garage. Note colour of any leak if they can see it from outside. That does **not** make it safe to restart. It does **not** close the lamp. Do not top up and drive. Do not “just pop it to the garage.” Do not give a flushing tutorial.

Owner facts (climbed gradually or spiked, heater hot or cold, recent topping-up, steam or a sweet smell) go in **[Since]** or **[Ask the garage]** — process, not a parts shortlist.

## Red lines

1. Do not say the head gasket failed. Do not name thermostat, hose, pump, radiator, or a warped head as today’s fault. A cost slug is not a diagnosis.
2. Never open a hot cap. No flushing tutorial. No driveway bleed, no lift, no “crack the cap to check.”
3. Do not diagnose. The lamp does not name the part.
4. No invented pounds for repair, sell, recovery, or “typical gasket / thermostat.” `gbp: null` is the answer.
5. No SAE J2012 wording or fault-code definition tables.
6. No real registration in this file or in speech. If a worked plate is required, only `AB12CDE`; then call it **your 2016 Fiesta**.
7. Safety before commerce. No scanner, shop, or parts link above Stop / recovery.
8. Never advise clearing the lamp. Never treat a cold tank glance as permission to drive.
9. Do not run this card on a **blue** thermometer. Blue is skip, not a weak-outlook gasket talk.
10. Do not instruct wrap, remap, or filter delete. Value-gain may state price effect only, after this outlook.

## Pass / fail

| Pass | Fail |
|---|---|
| Ask blue or red before id 2. Blue that went out → skip; no Step 6. | Treating a blue cold-engine lamp as this card, or opening a gasket sell talk on blue. |
| Stop. Do not drive it in. Recovery or collection. Never open a hot cap. | “Drive it slowly to the garage.” “Crack the cap and check the level.” |
| Repair may cost more than the car. Call `head-gasket-repair-cost` as invoice class if later billed. | “It’s the head gasket.” “The gasket has failed.” |
| `gbp: null` → we publish no figure — two written estimates. | “About £800–£1,500.” Any guessed GBP. Filling a null with a model guess. |
| Get one bid as it sits (not a runner). Compare it with the estimate. Recovery is part of sell cost. | Invented trade-in. “It’s a write-off.” Parkers / WeBuyAnyCar pounds. |
| Once fully cold, tank and floor are information, not a close. | “Level is fine, you’re safe to go.” Flushing steps. Top up and drive. |
| The lamp does not name the part. This skill does not diagnose. | Naming thermostat, hose, pump, radiator, or a warped head as the cause. |
| Thermostat job: no published slug; still no invented pounds. | Calling `cambelt-and-water-pump-cost` or diagnostic-test so there is a number. |
| If they ask what is wrong: no diagnosis; restate drive advice and outlook if they ask repair vs sell. | “Continue as a normal assistant” and then name a part. |
| Your 2016 Fiesta / your Transit. | A real plate in git or speech. |

**Pass sketch** (illustrative; no live pounds): Your 2016 Fiesta, red thermometer. Stop; do not drive it in; recover it. Never open a hot cap. Outlook: repair may cost more than the car. If a workshop later invoices a head-gasket job we may quote that page; it is often empty — then we publish no figure. Bid as it sits versus a written estimate. A cold look at the tank and the floor is not a close. The lamp does not name the part.
