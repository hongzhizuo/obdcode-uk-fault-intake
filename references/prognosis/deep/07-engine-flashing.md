# 7 `engine-flashing`

Deep outlook note for SKILL Step 6. Not a second skill. If this file disagrees, `SKILL.md`, `references/prognosis.md`, and `references/prognosis-cards.md` win.

**id:** `engine-flashing` · **bucket:** `poor` · **drive advice:** Stop · **close-it-yourself:** no

The spoken picture is the same engine-outline cell as 6. Flashing is spoken as 7; there is no second drawing.

---

## When

Use this card when the engine-family lamp is **flashing while running**. Typical routes:

- They said engine / EML / MIL / check-engine **and flashing**
- They picked circled **6**, then said it is flashing
- They named a flashing engine outline with judder, shake, or a rough run (those owner facts go in **[Since]**, not as a named part)

Do **not** use this card for:

- Key-on **bulb-check** flashes that go out — not a fault; skip Step 6
- A **steady** amber engine outline — that is `engine-steady` (6), `device` then `garage`
- A flashing **coil** on diesel — that is `glow-plug` (13), not 7
- Electric boards — the engine cell is not shown; do not force id 7

Bucket stays **`poor`**. A reader on the shelf does not upgrade this to Close it yourself. A published diagnostic figure does not upgrade it to “a garage can usually handle this.”

Run Step 6 in the **same turn** as the Stop statement. Do not ask if they are driving.

---

## Owner copy

≤120 words. After the fault statement. Restate Stop; do not put shop links above it.

The engine outline is flashing. Stop. Do not drive it in. Ask the garage to collect, or call recovery. This is not a driveway job, and a reader does not fix it. Repair may cost more than the car. We publish a diagnostic-test figure when the tool returns one. If a garage later invoices a converter, that job’s published range is an upper bound — not a diagnosis that the converter has failed. Get one bid as the car sits (it is not a runner) and one written estimate. Recovery is part of the sell cost. Compare them before you authorise work. The lamp does not name a part or a cylinder.

---

## Slugs

Call `repair_cost` only with slugs on this lamp’s allowlist. Never invent pounds. Never treat a cost page as the failed part.

| Slug | Call | How to speak it |
|---|---|---|
| `car-diagnostic-test-cost` | Always | First garage invoice class: a scan. Say the headline if verified. If `gbp: null`, say we publish no figure — two written estimates. |
| `catalytic-converter-replacement-cost` | Optional add | **Only** as “if the garage later invoices a converter.” Weak-outlook **upper bound**, not today’s diagnosis. Never “you have a failed cat.” |

Do **not** call clutch, cambelt, chain, wet-belt, DPF, battery, or pads slugs because this lamp is on.

Aftertreatment damage is why the outlook is weak. That sentence is not a named part.

---

## Sell

Always on this card (weak outlook). There is no sell-price tool.

1. Repair: verified diagnostic (and converter **if later invoiced**) or “we publish no figure.”
2. Sell: get **one** instant-sale or dealer bid **as the car sits** — usually not a runner; for parts if it must not be driven.
3. Get **one** written garage estimate.
4. If the estimate is larger than the bid, selling is often the better outlook.
5. **Recovery / collection is part of the sell cost** because **[Drive advice]** is Stop. Do not invent that fee.

Do not say the car is a write-off. Do not invent Parkers, WeBuyAnyCar, or trade-in pounds. Refer to the vehicle as “your 2016 Fiesta” (or make/model from lookup), never a plate.

---

## DIY

**No.** Red-class. Close-it-yourself never covers a flashing engine lamp.

- Do not keep driving “to see,” to reach the garage, or to “clear it.”
- Do not give coil, plug, injector, or converter steps.
- Do not run the engine-steady fuel-cap close on a flashing lamp.
- A small OBD reader does **not** close this. Do not clear codes. Do not describe freeze-frame steps as a repair.
- Scanner shop links, if mentioned at all, stay **below** Stop / recovery — and they are not a close on this id.

---

## Red lines

1. No SAE J2012 wording. A code number the garage later reads is a fact; the standard’s definition is not.
2. No diagnosis: not misfire, not cylinder *n*, not “failed cat,” not coil pack.
3. No invented GBP for repair, recovery, or sell.
4. Converter slug only as “if later invoiced,” never as the cause of today’s lamp.
5. No DIY. No “continue as a normal assistant.”
6. Never print, file, or speak a real registration. Illustrative plate in other files is `AB12CDE` only.
7. Never advise clearing the lamp as a fix.
8. Safety before commercial: Stop / recovery above any tool or cost line.
9. MOT: same first-use gate as the steady engine lamp. Do not say “expect a fail.”
10. Do not confuse with diesel glow (13) or a key-on bulb check.

---

## Pass / fail

**Pass**

- Stop. Do not drive it in; ask the garage to collect, or call recovery.
- “Repair may cost more than the car.” Bid as it sits vs written estimate. Recovery is part of the sell cost.
- “A scan is the next step; the lamp does not name the part.” Call `car-diagnostic-test-cost`.
- “If the garage later invoices a converter, published UK figures are …” — only then call `catalytic-converter-replacement-cost`.
- “The lamp does not say which cylinder.”
- Restate **[Drive advice]** and **[Outlook]** if they ask recovery, keep-driving, or repair-vs-sell.
- Quote `gbp: null` as no published figure.

**Fail**

- “You have a failed cat.” / “Likely a failing catalytic converter.”
- “It’s a misfire on cylinder 3.” / “Fit coils and it will stop flashing.”
- Keep driving / “pop to the garage” / “see if it settles.”
- Close it yourself with a reader, a fuel cap, or a code clear.
- Calling clutch or cat cost because an engine lamp is on, as if that were the diagnosis.
- “About £400–£800” with no `repair_cost` result; invented trade-in pounds; “it’s a write-off.”
- Shop or scanner links above the Stop line.
- Treating a flashing diesel coil as this id, or a bulb-check flash as a fault.
