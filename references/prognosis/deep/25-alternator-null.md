# 25 · `alternator-replacement-cost` if invoiced (often null)

Not a second SKILL. If this note disagrees with `SKILL.md`, `references/prognosis.md`, or `references/prognosis-cards.md`, those three win. Do not diagnose. Do not invent pounds. Do not add a 14th lamp id.

This slug is a **later invoice class**: charging repair, **if** the garage bills that job on the **charging path**. It is **not** today’s failed part. **Never “it is the alternator.”**

It is **often** `gbp: null`. Still call it. Still say we publish no figure. Live chats **must** call `repair_cost` and speak that turn’s result. **This file must not freeze a pound figure as always-true.** Do not copy a remembered £ amount into speech or into this note.

**Do not pick alternator versus battery.** On ICE lamp 8, this slug and `car-battery-replacement-cost` are both invoice classes. Do not skip this call because it is often empty. Do not treat the battery page as the diagnosis because that page has a number.

Live lamp card: `references/prognosis/deep/08-battery-charging.md`. Battery slug: `references/prognosis/deep/22-battery-cost-if-invoiced.md`. Null speech: `references/prognosis/deep/41-null-gbp-speech.md`.

---

## When

Call `repair_cost` with `job` = `alternator-replacement-cost` only when **this lamp’s allowlist says so**, and only as **“if they later invoice charging repair.”**

| Path | Bucket | Why this slug |
|---|---|---|
| **`battery-charging` (8)** ICE / hybrid, rectangle on while running, no Stop combo | `garage` | Allowed **if invoiced**. Also call `car-battery-replacement-cost` as “if they invoice a 12V battery.” **Do not pick** which. The lamp does not name the part. |
| **`battery-charging` (8)** ICE + belt noise / heavy steering / rising temperature | `poor` | Same two slugs, still **if invoiced**, still **not** a diagnosis. Stop / recovery already sits in **[Drive advice]**. Skip this belt combo on an electric car. |
| **Named charging / alternator job** (Path B, or after the outlook) | job range only | They already named that invoice. Call this slug for the **job’s** published range (often null). Still not “the lamp was the alternator.” Still no invented **gain**. |

**Often null is not a skip.** An often-null slug can still return a headline today; a published slug can still return null. Read the live result. Skipping the tool, or swapping to the battery slug because that page has a number, is a fail.

Skip the call (and skip Step 6) when lamp 8 was only a **key-on bulb check** that then went out — not a fault.

---

## When not

**Never on the electric board.** EV lamp 8 allowlist is `car-battery-replacement-cost` as “if invoiced” only. No alternator / belt story. Unmatched EV (turtle / car-with-! and no skids / HV or charge-plug text) is **not** 8 and **not** this slug.

Do **not** call this slug on:

- EV board lamp 8, or unmatched EV
- `oil-pressure`, red `coolant-temp`, hydraulic `brake-system`, `airbag-srs`, `power-steering`
- `engine-steady` / unmatched GPF / `engine-flashing` / `glow-plug`
- Diesel `dpf`, `tyre-pressure`, `abs`, `esc-traction`, AdBlue
- Any lamp because you want a charging number, or because this is the slug you remember

Never hunt it when the allowlist is empty. A cost page is not the failed part.

---

## How to call (live)

Prefer the tool. Same turn as **[Outlook]** / **[Repair]**, after **[Drive advice]**. Never above a Stop line.

```
POST https://obdcode.co.uk/mcp
{"jsonrpc":"2.0","id":1,"method":"tools/call",
 "params":{"name":"repair_cost","arguments":{"job":"alternator-replacement-cost"}}}
```

Plain HTTP if you do not speak MCP: the same job name is the slug on `https://obdcode.co.uk/guides/alternator-replacement-cost/`. Prefer the tool.

On ICE lamp 8, also call `car-battery-replacement-cost` in the same turn as the other invoice class. Speak **both** as if invoiced. Do not choose which job they will get. Do not drop this call when you expect `gbp: null`.

Speak the **live** result only, and only as invoice class:

- `status: ok` and a headline → “If they later invoice charging repair, published UK figures are …” then that headline. Planning range, not a quote for this car, **not** “it is the alternator.”
- `gbp: null` / `no_verified_price` / `no_published_job` → **that is the answer.** We publish no figure. Ask two local garages for a written estimate. Do not fill the gap with a remembered alternator price.

Do not cache yesterday’s pounds in this file or in the next chat.

---

## How to speak it

Garage path (default ICE lamp 8, no combo): a workshop can usually handle this. Charging voltage at idle and at raised revs is the next process step; **the lamp does not name the part.** If they later invoice charging repair, quote the live headline or — as is often the case — “we publish no figure.” If they later invoice a 12V battery, quote that job the same way. Do not pick which. Switching off heaters is **[Drive advice]**, not a close.

