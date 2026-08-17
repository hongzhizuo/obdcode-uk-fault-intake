# 93 · PAS lamp — Limited unless already heavy (then Stop / `poor`)

Not a second SKILL. If this file disagrees with `SKILL.md`, `references/prognosis.md`, `references/prognosis-cards.md`, or `references/value-gain.md`, those four win. Full lamp card: `05-power-steering.md`. Do not diagnose. Do not invent pounds. Do not add a 14th lamp id.

This note is the **drive-advice fork** only: Limited while they can still steer; **Stop and `poor`** once the wheel has gone heavy.

**Id:** `power-steering` (circled **5**)  
**Symbol:** steering wheel with an exclamation mark  
**Colour:** red or amber depending on the car — **colour does not set Stop**  
**safety_class:** Red (no owner repair; **not** Stop by itself)  
**Repair slugs:** **none** — no published PAS job  
**Close-it-yourself:** No

`safety_class: Red` is not Stop. Airbag stays Limited. PAS is the lamp that **escalates**: Limited unless the steering is already heavy, then Stop and weak outlook.

---

## When

Run this fork in the **same turn** as the fault statement when the showing lamp is PAS (named, or circled **5** on petrol / diesel / hybrid / electric / unknown). Slot 5 is live on every board.

| Facts | Drive advice | Bucket | Owner hears |
|---|---|---|---|
| Lamp on, steering still feels **normal** (or they added nothing — default “drives normally”) | **Limited:** drive directly there, no extra journeys | `garage` | A garage can usually handle this |
| Steering **already heavy**; they cannot safely get there | **Stop:** do not drive it in; garage collect, or call recovery | `poor` | Repair may cost more than the car |

Skip when:

- Key-on **bulb check** that then went out — not a fault; no outlook.
- Wrap / service / value and **no** lamp — that is `value-gain.md`.

Do **not** quiz “is the steering heavy?” as a parking-brake-style gate. After a valid pick: drive advice in that turn, then one optional “anything feel different?” If they do not add more, default **just now / drives normally** → Limited / `garage`. If they already said the wheel is heavy, or they say so later, **upgrade** to Stop / `poor`. Do not ask if they are driving.

Do **not** Stop this lamp because it is red. Do **not** stay Limited once the steering is already heavy. Do **not** upgrade to `poor` because the car is old. A large written PAS estimate they already hold can move speech to weak outlook while they can still steer; age cannot.

This is **not** lamp 8. Do not apply the ICE charging Stop combo (belt noise / rising temperature / heavy steering on the **charging** rectangle) as the test for PAS. On this id, Stop is **steering feel**. If they also named a charging lamp, still do not name a belt. On an **electric** car: same Limited / Stop fork; **no** belt / water-pump combo. Heavy steering is still Stop / `poor`.

Vans: same buckets. Say **your Transit**. Downtime is “a day off the road,” not a made-up day-rate.

History (statement, not outlook): same-system MOT notes only — steering, power steering fluid. Quote date and `type`. No causal verbs. End: **this does not show the cause of today’s lamp.** One negative line if nothing in-family.

