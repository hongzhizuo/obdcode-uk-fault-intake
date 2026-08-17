# Lamp picker

Owners recognise **shapes on the cluster**, not names like "oil-pressure".

The picker is **one still PNG**. Live lamps have circled numbers. Empty slots say they are not on this car and have **no** circled number. There is no in-chat click UI.

Numbers are **global**. 9 is DPF on diesel only. 7 is not a second drawing — the engine cell is 6; if it flashes they say flashing (id 7).

Do not ask if they are driving.

## How to show it

1. Look the vehicle up first if fuel is unknown, **after consent**. Classify from [boards.md](boards.md) (`fuel_type` **and** `fuel_raw`).
2. Call MCP `show_dashboard` with **required** `board=petrol|diesel|hybrid|electric|unknown`. Empty args is a fail.
3. The tool returns the PNG (spec `image/png`, or `png` on Cursor 3.11). Ask: "Which **circled** number matches the lamp that is lit? Do not count left to right. If it flashes, say flashing."
4. If the owner cannot see the picture: say so. On Cursor you **may** open the `file://` URI printed by the tool (`~/.cursor/obdcode-uk-dashboard.png`). If that tool does not exist, do not glob-and-pretend. Use the ASCII last resort below.

Do **not** list oil-can / engine-block / battery.

If `show_dashboard` is missing from the tool catalog, tell the operator to run `python3 scripts/install_mcp.py`, reload MCP, and start a **new** chat. Do not substitute a name list.

ASCII is last resort only if no PNG could be shown, and only the unknown board:

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

- Petrol / hybrid **9** or exhaust-dots → `unmatched-gpf`. Keep this board.
- Other empty slots: keep this board. That number is not on this car. Ask the circle on the matching live shape. Widen to `unknown` only if they say none of these shapes.
- After a **valid** live number: one-sentence confirm. Skip `show_lamp` unless they hesitate. Drive advice in that same turn.
- Engine cell 6 without "flashing" → ask steady vs flashing. Do not assume 6.
- 12: skid-lines only. Car-with-! and no tracks is `unmatched-ev`, not 12.
- 8 on electric: 12V rectangle only. Plug / HV message is `unmatched-ev`, not 8.
- 13: if it went out after start, not a fault. Flashing glow stays 13, never 7.
- Never map "a light came on" to a default lamp.
