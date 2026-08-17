# Vehicle boards

After a successful plate lookup, pick **ONE** still PNG. Numbers are **GLOBAL**: 9 is always DPF even when that slot is empty. Never renumber. **7 is not drawn** — one engine cell is 6; flashing is spoken as 7.

They are on a computer or phone. Do not ask if they are driving.

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

MCP: `show_dashboard` with **required** `board`. Empty args is a fail. Then `open_resource` the `file://` preview in the same turn.

PNG files:

- `unknown` → `assets/cluster.png`
- `petrol` → `assets/cluster-petrol.png` (ghost 9 and 13)
- `diesel` → `assets/cluster-diesel.png`
- `hybrid` → `assets/cluster-hybrid.png` (ghost 9 and 13)
- `electric` → `assets/cluster-electric.png` (ghost 1, 6, 9, 13)

## Lamps on each board

| board | circled numbers that are live | empty ghost slots |
|---|---|---|
| unknown / diesel | 1–6, 8–13 (7 is spoken flashing on the engine cell) | — |
| petrol / hybrid | 1–6, 8, 10–12 | 9, 13 |
| electric | 2–5, 8, 10–12 | 1, 6, 9, 13 |

## Off-board number

Keep **this** board. Say that circled number is not printed. Ask them to read the circle on the matching shape. Widen to `unknown` only if they say **none of these shapes**.

Never switch to a **smaller** board on owner talk (especially not electric). Caption from the record as fact. Do not ask them to audit petrol vs diesel.

## Unmatched paths (still write a thinner statement)

**GPF (petrol / hybrid):** exhaust-dots, or they pick 9. Not DPF. Drive with care. Scan. No regen copy.

**AdBlue (diesel):** they say AdBlue / urea / DEF. Not 9, not 6. Limited driving; remaining-starts / no-start is Stop. Ask the garage for SCR / reagent status, not a parts fork.

**EV:** turtle / limited power; car-with-! and no skid lines; charge plug; HV on-screen text. Not 12, not 8. Limited unless red or paired with a stop lamp. Tesla: accept pasted alert text.

**Blue / green:** main beam, indicators, cruise, fog. Name the status function. Ask if any circled lamp is also on. Engine-cold blue thermometer: not id 2.

**Glow 13 went out after start:** not a fault. No garage card.

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

Lookup 404 → ask fuel, then matching board. 503 → ask fuel; `unknown` only if they do not know. Never default electric.

Do not diagnose. Do not add new lamp ids.
