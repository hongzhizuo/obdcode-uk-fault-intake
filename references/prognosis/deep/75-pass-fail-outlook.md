# 75 · Pass versus fail (Step 6 outlook)

Not a second SKILL. If this note disagrees with `SKILL.md`, `references/prognosis.md`, or `references/prognosis-cards.md`, those three win. Do not diagnose. Do not invent pounds. Do not add a 14th lamp id.

Compact checklist for the spoken **[Outlook]** / **[Repair]** / **[Sell]** / **[Close it]** after the fault statement. Score the eight classic misses below. Live rules win.

---

## Inventing pounds

- Pass: quote the `repair_cost` headline, including “we publish no figure — two written estimates.”
- Pass: `gbp: null` / `no_verified_price` / `no_published_job` is the answer. Empty allowlist: same line, do not hunt a nearby slug.
- Pass: weak outlook — get **one** bid as it sits and **one** written estimate. No used-car API; no invented recovery fee.
- Fail: “about £400–£800” (or any range) with no tool result.
- Fail: filling a null with Parkers, WeBuyAnyCar, “typical trade-in,” a rebuild guess, a tyre-bill guess, or a made-up day-rate.

## Naming parts

- Pass: “a scan is the next step; the lamp does not name the part.”
- Pass: “if the garage later invoices this job, published UK figures are …” — a cost page is a planning range, not today’s failed part.
- Fail: “it’s the clutch / cat / head gasket / alternator.”
- Fail: “likely a failing catalytic converter,” “cylinder 3,” “sensor, reluctor, or wiring,” “soot-loaded or ash-loaded.”
- Fail: “it’s the cat, about £500” (named part **and** invented pounds).

## Clutch for an engine lamp

- Pass: `engine-steady` / `engine-flashing` → call `car-diagnostic-test-cost`. Converter only as “if later invoiced” on the flashing / weak path. Never clutch, cambelt, chain, or wet-belt because the engine outline is on.
- Pass: `clutch-replacement-cost` only when they already named a clutch job, or on Step 7 value-gain for that work — still not a **gain** in pounds, and still not a lamp cause.
- Fail: querying `clutch-replacement-cost` because lamp 6 or 7 is on.
- Fail: “it’s the clutch” on an engine lamp. A cost slug is not a diagnosis.

## Sell on TPMS

- Pass: simply on → **Close it yourself**. Cold pressures to the **placard**, inspect, handbook reset. No **[Sell]** block.
- Pass: flash-then-steady after correct pressures → **A garage can usually handle this.** No TPMS slug. We publish no figure. Still no sell.
- Fail: “sell it, TPMS isn’t worth fixing.”
- Fail: invented tyre or sensor pounds as a sell comparison. Close-it-yourself and garage outlooks do not push selling.

## DIY on oil

- Pass: red oil-can is `poor`. Stop. Do not drive it in. Recovery or collection. Repair may cost more than the car. We publish no engine-rebuild figure. Bid as it sits (not a runner). A cold dipstick is **information**, not a close. Do not restart.
- Fail: “top it up and go,” “level is fine, you’re safe to restart,” “drive it slowly to the garage.”
- Fail: naming the pump, sender, or a bearing. DIY switch or pressure-test steps.
- Fail: a reader, a code clear, or any driveway close. Close-it-yourself never covers Red-class oil work.

## Clearing codes

- Pass: on a `device` path — stored codes **and** freeze frame, written down, **do not clear**. Fuel cap clicked only on steady engine.
- Pass: TPMS / airbag / flashing engine / oil — no scan-tool clear as a fix.
- Fail: “clear it and see if it comes back.”
- Fail: treating a cleared lamp as a repair. Never advise clearing a lamp as a fix.

## Forced regen

- Pass: diesel DPF, steady, driving normally → **one** handbook regen. Not enclosed. Oil-level check. If one count does not clear it → garage; call `dpf-cleaning-cost` (often null — still say no figure).
- Pass: DPF flash / limp / oil over maximum → `poor`. No more motorway loops. Bid vs estimate. Do not suggest deletion.
- Pass: petrol / hybrid GPF — scan only. No diesel regen copy.
- Fail: scan-tool forced regen on any path.
- Fail: GPF “do a regen like a diesel DPF.” Fail: “just cut it out.”

## Fake scanner SKU

- Pass: they already own a reader → use that. Else link how-to-choose, and say the category may be **off the shelf**:
  - https://obdcode.co.uk/guides/best-obd2-scanner-uk/
  - https://obdcode.co.uk/tools/scanners/
- Pass: those URLs sit **below** Stop / recovery and below **[Drive advice]**. A published `car-diagnostic-test-cost` is the garage alternative, not a shop SKU.
- Fail: “buy this SKU, in stock today.”
- Fail: a named product as if it were on the shelf. Fail: a scanner or parts link above a Stop line.

---

## Quick score

| Miss | Pass in one line | Fail in one line |
|---|---|---|
| Inventing pounds | Tool headline or “we publish no figure.” | Any guessed GBP, including sell and recovery. |
| Naming parts | The lamp does not name the part. | Clutch / cat / gasket / alternator as today’s fault. |
| Clutch for engine lamp | Diagnostic slug only. Clutch only if they named that job. | `clutch-replacement-cost` because the engine lamp is on. |
| Sell on TPMS | Inflate or garage. No sell block. | “Sell it” or a made-up tyre bill. |
| DIY on oil | Stop. Dipstick is not a close. | Top-up, restart, or reader as a fix. |
| Clearing codes | Read and write. Do not clear. | Clear and see if it returns. |
| Forced regen | One handbook DPF count, or none. | Scan-tool regen, GPF copy, or delete. |
| Fake scanner SKU | How-to-choose; may be off the shelf. | Invented in-stock SKU, or shop above Stop. |

If they ask what is wrong: this skill does not diagnose. If they ask recovery, a scan, keep-driving, or repair-vs-sell: restate **[Drive advice]** and **[Outlook]**. Do not say “continue as a normal assistant.”
