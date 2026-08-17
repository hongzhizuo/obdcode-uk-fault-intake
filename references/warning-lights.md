# UK Dashboard Warning Lamps

Thirteen lamps cover almost everything a UK driver will see. Unlike fault codes, this list does not grow.

Grading follows a four-level scheme so it can be consumed programmatically:

- `safety_class` — `Green` (owner can act) · `Amber` (owner can check, repair is professional) · `Red` (no owner repair at all)
- `drive_advice` — `Yes` · `YesWithCare` · `Limited` (get it to a garage, no journeys) · `Stop` (pull over now)
- `warnings` — `W-SUPPORT` (lifting/support) · `W-HOT` (burns/scalding) · `W-ELECTRICAL` (12V, SRS, HV) · `W-CO` (exhaust gas/ventilation)

These 13 `id` values are stable. Do not rename them. Which still picture to show depends on the car (`references/boards.md`). 7 is not a second drawing: the engine cell is 6; flashing is spoken as 7.

Boards are subsets. Numbers stay global. Ghost slots keep omitted numbers in place so owners do not count cells.
- petrol / hybrid: ghost 9 DPF and 13 glow-plug
- diesel / unknown: live 1–6, 8–13
- electric: ghost 1, 6, 9, 13; keep 2, 3, 4, 5, 8, 10, 11, 12. Lamp 8 on an EV is the 12V system.

**Colour first.** Red means stop or act now. Amber means investigate. Blue and green are informational — main beam, cruise, indicators — and are not faults.

**Behaviour second.** Steady and flashing are frequently different faults with different urgency. Behaviour is already split into separate ids where it changes urgency (`engine-steady` vs `engine-flashing`). Only ask about behaviour when the chosen id still needs it: tyre-pressure flash-then-steady, `esc-traction`, and `glow-plug`.

MOT notes below say *where the lamp applies*. Whether a given lamp is testable depends on the vehicle's first-use date and whether the system is fitted. Verify against the current [DVSA inspection manual](https://www.gov.uk/guidance/mot-inspection-manual-for-private-passenger-and-light-commercial-vehicles) before stating a rule to an owner.

---

## Red lamps — stop or act now

### 1. Oil pressure

**id:** `oil-pressure`
**symbol:** old-fashioned oil can, sometimes with a drip
**colour:** red
**steady_or_flash:** either
**safety_class:** Red
**drive_advice:** Stop
**warnings:** W-HOT

**Symbol:** old-fashioned oil can, sometimes with a drip. **Colour:** red. Not shown on the electric board.

`safety_class: Red` · `drive_advice: Stop` · `warnings: W-HOT`

This is the most misunderstood lamp on the dashboard. It does **not** mean the oil is low — it means the oil is not being *pumped at pressure*. Unpressurised bearings can destroy an engine in well under a minute. The cost difference between stopping now and driving another mile is usually the difference between a repair and a new engine.

Stop as soon as it is safe, switch off immediately, and do not restart to reach a garage or get home. Arrange recovery.

**Owner can safely:** once the engine is completely cool, check the level on the dipstick. A correct level does not clear the meaning of the lamp and does not make the car safe to drive. Hot oil and hot engine parts cause serious burns.

**Tell the garage:** how long the lamp was on before stopping, whether the engine made any noise, when the oil was last changed.

**MOT:** no specific lamp check, but an engine that cannot safely run cannot complete a test.

---

### 2. Coolant temperature

**id:** `coolant-temp`
**symbol:** thermometer sitting in wavy liquid
**colour:** red when hot
**steady_or_flash:** either
**safety_class:** Red
**drive_advice:** Stop
**warnings:** W-HOT

**Symbol:** thermometer sitting in wavy liquid. **Colour:** red when hot. A **blue** version of the same symbol is engine-cold, not this id — ask colour before any Stop line.

`safety_class: Red` · `drive_advice: Stop` · `warnings: W-HOT`

The engine is overheating. Continuing risks a warped head or a failed head gasket, which is a four-figure repair on most cars. Stop, switch off, and let it cool.

**Never open the expansion tank or radiator cap while the system is hot.** It is pressurised, and the escaping coolant is above boiling point.

