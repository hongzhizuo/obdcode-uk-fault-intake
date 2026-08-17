# 90 · Inflate to the door-sill or flap placard

Not a second SKILL. If this note disagrees with `SKILL.md`, `references/prognosis.md`, `references/prognosis-cards.md`, or `references/value-gain.md`, those four win. Do not diagnose. Do not invent pounds. Do not add a 14th lamp id.

Live lamp card: `references/prognosis/deep/10-tyre-pressure.md`. This file is only the **number to use**.

**Lamp:** `tyre-pressure` (circled **10**, horseshoe tyre with !)  
**The number:** driver’s **door-sill** placard or **fuel-flap** placard  
**Not the number:** the figure **moulded on the tyre sidewall**  
**Owner close:** only when the lamp is **simply on** (`owner` → Close it yourself)  
**Drive advice:** drive with care — not Stop

---

## When

Use this note in the same turn as the Step 5 statement when the pick is lamp **10** and they will set pressures.

If behaviour is unknown, ask once: **simply on**, or **flash then steady** (about a minute at startup, then stays on). That split is classification, not a parts guess.

| Pattern | Bucket | Placard rule | Is it the close? |
|---|---|---|---|
| Simply on | `owner` → Close it yourself | Cold, all four, to the **door-sill or flap placard** | **Yes** — then inspect and handbook reset |
| Flash ~1 minute at startup, then steady | `garage` | Same placard check **first** | **No** — then a workshop |
| Key-on bulb check that went out | skip | — | Not a fault. No outlook |

Do not open a sell path. Do not upgrade to `poor` because the car is old. Do not send them to a scanner shop for this lamp.

Skip this file when the showing lamp is not 10, or when Step 5 already ended as not-a-fault (bulb check that went out).

Vans: same rule. Say **your Transit**.

MOT talk stays gated: M1 first used on or after 1 January 2012, and only a **malfunction** (often flash-then-steady). A lamp that only means inflate the tyre is not an automatic fail item. Never say “Expect a fail.”

---

## What the number is (and is not)

| Use this | Do not use this |
|---|---|
| The vehicle **placard** on the driver’s door sill (door shut / B-pillar sticker) | The large PSI / bar figure **moulded on the tyre sidewall** |
| The same target on the **fuel-flap** sticker, if that is where this car prints it | A garage-forecourt “typical 32 PSI”, a phone app guess, or the last car they owned |
| The placard’s **front / rear** (and load) lines, if it prints more than one | One sidewall number copied onto every corner |

The sidewall mould is not this car’s cold target. It is a tyre marking. Inflating to it is not the close, even if the lamp later goes out.

If they already pumped to the sidewall figure: that does **not** close the lamp. Set all four **cold** to the **placard**, then inspect and reset. Still do not name a sensor.

If they cannot find a placard: do not invent a PSI. Tell them to look on the driver’s door shut and inside the fuel flap, then the handbook. Do not fall back to the sidewall.

A spare is only in scope if **this** placard or handbook includes it. Do not invent a spare pressure.

---

## Owner copy

≤120 words. Spoken **[Outlook]** then **[Close it]** on simply on. No part names. No pounds. No plate.

**Simply on** (~55 words):

Close it yourself. Check all four tyres cold against the placard on the driver’s door sill or the fuel flap — not the number moulded on the tyre. Look for a nail or a bulge. Inflate to that placard, then reset as the handbook says. Do not clear the lamp with a scan tool.

**Flash-then-steady** (placard line only; garage is the outlook):

Still set all four tyres cold to the door-sill or fuel-flap placard first, not the sidewall. If pressures are already on the placard and the lamp flashed then stayed on, that check is not the close — a garage can usually handle this. We publish no figure. Do not clear it with a reader.

Spoken labels: **[Outlook]** Close it yourself, then **[Close it]**, on simply on. **[Outlook]** then **[Repair]** (no figure) on flash-then-steady. No **[Sell]** block.

