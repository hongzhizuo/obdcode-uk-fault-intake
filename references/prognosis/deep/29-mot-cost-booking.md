# 29 · `mot-cost` is a booking line, not a lamp repair

Not a second SKILL. If this note disagrees with `SKILL.md`, `references/prognosis.md`, `references/prognosis-cards.md`, or `references/value-gain.md`, those four win. Do not diagnose. Do not invent pounds. Do not add a 14th lamp id.

**Slug:** `mot-cost`  
**Use:** statement **[Book]** line, or a named MOT **job** (Step 7)  
**Never:** as the repair for a lamp  
**Often:** `gbp: null` — still call when allowed; that is the answer  
**Fresh MOT:** **Modest** sale-price band — not a lamp outlook

Live chats must call `repair_cost`. **This file must not freeze a pound figure as always-true.**

---

## When

Call `repair_cost` with `job` = `mot-cost` only in these cases:

1. **MOT expired, or due within 30 days.** Add an owner **[Book]** line in the **statement**, not a verdict and not a bucket change. You may call this slug as a **booking** figure for the test — not as today’s lamp repair.
2. **In-scope Major lamp** (after the `first_used` + fuel gate). **[Book]** may remind them to book the test. Still not “Expect a fail.” Still not the lamp’s **[Repair]** slug.
3. **They named the MOT as a job** — “what does an MOT cost?”, they are booking one, or they already have a test invoice.
4. **Path B / value-gain.** No lamp (or the lamp outlook is already done). They ask whether a **fresh MOT adds value**. Call this slug for the **job’s** published range. Band is **Modest**. Still no invented **gain**.

Do **not** call this slug when:

