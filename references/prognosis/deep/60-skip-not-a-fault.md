# 60 · Skip Step 6 — not a fault

Not a second SKILL. If this note disagrees with `SKILL.md`, `references/prognosis.md`, `references/prognosis-cards.md`, or `references/value-gain.md`, those four win. Do not diagnose. Do not invent pounds. Do not add a 14th lamp id.

Step 6 is repair-or-sell. Run it only on a **real fault**. When Step 5 already ended as not-a-fault, **skip Step 6**. Still **confirm the shape in one sentence**. Then stop. No garage card. No outlook.

Do not ask if they are driving.

## When

Skip Step 6 only after the facts match one of these five endings:

| Ending | What they saw | Confirm (one sentence) |
|---|---|---|
| Glow 13 went out | Coiled diesel lamp came on with ignition and went out after start | Preheat cycle — not a fault |
| Blue coolant went out | Thermometer was **blue**, then went out after a short run / as the engine warmed | Engine-cold mark — not a fault |
| Parking-brake brake lamp | Lamp 3 on, parking brake / EPB / Auto Hold **still on**, pedal **normal** | Brake mark with the parking brake applied — not a fault |
| ESC flashing while driving | Lamp 12 **skid-lines**, flashing in motion | System intervening — ease off; not a fault |
| Key-on bulb check that went out | Lamps lit with the key, then went out | Bulb check — not a fault |

SKILL Step 5 names the first four. `prognosis.md` also names the fifth. Treat all five as skip.

This note does not pick a bucket. There is no `owner` / `device` / `garage` / `poor` on these endings.

## Still confirm in one sentence

After a valid pick (or a unique named shape), **one sentence** to confirm what they matched. Do not skip the confirm because you are skipping outlook. Do not open `show_lamp` unless they hesitate. Do not list lamp names. Do not write the 60–80 word garage card. Do not continue to Step 6 in the same turn.

The sentence names the **shape** and that it is **not a fault**. Drive advice that is only “ease off” or “release the parking brake” may sit in that same sentence. Then stop.

Owner copy — one sentence each, then stop:

- **Glow went out:** That coiled lamp coming on with the key and going out after a few seconds is the diesel preheat cycle, not a fault.
- **Blue went out:** That blue thermometer is the engine-cold mark; it went out as the engine warmed, so it is not a fault.
- **Parking brake on, pedal normal:** That red circle-and-brackets mark is the brake lamp; with the parking brake still on and a normal pedal, it is not a fault.
- **ESC flashing while driving:** That amber car with wavy skid lines flashing while you drive is the system intervening — ease off; it is not a fault.
- **Key-on bulb check:** Those lamps lighting with the key and then going out is the bulb check, not a fault.

No **[Outlook]**. No **[Repair]**. No **[Sell]**. No **[Close it]**. No **[Ask the garage]**. No **[Book]** for the lamp. No `repair_cost`.

If they also named wrap / service / value work, the not-a-fault confirm still comes first. Then a separate **[Value]** block from `value-gain.md`. That is not Step 6.

## Classify first

Do not skip until the branch is known. Classification is not a driving quiz.

| If they named… | Ask once, if unknown |
|---|---|
| Glow / coiled 13 | Went out after start, stays on, or flashes |
| Thermometer / coolant / temp | **Blue or red**, then whether it went out |
| Brake lamp 3, parking brake not mentioned | Is the parking brake / EPB / Auto Hold **fully off**? Pedal normal? |
| ESC / skid-lines 12 | Flashing while driving, or steady |
| “Lights came on” at key-on | Did they go out after the ignition cycle, or stay on? |

Default since / symptoms to “just now / drives normally” only after a **real** fault is classified. Do not invent a garage visit to fill the gap.

Blue that is still on because the engine is still cold: one check — wait until it is warmed; the blue mark should go out. Still not id 2. Do not run red-coolant outlook.

ESC **steady**, traction button **was off**: skip once they turn it back on **and the lamp clears** (`prognosis-cards.md` lamp 12). If it stays on after the toggle, that is a real fault — run Step 6 on the ESC card, not this skip.

## Do not run Step 6

On a skip ending:

- Do not speak Close it yourself / A garage can usually handle this / Repair may cost more than the car
- Do not call any `repair_cost` slug
- Do not push a sell bid
- Do not give driveway plug-in, freeze-frame, or parts steps
- Do not diagnose why the lamp “came on”
- Do not invent pounds

A later question “so what is wrong?” still gets: this skill does not diagnose; that was not a fault. Do not then open outlook.

