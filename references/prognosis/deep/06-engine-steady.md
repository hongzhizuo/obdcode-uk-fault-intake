# 6 `engine-steady`

Deep note only. Not a second SKILL. If this file disagrees with `SKILL.md`, `references/prognosis.md`, or `references/prognosis-cards.md`, those three win.

Steady amber engine-block outline. Bucket: **`device` then `garage`**. Speech maps `device` to **Close it yourself**.

---

## When

Run Step 6 on this card after the Step 5 statement when:

- the pick is lamp **6** `engine-steady`, and
- they have said it is **steady**, not flashing.

Do not treat a bare 6 as this card until they have said it is not flashing. Flashing is **7** `engine-flashing` (Stop; not this file).

This lamp is ghosted on the electric board. Do not run this card for an EV turtle, a car-with-! with no skid lines, or HV / charge-plug text (unmatched EV). Do not run diesel DPF copy, petrol/hybrid GPF copy, or AdBlue copy.

Drive advice stays **drive with care**. Escalation: if it starts flashing, do not drive it in; arrange recovery.

Do not skip Step 6. Do not upgrade to `poor` only because the car is old. Switch to weak-outlook **speech** only after they already have a **large written garage estimate**.

Vans use the same buckets. Say “your Transit”.

---

## Owner copy

Spoken outlook after the statement. No ids, no fusion slugs, no URLs, no pounds unless `repair_cost` already returned a verified headline in this chat. Keep this block **≤120 words**.

> Drive with care. If the engine outline starts flashing, do not drive it in; arrange recovery. Close the next step yourself if you have a reader: click the fuel cap until it seats, then read the stored codes and the freeze frame. Write them down. Do not clear the lamp. If you have no reader, book a garage diagnostic test. We publish a planning figure for that test only when a verified UK source exists; otherwise we publish no figure — ask two garages for a written estimate. The lamp does not name the part.

(94 words.)

If they already own a reader, say to use that. If a later estimate is large, stop this close-it speech and use weak-outlook sell copy instead — still without naming a part.

---

## Slugs

Call **only** `car-diagnostic-test-cost` (`repair_cost` `{"job":"car-diagnostic-test-cost"}`).

- `status: ok` and a headline → say the headline as a **planning range**, not a quote for this car.
- `gbp: null` / `no_verified_price` / `no_published_job` → that is the answer. We publish no figure. Two written estimates. Do not fill the gap.

Never call these **because this lamp is on**:

- `catalytic-converter-replacement-cost`
- `clutch-replacement-cost`
- `cambelt-and-water-pump-cost`
- `timing-chain-replacement-cost`
- `wet-belt-replacement-cost`

A cost slug is not a diagnosis. Never pick a job because it is the only one with a number. Never treat a cost page as the failed part. This card does **not** allow cat as “if later invoiced” (that wording is for flashing, not here).

---

## Sell

Not first-line. Do not push selling on `device` or `garage`.

If they later show a **large** written estimate, switch speech to weak outlook:

1. Repair: the diagnostic-test headline if verified, or “we publish no figure.”
2. Sell: we publish no used-car price. Get **one** bid **as it sits**, and compare it with the estimate.
3. If the estimate is larger than the bid, selling is often the better outlook.

Do not invent Parkers / instant-sale pounds. Do not say the car is a write-off. Drive advice on this lamp is not Stop, so do not add recovery as a sell cost unless they have already moved to flashing / cannot drive.

---

## DIY

Allowed because outlook is good **and** a small reader changes the next step. Not parts. Not a repair.

1. Fuel cap clicked tight — the only extra driveway check on this lamp.
2. Plug in with the ignition in the handbook position, engine off unless the reader says otherwise.
3. Read **stored codes and freeze frame**.
4. Write them down for the garage.
5. Do **not** clear the lamp.

If they have no reader, the garage diagnostic test is the alternative — still call `car-diagnostic-test-cost`.

Scanner shops on the site may be **off the shelf**. After drive advice, link as how to choose, not as in-stock SKUs:

- https://obdcode.co.uk/guides/best-obd2-scanner-uk/
- https://obdcode.co.uk/tools/scanners/

Do not invent a product code, stock status, or price. If they already own a reader, use that.

---

## Red lines

- No diagnosis. Not “it’s the lambda / cat / coil / clutch / belt.”
- No SAE J2012 definition wording. A stored code number may be written down; the standard’s text may not.
- Never advise clearing the lamp as a fix.
- Never invent pounds. Never print a real plate.
- Never call cat, clutch, or belt slugs because this lamp is on.
- Never invent a scanner SKU or claim a reader is on the shelf.
- Device and shop links stay **below** drive advice (and never above a Stop line if they later escalate).
- A reader does not fix oil pressure, a hot engine, hydraulic brakes, an airbag, or a flashing engine lamp — those are other cards.

---

## Pass / fail

**Pass**

- Drive with care, plus flashing → recovery.
- “A scan is the next step; the lamp does not name the part.”
- “Read the freeze frame before replacing anything.”
- Fuel cap clicked; stored code **and** freeze frame; do not clear.
- Quote the `car-diagnostic-test-cost` headline, or “we publish no figure — two written estimates.”
- How-to-choose scanner links, no fake SKU.
- If they ask what is wrong: this skill does not diagnose. If they ask scan / keep-driving / repair-vs-sell: restate drive advice and outlook.

**Fail**

- “Likely a failing catalytic converter.” / “it’s the cat, about £500.”
- “It’s cylinder 3.” / “sensor, reluctor, or wiring.”
- Calling clutch, cat, or belt cost because the engine lamp is on.
- “About £400–£800” with no `repair_cost` result.
- “Clear it and see if it comes back.”
- “Buy scanner SKU X, in stock, £Y.”
- Treating pick 6 as steady before they said it is not flashing.
- Running this card on an EV unmatched path or as diesel regen / GPF copy.
