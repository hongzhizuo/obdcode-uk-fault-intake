# 18 · One handbook regen (diesel DPF, steady, driving normally)

Not a second SKILL. If this note disagrees with `SKILL.md`, `references/prognosis.md`, `references/prognosis-cards.md`, or `references/warning-lights.md`, those win. Do not diagnose. Do not invent pounds. Do not add a 14th lamp id.

Allowed **Close it yourself** on diesel lamp **9** (`dpf`) when the lamp is **steady** and the car is **driving normally**: **one** regeneration drive. Speed, gear, and duration come from **that car’s handbook** — not a generic motorway recipe in this file.

This is **not** a scan-tool forced regen. This is **not** petrol / hybrid GPF. This is **not** an enclosed-space idle burn.

The lamp card is `09-dpf.md`. Forced-regen and code-clear bans live in `26-never-clear-never-forced-regen.md`. GPF scan steps live in `14-gpf-unmatched.md` and `21-device-scan-steps.md`.

## When

Run these steps only when **all** of the following are true:

- Board is **diesel** (including diesel hybrid, and **your Transit** on the diesel picture).
- They picked **9**, or named the exhaust box with dots as the diesel particulate filter.
- The lamp is **steady amber**.
- The car is **driving normally** (no limp, no flash, no red warning, oil not over maximum).
- Outlook is good (`owner`). Close-it-yourself needs that good outlook.

Do **not** run this sequence when:

| Facts | What to do instead |
|---|---|
| Petrol or hybrid + exhaust-dots, or pick of 9 on a petrol / hybrid board | Unmatched GPF. Scan. **No** handbook regen copy. Do not switch board. |
| AdBlue / urea / DEF | Unmatched AdBlue. Not 9. |
| Flash, limp, a red warning, or oil over maximum | `poor` on the DPF card. **No more** motorway loops. Do not drive it in — arrange recovery. |
| They ask for a forced / service / parked / scan-tool regen | Refuse. That is not an owner job. |
| One handbook attempt already failed and the lamp stayed | Garage. Call `dpf-cleaning-cost`. Do not loop. |
| They want the filter cut out | Refuse. No how-to. Value-gain **Negative** if they asked sale effect. |

Vans: same one-count rule. Say **your Transit**. A handbook regen is not “a day off the road.”

Drive advice on this branch stays **Limited** (drive directly; no extra journeys). The regen drive **is** that one allowed journey when the handbook says to do it. `warnings:` **W-CO**.

## Owner copy

Spoken **[Close it]** after the statement. Keep the whole outlook under 120 words. No ids, no plates, no URLs, no pounds, no invented mph / gear / minutes.

Close it yourself. Check the oil. Then one regeneration drive exactly as this car’s handbook says — that book’s speed, gear, and duration, not a generic motorway loop. Do it in the open. Never regenerate in a garage, workshop, or any enclosed space: exhaust gas is a carbon monoxide risk. Do not force a regen with a scan tool. Do not clear the lamp. If the lamp stays after that one attempt, a garage can usually handle it.

(~90 words.)

Spoken labels on this branch: **[Outlook]** Close it yourself. **[Close it]** the lines above. **[Repair]** only if the lamp stays — then `dpf-cleaning-cost` (headline, or we publish no figure — two written estimates). Omit **[Sell]**.

If they ask what is wrong: this skill does not diagnose. If they ask keep-driving or repair-vs-sell: restate **[Drive advice]** and **[Outlook]**.

## The one count

1. **Oil level.** Owner-safe look. Over maximum ends this path — that is the `poor` branch, not another drive.
2. **Open this car’s handbook.** Use the regeneration procedure printed for **this** make and model. Do not invent 40–60 mph, a gear, or a time from this file or from another car.
3. **One drive** at that handbook speed, gear, and duration. Outdoors. Not in an enclosed garage or workshop (carbon monoxide).
4. **Stop at one.** If the lamp remains, garage. Do not keep repeating motorway runs.
5. **Do not** clear the lamp. **Do not** run a scan-tool forced regen. A small reader does not close this lamp.

