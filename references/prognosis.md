# Repair-or-sell outlook (愈后)

OBDCode’s core is **what happens after the lamp**, not a parts guess.

After the fault statement (SKILL Step 5), give one outlook. Do not diagnose. Do not name the failed part. Do not invent pounds.

Two other files sit next to this one:

- Per-lamp defaults: `references/prognosis-cards.md`
- No lamp, modification / service / presentation work: `references/value-gain.md` (skill states **sale-price effect only**)

Notes under `references/prognosis/deep/` are optional. If they disagree with this file, this file wins. Do not load the whole deep folder in a live chat.

## When this step runs

Run it when there is a **real fault**. Skip it when Step 5 already ended as not-a-fault:

- Glow 13 came on with ignition and went out
- Thermometer was **blue** and then went out
- Brake lamp with the parking brake / EPB / Auto Hold still on, and the pedal is normal
- ESC / traction **flashing while driving** (the system is working)
- Key-on bulb check that went out

If they also describe modification or service work, finish this outlook first (safety), then a separate **[Value]** block from `value-gain.md`.

## Three buckets the owner hears

| Bucket | When | What you say |
|---|---|---|
| **Close it yourself** | Outlook is good **and** either a driveway action is owner-safe, or a **small OBD device** (sold at obdcode.co.uk when a reader is on the shelf, or one they already own) changes the next step | How to close it. Device steps only on `device`. No cats, brakes, airbags, lifting, structural work |
| **Garage, cost in range** | A workshop can usually put the car right without writing it off | Approximate **repair** cost if `repair_cost` returns a verified figure |
| **Weak outlook** | The job may be large, and even a successful repair often leaves a car that is hard to sell | **Repair** cost (if verified) **and** how to get a **sell** figure. Never invent a used-car price |

Internal labels: `owner` · `device` · `garage` · `poor`. Speech maps `owner` and `device` to **Close it yourself**.

## Order in the reply

1. Spoken fault statement (~60–80 words), including **[Drive advice]**
2. Spoken **[Outlook]** (~40–60 words)
3. Device or shop links **below** Stop / recovery. Never above a Stop line
4. Then stop. Do not diagnose if they ask “so what part is it?”

## Spoken outlook

```
[Outlook]     Close it yourself / A garage can usually handle this / Repair may cost more than the car
[Repair]      Verified headline from repair_cost, or: we publish no figure — two written estimates
[Sell]        Only on weak outlook: we publish no used-car price. Get one bid as it sits, and compare it with the estimate
[Close it]    Only on Close it yourself: the driveway or scan steps. Never on Red-class work
```

Pass versus fail:

- Pass: “a scan is the next step; the lamp does not name the part.”
- Fail: “it’s the clutch / cat / head gasket / alternator.”
- Pass: quote `repair_cost` headline, including “we publish no figure.”
- Fail: “about £400–£800” with no tool result.
- Pass: “if the garage later invoices this job, published UK figures are …”
- Fail: querying clutch cost because an engine lamp is on.

## Money rules

### Repair

Call `repair_cost` only with a slug from this file’s allowlist for **this lamp** (or unmatched path).

```
POST https://obdcode.co.uk/mcp
{"jsonrpc":"2.0","id":1,"method":"tools/call",
 "params":{"name":"repair_cost","arguments":{"job":"<slug>"}}}
```

Plain HTTP if you do not speak MCP: the same job names are the slugs on `https://obdcode.co.uk/guides/<slug>/`. Prefer the tool.

- `status: ok` and a headline → say the headline. It is a planning range, not a quote for this car.
- `gbp: null` / `no_verified_price` / `no_published_job` → **that is the answer.** Say we publish no figure. Tell them to ask two local garages for a written estimate. Do not fill the gap.
- Never call a job because it is the only slug with a number.
- Never treat a cost page as a diagnosis.

Published jobs (call only when the allowlist says so):

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

If the allowlist is empty, do not hunt a nearby slug. Say we publish no figure for this class of job.

### Sell

There is **no** sell-price tool. Do not invent Parkers / WeBuyAnyCar / “typical trade-in” pounds.

On **weak outlook** only:

1. Repair: verified figure or “no published figure.”
2. Sell: get **one** instant-sale or dealer bid **as the car sits** (runner, or for parts if it must not be driven). Get **one** written garage estimate.
3. If the estimate is larger than the bid, selling is often the better outlook.
4. Recovery / collection is part of the sell cost when **[Drive advice]** is Stop. Do not invent that fee either.

On garage / close-it-yourself: do not push selling.

## Device and driveway rules

**Close it yourself** is allowed only when **both** are true:

1. Outlook is good (not `poor`)
2. Either `owner` (Green / handbook / fluid that is meant to be topped up) or `device` (a small reader changes the next step)

A reader **does not** fix oil pressure, a hot engine, a hydraulic brake lamp, an airbag, or a flashing engine lamp. Do not describe scan-tool forced DPF regen. Do not clear codes as a repair.

Scanner shops on the site are sometimes **off the shelf**. Link `https://obdcode.co.uk/guides/best-obd2-scanner-uk/` and `https://obdcode.co.uk/tools/scanners/` as how-to-choose, not as a fake in-stock SKU. If they already own a reader, use that. A published diagnostic test (`car-diagnostic-test-cost`) is the garage-cost alternative.

Device steps, when allowed:

1. Plug in with the ignition in the handbook position, engine off unless the reader says otherwise
2. Read **stored codes and freeze frame**
3. Write them down for the garage
4. Do **not** clear the lamp
5. Fuel cap clicked tight on a steady engine lamp is the only extra driveway check

## Default bucket by lamp

Full copy: `references/prognosis-cards.md`. Do not upgrade `garage` to `poor` because the car is old unless they already have a large estimate, or the lamp is in the weak-outlook column below.

| Id | Default | Repair slugs to call | Close-it-yourself |
|---|---|---|---|
| `oil-pressure` | `poor` | none (no engine-rebuild job) | Dipstick once **cold** is information, not a close |
| `coolant-temp` (red) | `poor` | `head-gasket-repair-cost` (often null) | Coolant level once **cold** is information, not a close |
| `brake-system` (hydraulic / pedal / leak) | `poor` | none as the cause; `brake-pads-and-discs-cost` only if they already have that job named | No |
| `brake-system` (parking brake was on) | skip | — | Not a fault |
| `airbag-srs` | `garage` | none | No |
| `power-steering` | `garage` | none | No |
| `engine-steady` | `device` then `garage` | `car-diagnostic-test-cost` | Scan + fuel cap. Not parts |
| `engine-flashing` | `poor` | `car-diagnostic-test-cost`; `catalytic-converter-replacement-cost` only as “if later invoiced” | No |
| `battery-charging` | `garage` | `car-battery-replacement-cost` as “if invoiced”; `alternator-replacement-cost` (often null) | No. Do not pick battery vs alternator |
| `battery-charging` + belt / heavy steering / rising temp (ICE) | `poor` | same, still not a diagnosis | No |
| `dpf` steady, driving normally | `owner` then `garage` | `dpf-cleaning-cost` (often null) | One handbook regen. Not a scan-tool regen |
| `dpf` flash / limp / oil over max | `poor` | `dpf-cleaning-cost` | No more motorway loops |
| `tyre-pressure` simply on | `owner` | none | Inflate to the **placard**, inspect, reset |
| `tyre-pressure` flash-then-steady | `garage` | none | Pressures first; then garage |
| `abs` | `garage` | none | No hydraulics |
| `esc-traction` steady, not switched off | `garage` | none | Toggle the button first |
| `glow-plug` went out | skip | — | Not a fault |
| `glow-plug` stays on / flashes | `garage` | `car-diagnostic-test-cost` | No |

Unmatched paths (not a 14th lamp):

| Path | Default | Repair slugs | Close-it-yourself |
|---|---|---|---|
| Petrol / hybrid GPF (exhaust-dots, not DPF) | `device` then `garage` | `car-diagnostic-test-cost` | Scan. No diesel regen copy |
| AdBlue / urea / DEF, level low | `owner` | none | Correct fluid, handbook filler. Not 9 or 6 |
| AdBlue remaining-starts / no-start | `poor` | none | No |
| EV turtle / car-with-! no skids / HV text | `garage` | none (no ICE slugs) | No. Not 12 or 8 |
| EV 12V rectangle (lamp 8 on electric board) | `garage` | `car-battery-replacement-cost` as “if invoiced” | No belt combo |

Vans: same buckets. Say “your Transit”. Downtime is part of outlook speech (“a day off the road”), not a made-up day-rate.

## Weak outlook without a sell number

Still give the **decision rule**. A missing pound is not a missing outlook.

Do not say the car is a write-off. Say the repair may cost more than a buyer will pay for it as it sits, so they should put an estimate next to a bid before they authorise the job.

## After the outlook

If they ask what is wrong: this skill does not diagnose.

If they ask recovery, scan, keep-driving, or repair-vs-sell: restate **[Drive advice]** and **[Outlook]**.

If they ask how to wrap, remap, or delete a filter: that is not this step. Value-gain may state the **price effect** and refuse the how-to.
