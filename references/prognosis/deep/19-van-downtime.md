# 19 · Van downtime (same lamp buckets)

Not a second SKILL. If this note disagrees with `SKILL.md`, `references/prognosis.md`, `references/prognosis-cards.md`, or `references/boards.md`, those win. Do not diagnose. Do not invent pounds. Do not add a 14th lamp id. Do not add a fifth cluster.

A van does **not** change the outlook bucket. Follow the lamp card. Speech names **your Transit** (or the looked-up model). The picture is the **fuel** board. Optional `body=van` is speech only. Downtime is **“a day off the road”**, not a made-up day-rate.

## When

After Step 5, when the looked-up make+model is on the van list in `references/boards.md` — or when `show_dashboard` was called with `body=van`.

There is **no** body-type field on the vehicle record. Van is not a fuel. Van is not a board.

Scan **make+model** (lowercase, hyphens → spaces, **keep** spaces so `ranger` does not match Range Rover). Never scan for `van` or `nv`.

Treat as a van when the model matches (examples): Transit, Sprinter, Transporter, Crafter, Ducato, Boxer, Relay, Trafic, Master, Vivaro, Movano, Daily, Vito, Citan, Caddy, Expert, Dispatch, Combo Cargo, Doblo, Kangoo, NV200 / NV300 / NV400, Navara, Hilux, Proace, D-Max, TGE, Maxus, LDV, Amarok, Ranger.

Skip: `berlingo`, `partner`, bare `combo`, `custom`, `connect`, `hercules`. Dual-use: ask van or car; do not guess.

Do **not** treat as vans: Fiesta, Focus, Golf, Kuga, Tiguan, Polo, Civic, Corolla, Yaris, Leaf, Model 3.

If it is not a van, this file does not apply. Still never say “van board.”

## Picture and speech

| Do | Do not |
|---|---|
| Classify fuel → `petrol` / `diesel` / `hybrid` / `electric` / `unknown` | Invent a van PNG |
| `show_dashboard` with **required** `board=` (fuel). Then `open_resource` the `file://` preview | Empty `board`. A fifth cluster. “Van board.” |
| Optional `body=van` — **speech only**. Same PNG as the fuel picture | Treat `body=van` as a different set of lamps or numbers |
| Say **your Transit** (or “your Sprinter”, from lookup) | “the van cluster”, “commercial board”, listing lamp names |
| Keep global numbers. 9 is always DPF even if empty on petrol | Renumber for vans. Shrink toward electric on owner talk |

Example G: TRANSIT, `fuel_type` diesel → `board=diesel`, same diesel picture, **your Transit**, they pick 9. Not a van board.

## Same buckets

Internal labels stay `owner` · `device` · `garage` · `poor`. Speech stays Close it yourself / A garage can usually handle this / Repair may cost more than the car.

The van does **not** upgrade `garage` to `poor` because it is a work vehicle. It does **not** skip Stop because they still have drops. It does **not** skip a driveway close because “they need the van.” Follow `references/prognosis.md` and the lamp card.

| Lamp / path | Bucket on a van | Same as a car |
|---|---|---|
| `oil-pressure` | `poor` | Yes. Stop. Not a close. |
| `coolant-temp` (red) | `poor` | Yes. |
| `brake-system` hydraulic / pedal / leak | `poor` | Yes. Parking brake still on → skip. |
| `airbag-srs` | `garage` | Yes. Red but Limited, not Stop. |
| `power-steering` | `garage` (`poor` if already heavy) | Yes. |
| `engine-steady` | `device` then `garage` | Yes. |
| `engine-flashing` | `poor` | Yes. |
| `battery-charging` | `garage` (ICE belt combo → `poor`) | Yes. |
| `dpf` steady, driving normally | `owner` then `garage` | Yes. One handbook regen. |
| `dpf` flash / limp / oil over max | `poor` | Yes. |
| `tyre-pressure` simply on | `owner` | Yes. |
| `tyre-pressure` flash-then-steady | `garage` | Yes. |
| `abs` | `garage` | Yes. |
| `esc-traction` steady, not off | `garage` | Flashing while driving → skip. |
| `glow-plug` went out | skip | Not a fault. |
| `glow-plug` stays on / flashes | `garage` | Yes. |
| GPF / AdBlue / EV unmatched | Same unmatched cards | Not a 14th lamp. Not DPF copy on petrol. |

