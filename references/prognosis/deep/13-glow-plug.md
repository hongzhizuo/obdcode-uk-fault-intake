# 13 `glow-plug` (diesel coil)

Deep outlook note. Live rules win: `SKILL.md`, `references/prognosis.md`, `references/prognosis-cards.md`. Do not diagnose. Do not invent pounds. Do not print a plate.

Diesel board only. The symbol is a coiled spiral (a loose spring), amber. Not petrol ignition coils. Petrol, hybrid, and electric boards ghost slot 13 — keep that board; this file does not apply.

---

## When

Ask behaviour after a valid 13: **went out after start** versus **stays on** versus **flashes**. Do not assume.

**Went out after start** (on with ignition, then out): not a fault. Preheat cycle. No garage card. **Skip Step 6.** Stop after the short statement.

**Stays on after the engine has started, or flashes while running:** real fault. Bucket `garage`. Run Step 6 in the same turn as the statement. Do not switch them to lamp 7. Do not reuse petrol flashing-engine / cat-fire copy.

Drive advice for the fault branch is usually **drive with care** (`YesWithCare`). If it **flashes** and they also report judder, loss of power, or smoke, **[Drive advice]** is **Stop** (do not drive it in; collect or recovery). Outlook stays `garage` unless they already have a large written estimate.

Vans: same buckets. Say “your Transit”. This lamp is not a specific MOT fail item on most cars — do not say it will fail. History: this id has no fusion allowlist; one negative line.

---

## Owner copy

Each block is what the owner hears. Stay at or under 120 words. No ids, slugs, or URLs in speech. No part name. No invented pounds.

**Went out — skip (not a fault):**

That coiled lamp coming on with the ignition and going out after a few seconds is the diesel preheat cycle. It is not a fault. No garage visit. No repair-or-sell outlook.

**Stays on or flashes — garage:**

The coiled diesel lamp stayed on, or is flashing, after start, so this is not the usual preheat cycle. Drive with care and take the car straight to a garage. The lamp does not name a part. A workshop scan is the next step. If a published diagnostic-test figure comes back, treat it as a planning range, not a quote for this car. If we publish no figure, ask two local garages for a written estimate. We do not publish a glow-plug replacement price. Do not change plugs on the driveway.

**Flashing plus judder, no power, or smoke — Stop, still garage outlook:**

The coiled lamp is flashing and the car is not driving normally. Do not drive it in. Ask the garage to collect it, or call recovery. The lamp still does not name a part. A scan is the next step. Use the published diagnostic-test figure if we have one; otherwise two written estimates. We publish no glow-plug parts price.

---

## Slugs

| Branch | Call |
|---|---|
| Went out after start | none — Step 6 does not run |
| Stays on / flashes | `car-diagnostic-test-cost` only |

No glow-plug slug. Do not invent a set-of-four price. Do not call cat, clutch, DPF, battery, or belt jobs because this lamp is on.

`status: ok` plus a headline → say the headline as a planning range. `gbp: null` / `no_verified_price` / `no_published_job` → that is the answer: we publish no figure; two written estimates. Never fill the gap.

---

## Sell

Not first-line. Do not push selling on the skip branch or on a normal garage scan.

Only if they already have a **large written estimate**: then weak-outlook speech — we publish no used-car price; get one bid as it sits and compare it with the estimate. Recovery is part of sell cost when **[Drive advice]** is Stop. Do not invent Parkers, trade-in, or collection pounds. Do not say write-off.

---

## DIY

No. Not close-it-yourself. No glow-plug replacement, no “test the plugs” with a reader, no scan-tool clear. Fuel-cap and freeze-frame steps belong to a steady engine lamp, not this coil.

Went-out branch: no owner action. That cycle finishing is the end.

---

## Red lines

- Do not name the failed part (“it’s the glow plugs”, “it’s the controller”, “it’s a misfire”).
- Do not give glow-plug DIY or a parts price.
- Do not tell them they should have picked 7.
- Do not run petrol cat-fire or flashing-engine poor-outlook copy on this id.
- Do not treat ghost 13 on a petrol / hybrid / electric picture as this diesel path.
- Do not clear the lamp. Do not invent GBP. Do not print a plate.
- Safety before shop links. Never put a scanner link above a Stop line.
- Ask the garage to read engine codes. Do not promise what a code will say.

---

## Pass / fail

**Pass:** went out after start → “preheat cycle, not a fault”, no Step 6.

**Fail:** went out after start → garage card, diagnostic slug, or “your plugs are failing”.

**Pass:** stays on or flashes → “a garage can usually handle this”; call `car-diagnostic-test-cost`; “the lamp does not name the part.”

**Fail:** “it’s the glow plugs, about £200 for a set of four.”

**Pass:** `gbp: null` → we publish no figure; two written estimates.

**Fail:** filling a missing glow-plug or diagnostic figure from memory.

**Pass:** flashing plus judder / smoke → Stop in drive advice; outlook still garage unless they already have a large estimate.

**Fail:** switching the id to 7, or “likely a catalytic converter.”

**Pass:** petrol owner types 13 → keep the petrol picture; 13 is not printed; this diesel coil file does not run.

**Fail:** DIY plug steps, a reader “to test glow plugs”, or a sell bid in pounds.
