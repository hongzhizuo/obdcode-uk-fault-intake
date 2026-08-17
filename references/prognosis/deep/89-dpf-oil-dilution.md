# 89 · DPF path: oil over maximum (fuel dilution)

Deep outlook note for SKILL Step 6. **Not a second SKILL.** If this file disagrees with `SKILL.md`, `references/prognosis.md`, `references/prognosis-cards.md`, or `references/value-gain.md`, those four win. Do not diagnose. Do not invent pounds. Do not add a 14th lamp id.

Lamp **9** `dpf`, **diesel board only**. This is the **oil-over-maximum** row of that card — not the one-handbook-regen row, not petrol GPF, not a filter delete.

**Bucket:** `poor`  
**Owner hears:** Repair may cost more than the car  
**Drive advice:** Do not drive it in. Ask the garage to collect, or call recovery. **No more motorway loops.**

---

## When

Use this note when **all** of:

- The board is **diesel** (including diesel hybrid). Vans: same bucket; say **your Transit**.
- They picked **9**, or named the exhaust box with dots as the diesel particulate filter.
- They have said the **oil is over maximum**, the dipstick is **above the max mark**, or the level has **risen**.

Oil over maximum **overrides** the owner regen path. Stay on `poor` even if:

- The DPF lamp is still **steady** (not flashing)
- The car still “drives normally”
- They have not yet done a handbook regen
- They want “one more motorway run”

A risen level here means **fuel is diluting the oil**. That is the meaning of the dipstick fact. It is **not** a named failed part (not injectors, not “blocked DPF”, not soot versus ash). It needs attention **now**, not another lap.

Do **not** use this file when:

- Diesel 9, **steady**, driving normally, oil **not** over max — that is `09-dpf.md` `owner` then `garage`: **one** handbook regen
- Oil level is **unknown** — do not assume dilution. A cold dipstick glance (as the handbook shows) is information. If it is then over max, switch to this card
- Petrol / hybrid exhaust-dots or a pick of 9 on a petrol board — unmatched **GPF**. No diesel regen copy. No this file
- AdBlue / urea / DEF — not 9
- Red oil-can **lamp 1** — that is oil **pressure**, not level. Do not reuse engine-destruction / do-not-restart copy from `01-oil-pressure.md`
- Flash / limp / red warning **without** oil over max — still `poor` on `09-dpf.md`; this file’s extra fact is the dilution

If they also ask to wrap, remap, or **delete** the filter: finish **[Drive advice]** and this outlook first. A delete does not fix a lamp. Sale-price speech for a delete is `71-illegal-mods-negative.md` (**Negative**). No how-to.

---

## Owner copy

≤120 words. Spoken **[Outlook]** after the fault statement (~40–60 of these). Recovery already sits in **[Drive advice]** — no shop or scanner link above it. No ids, no fusion slugs, no URLs, no plates, no pounds unless live `repair_cost` returned a headline in this chat.

Repair may cost more than the car. Oil over maximum means fuel is diluting the oil. Stop repeating motorway runs. That is not another regen. Do not drive it in; arrange recovery. We often publish no cleaning figure, and no replacement-filter price. Get one bid as it sits and one written estimate. Recovery is part of the sell cost. Do not delete the filter.

(64 words.)

Spoken labels:

```
[Outlook]  Repair may cost more than the car
[Repair]   dpf-cleaning-cost headline, or: we publish no figure — two written estimates. No published replacement-filter price
[Sell]     one bid as it sits vs one written estimate; recovery is part of the sell cost
```

Omit **[Close it]**. This branch is never Close it yourself.

If they ask keep-driving, another regen, recovery, or repair-versus-sell: **restate [Drive advice] and [Outlook]**. If they ask what part it is: this skill does not diagnose. Do not say “continue as a normal assistant.”

---

## Slugs

Call **only** `dpf-cleaning-cost`. Still call it when you expect `gbp: null`. Null / `no_verified_price` / `no_published_job` **is** the answer: we publish no figure; two written estimates; do not fill the gap.

- If `status: ok` and a headline exists, say that headline as a planning range, not a quote for this car.
- There is **no** published DPF-replace slug. Do not invent a filter price.
- Do **not** call `car-diagnostic-test-cost` on this diesel DPF path (that slug is for engine-steady / GPF).
- Do not call cat, clutch, belt, battery, head-gasket, or oil-related jobs because the level rose.
- Never pick a slug because it is the only one with a number.
- A cost page is not a diagnosis. Do not say the filter “needs a clean” because the cleaning slug exists.

**Ask the garage** (statement, not outlook): soot load and differential pressure readings, not a code alone, and **not** a soot-versus-ash fork. Tell them the oil was over maximum. Do not name the failed part.

---

## Sell

Always on this card (weak outlook). There is no sell-price tool.

1. Repair: verified cleaning headline, or “we publish no figure.” No invented replacement-filter pounds.
2. Sell: we publish no used-car price. Get **one** instant-sale or dealer bid **as the car sits** — usually not a runner; for parts if it must not be driven.
3. Get **one** written garage estimate.
4. If the estimate is larger than the bid, selling is often the better outlook.
5. **Recovery / collection is part of the sell cost** because they must not drive it in. Do not invent that fee.
6. A missing or failed factory DPF is a test and value problem. That sentence is **not** permission to delete it.

