# 73 · When to call `repair_cost`

Not a second SKILL. If this note disagrees with `SKILL.md`, `references/prognosis.md`, `references/prognosis-cards.md`, or `references/value-gain.md`, those four win. Do not diagnose. Do not invent pounds. Do not add a 14th lamp id.

Call `repair_cost` **only** with a slug on the allowlist for **this lamp** (or unmatched path), or a **named published job** they asked about in Step 7. Never hunt a nearby slug. An empty allowlist is the answer: we publish no figure for this class of job.

## When

Call it in **Step 6** (outlook) or **Step 7** (they named a published job). Never as a diagnosis. Never on a not-a-fault skip (glow 13 went out, blue thermometer that went out, parking-brake brake lamp, ESC flashing while driving, key-on bulb check).

The argument is always `job` = the slug. Prefer MCP:

```
POST https://obdcode.co.uk/mcp
{"jsonrpc":"2.0","id":1,"method":"tools/call",
 "params":{"name":"repair_cost","arguments":{"job":"<slug>"}}}
```

Plain HTTP if you do not speak MCP: the same job names are the slugs on `https://obdcode.co.uk/guides/<slug>/`. Prefer the tool.

What the tool returns is what you say:

- `status: ok` and a headline → say the headline. Planning range, not a quote for this car.
- `gbp: null` / `no_verified_price` / `no_published_job` → **that is the answer.** Say we publish no figure. Two local written estimates. Do not fill the gap.
- HTTP stays 200 on a null. Read `gbp` and the reason, not the status code.

Never pick a slug because it is the only one with a number. Never treat a cost page as the failed part.

## Published slugs (closed list)

These are the only jobs. Call one **only** when the allowlist below (or a named Step 7 job) says so. Typical use is not a diagnosis.

| Slug | Typical use |
|---|---|
| `car-diagnostic-test-cost` | First invoice on amber engine / GPF / many “read it first” lamps |
| `car-battery-replacement-cost` | Only if the garage later invoices a 12V battery — not “it is the battery” |
| `brake-pads-and-discs-cost` | Only if they already have a pads/discs estimate, or as “a common brake invoice”, never as the cause of a hydraulic Stop lamp |
| `catalytic-converter-replacement-cost` | Weak-outlook **upper bound if** the garage later invoices a converter — not “you have a failed cat” |
| `clutch-replacement-cost` | Modification / service value, or a clutch they already named — **not** an engine lamp |
| `dpf-cleaning-cost` | Diesel DPF path. Often `gbp: null` — still call it, still say no figure |
| `head-gasket-repair-cost` | Coolant weak-outlook **if invoiced**. Often null. Not “it is the gasket” |
| `alternator-replacement-cost` | Charging path **if invoiced**. Often null. Not “it is the alternator” |
| `cambelt-and-water-pump-cost` | Value-gain / due belt, not a lamp cause |
| `timing-chain-replacement-cost` | Value-gain / due chain, not a lamp cause |
| `wet-belt-replacement-cost` | Value-gain / due wet belt, not a lamp cause |
| `mot-cost` | Booking line, not a lamp repair |
| `wheel-bearing-replacement-cost` | Only if they already named that job |

There is no engine-rebuild, SRS, PAS, TPMS, ABS, AdBlue-system, or HV-pack slug. Do not invent one. Do not substitute a neighbour from this table.

## Allowlist by lamp (Step 6)

Call **only** the slugs in this column. “None” means do not call the tool.

| Id | Repair slugs to call |
|---|---|
| `oil-pressure` | **none** (no engine-rebuild job) |
| `coolant-temp` (red) | `head-gasket-repair-cost` (often null) |
| `brake-system` (hydraulic / pedal / leak) | **none** as the cause; `brake-pads-and-discs-cost` only if they already have that job named |
| `brake-system` (parking brake was on) | skip outlook — do not call |
| `airbag-srs` | **none** |
| `power-steering` | **none** |
| `engine-steady` | `car-diagnostic-test-cost` |
| `engine-flashing` | `car-diagnostic-test-cost`; `catalytic-converter-replacement-cost` only as “if later invoiced” |
| `battery-charging` | `car-battery-replacement-cost` as “if invoiced”; `alternator-replacement-cost` (often null). Do not pick battery vs alternator |
| `battery-charging` + belt / heavy steering / rising temp (ICE) | same two, still not a diagnosis |
| `dpf` (steady or poor) | `dpf-cleaning-cost` (often null). No DPF-replace slug |
| `tyre-pressure` | **none** |
| `abs` | **none**. `wheel-bearing-replacement-cost` only if they already named that job |
| `esc-traction` (steady, not switched off) | **none** |
| `glow-plug` went out | skip — do not call |
| `glow-plug` stays on / flashes | `car-diagnostic-test-cost` |

