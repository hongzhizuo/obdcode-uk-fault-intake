# 49 High MOT miles — diesel DPF / engine lamps

Deep outlook note for SKILL Step 6. Not a second skill. If this file disagrees, `SKILL.md`, `references/prognosis.md`, and `references/prognosis-cards.md` win. Do not diagnose. Do not invent pounds. Do not add a 14th lamp id.

High recorded mileage is **[Vehicle]** context. It is not a bucket. **Follow the card.**

---

## When

Use this note when the car is **diesel** (including diesel hybrid on the diesel board) and MOT tests, or the owner, show **high miles**, and the live lamp is:

- `engine-steady` (6)
- `engine-flashing` (7)
- `dpf` (9) — diesel board only

The same **do not auto-upgrade** rule applies to other `garage` lamps (glow 13 that stays on, ABS, airbag). This file is the diesel DPF / engine case.

Do **not** run this as diesel DPF copy on petrol / hybrid GPF (unmatched exhaust-dots / pick of 9 on a petrol board). High miles do not turn GPF into DPF.

Skip Step 6 when the showing was not a fault (glow 13 came on with ignition and went out; key-on bulb check). High miles do not create an outlook for a lamp that went out.

Do not ask if they are driving. Do not invent a mile cut-off.

---

## Rule

From `prognosis.md`: do not upgrade `garage` to `poor` because the car is **old** unless they already have a **large estimate**, or the lamp is already in the weak-outlook column.

High MOT mileage is the same kind of fact as age. **It does not move the bucket.**

| Showing | Card default | High MOT miles |
|---|---|---|
| Engine outline **steady**, driving normally | `device` then `garage` | Stay here |
| Engine outline **flashing** | `poor` | Already `poor` from the flash, not from miles |
| DPF **steady**, driving normally | `owner` then `garage` | Stay here. One handbook regen still first |
| DPF **flash / limp / oil over max** | `poor` | Already `poor` from behaviour, not from miles |
| Glow stays on / flashes while running | `garage` | Stay here |
| Glow on with ignition then out | skip | Still skip |

Upgrade `garage` → `poor` **only** when they already have a large written estimate (or the card already says `poor`). An odometer on a certificate is not that estimate. Do not invent a threshold such as “over 150,000 = sell it.”

Vans: same buckets. Say **your Transit**. Downtime is “a day off the road,” not a made-up day-rate.

---

## Owner copy

Spoken **[Outlook]** after the statement. ≤120 words. No plates, no fusion slugs, no invented GBP. Restate Stop above any shop link when drive advice is Stop.

### Engine-steady, high miles (card stays `device` then `garage`)

High recorded miles do not change this. Close it yourself if you have a reader: stored codes and freeze frame, write them down, do not clear. Click the fuel cap fully. If the lamp stays, a garage can usually handle a diagnostic. We publish that test figure when the tool returns one — or we publish no figure. Do not sell the car on mileage alone. The lamp does not name the part.

### DPF steady, driving normally, high miles (card stays `owner` then `garage`)

High recorded miles do not skip the handbook drive. If the DPF lamp is steady and the car is driving normally, do one regeneration at the speed and duration in the handbook. Check the oil. Never regen in an enclosed space. If the lamp stays, a garage can usually handle it. We publish a DPF-cleaning figure when the tool returns one — often we publish no figure; then two written estimates. Do not cut the filter out. The lamp does not name the part.

### Already weak outlook, or they have a large estimate

Repair may cost more than the car. High recorded miles can make a large job harder to recover from a buyer, but we publish no used-car price. Get one bid as it sits and one written estimate. Compare them before you authorise work. Recovery is part of the sell cost when drive advice is Stop. The lamp does not name the part.

---

## Slugs

Follow the **card** allowlist for **this lamp**. High miles do not add a job.

| Lamp | Call |
|---|---|
| `engine-steady` | `car-diagnostic-test-cost` |
| `engine-flashing` | `car-diagnostic-test-cost`; `catalytic-converter-replacement-cost` only as “if the garage later invoices a converter” |
| `dpf` | `dpf-cleaning-cost` (often `gbp: null` — still call it, still say no figure) |
| `glow-plug` stays on | `car-diagnostic-test-cost` |

Do **not** call clutch, cambelt, chain, wet-belt, pads, or battery because the odometer is high. There is **no** published DPF-replace slug — do not invent a filter price. Do not call cat or clutch because an engine lamp is on.

`gbp: null` / `no_verified_price` / `no_published_job` is the answer. Do not fill it with a high-miles surcharge.

---

## Sell

