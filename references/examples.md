# Worked examples

These conversations are **illustrative**.

The vehicle card matches the public `POST /api/vehicle` response shape.

The owner plate in the prose is always `AB12CDE` (fictional).

After a lookup, refer to the car as "your 2016 Fiesta" or "your Transit", never by plate.

When the owner only sent a plate, look the vehicle up first, then show the fuel-specific board. Example B is the exception: a named stop lamp while driving is stop-first, before lookup.

MOT records are Crown copyright. Lamp advice is original to this skill.

## Example A — main path: plate first, lookup, petrol board, then lamp 6 `engine-steady`

Owner starts with a plate and no lamp. The agent **looks the vehicle up first**. The illustrative card is a 2016 Fiesta petrol. Then the agent shows the **petrol board** (`cluster-petrol.png` via `show_dashboard` `board=petrol`), not the full 13-lamp cluster. DPF 9 and glow-plug 13 are not on this picture. A name-only list is a fail.

**Owner:** plate AB12CDE

Lookup is `POST /api/vehicle` with `{"reg":"AB12CDE"}`. Illustrative card (same shape as the live contract):

```
make FORD / model FIESTA / petrol / 998cc / year 2016 / colour Blue
first_used 2016-03-14 / mot_due 2027-03-01
last test 2026-03-02 PASSED 61201 mi
advisories: Front Brake pad(s) wearing thin; Nearside Front Tyre worn close to legal limit
fusion.matched includes brake-pads-wearing-thin count 1
NO emissions/exhaust/catalyst/lambda/smoke defects
```

**Agent:** Opens the petrol dashboard PNG (`show_dashboard` with `board=petrol`, then `open_resource` on the `file://` preview of `cluster-petrol.png`) and asks which **number on the picture** is lit. This board is for a petrol car. DPF 9 and glow-plug 13 are not on this picture. A name-only list is a fail. An iframe or clickable widget is not required.

**Owner:** 6

**Agent:** Calls MCP `show_lamp` with number 6 so they can confirm the shape. Asks only what the menu cannot know.

**Agent:** When did it start, and has power, noise, smell, smoke, steering or temperature changed?

**Owner:** This morning. The car drives normally. No smoke.

Then the statement the owner can read aloud:

**[Vehicle]** Your 2016 Fiesta, 998 cc petrol · 61,201 miles · MOT due 1 March 2027.

**[Showing]** Amber engine-block outline, steady (`engine-steady`).

**[Since]** This morning, in normal use.

**[Symptoms]** Drives normally. No smoke. No reported change in power, noise, smell, steering or temperature.

**[History]** There are no related MOT defects in the emissions, exhaust, catalyst, lambda or smoke family. Unrelated advisories exist on a different system: front brake pads wearing thin (`brake-pads-wearing-thin`, count 1) and a nearside front tyre worn close to the legal limit. Those do not explain this lamp.

**[Drive advice]** Drive with care. If it starts flashing, stop as soon as it is safe, switch off, and do not restart to get home. A scan is the correct next step. The lamp does not name the fault.

