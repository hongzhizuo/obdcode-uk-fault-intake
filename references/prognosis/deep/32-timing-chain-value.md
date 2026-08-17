# 32 · `timing-chain-replacement-cost` — due-chain value

Sale-price effect only. Live rules: `references/value-gain.md`, SKILL Step 7. This file is not a second SKILL. If it disagrees with `SKILL.md`, `references/prognosis.md`, `references/prognosis-cards.md`, or `references/value-gain.md`, those four win.

**Slug:** `timing-chain-replacement-cost`  
**Use:** value-gain / a **due** timing chain they already named  
**Band:** **Strong** when a **dated invoice** shows it was done **when due**. Proof beats a promise.  
**Never:** because an engine lamp is on (steady or flashing). Not a lamp cause.  
**Often null:** still call the slug; `gbp: null` is the answer. Do not invent a range.  
**Headline ≠ gain:** a published job range is the **work**, not what the sale price rises by.

Live chats must call `repair_cost`. This file must not freeze a pound figure as always-true.

## When

They name a **timing chain**, “chain due / overdue / just done”, or ask whether that work **adds value**, and there is **no** warning lamp — Path B.

- Lookup the plate only for year / make / model in the value line. **No** dashboard picker.
- If a lamp is also lit: fault statement + repair-or-sell outlook **first**, then this **[Value]** block. A due chain does **not** explain the lamp. Do not call this slug because an engine, oil, or charging lamp is on.
- Cambelt / timing belt / wet belt are the sibling Strong row (`cambelt-and-water-pump-cost`, `wet-belt-replacement-cost`), not this card.
- Auxiliary drive / charging-belt noise on lamp 8 is the charging card, not a timing chain.
- Do not infer chain vs belt from make, engine marketing name, or a lamp.

Do **not** call this slug when:

- A **steady** amber engine outline is on (`engine-steady`). Allowlist is `car-diagnostic-test-cost` only.
- The engine outline is **flashing** (`engine-flashing`). First invoice is still a diagnostic. Converter only as “if later invoiced.” Chain is never on that card.
- Any other lamp is on and they have **not** named a timing chain. Do not hunt this slug because it might have a number.
- They ask “so is it the timing chain?” after an engine lamp. That is a diagnosis request. Refuse. Restate **[Drive advice]** and **[Outlook]**. Do not fetch this slug to fill the silence.
- Rattle, stretch, or a rough idle with an engine lamp, and they never said **timing chain**. Those facts go in **[Since]**. They do not name this job.

Lamp **and** a chain they already named: finish the lamp statement and outlook **first** (safety). Use the lamp’s own slugs for **[Repair]**. Then a separate **[Value]** (this slug only for the named chain work). Do not fold the chain headline into the lamp as the cause.

Vans: same rule. Say **your Transit**.

## Owner copy

≤120 words. Speak this, then stop. No how-to.

A due timing chain is a heavy buyer discount: they often treat it as a bill they will pay. A dated invoice for the chain done when it was due is Strong — buyers usually pay more, or discount the car less, when they can see the work. Proof beats a promise that the chain “should be fine.” What you paid is spend, not a sale-price rise of the same pounds. We may quote a published planning range for the job; this job is often unpublished — if we publish no figure, get two written estimates. The gain stays a band. Record the date, mileage, and invoice on a vehicle card at obdcode.co.uk.

Spoken labels:

```
[Value]   Strong when a dated invoice shows the chain done when it was due. A due chain is a heavy discount. Proof beats a promise.
[Record]  Date, mileage, and the invoice they paid, on a vehicle card at obdcode.co.uk.
```

If they asked what the **work** costs, add the `repair_cost` headline (or “we publish no figure — two written estimates”) as the **job**, not as the gain. Do not invent a `[Repair]` / `[Outlook]` block on a value-only path.

If they only have an engine lamp and never named a chain, do **not** speak this block. Speak the lamp outlook. Scan or diagnostic-test cost. “The lamp does not name the part.”

## Band

**Strong** for a timing chain **with a dated invoice, if it was due**. Typical UK private-sale / part-exchange reaction, not a valuation.

| Work | Band | Skill line |
|---|---|---|
| Timing chain with a dated invoice (if it was due) | Strong | Same idea: proof beats a promise |

Until it is done, dated, and was due:

- Buyers often subtract the whole job. That is a discount, not a Negative illegal-mod band.
- Doing it when due and keeping the invoice is what moves the bid to **Strong**.
- A promise with no invoice is not Strong.
- Paying the invoice does **not** mean the sale price rises by that amount.

A wrap, wheels, or stereo invoice does **not** become Strong. This documented due-chain job usually does.

## Job headline is not sale gain

There is **no** modification-gain API. `repair_cost` never becomes an uplift in pounds.

