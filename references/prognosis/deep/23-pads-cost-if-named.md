# 23 · `brake-pads-and-discs-cost` only if named

Not a second SKILL. If this note disagrees with `SKILL.md`, `references/prognosis.md`, `references/prognosis-cards.md`, or `references/value-gain.md`, those four win. Do not diagnose. Do not invent pounds. Do not add a 14th lamp id.

This slug is a **common brake invoice class**. It is not today’s failed part. Live chats **must** call `repair_cost` and speak that turn’s result. **This file must not freeze a pound figure as always-true.**

---

## When

Call `repair_cost` with `job` = `brake-pads-and-discs-cost` only when **one** of these is true:

1. **They already named that job** — they said the garage quoted pads and discs, they already have a pads/discs estimate, or they asked what that invoice usually costs.
2. **Value-gain / no lamp** — they named pads and discs as service or presentation work (SKILL Step 7). Then the slug is the **job’s** published range. Sale-price effect stays the **Modest** band. Spend is not uplift.

Speak it as invoice class: “if the garage later invoices pads and discs, published UK figures are a planning range” / “a common brake invoice.” Never “the lamp is the pads.”

Do **not** call this slug as the **cause** of a hydraulic Stop lamp (`brake-system` with parking brake / EPB / Auto Hold fully off, or spongy pedal / pull / leak). Lamp 3’s allowlist is **empty as a cause**. If they have not named pads and discs: we publish no figure for hydraulic / ABS-combined brake-lamp work. Two written estimates. Do not hunt this slug because it has a number.

Lamp 3 exception: they **already** said the garage quoted pads and discs. You may then call this slug as that **invoice class** only. Still not a diagnosis. Still Stop / recovery first. Still no driveway pads.

Never pick this job because MOT fusion listed discs or pads. History notes end: **this does not show the cause of today’s lamp.**

---

## How to call (live)

Prefer the tool. Same turn as **[Repair]** (or the Step 7 job range). After **[Drive advice]**. Never above a Stop line.

```
POST https://obdcode.co.uk/mcp
{"jsonrpc":"2.0","id":1,"method":"tools/call",
 "params":{"name":"repair_cost","arguments":{"job":"brake-pads-and-discs-cost"}}}
```

Plain HTTP if you do not speak MCP: the same job name is the slug on `https://obdcode.co.uk/guides/brake-pads-and-discs-cost/`. Prefer the tool.

Speak the **live** result only:

- `status: ok` and a headline → say that headline. Planning range, not a quote for this car, not a named failed part.
- `gbp: null` / `no_verified_price` / `no_published_job` → **that is the answer.** We publish no figure. Two written local estimates. Do not fill the gap.

Do not cache yesterday’s pounds in this file or in the next chat.

---

## Off this slug

Do **not** call `brake-pads-and-discs-cost` because:

- A red brake lamp is on (hydraulic Stop) and they have **not** named pads and discs
- You want a number for lamp 3, 11 ABS, or any other empty allowlist
- Fusion / MOT listed pads, discs, pipes, or hoses
- An engine, DPF, charging, oil, coolant, airbag, or steering lamp is on
- ABS-only (11) is on — do not treat pads as the ABS cause. Wheel-bearing is a **different** slug, and only if they already named that job
- Parking brake / EPB / Auto Hold was still on and the pedal is normal — not a fault; skip Step 6; no slug

A cost page is not a diagnosis. Close-it-yourself is **no** pads, no discs, no lifting, no bleeding — even after they named the invoice.

Value-gain (no lamp): pads and discs with invoice is **Modest** — expected wear; proof helps; it rarely adds a premium. The slug is still not a **gain** in pounds.

---

## Pass versus fail

**Pass**

- Call this slug only after they already named pads and discs, or as a common invoice class on a job they asked about.
- “If the garage later invoices pads and discs, published UK figures are …” — live `repair_cost` headline, or “we publish no figure.”
- Hydraulic Stop lamp, job **not** named: no slug. We publish no figure for this class of brake work. Two written estimates. Bid as it sits; recovery is part of sell cost.
- Hydraulic Stop lamp, they **already** have a pads-and-discs quote: call as **invoice class** only. Still not “the lamp is the pads.” Stop / recovery stays above the cost line.
- Step 7: Modest band; their invoice is spend; slug is the job range, not sale-price uplift.
- MOT pads/discs note: prior context only; **this does not show the cause of today’s lamp.**
- No driveway pads. Restate Stop and the weak outlook if they ask repair vs sell.

**Fail**

- Calling `brake-pads-and-discs-cost` because a hydraulic Stop lamp is on, as the cause.
- “It’s the pads / discs / calipers.” / “The brake lamp means you need pads.”
- Calling this slug because an old MOT listed pads or discs.
- Calling this slug on ABS, engine, oil, coolant, or any lamp that did not name that job.
- “About £400–£800” (or any pounds) with no tool result, or a figure copied from this file.
- Treating the pads-and-discs cost page as today’s diagnosis.
- Bleed / pad-change / lift how-to, or “fit pads and the Stop lamp will go out.”
- Invented gain: “pads add £300 to the sale price.”
- Shop or parts link above Stop / recovery.
- Naming a likely part when they ask what is wrong.