---

## Slugs

None. There is no TPMS or tyre job on this lamp’s `repair_cost` allowlist.

- Do not call `car-diagnostic-test-cost`, `mot-cost`, or any nearby slug because it has a number.
- A later tyre bill is still **no** published figure. Do not invent one.
- Empty allowlist: say we publish no figure for this class of job. Two written estimates on the **garage** branch only.

A cost page is not the failed part. The placard is not a parts shortlist.

---

## Sell

**No.** Close-it-yourself and garage outlooks do not push selling. Do not invent a used-car price, a trade-in, or a tyre-bill comparison.

---

## DIY

**Simply on (this is the close):**

1. Read the **door-sill or fuel-flap placard**. Ignore the sidewall mould.
2. Set all four pressures **cold** to that placard (front / rear / load lines if printed).
3. Inspect for a nail or a bulge. That is an owner-safe look, not a named cause.
4. Handbook reset after inflating.
5. Do **not** clear the lamp with a reader.

**Flash-then-steady:** the same placard check first. Correct placard pressures do **not** close a remaining malfunction pattern. Then garage. Still no scan-tool clear.

A small OBD device is not the close for this lamp. Fuel-cap and engine-scan steps do not apply here.

---

## Red lines

1. Never tell them to inflate to the **sidewall** number.
2. Do not invent a PSI / bar figure when the placard is missing. Point at the door shut, the fuel flap, then the handbook.
3. Do not name the failed part (sensor, sensor battery, pairing, module, valve stem).
4. Do not treat flash-then-steady as “inflate only,” and do not skip the placard check on the garage branch.
5. Never advise clearing codes or the lamp as a repair.
6. Do not invent GBP for a tyre, a sensor, or a workshop visit.
7. Do not print, file, or speak a real registration. Refer to “your 2016 Fiesta” / “your Transit.”
8. Do not say the tester will fail the car for an inflate-only lamp. Link the [DVSA inspection manual](https://www.gov.uk/guidance/mot-inspection-manual-for-private-passenger-and-light-commercial-vehicles) when MOT scope is in play.
9. Do not say a prior MOT tyre note is causing today’s lamp.
10. Ask the garage for process (they will read the system), not a parts shortlist.

---

## Pass versus fail

**Pass**

- “Close it yourself. Cold pressures to the door-sill or fuel-flap placard, not the number moulded on the tyre. Inspect, handbook reset. No scan-tool clear.”
- Simply on → bucket `owner`. That **is** the close.
- “The sidewall figure is not this car’s target.”
- Front / rear (or load) lines from **this** placard, if it prints them.
- “The lamp does not name which tyre is low.” Inflate all four to the placard.
- Flash-then-steady: placard first, then “A garage can usually handle this. We publish no figure — two written estimates.” No sell block.
- They already used the sidewall: still not a close until cold pressures match the **placard**.
- In-family MOT tyre note, then: **this does not show the cause of today’s lamp.**

**Fail**

- “Put in what it says on the tyre.” / “The sidewall says 51 PSI.” / any sidewall number as the target.
- Inventing “32 PSI all round” because they cannot find the sticker.
- “It’s a dead TPMS sensor.” / “It needs pairing.” / “It’s the valve.”
- “About £80 a corner” / any invented tyre or sensor bill.
- “Clear it with a cheap OBD dongle.”
- Calling `car-diagnostic-test-cost` (or any other slug) because this lamp is on.
- Treating flash-then-steady as inflate-only, or skipping the pressure check.
- Sending them to the scanner shop as the TPMS close.
- “Expect a fail at MOT.” / “Sell it, TPMS isn’t worth fixing.”
- A real plate in git or speech.

**Pass sketch** (illustrative; no live pounds): Your 2016 Fiesta, tyre-pressure lamp simply on. Close it yourself. Cold, all four, to the door-sill or flap placard — not the sidewall. Inspect, handbook reset. Do not clear it with a reader.
