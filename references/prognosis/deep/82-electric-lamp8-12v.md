# Electric board lamp 8 (12V rectangle)

Deep outlook note for SKILL Step 6. Not a second SKILL. If this file disagrees with `SKILL.md`, `references/prognosis.md`, `references/prognosis-cards.md`, or `references/value-gain.md`, those four win. Do not diagnose. Do not invent pounds. Do not add a 14th lamp id.

**Path:** EV 12V rectangle (circled **8** on the **electric** board)  
**Id still used:** `battery-charging`  
**Default bucket:** `garage`  
**Owner hears:** A garage can usually handle this  
**Drive advice (statement):** Limited. Drive directly there, no extra journeys. **Skip** the ICE belt / heavy-steering / rising-temp Stop combo.  
**Close-it-yourself:** No

This is not ICE charging copy (`08`). This is not unmatched EV turtle / HV (`16`). Same circled 8, different board and different allowlist.

---

## When

Run Step 6 in the **same turn** as the fault statement when **all** of these are true:

1. Lookup classified **electric** (`fuel_type` electric). `show_dashboard` used **`board=electric`**.
2. They picked circled **8**, or confirmed the **12V battery rectangle** (+ and − terminals).
3. They did **not** describe a turtle / tortoise / limited power, a car-with-! and **no** skid lines, a charge-plug lamp, or HV / high-voltage / traction-pack on-screen text.

**[Showing]** 12V charging rectangle, not the traction pack.

Skip outlook when it was only a **key-on bulb check** and then went out — not a fault.

Do **not** use this file when:

| What they showed | Path instead |
|---|---|
| Turtle / tortoise / limited power; car-with-! and no skids; charge plug; lightning-bolt pack; HV / high-voltage message; Tesla pasted alert text | **Unmatched EV.** Not 8, not 12. Do not open the ICE unknown board. Stay `garage` (or `poor` only if they already have a traction-pack quote). **No ICE slugs. No invented pack price.** |
| Petrol / diesel / hybrid / unknown board, lamp 8 | ICE (or hybrid) charging card. Alternator slug **if invoiced** may be allowed there. Belt combo may escalate ICE to Stop / `poor`. |
| Skid-lines (12) | `esc-traction`, not this rectangle |
| Owner talk that “sounds electric” on a non-electric record | Never shrink the board toward electric. Caption from the record. |

Do not upgrade this path to `poor` because the car is old, or because steering feels heavy or a temperature gauge moved — **there is no auxiliary belt combo on an electric car.** Stay `garage`. Switching heaters and screens off is **[Drive advice]**, not a repair and not a Stop trigger.

Vans: same bucket. Say **your Transit**. Downtime is “a day off the road,” not a made-up day-rate.

History (statement, not outlook): same-system MOT notes only — battery security, auxiliary drive belt. Quote date and type. No causal verbs. End: **this does not show the cause of today’s lamp.** A belt note on an EV record still does not license an ICE belt story. If nothing in-family, one negative line.

MOT: the battery lamp itself is not a specific test item. Never say “Expect a fail.” Low voltage can light other lamps; that is not today’s diagnosis.

---

## Owner copy

≤120 words. Spoken **[Outlook]** after the statement (~40–60 of these). No ids, no fusion slugs, no URLs, no plates, no frozen pounds. Limited / extras-off already sits in **[Drive advice]** — do not put a shop link above it.

A garage can usually handle this. The rectangle is the 12-volt system, not the traction pack. Drive directly there with extras off — that is to get you there, not a repair. There is no belt or alternator story on this car. If the garage later invoices a 12-volt battery, we can quote the published UK figure for that job; the lamp does not say the battery has failed. We publish no figure for other 12-volt work — two written estimates. Do not fit a battery on the driveway. Do not clear the lamp.

If they already named a large 12-volt job, still **garage** unless a **traction-pack** quote exists — that quote belongs on unmatched EV, not on this rectangle. Do not push selling on this card.

---

## Slugs

Call `repair_cost` only with this path’s allowlist. Live chats must call the tool. This file must **not** freeze a pound figure as always-true.

| Slug | Call | How to speak it |
|---|---|---|
| `car-battery-replacement-cost` | Yes, as **if invoiced** | “If the garage later invoices a 12V battery, published UK figures are …” Say the headline if `status: ok`. If `gbp: null` / `no_verified_price`, that **is** the answer: we publish no figure — two written estimates. **Not** “it is the battery.” |

Do **not** call:

