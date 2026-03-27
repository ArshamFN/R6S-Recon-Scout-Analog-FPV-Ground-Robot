# Session 000 — Project Kickoff, Parts Acquired & First Wheel Print

**Date:** 2026-03-15  
**Status:** ✅ Complete

---

## Goal

Define the full project requirements, finalize all hardware decisions, establish
the GitHub repository and documentation structure, and begin physical prototyping
with the first 3D-printed wheel design.

---

## What Was Accomplished

1. Project requirements defined and locked in — 8 key requirements covering
   durability, runtime, video quality, charging, waterproofing, silence, cost, and
   material testing
2. All hardware decisions finalized — motor, ESC, receiver, and camera selections
   confirmed with reasoning documented
3. GitHub repository created with full documentation structure matching project
   standards
4. Full BOM compiled with all purchased and operator-owned components
5. First PLA wheel prototype designed and printed
6. ESC physical dimensions assessed on arrival — body design revised accordingly

---

## Project Requirements

The following requirements were defined at project kickoff and will govern all
design and testing decisions throughout the build:

1. **Material testing** — Multiple wheel materials must be printed and tested to
   identify the best fit for the project's performance requirements. Results to be
   documented session-by-session as a demonstration of methodical engineering process.
2. **Durability** — The robot must survive being dropped from 2 metres onto a hard
   surface without structural failure. Military-grade toughness is the target.
3. **Runtime** — Minimum 10 minutes of normal operation on a full charge.
4. **Video** — Clean, low-latency analog FPV video transmitted to goggles at all
   times during operation.
5. **Charging** — Battery charging must require minimal disassembly. A dedicated
   external battery pod is the target solution.
6. **Cost** — Total project cost to be minimized. Operator-owned drone components
   reused wherever possible.
7. **Water resistance** — The robot must be at minimum splash resistant. Full
   waterproofing is the target.
8. **Silence** — The robot must operate as quietly as possible on all surface types.

---

## Hardware Decisions

### Drive System
**2212 920KV Brushless Motors** were selected for their torque-to-size ratio and
suitability for ground drive applications. The lower KV rating means a controllable
top speed without requiring endpoint limiting on the transmitter from the outset.
The motors are operator-owned, adding zero cost to the build.

**2× HSKRC OPTIO 20A BLHeli_S 16.7 (A-H-25) ESCs** were selected for motor
control. Standard drone ESCs are unidirectional by default. BLHeli_S firmware
includes a bidirectional mode enabled via BLHeliSuite. One ESC is configured to
`Bidirectional`, the other to `Bidirectional Reversed`, so that forward throttle
drives both wheels in the correct direction without any additional wiring changes.

### Control System
**FlySky FS-iA6B** receiver selected to pair with the operator-owned FS-i6X
transmitter. AFHDS 2A protocol confirmed — provides two-way communication
including battery voltage telemetry displayed on the transmitter screen.
Differential steering is handled entirely in the FS-i6X transmitter using its
built-in elevon mix mode. No flight controller or microcontroller is required
on the robot.

### Video System
**AKK BA3 5.8G 40CH AIO FPV Camera** selected to replace the originally
considered AKK KC04. At 20×14mm and 4.7g, the BA3 is significantly more
appropriate for the barrel form factor. Max output of 200mW is sufficient for
the operating range of a ground robot. The BA3 operates on 3.3–5.5V and is
powered from the UBEC-3A 5V regulated output. The KC04 is shelved for a future
long-range build.

### Power System
Two 2S 800mAh 50C LiPo packs wired in parallel — 1600mAh total at 7.4V nominal.
Two 800mAh 50C packs in parallel deliver 80A max continuous, which is well within
the combined ESC rating. Estimated runtime at normal driving loads is approximately
10–12 minutes. A dedicated external battery pod with waterproof connector is
planned to allow charging without disassembly.

---

## Chassis Design Decisions

### Form Factor
The robot replicates the dumbbell silhouette of the R6S Recon Scout — two wheel
hubs flanking a central barrel, with a passive rear stabilizer stem. All structural
components will be 3D printed.

### Body Redesign — ESC Dimensions
The BLHeli_S 20A ESCs arrived significantly smaller than anticipated. The original
barrel internal volume estimate was based on larger ESC dimensions, leaving the
barrel oversized. The body design was revised to reflect the actual ESC footprint,
resulting in a more compact and accurate barrel diameter.

---

## First Wheel Print — PLA Prototype

The first wheel design was printed in PLA as a dimensional and fitment check.
PLA is not a candidate for the final wheel material — it is too brittle for the
2-metre drop requirement and offers poor grip on hard surfaces — but it is the
fastest and cheapest material for verifying geometry before committing to
engineering-grade filaments. The print confirmed the basic hub geometry and gave
a first physical reference for sizing the barrel end cap.

---

## Next Steps

- [ ] Flash both ESCs to bidirectional mode via BLHeliSuite using Arduino Uno as 4-way interface — `Bidirectional` on ESC 1, `Bidirectional Reversed` on ESC 2
- [ ] Bind FS-iA6B receiver to FS-i6X transmitter
- [ ] Configure elevon mix on FS-i6X for differential steering
- [ ] Finalize barrel body design around actual ESC dimensions
- [ ] Print and assemble barrel body
