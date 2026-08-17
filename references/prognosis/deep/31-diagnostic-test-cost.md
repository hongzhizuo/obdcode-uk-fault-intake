# 31 · When to call `car-diagnostic-test-cost`

Not a second SKILL. If this note disagrees with `SKILL.md`, `references/prognosis.md`, or `references/prognosis-cards.md`, those three win. Do not diagnose. Do not add a 14th lamp id.

This slug is the **first garage invoice class**: a scan. It is not a failed part. Live chats **must** call `repair_cost` and speak that turn’s result. **This file must not freeze a pound figure as always-true.** Do not copy a remembered £ amount into speech or into this note.

---

## When

Call `repair_cost` with `job` = `car-diagnostic-test-cost` only when **this lamp’s (or unmatched path’s) allowlist says so**. The four paths that do:

| Path | Bucket | Why this slug |
|---|---|---|
| **`engine-steady` (6)** | `device` then `garage` | Always call it for the **garage** path. A reader they already own (or a how-to-choose link) is Close it yourself; the published diagnostic test is the garage-cost alternative. Scan + fuel cap. Not parts. |
| **Unmatched petrol / hybrid GPF** | `device` then `garage` | Exhaust-dots / pick of 9 on a petrol or hybrid board. **This slug only.** Scan. No diesel DPF regen copy. Not lamp 9 on a diesel board. |
| **`glow-plug` (13) stays on or flashes while running** | `garage` | A scan is the first invoice. There is **no** glow-plug slug. Do not invent a set-of-four price. |
| **`engine-flashing` (7)** | `poor` | First invoice is still a diagnostic test. Stop / recovery already sits in **[Drive advice]**. A reader does not close this. You may add `catalytic-converter-replacement-cost` only as “if the garage later invoices a converter,” never as today’s diagnosis. |

Skip the call (and skip Step 6) when glow 13 came on with ignition and **went out** — not a fault.

Do **not** call this slug because you want a number on another card. Empty allowlist → say we publish no figure for this class of job. Do not hunt a nearby slug.

**Off this slug** (use the card’s own allowlist, or none):

- `oil-pressure`, red `coolant-temp`, hydraulic `brake-system`, `airbag-srs`, `power-steering`
- `battery-charging` (battery / alternator **if invoiced**, not a scan page as the cause)
- Diesel `dpf` (`dpf-cleaning-cost`, often null)
- `tyre-pressure`, `abs`, `esc-traction`
- AdBlue / EV unmatched / EV 12V rectangle
- Key-on bulb check, blue thermometer that went out, parking-brake-on brake lamp, ESC flashing while driving

Never call this job because it is the only published slug with a number.

---

## How to call (live)

Prefer the tool. Same turn as **[Outlook]** / **[Repair]**, after **[Drive advice]**. Never above a Stop line.

```
POST https://obdcode.co.uk/mcp
{"jsonrpc":"2.0","id":1,"method":"tools/call",
 "params":{"name":"repair_cost","arguments":{"job":"car-diagnostic-test-cost"}}}
```

Plain HTTP if you do not speak MCP: the same job name is the slug on `https://obdcode.co.uk/guides/car-diagnostic-test-cost/`. Prefer the tool.

Speak the **live** result only:

- `status: ok` and a headline → say that headline. Planning range, not a quote for this car.
- `gbp: null` / `no_verified_price` / `no_published_job` → **that is the answer.** We publish no figure. Ask two local garages for a written estimate. Do not fill the gap.

Do not cache yesterday’s pounds in this file or in the next chat.

---

## Slugs

| Slug | On these paths | How to speak it |
|---|---|---|
| `car-diagnostic-test-cost` | All four rows above | First invoice: a scan. Quote the live headline, or “we publish no figure.” Not a diagnosis. |
| `catalytic-converter-replacement-cost` | **`engine-flashing` only**, optional add | **Only** “if the garage later invoices a converter.” Weak-outlook upper bound. Never “you have a failed cat.” |

Do **not** call with this lamp / path:

- `clutch-replacement-cost`, `cambelt-and-water-pump-cost`, `timing-chain-replacement-cost`, `wet-belt-replacement-cost` — not an engine-lamp cause
- `dpf-cleaning-cost` on petrol/hybrid GPF
- A glow-plug, lambda, coil, or “set of four” job — none of those are published for these cards
- Cat / clutch / belt because a **steady** engine lamp or GPF is on

A cost page is not the failed part.

---

## Pass versus fail

**Pass**

- Call `repair_cost` `car-diagnostic-test-cost` on engine-steady (garage alternative), GPF, glow that stays on or flashes, and flashing engine as the **first** invoice.
- “A scan is the next step; the lamp does not name the part.”
- Quote this turn’s headline, including “we publish no figure.”
- “If the garage later invoices this job, published UK figures are …” — only after a live result, and on flashing only for the converter as a later invoice.
- GPF: this slug only; scan; no regen copy.
- Glow stays on / flashes: this slug; no DIY plug set price.
- Flashing: Stop first; diagnostic slug; converter only as “if later invoiced.”
- Engine-steady: fuel cap + reader close if they have one; still call this slug for the garage path.
- `gbp: null` spoken as no published figure. Two written estimates. Do not invent.

**Fail**

- “About £400–£800” (or any pounds) with no tool result, or a figure copied from this file.
- Freezing a diagnostic fee in this note as always-true.
- “It’s the clutch / cat / head gasket / alternator / glow plugs.”
- Querying clutch, cat, or belt cost because an engine lamp is on (cat on flashing only as later-invoice upper bound).
- Calling this slug on oil, hot coolant, hydraulic brakes, DPF, AdBlue, or EV so there is a number.
- Treating the diagnostic-cost page as the diagnosis.
- Glow that went out after start: still calling a scan fee.
- GPF spoken as diesel DPF cleaning / motorway regen.
- Shop or scanner links above Stop / recovery on the flashing path.
- “Clear the codes” as a cheaper alternative to the test.