A **blue** version of the same symbol means the engine is still cold. That is informational only, not a fault.

**Owner can safely:** once fully cool — an hour or more — look at the coolant level in the expansion tank and look underneath for puddles. Note the colour of any leak.

**Tell the garage:** whether the temperature climbed gradually or spiked, whether the heater was blowing hot or cold, whether coolant has needed topping up recently, whether there was steam or a sweet smell.

**MOT:** not directly tested. A visible serious leak can fail.

**Related:** the existing guides `car-overheating-but-coolant-full` and `coolant-keeps-disappearing-no-leak` cover the follow-up.

---

### 3. Brake system

**id:** `brake-system`
**symbol:** exclamation mark inside a circle, inside brackets. Some cars spell out `BRAKE`
**colour:** red
**steady_or_flash:** either
**safety_class:** Red
**drive_advice:** Stop only after parking brake / EPB / Auto Hold is fully off and the lamp stays on; YesWithCare until then unless they already reported a spongy pedal, a pull, or a leak
**warnings:** W-SUPPORT

**Symbol:** exclamation mark inside a circle, inside brackets. Some cars spell out `BRAKE`. **Colour:** red.

`safety_class: Red` · `drive_advice:` conditional Stop · `warnings: W-SUPPORT`

**Check the parking brake / EPB / Auto Hold first.** A partially applied parking brake is the most common cause. Electronic parking brakes can also fail to fully release.

If it is fully off and the lamp stays on, or they already reported a long/spongy pedal, a pull, or fluid at a wheel, treat it as a hydraulic fault. **Drive advice:** do not drive it in; arrange recovery.

**MOT:** a brake-fluid warning can be Minor in the current manual. Do not say Expect a fail. Gate on whether the lamp applies; link the DVSA manual.

**Owner can safely:** look at the brake fluid level *through* the translucent reservoir. Do not remove the cap — contaminated or aerated fluid is worse than no inspection. Below the MIN mark means stop.

**Topping up is not a repair.** Fluid does not evaporate. If the level dropped, it either leaked out or the pads have worn far enough to move it. Both need a mechanic.

**No owner repair.** Brake hydraulics, bleeding and ABS bleeding all require professional verification that cannot be done on a driveway.

**Tell the garage:** whether the pedal feels soft, spongy, or travels further than usual; whether the car pulls to one side under braking; whether there is any fluid on the inside of a wheel.

**MOT:** a brake warning lamp indicating a fault is a testable defect where the lamp applies.

**Related:** `brake-pedal-spongy-or-goes-to-floor`.

---

### 4. Airbag / SRS

**id:** `airbag-srs`
**symbol:** seated person with a large circle in front of them
**colour:** red
**steady_or_flash:** either
**safety_class:** Red
**drive_advice:** Limited
**warnings:** W-ELECTRICAL (srs)

**Symbol:** seated person with a large circle in front of them. **Colour:** red.

`safety_class: Red` · `drive_advice: Limited` · `warnings: W-ELECTRICAL (srs)`

The car drives normally, so this one gets ignored — but the supplementary restraint system has faulted, and in a collision the airbags and seat-belt pretensioners may not fire. Occasionally the risk runs the other way and a component fires when it should not.

Drive it to get it fixed. Do not treat it as something to deal with next year.

**Absolutely no owner work.** Airbag modules and pretensioners are pyrotechnic devices governed by explosives regulations. Do not probe SRS wiring, disconnect modules, or work under seats where an SRS connector lives. There are no publishable steps for this system.

**Owner can safely:** nothing beyond noting when the lamp appeared. If it started right after a seat was moved, a seat cover was fitted, or something heavy was dropped in a footwell, mention that — connectors under the seats are a common trigger.

**Tell the garage:** exactly when it started and what happened just before; whether the car has ever been in a collision; whether any seat, belt or trim work has been done.

**MOT:** an SRS lamp indicating a fault is a listed Major where that check applies. Do not say Expect a fail. Verify first-use / whether the lamp applies against the DVSA manual.

---

### 5. Power steering

**id:** `power-steering`
**symbol:** steering wheel with an exclamation mark beside it
**colour:** red or amber depending on the car
**steady_or_flash:** either
**safety_class:** Red
**drive_advice:** Limited, escalating to Stop
**warnings:** none

