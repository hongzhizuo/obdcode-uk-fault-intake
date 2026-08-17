# 100 · Merge note

These files are **notes**. They are not a second SKILL and they do not change live behaviour.

If a deep file disagrees with any of these four, **those four win**:

- `SKILL.md`
- `references/prognosis.md`
- `references/prognosis-cards.md`
- `references/value-gain.md`

Read the matching live file first. Use a deep note only to expand one topic. Do not stitch these notes into a parallel rulebook.

## Hard rules (same as the four)

**No 14th lamp.** The menu is a fixed set of 13 ids. Circled numbers stay global: 9 is always DPF even when a petrol board leaves that slot empty; 7 is spoken flashing on the engine cell, not a second drawing. GPF, AdBlue / urea / DEF, and EV turtle / HV / charge-plug text are **unmatched paths**, not ids 14+. Files `14`–`16` and `72` / `84` record that. Do not invent a new lamp id to make the folder look tidy.

**No invented GBP.** There is no sell-price tool and no modification-gain API. `gbp: null` / `no_verified_price` / `no_published_job` is the answer. Repeat an owner’s invoice only as what they paid, never as uplift. Do not freeze a planning headline in a note as always-true. Live chats call `repair_cost` with an allowlisted slug; empty allowlist means no hunt for a nearby slug.

Also: do not diagnose. A cost slug is not the failed part. Do not teach wrap / remap / filter delete / lift. Close-it-yourself never covers Red-class work.

## How to resolve a clash

1. `SKILL.md` for path, steps, red lines, and what the owner hears.
2. `prognosis.md` for buckets, money, device, and default-by-lamp.
3. `prognosis-cards.md` for the card of **this** lamp or unmatched path.
4. `value-gain.md` for Path B / **[Value]** bands only.

Then, if needed, the numbered note for extra examples. If two deep files disagree with each other, still prefer the four. Age, high MOT mileage, or a missing pound does not rewrite a card.

## Intended numbering 01–100 (high level)

One topic per file. `README.md` in this folder is the index, not a numbered note.

### 01–13 — the thirteen lamp cards

Same ids as the cluster. Defaults follow `prognosis-cards.md`.

| File | Id | Default (short) |
|---|---|---|
| `01-oil-pressure.md` | `oil-pressure` | `poor` — no rebuild slug |
| `02-coolant-temp.md` | `coolant-temp` (red) | `poor` — gasket slug often null; blue is skip |
| `03-brake-system.md` | `brake-system` | parking brake on = skip; hydraulic = `poor` |
| `04-airbag-srs.md` | `airbag-srs` | `garage` — no SRS slug |
| `05-power-steering.md` | `power-steering` | `garage`; heavy steering = Stop / `poor` |
| `06-engine-steady.md` | `engine-steady` | `device` then `garage` — diagnostic test only |
| `07-engine-flashing.md` | `engine-flashing` | `poor` — cat slug only if later invoiced |
| `08-battery-charging.md` | `battery-charging` | `garage`; ICE belt combo = `poor` |
| `09-dpf.md` | `dpf` | diesel only — handbook regen or `poor` |
| `10-tyre-pressure.md` | `tyre-pressure` | simply on = `owner`; flash-then-steady = `garage` |
| `11-abs.md` | `abs` | `garage` — no hydraulics DIY |
| `12-esc-traction.md` | `esc-traction` | flashing = skip; steady not off = `garage` |
| `13-glow-plug.md` | `glow-plug` | went out = skip; stays / flashes = `garage` |

### 14–16 — unmatched paths (not extra lamp ids)

| File | Path |
|---|---|
| `14-gpf-unmatched.md` | Petrol / hybrid GPF — not DPF, not id 9 |
| `15-adblue-unmatched.md` | AdBlue / urea / DEF — not 9, not 6 |
| `16-ev-unmatched.md` | Turtle / HV / charge-plug — not 12, not 8 |

### 17–21 — close-it-yourself and vans

`17` fuel cap (extra check, not a diagnosis). `18` one handbook DPF regen. `19` vans: same buckets, “your Transit,” no made-up day-rate. `20` the short owner-close list. `21` allowed scan steps (codes **and** freeze frame; do not clear).

### 22–35 — published slugs and when not to call them

