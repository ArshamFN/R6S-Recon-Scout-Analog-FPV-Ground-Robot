# R6S Recon Scout — Analog FPV Ground Robot

A miniature differential-drive ground robot inspired by the Recon Scout from Rainbow Six Siege, built around analog 5.8GHz FPV drone components for low-latency video and long-range RC control.

![Project Status](https://img.shields.io/badge/status-in%20progress-yellow)
![Platform](https://img.shields.io/badge/platform-FlySky%20FS--i6X-blue)
![Video](https://img.shields.io/badge/video-5.8GHz%20Analog%20FPV-orange)
![License](https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey)

## Project Overview

**Goal:** Build a functional miniature FPV ground robot matching the dumbbell form factor of the R6S Recon Scout, using off-the-shelf drone electronics for real-world performance.

**Why This Project:**
- Apply drone electronics knowledge to a ground robotics platform
- Achieve low-latency analog FPV video on a custom-built recon robot, driven by real-life law enforcement applications and inspired by the R6S Recon Scout
- Design and 3D print a compact dumbbell chassis from scratch
- Document the full hardware integration process — wiring, ESC flashing, TX configuration
- Build a fun, capable RC robot as a counterpart to more software-heavy portfolio projects

![Reference 1](images/Refrence-1.jpeg)
![Reference 2](images/Refrence-2.jpg)

## Hardware Platform

### Core Components
- **Chassis:** Custom 3D-printed dumbbell form factor
- **Drive Motors:** 2× 2212 920KV Brushless Motor (2S rated, operator-owned)
- **ESCs:** 2× HSKRC OPTIO 20A BLHeli_S 16.7 (A-H-25) (flashed to bidirectional mode)
- **Receiver:** FlySky FS-iA6B (6CH, AFHDS 2A, iBUS/PPM)
- **Transmitter:** FlySky FS-i6X (10CH, AFHDS 2A — operator-owned)
- **Camera + VTX:** AKK BA3 5.8GHz 40CH AIO, 200mW, 600TVL
- **FPV Goggles:** 5.8GHz receiver goggles (operator-owned)
- **Power:** 2× 2S 800mAh 50C LiPo in parallel (1600mAh total, operator-owned)
- **UBEC:** UBEC-3A 5V Mini BEC 2–6S DC-DC Converter (operator-owned)
- **RC Light Bar:** 32PCS LED Roof Lamp, 100mm, 5V–8.4V — 3 modes: On, Breathing, Strobe

### Technical Specifications

| Component | Specification |
|-----------|---------------|
| **Form Factor** | Dumbbell — two wheel hubs, central barrel, rear stabilizer stem |
| **Barrel Diameter** | ~40mm |
| **Total Width** | ~150mm + (wheel thickness × 2) |
| **Drivetrain** | Differential steering, 2WD brushless direct-drive |
| **Motor KV** | 920KV |
| **Battery** | 2× 2S 800mAh 50C in parallel — 7.4V nominal, 1600mAh, JST |
| **Est. Runtime** | ~10–12 min at normal driving loads |
| **ESC Signal Protocol** | PWM (BLHeli_S bidirectional mode) |
| **RC Protocol** | AFHDS 2A (2.4GHz) |
| **Video Protocol** | Analog 5.8GHz, 40 channels, up to 200mW |
| **Video Latency** | <30ms (analog) |
| **Camera Resolution** | 600TVL |
| **Telemetry** | Battery voltage via AFHDS 2A back-channel |

### Power Architecture

| Component | Power Source |
|-----------|-------------|
| ESCs | 2S LiPo main lead (parallel pack) |
| Receiver | 2S LiPo main lead — direct connection enables accurate voltage telemetry |
| AKK BA3 VTX + Camera | UBEC 5V regulated output (within BA3 operating range: 3.3–5.5V) |
| RC Light Bar | FS-iA6B receiver — 5V channel output (within light bar operating range: 5V–8.4V) |

## Chassis Design

The robot matches the R6S Recon Scout's dumbbell silhouette:

- **Wheel hubs:** Each hub houses one 2212 920KV brushless motor directly. The motor mounts to the barrel end cap via 4× M3 bolts on two 16mm and two 19mm bolt circles.
- **Barrel:** Central cylinder containing the ESCs, receiver, UBEC, and all wiring. The AKK BA3 camera faces forward through the front face of the barrel.
- **Rear stem:** Passive ground-contact leg that resists motor reaction torque — without it, the body would rotate in the opposite direction of the wheels rather than the wheels driving the robot forward.

### Body Structure

The barrel assembly consists of four 3D-printed pieces:

| Piece | Function |
|-------|----------|
| **Main Body** | Primary electronics housing — ESCs, receiver, UBEC, all wiring |
| **Main Body Cap** | Forward-facing face of the barrel — mounts AKK BA3 camera and antennas |
| **Battery Cover** | Removable panel providing frequent-access battery compartment |
| **Rear Stem** | Separate piece attaching above the Battery Cover — passive stabilizer leg |

All inter-piece joints use **M3×6×5 heat set inserts**: 4.1mm hole diameter, 7mm hole depth, minimum 1mm wall thickness around each insert.

## Current Status

**Last Updated:** March 27, 2026

### Completed Milestones

**Planning & Design:**
- ✅ System architecture defined — pure analog FPV, no onboard computer
- ✅ Motor and ESC selection finalized (2212 920KV + HSKRC OPTIO 20A BLHeli_S bidirectional)
- ✅ Receiver selected (FS-iA6B, confirmed AFHDS 2A telemetry support)
- ✅ Camera selected (AKK BA3 AIO — fits barrel form factor)
- ✅ Chassis concept designed — dumbbell form factor matching R6S reference
- ✅ Full BOM sourced and purchased
- ✅ All hardware received

**Electronics:**
- ✅ ESCs flashed to bidirectional mode via BLHeliSuite (ESC1: Bidirectional, ESC2: Bidirectional Reversed)
- ✅ FS-iA6B receiver bound to FS-i6X transmitter
- ✅ Elevon mix configured on FS-i6X — 100% travel, Rate 100, Expo 70
- ✅ ESC PWM calibration complete (Min 1000µs, Center 1500µs, Max 2000µs)
- ✅ ESC startup tuning complete — Low RPM Power Protect off, Startup Power high, Demag Compensation low, Motor Timing high
- ✅ Full wiring completed outside body

**Prototyping:**
- ✅ First wheel prototype printed (PLA — geometry check)
- ✅ Body structure defined — four-piece design with heat set insert joints

**Pending:**
- ⏳ Barrel body design finalized and printed
- ⏳ Full mechanical assembly
- ⏳ Wheel material testing (PLA baseline complete — TPU and others pending)
- ⏳ First drive test
- ⏳ Requirements verification (drop, runtime, splash resistance)

### Known Design Considerations

- **FS-iA6B antenna:** Must not be enclosed in a solid printed shell. Route antenna wire to exit through the barrel wall.
- **Battery connector:** 2S packs use JST — verify ESC power lead connector before wiring.
- **Motor direction:** ESC1 set to `Bidirectional`, ESC2 to `Bidirectional Reversed`. Getting this wrong results in one wheel driving backward — correct in BLHeliSuite, not by swapping motor wires.
- **VTX power level:** Drop to 25mW indoors to avoid multipath interference. 200mW for outdoor use.
- **Variable speed limiter:** Left stick throttle axis reserved for a future speed limiter feature. The FS-i6X cannot implement this natively — a microcontroller between the receiver and ESCs would be required.

## Documentation

- [Bill of Materials](docs/bill-of-materials.md) — Complete parts list with suppliers and costs
- [Build Log](docs/logs/0000-build-logs.md) — Session-by-session assembly and testing journal

## Author

**Arsham Faghihnasiri**

Building robots and learning real hardware engineering end-to-end.

- 📍 Greater Toronto Area, Ontario, Canada
- 💼 [LinkedIn](https://www.linkedin.com/in/arsham-faghihnasiri)
- 📧 arshamfaghihnasiri@gmail.com
- 🎓 Software Engineering

## License

[Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](LICENSE)

You are free to share and adapt this project for personal and non-commercial use with attribution. Commercial use of this design or derivatives requires explicit written permission from the author.
