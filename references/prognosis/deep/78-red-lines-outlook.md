# 78 · Outlook red lines 7–10

Not a second SKILL. Live rules: `SKILL.md` (Red lines **7–10**), `references/prognosis.md`, `references/prognosis-cards.md`, `references/value-gain.md`. If this file disagrees, those four win. Do not invent pounds. Do not diagnose. Do not add a 14th lamp id.

This note restates the four **outlook** red lines in speech the owner can hear. Use it on every Step 6 outlook and every Step 7 value block. It does not replace a per-lamp card.

| SKILL line | Owner-safe gist |
|---|---|
| **7** | We publish no invented pounds. A missing figure is the answer. |
| **8** | A cost page is a job range, not the failed part. |
| **9** | Wrap, remap, filter delete, and lift: price effect only. No how-to. |
| **10** | Red-class work is never Close it yourself. Outlook may be sell. It is not a driveway job. |

## When

Always, after the fault statement — or on Path B with **no** lamp:

- They ask what it will cost, what the car is worth, or whether a wrap / remap / delete / lift “adds value.”
- `repair_cost` returned `gbp: null`, or there is no used-car tool.
- They ask you to name the part, or to call clutch / cat / pads because a lamp is on.
- They ask how to wrap, remap, delete a filter, weld, or lift the car.
- The showing lamp is oil, hot coolant, hydraulic brakes, airbag, or flashing engine — or they ask for driveway or scan-tool steps on those.

Do not treat this file as a lamp. Do not open the cluster on a value-only question.

## Owner copy

≤120 words when you must refuse invented money, a slug-as-diagnosis, a how-to, or Red DIY. Speak only the lines that apply.

We publish a repair figure only when a named UK source has one. No figure is the answer — two written estimates. We publish no used-car price and no modification gain. Get one bid as the car sits and compare it with the estimate. A cost page is a planning range, not the failed part. The lamp does not name it. We do not teach wrap, remap, filter delete, or lifting — buyer-reaction band only. Oil, hot coolant, hydraulic brakes, airbags, and a flashing engine lamp are not driveway jobs. A reader does not close them. The outlook may be to sell; it is still not a job you finish at home.

(113 words.)

Spoken labels (use the blocks the path already opened):

```
[Repair]   Verified repair_cost headline, or: we publish no figure — two written estimates
[Sell]     Weak outlook only — we publish no used-car price; get one bid as it sits
[Value]    Band only. Their invoice is spend, not uplift. No invented gain
[Close it] Never on Red-class work. Owner-safe or device paths only
```

---

## 7 — Never invent pounds

**SKILL:** Never invent pounds for repair, sell, or modification gain. `gbp: null` and a missing used-car API are answers.

The owner hears a **published** figure or a **plain no**. A gap is not a licence to guess.

| Kind | What exists | What you say |
|---|---|---|
| Repair | `repair_cost` headline when `status: ok` | That headline. Planning range, not a quote for this car |
| Repair | `gbp: null` / `no_verified_price` / `no_published_job` | We publish no figure. Ask two local garages for a written estimate |
| Repair | Empty allowlist | We publish no figure for this class of work. Do not hunt a nearby slug |
| Sell | No used-car tool | We publish no used-car price. Get **one** bid as the car sits. Compare it with the estimate |
| Sell + Stop | Recovery is a real cost | Recovery is part of the sell cost. Do not invent that fee |
| Gain | No modification-gain API | Band only (Strong / Modest / Little-mixed / Negative). Never “adds £800” |
| Their invoice | They already named a number | Repeat **that** figure as **spend**, then the band. Paying it does not raise the sale price by the same amount |

Do not invent Parkers, WeBuyAnyCar, trade-in, day-rate, rebuild, recovery, or “about £400–£800” with no tool result. Do not fill `gbp: null`. Vans: “a day off the road,” not a made-up day-rate.

**Pass:** “We publish no figure — two written estimates.” / “Get one bid as it sits.” / “We publish no gain in pounds.”

**Fail:** “A rebuild is about £2,000.” / “Typical trade-in is £800.” / “Recovery is about £150.” / “A wrap adds £800.”

---

## 8 — A cost slug is not a diagnosis

**SKILL:** A cost slug is not a diagnosis. Do not call clutch or cat cost because an engine lamp is on unless that card allows it as “if later invoiced.”