MOT: a power-steering malfunction lamp can be a listed defect **where that check applies**. Link the [DVSA inspection manual](https://www.gov.uk/guidance/mot-inspection-manual-for-private-passenger-and-light-commercial-vehicles). Never say “Expect a fail.”

If they have this lamp **and** named a modification, finish **[Drive advice]** and this outlook first, then a separate **[Value]** block.

---

## Owner copy

≤120 words. Spoken **[Outlook]** after the statement (~40–60 of these). No ids, fusion slugs, URLs, plates, or pounds. Stop / recovery already sits in **[Drive advice]** when the wheel is heavy — no shop or scanner link above it. No `[Close it]` on either branch. No `[Sell]` on Limited / `garage`.

### Limited — lamp on, steering still normal (`garage`)

A garage can usually handle this. Drive directly to a workshop — no extra journeys. Red here means no owner repair, not Stop. We publish no figure for this class of job. Ask two garages for a written estimate. The lamp does not name the part. If the steering goes heavy, stop: do not drive it in; ask the garage to collect, or call recovery. Do not top up fluid to close it.

(73 words.)

### Stop — steering already heavy (`poor`)

The steering has gone heavy. Stop. Do not drive it in. Ask the garage to collect, or call recovery. Repair may cost more than the car. We publish no figure for this class of job — two written estimates. We publish no used-car price. Get one bid as it sits — it may need collection — and compare it with the estimate. Recovery is part of the sell cost. The lamp does not name the part.

(76 words.)

Owner facts (heavy all the time, only when cold, only at parking speed; both directions or one; any whine; whether a charging lamp or temperature gauge also changed) go in **[Since]** or **[Ask the garage]** — process, not a parts shortlist.

---

## Repair_cost slugs

**Call none.** There is **no** published PAS slug. Empty allowlist means **we publish no figure** — two written estimates. That is the answer. Do not hunt a nearby job.

Do **not** call:

- any PAS / EPS / rack / pump / column / fluid job (none is published)
- `car-diagnostic-test-cost` (not on this allowlist; a scan at the garage is still process speech, not a slug you fetch here)
- `alternator-replacement-cost` or `car-battery-replacement-cost` because a charging lamp was also mentioned
- clutch, cat, pads, belts, MOT, or any other published job because you want a number

Never pick a slug because it is the only one with a number. Never treat a cost page as the failed part. `gbp: null` / `no_verified_price` / `no_published_job` is not a gap to fill. Never invent GBP.

---

## Sell

Not first-line on Limited / `garage`. Do not push selling while they can still steer to a workshop.

Sell talk **only** on the Stop / already-heavy branch (`poor`), or if they already hold a large written PAS estimate:

1. Repair: no published figure. Two written estimates.
2. Sell: we publish no used-car price. Get **one** instant-sale or dealer bid **as the car sits** (for parts if it must not be driven). Get **one** written garage estimate.
3. If the estimate is larger than the bid, selling is often the better outlook.
4. Recovery / collection is part of the sell cost because **[Drive advice]** is Stop. Do not invent that fee. Do not tell them to drive it to a buyer.

Do not say write-off. Do not invent Parkers / WeBuyAnyCar / trade-in pounds. Limited runner: recovery is **not** automatic sell cost.

If they ask repair vs sell, or keep-driving: restate **[Drive advice]** and **[Outlook]**.

---

## Close-it-yourself

**No** on both branches. Outlook may be `garage` (good) but this is still Red-class. Close-it-yourself needs a good outlook **and** an owner-safe or device step. Neither applies. A reader does not close PAS. Do not clear the lamp.

- No fluid-for-life guessing. Do not invent a reservoir, a spec, or a top-up that puts the lamp out. Do not flush or bleed PAS.
- A reservoir glance **only if the handbook shows one** is **information** for the garage. It is not a close. Many cars have electric PAS and nothing to check.
- Noting whether it is heavy is classification for this fork, not a diagnosis and not a close.
- Device and shop links stay below Stop / recovery. This path has no `[Close it]` block.

---

## Red lines

1. Limited unless the steering is already heavy. Then Stop and `poor`. Colour does not set that. Red is not Stop by itself.
2. Do not stay Limited, “pop to the garage,” or “drive slowly” once the wheel is heavy.
3. Do not recover a normal-steer PAS lamp by default (that is airbag-style over-Stop).
4. Do not diagnose. Not the pump, rack, column, EPS motor, torque sensor, fluid, or auxiliary belt — even as a shortlist.
5. No published PAS slug. Do not call `repair_cost`. Do not hunt diagnostic-test or charging slugs.
6. No invented pounds for repair, sell, recovery, or “typical PAS jobs.”
7. Never advise clearing the lamp. Never treat a fluid top-up as a close.
8. Safety before commerce. No scanner, shop, or parts link above a Stop line.
9. Do not say “Expect a fail.” Prior MOT steering notes do not show the cause of today’s lamp.
10. No SAE J2012 wording. No real registration. Illustrative only: `AB12CDE`, then **your 2016 Fiesta** / **your Transit**.
11. On an EV, do not apply the ICE charging-belt combo. Heavy steering is still Stop.
12. Do not ask if they are driving. Do not say “continue as a normal assistant.”

---

## Pass vs fail

| Pass | Fail |
|---|---|
| Lamp on, steering still normal → **Limited.** Drive directly there, no extra journeys. Bucket `garage`. | Recover / Stop a PAS lamp that still steers normally because it is red. |
| Steering already heavy → **Stop.** Do not drive it in. Recovery or collection. Bucket `poor`. | “Keep driving, it’s only the lamp.” “Drive it slowly to the garage” once the wheel is heavy. |
| Red means no owner repair, not pull-over-now — until the steering is heavy. | Treating `safety_class: Red` as Stop on a normal-steer PAS lamp. Treating airbag and PAS as the same Stop rule. |
| Default if they add nothing: drives normally → Limited / `garage`. Optional “anything feel different?” | Parking-brake-style “is the steering heavy?” gate. “Are you still driving?” |
| Colour (red or amber) does not set Stop. | “It’s amber so you’re fine to finish the week.” “It’s red so recover it” with no heavy-steer fact. |
| “A garage can usually handle this” on Limited. | Close-it-yourself / reader / fluid top-up as the close. |
| Heavy: “Repair may cost more than the car.” Bid as it sits vs written estimate. Recovery is part of sell cost. | Pushing sell on a normal-steer garage path with no large quote. “Drive it to WeBuyAnyCar.” |
| We publish no figure — two written estimates. Empty allowlist. Do not call `repair_cost`. | “PAS jobs are about £400–£800.” Any guessed GBP. Calling diagnostic-test, battery, or alternator so there is a number. |
| The lamp does not name the part. This skill does not diagnose. | “It’s the pump / rack / EPS motor / belt.” Shared-belt as today’s cause. |
| Reservoir glance only if the handbook shows one: information, not a close. | “Top up the fluid-for-life reservoir and the lamp will go out.” Flush, bleed, belt, calibration, or lift how-to. |
| ICE charging Stop combo is lamp **8**, not this fork. PAS Stop is steering feel. EV: no belt combo; heavy still Stop. | Stopping PAS because the charging lamp or temperature gauge moved, while the steering still feels normal. Belt story on an EV. |
| Do not upgrade to `poor` because the car is old. | Weak outlook from age or high miles with a normal-feeling wheel. |
| In-family MOT steering / PAS-fluid note, then: **this does not show the cause of today’s lamp.** | “The old leak is causing today’s lamp.” “Expect a fail.” |
| Restate **[Drive advice]** and **[Outlook]** if they ask keep-driving, recovery, or repair-vs-sell. | “Continue as a normal assistant” and then name a part. |
| Your 2016 Fiesta / your Transit. | A real plate in git or speech. Shop or scanner link above a Stop line. |

**Pass sketch (Limited):** Your 2016 Fiesta, PAS lamp, steering still normal. Limited — drive directly to a garage, no extra journeys. Outlook: a garage can usually handle this. We publish no figure. Two written estimates. The lamp does not name the part. If it goes heavy, stop and recover it.

**Pass sketch (heavy / Stop / poor):** Your 2016 Fiesta, PAS lamp, steering gone heavy. Stop; do not drive it in; recover it. Outlook: repair may cost more than the car. We publish no figure. Bid as it sits versus a written estimate. Recovery is part of the sell cost. The lamp does not name the part.

**Fail sketch:** “Red PAS light — recover it. It’s the pump. About £600. Or top up the PAS bottle and drive it in.”
