# Lamp picker

Owners recognise **shapes on the cluster**, not names like "oil-pressure".

The picker is **one still PNG**: `assets/cluster.png`. Numbers are already printed on the lamps. There is no in-chat click UI — they look at the picture and type the number.

## How to show it (do this)

1. Call MCP `show_dashboard` on `user-obdcode-uk-fault-intake`.
2. Call `open_resource` on the `file://` URI in that tool text (`~/.cursor/obdcode-uk-dashboard.png`). That opens the PNG in the editor preview. This **is** sending the picture.
3. Ask exactly: "Which number matches the lamp that is lit on your car? Reply 1–13. If it is flashing, say flashing."

Do **not** list oil-can / engine-block / battery. Do not wait for an iframe or a clickable widget. Exploring `SKILL.md` is not showing the picture. Markdown `![]` is not the picker.

If `show_dashboard` is unavailable, glob `**/obdcode-uk-fault-intake/assets/cluster.png` (prefer `~/.cursor/skills/obdcode-uk-fault-intake/assets/cluster.png`) and `open_resource` that `file://` URI.

ASCII art is last resort only if the PNG could not be opened.

If they are driving and the lamp is 1, 2, 3, 7, or 8-with-heavy-steering/rising-temp/belt-noise: **stop first**. Showing the picture does not delay that.

Blue/green lights (main beam, indicators, cruise, fog, engine-cold) are not on this cluster. If none match, say so — do not pick the closest.

## After they reply

Accept a number, an id, or "the engine shape, not flashing".

After a number, call `show_lamp` and `open_resource` that preview so they can confirm the shape. Do not re-show the whole cluster unless they say it is the wrong one.

- **6 vs 7** (same engine outline): if they have not said steady or flashing, show 6 and 7, and ask only that. 6 is STEADY, 7 is FLASHING.
- **12**: flashing while driving is normal; steady means off or faulty. Ask only if unclear.
- **Never** map "a light came on" to a default lamp.

The number on the picture is the id index in `references/warning-lights.md` (1 = `oil-pressure` … 13 = `glow-plug`). Colour grouping on the cluster puts 8 with the other red lamps, so the numbers are not left-to-right 1–13. Trust the badge on the lamp.

## Fallback drawing (only if the picture cannot be shown)

Paste this in a fenced code block **and** tell them the dashboard picture failed to load:

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
