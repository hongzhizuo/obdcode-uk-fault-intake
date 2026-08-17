# 14 Unmatched petrol / hybrid GPF

Deep notes for SKILL Step 6. Not a second skill. Not a fourteenth lamp id. Live rules in `SKILL.md`, `references/prognosis.md`, `references/prognosis-cards.md`, and `references/boards.md` win. Do not diagnose. Do not invent pounds. Do not print a plate.

**Path:** unmatched petrol / hybrid GPF · **bucket:** `device` then `garage` · **drive advice:** drive with care · **slug:** `car-diagnostic-test-cost` only

Numbers stay global: **9 is always the DPF slot**. On petrol and hybrid boards that slot is an empty ghost. This path is **not** lamp id `dpf`. Do not add an id `gpf`.

---

## When

Run this after the Step 5 statement when **fuel is petrol**, or **hybrid on the hybrid board** (Hybrid Electric / no diesel cue in `fuel_raw`), **and** they:

- describe **exhaust-dots**, a **petrol particulate filter**, or “particulate filter” on this fuel, **or**
- **pick circled 9** on the petrol or hybrid picture

Keep **this** board. Say circled 9 is **not printed**. That empty slot is **not** diesel DPF. Unmatched petrol particulate-filter lamp. Still a thinner statement. Do not switch board. Do not open the diesel picture. Widen to `unknown` only if they say **none of these shapes** and they have not described exhaust-dots.

Do **not** use this card for:

- Diesel board pick of 9 — that is `dpf` (diesel DPF). Handbook regen belongs there, not here
- Hybrid whose `fuel_raw` is diesel / Electric Diesel / heavy oil — diesel board; pick 9 is DPF
- Hybrid with missing `fuel_raw` — ask petrol vs diesel hybrid (or unknown board) before treating 9 as GPF
- Electric pick of 9 — empty slot on the electric picture, not GPF
- AdBlue / urea / DEF — unmatched AdBlue, not 9
- Engine outline 6 / flashing 7 — those ids, unless they separately described exhaust-dots

Vans: same buckets. Say “your Transit” when it is a van. Do not say “van board.”

Run Step 6 in the **same turn** as the statement. Do not ask if they are driving.

---

## Owner copy

≤120 words. After the fault statement. No ids, no fusion slugs, no plates, no pounds except a verified `repair_cost` headline in live chat (not in this paragraph).

Circled 9 is empty on this petrol or hybrid picture. That is not a diesel filter lamp. Exhaust-dots or a petrol particulate-filter mark: drive with care, then a scan. Do not run motorway loops or a handbook regen. If you have a small reader, plug in with the ignition as the handbook says, read stored codes and freeze frame, write them down, and do not clear the lamp. If you have no reader, a garage diagnostic is next. We publish a planning figure for that test when the cost tool returns one; otherwise we publish no figure — two written estimates. The lamp does not name the part.

(~108 words.)

Spoken labels: **[Outlook]** Close it yourself if they have a reader (or when one is listed at obdcode.co.uk). **[Close it]** the scan steps. **[Repair]** `car-diagnostic-test-cost` as the garage alternative. No **[Sell]** block on the default path.

---

## Slugs

Call `repair_cost` only with this path’s allowlist. Never invent pounds. Never treat a cost page as the failed part.

| Slug | Call? | How to speak it |
|---|---|---|
| `car-diagnostic-test-cost` | **Always** on the garage path (no reader, or the lamp stays after a read) | First invoice class: a scan. Say the headline if verified. If `gbp: null` / `no_verified_price` / `no_published_job`, that is the answer — we publish no figure; two written estimates. |
| `dpf-cleaning-cost` | **No** | Diesel DPF only |
| `catalytic-converter-replacement-cost` | **No** | Not because this lamp is on |
| Any other published job (battery, clutch, belts, pads, head gasket, MOT, wheel bearing) | **No** | Do not hunt a nearby slug because it has a number |

There is no published GPF-replace slug. Do not invent a filter price.

A cost slug is not a diagnosis.

---

## Sell

**Not first-line.** Default is device then garage. Do not push selling because the car is old.

If a **later** written garage estimate is large, switch speech to weak outlook then:

