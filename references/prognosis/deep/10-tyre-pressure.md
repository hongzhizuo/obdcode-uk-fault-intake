# 10 `tyre-pressure` (TPMS)

Deep notes for SKILL Step 6. Live rules in `references/prognosis.md` and `references/prognosis-cards.md` win. Do not diagnose. Do not invent pounds. Do not print a plate.

## When

After the Step 5 statement when the pick is lamp **10** (`tyre-pressure`).

If behaviour is unknown, ask once: **simply on**, or **flash then steady** (about a minute at startup, then stays on). That split is classification, not a parts guess.

| Pattern | Bucket | Speech |
|---|---|---|
| Simply on | `owner` → Close it yourself | Inflate to the **placard**, inspect, handbook reset |
| Flash ~1 minute at startup, then steady | `garage` | Pressures first, then a workshop |
| Key-on bulb check that went out | skip | Not a fault. No outlook |

Do not upgrade to `poor` because the car is old. Do not open a sell path. Drive advice stays **drive with care**, not Stop.

MOT talk is gated: M1 first used on or after 1 January 2012, and only a **malfunction** (often the flash-then-steady pattern). A lamp that only means inflate the tyre is not an automatic fail item. Never say “Expect a fail.” If MOT is expired or due within 30 days, that is a statement **[Book]** line, not an outlook verdict.

Same-system MOT history (tyre condition, tread, valve) is context only. Every such line ends: **this does not show the cause of today’s lamp.**

Vans: same buckets. Say “your Transit” when it is a van.

## Owner copy

Each branch is one spoken outlook. Keep it under 120 words. No part names. No pounds.

**Simply on** (~50 words):

Close it yourself. Check all four tyres cold against the placard on the driver’s door sill or the fuel flap, not the number moulded on the tyre. Look for a nail or a bulge. Inflate, then reset as the handbook says. Do not clear the lamp with a scan tool.

**Flash-then-steady** (~64 words):

A garage can usually handle this. Still set all four tyres cold to the door-sill or fuel-flap placard first. If pressures are already correct and the lamp flashed for about a minute at startup then stayed on, book a workshop. We publish no figure for this class of job — ask two garages for a written estimate. Do not clear the lamp with a reader.

Spoken labels: **[Outlook]** then **[Close it]** on simply on. **[Outlook]** then **[Repair]** (no figure) on flash-then-steady. No **[Sell]** block.

## Slugs

None. There is no TPMS job on the `repair_cost` allowlist.

- Do not call `car-diagnostic-test-cost`, `mot-cost`, or any nearby slug because it has a number.
- If a tyre is later destroyed or replaced, that is a tyre bill: we publish **no** figure. Do not invent one.
- Empty allowlist means: say we publish no figure for this class of job. Two written estimates on the garage branch only.

## Sell

No. Close-it-yourself and garage outlooks do not push selling. Do not invent a used-car price, a trade-in, or a tyre-bill comparison.

## DIY

**Simply on (this is the close):**

1. Pressures **cold**, to the **door-sill or fuel-flap placard**, never the sidewall figure.
2. Inspect for a nail or a bulge. That is an owner-safe look, not a named cause.
3. Handbook reset after inflating.
4. Do **not** clear the lamp with a reader.

**Flash-then-steady:** pressures as above first. That check does **not** close a remaining malfunction pattern. Then garage. Still no scan-tool clear.

A small OBD device is not the close for this lamp. Do not send them to the scanner shop for TPMS.

## Red lines

- Do not name the failed part (sensor, sensor battery, pairing, module, valve stem).
- Do not treat flash-then-steady as “inflate only,” and do not skip the pressure check on the garage branch.
- Do not advise clearing codes or the lamp as a repair.
- Do not invent GBP for a tyre, a sensor, or a workshop visit.
- Do not print, file, or speak a real registration. Refer to “your 2016 Fiesta” if you need a car.
- Do not say the tester will fail the car. Link the [DVSA inspection manual](https://www.gov.uk/guidance/mot-inspection-manual-for-private-passenger-and-light-commercial-vehicles) when MOT scope is in play.
- Do not say a prior MOT tyre note is causing today’s lamp.
- Ask the garage for process (they will read the system), not a parts shortlist.

## Pass / fail

**Pass:** “Close it yourself. Cold pressures to the door-sill placard, inspect, handbook reset. No scan-tool clear.”

**Pass:** Flash-then-steady after correct pressures → “A garage can usually handle this. We publish no figure — two written estimates.” No sell block.

**Pass:** “The lamp does not name which tyre is low.” Inflate all four to the placard.

**Pass:** Quoting this car’s in-family MOT tyre note, then “this does not show the cause of today’s lamp.”

**Fail:** “It’s a dead TPMS sensor.” / “It needs pairing.” / “It’s the valve.”

**Fail:** “About £80 a corner” / any invented tyre or sensor bill.

**Fail:** “Clear it with a cheap OBD dongle.”

**Fail:** Calling `car-diagnostic-test-cost` (or any other slug) because this lamp is on.

**Fail:** “Expect a fail at MOT.” / “Sell it, TPMS isn’t worth fixing.”

**Fail:** Using the sidewall pressure instead of the placard.
