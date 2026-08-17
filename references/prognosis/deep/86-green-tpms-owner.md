# 86 · Green TPMS → owner close

Not a second SKILL. If this note disagrees with `SKILL.md`, `references/prognosis.md`, `references/prognosis-cards.md`, or `references/warning-lights.md`, those win. Do not diagnose. Do not invent pounds. Do not add a 14th lamp id.

`safety_class: Green` means **the owner can act**. It is **not** a green dashboard symbol. Lamp 10 is an **amber** horseshoe with an exclamation mark. Among the 13 lamps, only `tyre-pressure` is Green.

Green maps to bucket **`owner`** (speech: **Close it yourself**) **only when the lamp is simply on**. Flash-then-steady is a **malfunction** → **`garage`**. This path is **not** `device`. A small OBD reader does not close TPMS.

The full lamp card is `10-tyre-pressure.md`. This file is only the Green → owner mapping and the device split.

## When

After the Step 5 statement when the pick is lamp **10** (`tyre-pressure`), or they named the horseshoe / tyre-pressure / TPMS lamp.

If behaviour is unknown, ask once: **simply on**, or **flash then steady** (about a minute at startup, then stays on). That split is classification, not a parts guess. Key-on bulb check that went out: skip outlook — not a fault.

Do **not** use this file for:

- `engine-steady` / unmatched GPF — those are **`device`** (scan). Not Green.
- Diesel DPF handbook regen or AdBlue top-up — also `owner`, but **Amber** or unmatched, not this lamp.
- Red-class work — never a close.

Do not upgrade to `poor` because the car is old. Do not open a sell path. Drive advice stays **drive with care** (`YesWithCare`), not Stop.

Vans: same buckets. Say “your Transit”.

## Map

| What they see | `safety_class` | Bucket | Owner hears | Close |
|---|---|---|---|---|
| Simply on | Green | `owner` | Close it yourself | Cold pressures to the **placard**, inspect, handbook reset |
| Flash ~1 minute at startup, then steady | Green (still) | `garage` | A garage can usually handle this | Pressures first; remaining malfunction is **not** an inflate close |
| Key-on bulb check, then out | — | skip | Not a fault | No outlook |

Green does **not** always mean driveway. The class stays Green on both live patterns. The **bucket** follows behaviour.

Internal labels: `owner` · `device` · `garage` · `poor`. Speech maps **`owner` and `device`** to the same phrase **Close it yourself**. Do not treat that phrase as a scan. Device steps (plug in, stored codes and freeze frame) run only on `device`. TPMS simply on is `owner`.

## Owner copy

Each branch is one spoken outlook. Keep it under 120 words. No part names. No pounds. No scanner shop.

**Simply on** (~50 words):

Close it yourself. Check all four tyres cold against the placard on the driver’s door sill or the fuel flap, not the number moulded on the tyre. Look for a nail or a bulge. Inflate, then reset as the handbook says. Do not clear the lamp with a scan tool.

**Flash-then-steady** (~64 words):

A garage can usually handle this. Still set all four tyres cold to the door-sill or fuel-flap placard first. If pressures are already correct and the lamp flashed for about a minute at startup then stayed on, book a workshop. We publish no figure for this class of job — ask two garages for a written estimate. Do not clear the lamp with a reader.

Spoken labels: **[Outlook]** then **[Close it]** on simply on. **[Outlook]** then **[Repair]** (no figure) on flash-then-steady. No **[Sell]** block.

## Not a device-scan close

`prognosis.md` allows Close it yourself only when outlook is good **and** either `owner` (Green / handbook / fluid) or `device` (a small reader changes the next step). TPMS simply on is the first of those, not the second.

- Do **not** plug in a reader as the close.
- Do **not** send them to `https://obdcode.co.uk/guides/best-obd2-scanner-uk/` or `/tools/scanners/` for this lamp.
- Do **not** call `car-diagnostic-test-cost` (or any nearby slug). The TPMS allowlist is empty.
- A handbook **reset after inflating** is the owner close. It is not a scan-tool clear. Do not refuse it as if it were (`26-never-clear-never-forced-regen.md`).
- Flash-then-steady: garage may read the system. That is **[Ask the garage]** process, not an owner device close. Still no reader-clear.

Tell the garage (malfunction branch only): if pressures are already correct, read sensor IDs and battery status. Do not guess that a sensor battery has died. Do not offer a parts shortlist.

## MOT

Gated on first-use, not copied as a verdict. M1 first used on or after 1 January 2012: a **malfunction** (often flash-then-steady) may be in scope. A lamp that only means inflate the tyre is **not** an automatic fail item. Pre-2012: do not call this a testable MOT lamp item. Never say “Expect a fail.” Link the [DVSA inspection manual](https://www.gov.uk/guidance/mot-inspection-manual-for-private-passenger-and-light-commercial-vehicles) when scope is in play.

If MOT is expired or due within 30 days, that is a statement **[Book]** line, not an outlook verdict.

Same-system MOT history (tyre condition, tread, valve) is context only. Every such line ends: **this does not show the cause of today’s lamp.**

## Red lines

1. Do not confuse **amber lamp colour** with **Green safety class**, or Green class with a green status lamp (main beam / cruise).
2. Do not treat Green as always-DIY: flash-then-steady is garage.
3. Do not treat flash-then-steady as “inflate only,” and do not skip the pressure check on the garage branch.
4. Do not run device-scan steps, scanner-shop links, or `car-diagnostic-test-cost` because this lamp is on.
5. Do not name the failed part (sensor, sensor battery, pairing, module, valve stem).
6. Do not advise clearing codes or the lamp as a repair.
7. Do not invent GBP for a tyre, a sensor, or a workshop visit. Empty allowlist → we publish no figure; two written estimates on the garage branch only.
8. Do not push selling. Do not say the tester will fail the car.
9. Do not print a plate. Do not use the sidewall pressure instead of the placard.

## Pass versus fail

**Pass:** Simply on → **Close it yourself.** Cold pressures to the door-sill or fuel-flap placard, inspect, handbook reset. No scan-tool clear.

**Pass:** Flash-then-steady after correct pressures → **A garage can usually handle this.** We publish no figure — two written estimates. No sell block.

**Pass:** Ask simply on vs flash-then-steady once when behaviour is unknown.

**Pass:** “The lamp does not name which tyre is low.” Inflate all four to the placard.

**Pass:** “`safety_class: Green` is owner-act, not a green lamp. This horseshoe is amber.”

**Pass:** Quoting this car’s in-family MOT tyre note, then “this does not show the cause of today’s lamp.”

**Pass:** MOT in scope only as malfunction (often flash-then-steady) on M1 from 1 January 2012. Inflate-only is not an automatic fail item.

**Fail:** Mapping Green TPMS simply on to **`device`**: “plug in a reader / buy a scanner / call `car-diagnostic-test-cost`.”

**Fail:** Treating flash-then-steady as the inflate close, or skipping pressures on the garage branch.

**Fail:** “It’s a dead TPMS sensor.” / “It needs pairing.” / “It’s the valve.”

**Fail:** “Clear it with a cheap OBD dongle.”

**Fail:** “About £80 a corner” / any invented tyre or sensor bill.

**Fail:** “Expect a fail at MOT.” / “Sell it, TPMS isn’t worth fixing.”

**Fail:** Using the sidewall pressure instead of the placard.

**Fail:** Calling the horseshoe a green status lamp, or sending them to the scanner shop for TPMS.
