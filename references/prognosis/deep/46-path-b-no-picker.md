# Path B: wrap / value / service, no lamp — Step 7 only

Not a second SKILL. Live rules: `SKILL.md` (Entry, Order versus lookup, Step 7), `references/value-gain.md`. If this file disagrees, those win. Bands and how-to refusals live in `value-gain.md` and the matching deep cards (wrap `64`, maintenance `54`, modest `58`, presentation `50`, illegal `71`, vehicle card `92`). This file is the **gate**: no dashboard picker.

They are on a computer or a phone. Do **not** ask if they are driving. Do **not** hold lookup or the value line for a “have you stopped” check.

## When

Path B when **all** of these are true:

1. They name wrap, wheels, exhaust, remap, paint, PPF, stereo, racking, towbar, service, cambelt, clutch, tyres, vehicle card, or “does this add value?” / “I’ve just had X done.”
2. They have **not** said a warning lamp is lit, and they are not asking which light is on, MOT-as-fault, or a garage card for a lamp.
3. They are modifying, servicing, or presenting the car — sale-price effect only.

Then: **Step 7 only.** Skip Steps 1–6. No fault statement. No **[Drive advice]**. No **[Outlook]**. No PNG.

Lookup the plate **if they gave one**, for year / make / model in the value line. Still **no** picker.

Worked pattern: `references/examples.md` example N.

## When not

| They said | Path | This file |
|---|---|---|
| Plate only, lamp unnamed, **not** wrap / service / value | Path A: lookup, then the matching board | Do not skip the picture |
| Lamp / warning light / “there’s a light on” | Path A (Steps 1–6) | Do not stay on Step 7 |
| Lamp **and** wrap / service / value | Path A then a separate **[Value]** (`77-lamp-plus-mod.md`) | Do not drop the statement |
| “Is it worth repairing?” after a lamp | Path A through Step 6 | Not this file |

If they later say a lamp is lit, leave Path B. Run Path A (and `77` if the value question is still live). Do not stay on Step 7 only.

## Do not open the cluster

On Path B, **never** call:

- MCP `show_dashboard` (with or without `board=`)
- `open_resource` on the `file://` dashboard preview
- `show_lamp`
- a glob of `cluster-*.png` as a substitute picture
- the ASCII unknown board

Do not classify `fuel_type` / `fuel_raw` **for a board**. Fuel is not needed to state a sale-price band.

Do not list lamp names. Do not ask which **circled** number is lit. Do not ask them to pick 1–13. Empty `show_dashboard` args is a Path A fail; calling the tool at all is a Path B fail.

A plate in the same message as wrap / value / service is **not** a reason to show the PNG. That is the usual mistake. Example N: lookup, then **[Value]**. No picture.

No plate: still Step 7. Do **not** ask plate or fuel in order to open a board. Do not open the unknown 13-lamp picture as the first screen.

## Lookup (year / make / model only)

If they typed a plate, look it up in this turn. They already typed it — do not ask consent again.

```
POST https://obdcode.co.uk/api/vehicle
Content-Type: application/json

{"reg":"<the plate from this turn — do not print it>"}
```

Hard rules from `references/vehicle-lookup.md`:

- Field name is `reg`, not `registration`. POST body only.
- Do not put the plate in a URL, query string, log, filename, commit, or spoken reply.
- After success, refer to **your 2016 Fiesta** (year, make, model). Never echo the plate.
- Prefer that identity in the value line. Do not dump MOT fusion, defect lists, or a History block — there is no lamp to attach them to.
- Never invent an MOT history.

Lookup is **identity for speech**, not a board classifier. Skip Step 4 (MOT-as-lamp-context), Step 5, and Step 6.

### If lookup fails (still no PNG)

The value line still runs, thinner.

| Status | Tell the owner | Next on Path B |
|---|---|---|
| 200 | (nothing about the API) | Year / make / model in **[Value]**. No board |
| invalid_registration (400) | That registration was not accepted. Type it again with no spaces | Do not repeat the value. Do not show a picture |
| not_found (404) | New or imported cars may have no MOT yet | Ask make and year if you still need them for the value line. **Do not** ask fuel in order to pick a board. **Do not** show unknown |
| rate_limited (429) | Wait and retry once | Then continue without a board |
| lookup_unavailable (503) | Official record not available right now | Continue without a board. Do not ask fuel for a PNG |

