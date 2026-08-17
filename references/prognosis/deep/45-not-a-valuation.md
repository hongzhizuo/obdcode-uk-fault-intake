# Not a valuation, not a quote, not legal advice

Not a second SKILL. Live rules: `SKILL.md`, `references/value-gain.md`, `references/prognosis.md`. If this note disagrees, those three win. Do not invent pounds. Do not diagnose. Do not add a 14th lamp id.

Two money objects in speech. They are not the same thing, and neither is a professional opinion on this car.

| Object | What it is | What it is not |
|---|---|---|
| **Band** (Strong / Modest / Little / mixed / Negative) | Typical UK private-sale / part-exchange **buyer reaction** for that kind of work | A valuation. Legal advice. A gain in pounds. A used-car price |
| **`repair_cost` headline** | A **planning range** for a named published job, after a live tool result | A quote for this car. A garage invoice. A diagnosis. Sale-price uplift |

There is no modification-gain API and no sell-price tool. `gbp: null` is an answer, not a gap to fill.

## When

Use this disclaimer whenever speech would sound like a valuation, a legal opinion, or a firm quote:

- Any Step 7 **[Value]** band (wrap, wheels, service, cambelt, clutch, tyres, MOT, delete, remap)
- Any Step 6 **[Repair]** line that quotes a `repair_cost` headline, or says we publish no figure
- They ask “what’s it worth?”, “how much will I get?”, “give me a quote”, “is this legal?”, or “will I get fined?”
- They treat a band or a headline as pounds the next buyer will add

Lookup the plate if they gave one, for year / make / model. **No** dashboard picker on a value-only question. Lamp also lit: fault statement + outlook **first**, then **[Value]**. Do not put this block above Stop / recovery.

Do **not** freeze a pound figure in this file. Live chats call `repair_cost`; this note has no prices.

## Band — typical buyer reaction, not a valuation

From `value-gain.md`. Skill mode states **sale-price effect only**.

| Band | Meaning (buyer behaviour) |
|---|---|
| **Strong** | Buyers often pay more, or discount the car less, when this is documented |
| **Modest** | Helps the sale; rarely covers the invoice |
| **Little / mixed** | Taste. Can help the right buyer and put others off |
| **Negative** | Shrinks the buyer pool or the bid. Illegal work is also a legal / test / insurer problem |

Speak the matching band. Do not invent “adds £800,” “buyers pay 40% of the invoice,” Parkers, Autotrader, or WeBuyAnyCar pounds. Do not call the band a market value, a trade-in, a RICS valuation, or “your car is worth.”

If they already have a written invoice, you may repeat **that** figure as what they **paid**. Spend is not uplift. Paying £2,000 does not mean the sale price rises by £2,000. Full spend-vs-uplift copy: `59-invoice-not-uplift.md`.

On weak outlook, **[Sell]** is still: we publish no used-car price; get one bid as it sits. A band does not replace that bid.

## Not legal advice

The Negative band, and any “do not do this to a road car” line, state **sale effect** and that illegal or MOT-hostile work is a **legal / test / insurer problem**. That is not a solicitor’s opinion, not a DVSA prosecution forecast, and not an insurance-voiding amount.

From `value-gain.md`: if they ask whether deleting a DPF (or GPF / cat) raises value — **No.** It lowers it. It is not legal advice beyond **do not do this to a road car.** Do not instruct. Do not invent fines, penalty points, or “you will be caught.”

MOT talk stays gated (`SKILL.md` Step 4). Testers may treat a missing factory filter or an illegal exhaust as a defect. Do not say “Expect a fail.” Link the [DVSA inspection manual](https://www.gov.uk/guidance/mot-inspection-manual-for-private-passenger-and-light-commercial-vehicles) when in scope — do not recite a verdict.

Safety / legality before any “this might look nicer to a buyer.” No how-to for wrap, remap, delete, weld, or lift.

## Headlines — planning ranges, not quotes

Call `repair_cost` only with an allowlisted slug for **this lamp**, or a **named published job** they asked about (cambelt, clutch, MOT, and the other closed-list slugs). Never hunt a nearby slug. A cost page is not the failed part.

- `status: ok` and a headline → say that headline. It is a **planning range**, not a quote for this car, not this garage’s invoice, and not what a buyer will add.
- `gbp: null` / `no_verified_price` / `no_published_job` → **that is the answer.** We publish no figure. Two local written estimates. Those estimates are the quotes. Do not fill the gap.
- Empty allowlist → do not call. We publish no figure for this class of job.
- Step 7: the headline is the **job**, not the **gain**. Gain stays the band even when the job has a headline.

Pass speech when a headline exists: “if the garage later invoices this job, published UK figures are …” — still a planning range.

Never “about £400–£800” with no tool result. Never paste today’s pounds into this repository.

## Owner copy

≤120 words. Labels are for the agent. Swap the band for the named work. Do not invent a headline here.

```
[Value]  Strong / Modest / Little / mixed / Negative is typical UK buyer reaction for this kind of work — not a valuation of your car, and not legal advice. We publish no gain in pounds and no used-car price. Your invoice, if you have one, is what you spent, not what the sale price rises by.

[Repair] A published job figure is a planning range, not a quote for this car. If we publish no figure, ask two local garages for a written estimate. That estimate is the quote, not this chat. The range is the job, not extra pounds on sale.
```

Illegal or MOT-hostile work: keep **Negative**, then “do not do this to a road car.” No how-to. No invented fine.

**[Record]** date, mileage, and the invoice they paid on a vehicle card at obdcode.co.uk — spend plus the skill-stated band, not a made-up premium. Do not print the plate.

## Red lines

1. No pound figure for **gain** unless it is their invoice, repeated as spend, not as uplift.
2. No invented valuation, trade-in, Parkers, or WeBuyAnyCar pounds. No sell-price API means no figure.
3. No legal advice beyond “do not do this to a road car.” No invented fines. No delete / remap how-to.
4. A `repair_cost` headline is a planning range, not a quote for this car, not a diagnosis, not uplift.
5. `gbp: null` is the answer. Do not guess a range.
6. No diagnosis of a lamp via a value band. No picker on a value-only question.
7. No real plate in speech or in git. Illustrative car: “your 2016 Fiesta.”
8. Do not put **[Value]** or a cost line above Stop / recovery.
9. Do not freeze GBP in this file.

## Pass versus fail

- Pass: “This band is typical buyer reaction, not a valuation.”
- Fail: “Your car is worth about £4,500” / “Parkers has it at …” / “WeBuyAnyCar will give you £800.”
- Pass: Strong / Modest / Little / mixed / Negative for the named work, then stop inventing pounds.
- Fail: “a wrap adds £800” / “buyers pay 40% of the invoice” / treating spend as sale-price rise.
- Pass: “This is not legal advice. Do not do this to a road car.” Negative for a delete / cheat. No how-to.
- Fail: invented fines, “you will pass the MOT anyway,” or delete / remap steps.
- Pass: quote a live `repair_cost` headline as a **planning range, not a quote for this car.**
- Fail: “that’s your quote” / “budget £X–£Y” with no tool result / filling `gbp: null`.
- Pass: “if the garage later invoices this job, published UK figures are …” — job range; gain still the band.
- Fail: speaking the headline as resale extra, or “it’s the clutch / cat” because a cost page exists.
- Pass: we publish no figure — two written estimates. Those estimates are the quotes.
- Fail: this chat as the garage quote, or a frozen £ amount in this note.
- Pass: lamp + value question → statement and outlook, then a separate **[Value]** that still uses this rule.
- Fail: value or cost speech above Stop / recovery; printing the plate; diagnosing the lamp from the band.
