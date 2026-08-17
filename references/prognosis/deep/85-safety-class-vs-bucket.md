# 85 · Safety class is not the outlook bucket

Not a second SKILL. If this note disagrees with `SKILL.md`, `references/prognosis.md`, `references/prognosis-cards.md`, or `references/warning-lights.md`, those win. Do not diagnose. Do not invent pounds. Do not add a 14th lamp id.

**Do not collapse the two systems.** `safety_class: Red` is not automatically `poor`. It is not automatically Stop.

Live lamp cards: `04-airbag-srs.md`, `08-battery-charging.md`, `01-oil-pressure.md`. This file is the split only.

---

## Two systems (plus drive advice)

| System | Values | What it answers |
|---|---|---|
| **safety_class** | `Green` · `Amber` · `Red` | May the owner repair it? Green: owner can act. Amber: owner can check; repair is professional. Red: **no owner repair at all**. |
| **Outlook bucket** | `owner` · `device` · `garage` · `poor` | What happens after the lamp commercially? Speech: Close it yourself / A garage can usually handle this / Repair may cost more than the car. |
| **drive_advice** (third axis) | `Yes` · `YesWithCare` · `Limited` · `Stop` | May they drive, and how far? Limited: drive **directly** to a garage, no extra journeys. Stop: do not drive it in; recover. |

Drive advice lives in **[Drive advice]** in the fault statement. The bucket lives in **[Outlook]**. Class is not spoken as a colour word to the owner.

Pictogram colour on the dash is **not** `safety_class`. The battery rectangle is **red on most cars** and still `Amber`. Do not promote a red symbol to Red-class, Stop, or `poor`.

---

## Proof lamps

These three are the test. Same Limited drive advice can sit on Red or Amber. Same `garage` bucket can sit on Red or Amber. Oil is the coincidence people over-generalise — not a mapping rule.

| Lamp | Id | safety_class | Drive advice | Bucket | Owner hears |
|---|---|---|---|---|---|
| Airbag / SRS | `airbag-srs` (4) | **Red** | **Limited** | **`garage`** | A garage can usually handle this |
| Battery / charging | `battery-charging` (8) | **Amber** | **Limited** | **`garage`** | A garage can usually handle this |
| Oil pressure | `oil-pressure` (1) | **Red** | **Stop** | **`poor`** | Repair may cost more than the car |

- **Airbag:** Red without Stop, Red without `poor`. They may drive it in. A workshop can usually put it right. Still no DIY (pyrotechnic / SRS).
- **Battery:** Amber without Close it yourself. Limited, garage. Switching off heaters is drive advice, not a close. Do not treat the red rectangle as oil-can urgency.
- **Oil:** Red **and** Stop **and** `poor` together. Unpressurised engine. Do not drive it in. Repair may cost more than the car. That stack is this lamp, not “because it is Red.”

Default battery stays this row. ICE **plus** heavy steering, a rising temperature gauge, or a belt noise is a **separate** Stop + `poor` branch on that card. It does **not** rewrite `safety_class` to Red. Skip that belt combo on an electric car. Age does not rewrite any of these three.

---

## The only coupling

Close-it-yourself needs **both** a good outlook (not `poor`) **and** an owner-safe or device step.

**Red-class work never becomes Close it yourself.** Oil, hot coolant, hydraulic brakes, airbags, flashing engine: no `[Close it]`. A reader does not fix them. That is class → close, not class → bucket.

Red still splits:

| Red lamp | Bucket | Drive advice |
|---|---|---|
| `airbag-srs` | `garage` (upgrade to `poor` only on a large SRS quote they already have, or they refuse a safety repair) | Limited |
| `oil-pressure` | `poor` | Stop |
| `coolant-temp` (red) | `poor` | Stop |
| `brake-system` hydraulic / pedal / leak | `poor` | Stop |
| `engine-flashing` | `poor` | Stop |
| `power-steering` | `garage` (`poor` if already heavy) | Limited, Stop if heavy |

Amber still splits: battery and ABS are `garage`; steady engine is `device` then `garage`; DPF limp is `poor`. Amber is not automatically garage, and not automatically keep-driving.

Green (TPMS simply on) can be `owner`. That is not a licence to put Red on that list.

---

## When

Use this note whenever speech or routing would treat **Red** as a single knob:

- “It’s red, so Stop / recover it” on airbag
- “It’s red, so repair may cost more than the car” on airbag
- “The battery lamp is red, so it is Red-class / Stop / `poor`” with no ICE belt combo
- “Limited, so they can fix it on the drive” on airbag or charging
- “Garage bucket, so a reader is a close” on airbag (Red) or charging (Amber)