- `alternator-replacement-cost` — no alternator story on the electric board
- `car-diagnostic-test-cost` — not on this allowlist (a workshop scan may still be the next step in speech; do not hunt this slug for a number)
- `cambelt-and-water-pump-cost`, `timing-chain-replacement-cost`, `wet-belt-replacement-cost` — not a lamp cause; no belt combo
- Any HV / traction-pack job — none is published; do not invent a pack price
- Clutch, cat, DPF, pads, head-gasket, or any nearby slug because it has a number

Never pick a slug because it is the only one with a number. Never treat a cost page as today’s failed part.

**[Ask the garage]** (statement, not a parts fork): 12V / DC-DC health **before** any battery is sold. That is a process rule. Do not name the DC-DC converter as the failed part.

---

## Sell

Not first-line. Bucket is `garage`. Do not push selling.

No sell-price tool. Do not invent Parkers / WeBuyAnyCar / trade-in / pack pounds.

If they later produce a **traction-pack** quote, that is unmatched EV `poor`, not this file — compare that estimate with a bid **as it sits**. Still do not invent the bid.

Limited driving: the car is still a runner unless a Stop lamp is also on. Recovery is not part of this card’s sell cost.

---

## DIY

**No.** Close-it-yourself is not allowed.

- Switching off heaters, screens, and air-con is **[Drive advice]**, not a close.
- Do not fit a 12V battery on the driveway. Do not jump-start how-to as a repair.
- Do not give belt, alternator, or water-pump steps — they do not apply.
- A reader does not close this. Do not clear the lamp. Do not describe HV isolation or pack work.
- Owner-safe notes for the garage only: extras that were on; whether the car still drives normally. Information, not a repair.

This path has no `[Close it]` block. Device and shop links, if any, stay **below** drive advice.

---

## Red lines

1. Do not diagnose. Not “it’s the 12V battery,” not “it’s the DC-DC,” not “it’s the pack.”
2. Do not tell an ICE charging story: no alternator, no auxiliary belt, no water-pump Stop combo.
3. Turtle / HV / plug / car-with-! no skids is **unmatched EV**, not 8, not 12. Do not open the ICE unknown board.
4. Do not call `alternator-replacement-cost` on this board.
5. Battery slug only as **if invoiced**, never as today’s cause.
6. No invented GBP for repair, sell, recovery, or an HV pack.
7. No SAE J2012 wording. No real registration in this file or in speech. Illustrative only: `AB12CDE`, then **your 2016 Leaf** / **your Transit**.
8. Never advise clearing the lamp. No HV DIY. No lift how-to.
9. Safety before commerce. No shop or scanner link above Limited / recovery if a Stop lamp is also on.
10. Do not say “Expect a fail.” Do not add a 14th lamp id.

---

## Pass / fail

**Pass**

- Electric board, circled 8: “12V charging rectangle, not the traction pack.”
- “A garage can usually handle this.” Limited. Belt / water-pump / heavy-steering combo does not apply.
- Call `car-battery-replacement-cost` only as “if the garage later invoices a 12V battery.” Quote the live headline, or “we publish no figure.”
- “A scan is the next step; the lamp does not name the part.” (speech — do not hunt `car-diagnostic-test-cost` on this allowlist)
- Turtle / plug / HV text: unmatched EV, not 8, not 12. No ICE unknown board. No pack price.
- Restate Limited / extras-off if they ask keep-driving. This skill does not diagnose if they ask which part.
- Your 2016 Leaf / your Transit.

**Fail**

- “It’s the 12V battery — fit one.” / “It’s the DC-DC.” / “It’s the traction pack.”
- Calling `alternator-replacement-cost`, or any belt / water-pump / cambelt slug, because lamp 8 is on an EV.
- “Heavy steering / rising temp / belt noise — Stop” copied from ICE onto this board.
- Mapping turtle, charge plug, or HV message to 8 or 12, or switching to the ICE unknown cluster.
- “About £120 for a battery” with no `repair_cost` result. Invented pack or trade-in pounds.
- Driveway battery fit, jump-start tutorial, code clear, or HV isolation steps.
- Shop or scanner links above a Stop line (if another lamp made it Stop).
- “Expect a fail.” A real plate in git or speech.

**Pass sketch** (illustrative; no live pounds): Your 2016 Leaf, 12V rectangle, not the pack. Limited; extras off; no belt combo. Outlook: a garage can usually handle this. If they later invoice a 12V battery, quote the tool headline; the lamp did not name that part. Turtle or HV text would not have been this card.
