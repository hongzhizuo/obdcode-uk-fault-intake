# Vehicle Lookup

A UK number plate resolves to make, model, fuel, engine size, first-use date, MOT expiry, and the full recorded MOT test history including every defect and advisory.

This file is the **vehicle** lookup. Lamp identification is a numbered picker in `references/lamp-picker.md`, not something this API does. Do not skip the picker just because the plate lookup succeeded.

Try the tiers in order. Every tier below the first still produces a useful fault statement — it just carries less of the car's own history.

## Tier 1 — The hosted service

`obdcode.co.uk` runs a public, read-only lookup. **No key, no registration, no account.** Its server card declares `authentication.required: false`.

Two transports, same data, same upstream. Pick by what your agent already speaks.

### MCP (preferred if you speak it)

```
POST https://obdcode.co.uk/mcp
Content-Type: application/json

{"jsonrpc":"2.0","id":1,"method":"tools/call",
 "params":{"name":"vehicle_by_plate","arguments":{"registration":"AB12CDE"}}}
```

Streamable HTTP, protocol version `2026-07-28`. POST only — there is no GET stream and no session handshake to maintain. Server card at `https://obdcode.co.uk/.well-known/mcp/server-card.json`; readiness at `GET /mcp/health`.

Send no `Origin` header, or send `https://obdcode.co.uk`. A foreign `Origin` is rejected with 403. Server-side agents normally send none, which is allowed.

The tool returns `{"status":"ok","vehicle":{…}}` on success, or a bare `{"status":"…"}` token on failure. JSON-RPC reports tool failure in-band: the HTTP status stays 200, so read `status`, not the response code.

### Plain HTTP

```
POST https://obdcode.co.uk/api/vehicle
Content-Type: application/json

{"reg":"AB12CDE"}
```

The only accepted key is `reg`. Sending `{"registration":…}` here is a 422 with body `{"status":"invalid_request"}`, not a silent alias and not a FastAPI `detail` array whose `input` echoes the plate. That field name belongs to the older `/api/v1/mot` route, which exists for the site's own `/check/` page and returns raw DVSA shape without the advisory matching described below. Prefer `/api/vehicle`.

### Status tokens

| Status | Meaning | What to tell the user |
|---|---|---|
| 200 | Found | Continue |
| `invalid_registration` (400) | Fails `^[A-Z0-9]{2,8}$`, or DVSA rejected it | Ask them to re-read the plate, no spaces |
| `not_found` (404) | DVSA has no vehicle for that plate | Check the plate; brand-new and some imported vehicles have no MOT record yet — fall back to asking the owner |
| `rate_limited` (429) | Over 20 lookups / 10 minutes from your IP | Wait and retry once, then ask the owner |
| `lookup_unavailable` (503) | DVSA down or busy, or the site's daily DVSA cap is spent | Ask the owner immediately |

A DVSA 429 arrives as **503 `lookup_unavailable`**, not 429. A 429 means *you* were too fast; a 503 does not.

The site enforces a daily ceiling on how many lookups reach DVSA, shared across every caller. Do not burst valid plates to probe the limits — that spends a real quota that real owners need. Invalid-format plates never reach upstream and are safe for contract checks.

### The other four tools

`vehicle_by_plate` is one of five. The rest need no plate and are worth knowing for later steps of the workflow:

| Tool | Use it for |
|---|---|
| `decode_mot_advisory` | Turn MOT certificate wording into a plain-English explanation |
| `fault_code` | Whether a graded code is safe to drive with — refuses to guess at ungraded codes |
| `model_mot_stats` | This model's MOT record and worst years |
| `repair_cost` | UK cost, **only** where a named dated source exists |

`repair_cost` returns HTTP 200 with `gbp: null` and a stated reason when no verified figure exists. That null is the answer. Do not substitute your own estimate — the whole point of the null is that a made-up number is worse than none.

## Tier 2 — Your own DVSA credentials

If the user or operator holds their own DVSA MOT History API credentials, call DVSA directly instead.

