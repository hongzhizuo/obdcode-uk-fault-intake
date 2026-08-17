# 41 · Speak `gbp: null`

Not a second SKILL. If this note disagrees with `SKILL.md`, `references/prognosis.md`, or `references/vehicle-lookup.md`, those win. Do not diagnose. Do not invent pounds. Do not freeze a headline in this file.

`gbp: null`, `no_verified_price`, and `no_published_job` are the same owner answer: **we publish no figure — two written estimates.** That is the answer. Never fill the gap with a model guess.

## When

Use this speech in Step 6 **[Repair]** (and Step 7 job talk) when any of these is true:

1. You called `repair_cost` on an **allowlisted** slug and the tool came back `gbp: null`, `no_verified_price`, or `no_published_job` (HTTP 200 with a stated reason is still a success — the null is the payload).
2. The lamp / unmatched path **allowlist is empty**. Do not hunt a nearby slug. Say we publish no figure **for this class of job**.
3. They press for “roughly how much” after a null. Restate no figure and two estimates. Do not fill.

Do **not** use this copy when `status: ok` and a headline exists. Say that headline. It is a planning range, not a quote for this car.

Still **call** an allowlisted slug even when this file marks it often-null. Skipping the tool, or swapping to a different slug because it is the only one with a number, is a fail. Call `repair_cost` in **live chats**, not while editing this file. Do not paste today’s pounds here.

Never treat a cost page as the failed part. Never invent Parkers / WeBuyAnyCar / modification-gain pounds either — there is no sell-price tool.

## Owner copy

Spoken **[Repair]** after the statement. ≤120 words. No ids, no fusion slugs, no URLs, no plates, no invented pounds.

We publish no figure. That is the answer. Ask two local garages for a written estimate and compare them before you authorise the job. Do not use a guessed range from this chat, a forum, or a typical-job memory. A cost page is not the failed part. If the garage later invoices a named published job, we can quote that planning headline then. It is still not a quote for this car. Until then, two written estimates. On a weak outlook, put one of those estimates next to a bid as the car sits. We also publish no used-car price.

(100 words.)

On garage / close-it-yourself, stop after the two estimates. Do not push selling. On weak outlook, keep **[Sell]** as bid-as-it-sits versus estimate — still no invented bid.

## Published slugs vs often-null

From `references/prognosis.md`. Call **only** when that lamp’s (or unmatched path’s) allowlist says so. Headlines live in the tool, not here.

**Published jobs** (may return a verified headline *or* null on the day you call):

| Slug | Typical use |
|---|---|
| `car-diagnostic-test-cost` | First invoice on amber engine / GPF / many “read it first” lamps |
| `car-battery-replacement-cost` | Only if the garage later invoices a 12V battery — not “it is the battery” |
| `brake-pads-and-discs-cost` | Only if they already have a pads/discs estimate, or as “a common brake invoice”, never as the cause of a hydraulic Stop lamp |
| `catalytic-converter-replacement-cost` | Weak-outlook **upper bound if** the garage later invoices a converter — not “you have a failed cat” |
| `clutch-replacement-cost` | Modification / service value, or a clutch they already named — **not** an engine lamp |
| `dpf-cleaning-cost` | Diesel DPF path. Often `gbp: null` — still call it, still say no figure |
| `head-gasket-repair-cost` | Coolant weak-outlook **if invoiced**. Often null. Not “it is the gasket” |
| `alternator-replacement-cost` | Charging path **if invoiced**. Often null. Not “it is the alternator” |
| `cambelt-and-water-pump-cost` | Value-gain / due belt, not a lamp cause |
| `timing-chain-replacement-cost` | Value-gain / due chain, not a lamp cause |
| `wet-belt-replacement-cost` | Value-gain / due wet belt, not a lamp cause |
| `mot-cost` | Booking line, not a lamp repair |
| `wheel-bearing-replacement-cost` | Only if they already named that job |

**Often-null** (still call when allowlisted; if null, this file’s speech):

- `dpf-cleaning-cost`
- `head-gasket-repair-cost`
- `alternator-replacement-cost`

Often-null is a habit, not a licence to skip the call or to invent a range. A published slug can also return null today; an often-null slug can return a headline. Read the tool.

Empty allowlist (oil-pressure, airbag, power-steering, ABS, TPMS, ESC, AdBlue remaining-starts, unmatched EV pack work, and similar): **no slug**. Same owner line: we publish no figure for this class of job — two written estimates.

## Pass versus fail

**Pass**

- “We publish no figure — two written estimates.”
- Quoting a `repair_cost` headline **after** a live `status: ok` result, as a planning range, not a quote for this car.
- “If the garage later invoices this job, published UK figures are …” — only after an allowlisted call that returned a headline.
- Calling `dpf-cleaning-cost` / `head-gasket-repair-cost` / `alternator-replacement-cost` when the card allows it, then saying no figure if the tool returns null.
- Empty allowlist: no `repair_cost` hunt; “no figure for this class of job.”
- Weak outlook: no published repair figure **and** no used-car price; bid as it sits versus a written estimate.
- Restating **[Drive advice]** and **[Outlook]** when they ask repair-vs-sell.

**Fail**

- “About £400–£800” (or any range) with no tool result.
- Filling `gbp: null` / `no_verified_price` / `no_published_job` with a model guess, a memory of last week’s page, or a forum typical.
- Skipping an often-null slug, or calling a different job because it is the only slug with a number.
- Treating a cost page as the diagnosis (“it’s the cat / gasket / alternator”).
- Calling `clutch-replacement-cost` because an engine lamp is on.
- Invented Parkers / WeBuyAnyCar / “typical trade-in” / modification-gain pounds.
- Pasting a headline into this repository as if it were today’s figure.
