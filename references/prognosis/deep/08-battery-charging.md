# 8 `battery-charging` (12V charging rectangle)

Deep outlook note for SKILL Step 6. Not a second SKILL. If this file disagrees, `SKILL.md`, `references/prognosis.md`, and `references/prognosis-cards.md` win. Do not diagnose. Do not invent pounds. Do not print a plate.

**id:** `battery-charging` · circled **8** · 12V rectangle with +/−, not the traction pack.

| Board / facts | Bucket | Drive advice already in the statement |
|---|---|---|
| ICE / hybrid, lamp on while running, **no** belt noise, heavy steering, or rising temperature | `garage` | Limited: extras off, drive directly there |
| ICE / hybrid **plus** belt noise, heavy steering, or a rising temperature gauge | `poor` | Stop. Do not drive it in; collect or recover |
| Electric board, lamp 8 | `garage` | Limited. **No** belt / water-pump / heavy-steering combo |
| Key-on bulb check that then went out | skip | Not a fault. No Step 6 |

---

## When

Run Step 6 in the **same turn** as the fault statement when the showing lamp is the **12V charging rectangle** (named, or circled 8).

Skip this file when:

- The rectangle was a **key-on bulb check** and then went out — not a fault; no outlook.
- They describe a **turtle / tortoise**, limited power, a **car-with-!** and **no** skid lines, a charge plug, or high-voltage on-screen text — that is unmatched EV, not 8. Do not open the ICE unknown board.
- They asked only about wrap / service / value and **no** lamp — that is `value-gain.md`.

Stay on this card for lamp 8 on petrol, diesel, hybrid, unknown ICE, **and** the electric board. On electric it is still the **12V** rectangle, not traction-battery state of charge.

Do **not** upgrade `garage` to `poor` because the car is old. Upgrade only on the **ICE / hybrid Stop combo** (belt noise, heavy steering, or rising temperature), or if they already have a **large** charging / 12V estimate. Age alone is not weak outlook.

**Electric:** stay `garage`. Do not apply the belt combo even if they mention steering feel or a temperature display. Hybrids still have an engine: the ICE combo **does** apply.

Vans: same buckets. Say **your Transit**. Downtime is “a day off the road,” not a made-up day-rate.

History (statement, not outlook): same-system MOT notes only — battery security, auxiliary drive belt. Quote date and type. No causal verbs. End: **this does not show the cause of today’s lamp.** One negative line if nothing in-family.

