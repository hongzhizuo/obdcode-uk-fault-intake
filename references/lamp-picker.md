# Lamp picker

Owners recognise **shapes on the cluster**, not names like "oil-pressure".

The picker is **one picture**: `assets/cluster.png`. Numbers are printed on the lamps. The lamps are vector-sourced (see `assets/svg/`) and rasterized for chat. Never replace the picture with a prose list of English names.

## How to show it (do this)

Cursor's Read tool shows images to the **model**, not in the owner's chat. MCP image content does appear in the chat. That is why the picker is an MCP call, not a file Read.

1. Call MCP tool `show_dashboard` on server `user-obdcode-uk-fault-intake` (Cursor prefixes user MCP servers with `user-`). That puts the numbered dashboard in **their** message.
2. Ask exactly: "Which number matches the lamp that is lit on your car? Reply 1–13. If it is flashing, say flashing."
3. Do **not** also list "oil-can / engine-block / battery". The owner is looking at the picture.

Do not use Explore. Do not use `open_resource` as the picker. Do not paste markdown `![](assets/cluster.png)` — chat cannot resolve a skill-relative path, and even an https image often does not render in Cursor chat. ASCII art is a last resort only if the MCP server is disconnected **and** you have already said the picture could not be shown.

If they are driving and the lamp is 1, 2, 3, 7, or 8-with-heavy-steering/rising-temp/belt-noise: **stop first**. Showing the picture does not delay that.

Blue/green lights (main beam, indicators, cruise, fog, engine-cold) are not on this cluster. If none match, say so — do not pick the closest.

## After they reply

Accept a number, an id, or "the engine shape, not flashing".

After a number, call MCP `show_lamp` with that number so they can confirm the shape. Do not re-show the whole cluster unless they say it is the wrong one.

- **6 vs 7** (same engine outline): if they have not said steady or flashing, call `show_lamp` for 6 and for 7, and ask only that. 6 is STEADY, 7 is FLASHING.
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
