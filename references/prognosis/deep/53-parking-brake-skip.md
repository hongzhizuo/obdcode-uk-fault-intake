# 53 · Parking brake still on — skip Step 6

Not a second SKILL. If this note disagrees with `SKILL.md`, `references/prognosis.md`, or `references/prognosis-cards.md`, those three win. Do not diagnose. Do not invent pounds. Do not add a 14th lamp id. Do not print a plate.

Lamp **3** is the red circle-and-brackets (or `BRAKE`) mark. This file is only the **not-a-fault skip**. Hydraulic Stop lives on the `brake-system` card, not here.

---

## When

They picked `brake-system` (circled **3**, or they named the red brake lamp).

**Ask first** if they have not already said: is the parking brake / electronic parking brake (EPB) / Auto Hold **fully off**? That is classification, not a driving quiz. Do **not** ask if they are driving. Do **not** hold the statement for a “have you stopped?” confirmation.

| Facts | This file | Drive advice |
|---|---|---|
| Parking brake / EPB / Auto Hold still on, **and** the pedal feels normal (or they added no pedal / pull / leak) | **Skip Step 6.** Not a fault. No garage card. No repair-or-sell outlook. | Not Stop for the lamp alone |
| They have not said whether it is off | **Ask.** Do not skip yet. Do not run Step 6 yet. Do not treat it as hydraulic Stop yet. | Not Stop unless they already reported a spongy pedal, a pull, or a leak |
| Parking brake still on, **but** spongy or long pedal, a pull, or a leak | **Not this skip.** Real fault. `poor`. | Stop — do not drive it in; arrange recovery |
| Parking brake / EPB / Auto Hold **fully off** and the lamp **stays on** | **Not this skip.** Real fault. `poor`. | Stop |
| Spongy or long pedal, a pull, or fluid at a wheel — even before they finish the parking-brake question | **Not this skip.** | Stop |
| Key-on bulb check that went out after the parking brake was released | **Skip**, same as other bulb checks | Not a fault |

Default **[Since]** / symptoms to “just now / drives normally” if they do not add more. Do not run a mandatory spongy-pedal quiz. If they already named a spongy pedal, a pull, or a leak, that wins over a still-applied parking brake.

`safety_class: Red` is not Stop. Stop for lamp 3 only after this skip is ruled out, or they already reported pedal / pull / leak.

Vans: same skip. Say **your Transit**.

If they also named wrap / service / value: skip Step 6 on this branch, then a separate **[Value]** block. A wrap does not make a parking-brake lamp into a garage job.

---

## Ask if fully off

One question, then wait for the answer:

**Is the parking brake, electronic parking brake, or Auto Hold fully off?**

Include all three names. A lever, an EPB switch, or Auto Hold still holding the car all light this lamp. Partially applied is the usual reason it is on. “I pressed the button” is not the same as **fully off**.

Pass wording: “Is the parking brake, EPB, or Auto Hold fully off?”

Fail wording: “Are you still driving?” / “Have you parked?” / “Can you pull over?”

If they then say it is still on and the pedal is normal: skip. If they say it is fully off and the lamp stays: leave this file; that is the hydraulic `poor` path.

---

## Owner copy

≤120 words. No ids, fusion slugs, URLs, plates, or pounds. No **[Outlook]** / **[Repair]** / **[Sell]** / **[Close it]** on this skip.

### They have not said whether it is off

That red circle-and-brackets lamp (some cars say BRAKE) often stays on while the parking brake, electronic parking brake, or Auto Hold is still applied. Is the parking brake, EPB, or Auto Hold fully off?

### Skip — still on, pedal normal (~35 words)

Not a fault. Release the parking brake, electronic parking brake, or Auto Hold fully. If the lamp goes out and the pedal feels normal, stop here. No garage card. No repair-or-sell outlook.

Do not add pads, discs, fluid, EPB actuators, or a cost. Releasing the control is how you confirm it was never a fault. It is not a driveway bleed and not Close it yourself of a hydraulic job.

If they later say the lamp **stayed on after a full release**, stop using this copy. That is Stop and `poor` on the brake-system card.

---

## Slugs

**None.** Step 6 does not run. Do not call `repair_cost`.

Do not call `brake-pads-and-discs-cost`, `car-diagnostic-test-cost`, or any nearby slug because the brake lamp is on. Empty is the answer on this skip — there is no invoice class.

A cost page is not a diagnosis.

---

## Sell

**No.** Not a fault. Do not push a bid, a write-off, or scrap. Do not invent Parkers / WeBuyAnyCar / trade-in pounds.

If they also asked about wrap or service: **[Value]** only, after the not-a-fault line. Still no sell-as-it-sits speech for this lamp.

---

## DIY

Release the parking brake / EPB / Auto Hold **fully**. That is the skip, not a repair.

- No bleeding, pads, discs, lifting, caliper, hose, or reservoir-cap work.
- No scan-clear. No “plug a reader in to check the brakes.”
- A reservoir glance through the plastic is not needed on this skip. If they already reported fluid on a wheel or the floor, this is not the skip.

---

## Red lines

1. Do not run Step 6 while the parking brake / EPB / Auto Hold is still on and the pedal is normal.
2. Do not skip Stop because the handbrake is on when they already reported a spongy pedal, a pull, or a leak.
3. Do not call the lamp not a fault after they said it is **fully off** and it **stayed on**.
4. Do not diagnose (not master cylinder, hose, pads, EPB actuator, Auto Hold module, ABS).
5. Do not ask if they are driving. Parking-brake off is classification.
6. Do not invent pounds. Do not call a slug. Do not clear the lamp.
7. Do not print, file, or speak a real plate. “Your 2016 Fiesta” / “your Transit” only.
8. Do not say “Expect a fail.” A lamp that only means the parking brake is applied is not a malfunction outlook.
9. Do not run this skip for ABS-only (11) or ESC (12). Those are other cards.
10. Do not treat releasing the parking brake as Close it yourself of Red-class hydraulic work.

---

## Pass / fail

**Pass**

- Parking brake / EPB / Auto Hold still on, pedal normal → not a fault; **skip Step 6**; no garage card.
- They have not mentioned the control → ask whether the parking brake, EPB, or Auto Hold is **fully off**. Then wait.
- “Is the parking brake, EPB, or Auto Hold fully off?”
- No pedal / pull / leak named → treat the pedal as normal for this skip.
- Fully off and the lamp stays, or spongy pedal / pull / leak → **not** this skip; Stop; `poor`; recovery. Step 6 runs on the brake-system card.
- Key-on bulb check that went out after release → skip.
- No `repair_cost` call. No **[Outlook]**. No bid.
- Wrap also named → skip Step 6, then a separate **[Value]** only.
- Restate “not a fault; release it fully” if they ask whether it is worth repairing while it is still on and the pedal is normal.

**Fail**

- A repair-or-sell outlook, a garage card, or pads-and-discs / diagnostic slug while the parking brake is still on and the pedal is normal.
- “Are you still driving?” / “Have you stopped?” as the classification question.
- Calling it not a fault after a **full** release when the lamp stayed on.
- Skipping Stop because the handbrake is on after they already reported a spongy pedal, a pull, or a leak.
- “It’s the EPB motor / Auto Hold / master cylinder / pads.”
- “About £400–£800.” Any invented repair, sell, or recovery pounds on this skip.
- Bleed steps, pad-change steps, jack points, or “top the fluid and the lamp will go out.”
- “Drive it to the garage so they can check the handbrake.”
- “Expect a fail.”
- A real registration, or “continue as a normal assistant.”