Do not use this note to invent a fourth system. Do not use it to skip Stop on oil, red coolant, flashing engine, or hydraulic brakes. Do not use it to add a driveway close on any Red-class lamp.

Vans: same three rows. Say **your Transit**. Downtime is “a day off the road,” not a made-up day-rate.

---

## Owner copy (the split, not a diagnosis)

≤120 words in live chat, after the statement. Pick the lamp’s card for the full outlook. These lines only stop the collapse.

**Airbag:** A garage can usually handle this. Red here means no owner repair, not Stop. Drive directly to a workshop — no extra journeys. We publish no figure. Do not probe seats or wiring. Do not clear the lamp.

**Battery (no ICE Stop combo):** A garage can usually handle this. The rectangle is charging, not a battery-fit instruction. Limited: extras off, get it somewhere it can be left. Ask charging voltage (or 12V / DC-DC on EV) before they sell a battery. Do not treat the red symbol as an oil-can.

**Oil:** Repair may cost more than the car. Stop. Do not drive it in; recover it. We publish no figure for this class of work. Get one bid as it sits and one written estimate. Recovery is part of the sell cost. A cold dipstick is information, not a close. This stack is the oil-can, not “because the lamp is red.”

If they ask what is wrong: this skill does not diagnose. If they ask keep-driving or repair-vs-sell: restate **[Drive advice]** and **[Outlook]** from the live card.

---

## Red lines

1. Do not collapse `safety_class` into the outlook bucket. Red ≠ `poor`. Amber ≠ `garage`. Green ≠ Close it yourself on every lamp.
2. Do not collapse `safety_class` into drive advice. Red ≠ Stop. Airbag is Red and **Limited**.
3. Do not collapse pictogram colour into `safety_class`. Battery is often a red symbol and still Amber + Limited + `garage`.
4. Do not recover an airbag lamp by default. Do not push selling on airbag or battery garage.
5. Do not Close it yourself on airbag, charging, or oil. Heaters off and a cold dipstick are not closes.
6. Do not skip Stop on oil because “Red is not always Stop.” Oil **is** Stop.
7. Do not rewrite battery to Red-class to match the symbol, or to `poor` because the car is old.
8. Do not diagnose. Not the clock spring, not the battery, not the alternator, not the oil pump.
9. No invented pounds. Empty SRS and oil allowlists stay empty. Battery slugs only as **if invoiced**.
10. No SAE J2012 wording. No real registration. Illustrative only: `AB12CDE`, then **your 2016 Fiesta** / **your Transit**.

---

## Pass versus fail

| Pass | Fail |
|---|---|
| Name class, drive advice, and bucket as **separate** fields. | One red knob: Stop **and** `poor` **and** no-DIY because “it’s red.” |
| Airbag: **Red + Limited + `garage`**. Drive directly there. | Airbag Stop / recover. Airbag “repair may cost more than the car” as the default. |
| Battery: **Amber + Limited + `garage`**. Red symbol is not Red-class. | Battery as Red-class, Stop, or `poor` with no ICE belt combo. “Fit a battery.” |
| Oil: **Red + Stop + `poor`**. Do not drive it in. Bid as it sits. | “Red is not Stop, so creep to the garage.” Top-up and go. Oil as Close it yourself. |
| Close-it-yourself never on Red-class. Airbag stays garage, still no DIY. | Reader / scan-clear as the airbag or oil close. |
| Same Limited on airbag (Red) and battery (Amber) without copying class. | “Both Limited, so both Amber” or “both garage, so both keep-driving forever.” |
| ICE charging + belt / heavy steering / rising temp: Stop + `poor` on **that card**. Class stays Amber. Skip the combo on EV. | Using that combo to declare Red-class, or applying it on an electric car. |
| Upgrade airbag to `poor` only on a large SRS quote they already have. | Weak outlook because the car is old, or because the lamp is red. |
| Restate **[Drive advice]** and **[Outlook]** if they ask keep-driving or repair-vs-sell. | “Continue as a normal assistant.” Naming a part. Invented GBP. |

**Pass sketch** (illustrative; no live pounds): Your 2016 Fiesta. Red seated-person lamp → Limited, garage, no DIY — not Stop, not sell. Charging rectangle on while running, steering and temperature normal → Amber, Limited, garage — not an oil-can, not a battery-fit. Red oil-can → Stop, `poor`, recover — that coincidence is the oil lamp, not a rule for every red mark.