There is **no** sell-price tool. Do not invent Parkers, WeBuyAnyCar, or “typical trade-in” pounds.

**On garage / close-it-yourself:** do not push selling because MOT miles are high.

**On weak outlook only:** high miles may colour the speech **qualitatively**, with no invented GBP:

- A high-mileage diesel with a large outstanding job is often worth less **as it sits**
- That is why they should put **one** instant-sale or dealer bid next to **one** written garage estimate
- If the estimate is larger than the bid, selling is often the better outlook
- Still no invented bid, and do not call the car a write-off

If they later bring a **large estimate**, you may switch a previous garage path to weak outlook. The estimate is the trigger. The odometer was only context.

Stop paths (flashing engine; DPF limp / oil over max when they must not keep driving): bid as it sits — usually not a runner; recovery / collection is part of the sell cost. Do not invent that fee. Do not tell them to drive a Stop car to a buyer.

Do not suggest DPF deletion as a cheap high-miles fix. If they ask about delete as a mod, finish this outlook first; value-gain may then say **Negative** and refuse the how-to.

---

## MOT miles as context, not cause

Quote this car’s odometer on the **[Vehicle]** line when lookup returned it. Readings across tests may imply annual miles — worth a mention when a fault is mileage-related, not as today’s diagnosis.

Same-system fusion (DPF slug; engine-family emissions / exhaust / catalyst / lambda) is History. End every named prior note: **this does not show the cause of today’s lamp.** `count` above 1 is not “never fixed” and is not a bucket upgrade.

Do not say “Expect a fail.” MIL / DPF MOT talk stays gated on `first_used` + fuel. High miles do not skip that gate. Link the [DVSA inspection manual](https://www.gov.uk/guidance/mot-inspection-manual-for-private-passenger-and-light-commercial-vehicles) when in scope.

---

## Close-it-yourself

Unchanged by miles. Allowed only when outlook is **not** `poor` and the card is `owner` or `device`.

- **Engine-steady:** fuel cap clicked; stored codes and freeze frame; do not clear. Not parts.
- **DPF steady, driving normally:** one handbook regen. Oil level check. Never enclosed-space regen. Never scan-tool forced regen.
- **DPF flash / limp / oil over max:** no more motorway loops. Not a close.
- **Engine-flashing:** no. A reader does not fix it.
- **Glow stays on:** no DIY glow-plug set.

Do not skip the regen or the scan because “it’s high miles so it must be ash / a worn engine.” That is a diagnosis.

---

## Red lines

1. Do not auto-upgrade `owner` / `device` / `garage` to `poor` from MOT mileage, age, or “old diesel.”
2. Do not invent a mile threshold or a used-car price.
3. Do not diagnose (not ash-loaded, not worn engine, not failed DPF, not cat, not clutch).
4. Follow the card slugs only. No nearby-slug hunt because miles are high.
5. No DPF delete / remap how-to.
6. Petrol GPF is not this file. Keep the petrol board; no diesel regen copy.
7. Never print, file, or speak a real plate. “Your 2016 Fiesta” / “your Transit.”
8. Never advise clearing the lamp. No forced regen.
9. Safety before commerce. No shop links above Stop / recovery.
10. No SAE J2012 wording.

---

## Pass / fail

**Pass**

- High MOT odometer, steady DPF, driving normally → `owner` then `garage`. One handbook regen. Call `dpf-cleaning-cost`.
- High miles, steady engine outline → `device` then `garage`. Scan + fuel cap. Call `car-diagnostic-test-cost`.
- “High recorded miles can make a large job harder to recover; we publish no used-car price. Get one bid as it sits and one estimate.”
- Flashing engine or DPF limp / oil over max → `poor` **because of the card**, then qualitative high-miles sell speech, still no invented GBP.
- Garage stays garage until they have a large estimate.
- Quote `gbp: null` as no published figure.
- Petrol exhaust-dots: unmatched GPF, scan, no regen copy — miles still do not make it `poor`.

**Fail**

- “It’s done 200,000 miles, repair may cost more than the car” on a steady DPF or steady engine lamp with no large estimate.
- “Typical trade-in is £800.” / Parkers / WeBuyAnyCar pounds.
- “It’s a write-off.” / “DPFs fail after 150k, sell it.”
- Naming ash vs soot, a worn engine, a failed filter, or a clutch because miles are high.
- Calling `clutch-replacement-cost` or inventing a DPF-replace price because the odometer is high.
- Skipping regen or scan “because high miles.”
- “Just cut the DPF out; it’s high miles anyway.”
- Treating petrol exhaust-dots as this diesel path.
- Shop or scanner links above a Stop line.