“No more motorway loops” applies after flash / limp / red warning / oil over maximum — or after this **one** handbook attempt has already failed. It is not a ban on that single handbook drive.

## Not this file

- **Not enclosed space.** Never idle or “regenerate” in a garage, workshop, or any enclosed space.
- **Not scan-tool regen.** No menus, parked service burns, temperatures, or “use the scanner to burn it.” Garage speech is soot load and differential pressure, not a forced-regen script.
- **Not petrol GPF.** Exhaust-dots on petrol / hybrid is unmatched GPF: stored codes and freeze frame, written down, not cleared. No diesel regen copy.
- **Not a diagnosis.** Do not say soot-loaded versus ash-loaded, “blocked DPF,” or a named sensor.
- **Not a delete.** Never “just cut it out.”
- **Not a device path.** Handbook regen is `owner`, not `device`.

## Slugs

This close does **not** call a slug. If the one count fails and speech moves to garage, call **only** `dpf-cleaning-cost` (often `gbp: null` — still call it; still say we publish no figure). There is no published DPF-replace slug. Do not call `car-diagnostic-test-cost` on diesel DPF. Do not invent a filter price.

## Red lines

1. Speed, gear, and duration from **that** handbook only. No generic recipe in speech or in this file.
2. **One** attempt. Then garage if it stays.
3. Never enclosed-space regen (W-CO).
4. Never scan-tool forced regen — not even as “tell the garage to run one.”
5. Never petrol / hybrid GPF regen copy. Do not switch board.
6. Never clear the lamp as a fix.
7. Never diagnose (soot vs ash, blocked filter, named part).
8. Never invent pounds. Never print a plate. Worked speech is **your 2016 Fiesta** / **your Transit**.
9. Never instruct delete, remap, or cutting the filter out.
10. Safety before commerce. No scanner or shop link above **[Drive advice]**.
11. Do not map AdBlue to 9. Do not add a 14th lamp id.
12. MOT: do not say “Expect a fail” from this lamp alone. A missing factory DPF can be a Major where one was fitted — link the [DVSA inspection manual](https://www.gov.uk/guidance/mot-inspection-manual-for-private-passenger-and-light-commercial-vehicles).

## Pass / fail

**Pass**

- Diesel 9, steady, driving normally: “Close it yourself. One handbook regen. Speed, gear, and duration from this car’s handbook.”
- Oil check first. In the open. Never in an enclosed garage or workshop.
- “Not a scan-tool forced regen. Do not clear the lamp.”
- One count only. Lamp stays → garage; call `dpf-cleaning-cost`; headline or “we publish no figure — two written estimates.” No **[Sell]** on this branch.
- Petrol / hybrid exhaust-dots or pick of 9: unmatched GPF. Scan. No regen copy. Keep that board.
- Flash / limp / red warning / oil over maximum: no more loops; recovery. This file does not apply.
- “The lamp does not name the part.” Ask the garage for soot load and differential pressure.
- Van: **your Transit**. Same one handbook count.

**Fail**

- “Do 20 minutes at 50 mph in fourth” (or any speed / gear / time not taken from **that** handbook).
- Regen in a garage, workshop, or any enclosed space.
- Scan-tool forced / service / parked regen steps, or “burn it with a reader.”
- Handbook or motorway regen copy on petrol / hybrid GPF.
- A second or third “just try another motorway run” after the one count, or after flash / limp / oil over max.
- “It’s soot-loaded / ash-loaded / the DPF is blocked.”
- “Clear the code and the lamp will go out.”
- “Just cut it out” / delete how-to.
- Invented GBP (cleaning range, replacement-filter price, trade-in).
- Calling `car-diagnostic-test-cost` or a cat / clutch slug because this lamp is on.
- Mapping AdBlue to 9, or treating pick of 9 on petrol as diesel DPF.
- “Expect a fail.”
- A real registration in this file or in speech.
