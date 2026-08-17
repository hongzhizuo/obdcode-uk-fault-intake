# 61 · Fusion count is not today’s cause

Not a second SKILL. If this note disagrees with `SKILL.md`, `references/prognosis.md`, `references/prognosis-cards.md`, or `references/value-gain.md`, those four win. Do not diagnose. Do not invent pounds. Do not add a 14th lamp id.

Three facts that must stay separate:

1. **`fusion.matched` `count`** — how often the same slug appeared on certificates. Context for **[History]**. Not today’s cause.
2. **`first_used` + fuel** — whether you may talk about this lamp as an in-scope MOT item. Statement / **[Book]** only. Not the repair-or-sell bucket.
3. **The lamp card** — `owner` / `device` / `garage` / `poor`. Age, mileage, and fusion do not move that bucket.

Do not say **Expect a fail**. Do not upgrade `garage` to `poor` because the car is old.

## When

Use this note whenever lookup returned MOT / fusion, or you are about to mention the test, a prior advisory, or whether the lamp is a fail item.

It applies on every Path A lamp. It does not pick a bucket. It does not replace Step 6 cards.

Skip fusion speech when lookup failed or they gave make / year only — one honest **[History]** line that you are working from what they said, then no invented certificates.

## Fusion count is not today’s cause

`fusion.matched` `count` above 1 means the **same slug appeared on more than one certificate**. That is all.

It does **not** mean the defect was never fixed. A later pass can still carry a repeat advisory, or the same wording can return after a repair. It is **not** evidence that today’s lamp is that fault.

`vehicle-lookup.md` once said a repeat entry means “not fixed.” **SKILL Step 4 wins:** count is a repeat of wording, not a live cause.

### What you may put in [History]

Prefer `fusion.matched`. Do not substring-scan raw defect text for `smoke` / `steering` / `valve`.

Include a slug only when it is on the **same-system allowlist for this lamp**. Quote **date** and **`type`**. No causal verbs: not `causing`, `explains`, `related fault`, `so the lamp is…`.

| Lamp | Allowlist family |
|---|---|
| Engine management (6 / 7) | emissions, exhaust, catalyst, lambda — not a diagnosis |
| DPF (9, diesel only) | diesel particulate filter |
| Battery / charging (8) | battery security, auxiliary drive belt |
| Brake system (3) | brake fluid, pipes, hoses, discs, pads |
| ABS (11) | ABS, wheel speed sensor |
| Tyre pressure (10) | tyre condition, tread, valve |
| Power steering (5) | steering, power steering fluid |

No family row (oil, red coolant, airbag, glow, ESC, unmatched EV / AdBlue / GPF unless a card adds one): **one negative line**. Do not invent a family. Do not dump pads, tyres, or rust into an engine-lamp History.

Every History line that names a prior note must end: **this does not show the cause of today’s lamp.** If nothing in-family, one negative line is enough.

Spoken card: no fusion slugs, no advisory URLs, no ids. Date + type + plain English is enough.

### What fusion must not do

- Do not pick a `repair_cost` slug because fusion listed that job (pads on a Stop brake lamp, cat on a steady engine lamp).
- Do not upgrade `garage` or `device` to `poor` because `count` is 2 or 12.
- Do not treat `unmatched_count` as a hidden cause list.
- Do not invent MOT history when lookup missed.

## `first_used` gates MOT talk, not the bucket

`first_used` and fuel decide **whether this lamp is an automatic fail item on this car**. They do **not** choose Close it yourself / garage / weak outlook.

A 2001 petrol with a steady engine lamp can still be `device` then `garage`. A 2024 Fiesta with the same lamp is the same bucket. The difference is only the MOT sentence.

Copy the gate from **SKILL Step 4**, not from `warning-lights.md` “Expect a fail” leftovers:

