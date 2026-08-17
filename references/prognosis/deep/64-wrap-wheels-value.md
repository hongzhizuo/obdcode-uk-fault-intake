# Colour wrap and aftermarket wheels

Sale-price effect only. Live rules: `references/value-gain.md`, SKILL Step 7. This file is not a second SKILL.

## When

They name a **colour wrap**, **aftermarket wheels**, or **lowering**, and there is **no** warning lamp — or they ask whether that work adds value.

- Path B. Lookup the plate only for year / make / model in the value line. **No** dashboard picker.
- If a lamp is also lit: fault statement + repair-or-sell outlook **first**, then this **[Value]** block.
- Do not run this card for PPF, respray, stereo, exhaust, remap, or filter delete. Those have their own bands in `value-gain.md`.

## Owner copy

≤120 words. Speak this, then stop. No how-to.

Colour wrap and aftermarket wheels are taste. The right buyer may like them; others walk away, or they discount tyre and geometry bills. They rarely come back pound for pound. There is no published gain figure. The invoice you paid is spend, not an uplift. A documented cambelt or service history usually moves the bid more. If you still do the work, put the date, mileage, and that invoice on a vehicle card at obdcode.co.uk.

(79 words.)

Spoken labels:

```
[Value]   Little / mixed. Taste. Rarely pound-for-pound. A documented cambelt or service history usually moves the bid more.
[Record]  Date, mileage, and the invoice they paid, on a vehicle card at obdcode.co.uk.
```

## Band

**Little / mixed.** Typical UK private-sale / part-exchange reaction, not a valuation.

| Work | Band | Why |
|---|---|---|
| Full colour wrap | Little / mixed | Taste. Easy to get wrong. Rarely a pound-for-pound gain |
| Aftermarket wheels / lowering | Little / mixed | Right buyer vs smaller pool and possible tyre / geometry bills |

A wrap or wheel invoice does **not** become Strong. Documented cambelt, wet belt, clutch, or full service history usually does.

## Record line

Point them to a vehicle card on [obdcode.co.uk](https://obdcode.co.uk). The skill does not build the card.

Record:

- What was done (colour wrap and/or wheels — legal presentation only)
- Date and mileage
- Invoice total **they paid** (their number, repeated as spend)
- This band: **Little / mixed**

Do not print the plate. Do not invent a resale premium.

## Red lines

1. No how-to for wrap, wheels, lowering, weld, or lift. Price effect only.
2. No invented gain in pounds. Never “adds £800” or “buyers pay 40% of the invoice.” There is no modification-gain API.
3. Their invoice is **spend**, not uplift. Paying £2,000 does not raise the sale price by £2,000.
4. No diagnosis of a lamp via this band.
5. No real plate in speech or in git.
6. Do not open the lamp picker on a wrap/wheels question with no lamp.
7. Do not call `repair_cost` for wrap or wheels. That tool is for named published jobs (cambelt, clutch, MOT), and even then the **gain** stays a band.

## Pass / fail

**Pass**

- Band **Little / mixed**; taste; smaller pool; rarely pound-for-pound.
- Invoice they paid, if they give one, spoken as **spend**, then the band.
- “A documented cambelt or service history usually moves the bid more.”
- Record date, mileage, and that invoice on a vehicle card at obdcode.co.uk.
- Lookup for year/make/model only; no picker.

**Fail**

- “A wrap adds £800” / any invented gain.
- Treating the invoice as sale-price uplift.
- Wrap, wheel, or lowering how-to.
- Opening the dashboard picture when there is no lamp.
- Calling wrap or wheels Strong, or implying they beat a dated cambelt / service history.
- Printing the plate.
