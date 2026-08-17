# 30 · `wheel-bearing-replacement-cost` only if they already named that job

Not a second SKILL. If this note disagrees with `SKILL.md`, `references/prognosis.md`, or `references/prognosis-cards.md`, those three win. Do not diagnose. Do not invent pounds. Do not add a 14th lamp id.

**Slug:** `wheel-bearing-replacement-cost`  
**Use:** only if **they already named** a wheel-bearing / hub-bearing job  
**Never:** because the ABS lamp is on. Not an ABS diagnosis.  
**Headline ≠ failed part:** a published range is an **invoice class** if later billed — not “you have a failed bearing.”

Live chats **must** call `repair_cost` and speak that turn’s result. **This file must not freeze a pound figure as always-true.** Do not copy a remembered £ amount into speech or into this note.

Lamp 11 (`abs`) still has an **empty** allowlist. This slug is a named-job exception, not a new ABS cause. Full ABS card: `11-abs.md`. Working ordinary brakes: `94-abs-still-brakes.md`.

---

## When

Call `repair_cost` with `job` = `wheel-bearing-replacement-cost` only when **they already named that job**. Their words, not a guess from a lamp.

That includes:

- A written quote or invoice for a **wheel bearing** / **hub bearing**
- “How much is a wheel bearing?” / “the garage wants a wheel bearing”
- They said the next job **is** a wheel-bearing replacement

Then speak it only as **if later invoiced**: “If the garage later invoices a wheel bearing, published UK figures are …” Planning range, not a quote for this car, not today’s failed part.

Lamp **and** a bearing they already named: finish the fault statement and that lamp’s outlook **first** (safety). Use the lamp’s own slugs for **[Repair]**. Add this slug only for the named work. Do not fold the bearing headline into the lamp as the cause.

No lamp, they named the job: call this slug for the **job** range. That is not Path B value-gain (this work has **no** published sale-price band in `value-gain.md`). Do not invent a gain. The invoice they paid, if they give one, is **spend**.

Vans: same gate. Say **your Transit**. A day off the road may be speech. Do not invent a day-rate.

---

## When not

**Never because the ABS lamp is on.** Card 11 allowlist is **none**. We publish no figure for that class of job — two written estimates. A scan at the garage is still the next step in speech. Do not hunt this slug so there is a number.

Do **not** treat these as naming the job:

- Amber `ABS` in a circle with brackets (picked 11, or they said ABS / anti-lock)
- “Is it the wheel bearing?” / “could it be a hub?” after that lamp — diagnosis request. Refuse. Restate **[Drive advice]** and **[Outlook]**. Do not fetch this slug to fill the silence
- Growl, hum, rumble, or play that changes with speed, and they never said **wheel bearing**. Those facts go in **[Since]**. They do not name this job
- MOT fusion / a prior certificate that mentioned a bearing or a wheel-speed sensor. History is context. End: **this does not show the cause of today’s lamp.** Fusion does not authorise this slug
- Wheel-speed sensor, reluctor ring, wiring, module, pump, or hub as a shortlist we offered

Do **not** call this slug on:

- `abs` (11) when they have **not** named a wheel-bearing job
- `esc-traction` (12) — empty allowlist; traction-button check is not a bearing
- Hydraulic `brake-system` (3) — empty as a cause; pads-and-discs only if **they** already named that pads job, never this bearing slug instead
- `tyre-pressure`, `power-steering`, `airbag-srs`, engine lamps, DPF / GPF, charging, oil, coolant, glow, AdBlue, unmatched EV
- Because it is the only published slug with a number

Never pick a neighbour (pads, diagnostic test, clutch) to stand in for a bearing, or a bearing to stand in for ABS.

Skip Step 6 (and this slug) when the ABS mark was only a **key-on bulb check** that went out — not a fault.

Do not upgrade lamp 11 from `garage` to `poor` because they named a bearing, or because the car is old. Upgrade only if they already have a **large hydraulic quote**.

---

## How to call (live)

Prefer the tool. Same turn as **[Outlook]** / **[Repair]**, **after** **[Drive advice]**. Never above a Stop line. Call **only** after they named the job.

```
POST https://obdcode.co.uk/mcp
{"jsonrpc":"2.0","id":1,"method":"tools/call",
 "params":{"name":"repair_cost","arguments":{"job":"wheel-bearing-replacement-cost"}}}
```

Plain HTTP if you do not speak MCP: the same job name is the slug on `https://obdcode.co.uk/guides/wheel-bearing-replacement-cost/`. Prefer the tool.

Speak the **live** result only, and only in the **if-invoiced** frame when a lamp is also on:

| Result | Say |
|---|---|
| `status: ok` and a headline | “If the garage later invoices a wheel bearing, published UK figures are …” then that headline. Planning range, **not** a quote for this car, **not** “you need this job,” **not** “the lamp is a bearing.” |
| `gbp: null` / `no_verified_price` / `no_published_job` | **That is the answer.** We publish no figure. Two written estimates. Do not fill the gap with a remembered bearing price. |

No lamp, they named the job: same live headline or no-figure line, still as the **job they named**, still not a diagnosis.

Do not cache yesterday’s pounds in this file or in the next chat. A cost page is not the failed part.

---

## Owner copy

≤120 words. No ids, no fusion slugs, no URLs, no plates, no pounds unless this turn’s `repair_cost` returned a verified headline.

### They already named a wheel-bearing job

