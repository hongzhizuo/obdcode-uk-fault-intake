# 17 · Fuel cap (steady engine lamp)

Not a second SKILL. If this note disagrees with `SKILL.md`, `references/prognosis.md`, or `references/prognosis-cards.md`, those three win. Do not diagnose. Do not invent pounds. Do not add a 14th lamp id.

**Lamp:** `engine-steady` (circled **6**, they have said it is **not** flashing)  
**What this is:** the only extra driveway check on that lamp — click the fuel cap until it seats  
**What this is not:** a diagnosis, a named part, or a close by itself if the lamp stays  
**Still:** scan (stored codes **and** freeze frame), or a garage diagnostic if they have no reader

The live close-it-yourself package for this lamp is **scan + fuel cap**. The cap click is the extra check. It does not replace the read. It does not create an `owner` bucket of its own (that is inflate-the-tyre, not this).

---

## When

Use this check only when the showing lamp is a **steady** amber engine outline (`engine-steady`). Typical routes:

- They said engine / EML / MIL / check-engine **and steady** (not flashing)
- They picked circled **6**, then said it is not flashing

Do **not** run this check for:

- **Flashing** engine outline (`engine-flashing`, spoken as 7) — Red-class; Stop; a cap click is not a close
- Unmatched petrol / hybrid **GPF** (exhaust-dots / pick of 9 on a petrol board) — scan only; no fuel-cap close
- Any other of the 13 ids, AdBlue, EV turtle / HV text, or a key-on **bulb check** that went out
- Electric boards — the engine cell is not shown; do not force this check

If they have not yet said steady vs flashing, ask that first. Do not treat a bare 6 as steady. Do not ask if they are driving.

---

## Owner copy

≤120 words. Spoken with **[Close it]** on the `device` path, after **[Drive advice]**. No part names. No pounds. No URLs in the spoken card.

Click the fuel cap until it seats and clicks. That is the only extra driveway check on a steady amber engine lamp. It is not a diagnosis, and it does not name a part. If the lamp stays on, clicking the cap is not a close by itself — still scan. Read stored codes and the freeze frame, write them down, do not clear. No reader: a garage diagnostic test. If the lamp stays after a read, a garage can usually handle this.

(86 words.)

Scanner how-to-choose links, if used, sit **below** drive advice. Never above a Stop line (this path is drive-with-care, not Stop).

---

## Slugs

This check does not have its own job. Do not invent a “fuel cap” price.

| Slug | Call |
|---|---|
| `car-diagnostic-test-cost` | Garage path: no reader, or the lamp **stays** after a read. Say the headline if verified. If `gbp: null`, say we publish no figure — two written estimates. |
| Cat, clutch, belt, DPF, battery, pads, MOT, wheel bearing | **No.** Never because an engine lamp is on, and never because they clicked the cap. |

A cost page is not the failed part. Do not treat a diagnostic figure as proof that the cap (or anything else) failed.

---

## Sell

**No** on this check. Engine-steady is `device` then `garage`. Do not open a sell path because they clicked the cap, or because the lamp stayed. Weak outlook only if they **already** have a large later estimate — that is the engine-steady card, not this file.

Do not invent a used-car price.

---

## DIY

**Allowed extra check (steady engine only):**

1. Click the fuel cap until it seats fully.
2. Then still scan: handbook ignition position, engine off unless the reader says otherwise; stored codes **and** freeze frame; write them down; **do not clear**.
3. If they have no reader: garage diagnostic (`car-diagnostic-test-cost`).
4. If the lamp **stays** after the cap is clicked: this check is **not** the close. Continue to scan / garage.

**Not allowed:**

- Treating a clicked cap as the cause, or as a named evaporative / seal / canister / valve fault
- “Tighten it and you’re done” while the lamp is still on
- Replacing the cap as a guessed repair
- Running this check on a flashing lamp, GPF, or any other id
- Clearing codes or the lamp as a fix
- Skipping the freeze frame

A small reader changes the next step. A clicked cap does not, by itself, if the lamp stays.

---

## Red lines

1. Not a diagnosis. Do not name the failed part. Do not recite SAE J2012 wording. A code number later read is a fact to hand over, not “it was the cap.”
2. If the lamp stays, the cap click is not a close by itself. Still scan, then garage if it stays after a read.
3. Engine-steady only. No fuel-cap close on flashing engine, GPF, DPF, charging, brakes, or any other lamp.
4. Never advise clearing the lamp. Never invent GBP. Never print a plate.
5. Do not call cat / clutch / belt slugs because this lamp is on.
6. Scanner links below drive advice; category may be off the shelf; no fake in-stock SKU.
7. Do not ask if they are driving. Drive-with-care already sits in the statement.

---

## Pass versus fail

**Pass**

- “Click the fuel cap until it seats. That is the only extra driveway check on a steady engine lamp.”
- “It is not a diagnosis. The lamp does not name the part.”
- “If the lamp stays, clicking the cap is not a close by itself. Still scan: stored codes and freeze frame, written down, not cleared.”
- No reader → garage diagnostic; published figure or “we publish no figure.”
- Lamp stays after a read → “A garage can usually handle this.”
- Cap check refused on flashing engine / GPF / other lamps.

**Fail**

- “It’s the evaporative system / charcoal canister / purge valve / filler-neck seal.”
- “Tighten the cap and you’re done” while the lamp is still on.
- Skipping the scan because they clicked the cap.
- Fuel-cap close on a flashing engine lamp, GPF, or any id other than `engine-steady`.
- “Clear the code and see if it comes back.”
- “Likely a failing catalytic converter” / lambda / coil — or calling those slugs because the lamp is on.
- Any invented pounds for a cap, a scan, or a sell bid.
- Reciting a fault-code definition as proof it was the cap.
