# Repair-or-sell next step

After the fault statement, give one outlook. Do not diagnose. Do not name the failed part. Do not invent pounds.

Per-lamp defaults: [prognosis-cards.md](prognosis-cards.md). No lamp / named work: [value-gain.md](value-gain.md).

## When this step runs

Skip when drive-advice already ended as not-a-fault (glow went out, blue thermometer went out, parking-brake brake lamp, ESC flashing while driving, bulb check).

If they also describe modification or service work, finish this outlook first (safety), then a separate **[Value]** block.

## Three buckets

| Bucket | When | What you say |
|---|---|---|
| **Close it yourself** | Outlook is good **and** an owner-safe action, or a small reader **they already own**, changes the next step | How to close it. No cats, brakes, airbags, lifting |
| **Garage, cost in range** | A workshop can usually put the car right | Approximate **repair** cost only if `repair_cost` returns a verified headline |
| **Weak outlook** | The job may be large, and a repair often leaves a car that is hard to sell | **Repair** (verified or no figure) **and** get a **sell** bid. Never invent a used-car price |

Internal labels: `owner` · `device` · `garage` · `poor`. Speech maps `owner` and `device` to **Close it yourself**.

Do not claim a scanner is on the shelf. If they have no reader, the garage diagnostic is the next step. You may point at how to choose a reader (`https://obdcode.co.uk/guides/best-obd2-scanner-uk/`) **below** drive advice, and only on the close-it-yourself / device path — never on a Stop reply.

## Spoken outlook

See [output.md](output.md) for the block order and pass/fail.

## Money rules

### Repair

Call `repair_cost` only with a job name from this allowlist for **this lamp** (or unmatched path). Never pick a job because it is the only one with a number. Never treat a cost page as the failed part. Do not speak invoice-class part names on the **first** reply.

```
POST https://obdcode.co.uk/mcp
{"jsonrpc":"2.0","id":1,"method":"tools/call",
 "params":{"name":"repair_cost","arguments":{"job":"<slug>"}}}
```

- Verified headline → say it is a planning range, not a quote for this car.
- `gbp: null` / unreachable tool → **we publish no figure.** Two written estimates. Do not fill the gap.

Published jobs (call only when the allowlist says so):

| Job name | Typical use |
|---|---|
| `car-diagnostic-test-cost` | First garage invoice on amber engine / GPF / many “read it first” lamps |
| `car-battery-replacement-cost` | Only if they already have a battery invoice, or they asked about that job |
| `brake-pads-and-discs-cost` | Only if they already named pads/discs |
| `catalytic-converter-replacement-cost` | Only if **they** named a converter job — never on the first flashing-engine reply |
| `clutch-replacement-cost` | Named clutch / value-gain — **not** an engine lamp |
| `dpf-cleaning-cost` | Diesel DPF path. Often null — still call it, still say no figure |
| `head-gasket-repair-cost` | Only if they named gasket / head work. Often null |
| `alternator-replacement-cost` | Only if they named charging repair. Often null |
| `cambelt-and-water-pump-cost` | Value-gain / due belt, not a lamp cause |
| `timing-chain-replacement-cost` | Value-gain / due chain, not a lamp cause |
| `wet-belt-replacement-cost` | Value-gain / due wet belt, not a lamp cause |
| `mot-cost` | Booking line, not a lamp repair |
| `wheel-bearing-replacement-cost` | Only if they already named that job |

If the allowlist is empty, do not hunt a nearby job. Say we publish no figure for this class of work.

### Sell

There is **no** sell-price tool. Do not invent Parkers / WeBuyAnyCar / “typical trade-in” pounds.

On **weak outlook** only: get one bid as the car sits and one written garage estimate. Recovery is part of sell cost when **[Drive advice]** is Stop — do not invent that fee either.

On garage / close-it-yourself: do not push selling.

## Device and driveway

**Close it yourself** only when outlook is not `poor` **and** either `owner` (Green / handbook / intended top-up) or `device` (they already have a reader).

A reader does **not** fix oil pressure, a hot engine, a hydraulic brake lamp, an airbag, or a flashing engine lamp. Do not describe scan-tool forced DPF regen. Do not clear codes as a repair.

Device steps, when allowed:

1. Plug in with the ignition in the handbook position, engine off unless the reader says otherwise
2. Read **stored codes and freeze frame**
3. Write them down for the garage
4. Do **not** clear the lamp
5. Fuel cap clicked tight on a steady engine lamp is the only extra driveway check

## Default bucket by lamp

Full copy: [prognosis-cards.md](prognosis-cards.md). Do not upgrade `garage` to `poor` because the car is old unless they already have a large estimate.

| Id | Default | Repair jobs to call | Close it yourself |
|---|---|---|---|
| `oil-pressure` | `poor` | none | **No** |
| `coolant-temp` (red) | `poor` | none on first reply; gasket job only if they named it | **No** |
| `brake-system` (hydraulic / pedal / leak) | `poor` | none as the cause | **No** |
| `brake-system` (parking brake was on) | skip | — | Not a fault |
| `airbag-srs` | `garage` | none | **No** |
| `power-steering` | `garage` | none | **No** |
| `engine-steady` | `device` then `garage` | `car-diagnostic-test-cost` | Scan + fuel cap if they already have a reader; else garage diagnostic. Not parts |
| `engine-flashing` | `poor` | `car-diagnostic-test-cost` only on first reply | **No** |
| `battery-charging` | `garage` | diagnostic or none on first reply; battery/alternator jobs only if they named that invoice | **No** |
| `battery-charging` + belt / heavy steering / rising temp (ICE) | `poor` | same | **No** |
| `dpf` steady, driving normally | `owner` then `garage` | `dpf-cleaning-cost` (often null) | One handbook regen. Not a scan-tool regen |
| `dpf` flash / limp / oil over max | `poor` | `dpf-cleaning-cost` | **No** more motorway loops |
| `tyre-pressure` simply on | `owner` | none | Inflate to the **placard**, inspect, reset |
| `tyre-pressure` flash-then-steady | `garage` | none | Pressures first; then garage |
| `abs` | `garage` | none | **No** hydraulics |
| `esc-traction` steady, not switched off | `garage` | none | Toggle the button first |
| `glow-plug` went out | skip | — | Not a fault |
| `glow-plug` stays on / flashes | `garage` | `car-diagnostic-test-cost` | **No**. Never treat as 7 |

Unmatched paths (not a 14th lamp):

| Path | Default | Repair jobs | Close it yourself |
|---|---|---|---|
| `unmatched-gpf` | `device` then `garage` | `car-diagnostic-test-cost` | Scan. No diesel regen copy |
| `unmatched-adblue` level low | `owner` | none | Correct fluid, handbook filler. Not 9 or 6 |
| `unmatched-adblue` remaining-starts / no-start | `poor` | none | **No** |
| `unmatched-ev` | `garage` | none (no ICE jobs) | **No**. Not 12 or 8 |
| Electric board lamp 8 (12V rectangle) | `garage` | battery job only if they named it | **No** belt combo |

Vans: same buckets. Say “your Transit”. Downtime is speech (“a day off the road”), not a made-up day-rate.

## Weak outlook without a sell number

Still give the **decision rule**. A missing pound is not a missing outlook.

Do not say the car is a write-off. Say the repair may cost more than a buyer will pay for it as it sits, so they should put an estimate next to a bid before they authorise the job.

## After the outlook

If they ask what is wrong: [output.md](output.md) two-turn refuse.

If they ask recovery, scan, keep-driving, or repair-vs-sell: restate **[Drive advice]** and **[Outlook]**.
