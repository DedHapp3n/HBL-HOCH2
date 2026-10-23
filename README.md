# HBL²

**HBL²** is a personal Switch 2 homebrew-launcher and reverse-engineering research project.

The immediate goal is not CFW or persistence. The first target is much smaller and testable:

1. reproduce the public `ns2jb` path on owned hardware;
2. run a minimal custom native payload;
3. understand the available userland / sysmodule capabilities;
4. build a tiny launcher UI;
5. load our own homebrew payloads and assets from storage;
6. later investigate a nostalgic launcher entry flow inspired by the classic 3DS / Switch homebrew experience.

> **Status:** very early research. Nothing here should be treated as a finished exploit, CFW, or stable launcher.

## Start here

- **[Lab setup](docs/SETUP.md)** — host, WSL/network notes and the untouched ns2jb baseline
- **[Research log](docs/RESEARCH.md)** — dated findings with evidence status
- **[Entry points](docs/ENTRYPOINTS.md)** — SmileBASIC, Artemis and future application routes
- **[Architecture](docs/ARCHITECTURE.md)** — separation between entry point, platform primitives and launcher
- **[Risk notes](docs/RISK.md)** — brick/persistence boundaries and safe research policy
- **[Test matrix](docs/TEST_MATRIX.md)** — firmware/app/host compatibility and capability tracking
- **[Experiment template](docs/EXPERIMENT_TEMPLATE.md)** — copy this for every hardware test
- **[Agent rules](AGENTS.md)** — rules for Codex/local LLM work in this repository

## Related ecosystem projects

Useful projects currently appearing around ns2jb / Switch 2 research:

- [mhzsajan/ns2jb](https://github.com/mhzsajan/ns2jb) — GitHub mirror/rework of the Switch 2 FS jailbreak flow
- [Ludi-1225/switch2-ns2jb](https://github.com/Ludi-1225/switch2-ns2jb) — 22.5.0-focused ns2jb research/watch item
- [cpypwn/mac2jb](https://github.com/cpypwn/mac2jb) — Apple Silicon USB-HID tool for typing the ns2jb SmileBASIC bootstrap

More notes: **[docs/ECOSYSTEM.md](docs/ECOSYSTEM.md)**

## Current research base

Public work currently used as reference:

- [pepsipu — ns2jb technical write-up](https://pepsipu.com/blog/2026-10-switch2-jailbreak-ns2jb/)
- [pepsipu/ns2jb on GitLab](https://gitlab.com/pepsipu/ns2jb)
- Community reporting around Switch 2 homebrew, graphics, userland and modding

The upstream `ns2jb` repository stays separate from HBL². We do **not** vendor or copy the exploit wholesale into this repository. HBL² will document the exact upstream revision used for each experiment and keep our launcher / payload work separate.

## Research log

All findings, links, claims, reproduction status and open questions live in:

➡️ **[docs/RESEARCH.md](docs/RESEARCH.md)**

That document deliberately separates:

- **Verified by us**
- **Verified by upstream**
- **Community report / not yet reproduced**
- **Hypothesis / needs testing**

This matters because Switch 2 research is moving extremely quickly and claims can become stale within hours.

## Project rules

- No commercial ROMs, firmware images, title keys, prod.keys or copyrighted game assets are stored here.
- No credentials or console-unique secrets are committed.
- Public upstream projects are linked and referenced instead of blindly copied.
- Experiments should be reproducible and note firmware / software versions.
- A result is not marked **verified by us** until it has actually run on our hardware.

## Initial milestone

```text
ns2jb works unchanged
        ↓
minimal HBL² payload executes
        ↓
HBL² draws something we control
        ↓
storage / file I/O
        ↓
launcher prototype
```

## Current hardware/software target

Initial research target:

- Nintendo Switch 2
- System software: **23.0.1**
- SmileBASIC: **4.4.9**
- ns2jb host: Linux / Node.js 22+

These versions are recorded for reproducibility and may not describe future compatibility.

---

**HBL² is a research project. Expect crashes, reboots and rapidly changing assumptions.**
