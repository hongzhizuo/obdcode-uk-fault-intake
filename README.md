# obdcode-uk-fault-intake

An agent skill that takes two inputs — a **UK number plate** and **a pick from one of thirteen dashboard lamps** — and turns them into a structured, garage-ready description of a car fault.

The owner does not have to know the lamp's name. They give the plate and point at a **dashboard picture** (`assets/cluster.png`) whose shapes match the symbols on the car.

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
git clone <repo-url> ~/.agents/skills/obdcode-uk-fault-intake
```

The skill loads from ambient context. Both of these are valid triggers:

- Already picked: `reg AB12CDE, lamp 6` or `reg AB12CDE, engine-steady`
- Not yet picked: `amber engine light on, plate AB12CDE` — the skill must **show the dashboard picture** before looking up, unless a red lamp is already named

Cursor's Read tool shows images to the model, not in the owner's chat. After cloning, add this to `~/.cursor/mcp.json` (keep any servers you already have) and reload MCP / restart Cursor:

```json
"obdcode-uk-fault-intake": {
  "command": "python3",
  "args": ["/ABS/PATH/TO/obdcode-uk-fault-intake/scripts/show_lamps_mcp.py"]
}
```

Then **start a new agent conversation** — old threads will not reload the skill. A passing first run is a plate only: MCP `show_dashboard` puts the numbered cluster **in the chat** before any vehicle card. A passing safety run is an oil lamp while driving: the first sentence is stop, and lookup comes after.

## Layout

| File | Contents |
|---|---|
| `SKILL.md` | Workflow, safety ordering, output format, red lines |
| `references/lamp-picker.md` | How to show the picker: Read the cluster picture, then ask for the number |
| `assets/cluster.png` | One instrument-cluster picture; numbers are on the lamps |
| `assets/lamp-*.png` | The 13 glowing lamps (rasterized from SVG for chat) |
| `assets/svg/` | Vector sources: MDI Apache-2.0 plus three original pictograms |
| `scripts/compose_cluster.py` | Rasterizes the SVGs and rebuilds `cluster.png` |
| `scripts/show_lamps_mcp.py` | MCP server: `show_dashboard` / `show_lamp` (this is what the owner sees) |
| `references/warning-lights.md` | Thirteen UK dashboard lamps with safety grading and drive advice |
| `references/vehicle-lookup.md` | Three access tiers, response shape, privacy rules |
| `references/examples.md` | Worked runs: plate-then-picker, oil-lamp stop-first, not_found fallback, unmatched lamp, diagnosis refused |

## Vehicle lookup

Three tiers, tried in order. Everything below the first still produces a useful statement — it just carries less of the car's own history.

1. **The hosted service at `obdcode.co.uk`** — public and read-only, **no key or account needed**. Either `POST /mcp` (MCP, tool `vehicle_by_plate`) or `POST /api/vehicle` (plain JSON). Same data either way. `/api/vehicle` uses the JSON key `reg`, not `registration`.
2. **Your own DVSA credentials** — free registration at the [MOT History API portal](https://documentation.history.mot.api.gov.uk/mot-history-api/register), roughly one to five working days.
3. **Ask the owner** — make, model, year, fuel, mileage. Always available, no network needed.

Tier 1 does more than return the raw record: it resolves DVSA's certificate wording to known advisories with an explanatory URL, and tells you when the same fault has been flagged across several tests. That repeat-defect signal is the most useful thing the skill can hand a garage.

The service enforces a daily ceiling on lookups that reach DVSA, shared across all callers. Do not burst plates to probe it.

A number plate is personal data. It is used for one lookup and then discarded: never written to a file, a log, a URL, or a commit.

## Safety

Safety advice is ordered ahead of everything else, including any product or tool mention. Picker ids **1**, **2**, **3**, **7**, and **8-with-extra-symptoms** (heavy steering, a rising temperature gauge, or a belt noise) are stop-first. That triage happens **before** the vehicle lookup, because a driver may not have the seconds that lookup takes and you don't need to know the model to know that a red oil-pressure lamp means stop.

Whether a lamp constitutes an MOT defect depends on the vehicle's first-use date and whether the system is fitted. The skill links to the [DVSA inspection manual](https://www.gov.uk/guidance/mot-inspection-manual-for-private-passenger-and-light-commercial-vehicles) rather than asserting rules from memory.

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
