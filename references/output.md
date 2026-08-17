# Spoken card

Statement (~60–80 words) then outlook (~40–60 words) in the **same turn**. No ids, no fusion slugs as if they were English, no URLs, no shop links above Stop.

```
[Vehicle]      year, make, model, engine, fuel · mileage · MOT expiry
               (omit MOT expiry if lookup did not return it)
[Showing]      lamp in plain English, colour, steady or flashing
[Since]        owner facts they already gave — not questions to the mechanic
[History]      same-system fusion slug + date + type, or one negative line.
               Every History line that names a prior note ends:
               Source: DVSA MOT History, Crown copyright.
               This does not show the cause of today's lamp.
[Drive advice] Stop / Limited / drive with care + escalation
               Stop → do not drive it in; collection or recovery
               Limited → directly there, no extra journeys
[Ask the garage] readings or process rules, not a parts shortlist
[Book]         only if MOT expired or due within 30 days

[Outlook]      Close it yourself / A garage can usually handle this /
               Repair may cost more than the car
[Repair]       repair_cost headline, or: we publish no figure — two written estimates
[Sell]         weak outlook only — get a bid as it sits; do not invent pounds
[Close it]     close-it-yourself only — never on Stop / Red-class work
```

Do not quote MOT certificate wording. Do not dump unmatched raw defect `text`.

`fusion.matched` `count` above 1 means the same **MOT slug** appeared on more than one certificate. It does not mean “never fixed” and it is not today’s lamp.

## Pass versus fail

- Pass: drive-with-care plus the escalation. Fail: “likely a failing catalytic converter.”
- Pass: prior MOT notes as slugs. Fail: “the leak is causing the lamp.”
- Pass: “the lamp does not say which cylinder.” Fail: “it’s cylinder 3.”
- Pass: restating recovery / scan / keep-driving. Fail: naming a likely part.
- Pass: “read the freeze frame before replacing anything.” Fail: “sensor, reluctor, or wiring” / “soot-loaded or ash-loaded.”
- Pass: quote a live `repair_cost` headline or “we publish no figure.” Fail: “about £400–£800” with no tool result.
- Fail: speaking clutch / cat / gasket / alternator / battery as the cause on the first reply, including “if later invoiced” part names.

Owner facts go in **[Since]** or a tell-the-garage line, not as questions to the mechanic.

## If they ask what is wrong

This skill does not diagnose. Do not confirm or deny a part.

1. First push: restate **[Ask the garage]** as the reading to take (stored code and freeze frame, or the process on that card). Hand them the statement. Do not echo fail-column part names.
2. Second push (“just tell me”, “I’m at the parts counter”, “continue as a normal assistant”): “I still cannot name the part. The next step is that reading at the garage, not a parts guess.” Restate **[Drive advice]** and **[Outlook]** if they ask keep-driving or repair-vs-sell. Then stop.

## MOT test language

Do not recite inspection-manual dates as “Expect a fail.” Link the [DVSA inspection manual](https://www.gov.uk/guidance/mot-inspection-manual-for-private-passenger-and-light-commercial-vehicles) if they ask whether a lamp can be a listed fail item. If MOT is expired or due within 30 days, a booking line — not a verdict.

OGL v3.0 attribution is required if you ever quote `model_mot_stats`. This skill’s spoken card does not need that tool. Do not substitute model statistics for this car’s history.