Do not say the car is a write-off. Do not invent Parkers, WeBuyAnyCar, or trade-in pounds. Refer to “your 2016 Fiesta” or **your Transit**, never a plate.

---

## DIY

**No.** Outlook is `poor`. Oil over maximum is not a driveway regen, not a scan-tool regen, and not an oil-change tutorial.

- **Stop repeating motorway runs.** Not another handbook regen. Not “one more lap to burn it off.”
- Never scan-tool **forced** regen (menus, parked idle burns, “service regen”). Do not describe those steps for the owner or as “tell the garage to run one.”
- Never regenerate in an enclosed garage or workshop (carbon monoxide, `W-CO`).
- Never clear the lamp as a fix.
- Never “just cut it out,” blank it, weld it, or remap it away. No delete how-to.
- A small OBD reader does **not** close this. Do not treat freeze-frame steps as a repair.
- A dipstick reading that showed **over max** is how this branch was classified. It is **information**, not a close. Do not drain, flush, or “change the oil and carry on” as published owner work. Do not top up — the problem is **too much**, with fuel in it.
- Do not mix this with lamp 1: a correct or high **level** does not make an oil-**pressure** lamp safe, and a pressure lamp is not this card.

Owner facts (oil over max, how long the DPF lamp was on, any limp) go in **[Since]** or **[Ask the garage]**, not as a parts shortlist.

---

## Red lines

1. **Not another regen.** Oil over max ends the owner regen path, including a first handbook attempt they have not done yet.
2. **Not delete.** Not as a cheap DPF repair, not as a value add, no how-to. If they ask sale effect, **[Value] Negative** after this outlook — `references/value-gain.md` / `71-illegal-mods-negative.md`.
3. Fuel dilution is the **dipstick meaning**, not a diagnosis of injectors, seals, or a blocked filter.
4. No soot-loaded versus ash-loaded. No “the DPF is blocked.” No named sensor.
5. Not GPF. Not AdBlue. Not lamp 1.
6. No invented GBP for cleaning, a new filter, sell, or recovery.
7. No SAE J2012 wording. A code the garage later reads is a fact; the standard’s definition is not.
8. Never clear the lamp. Never forced regen. Never enclosed-space regen.
9. Safety before commerce: recovery **above** any tool, shop, or cost line.
10. No real registration in this file or in speech. Illustrative plate only: `AB12CDE`.
11. **MOT:** a missing factory DPF can be a Major where one was fitted. Do not say “Expect a fail” from this lamp, or from oil over max, alone. Gate on first-use and fuel; link the [DVSA inspection manual](https://www.gov.uk/guidance/mot-inspection-manual-for-private-passenger-and-light-commercial-vehicles).
12. A cost slug is not a diagnosis.
13. Same-system MOT notes (`diesel particulate filter`) are prior notes only. End: **this does not show the cause of today’s lamp.**

---

## Pass / fail

**Pass**

- Diesel 9 **and** oil over maximum → bucket **`poor`**, even if the lamp is still steady and the car still moves.
- “Oil over maximum means fuel is diluting the oil.” Attention now — not another motorway run.
- “Stop repeating motorway runs.” “That is not another regen.”
- Do not drive it in; ask the garage to collect, or call recovery.
- Call `dpf-cleaning-cost`; speak the headline or “we publish no figure — two written estimates.”
- “There is no published replacement-filter price.”
- Weak outlook: one bid as it sits versus one written estimate. Recovery is part of the sell cost.
- Dipstick over max is information, not a close. No **[Close it]** block.
- “Do not delete the filter.” If they ask value: Negative; no how-to.
- Ask the garage for soot load and differential pressure, and that the oil was over maximum — not a parts guess.
- Restate **[Drive advice]** and **[Outlook]** if they ask keep-driving, another regen, recovery, or repair-versus-sell.
- “This skill does not diagnose” if they ask which part.
- Petrol exhaust-dots sent to GPF, not this copy. Red oil-can sent to lamp 1, not this copy.

**Fail**

- “Do one more motorway run.” / “Finish the regen anyway.” / handbook regen on oil over max.
- Scan-tool forced regen, parked service regen, or “use the reader to burn it.”
- “Just cut it out” / delete / remap / weld as a cheap fix, or any how-to.
- “It’s soot-loaded / ash-loaded / a blocked DPF / leaking injectors.”
- Close it yourself: drain the oil, change it and carry on, clear the lamp, or a reader “fix.”
- “Drive it slowly to the garage” / keep extra journeys / enclosed-space regen.
- Invented GBP: cleaning range, new-filter price, trade-in, recovery fee, “it’s a write-off.”
- Calling `car-diagnostic-test-cost`, cat, clutch, or any slug off this allowlist because the DPF lamp is on.
- Treating the cleaning cost page as today’s failed part.
- “Expect a fail.”
- Mixing this with lamp 1 do-not-restart / bearing-destruction copy, or mapping AdBlue to 9.
- Regen copy on petrol / hybrid GPF.
- A real registration in this file or in speech.
- Shop or scanner links above the recovery line.
