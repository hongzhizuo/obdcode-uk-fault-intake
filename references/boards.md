# Vehicle boards

After a successful plate lookup, pick **ONE** still PNG. Numbers are **GLOBAL**: 9 is always DPF even when a petrol board omits it. Never renumber.

## Classify fuel → board

Use `vehicle.fuel_type` from `POST /api/vehicle` (`petrol` | `diesel` | `hybrid` | `electric` | `unknown`). Then `fuel_raw`. Apply **top row first**:

| fuel_type / raw | extra | board |
|---|---|---|
| diesel | | diesel |
| hybrid | `fuel_raw` contains `diesel` (e.g. Electric Diesel) | diesel |
| `Gas Diesel` in `fuel_raw` | | diesel |
| hybrid | otherwise, including missing `fuel_raw` | hybrid |
| electric | | electric |
| petrol | | petrol |
| LPG / Gas / CNG / LNG / `Gas Bi-Fuel` in `fuel_raw` | not `Gas Diesel` | petrol |
| unknown or missing | | unknown |

Do not add AdBlue, turtle, HV-isolation, or EV-system ids. The 13 numbers stay closed.

MCP: `show_dashboard` with argument `board` set to that id (`petrol` | `diesel` | `hybrid` | `electric` | `unknown`). Then `open_resource` the `file://` preview.

PNG files:

- `unknown` → `assets/cluster.png` (all 13)
- `petrol` → `assets/cluster-petrol.png` (hide 9, 13)
- `diesel` → `assets/cluster-diesel.png` (all 13)
- `hybrid` → `assets/cluster-hybrid.png` (same lamps as petrol)
- `electric` → `assets/cluster-electric.png` (show 2, 3, 4, 5, 8, 10, 11, 12 only)

## Lamps on each board

| board | numbers shown |
|---|---|
| unknown / diesel | 1–13 |
| petrol / hybrid | 1–8, 10–12 (no 9, 13) |
| electric | 2–5, 8, 10–12 |

## Van vs car

No body-type field on the API. Scan make+model against the conservative list below. A hit sets `body=van`. No hit: leave body unset (treat as a car). **A false van on a car is worse than missing a rare van** — do not guess, and do not widen the list.

Van does **not** change lamps. Caption only: "your 2018 Transit — diesel van board".

### Conservative lowercase substrings

Join `make` and `model` with a single space, lowercase, turn hyphens into spaces, and **keep** the remaining spaces (do not delete them — `ranger` must not match Range Rover). Never scan for `van` or `nv` (`TIGUAN` contains `van`; `CONVERTIBLE` contains `nv`). If that string contains any of these substrings, set `body=van`:

```
transit
transit custom
transit connect
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
caddy maxi
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

Use `combo cargo`, not bare `combo`. Use `transit custom` / `transit connect` as extra phrases; do not add bare `custom` or `connect`. Skip `berlingo`, `partner`, and `hercules` (passenger twins are too common).

Do **not** treat these as vans (passenger cars — never add them to the scan list):

```
fiesta
focus
golf
kuga
tiguan
polo
civic
corolla
yaris
leaf
model 3
```

## Owner talk

Refer to "your 2016 Fiesta", never the plate. Say "this board is for a petrol car. If the fuel looks wrong, say so."

If they pick a number not on this board, do not invent. Show the unknown/full board once.

## Fallback

Lookup fail → board `unknown` (ICE 13, never the electric subset). Owner says "it's a diesel" or "it's electric" → switch board and re-show.

Do not diagnose. Do not add new lamp ids.
