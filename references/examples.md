# Worked examples

These conversations are **illustrative**.

The vehicle card matches the public `POST /api/vehicle` response shape.

The owner plate in the prose is always `AB12CDE` (fictional).

After a lookup, refer to the car as "your 2016 Fiesta", never by plate.

MOT records are Crown copyright. Lamp advice is original to this skill.

## Example A — main path: plate first, then lamp 6 `engine-steady`

Owner starts with a plate and no lamp. The agent **draws the cluster** before any lookup. A name-only list is a fail.

**Owner:** plate AB12CDE

**Agent:** shows the 13 lamp **icons** from `assets/` via `references/lamp-picker.md`. Asks which **number matches the shape** that is lit. A name-only list is a fail.

**Owner:** 6

The agent does not diagnose. It asks only what the menu cannot know, then looks up `{"reg":"AB12CDE"}`.

**Agent:** When did it start, and has power, noise, smell, smoke, steering or temperature changed?

**Owner:** This morning. The car drives normally. No smoke.

Lookup is `POST /api/vehicle` with `{"reg":"AB12CDE"}`. Illustrative card (same shape as the live contract):

```
make FORD / model FIESTA / petrol / 998cc / year 2016 / colour Blue
first_used 2016-03-14 / mot_due 2027-03-01
last test 2026-03-02 PASSED 61201 mi
advisories: Front Brake pad(s) wearing thin; Nearside Front Tyre worn close to legal limit
fusion.matched includes brake-pads-wearing-thin count 1
NO emissions/exhaust/catalyst/lambda/smoke defects
```

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

They pick lamp 6. The statement still happens. Do not invent a DVSA history.

**[Vehicle]** Your 2014 Golf 2.0 TDI · about 80,000 miles (owner-stated). No MOT record available.

**[Showing]** Amber engine-block outline, steady (`engine-steady`).

**[Since]** Not given in this example.

**[Symptoms]** Not given in this example.

**[History]** This is owner-stated, not this car's MOT record.

**[Drive advice]** Drive with care. If it starts flashing, stop as soon as it is safe, switch off, and do not restart to get home. A scan is the correct next step. The lamp does not name the fault.

**[Ask the garage]** Please read the stored code and the freeze frame before replacing anything. Does the diagnostic fee come off the repair?

## Example D — unmatched lamp (short)

**Owner:** there's a light on

**Agent:** shows the same 13 icons. Does **not** default to `engine-steady`. Does not look up a plate it does not have.

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