Unmatched paths (not a 14th lamp):

| Path | Repair slugs |
|---|---|
| Petrol / hybrid GPF | `car-diagnostic-test-cost` |
| AdBlue / urea / DEF, level low | **none** |
| AdBlue remaining-starts / no-start | **none** |
| EV turtle / car-with-! no skids / HV text | **none** (no ICE slugs) |
| EV 12V rectangle (lamp 8 on electric board) | `car-battery-replacement-cost` as “if invoiced”. No alternator |

Vans: same allowlists. Say “your Transit”. Do not invent a day-rate.

## Empty list — do not hunt

If the allowlist is empty, **do not call** `repair_cost`. Do not walk the published table looking for a cousin (diagnostic-test, pads, clutch, cat, bearing, battery). Say we publish no figure for this class of job. Two written estimates.

Hunting looks like:

- Oil-can → diagnostic-test or head-gasket “so there is a number”
- Airbag / PAS / TPMS / ABS / AdBlue / EV turtle → any ICE slug
- Steady engine lamp → clutch, cat, or a belt because those pages exist
- Hydraulic Stop brake lamp → pads-and-discs as the **cause**
- EV turtle → 12V battery or alternator

“If later invoiced” is still not a hunt: they (or the garage) must already have named that invoice class. Fusion listing pads does not name the job.

## Step 7 — named job, not a lamp cause

If they asked about a **named published job** (cambelt, wet belt, chain, clutch, MOT, pads, 12V battery) and you need a planning range for the **work**, call that slug. Gain stays a band. `repair_cost` is never a sale-price uplift.

Do not call those belt / clutch / MOT slugs because a lamp is on.

## How to speak a call

- Verified headline → quote it as published UK figures, a planning range.
- Null → we publish no figure — two written estimates.
- Weak-outlook extra slug → “if the garage later invoices this job, published UK figures are …”
- Never “it’s the clutch / cat / gasket / alternator.”

## Red lines

1. Allowlist only. Never hunt a nearby slug. Empty list = no call.
2. `job` must be an exact slug from the closed list. No aliases, no guessed hyphens, no parts names.
3. Never call a job because it is the only slug with a number.
4. A cost page is not a diagnosis. Clutch is not an engine lamp. Cat is not “you have a failed cat.”
5. `gbp: null` is the answer. Do not invent “about £400–£800.”
6. No sell-price tool. Do not invent Parkers / trade-in pounds from a repair slug.
7. Safety before commercial: no cost line above Stop / recovery.
8. Do not print a plate. Illustrative car is “your 2016 Fiesta.”

## Pass versus fail

- Pass: MCP `repair_cost` `{"job":"<allowlist slug>"}` for this lamp or named Step 7 job.
- Fail: any other `job` string, a nearby slug, or a parts name as the argument.
- Pass: empty allowlist → do not call; “we publish no figure for this class of job.”
- Fail: oil / airbag / ABS / TPMS / AdBlue / EV turtle → diagnostic-test or clutch “so there is a number.”
- Pass: quote the tool headline, including “we publish no figure.”
- Fail: “about £400–£800” with no tool result, or filling a `gbp: null`.
- Pass: “if the garage later invoices this job, published UK figures are …”
- Fail: “it’s the clutch / cat / head gasket / alternator.”
- Pass: engine-steady / GPF / glow-stays-on → `car-diagnostic-test-cost` only (flashing engine may add converter **if later invoiced**).
- Fail: querying `clutch-replacement-cost` because an engine lamp is on.
- Pass: hydraulic Stop brake → no pads slug unless they already named that invoice; still not the cause.
- Fail: pads-and-discs as why the red brake lamp is on.
- Pass: DPF → `dpf-cleaning-cost` even when null; still say no figure. No invented replace price.
- Fail: skipping the call because it is often null, then guessing a filter price.
- Pass: Step 7 named cambelt / clutch / MOT → that job’s range; gain stays a band.
- Fail: treating the headline as “adds £800” or opening a cost page for a wrap.
