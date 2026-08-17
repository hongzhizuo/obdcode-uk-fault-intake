# Modest: matching tyres, fresh MOT, pads/discs, 12V battery

Not a second SKILL. Live rules: `SKILL.md` Step 7, `references/value-gain.md`. If this file disagrees, those win. Sale-price effect only. No how-to. No invented **gain** pounds.

These four jobs are **Modest**: they help the sale; they rarely cover the invoice; they rarely add a premium.

## When

Path B — **no** lamp — and they name, or ask whether this **adds value**:

- Matching **new tyres** with a date
- A **fresh MOT** with **no** dangerous / major carries
- **Pads and discs** with an invoice
- A **12V battery** with an invoice

Lookup the plate if they gave one, for year / make / model in the value line. **No** dashboard picker.

If a lamp is also lit: fault statement + repair-or-sell outlook **first**, then a separate **[Value]** block. Safety before this band.

Do **not** run this card for:

- Full service history, cambelt / wet belt / chain, clutch — those are **Strong** (`value-gain.md`)
- Wrap, wheels, stereo, remap, delete — other bands
- Two unmatched cheap tyres (not “matching new tyres with date”)
- An MOT that still carries **dangerous** or **major** defects — that is still a bill for the next buyer, not this Modest line
- TPMS lamp 10 as a close-it-yourself inflate (Path A, `prognosis-cards.md`) — fitting tyres later can still be Modest **on sale**
- Hydraulic Stop brake lamp — do not treat pads/discs as the **cause**; an invoice they already have can still be Modest **on sale** after the outlook
- Charging lamp 8 — do not pick battery vs alternator; a battery invoice they already have can still be Modest **on sale**

Vans: same band. Say **your Transit**.

## Owner copy

≤120 words. Price effect only. Speak the named job; do not dump all four if they only asked about one.

Matching new tyres with a date, a fresh MOT with no dangerous or major carries, pads and discs with an invoice, and a 12V battery with an invoice help the sale. They rarely cover the invoice and they are not a premium. Expected wear, or an immediate bill removed — not extra profit, and not a new car. We publish no gain in pounds. Your invoice is spend, not uplift. A dated cambelt or full service history usually moves the bid more. Record the date, mileage, and that invoice on a vehicle card at obdcode.co.uk.

(104 words.)

Per-job skill lines (use the one they named):

| Work | [Value] line |
|---|---|
| Matching new tyres with date | Modest. Helps; it is not a new car. Rarely a premium. |
| Fresh MOT, no dangerous / major carries | Modest. Removes an immediate bill; it is not extra profit. |
| Pads and discs with invoice | Modest. Expected wear. Proof helps; it rarely adds a premium. |
| 12V battery with invoice | Modest. Expected wear. Proof helps; it rarely adds a premium. |

Spoken labels:

```
[Value]   Modest. Helps the sale; rarely a premium. Rarely covers the invoice.
[Record]  Date, mileage, and the invoice they paid, on a vehicle card at obdcode.co.uk.
```

If they already have a written invoice, repeat **that** figure as what they **paid**, then this band. Paying £400 does not raise the sale price by £400.

## Band

**Modest.** Typical UK private-sale / part-exchange reaction, not a valuation. Helps the sale; rarely covers the invoice.

| Work | Band | Skill line |
|---|---|---|
| Matching new tyres with date | Modest | Helps; it is not a new car |
| Fresh MOT with no dangerous / major carries | Modest | Removes an immediate bill; it is not extra profit |
| Pads and discs with invoice | Modest | Expected wear. Proof helps, it rarely adds a premium |
| 12V battery with invoice | Modest | Same |

Do not upgrade these to **Strong**. Do not dump them into **Little / mixed**.

## repair_cost — the job, never the gain

Call `repair_cost` only when they ask about a **named published job** and you need a planning range for the **work**. Gain stays **Modest** even when the tool returns a headline. Live chats must call the tool. **This file must not freeze a pound figure as always-true.**

| Named work | Slug | Call when |
|---|---|---|
| Matching new tyres | **none** | There is **no** published tyre-set job. Do not hunt a nearby slug. Do not invent a tyre bill. Band is still Modest. |
| Fresh MOT | `mot-cost` | Booking / test **job** range. Not a lamp repair. Not “Expect a fail.” |
| Pads and discs | `brake-pads-and-discs-cost` | They named that invoice class, or asked what the **job** usually costs. Never as the cause of a hydraulic Stop lamp. |
| 12V battery | `car-battery-replacement-cost` | They named a battery invoice, or asked the **job** range. Not “it is the battery” on lamp 8. |

- `status: ok` and a headline → say the headline as the **job** planning range, then the Modest **gain** band.
- `gbp: null` / `no_verified_price` / `no_published_job` → we publish no figure for the job. Two written local estimates. Gain is still Modest.
- Do **not** call cambelt, clutch, cat, or diagnostic slugs because they asked about tyres, MOT, pads, or a battery invoice.
- A cost page is not a diagnosis and not a resale premium.

## Record line

Point them to a vehicle card on [obdcode.co.uk](https://obdcode.co.uk). The skill does not build the card.

Record:

- What was done (matching tyres / MOT / pads and discs / 12V battery)
- Date and mileage
- Invoice total **they paid** (their number, repeated as spend)
- This band: **Modest**

Do not print the plate. Do not invent a resale premium.

## Red lines

1. No invented **gain** pounds. Never “tyres add £400,” “an MOT adds £200,” or “buyers pay 40% of the invoice.” There is no modification-gain API.
2. Their invoice is **spend**, not uplift.
3. No how-to: no fitting tyres, pads, discs, or a battery; no “how to pass an MOT.”
4. No tyre-set `repair_cost` slug. No frozen GBP in this file.
5. No diagnosis of a lamp via this band. No picker on a value-only question.
6. No real plate in speech or in git.
7. Do not put **[Value]** above Stop / recovery.
8. MOT speech: do not say “Expect a fail.” A fresh pass with no dangerous / major carries is Modest on sale; an outstanding dangerous / major is not this card.
9. Do not call these Strong. Cambelt / service history usually moves the bid more.

## Pass / fail

- Pass: **[Value] Modest.** Helps the sale; rarely a premium; rarely covers the invoice.
- Fail: “buyers will pay the invoice back” / treating spend as sale-price rise.
- Pass: matching new tyres with date — “helps; it is not a new car.”
- Fail: invented tyre-set pounds, or calling unmatched cheap tyres Strong / Modest as if they were a dated matching set.
- Pass: fresh MOT, no dangerous / major carries — “removes an immediate bill; it is not extra profit.”
- Fail: “Expect a fail.” Calling a certificate that still carries dangerous / major Modest extra profit.
- Pass: pads/discs or 12V battery with invoice — expected wear; proof helps; rarely a premium.
- Fail: “it’s the battery / the pads” as a lamp diagnosis because they asked about value.
- Pass: `repair_cost` `mot-cost` / `brake-pads-and-discs-cost` / `car-battery-replacement-cost` for the **job** headline or “we publish no figure”; gain stays Modest.
- Fail: any invented **gain** GBP; freezing a job headline in this file as always-true; calling a tyre slug that does not exist.
- Pass: invoice they gave, spoken as **spend**, then Modest. Record date, mileage, invoice on a vehicle card at obdcode.co.uk.
- Fail: wrap/fit/pass-MOT how-to; opening the dashboard picture when there is no lamp; printing the plate.
- Pass: lamp also lit → statement and outlook first, then this **[Value]**.
- Fail: value line above Stop / recovery; upgrading these four to Strong.