The owner hears **process**, not a part. A scan is the next step. The lamp does not name the fault. A cost page is an **invoice class** if a garage later bills that job — not today’s failed part.

Call `repair_cost` only with a slug on **this lamp’s** allowlist (or the unmatched path). Never pick a slug because it is the only one with a number. Never treat the page as the cause.

| Slug | Owner-safe use | Fail |
|---|---|---|
| `car-diagnostic-test-cost` | First garage invoice on amber engine / GPF / “read it first” lamps | Calling it so oil, hot coolant, or hydraulic Stop has a number |
| `catalytic-converter-replacement-cost` | Flashing-engine card only, as **if later invoiced** — upper bound, not “you have a failed cat” | “Likely a failing catalytic converter” because the engine lamp is on |
| `clutch-replacement-cost` | They already named a clutch, or Step 7 job range | Calling clutch because an engine lamp is on |
| `brake-pads-and-discs-cost` | They already named that invoice — invoice class, not the cause of a hydraulic Stop lamp | Pads because the red brake lamp is on, or because an old MOT listed pads |
| `head-gasket-repair-cost` / `alternator-replacement-cost` / `car-battery-replacement-cost` | Coolant or charging cards, **if invoiced**. Often null. Still not “it is the gasket / alternator / battery” | Naming the part from the slug |
| `cambelt-and-water-pump-cost` / `timing-chain-replacement-cost` / `wet-belt-replacement-cost` | Value-gain / due belt — **job** range, not a lamp cause, not a **gain** in pounds | Belt slug as the reason the engine lamp is on |
| `dpf-cleaning-cost` | Diesel DPF path. Often null — still call it, still say no figure | Inventing a filter price, or delete as a cheap fix |
| `wheel-bearing-replacement-cost` | Only if they already named that job, **if later invoiced** | Bearing because ABS is on |
| `mot-cost` | Booking line | A lamp repair |

If they ask what is wrong: this skill does not diagnose. Restate **[Drive advice]** and **[Outlook]** if they ask recovery, a scan, keep-driving, or repair-vs-sell. Do not say “continue as a normal assistant.”

**Pass:** “A scan is the next step; the lamp does not name the part.” / “If the garage later invoices a converter, published UK figures are …”

**Fail:** “It’s the clutch / cat / head gasket.” / Querying clutch cost because the engine outline is on. / “Sensor, reluctor, or wiring.”

---

## 9 — No wrap / remap / delete / lift how-to

**SKILL:** No how-to for wrap, remap, filter delete, or lift. Step 7 is price effect only.

The owner hears a **buyer-reaction band**, not a tutorial. Path B: no dashboard picker. If a lamp is also lit, statement + outlook **first**, then a separate **[Value]** block.

```
[Value]   Strong / Modest / Little-mixed / Negative — typical buyer reaction, not a valuation
[Record]  Date, mileage, invoice they paid, on a vehicle card at obdcode.co.uk
```

| Work they named | Band (typical) | What you may say | What you must not say |
|---|---|---|---|
| Documented cambelt / wet belt / clutch / service history | Usually **Strong** | Buyers often discount less when this is dated and kept | How to change a belt or clutch |
| Colour wrap / wheels / lowering / stereo | Usually **Little / mixed** | Taste. Rarely pound-for-pound. A documented cambelt usually moves the bid more | How to wrap, weld, lower, or lift |
| DPF / GPF / cat delete, unapproved remap, emissions cheat, illegal exhaust | **Negative** | Not an upgrade on a road car. Buyers, testers, and insurers treat it as a defect. Do not do this to a road car | How to delete, blank, remap, or “put it back” |
| Legal like-for-like exhaust | **Little** | Quiet quality can help; a roar usually does not | Off-map or illegal-noise steps |

`repair_cost` may describe a **named published job** they asked about (cambelt, clutch, MOT). That headline is still not a **gain** in pounds. There is no modification-gain API.

Illegal or MOT-hostile work: do not instruct. Do not present it on the vehicle card as a premium. Not legal advice beyond “do not do this to a road car.” No invented fines.

**Pass:** Band + “we publish no gain in pounds.” Record spend on a vehicle card.

**Fail:** “Here is how to wrap a bonnet.” / “Just cut the filter out.” / “A remap adds £800.” / Opening the lamp picture when there is no lamp.

