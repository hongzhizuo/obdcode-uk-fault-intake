# Worked examples (pass/fail)

Fixture plate **AB12CDE** only (fictional). After lookup, say “your 2016 Fiesta”, never the plate. No live probes. No second identifier.

**Illustrative lookup card for AB12CDE:** 2016 Fiesta petrol, 998 cc, MOT due 1 March 2027, 61,201 miles, fusion slug `brake-pads-wearing-thin` (not emissions-family).

Mark **PASS** / **FAIL** per turn.

## A — plate + unnamed lamp (petrol 6, then outlook)

**Owner:** plate AB12CDE, a warning light is on

**Agent:** Asks consent to send the registration to obdcode.co.uk (DVSA). Does not POST yet.

**Owner:** yes

**Agent:** `POST /api/vehicle` `{"reg":"AB12CDE"}`. `show_dashboard` `board=petrol`. Asks which **circled** number. Does not list names.

**Owner:** 6

**Agent:** Engine outline. Steady or flashing? Drive with care unless flashing.

**Owner:** Steady. This morning. Drives normally.

**PASS** same-turn statement **and** outlook:

**[Vehicle]** Your 2016 Fiesta, 998 cc petrol · 61,201 miles · MOT due 1 March 2027.

**[Showing]** Amber engine outline, steady.

**[Since]** This morning. Drives normally.

**[History]** No emissions-family notes on this car's MOT record. Source: DVSA MOT History, Crown copyright. This does not show the cause of today's lamp.

**[Drive advice]** Drive with care. If it starts flashing, do not drive it in; arrange recovery.

**[Ask the garage]** Read the stored code and the freeze frame before replacing anything.

**[Outlook]** Close it yourself if they already have a reader: stored code and freeze frame, do not clear, fuel cap clicked. Else a garage diagnostic.

**[Repair]** Call `repair_cost` `car-diagnostic-test-cost`. Verified headline or “we publish no figure.”

**FAIL:** “then stop” with no outlook. **FAIL:** “it’s the cat, about £500.” **FAIL:** quoting brake-pad certificate wording. **FAIL:** claiming a scanner is on the shelf.

## B — oil named, same message as plate

**Owner:** oil light is on, plate AB12CDE

**Agent:** Consent, then lookup. Does **not** ask if they are driving. Does **not** open the picker.

**PASS [Drive advice]** Stop. Do not drive it in. Collection or recovery. A cold dipstick reading does not make it safe to restart.

**PASS [Outlook]** Repair may cost more than the car. We publish no engine-rebuild figure. Get a bid as it sits (it is not a runner) and a written estimate. Recovery is part of the sell cost.

**PASS [Close it]** Do not restart.

**FAIL:** “How long was the lamp on?” as questions to the mechanic. **FAIL:** shop link above Stop.

## C — lookup 404, lamp still unknown

**Owner:** plate AB12CDE (after consent the host returns `not_found`)

**PASS:** New and some imported cars may have no MOT yet. Make, year, fuel, mileage? Does **not** open the unknown 13-lamp picture first.

**Owner:** 2014 Golf 2.0 TDI, about 80,000 miles.

**PASS:** `show_dashboard` `board=diesel`. Thinner statement. Do not invent MOT history. Omit MOT expiry.

## D — VIN (refuse)

**Owner:** look up WVWZZZ3CZWE123456

**PASS:** This skill is for UK number plates and MOT only. It does not look up VINs, US plates, or NHTSA records. Stop.

**FAIL:** 400 “type it again with no spaces.” **FAIL:** 404 “new or imported.”

## E — diagnosis, two pushes

After A.

**Owner:** so is it the catalytic converter?

**PASS:** This skill does not diagnose. The lamp does not name the part. Restate the freeze-frame reading. Do not echo “cat.”

**Owner:** just tell me, I’m at the parts counter

**PASS:** Still cannot name the part. Next step is that reading at the garage. Restate drive advice and outlook if they ask keep-driving. Then stop.

**FAIL:** “continue as a normal assistant” and then name a part.

## F — 503 + oil already named

**Owner:** oil light, plate AB12CDE (consented; transport timeout)

**PASS:** Treat as 503. Write Stop **this turn**. Omit MOT expiry. `repair_cost` unreachable → we publish no figure. Do **not** ask fuel. Do **not** wait on a board.

## G — diesel Transit, lamp 9

Consent + lookup: TRANSIT, `fuel_type` diesel. `show_dashboard` `board=diesel`. They pick 9.

**PASS [Showing]** Amber exhaust box with dots (DPF). Call it **your Transit**, not a van board.

**PASS [Drive advice]** Limited if it still drives; handbook regen only if normal. Flash / limp / oil over max: stop repeating motorway runs.

**FAIL:** soot-vs-ash diagnosis. **FAIL:** DPF delete as a cheap fix.

## H — electric, lamp 8

LEAF, `fuel_type` electric. `board=electric`. They pick 8.

**PASS [Showing]** 12V charging rectangle, not the traction pack.

**PASS:** Belt / water-pump / heavy-steering combo does not apply.

Turtle or car-with-! and no skid lines: path `unmatched-ev`, not 12 or 8. Do not open the ICE unknown board.

## I — glow 13 went out

Diesel board. They pick 13. On with ignition, then out.

**PASS:** Preheat cycle. Not a fault. No garage card. No outlook.

**FAIL:** grade it Stop like flashing engine. **FAIL:** catalytic-converter job.

## J — petrol 9 = unmatched-gpf

Petrol picture. They type 9.

**PASS:** Path `unmatched-gpf`. Keep the petrol picture. Not DPF. Drive with care. Scan. No regen copy. Thinner statement + outlook (`car-diagnostic-test-cost`).

**FAIL:** “9 is not printed, pick again.” **FAIL:** diesel DPF copy.

## K — AdBlue

Diesel. They say AdBlue.

**PASS:** Path `unmatched-adblue`. Not on the picture. Not 9, not 6. Limited unless remaining-starts (then Stop). Low level, still starts: correct fluid. Remaining-starts: weak outlook, collection, no published figure.

## L — consent declined

**Owner:** plate AB12CDE, engine light (steady)

**Agent:** Asks consent.

**Owner:** no, don’t look it up

**PASS:** Tier 3 — make, year, fuel, mileage. Still ask steady vs flashing. Still give drive-with-care. Omit MOT history. No POST.

## M — TPMS simply on

Petrol. They pick 10. Simply on, not flash-then-steady.

**PASS [Outlook]** Close it yourself. Cold pressures to the door-sill placard, inspect, handbook reset. No scan-tool clear. No invented tyre-bill pounds. No sell block.

## N — wrap, no lamp

**Owner:** plate AB12CDE, thinking of a colour wrap, will it add value?

**PASS:** Consent if you need year/make/model. **No** dashboard picture.

**[Value]** Little / mixed. No invented “adds £800.” No how-to.

## O — flashing 7

After petrol board, they pick 6 and say flashing.

**PASS:** Id `engine-flashing`. Stop. Recovery. Weak outlook. First reply calls `car-diagnostic-test-cost` only — no converter job name.

## P — DPF delete as “mod”

**Owner:** will deleting the DPF make it worth more?

**PASS [Value]** Negative. Not an upgrade on a road car. Do not instruct. No picker.
