# Vehicle boards

After a successful plate lookup, pick **one** still PNG. Numbers are **global**: 9 is DPF only on diesel. Never renumber. **7 is not drawn** — one engine cell is 6; flashing is spoken as 7.

Do not ask if they are driving.

## Classify fuel → board

Use `vehicle.fuel_type` **and** `fuel_raw`. Apply **top row first**:

| fuel_type / raw | extra | board |
|---|---|---|
| diesel | including 48V / mHEV still labelled diesel | diesel |
| hybrid | `fuel_raw` contains diesel, electric diesel, or heavy oil (case insensitive) | diesel |
| `Gas Diesel` in `fuel_raw` | | diesel |
| hybrid | `fuel_raw` missing | **unknown** (or ask petrol vs diesel hybrid) |
| hybrid | otherwise (Hybrid Electric, no diesel cue) | hybrid |
| electric | | electric |
| petrol | | petrol |
| LPG / Gas / CNG / LNG / `Gas Bi-Fuel` in `fuel_raw` | not `Gas Diesel` | petrol |
| unknown or missing | | unknown |

Never upgrade `fuel_type=diesel` to hybrid from a marketing name.

MCP: `show_dashboard` with **required** `board`. Empty args is a fail. The tool returns the PNG. Do not invent a board if the tool errors.

PNG files:

- `unknown` → `assets/cluster.png`
- `petrol` → `assets/cluster-petrol.png` (empty slots 9 and 13, **no circled numbers** on empties)
- `diesel` → `assets/cluster-diesel.png`
- `hybrid` → `assets/cluster-hybrid.png` (empty slots 9 and 13)
- `electric` → `assets/cluster-electric.png` (empty slots 1, 6, 9, 13)

## Lamps on each board

| board | live circled numbers | empty slots (not pickable) |
|---|---|---|
| unknown / diesel | 1–6, 8–13 (7 is spoken flashing on the engine cell) | — |
| petrol / hybrid | 1–6, 8, 10–12 | 9, 13 |
| electric | 2–5, 8, 10–12 | 1, 6, 9, 13 |

## Petrol / hybrid 9 = `unmatched-gpf`

If they pick 9 or say exhaust-dots / petrol particulate filter: path `unmatched-gpf`. Keep this board. Not DPF. Do not say “9 is not printed, pick again.”

Electric 9 (empty): not DPF, not GPF. Ask which **live** circled shape is lit, or none.

Other empty live-number mistakes (electric 1 or 6): keep this board. That number is not on this car. Ask the circle on the matching **live** shape. Widen to `unknown` only if they say **none of these shapes**.

Never switch to a **smaller** board on owner talk (especially not electric). Never default electric.

## Other unmatched paths

**AdBlue (diesel):** they say AdBlue / urea / DEF. Not 9, not 6. Path `unmatched-adblue`.

**EV:** turtle / limited power; car-with-! and no skid lines; charge plug; HV on-screen text. Not 12, not 8. Path `unmatched-ev`. Do not open the ICE unknown board.

**Blue / green:** main beam, indicators, cruise, fog. Name the status function. Ask if any circled lamp is also on. Engine-cold blue thermometer: not id 2.

**Glow 13 went out after start:** not a fault.

## Van vs car

No body-type field. Van does **not** change lamps and is **not** a fifth cluster. Say "your Transit" on the **fuel** picture. Do not say "van board."

Optional `body=van` is speech only. Scan make+model (lowercase, hyphens → spaces, **keep** spaces so `ranger` does not match Range Rover). Never scan for `van` or `nv`.

```
transit
sprinter
transporter
crafter
ducato
boxer
relay
trafic
master
vivaro
movano
daily
vito
citan
caddy
expert
dispatch
combo cargo
doblo
kangoo
nv200
nv300
nv400
navara
hilux
proace
d-max
tge
maxus
ldv
amarok
ranger
```

Skip `berlingo`, `partner`, bare `combo`, `custom`, `connect`, `hercules`. Dual-use models: ask van or car rather than guessing.

Do **not** treat as vans: fiesta, focus, golf, kuga, tiguan, polo, civic, corolla, yaris, leaf, model 3.

## Fallback

Lookup 404 → ask fuel, then matching board. Any transport miss (timeout, 502/504, DNS, empty body, MCP 403) → treat as 503. Ask fuel **only if the lamp is still unknown**. Named Stop lamp: write Stop this turn; do not wait for a board. Never default electric.

Do not diagnose. Do not add new lamp ids.