| Figure | What it is | What it is not |
|---|---|---|
| `repair_cost` headline (`status: ok`) | Planning range for the **chain job** | A quote for this car; a sale-price rise |
| `gbp: null` / `no_verified_price` / `no_published_job` | The answer: we publish no figure — two written estimates | A gap to fill with “about £400–£800” |
| Their written invoice | What **they paid** (spend) | What buyers will add on |
| Value **band** | Typical buyer reaction | A valuation or a pound gain |

This slug is **often** `gbp: null`. Still call it when they named the job. Skipping the tool, or swapping to cambelt / clutch / diagnostic-test because those pages have a number, is a fail. An often-null slug can still return a headline; read the tool. Gain stays the Strong band even when the job has a headline.

Do not invent “adds £800” or “buyers pay 40% of the invoice.”

## Repair_cost slug

Call **only** this slug when they named a **timing chain** and need a planning range for the **work**. Not for the gain. Not because a lamp is on.

```
POST https://obdcode.co.uk/mcp
{"jsonrpc":"2.0","id":1,"method":"tools/call",
 "params":{"name":"repair_cost","arguments":{"job":"timing-chain-replacement-cost"}}}
```

Prefer the tool. The same name is the slug on `https://obdcode.co.uk/guides/timing-chain-replacement-cost/`.

- `status: ok` and a headline → say the headline as a planning range, not a quote for this car, **not** a resale uplift.
- `gbp: null` / `no_verified_price` / `no_published_job` → we publish **no** figure. Two written local estimates. Do **not** fill the gap. That is the usual answer for this job.
- Gain stays a **band** even when the job has a headline.
- Do not call `cambelt-and-water-pump-cost`, `wet-belt-replacement-cost`, clutch, cat, diagnostic-test, or any other slug to force a number.
- Do not infer the interval, or “replace the guides / tensioner while you are in there.” No how-to.
- Never treat a cost page as a diagnosis.

A cost page is not the failed part. Never pick this slug because it is the only one with a number.

## Record line

Point them to a vehicle card on [obdcode.co.uk](https://obdcode.co.uk). The skill does not build the card.

Record:

- What was done (timing chain — when it was due)
- Date and mileage
- Invoice total **they paid** (their number, repeated as spend)
- This band: **Strong**

Do not print the plate. Do not invent a resale premium.

## Red lines

1. No pound figure for **gain**. Their invoice is **spend**, not uplift. No “adds £800” or “buyers pay 40% of the invoice.” There is no modification-gain API.
2. No how-to: no chain-change steps, no interval guess, no “guides and tensioner while you are in there” tutorial. Price effect, and a published job range if the tool returns one.
3. Not a lamp cause. Do not call this slug because an engine lamp is on. Do not say the timing chain caused today’s lamp.
4. `gbp: null` is the answer. This job is often unpublished. Do not invent a job price. Do not skip the call, or swap slugs to find a number.
5. No dashboard picker on a chain-value question with no lamp.
6. No real plate in speech or in git. Illustrative only: `AB12CDE`, then **your 2016 Fiesta**.
7. Safety first if a lamp is also lit: statement + outlook, then this **[Value]** block. Never above a Stop line.
8. Cambelt / wet belt / charging-lamp belt noise are not this card.
9. No SAE J2012 wording. A later code number is a fact to hand over, not a named part.
10. Do not treat this file’s words as a frozen price.

## Pass / fail

**Pass**

- **[Value] Strong** when a dated invoice shows the chain done **when it was due**. Proof beats a promise.
- A **due** chain spoken as a **heavy buyer discount**, not as extra profit.
- Call `timing-chain-replacement-cost` for the **job** they named.
- `gbp: null` → “we publish no figure — two written estimates.” Still call; this slug is often null.
- Job headline (if any) is a planning range. **Gain stays a band.**
- Invoice they paid, if they give one, spoken as **spend**, then the band.
- Record date, mileage, and that invoice on a vehicle card at obdcode.co.uk.
- Lookup for year/make/model only; no picker on a value-only question.
- Lamp also lit → statement and outlook first, then a separate **[Value]**. The chain is not the cause.
- Engine lamp on, chain not named → `car-diagnostic-test-cost` (and cat only if the flashing card allows “if later invoiced”). “A scan is the next step; the lamp does not name the part.”
- “So is it the timing chain?” after a lamp → this skill does not diagnose. Restate drive advice and outlook.

**Fail**

- “A timing chain adds £800” / “buyers pay 40% back” / any invented **gain**.
- Treating the invoice or the job headline as sale-price uplift.
- Inventing a job price when the tool returns null.
- Skipping the call because it is often null, or calling cambelt / clutch / diagnostic-test to force a number.
- Calling this slug because an engine, oil, or charging lamp is on.
- “It’s the timing chain” as a diagnosis. Cost page as the failed part.
- Chain-change how-to, or inventing the replacement interval.
- Opening the dashboard picture when there is no lamp.
- Printing the plate.
- Dumping this job into Little / mixed, or a wrap into Strong because they also mention a chain.
- Using the chain headline as the cause of the lamp.