Repair slugs stay on **that lamp’s** allowlist. Do not invent a “van diagnostic” or “commercial downtime” slug. Empty allowlist → we publish no figure.

## Downtime speech

Downtime is **outlook colour**, not money.

Say it when a garage visit or a Stop lamp means the van will not work tomorrow: **a day off the road**. On Close it yourself (inflate, AdBlue top-up, one handbook regen, a driveway scan), do not invent a lost day.

Never turn that sentence into pounds:

- No day-rate, lost earnings, “£150 a day”, courier / tradesman charge-out
- No invented van-hire, recovery, or collection fee (recovery is still **part of sell cost** when **[Drive advice]** is Stop — still no number)
- No Parkers / trade-in / “typical Transit values”
- `gbp: null` remains the answer when the tool has no figure

Do not invent a van MOT regime, operator-licence, or tachograph line. MOT talk stays the lamp card: first-use + fuel, DVSA manual link, never “Expect a fail.” History lines still end: **this does not show the cause of today’s lamp.**

## Owner copy

Spoken **[Outlook]** after the statement (~40–60 words). Name the model, not the plate. No day-rate. No extra bucket.

**Garage path** (same lamp as a car, e.g. steady engine after a read, ABS, glow that stays on):

A garage can usually handle this. Plan a day off the road. We publish a figure only when `repair_cost` returns one for a slug on this lamp’s allowlist — otherwise no figure, two written estimates. The lamp does not name the part.

**Close-it-yourself** (TPMS simply on, AdBlue low, handbook DPF regen, device scan):

Close it yourself. That is not a day off the road unless the lamp stays and a workshop is next. Inflate / correct fluid / one handbook regen / stored code and freeze frame as the card says. Do not clear the lamp.

**Weak outlook** (oil, red coolant, hydraulic brakes, flashing engine, DPF limp / oil over max):

Repair may cost more than the van. We publish no used-car price. Get one bid as it sits and one written estimate. If **[Drive advice]** is Stop, do not drive it in — recovery is part of the sell cost. A day off the road is already true; do not add a made-up day-rate.

## Red lines

1. Same buckets as the lamp card. No van-only `poor`. No van-only skip of Stop or of a legal close.
2. Say **your Transit**. Never **van board**. `body=van` does not change the PNG.
3. Downtime = “a day off the road.” No invented day-rate, hire, or lost-earnings pounds.
4. No diagnosis. No extra lamp ids. No SAE J2012 wording.
5. No real registration. Worked plate in prose is only `AB12CDE`, then **your Transit**.
6. Safety before commerce. No scanner or shop link above Stop / recovery.
7. Never advise clearing the lamp. Never forced DPF regen. Never filter delete as a cheap van fix.
8. Do not scan the string `van` or `nv` to classify the vehicle.

## Pass versus fail

- Pass: `board=diesel` for a diesel Transit; **your Transit**; they pick 9; DPF card buckets.
- Fail: “van board”; a fifth PNG; empty `show_dashboard` args.
- Pass: optional `body=van` is speech only. Same fuel picture.
- Fail: treating `body=van` as different lamps, or scanning the word `van` in the record.
- Pass: oil-can on a Transit → `poor`, Stop, no close, no engine-rebuild figure.
- Fail: “keep the drops going, it’s only a van sensor” / “top it up, you can’t lose a day’s work.”
- Pass: TPMS simply on → Close it yourself. Not a day off the road.
- Fail: upgrading TPMS to `poor` because it is a work van.
- Pass: “Plan a day off the road.” No pounds attached.
- Fail: “That’s £200 a day lost” / “hire is about £80” / any made-up day-rate.
- Pass: `repair_cost` only with this lamp’s allowlist slug; `gbp: null` → we publish no figure.
- Fail: a “van downtime” slug, or filling a gap with a guessed commercial rate.
- Pass: dual-use model → ask van or car.
- Fail: calling a Fiesta a van, or a Range Rover a Ranger.
- Pass: if they ask what is wrong — no diagnosis; restate **[Drive advice]** and **[Outlook]**.
- Fail: naming a part so they can “get back on the road today.”
