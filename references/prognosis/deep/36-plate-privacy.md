# 36 · Plate privacy

Not a second SKILL. Live rules: `SKILL.md` Step 3 and Red line **5**, plus the Privacy section of `references/vehicle-lookup.md`. If this file disagrees, those win. Do not diagnose. Do not invent pounds. Do not add a 14th lamp id. Do not print a **real** registration in this file.

The plate is **personal data**. Use it once, in the lookup **POST body**. After that, every owner-facing line — garage card, outlook, and **vehicle card** speech — names **your 2016 Fiesta** (year / make / model from lookup). Vans: **your Transit**. Never print, file, URL, or commit the plate.

## When

Every turn that has a plate, and every artefact that might copy one:

- Path A lookup (Step 3), then the spoken **[Vehicle]** line
- Path B lookup for year / make / model in **[Value]** — still no picker
- **[Record]** / vehicle-card speech (Step 7)
- A 400 retry, a saved garage card, a log, a filename, a URL, or a git commit

They already typed it. Do not ask consent again. Do not hold lookup for a “may I look this up?” beat.

## Four channels

SKILL: **Never put the plate in a URL, query string, log, filename, commit, or spoken reply.**

| Channel | Pass | Fail |
|---|---|---|
| **Print** (speech, garage card, chat) | **Your 2016 Fiesta** / **your Transit**. Year, make, model, engine, fuel, mileage, MOT expiry | Echoing the plate. Reading it back “to confirm”. Putting it on **[Vehicle]** or **[Record]** |
| **File** | A saved statement with the plate **stripped**. No cache the owner did not ask for | `statement.md`, a scratch note, a screenshot dump, or a cache file that still holds the plate |
| **URL** | `POST /api/vehicle` or `POST /mcp` with the plate in the **JSON body only**. Point them to [obdcode.co.uk](https://obdcode.co.uk); they type the plate on the site | Query string, path, or hash (`/check/?reg=…`, `/mot/AB12CDE`, a vehicle-card deep link that embeds the plate). Logging the request URL |
| **Commit** | This repository may use the fictional worked plate `AB12CDE` only, in examples | A real registration in git, a commit message, a branch name, or a filename |

The hosted service keeps registrations out of URLs and access logs, keys its cache by SHA-256 of the plate, and never echoes the plate in a success or error body. An integration must not undo that by printing it, writing it to disk, or putting it in git.

The lookup **response** has no plate. Registration, MOT test numbers, and other unique upstream ids are already stripped. Do not add them back into speech or files.

## What the owner hears

Spoken **[Vehicle]** (Step 5) is identity, not the plate:

```
[Vehicle]      year, make, model, engine, fuel · mileage · MOT expiry
```

Pass line (illustrative Fiesta from the worked examples):

**[Vehicle]** Your 2016 Fiesta, 998 cc petrol · 61,201 miles · MOT due 1 March 2027.

Not: the registration, a spaced plate, “reg ending …”, or a DVLA / MOT-check URL.

The same name is used in **[Outlook]**, **[Value]**, and restates. “Discard” is **output hygiene**: do not print it. The chat still holds what they typed. Do not tell them the thread has deleted it.

## Vehicle card speech

The **site** can hold a vehicle data card. The **skill** does not build that card (`92-vehicle-card-skill.md`). Skill mode states the sale-price **band** and what to record. Point them to [obdcode.co.uk](https://obdcode.co.uk). Do not print the plate. Do not mint a card URL that contains it.

```
[Value]   Band: Strong / Modest / Little-mixed / Negative — typical buyer reaction, not a valuation
[Record]  Date, mileage, and the invoice they paid, on a vehicle card at obdcode.co.uk
```

Name the car **your 2016 Fiesta** (or the looked-up make / model) in that speech. They type the plate on the site themselves.

If asked to save the fault statement or a value note, **strip the plate first**. Keep year, make, model, mileage, MOT expiry, the lamp in plain English, drive advice, outlook, and the band.

Illegal work is still **Negative**. Do not instruct. Do not present a delete as a premium on the card. Still no plate on that line.

## Lookup transport (body only)

```
POST https://obdcode.co.uk/api/vehicle
Content-Type: application/json

{"reg":"<the plate from this turn — do not print it>"}
```

- Field name is `reg`, not `registration`. The wrong key is **422**. Prefer `/api/vehicle` so an error body cannot echo `input`.
- **POST body only.** Never a GET, never a query string.
- MCP, if you speak it: `POST https://obdcode.co.uk/mcp` tool `vehicle_by_plate` with `{"registration":"…"}` in the tool **arguments**. That is still a body, not a URL. A foreign `Origin` on `/mcp` is **403** — use `/api/vehicle`.
- Do not burst valid plates to probe rate limits. That spends a shared DVSA quota.

### If lookup fails (still do not print it)

| Status | Tell the owner | Do not |
|---|---|---|
| 200 | (nothing about the API) | Repeat the plate as “found” |
| invalid_registration (400) | That registration was not accepted. Type it again with no spaces | Repeat the value, or say which character was wrong |
| not_found (404) | New or imported cars may have no MOT yet | Print the plate while asking make, year, fuel, mileage |
| rate_limited (429) | Wait and retry once | Log the plate with the 429 |
| lookup_unavailable (503) | Official record not available right now | Put the plate in a fallback URL |

Then continue thinner: owner-stated make / year / fuel, still **your 2016 Fiesta** once you have a year and model — never the plate as the fallback name.

## Illustrative plate in this repository

Worked examples in `references/examples.md` may show the owner typing `AB12CDE`. That string is **fictional**. After lookup, even that example speaks **your 2016 Fiesta** or **your Transit**, never the plate.

A real UK registration in this folder, in speech, or in git is a fail. Do not “anonymise” by printing a live plate with one letter changed.

## Red lines

1. **The plate is personal data.** Do not print, file, URL, or commit it.
2. POST body only. Never a query string, path, log, filename, or commit message.
3. Do not echo it. Do not ask consent again. Refer to **your 2016 Fiesta** / **your Transit**.
4. Vehicle-card speech uses that name. Point at obdcode.co.uk. Do not build a card or `/check/` URL that contains the plate.
5. 400: do not repeat the value. Saving a statement: strip the plate first.
6. “Discard” is not deletion. Do not claim the thread has forgotten it.
7. Do not diagnose. Do not invent pounds. Do not add a 14th lamp id.

## Pass versus fail

**Pass**

- Lookup `POST /api/vehicle` `{"reg":"…"}` (or MCP tool arguments). Plate stays in the body.
- **[Vehicle]** Your 2016 Fiesta, 998 cc petrol · mileage · MOT expiry.
- **[Record]** Date, mileage, invoice on a vehicle card at obdcode.co.uk — still **your 2016 Fiesta**, no plate.
- Van: **your Transit**. Same fuel board. No plate.
- 400: “That registration was not accepted. Type it again with no spaces.”
- Saved card or statement with the plate stripped.
- Repo examples: `AB12CDE` only, then speech is your 2016 Fiesta.

**Fail**

- Reading the plate back, or putting it on **[Vehicle]**, **[Outlook]**, **[Value]**, or **[Record]**.
- `GET` / query / `/check/AB12CDE` / a vehicle-card link that embeds the plate.
- Writing it to a file, a log, a cache, a screenshot note, or git (commit, branch, filename).
- 400 that quotes the typed value.
- “I’ve discarded your registration” as if the chat had deleted it.
- Asking consent again before a lookup they already typed a plate for.
- A real plate in this file or any other commit.

**Pass sketch:** Your 2016 Fiesta. Lookup already ran; the plate is not in this reply. Garage card names year, make, model. Vehicle card: record date, mileage, and the invoice at obdcode.co.uk — they type the plate on the site.

**Fail sketch:** Your Fiesta AB12 CDE — here is `/check/?reg=AB12CDE` and a saved `AB12CDE-statement.md`.