## These still run Step 6

Skip is narrow. Same lamps, different facts → real fault → statement **and** Step 6 in the **same turn**.

| Facts | Not this skip | Card |
|---|---|---|
| Glow **stays on** or **flashes** after start | Garage (Stop in drive advice if flashing plus judder / power loss / smoke) | `13-glow-plug.md` |
| Thermometer is **red**, or stays red after they said colour | `poor`, Stop | coolant-temp (red) |
| Parking brake / EPB / Auto Hold **fully off** and lamp 3 stays, **or** spongy pedal / pull / leak | `poor`, Stop | `03-brake-system.md` |
| ESC **steady**, not switched off (or stays after toggle) | `garage` | `12-esc-traction.md` |
| Lamp **stayed on** after the key-on check | Real fault on that lamp’s card | that lamp, not this file |
| Engine outline **flashing while running** | `poor`, Stop — not a bulb check | `07-engine-flashing.md` |

Key-on bulb check is only the ignition self-test that **went out**. A lamp that came on **while driving** and then went out is not this skip, except ESC flashing in motion and a **blue** thermometer that went out as it warmed.

Do not treat glow-went-out as a bulb-check of oil, brakes, or engine. Confirm the **coil**. Do not switch them to lamp 7.

Do not treat blue as red. Ask colour before any coolant Stop line.

Do not treat ESC flashing as a garage job. Do not map EV car-with-! and no skid lines to 12.

## Red lines

1. Skip Step 6 on the five endings above. Do not “just give a small outlook anyway.”
2. Still confirm the shape in **one sentence**. Do not skip the confirm. Do not list names.
3. No garage card, no `repair_cost`, no invented pounds, no diagnosis.
4. Classify first. Parking-brake off, blue vs red, glow behaviour, ESC flash vs steady, bulb-check vs stayed on.
5. Do not ask if they are driving.
6. Do not print a plate. “Your 2016 Fiesta” / “your Transit” only.
7. Do not say Expect a fail. A not-a-fault lamp is not an MOT item.
8. Do not clear a lamp. There is nothing to clear on these endings.
9. Safety still precedes shop links. These endings have no shop links.

## Pass versus fail

- Pass: glow 13 on with ignition then out → one sentence, preheat, not a fault, no Step 6.
- Fail: glow went out → garage card, `car-diagnostic-test-cost`, or “your plugs are failing.”
- Pass: blue thermometer that went out → one sentence, engine-cold, not a fault.
- Fail: treating blue that went out as red coolant `poor` / head-gasket outlook.
- Pass: “is that thermometer blue or red?” before any coolant Stop line.
- Fail: Stop / recovery on a blue mark.
- Pass: parking brake still on, pedal normal → one sentence, not a fault, no Step 6.
- Fail: repair-or-sell while the handbrake is still on and the pedal is normal.
- Pass: “is the parking brake, EPB, or Auto Hold fully off?”
- Fail: “are you still driving?”
- Pass: parking brake off and lamp 3 stays, or spongy / pull / leak → do **not** skip; `poor`, Stop.
- Fail: calling that hydraulic Stop “not a fault.”
- Pass: ESC skid-lines flashing while driving → one sentence, ease off, not a fault, no Step 6.
- Fail: flashing-in-motion as a garage job, sensor guess, or remap.
- Pass: ESC steady, not switched off → run Step 6 on the ESC card.
- Fail: skipping outlook on a steady ESC lamp that did not clear.
- Pass: key-on bulb check that went out (oil-can, ABS, engine outline, any shape) → one sentence, not a fault, no Step 6.
- Fail: oil-can bulb check that went out → weak-outlook rebuild / sell speech.
- Pass: engine outline flashing **while running** → Step 6 on lamp 7, Stop.
- Fail: calling a running flash a bulb check, or calling a bulb-check flash lamp 7.
- Pass: one-sentence shape confirm, then stop.
- Fail: skipping the confirm, or a full garage card with Ask the garage / Book / Outlook on a skip ending.
- Pass: “this skill does not diagnose” if they then ask what part it was.
- Fail: naming glow plugs, a sender, a wheel-speed sensor, or a gasket after a skip.
- Pass: no `repair_cost` and no pounds on a skip ending.
- Fail: “about £80 to get it checked anyway.”
- Pass: wrap named as well → not-a-fault sentence, then a separate **[Value]** block; still no Step 6.
- Fail: opening Close it yourself / garage / sell because they also asked about a wrap.
