# 9 `dpf` — diesel only

Deep outlook notes for lamp 9. **Not a second SKILL.** If this file disagrees with `SKILL.md`, `references/prognosis.md`, or `references/prognosis-cards.md`, those three win.

Petrol / hybrid GPF is **not** this file. AdBlue is **not** this file.

## When

Run Step 6 from this card when **all** of:

- The board is **diesel** (including diesel hybrid, and “your Transit” on the diesel picture).
- They picked **9**, or named the exhaust box with dots as the diesel particulate filter.
- This is **not** AdBlue / urea / DEF (those are not 9 and not 6).
- This is **not** petrol or hybrid GPF (keep that board; do not run this copy; no regen speech).

Then pick **one** branch:

| Facts | Bucket | Close-it-yourself |
|---|---|---|
| Steady amber, driving normally | `owner`, then `garage` if **one** handbook regen does not clear it | One handbook regen. Not a scan-tool regen |
| Flash, limp, red warning, or oil over maximum | `poor` | No more motorway loops. Do not drive it in — arrange recovery |

Do not upgrade `garage` to `poor` only because the car is old, unless they already have a large estimate or they are on the flash / limp / oil-over-max row.

## Owner copy

Spoken outlook after the fault statement. Each branch is ≤120 words. No slugs, no URLs, no plates. No pounds unless the live `repair_cost` tool returned a headline in this chat.

### Steady, driving normally (~87 words)

**[Outlook]** Close it yourself first: one regeneration drive exactly as this car’s handbook says. If the lamp stays after that one attempt, a garage can usually handle it.

**[Repair]** We publish a cleaning figure only if the cost tool returns a headline. If it does not, we publish no figure — ask two local garages for written estimates.

**[Close it]** Check the oil. Use the handbook speed, gear, and duration, in the open — never in an enclosed garage. Do not clear the lamp. Do not force a regen with a scan tool.

Omit **[Sell]** on this branch.

### Flash, limp, or oil over maximum (~112 words)

**[Outlook]** Repair may cost more than the car as it sits. If the lamp flashes, a red warning is on, the car is in limp mode, or the oil is over maximum, arrange recovery — do not drive it in. Do not keep repeating motorway runs.

**[Repair]** We often publish no cleaning figure. There is no published replacement-filter price. Ask two garages for written estimates.

**[Sell]** We publish no used-car price. Get one bid as the car sits and one written estimate, then compare them before you authorise work. Recovery is part of that cost if it must not be driven in. A missing factory filter is a test and value problem — not a cheap delete.

Omit **[Close it]** on this branch.

## Slugs

Call **only** `dpf-cleaning-cost` — on **both** branches.

- Still call it when you expect `gbp: null`. Null / `no_verified_price` / `no_published_job` **is** the answer: we publish no figure; two written estimates; do not fill the gap.
- If `status: ok` and a headline exists, say that headline as a planning range, not a quote for this car.
- There is **no** published DPF-replace slug. Do not invent a filter price.
- Do not call `car-diagnostic-test-cost` on this diesel DPF path (that slug is for engine-steady / GPF).
- Do not call cat, clutch, belt, or battery slugs because this lamp is on.
- Never pick a slug because it is the only one with a number.
- A cost page is not a diagnosis. Do not say the filter “needs a clean” because the slug exists.

## Sell

Only on the **poor** branch, or if they later already have a large written estimate on the steady branch.

1. Repair: verified cleaning headline, or no published figure.
2. Sell: get **one** bid **as it sits** (often not a runner if recovery applies). Get **one** written garage estimate.
3. If the estimate is larger than the bid, selling is often the better outlook.
4. Recovery / collection is part of sell cost when they must not drive it in.
5. A missing or failed factory DPF is a test and value problem.
6. Do **not** suggest deletion as a cheap fix. Do not instruct how to remove it.

On the steady / close-it-yourself / garage branch: do not push selling.

There is no sell-price API. Do not invent Parkers, WeBuyAnyCar, or trade-in pounds. Do not say the car is a write-off.

## DIY

Allowed **only** when outlook is good **and** the lamp is steady with the car driving normally (`owner`):

1. Check the oil level.
2. **One** handbook regeneration: speed, gear, and duration from **this** car’s handbook — not a generic motorway recipe from this file.
3. In the open. Never regenerate in an enclosed garage or workshop (carbon monoxide).
4. If the lamp remains after that **one** attempt: garage. Do not keep looping.

The first handbook drive is allowed. “No more motorway loops” applies after flash / limp / red warning / oil over maximum — not as a ban on that single handbook attempt.

Not DIY (either branch):

- Scan-tool **forced** regen
- Clearing the lamp as a fix
- Repeating motorway runs after flash / limp / red warning / oil over maximum
- Enclosed-space regen
- Cutting out or deleting the filter
- Naming soot versus ash as the closed path
- Exhaust work or lifting the car

A small OBD reader does **not** close this lamp. Handbook regen is the owner path, not a device path.

Vans: same DIY rules. Say “your Transit”. A day off the road may be said as downtime, not as a made-up day-rate.

## Red lines

1. **Not GPF.** Petrol or hybrid + exhaust-dots or pick of 9: unmatched GPF. No diesel regen copy. Do not switch board.
2. **Not AdBlue.** Do not map urea / DEF to 9.
3. **No diagnosis.** Not “blocked DPF”, not soot-loaded versus ash-loaded, not a named sensor.
4. **Tell the garage** (statement, not diagnosis): soot load and differential pressure readings, not a parts shortlist and not a soot-versus-ash fork.
5. **No invented pounds.** No cleaning range, no replacement-filter price, no used-car bid invented in this file or in speech.
6. **No scan-tool forced regen.** Handbook regen is not forced regen.
7. **No delete.** Not as a repair, not as a value add, no how-to.
8. **Never clear the lamp** as a fix.
9. **Never enclosed-space regen.**
10. **No real plates** in this file. Do not print a plate in speech.
11. **No SAE J2012** wording.
12. **MOT:** a missing factory DPF can be a Major where one was fitted. Do not say “Expect a fail” from this lamp alone. Gate on first-use + fuel; link the [DVSA inspection manual](https://www.gov.uk/guidance/mot-inspection-manual-for-private-passenger-and-light-commercial-vehicles).
13. **A cost slug is not a diagnosis.**
14. Safety and recovery stay **above** any shop or scanner link.

## Pass / fail

**Pass**

- Diesel 9, steady, driving normally: one handbook regen, then garage if it stays.
- Flash / limp / oil over max: `poor`; no more motorway loops; do not drive it in; recovery.
- Call `dpf-cleaning-cost`; speak the headline or “we publish no figure — two written estimates.”
- Oil check + handbook regen only on the good branch; never in an enclosed space.
- Ask the garage for soot load and differential pressure, not a parts guess.
- Poor branch only: one bid as it sits versus one written estimate; recovery in the sell cost when they must not drive it in.
- Van: “your Transit” on the diesel board.
- Petrol exhaust-dots sent to GPF, not this copy.

**Fail**

- Regen copy on petrol / hybrid GPF.
- “It’s soot-loaded / ash-loaded / the DPF is blocked.”
- Scan-tool forced regen steps.
- “Just cut it out” / delete as a cheap fix, or delete how-to.
- Invented GBP (a cleaning range, a replacement-filter price, a trade-in figure).
- Clearing codes as a repair.
- Enclosed garage regen.
- Calling cat / clutch / `car-diagnostic-test-cost` because this lamp is on.
- Treating the cleaning cost page as the failed part.
- “Expect a fail.”
- A real registration in this file or in speech.
- Mapping AdBlue to 9.
