# obdcode-uk-fault-intake

An agent skill that takes two inputs — a **UK number plate** and **a pick from one of thirteen dashboard lamps** — and turns them into a structured, garage-ready description of a car fault.

The owner does not have to know the lamp's name. They give the plate and point at a **dashboard picture**. Which picture they see depends on petrol, diesel, hybrid, or electric. Numbers stay **global** (9 is always DPF). Empty grey slots mark lamps this car does not have, so people do not count cells. The engine cell is 6; flashing is spoken as 7.

It identifies the vehicle from its official MOT record, grades how urgent the lamp is, cross-references the car's own MOT defect history, and writes a statement the owner can read aloud at a service desk.

## Why lamps and not fault codes

Most OBD sites are fault-code dictionaries. This one deliberately is not, for two reasons.

**The owner usually hasn't scanned anything.** A warning lamp came on. Asking them for a `P` code assumes a tool they don't own and a step they haven't taken.

**Fault-code definitions aren't ours to publish.** Code numbers such as `P0420` are facts and free to use, but the SAE J2012 wording that defines them is copyrighted and licensed for internal use, not for republication. Datasets circulating as "CC0 J2012" have no upstream authorisation behind them. This skill sidesteps the problem entirely: it needs no code definitions, because the input is a lamp.

There is a practical consequence too. A fault-code library grows without limit — over a thousand codes, and more every year. A UK dashboard has about thirteen lamps, and that number does not grow.

## What it does not do

It does not diagnose. A steady amber engine lamp has hundreds of possible causes and naming one is guessing. The skill describes the fault precisely enough for a mechanic to narrow it down, and says plainly what remains unknown.

It also refuses to publish repair steps for work that shouldn't be attempted on a driveway: airbags and pyrotechnic components, brake hydraulics, high-pressure fuel systems, anything needing the car lifted.

## What this repository is not

This is the public skill only. It is not the [obdcode.co.uk](https://obdcode.co.uk) website source — that lives elsewhere.

It does not contain DVSA credentials, API keys, or anything that would let you call the MOT History API as DVSA.

It is not a fault-code dictionary and does not include SAE J2012 definitions.

## Install

```bash
git clone <repo-url> ~/.cursor/skills/obdcode-uk-fault-intake
```

Point `~/.cursor/mcp.json` at **that same checkout**:

```json
"obdcode-uk-fault-intake": {
  "command": "python3",
  "args": ["-u", "/ABS/PATH/TO/obdcode-uk-fault-intake/scripts/show_lamps_mcp.py"]
}
```

Reload MCP, then start a **new** Agent chat. Old threads will not reload the skill or the tools.

Triggers:

- Already picked: `reg AB12CDE, lamp 6` or `reg AB12CDE, engine-steady`
- Not yet picked: `plate AB12CDE` — lookup, then `show_dashboard` with **required** `board=`, then `open_resource`, then ask which circled number is lit
- Named engine light: ask steady vs flashing; do not open the cluster unless they are unsure

Do not ask if they are driving. Drive advice belongs in the statement.

A passing first run is a plate only: matching `cluster-*.png` (not the full 13 if fuel is known; empty `board` is a fail). A passing oil run names the oil-can and puts Stop + recovery in **[Drive advice]**, without a parking quiz.

## Layout

| File | Contents |
|---|---|
| `SKILL.md` | Workflow, safety ordering, output format, red lines |
| `references/boards.md` | Fuel → board (petrol / diesel / hybrid / electric / unknown); numbers stay 1–13 globally |
| `references/lamp-picker.md` | How to show the picker: Read the cluster picture, then ask for the number |
| `assets/cluster.png` | Unknown / full board (all 13) |
| `assets/cluster-*.png` | Per-fuel boards: petrol, diesel, hybrid, electric |
| `assets/lamp-*.png` | The 13 glowing lamps (rasterized from SVG for chat) |
| `assets/svg/` | Vector sources: MDI Apache-2.0 plus three original pictograms |
| `scripts/compose_cluster.py` | Rasterizes the SVGs and rebuilds all boards |
| `scripts/show_lamps_mcp.py` | MCP: `show_dashboard` (**required** `board=`, optional `body=` speech only) / `show_lamp` |
| `references/examples.md` | Plate-then-petrol-board, oil Stop+recovery, diesel Transit DPF, electric 12V, GPF, AdBlue, glow went out |
| `references/warning-lights.md` | Thirteen UK dashboard lamps with safety grading and drive advice |
| `references/vehicle-lookup.md` | Three access tiers, response shape, privacy rules |

## Vehicle lookup

Three tiers, tried in order. Everything below the first still produces a useful statement — it just carries less of the car's own history.

1. **The hosted service at `obdcode.co.uk`** — public and read-only, **no key or account needed**. Either `POST /mcp` (MCP, tool `vehicle_by_plate`) or `POST /api/vehicle` (plain JSON). Same data either way. `/api/vehicle` uses the JSON key `reg`, not `registration`.
2. **Your own DVSA credentials** — free registration at the [MOT History API portal](https://documentation.history.mot.api.gov.uk/mot-history-api/register), roughly one to five working days.
3. **Ask the owner** — make, model, year, fuel, mileage. Always available, no network needed.

Tier 1 also resolves DVSA certificate wording to known advisories. A slug that appears on more than one certificate is a prior note, not proof of today's lamp.

The service enforces a daily ceiling on lookups that reach DVSA, shared across all callers. Do not burst plates to probe it.

A number plate is personal data. Do not print, file, URL, or commit it after the lookup.

## Safety

Stop / recovery is **[Drive advice]** in the statement, not a flow lock and not a "are you driving?" quiz. They are using this on a computer or phone. Oil, red coolant, hydraulic brake (parking brake off), flashing engine, and ICE battery-plus-belt still grade as Stop in that block. Airbag is Limited. MOT outcome language is gated on first-use date and fuel.

## Data sources

- Vehicle and MOT records: DVSA MOT History API. Crown copyright.
- Aggregate MOT statistics, where used: DVSA anonymised MOT dataset, [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/). Attribution required on publication.
- Lamp meanings, safety grading and drive advice: original work in this repository.
- Lamp pictograms: Material Design Icons (Apache-2.0) plus original OBDCode UK drawings. See `assets/svg/NOTICE`.

Not affiliated with DVSA or DVLA. Guidance is general information for UK drivers, not a substitute for professional diagnosis.

## Licence

- Original skill text (workflow, 13-lamp reference, picker, examples) and original pictograms (oil-pressure, DPF, glow-plug): **CC-BY-4.0** (see `LICENSE`). Attribution: OBDCode UK.
- Vendored Material Design Icons in `assets/svg/`: **Apache-2.0**, Pictogrammers (see `assets/svg/NOTICE` and `PICTOGRAMMERS-LICENSE.txt`).
- Vehicle/MOT records retrieved at runtime: Crown copyright, via DVSA MOT History API. Not licensed by this file.
- Aggregate MOT statistics if quoted: OGL v3.0, attribution required.

## Contact

hello@obdcode.co.uk
