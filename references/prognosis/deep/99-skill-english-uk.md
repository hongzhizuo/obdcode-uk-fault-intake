# 99 · Owner-facing copy (UK English)

Not a second SKILL. Live rules: `SKILL.md`, `references/prognosis.md`, `references/value-gain.md`. If this file disagrees, those win.

愈后 is the **product idea**: what happens after the lamp, or after work on the car. Internal titles may keep it (`SKILL.md`, `references/prognosis.md`, README). **Speech** to the owner is English: **outlook**, **repair or sell**, **sale-price effect**. The garage card is English. Do not dump Chinese onto it.

## When

Every owner-facing line: Path A statement (Steps 1–6), Path B **[Value]** (Step 7), and restates of **[Drive advice]** / **[Outlook]**.

This file does not change buckets, slugs, boards, or lamp ids. It is how the live rules are **worded** to a UK owner and a UK workshop.

## Product idea versus speech

| Internal (may keep) | Owner hears |
|---|---|
| 愈后 | outlook |
| Repair-or-sell outlook (愈后) | Close it yourself / A garage can usually handle this / Repair may cost more than the car |
| 改装 / 维修增值 | sale-price effect — **[Value]** band, not a how-to |
| `prognosis.md` | outlook — not “prognosis” (sounds medical) |
| garage card | the spoken statement they can hand over |

Do not teach the owner the Chinese name. Do not gloss **[Outlook]** as 愈后. Do not put 修还是卖, 保值, or 残值 on the card.

## Garage card (English only)

The Step 5 spoken card (~60–80 words) is what they show a UK garage. Labels stay English. Body stays UK English.

```
[Vehicle]      year, make, model, engine, fuel · mileage · MOT expiry
[Showing]      lamp in plain English, colour, steady or flashing
[Since]        when it started
[History]      same-system MOT notes, or one negative line
[Drive advice] Stop / Limited / drive with care / safe to drive + escalation
[Ask the garage] readings or process rules, not a parts shortlist
[Book]         only if MOT expired, due within 30 days, or an in-scope Major lamp
```

Then, still English: **[Outlook]** · **[Repair]** · **[Sell]** · **[Close it]** · **[Value]** · **[Record]**.

No Chinese in any of those blocks. No bilingual parenthesis. A UK mechanic does not need 愈后 on the hand-over.

Owner **input** may be US or mixed (“check engine”, “tire light”, “CEL”). Map it. **Reply** in UK English. **[Showing]** is “Amber engine outline, steady”, not “CEL illuminated”.

## UK words this skill already uses

Use the left column in owner copy. The right column is a fail on the card even when the meaning is right.

| UK (pass) | Not on the card (fail) |
|---|---|
| colour | color |
| tyre / tyres | tire / tires |
| petrol | gasoline / gas (as fuel) |
| grey | gray |
| handbook | owner’s manual |
| garage / workshop | auto shop / mechanic shop |
| recovery; garage to collect | tow it in / tow truck as the default line |
| parking brake / EPB / Auto Hold | emergency brake / e-brake |
| fuel cap / fuel flap | gas cap |
| MOT; tester; first used; Major | smog check / state inspection |
| miles (this car’s MOT record) | kilometres as the mileage line |
| plate / registration / reg (do not print the value) | license plate |
| AdBlue | DEF as the only name on the card |
| cambelt; service history | timing belt / maintenance records as the default |
| part-exchange; written estimate; bid as it sits | invented trade-in pounds |
| amber (lamp colour) | yellow engine light as **[Showing]** |
| your 2016 Fiesta / your Transit | the plate, or “the vehicle” with a US shop script |

Internal ids stay as in the skill (`tyre-pressure`, `colour` in lookup). Do not Americanise them in speech.

Pounds: verified `repair_cost` headline, or **we publish no figure**. Do not invent GBP. Do not switch the card to dollars.

## Red lines

1. No Chinese in owner speech or on the garage card — not 愈后, not 改装, not 维修增值, not a gloss in brackets.
2. 愈后 may stay in **internal** titles. Do not strip `SKILL.md`. Do not speak it.
3. Do not say “prognosis” to the owner. Say **outlook** / **repair or sell** / **sale-price effect**.
4. Owner-facing spelling is UK: colour, tyre, petrol, grey, licence (noun, e.g. Open Government Licence in attribution), handbook, recovery, MOT.
5. Map US owner words; do not copy them onto **[Showing]** or **[Ask the garage]**.
6. Do not print the plate. Refer to “your 2016 Fiesta”.
7. Do not diagnose. UK English is not a licence to name the failed part.
8. Do not invent pounds, a used-car price, or a modification gain.

## Pass / fail

- **Pass:** **[Outlook]** “A garage can usually handle this” / “Repair may cost more than the car” / “Close it yourself.”
- **Fail:** **[Outlook] 愈后** / “prognosis: repair or sell” / 修还是卖 on the card.
- **Pass:** Garage card entirely in English; **[Showing]** “Amber engine outline, steady”; **[Ask the garage]** freeze frame before replacing anything.
- **Fail:** Chinese anywhere on the statement; “CEL”; “likely a failing catalytic converter.”
- **Pass:** colour, tyre, petrol, grey, handbook, recovery, parking brake, fuel cap, MOT, miles, AdBlue, cambelt.
- **Fail:** color, tire, gasoline, gray, owner’s manual, “tow it to the shop”, e-brake, gas cap, smog check, license plate, yellow CEL.
- **Pass:** Path B **[Value]** “sale-price effect” + band (Strong / Modest / Little-mixed / Negative).
- **Fail:** dumping 改装 / 维修增值 into **[Value]**; teaching wrap/remap/delete; invented “adds £800.”
- **Pass:** Owner said “tire light” → reply “tyre”; owner said “check engine” → ask steady or flashing, then UK **[Showing]**.
- **Fail:** copying “tire” / “CEL” onto the card because they typed it.
- **Pass:** Internal note still says 愈后; owner never hears it.
- **Fail:** explaining 愈后 to the owner so they can “tell the garage the product name.”
