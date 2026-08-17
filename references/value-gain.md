# Sale-price effect of work

Some people have **no warning lamp**. They are servicing, repairing, or presenting the car. This skill then states only what that work usually does to the **next buyer’s price**.

Do not teach the modification. Do not open the dashboard picker unless a lamp is also lit.

The website can hold a **vehicle data card**. The skill does not build that card. Point them to [obdcode.co.uk](https://obdcode.co.uk) to record it. Do not print the plate.

## When this step runs

- They name a wrap, wheels, exhaust, remap, paint, PPF, stereo, racking, towbar, or “I’ve just had X done”
- They ask whether a service, cambelt, clutch, tyres, or MOT **adds value**
- They want to annotate repairs that should raise the asking price

If a lamp is also lit: fault statement + repair-or-sell **first**, then a separate **[Value]** block.

## Spoken block

```
[Value]     what buyers usually do with this kind of work (raise / little change / shrink the pool)
[Record]    put the invoice and the date on your vehicle card at obdcode.co.uk
```

No how-to. No product-install steps.

## Money rules

There is **no** modification-gain API. Do **not** invent “a wrap adds £800” or “buyers pay 40% of the invoice.”

Use the **band** below. If they already have a written invoice, you may repeat **that** figure as what they paid, then the band for what it does on sale. Paying £2,000 does not mean the sale price rises by £2,000.

Call `repair_cost` only when they are asking about a **named published job** (cambelt, clutch, MOT) and you need a planning range for the **work**, not for the gain. Gain stays a band even when the job has a headline.

## Bands (typical UK private-sale / part-exchange reaction)

These are buyer-behaviour bands, not valuations.

| Band | Meaning |
|---|---|
| **Strong** | Buyers often pay more, or discount the car less, when this is documented |
| **Modest** | Helps the sale; rarely covers the invoice |
| **Little / mixed** | Taste. Can help the right buyer and put others off |
| **Negative** | Shrinks the buyer pool or the bid. Illegal work is also a legal problem |

### Documented maintenance (usually Strong or Modest)

| Work | Band | Skill line |
|---|---|---|
| Full stamped / digital service history | Strong | Buyers pay more for a car they can trust than for a fresh wrap |
| Cambelt or wet belt done on time, invoice kept | Strong | A due belt is a heavy discount; a dated invoice usually lifts the bid |
| Timing chain with a dated invoice (if it was due) | Strong | Same idea: proof beats a promise |
| Clutch with invoice on a high-mileage car | Strong | Buyers often subtract a clutch; proof they need not |
| Matching new tyres with date | Modest | Helps; it is not a new car |
| Fresh MOT with no dangerous / major carries | Modest | Removes an immediate bill; it is not extra profit |
| Pads and discs with invoice | Modest | Expected wear. Proof helps, it rarely adds a premium |
| 12V battery with invoice | Modest | Same |

Use `repair_cost` job names `cambelt-and-water-pump-cost`, `wet-belt-replacement-cost`, `timing-chain-replacement-cost`, `clutch-replacement-cost`, `brake-pads-and-discs-cost`, `car-battery-replacement-cost`, `mot-cost` only for the **job’s** published range. Still no invented **gain** in pounds.

### Presentation and modification

| Work | Band | Skill line |
|---|---|---|
| Professional respray of damaged panels | Modest | Tidies the asking price; a cheap respray can look worse than the scuff |
| Quality PPF / ceramic on a late car | Modest / mixed | Helps a careful buyer; many will not pay it back |
| Full colour wrap | Little / mixed | A taste item. Easy to get wrong. Rarely a pound-for-pound gain |
| Aftermarket wheels / lowering | Little / mixed | Right buyer vs smaller pool and possible tyre / geometry bills |
| Legal like-for-like exhaust | Little | Quiet quality can help; a roar usually does not |
| Stereo / screens | Little | You will not get the invoice back |
| Towbar (type-approved, documented) | Modest on the right car | Towing buyers pay; others ignore it |
| Van racking / ply-lining (neat, documented) | Modest on a working van | Trades pay for a ready van; private buyers may not |
| Interior “refresh” / aftermarket seats | Little / mixed | Factory-looking tidy helps; non-standard often hurts |

### Illegal or MOT-hostile work — Negative, no how-to

Do not explain how to do these. Say the sale effect and the legal / test problem.

| Work | Band | Skill line |
|---|---|---|
| DPF / GPF / cat removal | Negative | Illegal on a used-on-road car. Buyers, testers, and insurers treat it as a defect, not an upgrade |
| Unapproved remap / emissions cheat | Negative | Shrinks the pool; can fail the test; do not instruct |
| Illegal noise / off-map exhaust | Negative | MOT and neighbours. Not a value-add |
| Over-modded show car | Negative for most buyers | A small specialist pool; part-exchange usually worse |

If they ask “will deleting the DPF raise value?”: **No.** It lowers it. Do not instruct.

## Vehicle card (site, not skill)

They can record, on the site’s vehicle card: what was done, date and mileage, invoice total they paid (their number), and the **band** from this file.

Skill does **not**: upload photos, edit HTML, or invent a resale premium.

## Red lines

1. No pound figure for **gain** unless it is their invoice, repeated as spend, not as uplift.
2. No how-to for wrap, remap, delete, weld, or lift.
3. No diagnosis of a lamp via a value band.
4. No real plate in the card speech or in git.
5. Safety / legality before any “this might look nicer to a buyer.”