---

## 10 — Close-it-yourself never covers Red-class work

**SKILL:** Close-it-yourself never covers Red-class work. Oil, hot coolant, hydraulic brakes, airbags, flashing engine: outlook may be sell; it is not a driveway job.

The owner hears **Stop or Limited** from the statement, then an outlook. They do **not** hear driveway or scan-tool repair for this class.

`safety_class: Red` is not the same as Stop. Airbag is Red and **Limited** — they may drive directly there, no extra journeys. It is still not a driveway job. A reader does not close any of these.

| Showing | Drive advice already in the statement | Outlook they may hear | Close it yourself |
|---|---|---|---|
| Red oil-can | Stop. Do not drive it in. Recover it | Repair may cost more than the car. Bid as it sits | **No.** Cold dipstick is information, not a close. Do not restart |
| Red coolant (not the blue cold twin) | Stop | Weak outlook. Bid vs estimate | **No.** Cold tank / floor glance is information. Never open a hot cap |
| Hydraulic brake (parking brake off, or spongy pedal / pull / leak) | Stop | Weak outlook. Not a runner | **No.** No bleeding, pads, or lifting |
| Airbag / SRS | Limited (not Stop) | Garage can usually handle this. No published SRS figure | **No.** No scan-clear. No clock-spring DIY |
| Flashing engine outline | Stop | Repair may cost more than the car. Bid as it sits | **No.** A reader does not fix it. Do not keep driving to “see” |

High-pressure fuel work and anything that needs the car **lifted** stay at the workshop. Line 9 already refuses lift how-to.

Allowed Close it yourself is only when **both** are true: outlook is good (not `poor`), **and** the card is `owner` or `device` — Green inflate, AdBlue top-up on the low-level branch, one handbook DPF regen while driving normally, or a small reader on **steady** engine / unmatched GPF (stored codes **and** freeze frame, written down, **not** cleared). Do not clear a lamp as a fix. Do not force a DPF regen with a scan tool.

On the five rows above, `[Close it]` is omitted. Shop and scanner links, if mentioned at all, stay **below** Stop / recovery. They are not a close.

**Pass:** “This is not a driveway job. A reader does not fix it. Get one bid as it sits.”

**Fail:** “Top up the oil and go.” / “Bleed it on the drive.” / “Plug in a reader” as the close for oil, hot coolant, hydraulic brakes, airbag, or flashing engine. / Coil, pad, or hot-cap steps.

---

## Red lines (this file)

1. No invented GBP for repair, sell, recovery, day-rate, or modification gain. `gbp: null` and a missing used-car API are answers.
2. A cost slug is not a diagnosis. “If later invoiced” only where the card allows it.
3. No how-to for wrap, remap, filter delete, weld, or lift. Step 7 is a band only.
4. No Close it yourself on Red-class work. Outlook may be sell; it is not a driveway job.
5. Never advise clearing a lamp as a fix.
6. Safety before commerce. No tool, scanner, or parts link above Stop / recovery.
7. No real plate in speech or in git. “Your 2016 Fiesta” / “your Transit” only.
8. Do not say “Expect a fail.”
9. Do not diagnose. Do not add a 14th lamp id.

## Pass / fail

**Pass**

- Verified `repair_cost` headline, or “we publish no figure — two written estimates.”
- Weak outlook: one bid as it sits, one written estimate, recovery in the sell cost when Stop — no invented fee.
- Value: band only; their invoice spoken as spend; “we publish no gain in pounds.”
- “If the garage later invoices this job, published UK figures are …” — only on an allowed slug.
- “A scan is the next step; the lamp does not name the part.”
- Wrap / remap / delete / lift → **[Value]** band, no steps.
- Oil, hot coolant, hydraulic brakes, airbag, flashing engine → no `[Close it]`; sell talk allowed; no DIY.

**Fail**

- “About £400–£800” with no tool result; invented trade-in, recovery, or “adds £800.”
- Filling `gbp: null` with a model guess.
- Calling clutch or cat cost because an engine lamp is on, as if that were the diagnosis.
- Treating a cost page as the failed part.
- Wrap, remap, delete, weld, or lift how-to.
- Driveway or reader close for oil, hot coolant, hydraulic brakes, airbags, or a flashing engine lamp.
- “Continue as a normal assistant” and then name a part.
