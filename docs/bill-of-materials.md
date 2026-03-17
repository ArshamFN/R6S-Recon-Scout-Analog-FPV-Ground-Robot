# Bill of Materials
**Last Updated:** March 15, 2026  
**Total Cost:** ~$371 CAD

---

## Electronics

| Item | Model | Qty | Unit Price | Total | Supplier | Status |
|------|-------|-----|------------|-------|----------|--------|
| RC Receiver | FlySky FS-iA6B 6CH AFHDS 2A | 1 | $29.99 | $29.99 | Amazon.ca | ✅ Received |
| FPV Camera + VTX | AKK BA3 5.8G 40CH AIO 200mW 600TVL | 1 | $35.99 | $35.99 | Amazon.ca | ✅ Received |
| ESCs | BLHeli-S 20A 2–4S | 2 | $19.98 | $39.96 | Amazon.ca | ✅ Received |

**Subtotal:** $105.94 CAD (before tax)  
**Subtotal with tax:** ~$120 CAD

---

## Operator-Owned Components

| Item | Model | Price (tax included) | Notes |
|------|-------|-------|-------|
| RC Transmitter | FlySky FS-i6X 10CH | $108.01 | AFHDS 2A, elevon mix configured for differential steering |
| Drive Motors | 2212 920KV Brushless | $33.67 | ×2, one per wheel hub |
| UBEC | UBEC-3A 5V Mini BEC 2–6S | $8.99 | Powers AKK BA3 — 5V regulated output |
| FPV Goggles | 5.8GHz receiver goggles | Unknown | 40-channel, compatible with AKK BA3 |
| LiPo Batteries | 2S 800mAh 50C JST | $28.24 | ×2, wired in parallel — 1600mAh total |
| Silicone Wire | 24AWG mixed colours | Unknown | — |
| Heat Shrink | Assorted sizes | Unknown | — |
| JST Connectors | Male + female pairs | Unknown | Match battery connector |

**Assumed Value Total (including tax):** $250.91 CAD

---

## TOTAL PROJECT COST (purchased + pre-owned):  
**~$371 CAD (not including filaments)**

---

## Notes
- ESCs flashed to BLHeli-S bidirectional mode — one set to `Bidirectional`, one to `Bidirectional Reversed`
- Receiver powered directly from 2S LiPo main lead — within FS-iA6B operating range (4.0–8.4V), direct connection enables accurate voltage telemetry
- AKK BA3 powered from UBEC 5V regulated output — within 3.3–5.5V operating range
- Battery packs wired in parallel — voltage stays at 7.4V, capacity doubles to 1600mAh
- JST connector on battery packs — verify ESC power lead connector before wiring
- 1600mAh at 50C provides 80A max continuous — well within combined ESC limit
