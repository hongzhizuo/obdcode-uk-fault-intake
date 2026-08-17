# 37 · Petrol pick of 9 keeps the petrol picture

Not a second SKILL. If this note disagrees with `SKILL.md`, `references/boards.md`, `references/examples.md`, `references/prognosis.md`, or `references/prognosis-cards.md`, those win. Do not diagnose. Do not invent pounds. Do not add a 14th lamp id. Do not print a plate.

**Already showing:** petrol PNG (`assets/cluster-petrol.png`) after lookup classified petrol.  
**They type:** circled **9**, or they name exhaust-dots / “particulate filter.”  
**Keep:** this petrol picture. Do **not** switch board.  
**Empty slot:** 9 is ghosted. It is **not** diesel DPF. Never renumber.  
**Outlook:** unmatched petrol GPF — not lamp id `dpf`, not a new id `gpf`.

Worked path: Example J in `references/examples.md`. Outlook card: `references/prognosis/deep/14-gpf-unmatched.md`.

---

## When

The petrol picture is **already** open (`show_dashboard` `board=petrol`, then `open_resource`). They reply **9**, or they describe exhaust-dots / a petrol particulate filter.

Keep **this** PNG. Do not call `show_dashboard` again. Do not open diesel, hybrid, electric, or unknown to “make 9 live.”

Same keep-this-board rule on **hybrid** (ghost 9 and 13): keep `cluster-hybrid.png`. Do not swap hybrid for petrol, or petrol for diesel.

Caption fuel from the record as fact. Do **not** ask them to audit petrol vs diesel because they typed 9.

Vans: same fuel picture. Say **your Transit**. Do not say “van board.”

Do **not** use this file when:

- The board is **diesel** (including diesel hybrid / `Gas Diesel` / heavy oil in `fuel_raw`) and they pick 9 — that **is** DPF. Handbook regen lives on the diesel card.
- Hybrid + **missing** `fuel_raw` — ask petrol vs diesel hybrid (or unknown board) before treating 9 as GPF.
- The board is **electric** and they pick 9 — empty slot, **not** GPF. Keep the electric picture. Ask the circle on the shape that is lit. Unmatched EV only for turtle / car-with-! / charge plug / HV text.
- They say **AdBlue** / urea / DEF — unmatched AdBlue, not 9.
- They then name a **live** circled number (1–6, 8, 10–12) — that lamp’s card. Still keep the petrol picture.

---

## Empty slot, not DPF

Numbers are **global**. 9 is always the DPF slot, even when petrol leaves it grey. Never renumber. Never treat the empty cell as a live diesel filter.

Say: circled 9 is **not printed** on this petrol picture. Empty grey slots are not on this car. That slot is **not** DPF.

Do not run diesel DPF copy: no handbook regen, no motorway loops, no enclosed-space regen, no scan-tool forced regen, no soot-vs-ash fork, no `dpf-cleaning-cost`.

Do not force the nearest live lamp (not 6, not 8, not 10). Do not list lamp names. Do not shrink toward electric.

Widen to `unknown` **only** if they say **none of these shapes** and they have **not** described exhaust-dots / particulate filter. That is widen, not shrink. Never switch to a smaller board on owner talk.

If they typed 9 by counting cells: still say it is not printed. If they then give the circle on the shape that is lit, use that live id. If they persist with 9 or with exhaust-dots, unmatched GPF — still the petrol picture.

---

## Outlook is GPF unmatched

Petrol or hybrid + exhaust-dots / “particulate filter” / pick of 9: unmatched GPF. Thinner statement. Same turn as drive advice. Do not ask if they are driving.

| | This path |
|---|---|
| Bucket | `device` then `garage` |
| Owner hears | Close it yourself (reader) / a garage can usually handle this |
| Drive advice | Drive with care. If it starts flashing or a red warning appears, do not drive it in; arrange recovery. |
| Close it | Scan: stored codes **and** freeze frame, written down, **not** cleared. No fuel-cap close (that is engine-steady only). |
| Repair slug | `car-diagnostic-test-cost` only. Live `repair_cost` headline, or we publish no figure — two written estimates. |
| Sell | Not first-line. No deletion as a cheap fix. |

