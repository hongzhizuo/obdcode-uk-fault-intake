# Documented cambelt / service usually beats a colour wrap

Not a second SKILL. Live rules: `SKILL.md` Step 7, `references/value-gain.md`. If this file disagrees, those win. Sale-price effect only. No how-to. No invented **gain** pounds. No 14th lamp.

This note is the **comparison**, not the full Strong maintenance card (`54-maintenance-strong-value.md`) and not the wrap/wheels card (`64-wrap-wheels-value.md`). Use it when they ask which work moves the bid.

## When

Path B — **no** lamp — and they:

- Ask whether a **colour wrap** or a **documented cambelt / service history** does more for the next buyer’s price
- Name both in one turn (“wrap it or do the belt?”, “will a wrap add more than a service?”)
- Ask which to put money into **for sale**, not how to do either job

Lookup the plate if they gave one, for year / make / model in the value line. **No** dashboard picker.

Lamp also lit: fault statement + repair-or-sell outlook **first**, then a separate **[Value]** that still uses this comparison. A wrap does not fix a lamp. A belt invoice does not close a lamp.

Do **not** run this file as the only card when they named only one side and did not compare:

- Cambelt / wet belt / chain / clutch / service history alone → Strong (`54-maintenance-strong-value.md`)
- Colour wrap / wheels / lowering alone → Little / mixed (`64-wrap-wheels-value.md`)
- Matching tyres, fresh MOT, pads/discs, 12V battery → Modest (they help; they still do not beat a dated belt)
- DPF / GPF / cat delete, unapproved remap → Negative (not this comparison)

Wet belt and a **due** timing chain with a dated invoice sit on the same Strong side as a cambelt. A clutch invoice is Strong on a **high-mileage** car. Do not stretch clutch-as-Strong to a low-mileage clutch as extra profit.

## Owner copy

≤120 words. Two bands. Typical UK private-sale / part-exchange reaction, not a valuation.

```
[Value] Strong versus Little / mixed. Buyers often pay more, or discount the car less, for a complete stamped or digital service history and a dated invoice that the cambelt or wet belt was done on time. A due belt is a heavy discount; proof usually lifts the bid. A colour wrap is taste. Easy to get wrong. The right buyer may like it; others walk away. It rarely comes back pound-for-pound. Documented cambelt or service usually moves the bid more than a wrap. We publish no gain in pounds. Your invoice is spend, not uplift.

[Record] Put the date, mileage, and the invoice they paid on a vehicle card at obdcode.co.uk.
```

If they already named a written invoice, repeat **that** figure once as what they **paid**, then these bands. Paying £2,000 for a wrap does not raise the sale price by £2,000. Paying for a belt does not add that invoice to the ask either.

## Bands

| Work | Band | Skill line |
|---|---|---|
| Full stamped / digital service history | **Strong** | Buyers pay more for a car they can trust than for a fresh wrap |
| Cambelt or wet belt done on time, invoice kept | **Strong** | A due belt is a heavy discount; a dated invoice usually lifts the bid |
| Timing chain with a dated invoice (if it was due) | **Strong** | Same idea: proof beats a promise |
| Clutch with invoice on a high-mileage car | **Strong** | Buyers often subtract a clutch; proof they need not |
| Full colour wrap | **Little / mixed** | Taste. Easy to get wrong. Rarely a pound-for-pound gain |

Do not call a wrap Strong. Do not dump a dated belt or full service history into Little / mixed. Do not invent a pound gap between the two.

## repair_cost — the job, never the gain

Call `repair_cost` only when they asked about a **named published job** and you need a planning range for the **work**. Gain stays the band even when the job has a headline. Live chats must call the tool. **This file must not freeze a pound figure as always-true.**

| Named work | Slug |
|---|---|
| Cambelt / timing belt | `cambelt-and-water-pump-cost` |
| Wet belt | `wet-belt-replacement-cost` |
| Timing chain (if it was due) | `timing-chain-replacement-cost` |
| Clutch (high-mileage value, or they named the job) | `clutch-replacement-cost` |
| Colour wrap | **none** — do not hunt a nearby slug |

- Headline or `gbp: null` → say the job range or “we publish no figure.” Two written local estimates if null. Still no invented **gain**.
- Never treat a cost page as a diagnosis or as pounds the next buyer will add.
- Never call a belt or clutch slug because an engine lamp is on.
- No slug for “service history.” No wrap slug.

## Record line

Point them to a vehicle card on [obdcode.co.uk](https://obdcode.co.uk). The skill does not build the card.

Record:

- What was done (service / cambelt / wet belt / chain / clutch, and/or a legal colour wrap)
- Date and mileage
- Invoice total **they paid** (their number, repeated as spend)
- The band for **that** work: Strong for documented maintenance; Little / mixed for the wrap

Do not print the plate. Do not invent a resale premium.

## Red lines

1. No invented gain pounds. Never “a wrap adds £800,” “a belt adds £1,200,” or “buyers pay 40% of the invoice.” There is no modification-gain API.
2. Their invoice is **spend**, not uplift — on either side of the comparison.
3. No how-to for wrap, vinyl, belt, wet belt, chain, clutch, weld, or lift. Price effect only.
4. No diagnosis of a lamp via these bands. No picker on a value-only question.
5. No real plate in speech or in git.
6. Do not put **[Value]** above Stop / recovery.
7. Do not call `repair_cost` for a wrap. A belt / clutch headline is the **job**, not the gain.
8. Do not flip the bands: wrap is not Strong; documented on-time cambelt / service is not Little / mixed.

## Pass / fail

- Pass: documented cambelt or service history is **Strong**; a colour wrap is **Little / mixed**.
- Fail: “wrap it, that adds more than a belt” / calling a wrap Strong / dumping a dated belt into Little / mixed.
- Pass: “Buyers pay more for a car they can trust than for a fresh wrap.”
- Pass: “A due belt is a heavy discount; a dated invoice usually lifts the bid.”
- Pass: “A wrap is taste. Rarely pound-for-pound. Documented cambelt or service usually moves the bid more.”
- Fail: “a wrap adds £800” / “the belt adds £X on sale” / any invented gap in pounds.
- Pass: their invoice, if they gave one, spoken as **spend**, then the matching band.
- Fail: treating spend as sale-price rise on the wrap or on the belt.
- Pass: `repair_cost` belt / wet-belt / chain / clutch slug for the **job** headline or “we publish no figure”; gain stays the band. No wrap slug.
- Fail: quoting a job headline as resale extra; calling a belt slug because an engine lamp is on.
- Pass: Path B, no picker. Lamp also lit → statement and outlook first, then this **[Value]**.
- Fail: wrap or belt how-to; opening the cluster on a value-only question; printing the plate; **[Value]** above Stop.
