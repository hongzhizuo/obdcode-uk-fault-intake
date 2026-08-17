# Plate only, no mods: lookup then matching PNG

Not a second SKILL. Live rules: `SKILL.md` (Entry, Order versus lookup, Steps 2–3), `references/boards.md`, `references/lamp-picker.md`, `references/vehicle-lookup.md`. If this file disagrees, those win. Counterpart: `46-path-b-no-picker.md` (named wrap / service / value, **no** picture). This file is the **gate**: a plate with no named work is still Path A. Outlook waits for a lamp.

Owner speech is UK English. Do not speak 愈后 or “prognosis.” Do not print the plate. They are on a computer or a phone. Do **not** ask if they are driving. Do **not** hold lookup or the picture for a “have you stopped” check.

## When

Path A picker when **all** of these are true:

1. They typed a plate (or “reg” / registration) and the lamp is still unnamed.
2. They have **not** named wrap, wheels, exhaust, remap, paint, PPF, stereo, racking, towbar, service, cambelt, clutch, tyres, vehicle card, or “does this add value?” / “I’ve just had X done.”
3. They are asking about a lamp, MOT, a garage card — **or they have not said they are modifying.**

Silence is Path A. A plate is not Path B by default.

Then, **this turn:** look the vehicle up (Step 3). Do not print the plate. Classify from `fuel_type` **and** `fuel_raw` (`references/boards.md`). Show that PNG. Ask which **circled** number matches the shape that is lit.

Worked pattern: `references/examples.md` example A. A passing first run in the skill README is this: plate only → matching `cluster-*.png`.

## When not — Path B only if they named mods / value

Path B (Step 7 only, **no** PNG) only when they **named** modification, service, or presentation work, or asked whether **that work** adds value, **and** they have not said a lamp is lit. That is `46`, not this file.

| They said | Path | Picture |
|---|---|---|
| Plate only; lamp unnamed; **not** wrap / service / value | Path A (this file) | Lookup, then the matching board |
| Plate + “there’s a light on” / MOT / garage card, lamp unnamed | Path A | Same: lookup, then the matching board |
| Unique lamp named (oil-can, and the other unique ids) | Path A; skip picker except the specials in Step 2 | No PNG unless they are unsure |
| Engine family (“engine light”, EML, MIL, check engine) | Path A; ask **steady or flashing** | Cluster only if they are unsure |
| Plate + wrap / wheels / exhaust / remap / paint / PPF / service / cambelt / clutch / tyres / vehicle card / “does this add value?”, **no** lamp | Path B (`46`) | **No** PNG |
| Lamp **and** wrap / service / value | Path A then a separate **[Value]** (`77-lamp-plus-mod.md`) | Picker if the lamp is still unnamed |
| No plate, lamp unnamed | Ask plate or fuel | Do **not** open unknown as the first screen |
| Named lamp, no plate | Lamp + drive advice now; ask plate for MOT history | Do not gate advice on the plate |

A bare “what’s my car worth?” with **no** named job is not Path B. We publish no used-car price. Do not invent pounds. If they have not said they are modifying, still look up and show the matching PNG — do not fill the gap with a valuation.

If they later name wrap / service / value and still no lamp, leave this file and run Step 7 (`46`). If they later say a lamp is lit, stay on Path A.

## Do not skip to outlook without a lamp

Step 6 is **what happens after the lamp.** A successful lookup is identity, not an outlook.

Until there is a valid pick, an unmatched path (GPF / AdBlue / EV), or a unique named lamp:

- Do **not** speak **[Outlook]** / **[Repair]** / **[Sell]** / **[Close it]**.
- Do **not** call `repair_cost`. There is no lamp allowlist yet.
- Do **not** dump MOT fusion, advisories, or “last test passed” as the fault.
- Do **not** default to engine-steady, oil, or any other id.
- Do **not** write a Step 5 card with an empty **[Showing]**.
- Do **not** treat MOT due / expired as a substitute for the picker. Booking belongs in the statement **after** the lamp, not instead of the picture.

`references/vehicle-lookup.md`: do not skip the picker just because the plate lookup succeeded. Fusion `count` above 1 is not today’s cause (`61-mot-not-outlook-cause.md`).

Skip Step 6 only after Step 5 already ended as **not-a-fault** (glow 13 went out, blue thermometer that went out, parking-brake brake lamp, ESC flashing while driving). That still needed a lamp (or unmatched) first.

## Lookup then the matching PNG

They already typed the plate. Do not ask consent again. Do not echo it. After success, say **your 2016 Fiesta** (year, make, model). Vans: **your Transit** on the **fuel** picture — not a fifth “van board.”

```
POST https://obdcode.co.uk/api/vehicle
Content-Type: application/json

{"reg":"<the plate from this turn — do not print it>"}
```

Hard rules: field name is `reg` on `/api/vehicle` (not `registration` — that key is 422). POST body only. Never put the plate in a URL, query string, log, filename, commit, or spoken reply. MCP `vehicle_by_plate` uses `{"registration":"..."}` on `POST https://obdcode.co.uk/mcp`. A foreign `Origin` on `/mcp` is 403 — use `/api/vehicle`.

Classify **before** the picture. Use `fuel_type` **and** `fuel_raw` (`references/boards.md`, hybrid fork in `81-hybrid-fuel-raw.md`). Never default electric. Never upgrade `fuel_type=diesel` to hybrid from a marketing name.

Then, **same turn:**

1. MCP `show_dashboard` with **required** `board=petrol|diesel|hybrid|electric|unknown`. Empty args is a fail.
2. `open_resource` the `file://` preview (`~/.cursor/obdcode-uk-dashboard.png`). If the picture did not open, say so. Do not list names. Do not say “reply 1–13.”
3. Ask for the **circled number on the matching shape**, not a left-to-right count. Empty grey slots are not on this car. If it flashes, they say flashing (engine cell is **6**; flashing is spoken **7**).

