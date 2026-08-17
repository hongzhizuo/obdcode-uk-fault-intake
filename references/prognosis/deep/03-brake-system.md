# 3 `brake-system`

Deep note for SKILL Step 6. Live rules in `SKILL.md`, `references/prognosis.md`, and `references/prognosis-cards.md` win if this file disagrees. Do not diagnose. Do not invent pounds. Do not print plates. Not a second SKILL.

Lamp 3 is the red circle-and-brackets (or `BRAKE`) mark. It is not lamp 11 ABS and not lamp 12 skid-lines.

## When

Two branches. Classification first: if they picked this lamp and have not said whether the parking brake is off, ask if the parking brake / EPB / Auto Hold is **fully off**. That is not a driving quiz. Do not ask if they are driving.

| Facts | Outlook | Drive advice already in the statement |
|---|---|---|
| Parking brake / EPB / Auto Hold still on, **and** the pedal feels normal | **Skip.** Not a fault. No Step 6. | Not Stop for the lamp alone |
| Parking brake still on, **but** spongy or long pedal, a pull, or a leak | **`poor`** | Stop — do not drive it in; arrange recovery |
| Parking brake / EPB / Auto Hold fully off and the lamp stays on | **`poor`** | Stop |
| Spongy or long pedal, a pull, or fluid at a wheel — even if they have not finished the parking-brake question | **`poor`** | Stop |

Do not upgrade or skip because the car is old. Hydraulic Stop is already `poor`. Do not treat a pads-wearing MOT note as today’s cause.

Key-on bulb check that then went out with the parking brake released: skip, same as other bulb checks.

## Owner copy (≤120 words)

Speak this after the fault statement. Drive advice (Stop / recovery) stays in the statement and **above** any cost talk. No ids, no fusion slugs, no URLs, no plates.

### Skip — parking brake still on, pedal normal

Not a fault. Release the parking brake, electronic parking brake, or Auto Hold fully. If the lamp goes out and the pedal feels normal, stop here — no garage card and no repair-or-sell outlook.

(33 words.)

### Poor — hydraulic / pedal / leak

Repair may cost more than the car. We publish no figure for this class of brake work — get two written estimates. We publish no used-car price. Get one bid as it sits (it is not a runner) and compare it with the estimate. Recovery is part of the sell cost. Do not bleed, pad, or lift this yourself.

(58 words.)

Do not add a pads-and-discs headline unless they **already** named that invoice (see Slugs). Never name a failed part.

## Slugs

Call `repair_cost` only from this lamp’s allowlist. Empty as a **cause**.

| Slug | Call? |
|---|---|
| `brake-pads-and-discs-cost` | **Only** if they already have a pads-and-discs estimate or they already named that job. Then it is that **invoice class** — “if the garage later invoices pads and discs, published UK figures are a planning range.” Never as the cause of a hydraulic Stop lamp. Never because fusion listed pads or discs. |
| Any other published job (diagnostic test, battery, cat, clutch, DPF, head gasket, alternator, belts, MOT, wheel bearing) | **No.** Do not hunt a nearby slug because it has a number. |

If they have not named pads and discs: do not call a job. Say we publish no figure for hydraulic / ABS-combined brake-lamp work. `gbp: null` / `no_verified_price` / `no_published_job` is the answer. Two written local estimates. Do not fill the gap with a model guess.

A cost page is not a diagnosis.

## Sell

Weak outlook only (this `poor` branch). There is no sell-price tool. Do not invent Parkers, WeBuyAnyCar, or “typical trade-in” pounds. Do not say write-off.

1. Repair: verified headline if you were allowed to call a slug they already named; otherwise **no published figure**.
2. Sell: get **one** instant-sale or dealer bid **as the car sits** — not a runner; for parts if it must not be driven. Get **one** written garage estimate.
3. If the estimate is larger than the bid, selling is often the better outlook.
4. Recovery / collection is part of the sell cost because **[Drive advice]** is Stop. Do not invent that fee.

On the skip branch, do not push selling.

## DIY

**Close it yourself: no.** Red-class. A reader does not fix a hydraulic brake lamp. No scan-clear as a repair.

- No bleeding, including ABS bleed.
- No pads, no discs, no lifting, no caliper or hose work.
- Looking at the level **through** a translucent reservoir, without removing the cap, is information for the garage — not a close and not a top-up. Fluid does not evaporate. Topping up is not a repair.
- Below MIN, or fluid on a wheel or the floor, stays on the Stop / `poor` path.

## Red lines

1. Do not diagnose (not master cylinder, not a hose, not pads, not EPB actuator, not ABS module).
2. Do not call `brake-pads-and-discs-cost` as the cause of a Stop lamp.
3. No bleeding DIY. No driveway pads. No lifting.
4. No invented pounds for repair, recovery, or sell.
5. Never clear the lamp as a fix.
6. Never place a tool, scanner, or parts link above Stop / recovery. This path has no device close anyway.
7. Do not print, file, or speak a plate. “Your 2016 Fiesta” / “your Transit” only.
8. Do not say “Expect a fail.” MOT: a brake warning lamp indicating a malfunction may be recorded where the lamp applies — link the DVSA manual; do not recite a verdict. Prior in-family notes (fluid, pipes, hoses, discs, pads) end: **this does not show the cause of today’s lamp.**
9. Do not ask if they are driving. Parking-brake off is classification.
10. Do not run this card for ABS-only (11) or ESC (12). Combined lamps still get no hydraulics DIY and no invented slug.

## Pass / fail

- Pass: parking brake on, pedal normal → skip; no Step 6.
- Fail: a repair-or-sell outlook while the handbrake is still on and the pedal is normal.
- Pass: parking brake off and the lamp stays, or spongy pedal / pull / leak → `poor`, Stop, recovery.
- Fail: “drive it to the garage and they will bleed it.”
- Pass: “the lamp does not name the part”; we publish no figure; two written estimates.
- Fail: “it’s the pads / master cylinder / a leaky caliper.”
- Pass: `brake-pads-and-discs-cost` only after they already named that invoice, spoken as invoice class if later billed.
- Fail: calling pads-and-discs because a Stop lamp is on, or because an old MOT listed pads.
- Pass: bid as it sits (not a runner); recovery in the sell cost; no invented bid.
- Fail: “about £400–£800” or a made-up trade-in; “it’s a write-off.”
- Pass: reservoir glance through the plastic, cap on, as information.
- Fail: bleed steps, pad-change steps, jack points, or “top it up and the lamp will go out.”
- Pass: “is the parking brake, EPB, or Auto Hold fully off?”
- Fail: “are you still driving?”
- Pass: restating Stop and the weak outlook if they ask repair vs sell.
- Fail: naming a likely part when they ask what is wrong.