**Symbol:** steering wheel with an exclamation mark beside it. **Colour:** red or amber depending on the car.

`safety_class: Red` · `drive_advice: Limited, escalating to Stop` · `warnings: none`

**If the steering has physically gone heavy, stop.** Loss of assistance is manageable at speed but dangerous at junctions, in car parks and during any sudden avoidance. The steering still works mechanically on most cars, but it needs far more force than a driver expects.

If the lamp is on and the steering still feels normal, that is limited driving: get it looked at, don't plan journeys.

**Check for a shared belt.** On many engines one auxiliary belt drives the steering pump, the alternator and the water pump. If the charging lamp or the temperature gauge is also doing something unusual, the belt is the likely common cause — and that combination means stop, not continue.

**Owner can safely:** note whether it is heavy all the time, only when cold, or only at parking speed. On hydraulic systems, look for fluid level and leaks. Most modern cars are electric and have nothing to check.

**Tell the garage:** heavy in both directions or one; any whine when turning; whether the charging lamp or temperature gauge also changed.

**MOT:** a power steering malfunction lamp is a testable defect where the lamp applies.

---

## Amber lamps — investigate

### 6. Engine management, steady

**id:** `engine-steady`
**symbol:** engine block outline
**colour:** amber
**steady_or_flash:** steady
**safety_class:** Amber
**drive_advice:** YesWithCare
**warnings:** none

**Symbol:** engine block outline. **Colour:** amber. **Behaviour:** steady. Drawn once as cell 6; flashing is spoken as 7. Ghosted on the electric board.

Do not treat a pick of 6 as steady until they have said it is not flashing.

**MOT:** listed as a Major MIL item only where first-use and fuel put the car in scope (petrol cars from 1 July 2003; diesel from 1 July 2008). Pure EV: not an engine-MIL fail item. Never copy "Expect a fail." See SKILL Step 4.

`safety_class: Amber` · `drive_advice: YesWithCare` · `warnings: none`

The engine control unit has stored a fault. Steady, with the car driving normally, generally means drive with care and get the code read within days rather than weeks.

The lamp itself says nothing about *which* fault — that is the honest answer, and the reason a scan is the correct next step here rather than a guess. This is one of the few lamps where reading a code genuinely changes what happens next.

**Escalation:** if it starts flashing, see entry 7 and stop.

**Owner can safely:** check the fuel cap is properly seated and clicked — a loose cap can trigger an evaporative-system fault on many cars. Note whether performance, economy or starting has changed.

**Tell the garage:** ask them to read the stored code *and the freeze frame* before replacing anything, and ask whether the diagnostic fee comes off the repair.

**MOT:** gate on first-use and fuel (SKILL Step 4). Clearing the lamp without repair is not a fix.

**Existing guide:** `engine-management-light`.

---

### 7. Engine management, flashing

**id:** `engine-flashing`
**symbol:** same engine outline
**colour:** amber
**steady_or_flash:** flashing
**safety_class:** Red
**drive_advice:** Stop
**warnings:** W-HOT

**Symbol:** same engine outline. **Behaviour:** flashing, usually with juddering. Not shown on the electric board.

`safety_class: Red` · `drive_advice: Stop` · `warnings: W-HOT`

A flashing **engine-block** outline while running is a severe running fault that can damage aftertreatment. Word it that way — not "it is a misfire / it is the cat." Key-on bulb-check flashes are not this id.

On diesel, a flashing **coil** is id 13, not 7.

**Tell the garage:** read the stored code before ordering parts. The lamp does not name the cylinder.

**MOT:** same first-use gate as entry 6.

**Existing guide:** `engine-management-light-flashing-and-car-juddering`.

---

### 8. Battery / charging

**id:** `battery-charging`
**symbol:** battery with + and - terminals
**colour:** red on most cars, but the urgency behaves like amber
**steady_or_flash:** either
**safety_class:** Amber
**drive_advice:** Limited
**warnings:** W-ELECTRICAL (battery12)

**Symbol:** battery with + and - terminals. **Colour:** red on most cars, but the urgency behaves like amber.

