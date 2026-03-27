# Session 001 — Body Design v1, ESC Flashing, Receiver Binding & Elevon Mix

**Date:** 2026-03-17  
**Status:** ✅ Complete

---

## Goal

Design and print a first body to test motor fitment, flash both ESCs to
bidirectional mode, bind the FS-iA6B receiver to the FS-i6X transmitter, and
configure the elevon mix for differential steering.

---

## What Was Accomplished

1. First body design printed in PLA — motor fitment confirmed, but body was
   significantly oversized once ESCs arrived
2. Body redesigned around actual ESC dimensions — more compact and accurate barrel
   diameter
3. Both ESCs successfully flashed to bidirectional mode via BLHeliSuite
4. FS-iA6B receiver bound to FS-i6X transmitter
5. Elevon mix configured on FS-i6X — differential steering bench-tested and
   confirmed working
6. Wiring diagram produced for the repository

---

## Body Design — v1 and Redesign

The first body was designed and printed in PLA to verify motor fitment and establish
a physical reference for the barrel geometry. Motor fitment was confirmed. However,
once the ESCs arrived, it became clear the original barrel internal volume estimate
was based on incorrect ESC dimensions — the HSKRC OPTIO 20A ESCs are significantly
smaller than anticipated, leaving the body oversized.

![body v1](../images/session-001/session-001-body-v1.png)

The body was redesigned around the actual ESC footprint. The redesigned barrel is
more compact and better matches the target dumbbell silhouette.

---

## ESC Flashing — Correction to Session 000 Plan

Session 000 documented the plan to flash the ESCs using BLHeli Configurator via
Arduino Uno RESET-to-GND passthrough. This procedure is incorrect for a no-flight-
controller setup. BLHeli Configurator only supports ESC configuration via flight
controller passthrough — it cannot communicate directly with an ESC.

The correct tool for direct ESC flashing is **BLHeliSuite** (Windows desktop
application). The Arduino Uno was used as a 4-way interface by flashing it with
dedicated firmware via the Make Interfaces tab in BLHeliSuite.

**Arduino firmware:** `4wArduino_m328P_16_PB3PB4v20006.hex` (PB3PB4 variant —
the MULTI hex did not work)  
**ESC signal wire connection:** Arduino pin 11  
**Interface selection in BLHeliSuite:** SILABS BLHeli Bootloader (4way-if)

**Critical timing requirement:** Click Read Setup in BLHeliSuite first, then plug
in the LiPo within 1–2 seconds. The ESC bootloader window opens at power-on and
closes almost immediately — missing this window requires repowering the ESC and
retrying.

**ESC configuration:**
- ESC1 → Motor Direction: `Bidirectional`
- ESC2 → Motor Direction: `Bidirectional Reversed`

---

## Receiver Binding

Binding used the standard FS-iA6B bind plug method. The ESC BEC provided 5V to
the receiver during the bind sequence. Transmitter placed into bind mode via the
RX Bind menu. Bind completed on first attempt. Bind plug removed after binding.

---

## Elevon Mix Configuration

Elevon mix enabled on the FS-i6X for differential steering. The default travel
value within the elevon mix menu was 50% on both channels — this caused limited
throw and sluggish response. The fix was within the mix menu itself, not in the
endpoint/travel adjust settings.

**Final elevon mix settings:**
- CH1 and CH2 travel: 100%
- Rate: 100
- Expo: 70

**Control mapping:**
- Right stick Y axis — forward / reverse
- Right stick X axis — differential steering
- Left stick throttle Y axis — reserved for future variable speed limiter

The right stick is spring-loaded and self-centering. The left stick throttle axis
is non-spring-loaded and is reserved for a future variable speed limiter feature.
This feature cannot be implemented natively on the FS-i6X and would require a
microcontroller between the receiver and ESCs.

---

## Wiring Diagram

A wiring diagram was produced for the repository this session. The diagram reflects
the corrected ESC flashing procedure using BLHeliSuite and the PB3PB4 firmware —
not the BLHeli Configurator method originally documented in Session 000.

![ESC to Arduino Wiring Diagram](../images/session-001/session-001-esc-programming-wiring-diagram.png)

---

## Next Steps

- [ ] Print revised body in PLA
- [ ] Print battery cover and body cap in PLA
- [ ] Print wheels and rear stem in TPU
- [ ] Install heat set inserts
- [ ] Complete full wiring and assembly
