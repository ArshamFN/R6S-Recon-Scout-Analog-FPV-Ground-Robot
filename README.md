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
- Achieve low-latency analog FPV video on a custom-built recon drone, driven by real-life law enforcement applications and inspired by the R6S Recon Scout
- Design and 3D print a compact dumbbell chassis from scratch
- Document the full hardware integration process — wiring, ESC flashing, TX configuration
- Build a fun, capable RC robot as a counterpart to more software-heavy portfolio projects

![Reference 1](images/Refrence-1.jpeg)
![Reference 2](images/Refrence-2.jpg)

## Hardware Platform

### Core Components
- **Chassis:** Custom 3D-printed dumbbell form factor
- **Drive Motors:** 2× 2212 920KV Brushless Motor (2S rated, operator-owned)
- **ESCs:** 2× BLHeli-S 20A ESC (2–4S, flashed to bidirectional mode)
- **Receiver:** FlySky FS-iA6B (6CH, AFHDS 2A, iBUS/PPM)
- **Transmitter:** FlySky FS-i6X (10CH, AFHDS 2A — operator-owned)
- **Camera + VTX:** AKK BA3 5.8GHz 40CH AIO, 200mW, 600TVL
- **FPV Goggles:** 5.8GHz receiver goggles (operator-owned)
- **Power:** 2× 2S 800mAh 50C LiPo in parallel (1600mAh total, operator-owned)
- **UBEC:** UBEC-3A 5V Mini BEC 2–6S DC-DC Converter (operator-owned)

### Technical Specifications

| Component | Specification |
|-----------|---------------|
| **Form Factor** | Dumbbell — two wheel hubs, central barrel, rear stabilizer stem |
| **Barrel Diameter** | ~40mm |
| **Total Width** | ~150mm + (wheel thickness × 2) |
| **Drivetrain** | Differential steering, 2WD brushless |
| **Motor KV** | 920KV |
| **Motor Torque** | ~0.208 N·m per motor at 20A |
| **Battery** | 2× 2S 800mAh 50C in parallel — 7.4V nominal, 1600mAh, JST |
| **Est. Runtime** | ~10–12 min at normal driving loads |
| **ESC Protocol** | DSHOT / BLHeli-S, bidirectional mode enabled |
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
| AKK BA3 VTX + Camera | UBEC 5V regulated output (within 3.3–5.5V operating range) |

## Chassis Design

The robot matches the R6S Recon Scout's dumbbell silhouette:

- **Wheel hubs:** Each hub houses one 2212 920KV brushless motor directly. The motor mounts to the barrel end cap via 4× M3 bolts on two 16mm and two 19mm bolt circles.
- **Barrel:** Central cylinder containing the ESCs, receiver, UBEC, and all wiring. The AKK BA3 camera faces forward through the front face of the barrel.
- **Rear stem:** Passive ground-contact leg that resists motor reaction torque — without it, the body would rotate in the opposite direction of the wheels rather than the wheels driving the robot forward.

## Current Status

**Last Updated:** March 15, 2026

### Completed Milestones

**Planning & Design:**
- ✅ System architecture defined — pure analog FPV, no onboard computer
- ✅ Motor and ESC selection finalized (2212 920KV + BLHeli-S bidirectional)
- ✅ Receiver selected (FS-iA6B, confirmed AFHDS 2A telemetry support)
- ✅ Camera selected (AKK BA3 AIO — fits barrel form factor)
- ✅ Chassis concept designed — dumbbell form factor matching R6S reference
- ✅ Full BOM sourced and purchased
- ✅ All hardware received

**Prototyping:**
- ✅ First wheel prototype printed (PLA — geometry check)
- ✅ ESC bidirectional flashing
- ✅ Transmitter binding and mixer configuration

**Pending:**
- ⏳ Barrel body design finalized around actual ESC dimensions
- ⏳ Barrel body printed and assembled
- ⏳ Full mechanical assembly
- ⏳ First drive test

### Known Design Considerations

- **FS-iA6B antenna:** Must not be enclosed in a solid printed shell. Route antenna wire to exit through the barrel wall.
- **Battery connector:** 2S packs use JST — verify ESC power lead connector before wiring.
- **Motor direction:** One ESC set to `Bidirectional`, the other to `Bidirectional Reversed`. Getting this wrong results in one wheel driving backward — correct in BLHeli Configurator, not by swapping motor wires.
- **VTX power level:** Drop to 25mW indoors to avoid multipath interference. 200mW for outdoor use.

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
