# 24 · `head-gasket-repair-cost` — often null, never “it is the gasket”

Not a second SKILL. If this note disagrees with `SKILL.md`, `references/prognosis.md`, or `references/prognosis-cards.md`, those three win. Do not diagnose. Do not invent pounds. Do not add a 14th lamp id. Lamp card: `02-coolant-temp.md`. Null speech: `41-null-gbp-speech.md`.

This slug is a **weak-outlook invoice class**: what published UK figures look like **if the garage later invoices a head-gasket job**. It is **not** today’s failed part. **Never say “it is the gasket.”** Never say the gasket has failed.

You **may** call it on the red coolant `poor` path. You often get `gbp: null`. **Null is the answer**, not a gap. Live chats **must** call `repair_cost` and speak that turn’s result. **This file must not freeze a pound figure as always-true.** Do not copy a remembered £ amount into speech or into this note.

---

## When

Call `repair_cost` with `job` = `head-gasket-repair-cost` **only** when this lamp’s allowlist says so.

That is **one** path:

| Path | Bucket | How this slug is used |
|---|---|---|
| **`coolant-temp` red (2)** | `poor` | **May** call. Coolant weak-outlook **if invoiced**. Speak it only as “if the garage later invoices this job, published UK figures are …” Often `gbp: null` / `no_verified_price` / `no_published_job` — then say we publish no figure. Two written estimates. Never “it is the gasket.” |

Ask **blue or red** before id 2. This slug exists only on the **red** thermometer. **[Drive advice]** is already Stop. Do not drive it in; ask the garage to collect, or call recovery. Close-it-yourself is **no**. A reader does not fix a hot engine.

“May” means allowed, not a hunt for a number. Still call it when you expect null. Skipping because it is often empty, or swapping to a neighbour slug that has a figure, is a fail.

A caught-early thermostat (or hose, pump, radiator) job has **no** published slug. Still no invented pounds. Two written estimates. Do not substitute `cambelt-and-water-pump-cost` as a lamp cause.

---

## When not

**Never because you want a number** on another card. Empty allowlist → we publish no figure **for this class of job**. Do not hunt this slug.

Do **not** call this slug on:

- **Blue** thermometer — engine-cold, not id 2. Skip Step 6. No gasket sell talk.
- Key-on **bulb check** that then went out — not a fault
- **`oil-pressure` (1)** — allowlist is empty. No engine-rebuild job. Do not borrow this slug so there is a figure
- `engine-steady` / `engine-flashing` / GPF / glow — diagnostic (and converter **if later invoiced** on flashing only), not a gasket page
- Hydraulic `brake-system`, `airbag-srs`, `power-steering`, charging, DPF, TPMS, ABS, ESC
- AdBlue / unmatched EV turtle / HV text / EV 12V rectangle
- Value-gain / due cambelt — that is `cambelt-and-water-pump-cost`, not this lamp and not a diagnosis
- They asked “so is it the gasket?” after a red lamp — that is a diagnosis refusal, not an allowlist change. You may still call this slug as **if invoiced**; you still must not say it is the gasket

On an electric board, slot 2 can still be a **red** thermometer. Same invoice-class rule. Do not invent a pack, pump, or heater-matrix price. Do not map turtle / HV text to this slug.

Never pick this job because it is the only published slug with a number. A cost page is not the failed part.

---

## How to call (live)

Prefer the tool. Same turn as **[Outlook]** / **[Repair]**, **after** **[Drive advice]** (Stop / recovery). Never above a Stop line.

```
POST https://obdcode.co.uk/mcp
{"jsonrpc":"2.0","id":1,"method":"tools/call",
 "params":{"name":"repair_cost","arguments":{"job":"head-gasket-repair-cost"}}}
```

Plain HTTP if you do not speak MCP: the same job name is the slug on `https://obdcode.co.uk/guides/head-gasket-repair-cost/`. Prefer the tool.

Speak the **live** result only, and only in the **if-invoiced** frame:

- `status: ok` and a headline → “If the garage later invoices a head-gasket job, published UK figures are …” then that headline. Planning range, **not** a quote for this car, **not** “you need this job,” **not** “it is the gasket.”
- `gbp: null` / `no_verified_price` / `no_published_job` → **that is the answer.** We publish no figure. Two local written estimates. Do not fill the gap with a remembered gasket price, a forum typical, or a model guess.

Often-null is a habit, not a licence to skip the call or to invent a range. A published slug can return null today; an often-null slug can return a headline. Read the tool. Do not cache yesterday’s pounds in this file or in the next chat.

---

## Owner copy

