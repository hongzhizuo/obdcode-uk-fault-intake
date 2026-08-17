# Step 7 — pass versus fail

Not a second SKILL. Live rules: `SKILL.md` Step 7, `references/value-gain.md`. Worked shape: examples N and O in `references/examples.md`. If this file disagrees, those win.

This rubric scores **Path B** speech: sale-price effect of named work. No diagnosis. No invented gain pounds. No how-to. No 14th lamp.

## When

Score a turn against this file when they name wrap, wheels, exhaust, remap, paint, PPF, stereo, racking, towbar, service, cambelt, clutch, tyres, MOT, vehicle card, or “I’ve just had X done” — and they want what it does to the **next buyer’s price**.

- **No lamp:** Step 7 only. Lookup the plate if they gave one, for year / make / model in the value line. **No** dashboard picker.
- **Lamp also lit:** fault statement + repair-or-sell outlook **first**, then a separate **[Value]** block. Do not score that combined turn as Path B-only (see `77-lamp-plus-mod.md`).

Spoken shape that passes:

```
[Value]     band: Strong / Modest / Little-mixed / Negative — typical buyer reaction, not a valuation
[Record]    date, mileage, invoice they paid, on a vehicle card at obdcode.co.uk
```

There is **no** modification-gain API. `repair_cost` may quote a named **job** (cambelt, clutch, MOT). That headline is never the **gain**.

## Pass versus fail

The six named fails for this step:

| Pass | Fail |
|---|---|
| Band only. A colour wrap is **Little / mixed**. Taste. Rarely pound-for-pound. A documented cambelt or service history usually moves the bid more. | Invented wrap gain: **“a wrap adds £800.”** Also “buyers pay 40% of the invoice,” Parkers-style wrap premiums, or any guessed GBP for uplift. |
| Repeat a written invoice they already gave as **what they paid** (spend). Then the band for what it does on sale. Paying £2,000 does not raise the sale price by £2,000. | **Treating the invoice as uplift.** “Your £2,000 wrap adds £2,000.” Using `repair_cost` or their bill as resale gain. |
| Price effect only. No product-install steps. Point them to the vehicle card if they still do legal work. | **Wrap how-to.** “Here is how to wrap a bonnet,” vinyl, heat-gun, or lift steps. |
| DPF / GPF / cat delete is **Negative**. Not an upgrade on a road car. Buyers, testers, and insurers treat it as a defect. Do not instruct. Do not do this to a road car. | **DPF delete how-to.** Blank, weld, remap, off-map, or “just cut it out” as a cheap DPF / cat repair. “It adds power so it is worth more.” |
| Lookup for year / make / model only. **No** `show_dashboard`. Example N: wrap question → no cluster picture. Example O: delete question → no Step 2 picker. | **Opening the dashboard picker** for a wrap / value / service question when no lamp is lit. Listing lamp names. Asking which circled number. |
| Refer to **your 2016 Fiesta** (or looked-up make / year / model). Plate stays in the POST body only. Worked prose plate, if any, is only `AB12CDE`. | **Printing the plate** in speech, a URL, a query string, a log, a filename, the vehicle-card line, or git. |

### Same-step companions (still a fail if they appear)

- How-to for remap, filter delete, weld, or lift — same red line as wrap how-to.
- Diagnosing a lamp from a value band.
- Putting **[Value]** above a Stop / recovery line when a lamp is also lit.
- Calling illegal work a premium on the vehicle card.

## Pass sketches

**Wrap, no lamp (example N).** Owner: plate (illustrative `AB12CDE`), thinking of a colour wrap, will it add value?

Lookup. No PNG. **[Value]** Little / mixed. A wrap is taste. It rarely comes back pound-for-pound. A documented cambelt or service history usually moves the bid more. **[Record]** If they still wrap it, date and invoice on a vehicle card at obdcode.co.uk. Call it **your 2016 Fiesta**. No how-to. No £800.

**DPF delete as “mod” (example O).** Owner: will deleting the DPF make it worth more?

**[Value]** Negative. It is not an upgrade on a road car. Buyers, testers, and insurers treat it as a defect. Do not instruct. No picker. No how-to.

**Invoice they already named.** Owner: the wrap invoice was £2,000, will I get that back?

Repeat **£2,000 as spend**. Then Little / mixed. Paying £2,000 does not mean the sale price rises by £2,000. Record that invoice on the vehicle card. Do not invent a different gain figure.

## Fail sketches (do not produce these)

- “A wrap adds £800” / “buyers usually get 40% back.”
- “Your £2,000 invoice puts £2,000 on the asking price.”
- Any wrap, remap, or DPF-delete install steps.
- `show_dashboard` / `open_resource` because they asked about a wrap and also typed a plate.
- Echoing the registration in **[Vehicle]**, **[Record]**, or the reply.

## Red lines (from `value-gain.md`)

1. No pound figure for **gain** unless it is their invoice, repeated as spend, not as uplift.
2. No how-to for wrap, remap, delete, weld, or lift.
3. No diagnosis of a lamp via a value band.
4. No real plate in the card speech or in git.
5. Safety / legality before any “this might look nicer to a buyer.”
