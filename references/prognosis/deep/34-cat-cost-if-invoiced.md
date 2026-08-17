# 34 · `catalytic-converter-replacement-cost` only if later invoiced

Not a second SKILL. If this note disagrees with `SKILL.md`, `references/prognosis.md`, or `references/prognosis-cards.md`, those three win. Do not diagnose. Do not invent pounds. Do not add a 14th lamp id.

This slug is a **weak-outlook upper bound**: what published UK figures look like **if the garage later invoices a converter**. It is **not** today’s failed part. Never say “you have a failed cat.” Never call it because a **steady** engine lamp is on.

Live chats **must** call `repair_cost` and speak that turn’s result. **This file must not freeze a pound figure as always-true.** Do not copy a remembered £ amount into speech or into this note.

---

## When

Call `repair_cost` with `job` = `catalytic-converter-replacement-cost` only when **this lamp’s allowlist says so**.

That is **one** path:

| Path | Bucket | How this slug is used |
|---|---|---|
| **`engine-flashing` (7)** | `poor` | **Optional add** after `car-diagnostic-test-cost`. Speak it only as “if the garage later invoices a converter.” Planning **upper bound** for the weak-outlook decision — not a diagnosis that the converter has failed. |

The spoken picture is the same engine-outline cell as 6. Flashing is spoken as 7. **[Drive advice]** is already Stop. A reader does not close this. Close-it-yourself is **no**.

Always call the diagnostic slug first on this card. The converter slug is extra, not a substitute for a scan, and not the reason the lamp is on.

Aftertreatment damage is why outlook is **weak**. That sentence is not a named part.

Do **not** upgrade `engine-steady` to this call because they asked “is it the cat?” That question is a diagnosis refusal (example E), not an allowlist change.

---

## When not

**Never because a steady engine lamp is on.** Card 6 `engine-steady` allowlist is `car-diagnostic-test-cost` only. Fuel cap + scan. Not parts. Not this slug — even as “if later invoiced.” That wording is for **flashing**, not here.

Do **not** call this slug on:

- `engine-steady` (6) — including “so is it the cat?” / a guessed misfire / a code they read
- Unmatched petrol / hybrid GPF — diagnostic only; not a converter page
- Diesel `dpf` — `dpf-cleaning-cost` (often null). There is no published DPF-replace slug; do not use this cat job as a nearby substitute
- `glow-plug` (13), `oil-pressure`, red `coolant-temp`, hydraulic brakes, charging, ABS, TPMS, airbag, PAS
- AdBlue / EV unmatched / EV 12V rectangle
- Value-gain / cat **delete** — that work is **Negative**; this slug is a **replacement invoice class**, not a delete price, and not how-to
- Clutch, cambelt, chain, wet-belt, battery, pads — different jobs

Never call this job because it is the only published slug with a number. Never hunt it when the allowlist is empty. A cost page is not the failed part.

Skip Step 6 (and this slug) when the flash was only a **key-on bulb check** that went out — not a fault. A flashing **coil** on diesel is `glow-plug` (13), not 7.

---

## How to call (live)

Prefer the tool. Same turn as **[Outlook]** / **[Repair]**, **after** **[Drive advice]** (Stop / recovery). Never above a Stop line. Never instead of `car-diagnostic-test-cost`.

```
POST https://obdcode.co.uk/mcp
{"jsonrpc":"2.0","id":1,"method":"tools/call",
 "params":{"name":"repair_cost","arguments":{"job":"catalytic-converter-replacement-cost"}}}
```

Plain HTTP if you do not speak MCP: the same job name is the slug on `https://obdcode.co.uk/guides/catalytic-converter-replacement-cost/`. Prefer the tool.

Speak the **live** result only, and only in the **if-invoiced** frame:

- `status: ok` and a headline → “If the garage later invoices a converter, published UK figures are …” then that headline. Planning range, **not** a quote for this car, **not** “you need this job.”
- `gbp: null` / `no_verified_price` / `no_published_job` → **that is the answer.** We publish no figure. Two written estimates. Do not fill the gap with a remembered cat price.