Path A’s “then the matching board” after 404 / 503 does **not** apply here.

## Step 7 speech

Read `references/value-gain.md`. State **only** the price effect of the named work. No wrap / remap / delete / lift how-to. No invented “adds £800.”

```
[Value]   band: Strong / Modest / Little-mixed / Negative — typical buyer reaction, not a valuation
[Record]  date, mileage, invoice they paid, on a vehicle card at obdcode.co.uk
```

Point them to a vehicle card on [obdcode.co.uk](https://obdcode.co.uk). The skill does not build the card.

`repair_cost` may describe a **named published job** they asked about (cambelt, clutch, MOT). That headline is the **job**, not the **gain**. Gain stays a band. `gbp: null` means we publish no figure for the job — still no invented gain.

Illegal or MOT-hostile work stays **Negative**. Do not instruct (`71-illegal-mods-negative.md`).

### Owner copy (wrap, no lamp)

≤120 words. Fictional plate in the agent’s notes only: `AB12CDE`. Owner hears the car, not the plate.

**Owner:** plate plus “thinking of a colour wrap, will it add value?”

**Agent:** Lookup. **No** `show_dashboard`.

```
[Value] Little / mixed. On your 2016 Fiesta a colour wrap is taste. The right buyer may like it; others walk away. It rarely comes back pound-for-pound. We publish no gain in pounds. A documented cambelt or service history usually moves the bid more.

[Record] If you still wrap it, put the date, mileage, and the invoice you paid on a vehicle card at obdcode.co.uk.
```

Swap the band when the named work is service / cambelt / clutch (**Strong**), tyres / MOT / pads (**Modest**), or a delete (**Negative**). Do not dump the whole table.

## Red lines

1. No `show_dashboard`, no cluster PNG, no lamp-name list, no circled-number prompt on a value-only question.
2. No how-to for wrap, remap, filter delete, weld, or lift.
3. No invented gain pounds. Invoice they paid is **spend**, not uplift.
4. No diagnosis of a lamp via a value band — there is no lamp on this path.
5. No real plate in speech, URL, filename, log, or git.
6. Do not run Steps 1–6, **[Drive advice]**, or **[Outlook]** because they also sent a plate.
7. Do not ask if they are driving.
8. A cost slug is not a gain and not a diagnosis.

## Pass / fail

**Pass**

- Wrap / wheels / exhaust / remap / paint / PPF / service / cambelt / clutch / tyres / vehicle card / “does this add value?” and **no** lamp → Step 7 only.
- Lookup if they gave a plate; speak **your 2016 Fiesta** (or make / year / model). No plate printed.
- **[Value]** names a band from `value-gain.md`; **[Record]** date, mileage, invoice on a vehicle card at obdcode.co.uk.
- No `show_dashboard`. No `open_resource` of a dashboard PNG. No fuel-to-board classify.
- How-to refused. “We publish no gain in pounds.” Their invoice, if given, spoken as spend.
- Example N: plate + wrap → lookup, value line, stop.

**Fail**

- Calling `show_dashboard` (including empty args, `board=petrol`, or unknown) because they sent a plate with the wrap question.
- Opening `cluster-*.png`, `show_lamp`, or the ASCII board on Path B.
- Listing oil-can / engine-block names, or asking which circled number is lit.
- Asking plate or fuel **in order to show a picture** when they only asked about value.
- Asking if they are driving, or holding the value line until they confirm they have parked.
- Running Steps 1–6 / a fault statement / **[Outlook]** on wrap / service with no lamp.
- Staying on Path B after they say a lamp is lit (that is Path A, then `77` if value is still in play).
- “A wrap adds £800” / buyers pay 40% of the invoice / treating spend as uplift.
- Wrap, remap, or delete how-to.
- Printing the plate. Dumping MOT fusion into a value-only reply.
- Path A 404/503 “then the matching board” after a value-only lookup miss.
