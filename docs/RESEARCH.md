# HBL² Switch 2 Research Log

Last updated: **2026-10-22**

This file is the living notebook for Switch 2 homebrew / reverse-engineering developments relevant to HBL².

## Status labels

- **VERIFIED BY US** — reproduced on our own hardware.
- **VERIFIED UPSTREAM** — demonstrated/documented by the original project or author, but not yet reproduced by us.
- **COMMUNITY REPORT** — reported publicly, but not yet independently reproduced by us.
- **HYPOTHESIS** — plausible direction that still needs evidence.

---

## 2026-10-22 — ns2jb

**Status:** VERIFIED UPSTREAM

Primary sources:

- https://pepsipu.com/blog/2026-10-switch2-jailbreak-ns2jb/
- https://gitlab.com/pepsipu/ns2jb

Current public claims from the upstream write-up:

- software-only, tethered Switch 2 jailbreak;
- demonstrated on system software **23.0.1**;
- SmileBASIC **4.4.9** used as the packaged entry point;
- arbitrary native code execution as ordinary sysmodules and as the built-in `fs` sysmodule;
- intended use cases explicitly include homebrew, reverse engineering, game modding and save backup;
- access to many peripherals through MMIO;
- no coldboot persistence;
- no public full kernel / Secure Monitor takeover;
- reboot restores the original system state.

### Why it matters for HBL²

We do not need a full CFW before beginning useful work. The immediate research question is whether the published execution environment is enough to bootstrap:

1. a custom payload;
2. drawing / graphics;
3. file access;
4. a launcher;
5. eventually a more convenient entry flow.

### Local reproduction status

**NOT YET VERIFIED BY US**

Planned first reproduction:

- Switch 2 system software 23.0.1
- SmileBASIC 4.4.9
- Linux host
- Node.js 22+
- run unmodified upstream `ns2jb`
- preserve the generated `runs/` logs
- record exact upstream commit

No HBL² modification should be introduced until the unmodified demo succeeds at least once.

---

## 2026-10-22 — Mario Kart World modding demonstration

**Status:** VERIFIED UPSTREAM

pepsipu's public ns2jb write-up demonstrates modified content in **Mario Kart World** as a practical result of the jailbreak.

Important distinction:

This proves that the access is useful for real game modding. It does **not**, by itself, prove that HBL² already has a generic LayeredFS-like replacement system, a finished filesystem overlay, a permanent title takeover, or kernel control.

### HBL² takeaway

The useful question is not "can we reproduce that exact Mario Kart mod?"

The useful question is:

> Which primitive made the mod possible, and can we generalize that primitive into a clean homebrew-facing API?

---

## 2026-10-22 — Vulkan in userland

**Status:** COMMUNITY REPORT

Reported by **RavensClawX** and mirrored by the Switch 2 hacking community as:

> "Full Vulkan GPU working in userland"

Community mirror:

- https://www.reddit.com/r/switch2hacks/comments/1xcrvhb/full_vulkan_gpu_working_in_userland/

### Why this is important

If reproducible, a usable Vulkan path from userland would be a major building block for real graphical homebrew. It could move HBL² away from crude proof-of-concept drawing toward a proper accelerated UI.

Potential implications:

- accelerated launcher rendering;
- textures and icons;
- scalable UI;
- easier ports of existing graphics code;
- a foundation for emulators and richer homebrew.

### What is *not* yet established by us

We have **not** yet reproduced this result.

Before treating Vulkan as part of the HBL² architecture we need:

1. the original code / repository / technical notes;
2. required services and permissions;
3. initialization sequence;
4. swapchain / presentation path;
5. shader requirements;
6. whether the implementation is generic userland or depends on a particular exploited process;
7. successful reproduction on our hardware.

Until then, keep this as a high-priority lead rather than an architectural dependency.

---

## Entry points

### SmileBASIC 4.4.9

**Status:** VERIFIED UPSTREAM / locally installed

Current packaged ns2jb route.

Known downside:

- tethered;
- depends on a vulnerable application;
- availability can change;
- no persistence after reboot.

### Other game / cartridge entry point

**Status:** COMMUNITY REPORT / DETAILS NOT YET PUBLICLY VERIFIED

There are active community discussions about other possible application or cartridge-based entry points.

Do not buy random games based on speculation.

When a concrete title is published, record:

- exact title;
- region;
- cartridge / digital;
- version;
- required system software;
- vulnerability class;
- whether it reaches the same post-exploitation environment as ns2jb.

---

## HBL² architecture — working hypothesis

**Status:** HYPOTHESIS

```text
Entry point
    ↓
native userland/sysmodule execution
    ↓
HBL² bootstrap
    ↓
service discovery / graphics / filesystem
    ↓
launcher runtime
    ├── app enumeration
    ├── icons / metadata
    ├── payload loading
    └── logging / crash diagnostics
```

Long-term UX target:

```text
convenient title/Album-style entry
        ↓
HBL²
        ↓
Homebrew applications
```

The "Album → HBL²" experience is a **long-term UX goal**, not a currently demonstrated capability.

---

## First HBL² milestones

### M0 — Reproduce upstream

- [ ] Linux host stable
- [ ] Node.js 22+
- [ ] upstream ns2jb untouched
- [ ] FS execution verified
- [ ] logs archived
- [ ] exact upstream commit recorded

### M1 — Own code

- [ ] minimal custom payload
- [ ] deterministic return value / marker
- [ ] no game modification
- [ ] repeatable across fresh boots

### M2 — Output

- [ ] basic text / framebuffer / graphics proof
- [ ] identify usable display path
- [ ] investigate RavensClawX Vulkan work
- [ ] minimal HBL² splash screen

### M3 — Storage

- [ ] read an HBL²-owned test file
- [ ] enumerate an HBL² directory
- [ ] define safe app/package directory layout

### M4 — Launcher prototype

- [ ] application metadata format
- [ ] icon loading
- [ ] list / grid UI
- [ ] launch one test homebrew payload
- [ ] return to launcher if technically possible

### M5 — Better entry flow

- [ ] research title takeover / convenient launch vectors
- [ ] investigate Album-style UX only after capabilities are understood

---

## Proposed on-device filesystem layout

**Status:** HYPOTHESIS

```text
/HBL2/
├── apps/
│   └── hello/
│       ├── app.json
│       ├── icon.png
│       └── payload.bin
├── assets/
├── logs/
└── config/
```

No final path should be chosen until actual storage APIs and permissions are confirmed.

---

## Research hygiene

For every new claim, add:

- date;
- author / project;
- original source URL;
- exact firmware;
- exact application version;
- code/repository link if available;
- what was demonstrated;
- what is inferred;
- whether we reproduced it;
- hashes / commit IDs where useful.

This prevents a fast-moving scene from turning the project into a pile of rumors.

---

## Sources to watch

Primary / high-value:

- pepsipu blog
- pepsipu/ns2jb GitLab
- original developer repositories
- original X posts from researchers
- technical write-ups

Secondary / discovery:

- r/switch2hacks
- GBAtemp
- emulator / homebrew developer repositories

Secondary sources are useful for finding new work, but HBL² should link back to the original author whenever possible.