- A lamp is on and you need a **repair** figure. Use that lamp’s allowlist (`prognosis.md`). `mot-cost` is on **no** lamp allowlist.
- The allowlist is empty and you want a number. Do not hunt this slug because it exists.
- Fusion listed a defect. History is not a booking fee and not today’s cause.
- They ask “so will it fail MOT?” That is not a cost call. Gate first-use + fuel, link the [DVSA inspection manual](https://www.gov.uk/guidance/mot-inspection-manual-for-private-passenger-and-light-commercial-vehicles), never recite a fail verdict.
- Key-on bulb check, glow 13 that went out, blue thermometer that went out, parking-brake brake lamp, ESC flashing while driving — not a fault; no outlook; no MOT-cost hunt.

Lamp **and** a due test: finish **[Drive advice]** and the lamp outlook **first**. **[Book]** sits in the statement. Lamp **[Repair]** stays on the lamp card. This slug, if called, is only the **test booking**, spoken after Stop / recovery.

Vans: same rule. Say **your Transit**. Do not invent a van MOT regime or a day-rate.

---

## Not a lamp repair

`mot-cost` never becomes the failed part, the outlook bucket, or a substitute for `car-diagnostic-test-cost`, pads, cat, clutch, DPF cleaning, or any other job.

| Line | What it is | What it is not |
|---|---|---|
| **[Book]** | Expired / due in 30 days / in-scope Major — book the test | A fail prediction; a sell trigger |
| **[Repair]** | The **lamp** allowlist (or “no figure for this class of job”) | This slug |
| **[Outlook]** | Close it yourself / garage / repair may cost more than the car | A fresh certificate |
| **[Value]** Modest | Fresh MOT with **no** dangerous / major carries — typical buyer reaction | A lamp close; extra profit |

Do not upgrade `garage` to `poor` because the MOT is due. Do not skip a Stop lamp because they need a certificate. Do not treat a new pass as proof the lamp is fixed.

---

## Often null

This slug is **often** `gbp: null` / `no_verified_price` / `no_published_job`. That is the answer.

Still **call** it when the cases above apply. Skipping the tool, or swapping to a different slug because it is the only one with a number, is a fail. A published slug can also return a headline today; read the live result.

- `status: ok` and a headline → say the headline. Planning range for the **test booking**, not a quote for this car, not a repair, not a gain.
- Null → **we publish no figure.** Ask two local testers or garages for a written booking quote. Do not fill the gap with a remembered fee, a legal maximum, or “about fifty pounds.”

Do not cache yesterday’s pounds in this file or in the next chat.

---

## Fresh MOT is Modest, not a lamp outlook

A **fresh MOT with no dangerous / major carries** is Step 7 **[Value] Modest**: it removes an immediate bill; it is not extra profit. It is not Close it yourself, not “a garage can usually handle this,” and not a weak-outlook sell speech.

A certificate that still carries **dangerous** or **major** defects is still a bill for the next buyer — not this Modest line.

There is **no** modification-gain API. The job headline (or null) is never an uplift in pounds. Their invoice is **spend**, not sale-price rise. Record date, mileage, and what they paid on a vehicle card at obdcode.co.uk. Do not print the plate.

Full Modest copy for tyres / pads / battery as well: `58-modest-value-tyres-mot.md`. Fusion / “Expect a fail”: `61-mot-not-outlook-cause.md`.

```
[Value]   Modest. Removes an immediate bill; it is not extra profit.
[Record]  Date, mileage, invoice they paid, on a vehicle card at obdcode.co.uk
```

No lamp, MOT-value question: lookup for year / make / model in the value line. **No** dashboard picker.

---

## How to call (live)

Prefer the tool. Never above a Stop line.

```
POST https://obdcode.co.uk/mcp
{"jsonrpc":"2.0","id":1,"method":"tools/call",
 "params":{"name":"repair_cost","arguments":{"job":"mot-cost"}}}
```

Plain HTTP if you do not speak MCP: the same job name is the slug on `https://obdcode.co.uk/guides/mot-cost/`. Prefer the tool.

---

## Owner copy

≤120 words. Booking or Modest value. No fail verdict. No part guess. No pounds unless the live tool returned a headline.

MOT expired or due within 30 days: book the test. That is a booking line, not a repair of today’s lamp, and not a prediction that the car will fail. We publish a test figure only when the tool returns one; it is often none — then we publish no figure. Ask two local testers for a written quote. If a lamp is also lit, the lamp outlook is separate: a scan or a workshop job is not this booking. A fresh pass with no dangerous or major carries is Modest on sale: it removes an immediate bill; it is not extra profit. Put the date, mileage, and what you paid on a vehicle card at obdcode.co.uk.

(117 words.)

**[Book]** (statement, when due / expired / in-scope Major): MOT is due — book the test. Not a repair-or-sell change.

**In scope (after the gate):** the tester may record a Major if the lamp still indicates a malfunction — check the DVSA inspection manual. Out of scope: this lamp is not an automatic fail item on this car.

---

## Red lines

1. Never call `mot-cost` as the **repair** for a lamp. Never hunt it for a number.
2. Never say “Expect a fail” or “will likely fail as it stands.”
3. `gbp: null` is the answer. Do not invent a test fee or a gain.
4. Fresh MOT is **Modest** value, not a lamp outlook and not Strong.
5. Job headline ≠ sale gain. Their invoice is spend.
6. No how-to for “passing” an MOT, deleting a filter, or clearing a lamp for the test.
7. No real plate in speech or in git. Illustrative only: `AB12CDE`, then **your 2016 Fiesta**.
8. No dashboard picker on a no-lamp MOT-value question.
9. Do not put this booking or value line above Stop / recovery.
10. Do not freeze a fee in this file.

---

## Pass versus fail

**Pass**

- MOT expired or due in 30 days → **[Book]** in the statement; bucket unchanged.
- Call `repair_cost` `mot-cost` as the **booking** / named-job range; quote this turn’s headline, or “we publish no figure.”
- Often null → still call when allowed; then two written booking quotes. Do not invent.
- Lamp on → lamp allowlist for **[Repair]**; this slug is not that repair. “A scan is the next step; the lamp does not name the part.”
- In-scope lamp: tester **may** record a Major if it still indicates a malfunction; link the DVSA manual.
- Out of scope: not an automatic fail item on this car.
- Fresh MOT, no dangerous / major carries → **[Value] Modest.** Removes an immediate bill; it is not extra profit. Record it on the vehicle card.
- Lamp plus MOT question → statement and outlook first, then **[Book]** / **[Value]**.
- No lamp, “does an MOT add value?” → no picker; Modest; job range is not gain.
- `gbp: null` spoken as no published figure.

**Fail**

- “It’s an MOT job” / treating `mot-cost` as why the lamp is on.
- Calling `mot-cost` because an engine, DPF, ABS, oil, or brake lamp is on, or because it is the only slug with a number.
- “Expect a fail.” / “it will fail as it stands.”
- “About £40–£60” (or any pounds) with no tool result, or a figure copied from this file.
- Skipping the call because it is often null, then guessing the legal maximum or a high-street fee.
- Due-soon MOT → “Repair may cost more than the car” with no lamp card that is already `poor`.
- “A fresh MOT adds £200” / treating the headline or their invoice as sale-price uplift.
- Calling a certificate that still carries dangerous / major Modest extra profit, or upgrading a clean fresh MOT to Strong.
- Opening the cluster picture for “does a fresh MOT add value?”
- “Clear the lamp before the test.” / filter-delete how-to so it will pass.
- Shop or booking link above Stop / recovery.
- Printing the registration.