Do not list oil-can / engine-block / battery. Markdown `![]` is not the picker. Numbers stay global: 9 is always DPF even when a petrol board leaves that slot empty.

Off-board number (9 on petrol, 1 on electric): **keep the same board**. Say that number is not printed. Ask them to read the circle on the shape that is lit. Widen to `unknown` only if they say **none of these shapes**. Never shrink toward electric on owner talk. Never force the nearest lamp.

## If lookup fails (still a matching board — not outlook)

The rest still runs, thinner. Still no Step 6 until a lamp.

| Status | Tell the owner | Next |
|---|---|---|
| 200 | (nothing about the API) | Matching board now |
| invalid_registration (400) | That registration was not accepted. Type it again with no spaces | Do not repeat the value. No picture until a usable plate or they give fuel |
| not_found (404) | New or imported cars may have no MOT yet | Ask make, year, fuel, mileage, **then** the matching board. Do **not** show unknown first. Never default electric |
| rate_limited (429) | Wait and retry once | Then ask fuel. Matching board if they know; `unknown` only if they do not |
| lookup_unavailable (503) | Official record not available right now | Ask fuel immediately. Matching board if they know; `unknown` only if they do not. Never default electric |

Path B’s “lookup for the value line, never a board” does **not** apply here. They did not name mods / value.

Never invent an MOT history. If working from owner-stated make / year, say so once in **[History]** — after the lamp, not as a stand-in for the picture.

## After they pick

One sentence to confirm the shape. Skip `show_lamp` unless they hesitate. Give **drive advice in that same turn**. Then one optional “anything feel different?” Default since / symptoms to “just now / drives normally” if they do not add more.

Engine cell 6: ask **steady or flashing** before treating it as lamp 6. Thermometer: **blue or red** before id 2. Then the Step 5 statement and, unless not-a-fault, Step 6 **in the same turn** as the statement.

Until that pick, stop after the picture and the circled-shape question.

## Owner copy (plate only)

≤120 words before they pick. Fictional plate in notes only: `AB12CDE`. Owner hears the car, not the plate. UK English.

**Owner:** plate AB12CDE

**Agent:** Lookup `{"reg":"AB12CDE"}`. Illustrative: 2016 Fiesta petrol. `show_dashboard` `board=petrol`, then `open_resource`. Does **not** list names. Does **not** speak **[Outlook]**.

Your 2016 Fiesta is on the petrol picture. Which **circled** number matches the lamp that is lit? Do not count left to right. Empty grey slots are not on this car. If the engine outline flashes, say flashing.

**Fail this turn:** “Repair may cost more than the car” / a value band / a lamp-name list / “are you driving?” / printing the plate.

After they pick **6**, then steady: example A + L (statement, then outlook). Not before.

## Red lines

1. Plate only and they have not said they are modifying → lookup, then the matching PNG. Not Path B. Not outlook.
2. Path B only if they **named** mods / value (and no lamp). A silent plate is not “presenting the car.”
3. Empty `show_dashboard` args is a fail. `board=` is required. Open the preview in the same turn.
4. Do not list lamp names. Do not ask them to pick 1–13 as a menu. Do not open unknown as the homepage when fuel is known.
5. Never default electric. Never skip the picker because lookup succeeded.
6. No **[Outlook]** / `repair_cost` / sell bid / MOT-dump as the fault until a lamp (or unmatched path).
7. No real plate in speech, URL, filename, log, or git.
8. Do not ask if they are driving. Stop / recovery lives in **[Drive advice]** after the pick.
9. No SAE J2012 wording. Do not diagnose. Do not invent pounds.
10. Owner-facing copy is English (outlook, not 愈后). See `99-skill-english-uk.md`.

## Pass / fail

**Pass**

- Plate only, no named wrap / service / value → Path A. Lookup this turn. Classify `fuel_type` **and** `fuel_raw`. Matching PNG.
- `show_dashboard` with required `board=`, then `open_resource` in the same turn. If the picture failed, say so.
- Ask the **circled** number on the matching shape. No name list. No “reply 1–13.”
- Speak **your 2016 Fiesta** / **your Transit**. Plate not printed. UK English.
- Do not ask if they are driving.
- No **[Outlook]** until a valid pick (or unmatched / unique named lamp). Then statement, then outlook.
- 404: make, year, fuel, mileage, then the matching board — not unknown first.
- 503 / 429 after retry: ask fuel; `unknown` only if they do not know. Never default electric.
- Example A: plate → petrol picture → they pick 6 → steady check → statement → outlook.
- Named wrap / value and no lamp → Path B (`46`), no PNG. Lamp plus wrap → `77`, outlook first.

**Fail**

- Treating a silent plate as Path B: value band, vehicle-card speech, or “what work are you doing?” instead of the picture.
- Skipping to **[Outlook]** / repair-or-sell / `repair_cost` / a sell bid with no lamp.
- Dumping MOT fusion or “last test passed” as today’s fault, or booking MOT instead of showing the cluster.
- Defaulting to engine-steady, oil, or any id because lookup succeeded.
- Empty `show_dashboard` args, or the unknown 13-lamp picture while fuel is already known.
- Listing oil-can / engine-block names, or asking them to count cells left to right.
- Asking if they are driving, or holding lookup / the picture until they confirm they have parked.
- Printing the plate. Defaulting electric. Shrinking the board toward electric on owner talk.
- Opening the picker on a named wrap / value question with no lamp (that is `46`).
- Speaking 愈后 / “prognosis” to the owner, or inventing pounds / a used-car price to fill a plate-only turn.