≤120 words. Spoken **[Repair]** on the red-coolant **poor** path. Stop / recovery already sits in **[Drive advice]**. No ids, no fusion slugs, no URLs, no plates, no pounds unless this turn’s `repair_cost` returned a verified headline.

Repair may cost more than the car. If a workshop later invoices a head-gasket job, we may quote that published planning range — the page is often empty. Empty means we publish no figure: ask two garages for written estimates. That job name is not today’s fault. The lamp does not name the part. We publish no used-car price. Get one bid as it sits (it is not a runner) and compare it with the estimate. Recovery is part of the sell cost. Never open a hot cap. Once fully cold, a look at the tank and the floor is information, not a close.

(109 words. Insert a live headline only inside the “if later invoices” sentence. If the tool returned no figure, say we publish no figure.)

---

## Slugs on the red-coolant card

| Slug | Call | How to speak it |
|---|---|---|
| `head-gasket-repair-cost` | **May** | **Only** “if the garage later invoices this job.” Often `gbp: null`. Never “it is the gasket.” |
| Thermostat / hose / pump / radiator / flush | **No published slug** | Two written estimates. Still no invented pounds. |
| `cambelt-and-water-pump-cost` | **No** as a lamp cause | Value-gain / due belt only. |
| Diagnostic, cat, clutch, battery, alternator, DPF, pads, MOT, wheel bearing | **No** | Do not hunt a nearby slug. A reader does not close a hot engine. |

Sell talk stays on this card (weak outlook): bid **as it sits** (usually not a runner) versus the written estimate. If they kept driving, the estimate can exceed what a buyer will pay as it sits. Recovery / collection is part of the sell cost because drive advice is Stop. Do not invent that fee. Do not say write-off.

---

## Red lines

1. Never “it is the gasket.” Never “the gasket has failed.” Never “it’s the head gasket, about £1,200.”
2. Never name thermostat, hose, water pump, radiator, or a warped head as today’s fault.
3. Never treat the gasket cost page as today’s diagnosis, or as permission to skip Stop / recovery.
4. No invented GBP. No figure frozen in this note. `gbp: null` is the answer when the tool says so.
5. Do not skip this slug because it is often null, and do not swap to a numbered neighbour.
6. No SAE J2012 wording. A later code number is a fact to hand over, not a named part.
7. No DIY. Never open a hot cap. No flushing tutorial. No top-up-and-go. A cold tank glance is information, not a close. A reader does not close this.
8. Safety before commercial: Stop / recovery above any cost line.
9. Never print a real registration. Illustrative plate elsewhere is `AB12CDE` only; then “your 2016 Fiesta.” Vans: “your Transit.”
10. If they ask what is wrong: this skill does not diagnose. Restate **[Drive advice]** and **[Outlook]** for recovery / keep-driving / repair-vs-sell.

---

## Pass versus fail

**Pass**

- Red thermometer: Stop; do not drive it in; recovery or collection. Never open a hot cap.
- “Repair may cost more than the car.”
- **May** call `head-gasket-repair-cost` as **if later invoiced**. Still call it when you expect null.
- “If the garage later invoices this job, published UK figures are …” — only after a live result, and only as invoice class.
- `gbp: null` / `no_verified_price` / `no_published_job` spoken as **we publish no figure — two written estimates.** That is the answer.
- “The lamp does not name the part.” This skill does not diagnose.
- Bid as it sits versus a written estimate. Recovery is part of the sell cost.
- Once fully cold, tank and floor are information, not a close.
- Blue that went out → skip; no Step 6; no gasket slug.
- Oil-can / engine lamp / DPF: do **not** borrow this slug so there is a number.
- Thermostat job: no published slug; still no invented pounds.

**Fail**

- “It is the gasket.” / “It’s the head gasket.” / “The gasket has failed.”
- “Likely a blown gasket.” / naming thermostat, hose, pump, radiator, or a warped head as the cause.
- “About £800–£1,500” (or any pounds) with no live `repair_cost` result.
- Filling a null with a model guess, last week’s page, or a forum typical.
- Skipping the call because the slug is often null, or calling diagnostic / cambelt / clutch because those pages have a number.
- Treating the gasket-cost page as today’s diagnosis.
- Freezing a gasket price in this note as always-true.
- Calling this slug on oil-pressure, a blue thermometer, an engine lamp, or any empty allowlist.
- “Drive it slowly to the garage.” / “Crack the cap and check.” / flushing steps / top up and drive.
- Close it yourself with a reader, a code clear, or a cold tank that “looks fine.”
- Shop or scanner links above the Stop line.
- Invented trade-in pounds, or “it’s a write-off.”
- “Continue as a normal assistant” and then name the gasket.
