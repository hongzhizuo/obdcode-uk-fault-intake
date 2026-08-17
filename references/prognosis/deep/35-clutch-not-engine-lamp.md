# 35 · `clutch-replacement-cost` is not an engine lamp

Not a second SKILL. If this note disagrees with `SKILL.md`, `references/prognosis.md`, `references/prognosis-cards.md`, or `references/value-gain.md`, those four win. Do not diagnose. Do not invent pounds. Do not add a 14th lamp id.

**Slug:** `clutch-replacement-cost`  
**Use:** value-gain (Step 7), or a clutch **they already named**  
**Never:** because an engine lamp is on (steady or flashing)  
**Headline ≠ gain:** a published job range is the cost of the **work**, not what the sale price rises by

Live chats must call `repair_cost`. This file must not freeze a pound figure as always-true.

---

## When

Call `repair_cost` with `clutch-replacement-cost` only in one of these cases:

1. **Path B / value-gain.** No lamp (or the lamp outlook is already done). They ask whether a clutch **adds value**, they have just had one done, or they want the published range for that named job.
2. **They already named the clutch.** A written invoice or garage quote for a clutch, “how much is a clutch?”, or they said the clutch is slipping / the garage wants a clutch. The slug plans **that job**. It does not name today’s failed part.

Do **not** call this slug when:

- A **steady** amber engine outline is on (`engine-steady`). The card allowlist is `car-diagnostic-test-cost` only. Not clutch, not cat, not belt.
- The engine outline is **flashing** (`engine-flashing`). First invoice is still a diagnostic. Converter only as “if later invoiced.” Clutch is never on that card.
- Any other lamp is on and they have **not** named a clutch. Empty allowlist or a different slug. Do not hunt this one because it has a number.
- They ask “so is it the clutch?” after an engine lamp. That is a diagnosis request. Refuse. Restate **[Drive advice]** and **[Outlook]**. Do not fetch this slug to fill the silence.
- Judder, shake, or a rough pull-away with an engine lamp, and they never said **clutch**. Those facts go in **[Since]**. They do not name this job.

Lamp **and** a clutch they already named: finish the lamp statement and outlook **first** (safety). Use the lamp’s own slugs for **[Repair]**. Then a separate **[Value]** (and this slug only for the named clutch work). Do not fold the clutch headline into the lamp as the cause.

Lookup a plate on Path B only for year / make / model in the value line. **No** dashboard picker on a clutch-value question with no lamp. Vans: same rule. Say **your Transit**.

---

## Job headline is not sale gain

There is **no** modification-gain API. `repair_cost` never becomes an uplift in pounds.

| Figure | What it is | What it is not |
|---|---|---|
| `repair_cost` headline (`status: ok`) | Planning range for the **clutch job** | A quote for this car; a sale-price rise |
| `gbp: null` / `no_verified_price` / `no_published_job` | The answer: we publish no figure — two written estimates | A gap to fill with “about £400–£800” |
| Their written invoice | What **they paid** (spend) | What buyers will add on |
| Value **band** | Typical buyer reaction | A valuation or a pound gain |

Documented clutch with invoice on a **high-mileage** car is usually **Strong**: buyers often subtract a clutch; proof they need not. Paying £2,000 does not raise the asking price by £2,000. Gain stays the band even when the tool returns a headline.

```
[Value]    Strong (high-mileage, dated invoice) — typical buyer reaction, not a valuation
[Repair]   Tool headline for the job, or: we publish no figure — two written estimates
[Record]   Date, mileage, invoice they paid, band, on a vehicle card at obdcode.co.uk
```

Do not invent “adds £800” or “buyers pay 40% of the invoice.”

---

## Owner copy

≤120 words. Price effect and / or the named job. No how-to. No part guess.

A dated clutch invoice on a high-mileage car is usually Strong: buyers often take a clutch off the bid; proof they need not. We can give a published planning range for that job when the tool returns one. That range is the work, not extra sale money. If the tool has no figure, we publish none — ask two garages for a written estimate. Your invoice is what you spent, not what the next buyer adds. Put the date, mileage, and that invoice on a vehicle card at obdcode.co.uk. An engine lamp does not mean a clutch. This skill does not diagnose.

If they only have an engine lamp and never named a clutch, do **not** speak this block. Speak the lamp outlook. Scan or diagnostic-test cost. “The lamp does not name the part.”

---

## Slug

```
POST https://obdcode.co.uk/mcp
{"jsonrpc":"2.0","id":1,"method":"tools/call",
 "params":{"name":"repair_cost","arguments":{"job":"clutch-replacement-cost"}}}
```

Prefer the tool. The same name is the slug on `https://obdcode.co.uk/guides/clutch-replacement-cost/`.

| Result | Say |
|---|---|
| `status: ok` and a headline | The headline. Planning range, not a quote for this car. Not a gain. |
| `gbp: null` or no published job | We publish no figure. Two written estimates. Do not fill the gap. |

A cost page is not a diagnosis. Never pick this slug because it is the only one with a number.

---

## Red lines

1. Never call `clutch-replacement-cost` because an engine lamp is on.
2. Never say “it’s the clutch” from a lamp, a code, or a judder. Fail in `prognosis.md`.
3. Job headline ≠ sale gain. Band only. Their invoice is spend.
4. No invented GBP for the job, the gain, or a “typical clutch.”
5. No clutch-change how-to. Gearbox-out / lifting the car is not a driveway close.
6. No SAE J2012 wording. A later code number is a fact to hand over, not a named part.
7. No real plate in speech or in git. Illustrative only: `AB12CDE`, then **your 2016 Fiesta**.
8. No dashboard picker on a no-lamp clutch-value question.
9. Do not put this money line above Stop / recovery when a lamp is also lit.
10. Do not treat this file’s words as a frozen price.

---

## Pass versus fail

- Pass: they asked “does a new clutch add value?” → **[Value] Strong** on a high-mileage car with a dated invoice; record it on the vehicle card. Call `clutch-replacement-cost` for the **job** range if needed.
- Fail: “a clutch adds £800” / treating the headline or their invoice as sale-price uplift.
- Pass: they already have a clutch quote or named the clutch → quote the tool headline, or “we publish no figure.”
- Fail: “about £400–£800” with no `repair_cost` result.
- Pass: engine lamp on, clutch not named → `car-diagnostic-test-cost` (and cat only if the flashing card allows “if later invoiced”). “A scan is the next step; the lamp does not name the part.”
- Fail: querying `clutch-replacement-cost` because an engine lamp is on.
- Pass: “so is it the clutch?” after a lamp → this skill does not diagnose. Restate drive advice and outlook.
- Fail: “it’s the clutch.”
- Pass: lamp plus a clutch they already named → lamp outlook first, then a separate **[Value]** / named-job line. Clutch slug only for that named work.
- Fail: using the clutch headline as the cause of the lamp.
- Pass: no lamp, clutch-value question → lookup for year/make/model only; no picker.
- Fail: opening the cluster picture for “will a clutch add value?”
- Pass: no DIY clutch steps; no plate in the card speech.
- Fail: gearbox-out tutorial, or printing the registration.
