# 20 · Owner-close list

Not a second SKILL. If this note disagrees with `SKILL.md`, `references/prognosis.md`, or `references/prognosis-cards.md`, those three win. Do not diagnose. Do not invent pounds. Do not add a 14th lamp id.

This is the **`owner`** allowlist for **Close it yourself**. Scan-tool steps live in `21-device-scan-steps.md`. Speech maps `owner` (and `device`) to **Close it yourself**.

## Gate

Close it yourself is allowed only when **both** are true:

1. Outlook is good (not `poor`)
2. The card is `owner` — Green / handbook / a fluid that is meant to be topped up — **or** the extra check below on an already-allowed `device` path

A reader does **not** move a Red-class lamp onto this list. Do not clear codes. Do not force a DPF regen with a scan tool.

## Allowed

Five owner-safe closes. Nothing else on this list.

| Close | When | What they do | If it stays |
|---|---|---|---|
| **TPMS inflate** | Lamp 10 **simply on** | Cold pressures to the **door-sill or fuel-flap placard**, not the sidewall. Inspect for a nail or a bulge. Handbook reset. No scan-tool clear | That *is* the close |
| **TPMS inflate first** | Lamp 10 **flash then steady** (~1 minute at startup) | Same pressure check | Not the close. Then **garage**. No figure |
| **AdBlue top-up** | Unmatched AdBlue / urea / DEF, **level low**, car still starts | Correct fluid only, **handbook filler**. Not lamp 9 or 6. No water. No tank-reset DIY | That *is* the close |
| **One handbook DPF regen** | Diesel lamp 9 **steady**, driving normally | **One** regen at the speed, gear, and duration in **that** handbook. Oil-level check. Never in an enclosed space | Then **garage**. Call `dpf-cleaning-cost` (often null) |
| **ESC button** | Lamp 12 **steady** | Traction / ESC **button** only — often the same skid-lines symbol. Confirm it toggles | Button was off and the lamp clears → **skip** (not a fault). Not switched off and still on → **garage**. No figure |
| **Fuel cap (extra check)** | Lamp 6 **engine-steady** only (they have said it is **not** flashing) | Fuel cap clicked fully tight. Then the **device** sequence: stored codes **and** freeze frame, written down, **not** cleared | Cap alone does not close the lamp. No reader → garage diagnostic |

GPF is not on this list. Petrol / hybrid exhaust-dots is **scan**, not a diesel regen.

Vans: same list. Say “your Transit”.

## Not on this list

These never become a driveway close. A reader does not fix them either.

| Path | Why it is out |
|---|---|
| `oil-pressure` (1) | Red-class. Cold dipstick is **information**, not a close. Do not top up and drive |
| `coolant-temp` red (2) | Red-class. Cold tank / floor glance is **information**, not a close. Never open a hot cap |
| `brake-system` hydraulic (3) | Red-class. No bleeding, pads, or lifting |
| `airbag-srs` (4) | No. No scan-clear. No clock-spring DIY |
| `engine-flashing` (7) | Red-class. No fuel-cap close. No reader close |
| AdBlue **remaining-starts / no-start** | `poor`. Recovery or collection. No published slug |
| DPF **flash / limp / oil over max** | `poor`. No more motorway loops. No scan-tool regen |
| ESC **flashing while driving** | Skip. The system is working. Not a close |
| Power-steering reservoir glance | Information, not a close |
| ABS (11), charging (8), glow stays on (13), EV turtle / HV | Garage (or `poor` where the card says). Not this list |

Do not upgrade `garage` or `poor` to this list because the car is old, or because a reader is on the shelf.

## Owner copy

Each line is a spoken **[Close it]** (or the first check, then garage). Keep the whole outlook under 120 words. No part names. No pounds.

**TPMS simply on:** Close it yourself. Check all four tyres cold against the placard on the driver’s door sill or the fuel flap, not the number moulded on the tyre. Look for a nail or a bulge. Inflate, then reset as the handbook says. Do not clear the lamp with a scan tool.

**AdBlue low:** Close it yourself. Use the correct AdBlue / urea / DEF in the handbook filler. Not water. This is not the DPF lamp and not the engine lamp.

**DPF steady, driving normally:** Close it yourself with **one** handbook regeneration. Check the oil. Do not regen in a garage or other enclosed space. If it flashes, goes into limp, or the oil is over maximum, stop repeating motorway runs — that is no longer a driveway close.