`safety_class: Amber` · `drive_advice: Limited` · `warnings: W-ELECTRICAL (battery12)`

Despite the symbol, this almost never means the battery needs replacing. Lit with the engine running, it means the charging system is not keeping up — usually the alternator, the drive belt, or the wiring between them. The car is running on stored charge and will eventually stop, possibly without warning. On an EV or hybrid this is still the 12V charging lamp, not traction-battery state of charge. Plug, lightning-bolt pack, or a message that says high-voltage is unmatched EV, not 8.

Turn off heated screens, heated seats, air conditioning and anything else non-essential, and get it somewhere it can be left.

**Escalate to Stop** on ICE if the temperature gauge starts rising, the steering goes heavy, or you hear a belt noise — one belt may drive all three. **Skip that belt combo on an electric car.**

**Tell the garage:** charging voltage at idle and at raised revs (ICE), or 12V / DC-DC health (EV/hybrid), before any battery is sold.

**MOT:** the battery lamp itself is not a specific test item, but low voltage can trigger ABS, SRS and emissions lamps which are.

**Existing guide:** `battery-light-on-while-driving`.

---

### 9. Diesel particulate filter

**id:** `dpf`
**symbol:** exhaust box emitting dots
**colour:** amber
**steady_or_flash:** either
**safety_class:** Amber
**drive_advice:** Limited
**warnings:** W-CO

**Symbol:** exhaust box emitting dots. **Colour:** amber. **Diesel DPF only.** Ghosted on petrol/hybrid/electric boards. A petrol exhaust-dots lamp is unmatched GPF — do not use this entry or regen copy.

`safety_class: Amber` · `drive_advice: Limited` · `warnings: W-CO`

The filter is not clearing its soot load. On a steady amber lamp with the car driving normally, one correct regeneration drive — at the speed, gear and duration in the handbook — is the right first attempt.

**Do not keep repeating motorway runs** if the lamp flashes, a red warning appears, the car is in limp mode, or the oil level has risen above maximum. A rising oil level means fuel is diluting the oil and needs attention now, not another lap of the motorway.

**Never run the engine to regenerate in an enclosed space.** Exhaust gas in a garage or workshop is a carbon monoxide risk.

**Owner can safely:** check the oil level, and read the handbook's regeneration procedure for that specific car.

**Tell the garage:** soot load and differential pressure readings, not just a code. Do not offer soot-vs-ash as a closed repair path.

**MOT:** a missing factory DPF can be a Major where one was fitted. Do not say Expect a fail from this lamp alone.

**Existing guide:** `dpf-light-wont-go-off-after-driving`.

---

### 10. Tyre pressure monitoring

**id:** `tyre-pressure`
**symbol:** horseshoe-shaped tyre cross-section with an exclamation mark
**colour:** amber
**steady_or_flash:** either
**safety_class:** Green
**drive_advice:** YesWithCare
**warnings:** none

**Symbol:** horseshoe-shaped tyre cross-section with an exclamation mark. **Colour:** amber.

`safety_class: Green` · `drive_advice: YesWithCare` · `warnings: none`

Usually exactly what it says: one or more tyres are below the target pressure. This is the one lamp where the owner can reliably fix the cause themselves.

**Behaviour matters here.** A lamp that flashes for roughly a minute at startup and then stays steady normally indicates a *system* fault — a dead sensor battery or a sensor not paired — rather than a low tyre.

**Owner can safely:** check all four pressures cold against the placard in the driver's door sill or the fuel flap, not against the number moulded on the tyre. Inspect for a nail or a bulge. Reset the system per the handbook after inflating.

**Tell the garage:** if pressures are correct and it persists, read sensor IDs and battery status. Do not guess that a sensor battery has died.

**MOT:** TPMS inspection is for M1 first used on or after 1 January 2012. A lamp that only means inflate the tyre is not automatically a malfunction fail. Flash-then-steady is the usual malfunction pattern. Pre-2012: do not call this a testable MOT lamp item.

**Existing guide:** `tyre-pressure-light`.

---

### 11. ABS

