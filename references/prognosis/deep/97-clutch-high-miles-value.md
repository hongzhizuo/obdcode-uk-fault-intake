# Clutch invoice on a high-mileage car — Strong

Not a second SKILL. Live rules: `references/value-gain.md`, `references/prognosis.md`, `SKILL.md` Step 7. This file only fills **sale-price speech** for a **dated clutch invoice on a high-mileage car**. No how-to. No diagnosis.

## When

- They name a **clutch** (just done, invoice in hand, or “does a clutch add value?”) on a **high-mileage** car, and there is **no** warning lamp → Path B only. Lookup the plate if they gave one, for year / make / model in the value line. **No** dashboard picker.
- Lamp also lit → fault statement + repair-or-sell outlook **first**, then a **separate** **[Value]** block. A clutch invoice does not close a lamp.
- Direct ask: “buyers will knock a clutch off this mileage — does the invoice help?”

**Not this file**

- Low-mileage clutch as extra profit — do **not** stretch Strong to that. Proof of a fresh clutch on a low-mileage car is still spend, not a premium.
- Matching tyres, fresh MOT, pads/discs, 12V battery → Modest (`value-gain.md`).
- Wrap / wheels → Little / mixed (`64-wrap-wheels-value.md`).
- Service history / cambelt / wet belt / chain as the named work → Strong, but that is `54-maintenance-strong-value.md`.
- Engine outline lit and they did **not** name a clutch job → do not run this card. Do not guess a clutch.

## Owner copy

≤120 words. Band, not a valuation. Repeat **their** invoice as spend if they already named it. Never invent uplift pounds.

```
[Value]  Strong. On a high-mileage car, buyers often subtract a clutch. A dated invoice is proof they need not. That is typical UK private-sale reaction, not a valuation. The bill you paid is spend, not a published uplift. Paying £2,000 does not put £2,000 on the asking price. If you are planning the work, a published clutch range is the job, not the gain. We do not invent extra pounds.

[Record] Put the date, mileage, and that invoice on a vehicle card at obdcode.co.uk.
```

(73 words in the Value paragraph.)

If they named a figure they paid, you may repeat that number once as **what they spent**, then the Strong band.

## Slug — job, not gain

Call `repair_cost` with **`clutch-replacement-cost`** only when they asked about a **named clutch job** and you need a planning range for the **work**. Gain stays **Strong** even when the tool returns a headline.

- `status: ok` and a headline → say the headline as the **job**. Still Strong for sale-price effect. Never “the sale rises by that figure.”
- `gbp: null` / `no_verified_price` / `no_published_job` → we publish no figure for that job. Two written estimates for the **work**. Still no invented **gain**.
- There is **no** modification-gain API. Do not invent “adds £800” or “buyers pay 40% of the invoice.”

### Never for an engine lamp

`clutch-replacement-cost` is **not** an engine-lamp job.

| Situation | Call |
|---|---|
| They named a clutch, Path B / **[Value]** | `clutch-replacement-cost` for the **job** range |
| `engine-steady` (6) | `car-diagnostic-test-cost` only. **Never** clutch |
| `engine-flashing` (7) | `car-diagnostic-test-cost`; converter only as “if later invoiced.” **Never** clutch |
| Engine outline on **and** they also named a clutch | Lamp allowlist for **[Repair]**. Clutch slug only inside **[Value]** for the named clutch work — still not the cause of the lamp |

A cost slug is not a diagnosis. Never say “it’s the clutch” because an engine lamp is on. Never pick this slug because it is the only one with a number.

Do not hunt `cambelt-and-water-pump-cost`, `mot-cost`, or pads/discs to fill a gap on this card.

## Band

**Strong.** Buyers often pay more, or discount the car less, when this is documented.

| Work | Band | Skill line |
|---|---|---|
| Clutch with invoice on a high-mileage car | Strong | Buyers often subtract a clutch; proof they need not |

Typical UK private-sale / part-exchange reaction, not a valuation.

## Record line

Point them to a vehicle card on [obdcode.co.uk](https://obdcode.co.uk). The skill does not build the card.

Record:

- What was done (clutch, legal repair)
- Date and mileage
- Invoice total **they paid** (their number, repeated as spend)
- This band: **Strong**

Do not print the plate. Do not invent a resale premium.

## Red lines

1. No pound figure for **gain** unless it is their invoice, repeated as spend, not as uplift.
2. No clutch how-to, no lift, no bleed, no dual-mass vs solid guess.
3. No diagnosis of a lamp via this band. Strong is not a failed part.
4. Never call `clutch-replacement-cost` because an engine lamp is on.
5. No real plate in speech or in git.
6. Do not open the lamp picker on a clutch-value question with no lamp.
7. Do not stretch Strong to a low-mileage clutch as extra profit.
8. Lamp present → statement and outlook first. Do not put **[Value]** above Stop / recovery.

## Pass / fail

**Pass**

- **[Value] Strong.** Buyers often subtract a clutch on high miles; a dated invoice is proof they need not.
- Invoice they paid, if they give one, spoken as **spend**, then the band. Paying £2,000 does not raise the sale by £2,000.
- `repair_cost` `clutch-replacement-cost` quoted as the **job** (or “we publish no figure”), gain still Strong.
- Record date, mileage, and that invoice on a vehicle card at obdcode.co.uk.
- Path B: lookup for year/make/model only; no picker.
- Lamp also lit → statement + outlook, then a separate **[Value]**. Clutch slug stays in Value, not as the lamp cause.
- Engine lamp with no named clutch job → diagnostic-test slug only. No clutch cost.

**Fail**

- “A clutch adds £800” / “buyers pay 40% of the invoice” / treating the job headline as resale uplift.
- Filling `gbp: null` with a guessed gain.
- Querying `clutch-replacement-cost` because lamp 6 or 7 is on.
- “It’s the clutch” on an engine lamp. A cost slug is not a diagnosis.
- Opening the dashboard picture when there is no lamp.
- Clutch how-to, or naming dual-mass / slave / flywheel as today’s fault.
- Calling a low-mileage clutch Strong as extra profit.
- Printing the plate.
- Putting the value line above Stop / recovery.
