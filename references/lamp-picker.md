# Lamp picker

Owners recognise **shapes on the cluster**, not names like "oil-pressure".

The picker is **one still PNG**. Numbers are circled on the lamps. Empty grey slots are not on this car. There is no in-chat click UI.

Numbers are **global**. 9 is always DPF. 7 is not a second drawing — the engine cell is 6; if it flashes they say flashing (id 7).

Do not ask if they are driving.

## How to show it

1. Look the vehicle up first if fuel is unknown. Classify from `references/boards.md` (`fuel_type` **and** `fuel_raw`).
2. Call MCP `show_dashboard` with **required** `board=petrol|diesel|hybrid|electric|unknown`. Empty args is a fail.
3. Call `open_resource` on the `file://` URI **in the same turn** (`~/.cursor/obdcode-uk-dashboard.png`). If that fails, say the picture did not open. Do not list names. Do not ask for a number.
4. Ask: "Which **circled** number matches the lamp that is lit? Do not count left to right. If it flashes, say flashing."

Live numbers:

- petrol / hybrid — 1–6, 8, 10–12 (ghost 9, 13)
- electric — 2–5, 8, 10–12 (ghost 1, 6, 9, 13)
- diesel / unknown — 1–6, 8–13

Do **not** list oil-can / engine-block / battery. Markdown `![]` is not the picker.

If `show_dashboard` is missing from the tool catalog, tell the operator to reload MCP and start a **new** Agent chat. Do not substitute a name list.

If `show_dashboard` exists but `open_resource` does not, glob `~/.cursor/skills/obdcode-uk-fault-intake/assets/cluster-*.png` and `open_resource` that URI.

ASCII is last resort only if no PNG could be opened, and only the unknown board:

```
                    YOUR DASHBOARD (look here)
     .--------------------------------------------------.
     |    (  RPM  )     CIRCLED NUMBERS     ( SPEED )   |
     |     .----.        .------------.      .----.     |
     |    /      \       | 1  2  3  4 |     /      \    |
     |   |   o    |      | 5  8  6    |    |    o   |   |
     |    \      /       | 9 10 11 12 |     \      /    |
     |     '----'        | 13         |     '----'     |
     '--------------------------------------------------'
  Engine cell is 6. Flashing → say flashing (7). Use circles, do not count.
```

## After they reply

Off-board number: **keep this board**. "9 is not printed on this petrol picture (empty slot). Read the circle on the shape that is lit." Widen to `unknown` only if they say none of these shapes.

After a **valid** number: one-sentence confirm. Skip `show_lamp` unless they hesitate. Drive advice in that same turn.

- Engine cell 6 without "flashing" → ask steady vs flashing. Do not assume 6.
- 12: skid-lines only. Car-with-! and no tracks is unmatched EV, not 12.
- 8 on electric: 12V rectangle only. Plug / HV message is unmatched, not 8.
- 13: if it went out after start, not a fault.
- Never map "a light came on" to a default lamp.