**id:** `abs`
**symbol:** `ABS` inside a circle with brackets
**colour:** amber
**steady_or_flash:** either
**safety_class:** Amber
**drive_advice:** Limited
**warnings:** W-SUPPORT

**Symbol:** `ABS` inside a circle with brackets. **Colour:** amber.

`safety_class: Amber` · `drive_advice: Limited` · `warnings: W-SUPPORT`

The normal brakes still work. Anti-lock does not. Under hard braking on a wet, loose or icy surface the wheels can lock and the car will slide instead of steering. On many cars the ABS fault also disables stability control and hill-hold.

Drive gently and directly to a garage. Leave extra stopping distance and avoid heavy braking.

**No owner repair on ABS hydraulics.**

**Owner can safely:** note whether the lamp appeared together with the brake lamp or the stability lamp, and whether it comes and goes at a particular speed.

**Tell the garage:** which wheel the scan reports. Do not offer sensor / reluctor / wiring as a closed list.

**MOT:** an ABS lamp indicating a malfunction is a listed Major where ABS is required. Do not say Expect a fail. Verify against the current manual.

---

### 12. Stability / traction control

**id:** `esc-traction`
**symbol:** car with wavy skid lines behind it
**colour:** amber
**steady_or_flash:** normal-flash-vs-steady-fault
**safety_class:** Amber
**drive_advice:** YesWithCare
**warnings:** none

**Symbol:** car with wavy skid lines behind it. **Colour:** amber. This id is the **skid-lines** shape only. A car-with-! and no tracks on an EV is unmatched EV, not this lamp.

`safety_class: Amber` · `drive_advice: YesWithCare` · `warnings: none`

This lamp is misread more often than any other, because flashing and steady mean opposite things.

**Flashing while driving is normal.** It means the system is actively intervening because a wheel is slipping. Ease off. Nothing is broken.

**Steady means the system is off or faulty.** Check first whether someone has pressed the traction control button — often a small button with the same symbol. If it has not been switched off, there is a fault, and it commonly shares a root cause with an ABS fault since both rely on the wheel speed sensors.

**Owner can safely:** press the button to confirm the system toggles, and note whether the ABS lamp is also on.

**Tell the garage:** whether both lamps are lit, and whether it started after a wheel, tyre or suspension job.

**MOT:** a stability control lamp indicating a fault is testable where the system applies.

---

### 13. Glow plug / preheat

**id:** `glow-plug`
**symbol:** coiled spiral, like a loose spring
**colour:** amber
**steady_or_flash:** ignition-cycle-is-normal
**safety_class:** Amber
**drive_advice:** YesWithCare
**warnings:** none

**Symbol:** coiled spiral, like a loose spring. **Colour:** amber. **Diesel only.** Not shown on petrol/hybrid/electric boards.

`safety_class: Amber` · `drive_advice: YesWithCare` · `warnings: none`

**Coming on with the ignition and going out after a few seconds is normal.** That is the preheat cycle. It is not a fault. If they picked 13 and it went out, stop — no garage card.

It matters when it does something else:

- **Stays on after the engine has started** — a preheat system fault.
- **Flashes** — on many diesels this is engine-management, not a preheat-system story. Ask judder, power, smoke. If those are present, grade Stop like 7; if the car is driving normally, Limited and get codes. Do not reuse petrol cat-fire copy. Do not tell them they should have picked 7.

**Ask the garage:** read engine codes. Do not promise what the code will say.

**MOT:** not a specific lamp check on most vehicles. Excess smoke and emissions failures are separate test items.

---

## Not faults

Blue and green symbols report status: main beam, indicators, cruise control, fog lamps, engine cold.

Name the status function. One check (beam/fog/cruise off → lamp out; engine warmed → blue thermometer out). Ask if any **circled** lamp is also on. If not, a short "not a fault" note — not a garage card.

A **blue** thermometer is not id 2. Ask colour before any coolant Stop line.

## When the description does not match

Do not pick the closest of the 13. Split:

- named blue/green → Not faults
- number not printed on this fuel picture → keep this board; unknown only if they say none of these shapes
- AdBlue / GPF / EV turtle / car-with-! / charge plug → unmatched path in `references/boards.md`, still a thinner statement
- else → cluster photo or handbook symbol