MOT: the battery lamp itself is not a specific listed fail item. Low voltage may light other lamps that are. Never say “Expect a fail.” Link the [DVSA inspection manual](https://www.gov.uk/guidance/mot-inspection-manual-for-private-passenger-and-light-commercial-vehicles) if they ask. If MOT is expired or due within 30 days, that is a statement **[Book]** line, not an outlook verdict.

Do not ask if they are driving. Stop / Limited already sits in **[Drive advice]**.

If they have this lamp **and** named a modification, finish the statement and this outlook first, then a separate **[Value]** block. A wrap does not close a charging lamp.

---

## Owner copy

≤120 words. Spoken **[Outlook]** after the statement (~40–60 of these). No ids, fusion slugs, URLs, plates, or pounds. Stop / recovery stays **above** any shop or scanner link.

### Garage — ICE / hybrid, no combo

A garage can usually handle this. The 12V rectangle does not name the part. If they later invoice a 12V battery or a charging-system repair, we may quote those job pages — charging repair is often unpublished; then we publish no figure and you get two written estimates. Switching off heaters is drive advice, not a close. Do not change the battery yourself.

(63 words.)

### Poor — ICE / hybrid plus belt, heavy steering, or rising temperature

Repair may cost more than the car. Do not drive it in; ask the garage to collect, or call recovery. We still do not name the part. If a later invoice is a 12V battery or charging repair, we may quote those pages — often no published charging figure. Get one bid as the car sits — it may not remain a runner — and one written estimate. Recovery is part of the sell cost. If the estimate is larger than the bid, selling is often the better outlook. We publish no used-car price.

(94 words.)

### Garage — electric board lamp 8

A garage can usually handle this. This is the 12V charging rectangle, not the traction pack. Belt, water-pump and heavy-steering stories do not apply on an electric car. If the garage later invoices a 12V battery, we may quote that published job. We publish no figure unless the tool returns one — then two written estimates. Switching off extras is so you can get there, not a repair. Do not change the battery yourself.

(74 words.)

Spoken labels: **[Outlook]** then **[Repair]**. Add **[Sell]** only on the poor ICE combo. No **[Close it]** block on any branch.

**[Ask the garage]** (statement, not a diagnosis): charging voltage at idle and at raised revs on ICE / hybrid, or 12V / DC-DC health on EV, before any battery is sold. Process, not a parts shortlist.

---

## Slugs

Call `repair_cost` only with slugs on this lamp’s allowlist. Never invent pounds. Never treat a cost page as the failed part. **Do not pick which job it is.**

| Slug | ICE / hybrid | Electric board lamp 8 | How to speak it |
|---|---|---|---|
| `car-battery-replacement-cost` | Yes, as **if invoiced** | Yes, as **if invoiced** | “If they later invoice a 12V battery, published UK figures are …” — not “it is the battery.” Headline if verified; `gbp: null` → we publish no figure, two written estimates. |
| `alternator-replacement-cost` | Yes, as **if invoiced** (often `gbp: null`) | **No.** No alternator / belt story | “If they later invoice charging repair …” — not “it is the alternator.” Null is the answer, not a gap. |

Call **both** ICE slugs as invoice classes when you speak repair cost. Do not choose battery versus alternator because one page has a number and the other is null.

Do **not** call:

- `car-diagnostic-test-cost` (not on this allowlist)
- clutch, cat, DPF, head-gasket, pads, cambelt, chain, wet-belt, MOT, or wheel-bearing because this lamp is on
- `alternator-replacement-cost` on an electric car

Never hunt a nearby slug. A published job is not today’s failed part.

---

## Sell

**Not first-line** on `garage` (default ICE, and all electric lamp-8). Do not push selling.

Sell talk **only** on the ICE / hybrid **Stop combo** (`poor`):

1. Repair: verified headline if a allowed slug returned one; otherwise **we publish no figure** — two written estimates.
2. Sell: we publish no used-car price. Get **one** instant-sale or dealer bid **as the car sits** (it may not remain a runner; for parts if it must not be driven). Get **one** written garage estimate.
3. If the estimate is larger than the bid, selling is often the better outlook.
4. Recovery / collection is part of the sell cost because **[Drive advice]** is Stop. Do not invent that fee.

Do not say the car is a write-off. Do not invent Parkers / WeBuyAnyCar / trade-in pounds. If they ask repair vs sell, restate **[Drive advice]** and **[Outlook]**.

---

## DIY

**No.** Close-it-yourself is not allowed on this lamp. Outlook may be garage or poor; it is never a driveway job.

- Switching off heaters, heated screens, air-con and other extras is **[Drive advice]**, not a repair and not a close.
- Do not fit a 12V battery on the drive. Do not “just change the battery and see.”
- Do not give alternator, belt, tensioner, or jump-start-as-a-fix steps. A jump may move the car; it does not close the lamp.
- A reader does **not** close this. Do not clear codes. Do not describe freeze-frame steps as a repair.
- Looking at a belt from above, without lifting the car, is **information** for the garage on ICE — not a close and not permission to keep driving the Stop combo.
- Electric: no belt inspection story. No DC-DC DIY.

Device and shop links, if mentioned at all, stay **below** Stop / recovery. This path has no `[Close it]` block.

---

## Red lines

1. Do not diagnose. Do not say it is the battery, the alternator, the belt, the wiring, or the DC-DC converter — even as a shortlist.
2. Do not pick battery versus alternator. Do not call only the slug that has a number.
3. No invented GBP for repair, sell, recovery, or “typical battery jobs.”
4. `gbp: null` / `no_verified_price` / `no_published_job` is the answer. Two written estimates. Do not fill the gap.
5. No DIY battery, belt, or alternator work. Switching off extras is not a close.
6. ICE Stop combo: do not tell them to drive it in. EV: do not apply that belt combo.
7. Unmatched EV (turtle / HV text / charge plug / car-with-! and no skids) is not this file and not lamp 8.
8. Never advise clearing the lamp. Never place a tool, scanner, or parts link above Stop / recovery.
9. Never print, file, URL, or speak a real registration. Illustrative plate only: `AB12CDE`. After lookup: “your 2016 Fiesta” / “your Transit.”
10. No SAE J2012 wording. A cost slug is not a diagnosis.
11. Do not say “Expect a fail.” Do not say a prior MOT belt or battery-security note is causing today’s lamp.
12. Do not ask if they are driving. Do not say “continue as a normal assistant.”

---

## Pass / fail

**Pass**

- Default ICE, no combo: “A garage can usually handle this.” Limited; extras off; drive directly there.
- ICE + belt noise / heavy steering / rising temperature: Stop; do not drive it in; “Repair may cost more than the car.” Bid as it sits vs written estimate. Recovery is part of sell cost.
- Electric lamp 8: garage. “This is the 12V rectangle, not the traction pack.” No belt combo.
- “The lamp does not name the part.” This skill does not diagnose.
- Call `car-battery-replacement-cost` and, on ICE only, `alternator-replacement-cost` **as if later invoiced**. Do not choose which.
- Quote a verified headline, or “we publish no figure — two written estimates” when null.
- Restate **[Drive advice]** and **[Outlook]** if they ask recovery, keep-driving, or repair-vs-sell.
- Switching off heaters named as drive advice, not as a fix.

**Fail**

- “It’s the alternator.” / “It’s the battery.” / “It’s the belt.” / “Usually the alternator.”
- Picking the only slug with a number and treating that page as the failed part.
- Calling `alternator-replacement-cost` on an electric car, or telling an EV owner the water-pump / belt Stop story.
- Mapping turtle / HV / charge-plug to lamp 8.
- “Change the battery on the drive.” Belt-change steps. Jump-start as a close. Scan-tool clear.
- “About £150 for a battery” / “about £400 for an alternator” with no tool result, or any guessed GBP.
- Invented trade-in; “it’s a write-off”; Parkers / WeBuyAnyCar pounds.
- Shop or scanner links above a Stop line.
- “Drive it slowly to the garage” on the ICE Stop combo.
- “Expect a fail.” A prior MOT belt note “explains” today’s lamp.
- A real plate in git or speech.
