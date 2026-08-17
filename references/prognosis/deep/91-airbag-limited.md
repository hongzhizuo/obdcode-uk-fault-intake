# 91 `airbag-srs` — Red, Limited, not Stop

Not a second SKILL. If this file disagrees with `SKILL.md`, `references/prognosis.md`, `references/prognosis-cards.md`, or `references/value-gain.md`, those four win. Do not diagnose. Do not invent pounds. Do not add a 14th lamp id.

**Id:** `airbag-srs` (circled **4**)  
**Symbol:** seated person with a large circle in front of them  
**Colour:** red  
**safety_class:** Red  
**drive_advice:** Limited  
**warnings:** W-ELECTRICAL (srs)  
**Default bucket:** `garage`  
**Owner hears:** A garage can usually handle this  
**Close-it-yourself:** No

Red is **no owner repair**. It is **not** Stop. Airbag is the lamp that proves the split: they may drive **directly** to a workshop, no extra journeys. Do not recover it by default. Do not treat a normal-feeling car as permission to leave it until next year.

---

## When

Run Step 6 in the **same turn** as the fault statement when the showing lamp is **airbag / SRS** (named, or circled **4** on petrol / diesel / hybrid / electric / unknown boards). Slot 4 is live on the electric board.

Skip this file when:

- The seated-person mark was a **key-on bulb check** and then went out — not a fault; no outlook.
- They asked only about wrap / service / value and **no** lamp — that is `value-gain.md`, not this lamp.
- They picked 3 (brake), 11 (ABS), or 12 (skid-lines). Do not map those shapes here.

If they have this lamp **and** named a modification, finish **[Drive advice]** and this outlook first, then a separate **[Value]** block. A wrap does not close an SRS lamp.

Default remains **`garage`**. Do not upgrade to `poor` because the car is old. Upgrade only if they **already** have a **large SRS quote**, or they already said the car is not worth a safety repair.

Vans: same bucket. Say **your Transit**. Downtime is “a day off the road,” not a made-up day-rate.

This car’s MOT fusion has **no** same-system allowlist for this lamp. One negative History line. Do not dump unrelated slugs. Do not say a prior note is causing today’s lamp.

