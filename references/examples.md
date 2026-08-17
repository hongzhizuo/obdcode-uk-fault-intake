# Worked examples

Illustrative. The owner plate in prose is always `AB12CDE` (fictional). After lookup, refer to the car as "your 2016 Fiesta" or "your Transit", never by plate.

Do not ask if they are driving. Stop / recovery belongs in **[Drive advice]**.

## Example A — plate first, petrol picture, lamp 6 then flashing check

**Owner:** plate AB12CDE

Lookup `POST /api/vehicle` `{"reg":"AB12CDE"}`. Illustrative card: 2016 Fiesta petrol, 998cc, MOT due 1 March 2027, last test 61,201 mi, fusion includes brake-pads-wearing-thin, no emissions-family defects.

**Agent:** `show_dashboard` `board=petrol` (required), then `open_resource`. Asks which **circled** number. Does not say reply 1–13. Does not list names.

**Owner:** 6

**Agent:** Same turn: this is the engine outline. Steady or flashing? Drive with care unless it is flashing. Anything feel different?

**Owner:** Steady. This morning. Drives normally.

Spoken card (~70 words), then stop:

**[Vehicle]** Your 2016 Fiesta, 998 cc petrol · 61,201 miles · MOT due 1 March 2027.

**[Showing]** Amber engine outline, steady.

**[Since]** This morning. Drives normally.

**[History]** No emissions-family notes on this car's MOT record. This does not show the cause of today's lamp.

**[Drive advice]** Drive with care. If it starts flashing, do not drive it in; arrange recovery. A scan is the next step. The lamp does not name the fault.

**[Ask the garage]** Read the stored code and the freeze frame before replacing anything. Does the diagnostic fee come off the repair?

If they then ask "so is it the cat?", example E.

## Example B — oil lamp named, plate in the same message

**Owner:** oil light is on, plate AB12CDE

**Agent:** Does **not** ask if they are driving. Lookup. Statement with Stop + recovery. No picker.

**[Vehicle]** Your 2016 Fiesta, 998 cc petrol · 61,201 miles · MOT due 1 March 2027.

**[Showing]** Red oil-can.

**[Drive advice]** Stop. Do not drive it in. Ask the garage to collect, or call recovery. A correct dipstick reading once cold does not make it safe to restart.

**[Since]** (owner facts) How long was the lamp on? Any engine noise? When was the oil last changed?

## Example C — `not_found`

Live probe 17 August 2026: `{"reg":"ZZ99ZZZ"}` → 404 `not_found`.

**Agent:** New and some imported cars may have no MOT yet. Make, year, fuel, mileage? Does **not** open the unknown 13-lamp picture first.

**Owner:** 2014 Golf 2.0 TDI, about 80,000 miles.

**Agent:** `show_dashboard` `board=diesel`. They pick 6, say not flashing. Thinner statement. Do not invent MOT history.

## Example D — unnamed lamp, no plate

**Owner:** there's a light on

**Agent:** Asks plate or fuel. Does **not** open unknown as the homepage. Does **not** default to engine-steady.

## Example E — diagnosis refusal

**Owner:** so is it the catalytic converter?

**Agent:** This skill does not diagnose. The lamp does not name the part. Hand the statement to the garage. If they ask whether they can keep driving, restate drive advice. Do not say "continue as a normal assistant."

## Example F — repo hygiene

No real registrations. No SAE J2012 tables. Only `AB12CDE` as the owner plate.

## Example G — diesel Transit, lamp 9

Lookup: TRANSIT, `fuel_type` diesel.

**Agent:** `show_dashboard` `board=diesel`. Same diesel picture. Call it **your Transit**, not a van board. They pick 9.

**[Vehicle]** Your Transit, diesel.

**[Showing]** Amber exhaust box with dots (DPF).

**[Drive advice]** Limited. Drive directly there, no extra journeys. One handbook regen if it is driving normally. If it flashes, a red warning appears, limp mode, or the oil is over maximum: do not keep repeating motorway runs. Do not drive it in if those apply — arrange recovery.

**[Ask the garage]** Soot load and differential pressure. Not a soot-vs-ash fork.

## Example H — electric, lamp 8

Lookup: LEAF, `fuel_type` electric. `show_dashboard` `board=electric`. They pick 8.

**[Showing]** 12V charging rectangle, not the traction pack.

**[Drive advice]** Limited. Belt / water-pump / heavy-steering combo does not apply.

If they describe a turtle or a car-with-! and no skid lines: unmatched EV, not 12 or 8. Do not open the ICE unknown board.

## Example I — glow 13 went out after start

Diesel board. They pick 13. It came on with ignition and went out.

**Agent:** That is the preheat cycle. Not a fault. No garage card.

## Example J — petrol GPF

Petrol picture. They say exhaust-dots, or they type 9.

**Agent:** Keep the petrol picture. 9 is an empty slot, not DPF. Unmatched petrol particulate-filter lamp. Drive with care. Scan. No regen copy. Still a thinner statement.

## Example K — AdBlue

Diesel. They say AdBlue.

**Agent:** Not on the picture. Not 9, not 6. Limited unless remaining-starts / no-start (then Stop, do not drive it in). Ask SCR / reagent status, not a parts fork.