ICE Stop combo: repair may cost more than the car. Same if-invoiced speech for both slugs. Get one bid as it sits and one written estimate. Recovery is part of the sell cost. Still do not say it is the alternator, the battery, or the belt.

**[Ask the garage]** is process, not a parts shortlist: charging voltage at idle and at raised revs (ICE), **before** any battery or charging unit is sold.

Close-it-yourself: **no.** A reader does not close charging. Do not clear the lamp. Do not change a battery or an alternator on the drive.

---

## Owner copy

≤120 words. Spoken **[Repair]** on the ICE charging path. No ids, no fusion slugs, no URLs, no plates, no pounds unless this turn’s tool returned a verified headline.

A garage can usually handle this unless the charging lamp sits with heavy steering, a rising temperature, or a belt noise — then do not drive it in. The rectangle does not name the part. We do not choose battery versus charging repair. If they later invoice charging repair, we may quote that job page; it is often unpublished — then we publish no figure and you get two written estimates. If they later invoice a 12V battery, that page is a planning range for that invoice, not a diagnosis. Switching off extras is so you can get there, not a fix.

(108 words. Insert a live charging-repair headline only inside the “if later invoices” sentence. If the tool returned no figure, say we publish no figure.)

---

## Slugs on the charging card

| Slug | On these paths | How to speak it |
|---|---|---|
| `alternator-replacement-cost` | ICE 8 and ICE 8 Stop combo only | **Only** “if they invoice charging repair.” **Often `gbp: null`.** Never “it is the alternator.” Never on EV 8. |
| `car-battery-replacement-cost` | ICE 8, ICE 8 Stop combo, EV 8, named 12V job | **Only** “if they invoice a 12V battery.” Never “it is the battery.” |

Call **both** on ICE. Do not pick. Do not call only the slug that returned a number.

Do **not** call with this lamp / path:

- `car-diagnostic-test-cost` as the cause of lamp 8
- clutch, cat, DPF, head-gasket, pads, cambelt, chain, wet-belt, MOT, wheel bearing
- this slug on **EV** lamp 8 or unmatched EV

A cost page is not the failed part.

---

## Red lines

1. Never “it’s the alternator.” Never “usually the alternator.” Never pick battery vs alternator vs belt vs wiring — even as a shortlist.
2. Never skip this call on ICE lamp 8 because it is often null, or call only the battery slug because that page has a number.
3. Never call this slug on an electric car.
4. Never treat the charging-repair cost page as today’s diagnosis.
5. No invented GBP. No figure frozen in this note. `gbp: null` is the answer when the tool says so.
6. No DIY alternator, belt, or battery work. Switching off extras is not a close.
7. ICE Stop combo: do not tell them to drive it in. EV: do not apply that belt combo and do not use this slug.
8. Safety before commercial: Stop / recovery above any cost line.
9. Never print a real registration. Illustrative plate elsewhere is `AB12CDE` only; then “your 2016 Fiesta” / “your Transit.”
10. If they ask what is wrong: this skill does not diagnose. Restate **[Drive advice]** and **[Outlook]** for recovery / keep-driving / repair-vs-sell.

---

## Pass versus fail

**Pass**

- ICE lamp 8: call `alternator-replacement-cost` **and** `car-battery-replacement-cost` as **if later invoiced**. Do not pick which.
- “If they later invoice charging repair, published UK figures are …” — or, often, “we publish no figure — two written estimates.”
- Still call when you expect `gbp: null`. Null / `no_verified_price` / `no_published_job` is the answer, not a gap.
- “The lamp does not name the part.” This skill does not diagnose.
- Default ICE, no combo: “A garage can usually handle this.”
- ICE + belt / heavy steering / rising temp: Stop first; same two if-invoiced slugs; still not a diagnosis.
- EV 8: **do not** call this slug. Battery invoice class only. No belt story.
- Quote this turn’s live result only. Do not freeze pounds in this file.
- Restate **[Drive advice]** and **[Outlook]** if they ask keep-driving or repair-vs-sell.

**Fail**

- “It’s the alternator.” / “Usually the alternator.” / “Fit an alternator and the lamp will go out.”
- “It’s the battery.” / picking battery vs alternator vs belt.
- Skipping this slug because it is often null, then quoting only the battery page as the diagnosis.
- Calling only the slug that has a number.
- “About £250–£600 for an alternator” (or any pounds) with no tool result, or a figure copied from this file.
- Filling `gbp: null` with a remembered charging-repair price.
- Calling this slug on EV lamp 8, unmatched EV, oil, engine, DPF, or any empty allowlist.
- Treating the alternator-cost page as today’s failed part.
- Close it yourself: belt change, battery swap, jump leads, a reader, a code clear.
- Shop or parts links above Stop / recovery on the ICE belt combo.
- “Drive it slowly to the garage” on the ICE Stop combo.