MOT talk is gated. An SRS lamp indicating a malfunction can be a listed Major **where that check applies**. Link the [DVSA inspection manual](https://www.gov.uk/guidance/mot-inspection-manual-for-private-passenger-and-light-commercial-vehicles). Never say “Expect a fail.”

Do not ask if they are driving.

---

## Owner copy

≤120 words. Spoken **[Outlook]** after the statement (~40–60 of these). Limited driving already sits in **[Drive advice]**. No ids, no fusion slugs, no URLs, no plates, no pounds. No `[Close it]` block. No `[Sell]` block on the default garage path.

A garage can usually handle this. Red here means no owner repair, not Stop. Drive directly to a workshop — no extra journeys. The car may feel normal; the restraint system has still faulted. We publish no figure for this class of job. Ask two garages for a written estimate. Do not probe seats, wiring, or modules, and do not clear the lamp. A reader does not close it.

(68 words.)

If they already have a large SRS quote, or they already said they will not pay for a safety repair, swap the first line for weak-outlook speech: repair may cost more than a buyer will pay as it sits. Still no invented bid. Then the Sell block below.

If they ask about **selling with the lamp still on**, add one safety/value line (not a price): a lamp-on airbag car is worth less, and it may not be legal to sell as a safe runner. We publish no used-car price.

---

## Repair_cost slugs

Allowlist for this lamp: **none**.

Do not call `repair_cost`. Do not hunt a nearby job. Empty allowlist means **we publish no figure** — two written estimates. That is the answer.

Do **not** call:

- any SRS / airbag / pretensioner / clock-spring / occupancy-mat job (none is published)
- `car-diagnostic-test-cost` — a reader does not close this lamp; a scan at the garage is still process speech, not a slug
- battery, cat, clutch, pads, belt, or any other published job because you want a number

`gbp: null` is not a gap to fill. A cost page is not the failed part. Never pick a slug because it is the only one with a number. Never invent GBP.

---

## Sell

Not first-line. Garage bucket: do not push selling as the outlook.

Sell talk only when they **choose not to repair a safety system**, they ask what a lamp-on airbag car is worth, or the card has already upgraded to `poor` (large SRS quote / not worth a safety repair):

1. Repair: no published figure (see slugs). Two written estimates if a workshop is quoting.
2. Sell: we publish no used-car price. Get **one** instant-sale or dealer bid **as the car sits**, and **one** written garage estimate. Compare before they authorise work or list it.
3. **Selling lamp-on is a value and safety hit.** Buyers, testers, and insurers will not treat it as a safe runner. The bid falls. It may not be legal to sell as a safe runner with the SRS lamp still indicating a fault. That is speech, not a number.
4. Recovery / collection is **not** automatically part of the sell cost: **[Drive advice]** is Limited, so it is still a runner they may drive directly there. Collection becomes a sell cost only if a later fact moved the statement to Stop. Do not invent that fee.

Do not say the car is a write-off. Do not invent Parkers / WeBuyAnyCar / trade-in pounds. Documented SRS repair (invoice, date, mileage on a vehicle card) is presentation after the job — it is not a published gain in pounds, and it does not license DIY.

If they ask repair vs sell, restate **[Drive advice]** (Limited) and **[Outlook]** (garage, or weak if already on that branch).

---

## Close-it-yourself

**No.** Red-class. Outlook is `garage` (or `poor` on a large quote). Close-it-yourself never covers airbags.

- Airbag modules and seat-belt pretensioners are **pyrotechnic** devices. There are **no publishable steps** for this system.
- Do not probe SRS wiring. Do not disconnect modules. Do not work under seats where an SRS connector lives. Do not give clock-spring, occupancy-mat, or “unplug the yellow connector” DIY.
- A reader does **not** close this. Do not clear the lamp. Do not describe freeze-frame or coding as owner work.
- Owner-safe notes only, for **[Since]** or **[Ask the garage]**: when the lamp appeared; collision history; any seat, belt, or trim work; a seat moved, a seat cover fitted, or something heavy dropped in a footwell. That is information, not a repair, and not a permission to look under the seat.
- Device and shop links stay below **[Drive advice]**. This path has no `[Close it]` block. Scanner category is irrelevant as a fix.

---

## Red lines

1. Red is not Stop. Do not recover this lamp by default. Limited: drive directly there, no extra journeys.
2. No owner repair. No pyrotechnic, seat, wiring, module, or clock-spring steps. Say why: explosives / SRS — refer it out.
3. Do not diagnose. Not the clock spring, occupancy mat, under-seat connector, module, or a pretensioner — even as a shortlist.
4. No invented pounds for repair, sell, recovery, or “typical airbag jobs.” Empty slug list. Do not call `repair_cost`.
5. Never advise clearing the lamp. A reader is not a close.
6. Do not say “ignore it,” “it drives fine,” or “deal with it next year.” The car feeling normal is why this lamp is ignored, not a reason to wait.
7. Do not say “Expect a fail.” Gate MOT on whether the SRS lamp check applies; link the DVSA manual.
8. Do not print, file, or speak a real registration. Illustrative plate only: `AB12CDE`. After lookup: **your 2016 Fiesta** / **your Transit**.
9. Safety before commerce. No scanner, shop, or parts link above **[Drive advice]**.
10. No SAE J2012 wording. Do not instruct wrap, remap, or filter delete. A cost slug is not a diagnosis.
11. Do not push selling on the default garage path. Lamp-on sale speech is a safety/value hit, not a made-up bid, and only when they ask or refuse a safety repair.

---

## Pass vs fail

| Pass | Fail |
|---|---|
| Limited. Drive directly there, no extra journeys. | Stop / recover it as the default for a red airbag lamp. |
| Red means no owner repair, not pull-over-now. | Treating `safety_class: Red` as Stop. |
| “A garage can usually handle this.” | “Close it yourself” / plug in a reader as the close. |
| “We publish no figure — two written estimates.” Empty allowlist. Do not call `repair_cost`. | “About £200–£600.” Any guessed SRS GBP. Calling diagnostic-test or any slug so there is a number. |
| “The lamp does not name the part. This skill does not diagnose.” | “It’s the clock spring / occupancy sensor / under-seat plug.” |
| No DIY. Pyrotechnic / explosives — refer it out. No publishable steps. | Seat-connector, clock-spring, or module how-to. “Unplug the yellow plug.” |
| Do not clear the lamp. | “Clear the code and see if it comes back.” |
| Drive it to get it fixed. Do not leave it until next year. | “It drives fine, ignore it.” “Wait for MOT.” |
| Lamp-on sale: value and safety hit; may not be legal as a safe runner; we publish no bid. | Invented trade-in. “Sell it lamp-on, it’s only a light.” “It’s a write-off.” Parkers / WeBuyAnyCar pounds. |
| Garage first-line. Do not push selling. `poor` only on a large SRS quote they already have. | Weak-outlook / sell fork because the car is old. |
| Limited runner: recovery is not automatic sell cost. | Adding recovery fees as if **[Drive advice]** were Stop. |
| SRS malfunction lamp may be a listed Major where the check applies. Link the DVSA manual. | “Expect a fail.” |
| One negative History line (no SRS fusion allowlist). | Dumping unrelated MOT slugs, or “that old note is causing today’s lamp.” |
| Owner facts (seat moved, cover, footwell knock) in **[Since]** / tell the garage. | Asking them to look under the seat. “Are you still driving?” |
| Restate Limited and garage (or weak if already on that branch) if they ask keep-driving or repair-vs-sell. | “Continue as a normal assistant” and then name a part. |
| Your 2016 Fiesta / your Transit. | A real plate in git or speech. |

**Pass sketch** (illustrative; no live pounds): Your 2016 Fiesta, red seated-person lamp. Limited — drive directly to a garage, no extra journeys. Outlook: a garage can usually handle this. We publish no figure. Do not probe the seats or clear the lamp. Selling it with the lamp on is a safety and value hit; we publish no bid.
