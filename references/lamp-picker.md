# Lamp picker

Owners recognise **shapes on the cluster**, not names like "oil-pressure".

The picker is **one picture**: `assets/cluster.png`. Numbers are printed on the lamps. Never replace it with a prose list of English names.

## How to show it (do this)

1. Find this skill's folder (the directory that contains `SKILL.md`).
2. **Read** `assets/cluster.png` from that folder with the Read tool so the picture appears in the conversation.
3. If the path is unknown, glob `**/obdcode-uk-fault-intake/assets/cluster.png` and Read the hit.
4. Ask exactly: "Which number matches the lamp that is lit on your car? Reply 1–13. If it is flashing, say flashing."
5. Do **not** also list "oil-can / engine-block / battery". The owner is looking at the picture.

Markdown `![](assets/cluster.png)` is **not** the picker. Chat cannot resolve a skill-relative image path. If Read fails, use the ASCII fallback at the bottom — still a drawing, not a name list.

If they are driving and the lamp is 1, 2, 3, 7, or 8-with-heavy-steering/rising-temp/belt-noise: **stop first**. Showing the picture does not delay that.

Blue/green lights (main beam, indicators, cruise, fog, engine-cold) are not on this cluster. If none match, say so — do not pick the closest.

## After they reply

Accept a number, an id, or "the engine shape, not flashing".

- **6 vs 7** (same engine outline): if they have not said steady or flashing, Read `assets/lamp-06-engine-steady.png` and `assets/lamp-07-engine-flashing.png`, and ask only that. 6 is STEADY, 7 is FLASHING.
- **12**: flashing while driving is normal; steady means off or faulty. Ask only if unclear.
- **Never** map "a light came on" to a default lamp.

The number on the picture is the id index in `references/warning-lights.md` (1 = `oil-pressure` … 13 = `glow-plug`). Colour grouping on the cluster puts 8 with the other red lamps, so the numbers are not left-to-right 1–13. Trust the badge on the lamp.

## Fallback drawing (only if the picture cannot be shown)

Paste this in a fenced code block:

```
                    YOUR DASHBOARD (look here)
     .--------------------------------------------------.
     |    (  RPM  )          LAMPS          ( SPEED )   |
     |     .----.        .------------.      .----.     |
     |    /      \       | 1    2    3|     /      \    |
     |   |   o    |      | 8    6    7|    |    o   |   |
     |    \      /       | 4    5   11|     \      /    |
     |     '----'        | 9   10 12 13|     '----'     |
     '--------------------------------------------------'
```