Registration is free at the [DVSA MOT History API portal](https://documentation.history.mot.api.gov.uk/mot-history-api/register) and takes roughly one to five working days. It requires a token URL, client ID, client secret and API key, exchanged for a bearer token via client credentials.

Read these from the environment. Never accept credentials pasted into a chat, and never write them to a file.

This tier returns raw DVSA shape — no advisory matching, no site deep links.

## Tier 3 — Ask the owner

Always available, needs no network, and is the correct fallback whenever the tiers above fail.

Ask for: make, model, year or registration letter, engine size, fuel, and approximate mileage.

What is lost: the car's own MOT defect history, which is the highest-value part of step 4 in the main workflow. Say so once — "I can't pull your MOT record, so I'm working from what you've told me" — and carry on. Do not silently degrade.

Do not substitute general model-level statistics for this specific car's history and present them as the same thing.

## Response shape

From tier 1. Abridged; the plate appears nowhere in it.

```json
{
  "vehicle": {
    "make": "FORD", "model": "FIESTA",
    "fuel_type": "petrol", "fuel_raw": "Petrol",
    "year": 2016, "engine_cc": "998", "colour": "Blue",
    "mot_due": "2027-03-01", "first_used": "2016-03-14"
  },
  "mot": {
    "tests": [
      {
        "date": "2026-03-02", "result": "PASSED", "expiry": "2027-03-01",
        "odometer": "61201", "odometer_unit": "MI",
        "defects": [
          {
            "text": "Front Brake pad(s) wearing thin (1.1.13 (a) (ii))",
            "type": "ADVISORY", "dangerous": false,
            "match": {"slug": "brake-pads-wearing-thin", "confidence": 1.0,
                      "url": "/advisories/brake-pads-wearing-thin/"}
          }
        ]
      }
    ],
    "test_count": 2, "last_test_date": "2026-03-02",
    "last_result": "PASSED", "advisories_last_test": 3
  },
  "fusion": {
    "matched": [{"slug": "brake-pads-wearing-thin", "count": 1,
                 "latest": "2026-03-02", "url": "/advisories/brake-pads-wearing-thin/"}],
    "unmatched_count": 1, "threshold": 0.75, "enabled": true
  },
  "links": {"make": "/mot/ford/", "model": "/mot/ford-fiesta/"},
  "sources": {"dvsa": true, "dvla_ves": false}
}
```

`fuel_type` is normalised to `petrol` / `diesel` / `hybrid` / `electric` / `unknown`; `fuel_raw` keeps the upstream wording.

Classify the lamp picture from **both** fields (`references/boards.md`). `fuel_type` alone is not enough: hybrid + Electric Diesel is the diesel picture; hybrid + missing `fuel_raw` is `unknown` (or ask petrol vs diesel hybrid). After a successful lookup, if the lamp is not yet identified, show that picture immediately — `board` is required. Empty `show_dashboard` args is a fail.

There is no van or body-type field. Optional `body=van` is speech only ("your Transit"). Same PNG as the fuel picture. Do not call it a van board.

If lookup fails, ask the owner for fuel with make, year, and mileage, then the matching picture. `unknown` only if they do not know fuel. Never default electric.

Tests come newest first. Odometer readings across tests give an annual mileage, worth mentioning when a fault is mileage-related.

Defect `type` is one of `ADVISORY`, `MINOR`, `MAJOR`, `DANGEROUS`, `FAIL` or `USER ENTERED`. Treat any entry with `"dangerous": true` as significant even on a test the car passed.

### Use `fusion`, not your own matching

`fusion.matched` is the part worth having: DVSA's raw certificate wording already resolved to a known advisory, deduped across tests, with a count, a latest date and an explanatory URL. A repeat entry means the same fault has been flagged more than once and not fixed — the single most useful thing you can hand a garage.

`match` is `null` below a 0.75 confidence threshold, and `unmatched_count` tells you how many defects that happened to. A null is honest: the service refuses to force a weak match. Quote the raw `text` for those rather than guessing at what they mean.

Registration, MOT test numbers, and other unique upstream ids are stripped before shaping.

## Privacy

The plate is personal data. The hosted service keeps registrations out of URLs and access logs, keys its cache by SHA-256 of the plate, and never echoes the plate in a success or error body. An integration must not undo that.

- Use the plate for the lookup. Do not print it afterwards.
- Never write it to a file, a log, a commit message, a filename, or a URL.
- Refer to the vehicle as "your 2016 Fiesta", never by plate.
- Do not cache the response anywhere the user did not ask for.
- If asked to save the fault statement, strip the plate from it first.
- They already typed it in the first message. Do not ask consent again. Do not claim the thread has discarded it.
- For 400: "That registration was not accepted. Type it again with no spaces." Never repeat the value.

## Terms

Vehicle and MOT records are Crown copyright. State the source when displaying them.

Aggregate MOT statistics behind `model_mot_stats` come from the DVSA anonymised MOT dataset under the [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/), which requires attribution on publication.

Per-vehicle lookups come from the DVSA MOT History **trade** API. Its terms govern what a licensee may do with the data, including re-exposure through an intermediary. That is a licensing question for whoever operates the endpoint, not something an integrator resolves — if you run your own deployment under tier 2, check your own terms.
