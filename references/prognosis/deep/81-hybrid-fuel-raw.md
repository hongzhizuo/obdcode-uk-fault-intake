# 81 · Hybrid + missing `fuel_raw` → unknown board

Not a second SKILL. If this note disagrees with `SKILL.md`, `references/boards.md`, `references/prognosis.md`, or `references/prognosis-cards.md`, those four win. Do not diagnose. Do not invent pounds. Do not add a 14th lamp id.

Classify the **picture** from `vehicle.fuel_type` **and** `fuel_raw`. Then the **outlook card follows that board**. GPF copy is for petrol / hybrid boards. DPF and glow copy is for the diesel board (and only then).

## When

After a successful plate lookup, before `show_dashboard`. Apply `references/boards.md` **top row first**. This file only fills the hybrid / diesel-cue / marketing-name cases.

MCP: `show_dashboard` with **required** `board`. Empty args is a fail. Then `open_resource` the `file://` preview in the **same turn**.

They are on a computer or phone. Do not ask if they are driving.

## Classify

| Record | Board | Live aftertreatment |
|---|---|---|
| `fuel_type=hybrid` and `fuel_raw` **missing** (null, empty, or whitespace) | **unknown** — or ask petrol vs diesel hybrid **before** the PNG | 9 and 13 are printed. Do **not** pick a GPF or DPF card until they answer |
| `fuel_type=hybrid` and `fuel_raw` contains `diesel`, `electric diesel`, or `heavy oil` (case insensitive) | **diesel** | DPF (9) and glow (13) are live |
| `Gas Diesel` in `fuel_raw` | **diesel** | Same. Not the LPG / petrol path |
| `fuel_type=hybrid` and `fuel_raw` is Hybrid Electric / petrol hybrid / no diesel cue | **hybrid** | Ghost 9 and 13. Exhaust-dots or pick of 9 → unmatched **GPF** |
| `fuel_type=diesel` — including 48V / mHEV / “hybrid” in the **model or marketing name** | **diesel** | Stay diesel. DPF and glow stay live |

`fuel_type` alone is not enough. Hybrid + Electric Diesel is the diesel picture. Hybrid + missing raw is not the hybrid picture.

Prefer the ask when raw is missing, then show the matching PNG. If you already opened **unknown**, **keep that board**. Do not shrink to hybrid on owner talk.

## Never upgrade diesel to hybrid

`fuel_type=diesel` stays **diesel**. A badge or brochure word does not change the board.

Do not move these to `board=hybrid` (and do not ghost 9 or 13):

- 48V, mHEV, mild hybrid, EcoBlue Hybrid, e-TDI, EQ Boost
- “hybrid” in the make / model string while `fuel_type` is still diesel
- Any other marketing name on a record that is labelled diesel

That is the opposite of the diesel-hybrid row above. Hybrid + diesel **raw** → diesel board (keep DPF / glow). Diesel **type** + hybrid **name** → still diesel board. Never the hybrid PNG.

## Outlook follows the board

Do not mix the cards. The aftertreatment path is the board you showed, not the word “hybrid” in the record.

### Diesel board (hybrid + diesel raw, or `fuel_type=diesel`)

Lamp 9 is **DPF**. Use the DPF card in `prognosis-cards.md`.

- Steady, driving normally: `owner` then `garage`. One handbook regen. Call `dpf-cleaning-cost` (often `gbp: null` — still say no figure).
- Flash / limp / oil over maximum: `poor`. No more motorway loops. No scan-tool forced regen. No “just cut it out.”
- Glow 13 on with ignition then out: **not a fault**. No outlook.
- Glow 13 stays on or flashes: `garage`. `car-diagnostic-test-cost`. No glow-plug DIY.
- AdBlue / urea / DEF: unmatched. Not 9, not 6.

Never run GPF copy on this board. Never say 9 is an empty slot.

### Hybrid board (Hybrid Electric / no diesel cue)

Ghost 9 and 13. Keep this board if they type 9.

- Exhaust-dots, “particulate filter”, or pick of 9: unmatched **GPF**. Not DPF. Drive with care. `device` then `garage`. `car-diagnostic-test-cost` only. Scan + freeze frame, do not clear. **No** diesel regen copy.
- 13 is not printed. Not a glow fault. Ask the circle on the matching shape. Widen to unknown only if they say **none of these shapes**.

Never call `dpf-cleaning-cost` on this board. Never a handbook regen loop.

