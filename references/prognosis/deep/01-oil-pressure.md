# 1 `oil-pressure` — red oil-can

Not a second SKILL. If this file disagrees with `SKILL.md`, `references/prognosis.md`, `references/prognosis-cards.md`, or `references/value-gain.md`, those four win.

**Id:** `oil-pressure` (circled **1**)  
**Default bucket:** `poor`  
**Owner hears:** Repair may cost more than the car  
**Drive advice (statement):** Stop. Do not drive it in. Ask the garage to collect, or call recovery.

## When

Run Step 6 in the **same turn** as the fault statement when the showing lamp is the **red oil-can** (named, or circled 1 on a petrol / diesel / hybrid / unknown ICE board).

Skip this file when:

- The oil-can was a **key-on bulb check** and then went out — not a fault; no outlook.
- The board is **electric**. Slot 1 is not printed. Do not map a turtle, HV text, or lamp 8 to this card.
- They asked only about wrap / service / value and **no** lamp — that is `value-gain.md`, not this lamp.

If they have this lamp **and** named a modification, finish **[Drive advice]** and this outlook first, then a separate **[Value]** block. A wrap does not close an oil-can.

Age does not change this bucket. The lamp is already `poor` on a new car. Do not upgrade to a driveway close because the dipstick looks fine.

Vans use the same bucket. Say **your Transit**. Downtime is “a day off the road,” not a made-up day-rate.

This car’s MOT fusion has **no** same-system allowlist for this lamp. One negative History line. Do not dump unrelated slugs. Do not say the lamp is an automatic MOT fail.

## Owner copy

≤120 words. Spoken **[Outlook]** after the statement (~40–60 of these). Stop / recovery already sits in **[Drive advice]** — do not put a shop or scanner link above it.

Repair may cost more than the car. We publish no figure for this class of work. Get one bid as it sits — it is not a runner — and one written estimate. Recovery is part of the sell cost. Compare those two before you authorise any engine job. Do not restart. A cold dipstick reading is information for the garage, not a close. The lamp does not name the part. This skill does not diagnose.

## Repair_cost slugs

**Call none.** The allowlist is empty. There is **no** published engine-rebuild job. Do not hunt a nearby slug.

Do **not** call:

- `car-diagnostic-test-cost` — a reader does not close this lamp
- `head-gasket-repair-cost`, `alternator-replacement-cost`, `clutch-replacement-cost`, or any other published job because you want a number

`gbp: null` is not a gap to fill. Say: we publish no figure for this class of work. Two written estimates **only if** they have already recovered the car and a garage is quoting. A cost page is not the failed part.

## Sell talk

Weak outlook only — this is that case.

1. Repair: no published figure (see slugs).
2. Sell: we publish no used-car price. Get **one** instant-sale or dealer bid **as the car sits** (for parts if it must not be driven — usually not a runner). Get **one** written garage estimate.
3. If the estimate is larger than the bid, selling is often the better outlook.
4. Recovery / collection is part of the sell cost because **[Drive advice]** is Stop. Do not invent that fee.

Do not say the car is a write-off. Do not invent Parkers / WeBuyAnyCar / trade-in pounds. If they ask repair vs sell, restate **[Drive advice]** and **[Outlook]**.

## Close-it-yourself

**No.** Outlook is `poor`. Red-class work is never a driveway or scan-tool close.

Once the engine is **completely cold**, a dipstick reading is **information** for the garage (level, and whether anything is on the floor). It does **not** make it safe to restart. It does **not** close the lamp. Do not top up and drive. Do not “just pop it to the garage.” Do not plug in a reader as a fix. Do not clear codes.

Owner facts (how long the lamp was on, any noise, last oil change) go in **[Since]** or **[Ask the garage]** — process, not a parts shortlist.

## Red lines

1. Do not name the pump, the sender, or a bearing. Do not give DIY switch, sender, or pressure-test steps.
2. Do not diagnose. Do not say which part failed. The lamp does not name it.
3. No invented pounds for repair, sell, recovery, or “typical rebuild.”
4. No SAE J2012 wording or fault-code definition tables.
5. No real registration in this file or in speech. If a worked plate is required, only `AB12CDE`; then call it **your 2016 Fiesta**.
6. Safety before commerce. No scanner, shop, or parts link above Stop / recovery.
7. Never advise clearing the lamp. Never treat a cold dipstick as permission to drive.
8. Do not instruct wrap, remap, or filter delete. Value-gain may state price effect only, after this outlook.

## Pass vs fail

| Pass | Fail |
|---|---|
| Stop. Do not drive it in. Recovery or collection. | “Drive it slowly to the garage.” |
| Repair may cost more than the car. We publish no figure. Two written estimates if they are already quoting. | “A rebuild is about £2,000–£4,000.” Any guessed GBP. |
| Get one bid as it sits (not a runner). Compare it with the estimate. Recovery is part of sell cost. | Invented trade-in. “It’s a write-off.” Parkers / WeBuyAnyCar pounds. |
| A cold dipstick is information, not a close. Do not restart. | “Level is fine, you’re safe to go.” “Top it up and it’ll go out.” |
| The lamp does not name the part. This skill does not diagnose. | Naming the pump, sender, or a bearing. DIY switch steps. |
| Empty slug list. Do not call `repair_cost`. | Calling diagnostic-test (or any slug) so there is a number. |
| If they ask what is wrong: no diagnosis; restate drive advice and outlook if they ask repair vs sell. | “Continue as a normal assistant” and then name a part. |
| Your 2016 Fiesta / your Transit. | A real plate in git or speech. |

**Pass sketch** (illustrative; no live pounds): Your 2016 Fiesta, red oil-can. Stop; do not drive it in; recover it. Outlook: repair may cost more than the car. We publish no figure. Bid as it sits versus a written estimate. Do not restart. A cold dipstick is not a close.
