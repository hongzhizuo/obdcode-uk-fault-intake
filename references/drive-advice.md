# Drive advice

They are on a computer or phone. Do **not** ask if they are driving. Do **not** hold the statement for a parked confirmation.

**Colour does not set drive advice.** A red lamp is not automatically Stop. Airbag is red and **Limited**. Flashing engine is amber and **Stop**. Ignore any picture caption that groups lamps by colour.

`safety_class: Red` means no owner repair. It is not Stop.

Give **[Drive advice]** in the same turn as a named lamp or a valid pick — including while a plate lookup is failing.

## Stop (do not drive it in; arrange collection or recovery)

- `oil-pressure` (1) — always. A cold dipstick reading is information for the garage, not a restart.
- `coolant-temp` (2) when the lamp is **red**. If they named a thermometer and did not give colour, ask blue or red before this id. Blue after a short run that then goes out is engine-cold, not a fault — skip outlook.
- `brake-system` (3) if the parking brake / EPB / Auto Hold is **fully off** and the lamp stays, **or** they already reported a spongy pedal, a pull, or a leak. If they pick 3 and have not mentioned the parking brake, ask whether it is fully off (classification, not a driving quiz). Until that answer, **YesWithCare** — then Stop if it stays on with EPB off.
- `engine-flashing` (7)
- `battery-charging` (8) on an ICE car **plus** heavy steering, a rising temperature gauge, or a belt noise. Skip that combo on electric. Default “drives normally” does **not** skip Stop if they already volunteered the combo.
- `unmatched-adblue` with remaining-starts or will not start.

If they are still on the picker, and speech already maps to oil-can, flashing engine, or red thermometer, put that Stop line in the **same turn** as the picture.

## Limited (drive directly there, no extra journeys)

- `airbag-srs` (4)
- `power-steering` (5) unless steering is already heavy (then Stop)
- `dpf` (9) on diesel when the lamp is on and the car still drives; flash / limp / oil over max → Stop repeating motorway loops; recover if it will not stay a runner
- `unmatched-gpf` — drive with care / Limited; scan; no diesel regen copy
- `unmatched-ev` unless a red stop lamp is also on
- Electric board lamp 8 (12V rectangle)

## Not a fault — skip outlook

- Glow 13 on with ignition then **out**
- Blue thermometer that went out
- Brake lamp with parking brake still on and a normal pedal
- ESC 12 **flashing while driving**
- Key-on bulb check that went out

## Glow is never engine-flashing

Stays on or flashes at 13 → garage, still id `glow-plug`. Do not grade it “like 7”. Do not call catalytic-converter cost. If they also report misfire or smoke, say so in **[Since]**; keep id 13.

## Extra questions (only these)

- `tyre-pressure` — flash-then-steady at startup (malfunction) vs simply on (likely inflate)
- `esc-traction` — flashing (intervening) vs steady (off or faulty)
- `glow-plug` — went out vs stays vs flashes
- Engine family (“engine light”, EML, MIL, check engine): **steady or flashing** before id 6 vs 7. Do not open the cluster unless they are unsure. Do not treat a bare 6 as steady until they said it is not flashing.
- Thermometer: **blue or red** before id 2
- Brake 3: parking brake fully off?

## Unmatched paths (not a 14th lamp)

- **AdBlue / urea / DEF:** not on any picture. Do not map to 9 or 6. Path `unmatched-adblue`.
- **Petrol or hybrid + exhaust-dots / “particulate filter” / pick of 9:** path `unmatched-gpf`. Keep that board. Not DPF. Not “9 is not printed, pick again.”
- **Electric + turtle / tortoise / limited power / car-with-! and no skid lines / charge plug / HV text:** path `unmatched-ev`. Do not pick 12 or 8. Do not open the ICE unknown board.

12 is skid-lines only.
