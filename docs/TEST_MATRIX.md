# HBL² Test Matrix

This matrix records what has actually been tested. Empty cells are unknown, not failures.

## Entry-point compatibility

| Date | Console | System | Entry app | App version | Upstream commit | Host | Result | Notes |
|---|---|---|---|---|---|---|---|---|
| 2026-10-22 | Switch 2 | 23.0.1 | SmileBASIC | 4.4.9 | TBD | Linux/WSL planned | NOT TESTED | Initial HBL² baseline |

## Capability matrix

| Capability | Upstream reported | Verified by HBL² | First experiment |
|---|---:|---:|---|
| SmileBASIC initial code execution | Yes | No | M0 |
| FS exploit / FS native execution | Yes | No | M0 |
| Custom HBL² native payload | Not applicable | No | M1 |
| Deterministic custom return marker | Not applicable | No | M1 |
| Basic graphical output | Community work exists | No | M2 |
| Vulkan userland path | Community report | No | M2 |
| Controller input | TBD | No | M2/M4 |
| Read HBL²-owned file | Expected research target | No | M3 |
| Enumerate HBL² app directory | Not applicable | No | M3 |
| Launch HBL²-owned second payload | Not applicable | No | M4 |
| Return to HBL² launcher | Unknown | No | M4 |
| Convenient Album/title entry | Unknown | No | M5 |

## Failure taxonomy

Use one primary category per failed run:

- **HOST** — Node/Linux/tooling failure
- **NETWORK** — Switch cannot reach host / port issue
- **ENTRY** — SmileBASIC/bootstrap state
- **TIMING** — known timing-sensitive chain behavior
- **VALIDATION** — exploit validation/check failed
- **PAYLOAD** — exploit succeeded but custom payload failed
- **GRAPHICS** — payload runs but display path fails
- **STORAGE** — payload runs but storage primitive fails
- **UNKNOWN** — insufficient evidence

Keeping these categories separate prevents a WSL networking bug from being mistaken for an exploit regression.
