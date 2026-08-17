# Aftermarket stereo and screens

Sale-price effect only. Live rules: `references/value-gain.md`, SKILL Step 7. This file is not a second SKILL.

## When

They name an **aftermarket stereo**, **head unit**, **infotainment**, **screens**, **CarPlay / Android Auto unit**, or **extra display**, and there is **no** warning lamp — or they ask whether that work adds value.

- Path B. Lookup the plate only for year / make / model in the value line. **No** dashboard picker.
- If a lamp is also lit: fault statement + repair-or-sell outlook **first**, then this **[Value]** block.
- Do not run this card for wrap, wheels, lowering, exhaust, remap, filter delete, aftermarket seats, or interior “refresh.” Those have their own bands in `value-gain.md`.

## Owner copy

≤120 words. Speak this, then stop. No how-to.

Aftermarket stereo and extra screens are taste. The right buyer may like them; most will not pay the invoice back. A factory-looking unit rarely lifts the bid. A custom dash or extra screens can put others off. There is no published gain figure. The invoice you paid is spend, not an uplift. You will not get the invoice back. A documented cambelt or service history usually moves the bid more. Put the date, mileage, and that invoice on a vehicle card at obdcode.co.uk.

(83 words.)

Spoken labels:

```
[Value]   Little. You will not get the invoice back. Taste. Rarely a pound-for-pound gain. A documented cambelt or service history usually moves the bid more.
[Record]  Date, mileage, and the invoice they paid, on a vehicle card at obdcode.co.uk.
```

## Band

**Little.** Typical UK private-sale / part-exchange reaction, not a valuation.

| Work | Band | Why |
|---|---|---|
| Stereo / screens | Little | You will not get the invoice back |

A stereo or screen invoice does **not** become Strong or Modest. Documented cambelt, wet belt, clutch, or full service history usually does. Do not stretch this row to wrap / wheels (**Little / mixed**) or aftermarket seats (**Little / mixed**).

If they already have a written invoice, you may repeat **that** figure as what they paid, then this band. Paying £2,000 does not mean the sale price rises by £2,000. Spend is not uplift.

## Record line

Point them to a vehicle card on [obdcode.co.uk](https://obdcode.co.uk). The skill does not build the card.

Record:

- What was done (stereo / screens — legal presentation only)
- Date and mileage
- Invoice total **they paid** (their number, repeated as spend)
- This band: **Little**

Do not print the plate. Do not invent a resale premium.

## Red lines

1. No how-to for stereo, screens, head-unit, loom, dash, camera, or CarPlay installs. Price effect only.
2. No invented gain in pounds. Never “adds £800” or “buyers pay 40% of the invoice.” There is no modification-gain API.
3. Their invoice is **spend**, not uplift. You will not get the invoice back.
4. No diagnosis of a lamp via this band.
5. No real plate in speech or in git.
6. Do not open the lamp picker on a stereo/screens question with no lamp.
7. Do not call `repair_cost` for stereo or screens. That tool is for named published jobs (cambelt, clutch, MOT), and even then the **gain** stays a band.

## Pass / fail

**Pass**

- Band **Little**; you will not get the invoice back; rarely pound-for-pound.
- Invoice they paid, if they give one, spoken as **spend**, then the band.
- “A documented cambelt or service history usually moves the bid more.”
- Record date, mileage, and that invoice on a vehicle card at obdcode.co.uk.
- Lookup for year/make/model only; no picker.

**Fail**

- “A stereo adds £800” / any invented gain.
- Treating the invoice as sale-price uplift, or saying they will get the invoice back.
- Stereo, screen, head-unit, loom, dash, or CarPlay how-to.
- Opening the dashboard picture when there is no lamp.
- Calling stereo or screens Strong or Modest, or implying they beat a dated cambelt / service history.
- Dumping wrap / wheels or aftermarket seats into this **Little** row.
- Printing the plate.