A scan is the next step. The lamp does not name the part. There is no published GPF-replace slug. Do not invent a filter price. Do not name soot, ash, or a blocked filter.

No reader: garage diagnostic. Scanner how-to-choose links sit **below** **[Drive advice]**. Category may be off the shelf. No fake SKU.

---

## Owner copy

≤120 words. After the statement. No ids, no plates, no frozen pounds.

Nine is empty on this petrol picture. That slot is not a diesel filter. An exhaust-dots or petrol particulate-filter mark is still a warning — drive with care, then a scan. Do not run motorway loops to clear it. If you have a reader, read stored codes and freeze frame, write them down, and do not clear the lamp. If you have no reader, a garage diagnostic is next. We publish a planning figure for that test when the cost tool returns one; otherwise we publish no figure. The lamp does not name the part.

Spoken labels: **[Outlook]** Close it yourself if they have a reader. **[Close it]** the scan. **[Repair]** diagnostic-test as the garage alternative. No **[Sell]** on the default path.

---

## Red lines

1. Keep the petrol picture. Do not switch to diesel, unknown, hybrid, or electric because they typed 9.
2. Empty slot is not DPF. Not lamp id `dpf`. Not a 14th id `gpf`.
3. No diesel regen copy. No `dpf-cleaning-cost`.
4. No diagnosis: not “blocked GPF,” not soot-loaded, not a failed cat.
5. Never clear the lamp. Never force a regen with a scan tool. Never “just cut it out.”
6. Never invent GBP. Never freeze a diagnostic fee in this file.
7. Never print, file, URL, or commit a real registration. “Your 2016 Fiesta” only.
8. Never shrink toward electric. Never force the nearest circled lamp.
9. Do not ask them to audit petrol vs diesel. Do not ask if they are driving.
10. Fusion slug `diesel particulate filter` is not evidence for today’s petrol lamp. Never say “Expect a fail.”

---

## Pass versus fail

**Pass**

- Petrol board already showing. They type 9. **Keep the petrol picture.** “9 is not printed. Empty slot, not DPF.” Unmatched petrol particulate-filter lamp.
- Exhaust-dots or “particulate filter” on petrol: same keep-board; unmatched GPF; no second PNG.
- Drive with care. Scan. Stored codes **and** freeze frame, not cleared. No regen copy.
- Bucket `device` then `garage`. Call only `car-diagnostic-test-cost`. Quote this turn’s headline or “we publish no figure.”
- Hybrid board + 9: keep the **hybrid** picture; same unmatched GPF outlook.
- They then name a live circle: that lamp’s card; still the petrol PNG.
- They say **none of these shapes** (and not exhaust-dots): widen to `unknown` only then.
- Diesel board + 9: DPF card, not this file.
- Electric board + 9: empty slot, not GPF; keep electric.

**Fail**

- Switching to the diesel picture so 9 becomes DPF.
- Opening unknown, hybrid, or electric because a petrol owner typed 9.
- Diesel regen / motorway-loop / soot-vs-ash / `dpf-cleaning-cost` on petrol.
- Treating pick of 9 as lamp id `dpf`, or adding id `gpf`.
- Forcing the nearest live lamp (engine 6, charging 8, TPMS 10).
- Asking them to confirm petrol vs diesel from the empty slot.
- Shrinking toward electric. Asking if they are driving.
- “It’s a blocked GPF.” / “Likely the cat.” / “About £400–£800 to replace the petrol filter.”
- “Clear the code.” / “Force a regen.” / “Just cut it out.”
- Fuel-cap close copied from engine-steady as if it closed GPF.
- Mapping AdBlue, or an electric 9, onto this petrol GPF path.
- Printing a real plate.