- **Engine MIL** as a listed fail item: petrol first used on or after **1 July 2003**; diesel (including diesel hybrid) on or after **1 July 2008**. Pure EV: do **not** call the engine lamp an MOT fail item.
- **TPMS** as a listed fail item: M1 first used on or after **1 January 2012**, and only a **malfunction** (often flash-then-steady). A lamp that only means inflate the tyre is not an automatic fail item.
- Other lamps: say the tester **may** record a defect **where that check applies** — only after you have gated first-use / whether the system is fitted. Link the [DVSA inspection manual](https://www.gov.uk/guidance/mot-inspection-manual-for-private-passenger-and-light-commercial-vehicles). Do not recite a verdict.

**In scope:** the tester may record a Major if the lamp still indicates a malfunction — check the manual.

**Out of scope:** this lamp is not an automatic fail item on this car.

If MOT is expired or due within 30 days, add an owner **[Book]** line in the **statement**, not a fail verdict and not a bucket change. You may call `mot-cost` as a booking figure, not as the lamp repair.

`first_used` is also not a sell trigger. An old first-use date does not open **[Sell]**.

## Do not say Expect a fail

Never:

- “Expect a fail”
- “will likely fail as it stands”
- “it will fail MOT until you fix this”

Those lines are banned even when the car is in scope and the lamp is still on.

In scope, point at the manual. Out of scope, say it is not an automatic fail item. A booking reminder is not a prediction.

A missing factory DPF, an illegal exhaust, or a delete is a **value** / defect problem (`71-illegal-mods-negative.md`). Still do not copy “Expect a fail” from lamp speech.

## Age does not upgrade garage to poor

Default bucket is the **lamp card**. `references/prognosis.md`: do not upgrade `garage` to `poor` because the car is old unless they already have a **large estimate**, or the card is already `poor`.

Stay on the card when the only extra fact is age, high mileage, an early `first_used`, or a long fusion list.

| Fact | Moves the bucket? |
|---|---|
| Car is old / high miles / first used before a MIL date | No |
| Fusion `count` ≥ 2 on an in-family slug | No — History only |
| MOT expired or due in 30 days | No — **[Book]** in the statement |
| Lamp card default is `poor` (oil, red coolant, hydraulic brake, flashing engine, DPF limp, AdBlue no-start, ICE charging + belt) | Already `poor` — age did not do that |
| They already have a **large written estimate** | Yes — you may move `garage` → `poor` and open sell |
| Card names its own upgrade (heavy steering on PAS; large SRS quote) | Follow **that** card, not age |

Airbag, ABS, charging without the belt combo, power steering with normal weight, glow that stays on, engine-steady after a read, TPMS malfunction, ESC steady: these stay **`garage`** on a 20-year-old car. Do not open **[Sell]** because “it is not worth fixing at that age” unless they already brought a large estimate or the card says `poor`.

Close-it-yourself still needs a good outlook **and** an owner-safe or device path. Age does not create one. Age does not remove one that the card already allows (inflate, AdBlue top-up, one handbook DPF regen, engine-steady scan).

## Owner copy

History and MOT lines only. Bucket speech stays on the lamp card. No slugs, no URLs, no plates, no pounds.

**In-family note:** On the 2 March 2026 test the tester recorded an advisory for thin front brake pads. This does not show the cause of today’s lamp.

**Nothing in-family:** No emissions-family notes on this car’s MOT record. This does not show the cause of today’s lamp.

**In-scope lamp (after the first-use gate):** If the lamp still indicates a malfunction at the test, the tester may record a Major. Check the DVSA inspection manual. This is not a prediction that the car will fail.

**Out-of-scope lamp:** This lamp is not an automatic fail item on this car.

**Due soon:** MOT is due within 30 days — book the test. Not a repair-or-sell change.

**Old car, garage card:** A garage can usually handle this. Age does not make this a sell decision on its own.

## Red lines

1. Fusion `count` is not “never fixed” and not today’s cause.
2. No causal verbs from History to the lamp.
3. No off-family fusion dump. No raw-text substring hunt.
4. Spoken card: no fusion slugs, no advisory URLs.
5. Do not call a repair slug because fusion named that job.
6. `first_used` + fuel gate MOT sentences only. They do not pick `owner` / `device` / `garage` / `poor`.
7. Never say “Expect a fail” or “will likely fail as it stands.”
8. Do not upgrade `garage` to `poor` because the car is old, unless they have a large estimate or the lamp card is already `poor`.
9. Expired / due-soon MOT is a **[Book]** line, not a weak-outlook trigger.
10. Never invent MOT history. Never print a real plate.

## Pass versus fail

- Pass: “the same note appeared on more than one certificate; this does not show the cause of today’s lamp.”
- Fail: “it has never been fixed, so that is today’s lamp.”
- Pass: in-family slug only; date and `type`; disclaimer on the same line.
- Fail: pads fusion on an engine lamp; “the leak is causing the lamp”; dumping unmatched raw text.
- Pass: petrol first used 1 July 2003 or later — tester **may** record a Major if the MIL still indicates a malfunction; link the DVSA manual.
- Fail: “Expect a fail.” / “it will fail as it stands.”
- Pass: 2002 petrol MIL — out of scope; still `device` then `garage` if that is the card.
- Fail: calling a pre-gate MIL an automatic fail item, or moving that car to `poor` because it is old.
- Pass: TPMS simply on, any year — inflate close; not a listed malfunction fail.
- Fail: “TPMS light means it will fail MOT” on a low-pressure-only lamp.
- Pass: MOT due in 30 days → **[Book]** in the statement; bucket unchanged.
- Fail: due-soon MOT → “Repair may cost more than the car.”
- Pass: 2004 airbag or ABS lamp stays `garage` unless they already have a large estimate or the card says `poor`.
- Fail: “it’s old, not worth fixing — sell it” with no large estimate and a `garage` card.
- Pass: oil-can / flashing engine already `poor` on a new car; age is irrelevant.
- Fail: using fusion count or first-use date to open **[Sell]** on a `garage` or `device` card.
- Pass: `repair_cost` only from the lamp allowlist, never from a fusion slug.
- Fail: calling `brake-pads-and-discs-cost` or cat cost because History mentioned pads or a catalyst.
