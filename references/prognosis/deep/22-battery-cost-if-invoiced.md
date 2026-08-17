# 22 · When to call `car-battery-replacement-cost` (if invoiced)

Not a second SKILL. If this note disagrees with `SKILL.md`, `references/prognosis.md`, or `references/prognosis-cards.md`, those three win. Do not diagnose. Do not add a 14th lamp id.

This slug is a **later invoice class**: a 12V battery, **if** the garage bills that job. It is **not** today’s failed part. **Lamp 8 is not “it is the battery.”** Live chats **must** call `repair_cost` and speak that turn’s result. **This file must not freeze a pound figure as always-true.** Do not copy a remembered £ amount into speech or into this note.

---

## When

Call `repair_cost` with `job` = `car-battery-replacement-cost` only when **this lamp’s (or unmatched path’s) allowlist says so**, and only as **“if the garage later invoices a 12V battery.”** The paths that do:

| Path | Bucket | Why this slug |
|---|---|---|
| **`battery-charging` (8)** ICE / hybrid rectangle | `garage` | Allowed **if invoiced**. You may also call `alternator-replacement-cost` (often `gbp: null`) as “if they invoice charging repair.” **Do not pick** battery vs alternator. The lamp does not name the part. |
| **`battery-charging` (8)** ICE + belt noise / heavy steering / rising temperature | `poor` | Same two slugs, still **if invoiced**, still **not** a diagnosis. Stop / recovery already sits in **[Drive advice]**. Skip this belt combo on an electric car. |
| **EV board lamp 8** (12V rectangle) | `garage` | **This slug only**, as “if invoiced.” No alternator. No belt story. Turtle / car-with-! (no skids) / HV or charge-plug text is unmatched EV, **not** 8 — do not call this slug there. |
| **Path B / named 12V job** (no lamp, or after the outlook) | sale-price only | They already named a 12V battery job or invoice. Call this slug for the **job’s** published range. Band is usually **Modest**. Still no invented **gain**. Still not “the lamp was the battery.” |

Skip the call (and skip Step 6) when lamp 8 was only a **key-on bulb check** that then went out — not a fault.

Do **not** call this slug because you want a number on another card. Empty allowlist → say we publish no figure for this class of job. Do not hunt a nearby slug.

**Off this slug** (use the card’s own allowlist, or none):

- `oil-pressure`, red `coolant-temp`, hydraulic `brake-system`, `airbag-srs`, `power-steering`
- `engine-steady` / unmatched GPF / `engine-flashing` / `glow-plug` — diagnostic-test (and converter **if later invoiced** on flashing only), not a battery page
- Diesel `dpf` (`dpf-cleaning-cost`, often null)
- `tyre-pressure`, `abs`, `esc-traction`
- AdBlue remaining-starts / unmatched EV turtle / HV text
- Any lamp because this job is the only published slug with a number

Never treat the battery-cost page as the diagnosis of lamp 8.

---

## How to call (live)

Prefer the tool. Same turn as **[Outlook]** / **[Repair]**, after **[Drive advice]**. Never above a Stop line.

```
POST https://obdcode.co.uk/mcp
{"jsonrpc":"2.0","id":1,"method":"tools/call",
 "params":{"name":"repair_cost","arguments":{"job":"car-battery-replacement-cost"}}}
```

Plain HTTP if you do not speak MCP: the same job name is the slug on `https://obdcode.co.uk/guides/car-battery-replacement-cost/`. Prefer the tool.

Speak the **live** result only, and only as invoice class:

- `status: ok` and a headline → “If the garage later invoices a 12V battery, published UK figures are …” then that headline. Planning range, not a quote for this car, **not** “fit a battery.”
- `gbp: null` / `no_verified_price` / `no_published_job` → **that is the answer.** We publish no figure. Ask two local garages for a written estimate. Do not fill the gap.

Do not cache yesterday’s pounds in this file or in the next chat.

On ICE lamp 8 you may also call `alternator-replacement-cost` the same way (often null). Speak both as **if invoiced**. Do not choose which job it is. On EV lamp 8, do not call the alternator slug.

