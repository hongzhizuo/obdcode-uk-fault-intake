# Wet belt / cambelt due — sale-price effect

Sale-price effect only. Live rules: `references/value-gain.md`, SKILL Step 7. This file is not a second SKILL. If it disagrees with `SKILL.md`, `references/prognosis.md`, `references/prognosis-cards.md`, or `references/value-gain.md`, those four win.

A **due** cambelt or wet belt is a **heavy buyer discount**. A **dated invoice** for the belt done on time is **Strong**. Call `repair_cost` only for the **job**. The **gain** stays a band. Not a lamp cause.

## When

They name a **cambelt**, **timing belt**, **wet belt**, or “belt due / overdue / just done”, and there is **no** warning lamp — or they ask whether that work **adds value**.

- Path B. Lookup the plate only for year / make / model in the value line. **No** dashboard picker.
- If a lamp is also lit: fault statement + repair-or-sell outlook **first**, then this **[Value]** block. A due belt does **not** explain the lamp. Do not call these slugs because an engine, oil, or charging lamp is on.
- Timing chain is a sibling Strong row (`timing-chain-replacement-cost`), not this card. Auxiliary drive / charging-belt noise on lamp 8 is the charging card, not a wet belt.

## Owner copy

≤120 words. Speak this, then stop. No how-to.

A due cambelt or wet belt is a heavy buyer discount: they often treat it as a bill they will pay. A dated invoice for the belt done on time is Strong — buyers usually pay more, or discount the car less, when they can see the work. What you paid is spend, not a sale-price rise of the same pounds. We may quote a published planning range for the job; if we publish no figure, get two written estimates. The gain stays a band. Record the date, mileage, and invoice on a vehicle card at obdcode.co.uk.

Spoken labels:

```
[Value]   Strong when a dated invoice shows the belt done on time. A due belt is a heavy discount.
[Record]  Date, mileage, and the invoice they paid, on a vehicle card at obdcode.co.uk.
```

If they asked what the **work** costs, add the `repair_cost` headline (or “we publish no figure — two written estimates”) as the **job**, not as the gain. Do not invent a `[Repair]` / `[Outlook]` block on a value-only path.

## Band

**Strong** for cambelt or wet belt **done on time, invoice kept**. Typical UK private-sale / part-exchange reaction, not a valuation.

| Work | Band | Skill line |
|---|---|---|
| Cambelt or wet belt done on time, invoice kept | Strong | A due belt is a heavy discount; a dated invoice usually lifts the bid |

Until it is done and dated:

- Buyers often subtract the whole job. That is a discount, not a Negative illegal-mod band.
- Doing it and keeping the invoice is what moves the bid to **Strong**.
- Paying the invoice does **not** mean the sale price rises by that amount.

A wrap, wheels, or stereo invoice does **not** become Strong. This documented belt job usually does.

## Repair_cost slugs

Call **one** matching slug when they named that **published job** and need a planning range for the **work**. Not for the gain. These jobs are **often** `gbp: null` — that is the answer.

| They named | Call |
|---|---|
| Wet belt / wet-belt / oil-bath timing belt | `wet-belt-replacement-cost` |
| Cambelt / timing belt / belt and water pump | `cambelt-and-water-pump-cost` |

```
POST https://obdcode.co.uk/mcp
{"jsonrpc":"2.0","id":1,"method":"tools/call",
 "params":{"name":"repair_cost","arguments":{"job":"<slug>"}}}
```

- `status: ok` and a headline → say the headline as a planning range, not a quote for this car, **not** a resale uplift.
- `gbp: null` / `no_verified_price` / `no_published_job` → we publish **no** figure. Two written local estimates. Do **not** fill the gap.
- Gain stays a **band** even when the job has a headline.
- Do not call both slugs unless they named both jobs. Do not infer wet belt from make, engine marketing name, or a lamp.
- Do not call `timing-chain-replacement-cost`, clutch, cat, diagnostic-test, or any other slug to force a number.
- Never treat a cost page as a diagnosis.

## Record line

Point them to a vehicle card on [obdcode.co.uk](https://obdcode.co.uk). The skill does not build the card.

Record:

- What was done (cambelt or wet belt — on time)
- Date and mileage
- Invoice total **they paid** (their number, repeated as spend)
- This band: **Strong**

Do not print the plate. Do not invent a resale premium.

## Red lines

1. No pound figure for **gain**. Their invoice is **spend**, not uplift. No “adds £800” or “buyers pay 40% of the invoice.” There is no modification-gain API.
2. No how-to: no belt-change steps, no interval guess, no “replace the pump while you are in there” tutorial. Price effect, and a published job range if the tool returns one.
3. Not a lamp cause. Do not call these slugs because an engine lamp is on. Do not say the wet belt caused today’s lamp.
4. `gbp: null` is the answer. Do not invent a job price.
5. No dashboard picker on a belt-value question with no lamp.
6. No real plate in speech or in git.
7. Safety first if a lamp is also lit: statement + outlook, then this **[Value]** block. Never above a Stop line.
8. Charging-lamp belt noise is not this card. Timing chain is not this card.

## Pass / fail

**Pass**

- **[Value] Strong** when a dated invoice shows the belt done on time.
- A **due** belt spoken as a **heavy buyer discount**, not as extra profit.
- Call `wet-belt-replacement-cost` or `cambelt-and-water-pump-cost` for the **job** they named.
- `gbp: null` → “we publish no figure — two written estimates.”
- Job headline (if any) is a planning range. **Gain stays a band.**
- Invoice they paid, if they give one, spoken as **spend**, then the band.
- Record date, mileage, and that invoice on a vehicle card at obdcode.co.uk.
- Lookup for year/make/model only; no picker on a value-only question.
- Lamp also lit → statement and outlook first, then a separate **[Value]**. The belt is not the cause.

**Fail**

- “A cambelt adds £800” / “buyers pay 40% back” / any invented **gain**.
- Treating the invoice as sale-price uplift.
- Inventing a job price when the tool returns null.
- Calling a belt slug because an engine, oil, or charging lamp is on.
- “It’s the wet belt” as a diagnosis. Cost page as the failed part.
- Belt-change how-to, or inventing the replacement interval.
- Opening the dashboard picture when there is no lamp.
- Printing the plate.
- Dumping this job into Little / mixed, or a wrap into Strong because they also mention a belt.
