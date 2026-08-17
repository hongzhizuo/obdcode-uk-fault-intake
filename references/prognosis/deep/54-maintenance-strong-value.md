# Documented maintenance — Strong sale-price band

Not a second SKILL. Live rules: `references/value-gain.md`, `references/prognosis.md`, `SKILL.md` Step 7. Path B: sale-price effect only. No how-to. No dashboard picker unless a lamp is also lit.

## When

- They ask whether a **service history**, **cambelt**, **wet belt**, **timing chain**, or **clutch** adds value, or they have just had that work done and want the sale effect.
- No lamp → Step 7 only. Lookup the plate if they gave one, for year/make/model in the value line. Still no picker.
- Lamp also lit → fault statement + repair-or-sell outlook **first**, then a separate **[Value]** block. A belt or clutch invoice does not close a lamp.
- **Clutch is Strong on a high-mileage car** with a dated invoice. Do not stretch that band to a low-mileage clutch as extra profit.
- Belt or chain is Strong when it was **due and done on time**, invoice kept. Proof beats a promise that it “should be fine.”
- Not this file: matching tyres, fresh MOT, pads/discs, 12V battery (Modest); wrap/wheels (Little / mixed); deletes and cheats (Negative).

## Owner copy

Word count ≤120. Band, not a valuation. Repeat **their** invoice as spend if they already named it. Never invent uplift pounds.

```
[Value]  Strong. Buyers often pay more, or discount the car less, when the stamped or digital service history is complete, and when a dated invoice shows the cambelt, wet belt, or timing chain was done on time, or a clutch on a high-mileage car. A due belt is a heavy discount; proof usually lifts the bid. Buyers often subtract a clutch; proof they need not. The bill you paid is spend, not a published uplift. If you are planning the work, a published job range is the job, not the gain. We do not invent extra pounds.

[Record] Put the date, mileage, and that invoice on a vehicle card at obdcode.co.uk.
```

If they named a figure they paid, you may repeat that number once as **what they spent**, then the Strong band. Paying £2,000 does not mean the sale price rises by £2,000.

## Slugs allowed for the job

Call `repair_cost` only when they asked about a **named published job** and you need a planning range for the **work**. Gain stays the Strong band even when the job has a headline. `gbp: null` / `no_verified_price` / `no_published_job` → we publish no figure for that job; still no invented gain. Never treat a cost page as a diagnosis. Never pick a slug because an engine lamp is on.

| Slug | When to call |
|---|---|
| `cambelt-and-water-pump-cost` | They named a cambelt / timing-belt job |
| `wet-belt-replacement-cost` | They named a wet belt |
| `timing-chain-replacement-cost` | They named a timing chain (if it was due) |
| `clutch-replacement-cost` | They named a clutch, or high-mileage clutch value — **not** an engine lamp |

No slug for “service history.” Do not hunt `mot-cost` or `brake-pads-and-discs-cost` to fill a gap. Do not call `clutch-replacement-cost` or a belt slug as the cause of a lamp.

## Band

**Strong** — buyers often pay more, or discount the car less, when this is documented.

| Work | Band | Skill line |
|---|---|---|
| Full stamped / digital service history | Strong | Buyers pay more for a car they can trust than for a fresh wrap |
| Cambelt or wet belt done on time, invoice kept | Strong | A due belt is a heavy discount; a dated invoice usually lifts the bid |
| Timing chain with a dated invoice (if it was due) | Strong | Same idea: proof beats a promise |
| Clutch with invoice on a high-mileage car | Strong | Buyers often subtract a clutch; proof they need not |

## Pass versus fail

- Pass: **[Value] Strong** plus typical buyer reaction; **[Record]** date, mileage, invoice on a vehicle card. Do not print the plate.
- Fail: “this adds £800” / “buyers pay 40% of the invoice” / “your £2,000 job puts £2,000 on the asking price.”
- Pass: quote a `repair_cost` headline (or “we publish no figure”) as the **job**, then still Strong for the **gain**.
- Fail: using a job headline as the resale uplift, or filling `gbp: null` with a guessed gain.
- Pass: “if the garage later invoices this job, published UK figures are …”
- Fail: querying clutch or cambelt cost because an engine lamp is on; “it’s the clutch / the belt.”
- Pass: Path B with no picker; lamp present → outlook first, then Value.
- Fail: wrap/remap/belt how-to; opening the cluster for a service-value question with no lamp.