---

## How to speak it

Garage path (default lamp 8, including EV 12V rectangle): a workshop can usually handle this. A scan / charging check is the next step; **the lamp does not name the part.** If a garage later invoices a 12V battery, quote the live headline or “we publish no figure.” Switching off heaters is **[Drive advice]**, not a close.

ICE Stop combo: repair may cost more than the car. Same if-invoiced speech. Get one bid as it sits and one written estimate. Recovery is part of the sell cost. Still do not say it is the battery, the alternator, or the belt.

**[Ask the garage]** is process, not a parts shortlist: charging voltage at idle and at raised revs (ICE), or 12V / DC-DC health (EV / hybrid), **before** any battery is sold.

Close-it-yourself: **no.** A reader does not close charging. Do not clear the lamp. Do not jump-start as a repair. MOT same-system notes (battery security, auxiliary drive belt) end: **this does not show the cause of today’s lamp.**

---

## Slugs

| Slug | On these paths | How to speak it |
|---|---|---|
| `car-battery-replacement-cost` | ICE 8, ICE 8 Stop combo, EV 8, named 12V job | **Only** “if the garage later invoices a 12V battery.” Quote the live headline, or “we publish no figure.” Never “it is the battery.” |
| `alternator-replacement-cost` | ICE 8 and ICE 8 Stop combo only | **Only** “if they invoice charging repair.” Often `gbp: null`. Never “it is the alternator.” Never on EV 8. |

Do **not** call with this lamp / path:

- `car-diagnostic-test-cost` as the **cause** of lamp 8 (not on this allowlist)
- `clutch-replacement-cost`, `cambelt-and-water-pump-cost`, `timing-chain-replacement-cost`, `wet-belt-replacement-cost` — not a charging-lamp cause
- `catalytic-converter-replacement-cost`, `dpf-cleaning-cost`, `head-gasket-repair-cost`, pads, wheel bearing
- An ICE alternator / belt job on **EV** lamp 8 or unmatched EV

A cost page is not the failed part.

---

## Pass versus fail

**Pass**

- Call `repair_cost` `car-battery-replacement-cost` on lamp 8 (ICE or EV 12V rectangle) **only** as “if the garage later invoices a 12V battery.”
- “A garage can usually handle this.” / ICE Stop combo: “Repair may cost more than the car.”
- “The lamp does not name the part.” Do not pick battery vs alternator.
- Quote this turn’s headline, including “we publish no figure.”
- “If the garage later invoices this job, published UK figures are …” — only after a live `repair_cost` result.
- EV 8: this slug only; no belt combo; no alternator page.
- Unmatched EV turtle / HV: **not** 8; do not call this slug.
- ICE + belt / heavy steering / rising temp: Stop first; same if-invoiced slugs; still not a diagnosis.
- `gbp: null` spoken as no published figure. Two written estimates. Do not invent.
- Named 12V job with no lamp: job range only; Modest sale-price band; no invented gain.
- Restate **[Drive advice]** and **[Outlook]** if they ask keep-driving or repair-vs-sell.
- “This skill does not diagnose” if they ask which part.

**Fail**

- “It’s the battery.” / “Fit a battery and the lamp will go out.” / “Lamp 8 means a flat battery.”
- “It’s the alternator / belt / DC-DC.” (picking a part, including from the symbol)
- “About £400–£800” (or any pounds) with no tool result, or a figure copied from this file.
- Freezing a battery price in this note as always-true.
- Calling this slug because an engine, DPF, ABS, or oil lamp is on, or because it is the only slug with a number.
- Treating the battery-cost page as today’s diagnosis.
- EV turtle / HV spoken as lamp 8, or an ICE belt / alternator story on an electric car.
- Close it yourself: jump leads, a reader, a code clear, or “buy a battery on the way.”
- Shop or parts links above Stop / recovery on the ICE belt combo.
- Invented trade-in pounds, or a sell push on ordinary garage lamp 8.
- Selling them a battery before charging-voltage / 12V health readings.