**ESC steady:** Check the traction button first. If someone had switched it off and the lamp goes out, it was not a fault. If it was not switched off and the lamp stays on, a garage can usually handle this. We publish no figure — two written estimates. Not a remap. Not a sensor DIY.

**Fuel cap (engine-steady only):** Click the fuel cap fully tight. That is the only extra driveway check on this lamp. Then scan: stored codes and freeze frame, written down, do not clear. A scan is the next step; the lamp does not name the part.

Spoken labels: **[Outlook]** Close it yourself, then **[Close it]**. No **[Sell]** on these branches. Fuel-cap speech sits on the `device` path; still no sell.

## Money

Owner closes do **not** call `repair_cost` as the close.

- TPMS / ESC / AdBlue low: allowlist **empty**. Do not hunt a nearby slug.
- DPF after one handbook regen fails: `dpf-cleaning-cost` on the **garage** follow-on (often `gbp: null` — that is the answer).
- Engine-steady if they will not scan: `car-diagnostic-test-cost` as the garage alternative, not as a named part.

Never invent GBP. Never treat a cost page as the failed part.

## Red lines

1. Not oil, hot coolant, hydraulic brakes, airbags, or a flashing engine lamp.
2. Never advise clearing codes or the lamp as a fix.
3. Never describe a scan-tool forced DPF regen. Never “just cut it out.”
4. Never copy diesel regen onto GPF.
5. Fuel cap is **engine-steady only**. It does not close flashing engine, GPF, DPF, AdBlue, or TPMS.
6. AdBlue is not 9 and not 6. No water. Top-up only on the low-level branch.
7. TPMS: placard, not sidewall. Flash-then-steady is not “inflate only.”
8. ESC close is the **button**. Not a sensor, module, or remap.
9. One handbook DPF regen, not a campaign of motorway loops. Never enclosed-space regen.
10. Information (cold dipstick, cold coolant glance) is not a close.
11. No invented pounds. No diagnosis. No real registration in this file or in speech.
12. Device and shop links stay **below** Stop / recovery. These owner paths are not Stop, but never put a shop link above **[Drive advice]**.

## Pass versus fail

- Pass: TPMS simply on → inflate to the **placard**, inspect, handbook reset. No scan-tool clear.
- Fail: “It’s a dead TPMS sensor.” / sidewall pressure / “clear it with a dongle.”
- Pass: Flash-then-steady → pressures first, then garage, no figure, no sell.
- Fail: Treating flash-then-steady as inflate-only, or skipping the pressure check.
- Pass: AdBlue low → correct fluid, handbook filler. Not 9 or 6.
- Fail: “Just add water.” / tank-reset DIY / mapping AdBlue to DPF or the engine lamp.
- Pass: Remaining-starts / no-start → weak outlook, collection, no published figure. Not a top-up close.
- Fail: “Fill it and it will start.”
- Pass: DPF steady and driving normally → **one** handbook regen. Oil check. Not enclosed. Not a scan-tool regen.
- Fail: Repeated motorway loops after flash / limp / oil over max. “Force regen with the reader.” GPF “do a diesel regen.”
- Pass: ESC steady → toggle the button first; then garage if it was not switched off.
- Fail: “It’s a wheel-speed sensor.” / remap / skipping the button.
- Pass: ESC flashing while driving → skip. Not a fault. Not this list.
- Pass: Engine-steady → fuel cap clicked **and** stored codes plus freeze frame, not cleared. Cap is the extra check, not the whole close.
- Fail: Fuel cap as the close for a flashing engine lamp. “Clear it and see.”
- Pass: Oil / red coolant / hydraulic brakes / airbag / flashing engine → **no** owner close. Restate Stop or garage. Dipstick or cold tank is information only.
- Fail: “Top up the oil and go.” / “Bleed the brakes on the drive.” / “Plug in a reader” as the close for those lamps.
- Pass: “A scan is the next step; the lamp does not name the part” on engine-steady.
- Fail: Naming lambda, cat, coil, soot-vs-ash, or any SAE J2012 definition as the close.
- Pass: Empty allowlist → we publish no figure. Two written estimates on the garage follow-on only.
- Fail: “About £80” / any guessed top-up, sensor, or regen fee with no tool result.