1. Repair: verified diagnostic headline, or “we publish no figure.” Still no invented GPF-replace pounds.
2. Sell: get **one** bid **as the car sits** and **one** written estimate. If the estimate is larger than the bid, selling is often the better outlook.
3. Drive advice on this path is **drive with care**, not Stop — recovery is not part of the default sell cost.

There is no sell-price tool. Do not invent Parkers, WeBuyAnyCar, or trade-in pounds. Do not say write-off. Do not suggest cutting the filter out as a cheap fix (deletion is illegal on a used-on-road car; that sale-price band lives in `value-gain.md`, not here).

---

## DIY

**Close it yourself = scan only.** Outlook is good. A small reader changes the next step. Sequence (same as engine-steady device, without the fuel-cap extra):

1. Plug in with the ignition in the handbook position, engine off unless the reader says otherwise
2. Read **stored codes and freeze frame**
3. Write them down for the garage
4. Do **not** clear the lamp

If they already own a reader, use that. How-to-choose links sit **below** **[Drive advice]**:

- https://obdcode.co.uk/guides/best-obd2-scanner-uk/
- https://obdcode.co.uk/tools/scanners/

Category may be off the shelf. Do not invent an in-stock SKU.

**No diesel regen copy.** No motorway loops. No handbook regen. No enclosed-space regen. No scan-tool forced regen. Fuel cap clicked tight is **engine-steady only** — it does not close this path.

No reader, or the lamp stays after a read: garage. Call `car-diagnostic-test-cost`.

---

## Red lines

1. Not lamp 9 `dpf`. Not a 14th id. Do not switch board.
2. No diesel regen, soot-vs-ash, or `dpf-cleaning-cost` on petrol / petrol-hybrid.
3. No diagnosis: not “blocked GPF,” not soot-loaded, not a failed cat, not a named sensor.
4. No SAE J2012 wording. A code number they write down is a fact; the standard’s definition is not.
5. Never advise clearing the lamp as a fix.
6. Never invent GBP for a scan, a filter, or a sell bid.
7. Never print, file, or speak a real registration. “Your 2016 Fiesta” / “your Transit” only.
8. Do not instruct GPF / cat delete. Do not treat deletion as a repair.
9. Do not map AdBlue or EV turtle / charge-plug text onto this path.
10. MOT: do not say “Expect a fail.” Do not copy diesel-DPF MOT copy. Fusion slug `diesel particulate filter` is not evidence for today’s petrol lamp. Any in-family emissions / exhaust / catalyst note still ends: **this does not show the cause of today’s lamp.** Link the [DVSA inspection manual](https://www.gov.uk/guidance/mot-inspection-manual-for-private-passenger-and-light-commercial-vehicles) if scope is in play.
11. Ask the garage for a read (stored codes and freeze frame), not a parts shortlist.

---

## Pass / fail

**Pass**

- Keep the petrol or hybrid picture. “9 is not printed. Not DPF.” Unmatched petrol particulate-filter lamp. Drive with care. Scan.
- Bucket `device` then `garage`. Call only `car-diagnostic-test-cost`. Quote the headline or “we publish no figure.”
- Stored codes **and** freeze frame, written down, not cleared. Scanner links below drive advice. Off-the-shelf, no fake SKU.
- “A scan is the next step; the lamp does not name the part.”
- No regen copy. No sell block unless a later estimate is large.
- Restate **[Drive advice]** and **[Outlook]** if they ask keep-driving or repair-vs-sell.

**Fail**

- Switching to the diesel board, or running DPF regen / motorway-loop copy.
- Treating pick of 9 as lamp id `dpf`, or adding lamp id `gpf` / a 14th lamp.
- “It’s a blocked GPF.” / “Soot-loaded or ash-loaded.” / “Likely a failing catalytic converter.”
- Calling `dpf-cleaning-cost`, cat, clutch, or any non-allowlist slug because this mark is on.
- “About £400–£800 to replace the petrol filter” with no tool result, or any invented sell pounds.
- “Clear the code.” / “Force a regen with a scan tool.” / “Just cut it out.”
- Fuel-cap close copied from engine-steady as if it closed GPF.
- Mapping AdBlue, EV turtle, or a diesel-hybrid 9 onto this file.
- “Expect a fail.” / quoting a diesel DPF MOT note as the cause of today’s petrol lamp.
- Printing a real plate.
