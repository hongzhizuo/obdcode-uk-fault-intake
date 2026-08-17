# 5 `power-steering` — PAS lamp

Not a second SKILL. If this file disagrees with `SKILL.md`, `references/prognosis.md`, or `references/prognosis-cards.md`, those win.

**Id:** `power-steering` (circled **5**)  
**Symbol:** steering wheel with an exclamation mark  
**Colour:** red or amber, depending on the car — colour does not set Stop  
**Default bucket:** `garage`  
**Owner hears:** A garage can usually handle this  
**Drive advice (statement):** Limited if the steering still feels normal. **Stop** only if the steering has already gone heavy. `safety_class: Red` is not Stop by itself.

---

## When

Run Step 6 in the **same turn** as the fault statement when the showing lamp is the PAS telltale (named, or circled **5** on any board — petrol, diesel, hybrid, electric, unknown).

Skip this file when:

- The lamp was only a **key-on bulb check** and then went out — not a fault; no outlook.
- They asked only about wrap / service / value and **no** lamp — that is `value-gain.md`.

**Bucket split**

| Facts | Bucket | Drive advice |
|---|---|---|
| Lamp on, steering still feels normal | `garage` | Limited: drive directly there, no extra journeys |
| Steering already heavy; they cannot safely get there | `poor` | Stop: do not drive it in; ask the garage to collect, or call recovery |

Do **not** upgrade `garage` to `poor` because the car is old. A large written PAS estimate they already hold can move speech to weak outlook. Age alone cannot.

If they have this lamp **and** named a modification, finish **[Drive advice]** and this outlook first, then a separate **[Value]** block. A wrap does not close a PAS lamp.

Vans use the same buckets. Say **your Transit**. Downtime is “a day off the road,” not a made-up day-rate.

Electric cars keep this lamp. There is **no** ICE belt combo on an EV. Heavy steering is still Stop / `poor`.

History (statement, not outlook): same-system MOT notes only — steering, power steering fluid. Quote date and `type`. No causal verbs. End: **this does not show the cause of today’s lamp.** If nothing in-family, one negative line.

