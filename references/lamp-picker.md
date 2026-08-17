# Lamp picker

Owners recognise **shapes on the cluster**, not names like "oil-pressure".

The picker is **one still PNG**. Numbers are already printed on the lamps. There is no in-chat click UI — they look at the picture and type the number. The PNG is **fuel-specific**. Numbers are **global** (9 is always DPF even when a petrol board omits it). Never renumber. Do not add lamp ids.

## How to show it (do this)

If the owner only sent a plate (lamp unknown):

1. Look the vehicle up first (SKILL step 3). Classify the board from `references/boards.md`.
2. Call MCP `show_dashboard` on `user-obdcode-uk-fault-intake` with `board=petrol|diesel|hybrid|electric|unknown` and `body=car|van`.
3. Call `open_resource` on the `file://` URI in that tool text (`~/.cursor/obdcode-uk-dashboard.png`). That opens the PNG in the editor preview. This **is** sending the picture.
4. Ask which number on **this** picture is lit. Say: "Reply with the number printed on the matching lamp." Do **not** say "reply 1–13" if this board omits some numbers. If it flashes, say flashing.

Boards omit lamps (do not invent a pick for a missing number):

- petrol / hybrid — no 9, 13
- electric — no 1, 6, 7, 9, 13
- diesel / unknown — all 13

Do **not** list oil-can / engine-block / battery. Do not wait for an iframe or a clickable widget. Exploring `SKILL.md` is not showing the picture. Markdown `![]` is not the picker.

If `show_dashboard` is unavailable, glob the matching cluster under `~/.cursor/skills/obdcode-uk-fault-intake/assets/` and `open_resource` that `file://` URI:

- petrol → `cluster-petrol.png`
- diesel → `cluster-diesel.png`
- hybrid → `cluster-hybrid.png`
- electric → `cluster-electric.png`
- unknown → `cluster.png`

ASCII art is last resort only if the PNG could not be opened. The drawing below is the **unknown / full board only**.

If they are driving and the lamp is 1, 2, 3, 7, or 8-with-heavy-steering/rising-temp/belt-noise: **stop first**. Showing the picture does not delay that.

Blue/green lights (main beam, indicators, cruise, fog, engine-cold) are not on this cluster. If none match, say so — do not pick the closest.

## After they reply

Accept a number, an id, or "the engine shape, not flashing".

If they pick a number **not on this board** (e.g. 9 on petrol, 1 on electric), do not invent. Call `show_dashboard` with `board=unknown` once, `open_resource` the preview, and ask again.

After a **valid** number, call `show_lamp` and `open_resource` that preview so they can confirm the shape. Do not re-show the whole cluster unless they say it is the wrong one.

- **6 vs 7** (same engine outline): still applies on petrol / diesel / hybrid. If they have not said steady or flashing, show 6 and 7, and ask only that. 6 is STEADY, 7 is FLASHING. The electric board has neither 6 nor 7.
- **12**: flashing while driving is normal; steady means off or faulty. Ask only if unclear.
- **Never** map "a light came on" to a default lamp.

The number on the picture is the id index in `references/warning-lights.md` (1 = `oil-pressure` … 13 = `glow-plug`). Colour grouping on the cluster puts 8 with the other red lamps, so the numbers are not left-to-right 1–13. Trust the badge on the lamp.

## Fallback drawing (only if the picture cannot be shown)

Paste this in a fenced code block **and** tell them the dashboard picture failed to load. This is the **unknown / full board** (all 13), not a fuel-specific cluster:

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
