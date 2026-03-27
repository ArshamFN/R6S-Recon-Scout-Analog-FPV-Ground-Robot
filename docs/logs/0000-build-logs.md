# Test Logs & Build Journal

## Purpose

This file serves as an index of all session logs. Each session has its own
dedicated file in this folder with full details.

---

## Session Index

| Session | Date | Title | Status |
|---------|------|-------|--------|
| 000 | 2026-03-15 | Project Kickoff, Parts Acquired & First Wheel Print | ✅ Complete |
| 001 | 2026-03-17 | Body Design v1 | ✅ Complete |
| 002 | 2026-03-19 | ESC Programming Research & Arduino Interface Solution | ✅ Complete |
| 003 | 2026-03-21 | ESC Flashing, Receiver Binding, Elevon Mix & Body Redesign | ✅ Complete |
| 004 | 2026-03-23 | Heat Set Insert Testing, PETG & TPU Prints | ✅ Complete |
| 005 | 2026-03-25 | Full Assembly, First Drive Test & ESC Tuning | ✅ Complete |

---

## Session 000 — 2026-03-15: Project Kickoff, Parts Acquired & First Wheel Print

**Goal:** Define project requirements, finalize all hardware decisions, establish
the GitHub repository, and begin physical prototyping with the first 3D-printed
wheel design.

**Summary:** All hardware decisions finalized around a pure analog FPV drone
electronics stack — 2212 920KV brushless motors, HSKRC OPTIO 20A BLHeli_S ESCs,
FlySky FS-iA6B receiver, and AKK BA3 AIO FPV camera. Eight project requirements
locked in. Repository created and documentation structure established. First PLA
wheel prototype printed to verify hub geometry. ESCs arrived significantly smaller
than anticipated, requiring a body redesign.

**→ [Full session log](2026-03-15-session-000-project-kickoff.md)**

---

## Session 001 — 2026-03-17: Body Design v1

**Goal:** Design and print a first body to verify motor fitment and establish a
physical reference for the barrel geometry.

**Summary:** First body designed and printed in PLA. Motor fitment confirmed.
ESCs arrived during this session — body found to be significantly oversized against
the actual ESC dimensions. Body redesign deferred to a later session pending
research into the ESC programming approach.

**→ [Full session log](2026-03-17-session-001-body-design-and-esc-flash.md)**

---

## Session 002 — 2026-03-19: ESC Programming Research & Arduino Interface Solution

**Goal:** Research and confirm the correct software and hardware approach for
programming the BLHeli_S ESCs without a flight controller.

**Summary:** BLHeli Configurator confirmed incompatible with direct ESC
programming — it requires a flight controller in the signal path. BLHeliSuite
identified as the correct tool. Arduino Uno identified as a viable 4-way interface
using the PB3PB4 firmware, eliminating the need for a ~$30 dedicated USB linker.

**→ [Full session log](2026-03-19-session-002-esc-programming-research.md)**

---

## Session 003 — 2026-03-21: ESC Flashing, Receiver Binding, Elevon Mix & Body Redesign

**Goal:** Execute ESC flashing, receiver binding, and elevon mix configuration.
Redesign the body around the actual ESC footprint.

**Summary:** Arduino Uno flashed with PB3PB4 firmware. Both ESCs flashed to
bidirectional mode via BLHeliSuite — ESC1 set to Bidirectional, ESC2 to
Bidirectional Reversed. Receiver bound to transmitter. Elevon mix configured at
100% travel, Rate 100, Expo 70. Body redesigned around actual ESC dimensions.
Wiring diagram produced for the repository.

**→ [Full session log](2026-03-21-session-003-ESC-flashin-binding-body-redesign.md)**

---

## Session 004 — 2026-03-23: Heat Set Insert Testing, PETG & TPU Prints

**Goal:** Install heat set inserts into the printed body, resolve any fitment
issues, and reprint body components in PETG with corrected geometry.

**Summary:** Heat set insert installation attempted on PLA body — part destroyed.
Root causes identified: insufficient wall material around the cavity, and PLA
unsuitable at this wall thickness. Correct cavity dimensions established — 4.2mm
diameter, 7.2mm depth, 9.35mm outer wall. Body, body cap, and battery cover
reprinted in PETG with corrected geometry. Wheels and rear stem printed in TPU.

**→ [Full session log](2026-03-23-session-004-heat-set-testing-PETG-TPU-prints.md)**

---

## Session 005 — 2026-03-25: Full Assembly, First Drive Test & ESC Tuning

**Goal:** Complete full mechanical and electrical assembly and perform the first
drive test.

**Summary:** Heat set inserts installed, electronics soldered, full assembly
completed. First drive test: motors clicked with no forward motion — root cause
was default BLHeli_S startup parameters tuned for drone propellers, not direct-
drive wheels. Resolved via BLHeliSuite parameter changes: Low RPM Power Protect
off, Startup Power high, Demag Compensation low, Motor Timing high. PPM values
corrected to 1000/1500/2000µs. Deadband increased to eliminate spin at zero
throttle. Second drive test: robot moves under power but exhibits excessive speed,
near-zero traction, and inconsistent motor behaviour.

**→ [Full session log](2026-03-25-session-005-assembly-and-first-drive.md)**

---