Do not cache yesterday’s pounds in this file or in the next chat.

---

## Owner copy

≤120 words. Spoken **[Repair]** add-on on the flashing-engine **poor** path only. Stop / recovery already sits in **[Drive advice]**. No ids, no fusion slugs, no URLs, no pounds unless this turn’s `repair_cost` returned a verified headline.

Repair may cost more than the car. A scan is the first invoice; the lamp does not name the part. If a garage later invoices a converter, that job’s published UK figures are an upper bound for planning — not a diagnosis that the converter has failed. We publish no used-car price. Get one bid as the car sits and one written estimate. Recovery is part of the sell cost. Compare them before you authorise work.

(94 words. Insert the live converter headline only inside the “if later invoices” sentence. If the tool returned no figure, say we publish no figure.)

---

## Slugs on the flashing card

| Slug | Call | How to speak it |
|---|---|---|
| `car-diagnostic-test-cost` | Always | First garage invoice: a scan. Quote the live headline, or “we publish no figure.” |
| `catalytic-converter-replacement-cost` | Optional add | **Only** “if the garage later invoices a converter.” Weak-outlook **upper bound**. Never “you have a failed cat.” |

Do **not** call clutch, belt, chain, DPF, battery, or pads because this lamp is flashing.

Sell talk stays on this card (weak outlook): bid **as it sits** (usually not a runner) versus the written estimate. Recovery / collection is part of the sell cost because drive advice is Stop. Do not invent that fee. Do not say write-off.

---

## Red lines

1. Never “you have a failed cat.” Never “likely a failing catalytic converter.” Never “it’s the cat, about £500.”
2. Never call this slug because a **steady** engine lamp is on.
3. Never treat the converter cost page as today’s diagnosis, or as a reason to skip the diagnostic slug.
4. No invented GBP. No figure frozen in this note. `gbp: null` is the answer when the tool says so.
5. No SAE J2012 wording. A code the garage later reads is a fact; it does not authorise this slug on a steady lamp.
6. No DIY coils, plugs, converters, or “keep driving to see.” Flashing engine is Red-class. A reader does not close it.
7. No cat / GPF / DPF **delete** how-to. Delete is Negative on sale; this file is not that step.
8. Safety before commercial: Stop / recovery above any cost line.
9. Never print a real registration. Illustrative plate elsewhere is `AB12CDE` only; then “your 2016 Fiesta.”
10. If they ask what is wrong: this skill does not diagnose. Restate **[Drive advice]** and **[Outlook]** for recovery / keep-driving / repair-vs-sell.

---

## Pass versus fail

**Pass**

- Flashing engine: Stop; do not drive it in; recovery or collection.
- Call `car-diagnostic-test-cost` as the first invoice.
- Add `catalytic-converter-replacement-cost` **only** as “if the garage later invoices a converter, published UK figures are …”
- “A scan is the next step; the lamp does not name the part.”
- Aftertreatment damage is why outlook is weak — without naming the converter as the failed part.
- Quote this turn’s headline, including “we publish no figure.”
- Bid as it sits versus a written estimate. Recovery is part of the sell cost.
- Steady engine lamp: diagnostic slug only; refuse the cat job even if they ask “is it the cat?”
- GPF / DPF / glow: do not borrow this slug.

**Fail**

- “You have a failed cat.” / “Likely a failing catalytic converter.”
- “It’s the cat, about £500.” / any pounds with no live `repair_cost` result.
- Calling this slug because a **steady** engine lamp (or GPF) is on.
- Calling it because it is the only slug with a number, or instead of the diagnostic test.
- Treating the converter cost page as the diagnosis.
- Freezing a converter price in this note as always-true.
- Keep driving / “pop to the garage” / DIY cat or coil steps.
- Cat delete as a cheaper fix, or any delete how-to.
- Shop or scanner links above the Stop line.
- “Clear the codes” so they can skip a scan or a later converter invoice.
