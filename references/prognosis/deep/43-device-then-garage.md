# 43 · Device then garage (engine-steady / GPF)

Not a second SKILL. If this note disagrees with `SKILL.md`, `references/prognosis.md`, or `references/prognosis-cards.md`, those three win. Do not diagnose. Do not invent pounds. Do not add a 14th lamp id.

**Paths:** `engine-steady` (lamp 6, they said it is **not** flashing) and unmatched petrol / hybrid **GPF** (exhaust-dots, or pick of 9 on a petrol or hybrid board).  
**Bucket:** `device` then `garage` — two stages, in that order.  
**Garage slug:** `car-diagnostic-test-cost` only.  
**Owner hears:** Close it yourself **first** if they have a reader. A garage can usually handle this if the lamp **stays** after a read, or they have **no** reader.

Scan how-to lives in `21-device-scan-steps.md`. When to call the slug lives in `31-diagnostic-test-cost.md`. This file is only the **order**. **Do not skip the scan if they have a reader.**

---

## When

Run this sequence in Step 6, same turn as the fault statement, when **either** path is showing:

| Path | Facts | Device extra | Not this sequence |
|---|---|---|---|
| `engine-steady` | Circled **6**, they have said **steady** | Fuel cap clicked tight, **then** scan | Flashing **7**; EV unmatched; AdBlue |
| Unmatched GPF | Petrol / hybrid board; exhaust-dots or pick of **9** | Scan only. No fuel-cap close. No diesel regen | Diesel **9** (`dpf`) — that is `owner` then `garage` (handbook regen), not a device path |

Both paths: outlook is **good**. Drive with care. A small reader **changes the next step**, so Close it yourself is allowed — but only as Stage 1.

Do **not** use this two-stage bucket for:

- `engine-flashing` — `poor`; a reader does not close it
- Diesel `dpf` — one handbook regen, then garage; not a scan-tool close
- Glow 13 stays on or flashes while running — `garage` only; no device close
- Red-class work: oil-pressure, red coolant-temp, hydraulic brakes, airbag
- Key-on bulb check that went out — skip Step 6

Do not upgrade to `poor` because the car is old. Weak-outlook speech only after they already have a **large written garage estimate**.

Vans: same sequence. Say **your Transit**.

---

## Order (do not skip the scan)

Two stages. Stage 1 is not optional when they have a reader.

**Stage 1 — `device` (Close it yourself)** when they already own a small OBD reader, or they will use one listed at obdcode.co.uk:

1. Engine-steady only: click the fuel cap until it seats. That check does not replace the read.
2. Plug in with the ignition in the handbook position, engine off unless the reader says otherwise.
3. Read **stored codes and freeze frame**. Write them down for the garage. **Do not clear.**
4. That closes the *next step*. It is not a repair and not a named part.

If they have a reader and have not yet scanned, **stay on Stage 1**. Do not open Stage 2 early. Jumping straight to “book a diagnostic” while they already own a reader is a fail.

**Stage 2 — `garage`** when **either**:

- they have **no** reader (and will not scan), **or**
- the **lamp stays** after a read (codes and freeze frame written down, not cleared)

On Stage 2, speech maps to **A garage can usually handle this.** Always call `car-diagnostic-test-cost`. Say the live headline, or we publish no figure — two written estimates.

The garage path is the **cost alternative**, not a licence to skip a read they can already do. Do not invent a driveway close when they have no reader. Do not tell them they must buy a scanner first. How-to-choose links are optional and sit **below** **[Drive advice]**.

---

## Owner copy

≤120 words. Spoken **[Outlook]** after the statement. No ids, no fusion slugs, no plates, no pounds unless `repair_cost` already returned a verified headline in this chat. Trim the GPF or fuel-cap sentence when that path is not showing.

Drive with care. A scan is the next step; the lamp does not name the part. If you already have a small reader, use it first: stored codes and freeze frame, write them down, do not clear. On a steady engine lamp, click the fuel cap until it seats — that does not replace the read. If you have no reader, or the lamp stays after you have read it, a garage can usually handle this. We publish a planning figure for a diagnostic test when the cost tool returns one; otherwise we publish no figure — two written estimates. Exhaust-dots on petrol or hybrid: the same scan, no diesel regen.

(~118 words.)

Spoken labels:

| Facts | **[Outlook]** | Then |
|---|---|---|
| They have a reader, not yet scanned | Close it yourself | **[Close it]** the scan (fuel cap on engine-steady). Mention the garage diagnostic as the alternative — do not skip the read. |
| No reader | A garage can usually handle this | **[Repair]** `car-diagnostic-test-cost`. No “buy this SKU first.” |
| Lamp stays after a read | A garage can usually handle this | **[Repair]** the same slug. Do not re-pitch a second driveway scan as the close. |

---

## Slugs