If-invoiced or already-named only: `22` 12V battery, `23` pads and discs, `24` head gasket (often null), `25` alternator (often null), `30` wheel bearing, `34` converter on the flashing / weak path.

Always-or-never: `26` never clear / never forced regen. `27` no Red-class DIY. `28` scanner category may be off the shelf — no fake SKU. `29` `mot-cost` is booking, not a lamp repair. `31` when to call `car-diagnostic-test-cost`. `32` timing-chain slug is value-gain, not an engine-lamp cause. `33` stereo is Little. `35` clutch slug is never because an engine lamp is on.

### 36–40 — privacy, board, and value extras

`36` plate privacy. `37` petrol pick of 9 keeps the petrol picture (GPF path). `38` legal exhaust Little; illegal noise Negative. `39` interior refresh Little / mixed. `40` documented cambelt / service usually beats a wrap — still no invented pounds.

### 41–49 — money speech and sell

`41` how to say `gbp: null`. `42` airbag lamp-on sale hit, still no invented bid. `43` device then garage. `44` Stop lamps: bid as it sits, collection, no invented recovery fee. `45` bands are not a valuation. `46` Path B: no dashboard picker. `47` one bid vs one estimate. `48` scrap last, no invented scrap pounds. `49` do not auto-upgrade DPF / engine to `poor` from high mileage.

### 50–64 — sale-price bands (Path B)

`50` respray / PPF / presentation. `51` towbar Modest on the right car. `52`–`53` / `55`–`56` / `60` skip-not-a-fault (blue coolant, parking brake, glow out, ESC flashing). `54` Strong maintenance. `57` over-mod Negative. `58` Modest tyres / MOT / pads / 12V. `59` invoice is spend, not uplift. `61` MOT fusion is not today’s cause. `62` van racking Modest on a working van. `63` remap Negative, no how-to. `64` wrap / wheels Little / mixed.

### 65–78 — cross-cutting outlook rules

`65` missing pounds is not a missing outlook. `66` do not say write-off. `67` commercial links below Stop. `68` DPF delete is not a cheap fix. `69` ask the garage for process, not a parts list. `70` plate-only still needs a lamp before outlook. `71` illegal mods Negative. `72` unmatched paths still get Step 6 (unless skip). `73` allowlist only for `repair_cost`. `74` spoken length and UK tone. `75` / `76` pass vs fail for Steps 6 and 7. `77` lamp plus mod: outlook first, then **[Value]**. `78` red lines 7–10 restated.

### 79–86 — sketches and traps

`79` oil-lamp outlook sketch. `80` wrap value sketch. `81` hybrid `fuel_raw` → board. `82` electric lamp 8 is 12V. `83` restate **[Drive advice]** and **[Outlook]**. `84` no 14th lamp (same rule as this file). `85` safety class is not the outlook bucket. `86` Green TPMS owner-close vs malfunction.

### 87–99 — lamp traps, card vs skill, language

`87` oil-can is not “add a litre.” `88` lamp 8 is charging, not “fit a battery.” `89` DPF oil over max: `poor`, no more regen loops. `90` inflate to the placard. `91` airbag is Red and Limited, not Stop. `92` vehicle card is site work; skill states the band only. `93` PAS heavy = Stop / `poor`. `94` ABS: normal brakes still work. `95` AdBlue remaining-starts = `poor`. `96` EV pack: compare **their** quote with a bid; do not invent pack pounds. `97` clutch invoice on high miles is Strong, never for an engine lamp. `98` wet belt / cambelt due: Strong with invoice; job slug ≠ gain. `99` owner-facing copy is UK English; 愈后 stays the product idea, not garage-card speech.

### 100 — this file

`100-merge-note.md` — notes only; the four live files win; no 14th lamp; no invented GBP.

## Pass / fail

- Pass: treat a clash by opening `SKILL.md` / `prognosis.md` / `prognosis-cards.md` / `value-gain.md` and following those.
- Pass: GPF / AdBlue / EV stay unmatched; circled numbers stay 1–13.
- Pass: “we publish no figure” / `gbp: null` / one bid as it sits — no filled-in pounds.
- Fail: “the deep notes say X, so ignore the card.”
- Fail: adding lamp 14 (or remapping 9 on petrol to DPF) because file `14` exists.
- Fail: copying a pound figure out of a note instead of calling `repair_cost`, or inventing Parkers / wrap-uplift / scrap / recovery fees.