You named a wheel-bearing job. If a garage later invoices that work, published UK figures are a planning range — not a quote for this car, and not a diagnosis that a lamp is a bearing. If we publish no figure, ask two workshops for a written estimate. An ABS lamp still does not name the part. A scan is the next step when that lamp is on. Do not lift or press a hub on the driveway. This skill does not diagnose.

(83 words. Insert the live headline only inside the “if later invoices” sentence.)

If an ABS lamp is also on, keep that card’s garage speech: ordinary brakes still work; anti-lock does not; drive gently and directly there. Do not put the bearing range above Limited / Stop.

### ABS lamp, bearing **not** named

Do **not** speak a bearing block. Speak the ABS outlook only.

A garage can usually handle this. We publish no figure for this class of job. Ask two workshops for a written estimate. A scan is the next step; the lamp does not name the part.

(35 words.)

If they then ask “so is it the wheel bearing?”: this skill does not diagnose. Restate **[Drive advice]** and **[Outlook]**. Do not call the slug.

---

## Slugs next to ABS

| Slug | On lamp 11 | How to speak it |
|---|---|---|
| *(none)* | Default | Empty allowlist. We publish no figure — two written estimates. A scan at the garage is speech, not `car-diagnostic-test-cost`. |
| `wheel-bearing-replacement-cost` | **Only** if they already named that job | **If later invoiced.** Never “the ABS lamp is a bearing.” |
| `brake-pads-and-discs-cost` | **No** as the cause of this lamp | Pads only if they already named a pads/discs job on the brake card — not here. |
| `car-diagnostic-test-cost` | **No** | Not on this allowlist. |

Do **not** call sensor / modulator / pump jobs. None is published. Do not invent one.

---

## Sell and DIY

**Sell:** not first-line on ABS (`garage`). Do not push selling because they named a bearing. Sell talk only on a `poor` branch (they already have a **large hydraulic quote**): we publish no used-car price; **one** bid as it sits and **one** written estimate. Recovery is part of sell cost only when **[Drive advice]** is Stop. ABS-only Limited driving is still a runner unless hydraulics took it to Stop. Do not say write-off. Do not invent Parkers / trade-in pounds. There is **no** published sale-price **gain** for a new bearing.

**Close it yourself: no.** Hub and bearing work needs the car lifted. Red-class workshop. A reader does not close ABS and does not prove a bearing.

- No lifting, no hub nuts, no press, no driveway sensor or reluctor work
- No ABS bleed. No pads as a substitute job
- Ordinary brakes still working is **[Drive advice]**, not a close
- Do not clear the lamp
- Owner-safe notes for the garage only: which side they hear a noise, whether it comes and goes at a speed. Information, not a named part

This path has no `[Close it]` block.

---

## Red lines

1. Do not diagnose. Not the bearing, hub, sensor, reluctor, wiring, module, or pump — even as a shortlist.
2. Do not call `wheel-bearing-replacement-cost` because the ABS lamp is on.
3. Do not treat growl / hum / play, an MOT note, or “is it the bearing?” as naming the job.
4. Never “it’s the wheel bearing” / “ABS usually means a hub.” A cost slug is not a diagnosis.
5. No invented GBP for repair, sell, recovery, or a “typical bearing.” No figure frozen in this note.
6. No lift / hub / press how-to. No driveway ABS bleed or code clear.
7. No SAE J2012 wording. A later code number is a fact to hand over, not a named part.
8. Never print a real registration. Illustrative only: `AB12CDE`; then “your 2016 Fiesta.”
9. Safety before commercial: Limited / Stop / recovery above any cost line.
10. Do not mix this slug into lamp 3 Stop speech, lamp 12, or an engine lamp as the cause.

---

## Pass versus fail

**Pass**

- They already named a wheel-bearing job → call `wheel-bearing-replacement-cost`; “if the garage later invoices a wheel bearing, published UK figures are …” after a live result.
- Quote this turn’s headline, including “we publish no figure — two written estimates.”
- ABS lamp, bearing **not** named → empty allowlist; garage; no figure; “a scan is the next step; the lamp does not name the part.”
- “Is it the wheel bearing?” after ABS → this skill does not diagnose. Restate **[Drive advice]** and **[Outlook]**. Do not call the slug.
- Growl / hum in **[Since]** only; still no slug until they name the job.
- Prior MOT bearing or wheel-speed note ends: **this does not show the cause of today’s lamp.**
- Lamp plus a named bearing → lamp outlook first; slug only for that named invoice class; not as the cause.
- Ordinary brakes still work; anti-lock does not. Drive directly there. No driveway lift.
- Restating Limited / recovery when they ask keep-driving or repair-vs-sell.

**Fail**

- Calling `wheel-bearing-replacement-cost` because the ABS lamp is on.
- “It’s the wheel bearing / hub / sensor / reluctor / wiring.”
- “Sensor, reluctor, or wiring.”
- Treating growl, play, or an old MOT line as naming this job.
- Answering “is it the bearing?” with this slug or a parts shortlist.
- “About £150–£400” (or any pounds) with no live `repair_cost` result, or a figure copied from this file.
- Treating the bearing cost page as today’s diagnosis, or as a reason to skip the ABS garage scan.
- Calling this slug because it is the only one with a number, or instead of “no figure for this class of job.”
- Pads-and-discs or diagnostic-test as a stand-in for ABS or for a bearing they did not name.
- Lift / press / hub DIY, or “clear the code and see.”
- Invented trade-in, “adds £X on sale,” or “Expect a fail.”
- Naming a likely part when they ask what is wrong.
