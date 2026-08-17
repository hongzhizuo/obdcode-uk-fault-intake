# Website vehicle card vs skill

Not a second SKILL. Live rules: `SKILL.md` Step 7 and `references/value-gain.md`. If this file disagrees, those win.

The **site** can hold a vehicle data card (work done, invoices, presentation). The **skill** does not build that card. In skill mode, state the **sale-price band** and tell them what to record. Point them to [obdcode.co.uk](https://obdcode.co.uk). Do not print the plate.

## When

- They name wrap, wheels, exhaust, remap, paint, PPF, stereo, racking, towbar, service, cambelt, clutch, tyres, MOT, or “I’ve just had X done,” and they ask what it does to sale price.
- They ask to annotate repairs or presentation that should raise the asking price.
- They ask what a vehicle card is, or how to put work on the site.

If a **lamp is also lit:** fault statement + repair-or-sell outlook **first** (safety). Then a **separate** `[Value]` / `[Record]` block. A wrap does not fix a lamp. Do not open the dashboard picker for Path B alone.

## Owner copy

Use the band that `value-gain.md` gives for the named work. Example (Modest). Do not invent pounds of gain.

```
[Value] Buyers usually treat this kind of work as Modest. That is typical UK private-sale reaction, not a valuation. If you already have a written invoice, that figure is what you paid — not what the sale price will rise by.

[Record] Record the date, the mileage, and that invoice on your vehicle card at obdcode.co.uk. This chat states the band only. It does not upload photos, edit the card, or invent a resale premium.
```

Swap Modest for Strong / Little-mixed / Negative when the named work matches that table. Illegal or MOT-hostile work stays Negative; do not instruct.

If they also have a lamp, speak this block **after** `[Outlook]`. Do not merge value into drive advice.

If the card UI is not in front of them, the spoken `[Value]` plus “record it on your vehicle card” is enough.

## Fields to record

Tell them they can put these on the **site** card. The skill states them; it does not fill the form.

| Field | Whose number | Notes |
|---|---|---|
| What was done | Owner | Service, repair, presentation, or **legal** modification. Plain English. |
| Date | Owner | When the work was done. |
| Mileage | Owner | Mileage at that date. |
| Invoice they paid | Owner | Their figure as **spend**, not as uplift. |
| Band | Skill | Strong / Modest / Little-mixed / Negative from `value-gain.md`. Buyer reaction, not a valuation. |

Do **not** tell the skill to: upload photos, edit HTML, attach files, or invent a resale premium.

Refer to the car as “your 2016 Fiesta” (or make/year/model from lookup). The plate is personal data — never print it in card speech, a URL, a filename, a log, or git.

`repair_cost` may quote a **named published job** (cambelt, clutch, MOT). That headline is the **job**, not the **gain**. Gain stays a band.

## Red lines

1. No pound figure for **gain** unless it is their invoice, repeated as spend, not as uplift. There is no modification-gain API.
2. No how-to for wrap, remap, filter delete, weld, or lift. Skill mode is price effect only.
3. No diagnosis of a lamp via a value band.
4. No real plate in the card speech or in git. Do not echo it after lookup.
5. Safety / legality before any “this might look nicer to a buyer.” Lamp path: statement and outlook first, then Value.
6. Skill does not upload photos, edit the card, or invent a premium. Point to the site.
7. Illegal work (DPF/GPF/cat delete, unapproved remap, emissions cheat) is Negative. Do not instruct. Do not present it as an upgrade to record.

## Pass / fail

- **Pass:** `[Value]` names a band from `value-gain.md`; `[Record]` says date, mileage, invoice on a vehicle card at obdcode.co.uk.
- **Fail:** “a wrap adds £800” / “buyers pay 40% of the invoice” with no invoice from them, or treating spend as uplift.
- **Pass:** repeat their written invoice as what they paid, then the band.
- **Fail:** skill uploads photos, edits HTML, or pretends it built the card.
- **Pass:** “your 2016 Fiesta” (or equivalent). Plate used only in the lookup body.
- **Fail:** printing the plate on the card speech, in a URL, a filename, or git.
- **Pass:** lamp also lit → statement + outlook, then a separate Value block.
- **Fail:** wrap/value speech before Stop / recovery / outlook; or “the wrap will sort the lamp.”
- **Pass:** spoken Value + record line when the card UI is not on screen.
- **Fail:** how-to for wrap, remap, or delete; or calling illegal work a value-add.
- **Pass:** `repair_cost` headline for a named job, gain still a band.
- **Fail:** using a cost slug as a diagnosis or as invented resale premium.
