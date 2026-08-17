# 88 · Lamp 8 with the engine running is charging, not “fit a battery”

Deep outlook note. Not a second SKILL. If this file disagrees with `SKILL.md`, `references/prognosis.md`, `references/prognosis-cards.md`, or `references/value-gain.md`, those four win. Do not diagnose. Do not invent pounds. Do not add a 14th lamp id.

**Id:** `battery-charging` (circled **8**, battery rectangle with + and −)  
**Default bucket:** `garage`  
**Owner hears:** A garage can usually handle this  
**Drive advice:** Limited — escalate to Stop on ICE only with heavy steering, a rising temperature gauge, or a belt noise  
**Close-it-yourself:** No

The symbol looks like a battery. Lit **with the engine running**, it reports that the **charging system is not keeping up**. That is not an instruction to fit a 12V battery. You may still quote published **battery-replacement** (and, on ICE, **alternator**) figures **only if invoiced**. Do **not** pick battery versus alternator.

Live lamp card: `references/prognosis/deep/08-battery-charging.md`. This file is the misconception.

---

## When

Run this note with Step 6 when lamp **8** is **on while the engine is running** (named charging / battery rectangle, or circled 8).

| Facts | Outlook | Do not say |
|---|---|---|
| Rectangle on, engine running, ICE, steering and temperature normal, no belt noise | `garage` · Limited | “Fit a battery.” “It’s the alternator.” |
| Same, plus ICE heavy steering / rising temp / belt noise | `poor` · Stop (already in **[Drive advice]**) | Still not a named part. Skip the belt combo on an electric car. |
| Electric board, they picked 8 | `garage` · Limited · 12V rectangle | Traction-pack, turtle, plug, or HV text. No alternator / belt story. |
| Hybrid, they picked 8 | `garage` (or `poor` on the ICE Stop combo) · still the **12V** charging lamp | High-voltage state of charge. |
| Key-on bulb check that went out once the engine started | **Skip.** Not a fault. No Step 6. | A battery or charging invoice. |
| Plug / lightning-bolt pack / HV on-screen text / turtle / car-with-! and no skid lines | Unmatched EV — **not** this id | Mapping those to 8. |

Do not upgrade `garage` to `poor` because the car is old, or because the symbol is a battery. Upgrade only on the ICE Stop combo, or if they already have a large charging quote.

Vans: same buckets. Say **your Transit**. Downtime is “a day off the road,” not a made-up day-rate.

**History** (statement, not cause): same-system MOT notes only — battery security, auxiliary drive belt. Quote date and `type`. No causal verbs. End: **this does not show the cause of today’s lamp.**

**MOT:** the battery lamp itself is not a specific test item. Low voltage can light ABS, SRS, or emissions lamps which are. Never say “Expect a fail.”

Do not ask if they are driving. Switching off heaters is **[Drive advice]**, not a quiz and not a close.

---

## Owner copy

≤120 words. Spoken **[Outlook]** after the fault statement. No ids, no fusion slugs, no URLs, no plates, no pounds unless `repair_cost` returned a headline in live chat. Shop links stay **below** Stop / recovery.

### Garage — engine running, no ICE Stop combo (~95 words)

A garage can usually handle this. The rectangle is the charging lamp. Lit with the engine running, the charging system is not keeping up — that is not an instruction to fit a battery. Switch off heaters, heated screens, and air conditioning, and get it somewhere it can be left. Ask the garage for charging voltage at idle and at raised revs before they sell a battery. If they later invoice a 12V battery or a charging repair, published figures are a planning range for that invoice — not a diagnosis of which part failed today.

### Poor — ICE Stop combo (~55 words)

Repair may cost more than the car. Stop. Do not drive it in; ask the garage to collect, or call recovery. The charging lamp plus heavy steering, a rising temperature gauge, or a belt noise is still not a battery-fit job. Get one bid as it sits and one written estimate. Recovery is part of the sell cost. The lamp does not name the part.

### Electric board, lamp 8 (~60 words)

A garage can usually handle this. On this car the rectangle is the 12-volt charging lamp, not the traction pack. Switch off extras and get it somewhere it can be left. No belt or water-pump story. If they later invoice a 12V battery, published figures are for that invoice class. Ask 12V or DC-DC health before any battery is sold.

---

## Repair_cost slugs

Call only from this lamp’s allowlist. A cost page is not the failed part. Never invent GBP. If `gbp: null` / `no_verified_price` / `no_published_job`, that is the answer — we publish no figure; two written estimates.

| Slug | Call | How to speak it |
|---|---|---|
| `car-battery-replacement-cost` | **May** | **Only** as “if they invoice a 12V battery.” Not “it is the battery.” Not because the pictogram is a battery. |
| `alternator-replacement-cost` | **May** on ICE / engine-running hybrid | **Only** as “if they invoice charging repair.” Often `gbp: null`. Not “it is the alternator.” |
| `alternator-replacement-cost` | **No** on the electric board | No alternator / belt invoice class on EV lamp 8. |
| Any other published job | **No** | Do not hunt diagnostic-test, clutch, pads, cat, DPF, or belt slugs because this lamp is on. |

You **may** call **both** allowed slugs as invoice-class planning ranges in the same turn. You must **not** choose which job they will get.