### Unknown board (hybrid + missing raw)

Same printed set as diesel: 1–6, 8–13. That is why the hybrid PNG is wrong here — it would hide DPF and glow on a car that might be a diesel hybrid.

- Other lamps (oil, brakes, engine, TPMS, and the rest): their usual cards. Hybrid in the record does not change those buckets.
- Lamp 9, lamp 13, exhaust-dots, or glow: **ask petrol vs diesel hybrid** before the outlook. Then apply the matching card above.
- Until they answer: thinner statement only. Do not give a handbook regen. Do not give GPF-only “scan, not DPF” as if the fuel were settled.
- If they then say petrol hybrid: GPF card. **Keep** the unknown PNG (do not shrink).
- If they then say diesel hybrid: DPF / glow cards. The unknown PNG already shows 9 and 13.

Caption the record as fact. Do not ask them to audit petrol vs diesel except this missing-raw fork.

## Owner copy (routing only)

Do not invent a second spoken card. After the fault statement, speak the outlook from the **board’s** card.

- Diesel board + 9: DPF outlook (handbook regen or weak limp branch).
- Hybrid board + exhaust-dots / 9: GPF outlook (scan; no regen).
- Unknown + 9 or 13, fuel still unsettled: ask petrol vs diesel hybrid, then the matching outlook.

A scan is the next step on GPF and on a steady engine lamp; the lamp does not name the part. A cost page is not a diagnosis. `gbp: null` is the answer.

Vans: same fuel picture. Say **your Transit**. Not a van board.

## Red lines

1. Hybrid + missing raw → `unknown` (or ask first). Not `hybrid`. Not `diesel` by guess. Never default electric.
2. Hybrid + diesel / Electric Diesel / heavy oil → `diesel`. DPF and glow stay live.
3. Never upgrade `fuel_type=diesel` to hybrid from a marketing name. 48V / mHEV still labelled diesel stay diesel.
4. Outlook cards follow the board. GPF is not DPF. DPF is not GPF.
5. Empty `show_dashboard` args is a fail. `board` is required. Open the preview in the same turn.
6. Do not shrink the board on owner talk. Do not switch to electric because they said “hybrid.”
7. Do not diagnose. Do not name the failed part. Do not invent pounds.
8. No scan-tool forced DPF regen. No filter delete as a cheap fix. No SAE J2012 wording.
9. No real registration in this file or in speech.

## Pass versus fail

- Pass: `fuel_type=hybrid`, `fuel_raw` missing → `board=unknown`, or ask petrol vs diesel hybrid, then the matching PNG.
- Fail: hybrid + missing raw → `board=hybrid` (ghosts 9 and 13 on a car that may be diesel).
- Pass: hybrid + `Electric Diesel` / `diesel` / `heavy oil` → `board=diesel`; 9 and 13 live; DPF / glow cards.
- Fail: that record → hybrid PNG, then GPF copy or “9 is empty.”
- Pass: `fuel_type=diesel` plus 48V / mHEV / EcoBlue Hybrid in the name → still `board=diesel`; DPF card for 9.
- Fail: “it’s a mild hybrid, so use the hybrid picture” / GPF / ghost 9.
- Pass: hybrid board + exhaust-dots or pick of 9 → unmatched GPF; scan; `car-diagnostic-test-cost`; no regen.
- Fail: hybrid board + regen loop, `dpf-cleaning-cost`, or “it’s the DPF.”
- Pass: diesel board + 9 → DPF card; handbook regen only if steady and driving normally; `dpf-cleaning-cost` even when `gbp: null`.
- Fail: diesel board + “GPF, just scan, not a filter.”
- Pass: unknown board + 9, they have not said petrol vs diesel → ask; no GPF-or-DPF outlook yet.
- Fail: unknown + 9 → diesel regen, or GPF-only copy, as if fuel were known.
- Pass: they later say petrol hybrid after unknown was shown → GPF outlook; **keep** unknown PNG.
- Fail: shrink to `board=hybrid` because they said petrol hybrid.
- Pass: `show_dashboard` with `board=unknown|diesel|hybrid|…` then `open_resource` the preview.
- Fail: empty `show_dashboard` args, or a name list instead of the picture.
- Pass: “a scan is the next step; the lamp does not name the part.”
- Fail: “it’s the clutch / cat / DPF / GPF soot.” Any guessed GBP.
