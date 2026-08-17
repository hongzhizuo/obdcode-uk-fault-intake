# Lamp picker

Owners recognise **shapes on the cluster**, not names like "oil-pressure". Always show the **icons**. Never replace them with a prose list of English names.

Show all 13 images below (paths are from the skill root). Ask: "Which number matches the lamp that is lit on your car? Reply 1–13. If it is flashing, say flashing."

If the client cannot render images, fall back to the ASCII cluster at the bottom — still a drawing, not a name list.

If they are driving and the lamp is 1, 2, 3, 7, or 8-with-heavy-steering/rising-temp/belt-noise: **stop first**. This picker does not delay that.

Blue/green lights (main beam, indicators, cruise, fog, engine-cold) are not here. If none match, say so — do not pick the closest.

## Icons (show these)

**1** red oil can · `oil-pressure` · **Stop**

![1 oil-pressure](assets/lamp-01-oil-pressure.png)

**2** red thermometer in waves · `coolant-temp` · **Stop** (blue version of the same symbol = still cold, not a fault)

![2 coolant-temp](assets/lamp-02-coolant-temp.png)

**3** red (!) in a circle, or BRAKE · `brake-system` · check handbrake first; if still on, **Stop**

![3 brake-system](assets/lamp-03-brake-system.png)

**4** red seated person with a circle · `airbag-srs` · limited driving, no owner repair

![4 airbag-srs](assets/lamp-04-airbag-srs.png)

**5** steering wheel with ! · `power-steering` · **Stop** if steering has gone heavy

![5 power-steering](assets/lamp-05-power-steering.png)

**6** amber engine outline, **steady** · `engine-steady` · drive with care; does not name the fault

![6 engine-steady](assets/lamp-06-engine-steady.png)

**7** same engine, **flashing** · `engine-flashing` · **Stop**

![7 engine-flashing](assets/lamp-07-engine-flashing.png)

**8** red battery +/- · `battery-charging` · not "fit a new battery"; **Stop** if steering goes heavy, temp rises, or belt noise

![8 battery-charging](assets/lamp-08-battery-charging.png)

**9** amber exhaust with dots · `dpf` · diesel only

![9 dpf](assets/lamp-09-dpf.png)

**10** amber horseshoe tyre with ! · `tyre-pressure` · usually low pressure

![10 tyre-pressure](assets/lamp-10-tyre-pressure.png)

**11** amber ABS · `abs` · normal brakes work, anti-lock does not

![11 abs](assets/lamp-11-abs.png)

**12** amber car with skid lines · `esc-traction` · flashing while driving is **normal**; steady = off or faulty

![12 esc-traction](assets/lamp-12-esc-traction.png)

**13** amber coil · `glow-plug` · diesel; on with ignition then off is **normal**

![13 glow-plug](assets/lamp-13-glow-plug.png)

Accept number, id, or "the engine shape, not flashing". If 6 vs 7 is unclear, ask only: steady or flashing? If 12 is unclear, ask only: flashing or steady? Never map "a light came on" to a default lamp.

## Fallback drawing (only if icons cannot be shown)

Paste this in a fenced code block:

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