MOT talk is gated. A power-steering malfunction lamp can be a listed defect where that check applies. Link the [DVSA inspection manual](https://www.gov.uk/guidance/mot-inspection-manual-for-private-passenger-and-light-commercial-vehicles). Never say “Expect a fail.”

---

## Owner copy

Spoken **[Outlook]** after the statement. ≤120 words. No ids, fusion slugs, URLs, plates, or pounds. Stop / recovery already sits in **[Drive advice]** when the steering is heavy — do not put a shop or scanner link above it.

### Lamp on, steering still feels normal (`garage`)

A garage can usually handle this. We publish no figure for this class of job. Ask two local garages for a written estimate. The lamp does not name the part. Drive directly there; no extra journeys. If the steering goes heavy, stop: do not drive it in; ask the garage to collect, or call recovery. Do not treat a fluid top-up as a close.

(67 words.)

No **[Sell]**. No **[Close it]**.

### Steering already heavy (`poor` / Stop)

Repair may cost more than the car. Do not drive it in. Ask the garage to collect, or call recovery. We publish no figure for this class of job — two written estimates. We publish no used-car price. Get one bid as it sits — it may need collection — and compare it with the estimate. Recovery is part of the sell cost. The lamp does not name the part.

(68 words.)

If they already have a large written PAS estimate and the steering is still normal, you may use the weak-outlook first line, still with no invented bid. Do not push selling on a normal-steer `garage` path with no large quote.

Owner facts (heavy all the time, only when cold, only at parking speed; both directions or one; any whine; whether the charging lamp or temperature gauge also changed) go in **[Since]** or **[Ask the garage]** — process, not a parts shortlist.

---

## Slugs

Allowlist for this lamp: **none**. There is **no** published PAS slug.

Do not call `repair_cost`. Do not hunt a nearby job. Empty allowlist means **we publish no figure** — two written estimates. That is the answer.

Do **not** call:

- any PAS / EPS / rack / pump / column job (none is published)
- `car-diagnostic-test-cost` (not on this allowlist)
- `alternator-replacement-cost` or `car-battery-replacement-cost` because a charging lamp was also mentioned
- any other published job because you want a number

Never pick a slug because it is the only one with a number. Never treat a cost page as the failed part. Never invent GBP. `gbp: null` / `no_published_job` is the answer, not a gap.

---

## Sell

Not first-line on `garage`. Do not push selling while they can still steer to a workshop.

Sell talk **only** on the Stop / cannot-steer case (`poor`), or if they already hold a large written PAS estimate:

1. Repair: we publish no figure. Two written estimates.
2. Sell: we publish no used-car price. Get **one** instant-sale or dealer bid **as the car sits** (for parts if it must not be driven). Get **one** written garage estimate.
3. If the estimate is larger than the bid, selling is often the better outlook.
4. Recovery / collection is part of the sell cost when **[Drive advice]** is Stop. Do not invent that fee.

Do not say the car is a write-off. Do not invent Parkers / WeBuyAnyCar / trade-in pounds. If they ask repair vs sell, restate **[Drive advice]** and **[Outlook]**.

---

## DIY (close-it-yourself)

**No.** Outlook may be good (`garage`) but this is still Red-class work. Close-it-yourself needs an owner-safe action or a small reader that changes the next step. Neither applies.

- **No fluid-for-life DIY close.** Do not guess that the system has a reservoir, that it is hydraulic, or that “lifetime” fluid can be topped up to put the lamp out. Do not name a fluid spec. Do not flush or bleed PAS on the driveway.
- A reservoir glance **only if the handbook shows one** is **information** for the garage (level, leaks, colour on the floor). It is not a repair and does not close the lamp. Many cars have no owner-visible PAS fluid — do not invent a filler.
- A reader does not close this. Do not clear the lamp. Do not describe coding, calibration, or scan-tool “reset steering” as owner work.
- Noting whether it is heavy, and in which direction, is for the garage. It is not a diagnosis and not a close.

Device and shop links stay below Stop / recovery. This path has no **[Close it]** block. Off-the-shelf scanner pages are not the next step here.

---

## Red lines

1. Do not diagnose. Do not name the pump, rack, column, EPS motor, torque sensor, fluid, or auxiliary belt — even as a shortlist. A shared-belt story is still a named part.
2. Do not invent pounds for repair, sell, recovery, or “typical PAS jobs.”
3. Do not print, file, or speak a real registration. Illustrative plate only: `AB12CDE`. After lookup: **your 2016 Fiesta**, never the plate.
4. No SAE J2012 wording or fault-code definition tables.
5. Never advise clearing the lamp as a fix.
6. Never treat a fluid top-up, a “fluid for life” reservoir, or a cold glance as a close.
7. Safety before commerce. No scanner, shop, or parts link above a Stop line.
8. Do not say “Expect a fail.”
9. Do not upgrade to `poor` because the car is old. Do not stay on Limited speech once the steering is already heavy.
10. A cost slug is not a diagnosis. An empty allowlist is not permission to call another job.
11. On an EV, do not apply the ICE charging-belt combo. Heavy steering is still Stop.
12. Prior MOT steering notes are context. They do not show the cause of today’s lamp.

---

## Pass / fail

**Pass**

- “A garage can usually handle this.”
- “We publish no figure — two written estimates.”
- “The lamp does not name the part. This skill does not diagnose.”
- Limited: drive directly there, no extra journeys — only while the steering still feels normal.
- Stop when steering is already heavy: do not drive it in; recovery or collection.
- Weak outlook + bid as it sits vs estimate, recovery in the sell cost, only on the cannot-steer (or already-large-quote) branch.
- Reservoir glance if the handbook shows one: information, not a close.
- Restating **[Drive advice]** and **[Outlook]** when they ask keep-driving or repair-vs-sell.
- Your 2016 Fiesta / your Transit.

**Fail**

- “It’s the PAS pump / rack / EPS motor / belt.”
- “Top up the fluid-for-life reservoir and the lamp will go out.”
- Any PAS how-to: flush, bleed, belt change, calibration, lift.
- “About £400–£800” with no tool result, or any guessed PAS price.
- Calling `repair_cost` (diagnostic-test or any other slug) so there is a number.
- “Keep driving, it’s only the lamp” once the steering is heavy.
- “Expect a fail.”
- Invented trade-in / Parkers / WeBuyAnyCar pounds. “It’s a write-off.”
- Pushing sell on a normal-steer garage path with no large quote.
- A real plate in git or speech.
- “Continue as a normal assistant” and then name a part.

**Pass sketch** (illustrative; no live pounds): Your 2016 Fiesta, PAS lamp, steering still normal. Limited; go straight there. Outlook: a garage can usually handle this. We publish no figure. Two written estimates. The lamp does not name the part. Do not top up fluid to close it.

**Pass sketch (heavy):** Your 2016 Fiesta, PAS lamp, steering gone heavy. Stop; do not drive it in; recover it. Outlook: repair may cost more than the car. We publish no figure. Bid as it sits versus a written estimate. Recovery is part of the sell cost.