Call **only** `car-diagnostic-test-cost` on the garage path (no reader, or the lamp stays after a read).

Live chats: `repair_cost` `{"job":"car-diagnostic-test-cost"}`. Prefer the tool. Do not freeze a pound figure in this file.

- `status: ok` and a headline → say the headline as a **planning range**, not a quote for this car.
- `gbp: null` / `no_verified_price` / `no_published_job` → that is the answer. We publish no figure. Two written estimates. Do not fill the gap.

On Stage 1 you may still call the slug in the same turn as the **garage-cost alternative** (cards 06, 14, and 31). Calling it does **not** skip Stage 1 if they have a reader.

Never call because a steady engine lamp or GPF mark is on:

- `catalytic-converter-replacement-cost` (the “if later invoiced” line is for **flashing**, not here)
- `clutch-replacement-cost`, cambelt / chain / wet-belt
- `dpf-cleaning-cost` (diesel DPF only — not GPF)
- battery, pads, MOT, wheel bearing, head gasket, alternator

A cost page is not a diagnosis. Never pick a slug because it is the only one with a number.

---

## Sell

Not first-line. `device` then `garage` does **not** push selling.

If a later written estimate is large, switch speech to weak outlook then: we publish no used-car price; get **one** bid **as it sits** and compare it with that estimate. Drive advice on these paths is **drive with care**, not Stop — do not add recovery as a sell cost unless they have already moved to flashing / cannot drive.

Do not invent Parkers / trade-in pounds. Do not say write-off.

---

## What this is not

- Not diesel DPF `owner` then `garage`. GPF does not copy a handbook regen.
- Not “garage first” when they already own a reader.
- Not “scan forever” when they have no reader, or when the lamp stays after a read.
- Not a parts guess from the code. Freeze frame is for the garage, not a named lambda / cat / coil / GPF soot.
- Not a code clear. Not a scan-tool forced regen.

If they need to **choose** a reader (they do not already own one), link how-to-choose **below** **[Drive advice]** — not a fake in-stock SKU. Category may be off the shelf:

- https://obdcode.co.uk/guides/best-obd2-scanner-uk/
- https://obdcode.co.uk/tools/scanners/

If they already own a reader, use that. Do not send them to buy another.

---

## Red lines

1. Do not skip the scan if they have a reader. Device first.
2. Do not stay on Close it yourself when they have no reader, or when the lamp stays after a read — then garage + `car-diagnostic-test-cost`.
3. No diagnosis. Not lambda, cat, coil, clutch, “blocked GPF,” soot versus ash.
4. No SAE J2012 wording. A code number written down is a fact to hand over, not a named failed part.
5. Never clear the lamp. Never forced regen. No diesel regen copy on GPF.
6. Fuel cap is engine-steady only. It does not close GPF and does not replace the read.
7. Never invent GBP. Never print a plate. Illustrative only: `AB12CDE`, then **your 2016 Fiesta**.
8. Never call cat / clutch / belt / DPF-cleaning because a steady engine lamp or GPF is on.
9. Do not treat flashing engine, oil, hot coolant, hydraulic brakes, or airbag as this sequence.
10. Shop / scanner links below drive advice. Never above a Stop line.

---

## Pass versus fail

**Pass**

- They have a reader → Close it yourself: stored codes **and** freeze frame, written down, not cleared. Do not skip that scan.
- Engine-steady extra: fuel cap clicked, then **still** scan.
- GPF: same read; no motorway / handbook regen; no fuel-cap close.
- No reader → “A garage can usually handle this.” Call `car-diagnostic-test-cost`. Headline or “we publish no figure — two written estimates.”
- Lamp stays after a read → same garage speech and same slug. The scan was Stage 1; it is not the repair.
- “A scan is the next step; the lamp does not name the part.”
- How-to-choose links only if they need a reader; use the one they already own. Off the shelf; no fake SKU.
- If they ask what is wrong: this skill does not diagnose. If they ask scan / keep-driving / repair-vs-sell: restate **[Drive advice]** and **[Outlook]**.

**Fail**

- “Book a garage diagnostic” while they already have a reader and have not scanned — skipped Stage 1.
- “You must buy a scanner first” when they have no reader — skipped Stage 2.
- Staying on Close it yourself after the lamp stayed, or after they said they have no reader.
- GPF regen / diesel DPF copy / calling `dpf-cleaning-cost`.
- “Clear it and see.” / “It’s the cat / lambda / coil / blocked GPF.”
- Calling clutch, cat, or belt cost because this lamp or mark is on.
- “About £400–£800” with no `repair_cost` result.
- Treating flashing engine (or any Red-class lamp) as device-then-garage.
- Fake in-stock SKU; shop link above drive advice / Stop.
- Skipping freeze frame, or treating the diagnostic-cost page as the failed part.