Pass speech: “If the garage later invoices a 12V battery, published UK figures are …” and, on ICE, “If they later invoice charging repair, published figures are …” (or “we publish no figure” when null).

Fail speech: “It’s a dead battery — here’s the battery price.” / “It’s the alternator.” / calling the battery slug because the lamp looks like a battery.

Tell the garage (process, not a parts shortlist): charging voltage at idle and at raised revs (ICE), or 12V / DC-DC health (EV / hybrid), **before any battery is sold**.

---

## Sell

Not first-line on `garage`. Do not push selling because they might need a battery.

**ICE Stop combo only** (`poor`):

1. Repair: verified headline **if invoiced**, or “we publish no figure.”
2. Sell: we publish no used-car price. Get **one** bid **as the car sits** (it may not remain a runner) and **one** written estimate.
3. If the estimate is larger than the bid, selling is often the better outlook.
4. Recovery / collection is part of the sell cost because **[Drive advice]** is Stop. Do not invent that fee.

Do not say write-off. Do not invent Parkers / WeBuyAnyCar / trade-in pounds. EV lamp 8 stays `garage` — no belt-combo sell speech.

---

## Close-it-yourself

**No.** Outlook is `garage` or `poor`. Switching off heaters, heated seats, heated screens, and air conditioning is **drive advice**, not a repair and not a close.

- Do not fit, jump, or charge a 12V battery as the fix for a lamp that is on **with the engine running**.
- Do not give alternator, belt, or wiring DIY.
- A reader does not close this. Do not clear the lamp.
- A supermarket battery is not the next step. Voltage checks belong at the garage **before** a battery is sold.
- Key-on glow that went out is not this card — and still not a parts job.

---

## Red lines

1. Do not say “fit a battery,” “dead battery,” or “it’s the alternator.” Do not pick battery versus alternator versus belt versus wiring — even as a shortlist.
2. Do not call `car-battery-replacement-cost` as today’s diagnosis. Invoice class only.
3. Do not call `alternator-replacement-cost` as today’s diagnosis. Invoice class only; often null; never on EV lamp 8.
4. No invented pounds for repair, sell, recovery, or “a typical battery.”
5. No SAE J2012 wording. No real registration. Illustrative plate only: `AB12CDE`, then **your 2016 Fiesta** / **your Transit**.
6. Never advise clearing the lamp. Never place a shop or scanner link above Stop / recovery.
7. Do not map unmatched EV (turtle, car-with-! no skids, charge plug, HV text) to 8. Do not treat EV/hybrid 8 as traction-pack state of charge.
8. Do not skip the ICE Stop combo, and do not apply that belt combo on an electric car.
9. Do not treat a prior MOT belt or battery-security note as the cause of today’s lamp.
10. This skill does not diagnose. If they ask what is wrong, say the lamp does not name the part. If they ask keep-driving or repair-vs-sell, restate **[Drive advice]** and **[Outlook]**.

---

## Pass versus fail

**Pass**

- “Lit with the engine running, this is the charging system, not an instruction to fit a battery.”
- “A garage can usually handle this.” Limited: switch off extras, get it somewhere it can be left.
- “Ask for charging voltage at idle and at raised revs before they sell a battery.” (ICE) / “Ask 12V or DC-DC health before any battery is sold.” (EV / hybrid)
- “If the garage later invoices a 12V battery, published UK figures are …” — only after `repair_cost` `car-battery-replacement-cost`, spoken as invoice class.
- ICE: same pattern for `alternator-replacement-cost` as “if they invoice charging repair,” including “we publish no figure” when null. Do not choose which invoice they will get.
- ICE + heavy steering / rising temp / belt noise: Stop, `poor`, bid as it sits versus estimate. Still no named part.
- EV lamp 8: 12V rectangle, `garage`, battery slug only if invoiced, **no** alternator or belt story.
- Key-on bulb check that went out: not a fault; no outlook; no battery job.
- “The lamp does not name the part.” Restate drive advice and outlook if they ask what is wrong, keep-driving, or repair-vs-sell.
- In-family MOT belt or battery-security note, then: **this does not show the cause of today’s lamp.**

**Fail**

- “It’s a dead battery — fit a new one.” / “Pop a battery in at the supermarket.”
- “It’s the alternator.” / “It’s the belt.” / “Alternator, battery, or wiring” as a closed cause list.
- Calling `car-battery-replacement-cost` because the pictogram is a battery, as if that were the diagnosis.
- Calling `alternator-replacement-cost` as today’s failed part, or on EV lamp 8.
- “About £80–£150 for a battery” / “alternator is about £400” with no tool result.
- Jump-start, charge, or DIY belt steps as a close. “Heaters off will fix it.”
- Mapping a turtle, charge plug, or HV message to 8. Treating hybrid 8 as traction-pack charge.
- Keep driving on the ICE Stop combo, or applying that combo on an electric car.
- “Expect a fail.” Invented trade-in. Shop link above Stop / recovery.
- “Continue as a normal assistant” and then name the battery or the alternator.

**Pass sketch** (illustrative; no live pounds): Your 2016 Fiesta, charging rectangle on with the engine running. Limited: extras off, get it left. Outlook: a garage can usually handle this — charging, not a battery-fit. Ask voltage at idle and raised revs before they sell a battery. If they later invoice a 12V battery or a charging repair, quote those invoice classes; do not pick which.