**[Ask the garage]** Please read the stored code and the freeze frame before replacing anything. Does the diagnostic fee come off the repair? Check this car against the [DVSA inspection manual](https://www.gov.uk/guidance/mot-inspection-manual-for-private-passenger-and-light-commercial-vehicles) rather than assuming the MOT outcome.

The agent **stops**. If the owner then asks "so is it the cat?", the reply is example E.

## Example B — safety path: oil lamp while driving, lamp 1 `oil-pressure`

Owner names a stop lamp and is already driving. The first assistant message is **stop**. No lookup in that message.

**Owner:** oil light is on, I'm driving, plate AB12CDE

**Agent:** Stop as soon as it is safe. Pull over, switch off, and do not restart to get home. This is the red oil-can. It means oil is not at pressure. Confirm when you have stopped.

**Owner:** I've stopped and switched off.

Then lookup `{"reg":"AB12CDE"}` (same illustrative card as A). Then the statement.

**[Vehicle]** Your 2016 Fiesta, 998 cc petrol · 61,201 miles · MOT due 1 March 2027.

**[Showing]** Red oil-can (`oil-pressure`).

**[Since]** Came on while driving.

**[Symptoms]** Lamp on in motion. No further symptoms given.

**[History]** No oil-pressure-related items on this car's MOT record.

**[Drive advice]** Stop now. Do not drive to a garage. Arrange recovery. A correct dipstick reading once the engine is completely cool does not make the car safe to restart. No owner repair of bearings.

**[Ask the garage]** How long was the lamp on before you stopped? Did the engine make any noise? When was the oil last changed?

## Example C — live `not_found` (short)

Live probe on 17 August 2026: `POST /api/vehicle` `{"reg":"ZZ99ZZZ"}` → HTTP 404 `{"status":"not_found"}`.

**Agent:** New and some imported cars may have no MOT record yet. What is the make, year, fuel, and approximate mileage?

**Owner:** 2014 Golf 2.0 TDI, about 80,000 miles.

**Agent:** `show_dashboard` `board=diesel` (owner-stated fuel), then they pick lamp 6. The statement still happens. Do not invent a DVSA history.

**[Vehicle]** Your 2014 Golf 2.0 TDI · about 80,000 miles (owner-stated). No MOT record available.

**[Showing]** Amber engine-block outline, steady (`engine-steady`).

**[Since]** Not given in this example.

**[Symptoms]** Not given in this example.

**[History]** This is owner-stated, not this car's MOT record.

**[Drive advice]** Drive with care. If it starts flashing, stop as soon as it is safe, switch off, and do not restart to get home. A scan is the correct next step. The lamp does not name the fault.

**[Ask the garage]** Please read the stored code and the freeze frame before replacing anything. Does the diagnostic fee come off the repair?

## Example D — unmatched lamp (short)

**Owner:** there's a light on

**Agent:** no plate yet, so `board=unknown` (full cluster). Does **not** default to `engine-steady`. Does not look up a plate it does not have.

## Example E — diagnosis refusal (short)

After example A:

**Owner:** so is it the catalytic converter?

**Agent:** This skill does not diagnose. The lamp does not name the part. Hand the statement to the garage. Continue as a normal assistant. Do not invent a cause.

## Example F — repo hygiene

The published skill must not contain:

- Real registrations
- SAE J2012 definition tables
- Site source paths

This file uses only `AB12CDE` as the owner plate.

## Example G — diesel van: lamp 9 `dpf` (short)

Owner starts with a plate and no lamp. Lookup first. The card is a Transit, `fuel_type` diesel. Then the diesel van board — not a car cluster and not a petrol board.

**Owner:** plate AB12CDE

Lookup is `POST /api/vehicle` with `{"reg":"AB12CDE"}`. Illustrative card:

```
make FORD / model TRANSIT / fuel_type diesel / year 2018
```

**Agent:** `show_dashboard` with `board=diesel` `body=van`, then `open_resource` the `file://` preview. Caption: this board is for a diesel van. Asks which **number on the picture** is lit.

**Owner:** 9

**Agent:** Calls MCP `show_lamp` with number 9 (`dpf`). Then the statement. Refer to **your Transit**, never the plate.

**[Vehicle]** Your Transit, diesel.

**[Showing]** Amber exhaust box with dots (`dpf`).

**[Drive advice]** Limited driving. A handbook regeneration drive is the usual first attempt if the van is driving normally. If the lamp flashes, a red warning appears, the van is in limp mode, or the oil level has risen above maximum, do not keep repeating motorway runs.

The agent **stops**. It does not diagnose.

## Example H — electric car: lamp 8 `battery-charging` (short)

Owner starts with a plate and no lamp. Lookup first. `fuel_type` electric. Then the electric board. That picture has no oil, engine, DPF or glow-plug.

**Owner:** plate AB12CDE

Lookup is `POST /api/vehicle` with `{"reg":"AB12CDE"}`. Illustrative card:

```
make NISSAN / model LEAF / fuel_type electric / year 2021
```

**Agent:** `show_dashboard` with `board=electric`, then `open_resource` the `file://` preview. This board has no oil (1), engine (6/7), DPF (9) or glow-plug (13). Asks which **number on the picture** is lit.

**Owner:** 8

**Agent:** Calls MCP `show_lamp` with number 8 (`battery-charging`). On this board, 8 is the **12V** system, not the traction pack. Then the statement. Do not diagnose.

**[Vehicle]** Your 2021 Leaf, electric.

**[Showing]** Battery / charging (`battery-charging`). This is the 12V system, not traction-battery state of charge.

**[Drive advice]** Limited driving. The lamp does not name the part.

The agent **stops**. It does not diagnose. It does not name a DC-DC converter, a traction pack, or any other cause.
