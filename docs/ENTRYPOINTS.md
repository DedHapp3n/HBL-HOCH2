# HBL² Entry-Point Research

Last updated: **2026-10-23**

This document tracks application-level entry points that may be useful for HBL².

The goal is to keep **entry point** research separate from the launcher itself. HBL² should eventually be able to use whichever entry point is available without coupling its UI/runtime to one vulnerable title.

## Evidence labels

- **VERIFIED BY US** — reproduced on our hardware.
- **VERIFIED UPSTREAM** — original researcher/project demonstrated it.
- **OFFICIALLY CONFIRMED COMPONENT** — a relevant engine/title fact is confirmed by the vendor/developer, but exploitability is not.
- **COMMUNITY REPORT** — credible current report, not yet independently reproduced.
- **HYPOTHESIS** — research lead only.

---

# 1. SmileBASIC / ns2jb

**Status:** VERIFIED UPSTREAM

Current primary route.

Known target from upstream:

- Switch 2 system software: **23.0.1**
- SmileBASIC: **4.4.9**
- host: Linux/macOS + Node.js 22+
- tethered
- native execution demonstrated in the published chain
- no persistence after reboot

Primary sources:

- https://pepsipu.com/blog/2026-10-switch2-jailbreak-ns2jb/
- https://gitlab.com/pepsipu/ns2jb

HBL² role:

- baseline entry point;
- reproduce unchanged first;
- do not permanently couple launcher architecture to SmileBASIC.

---

# 2. Artemis Engine route

## Why Artemis matters

Artemis Engine has a history of Lua-based userland entry on PlayStation systems.

On PS4/PS5, public research uses Artemis titles whose save handling can lead to arbitrary Lua loading / Lua sandbox escape and eventually usermode arbitrary read/write / ROP.

This history is useful context only. A PlayStation exploit does **not** automatically transfer to Nintendo Switch.

Reference:

- https://github.com/n0llptr/remote_lua_loader
- https://www.psdevwiki.com/ps4/Vulnerabilities

## Switch titles using Artemis

### Nora, Princess and Stray Cat Heart 2
Japanese title:

```text
ノラと皇女と野良猫ハート2
```

**Engine on Switch:** OFFICIALLY CONFIRMED COMPONENT

The official Artemis Engine site explicitly states that the Nintendo Switch release uses Artemis Engine.

Nintendo JP product ID observed:

```text
D70010000013424
```

Nintendo JP product page:

https://store-jp.nintendo.com/item/software/D70010000013424

The title had a Nintendo Switch demo.

Historical official announcement:

https://nora-anime.net/news/1324

The official Artemis Engine site also lists both the Switch product and demo for this title:

https://www.ies-net.com/?cat=31

### Nora, Princess and Stray Cat Heart HD

**Engine on Switch:** OFFICIALLY CONFIRMED COMPONENT

The Artemis Engine vendor states that this was the **first Nintendo Switch title adopting Artemis Engine**.

This makes it useful for comparing engine generations and identifying common runtime fingerprints.

## Current Switch 2 exploit relevance

**Status:** COMMUNITY REPORT / NOT YET VERIFIED BY HBL²

On 2026-10-22/23, current Switch 2 hacking discussions began pointing to Artemis Engine as an alternative application route after the SmileBASIC/ns2jb release and SmileBASIC availability changes.

Alula publicly teased custom-code activity and referenced Artemis Engine in the same discussion window.

At this time HBL² must **not** claim:

- a public reproducible Artemis Switch 2 exploit exists;
- the PlayStation Artemis Lua exploit works unchanged on Switch;
- every Artemis Switch game is vulnerable;
- a demo is necessarily equivalent to a full-version build;
- Artemis provides FS/sysmodule privileges comparable to ns2jb.

Those are questions to test, not facts.

---

# 3. Artemis research checklist

## Passive identification first

Before trying any exploit behavior:

- [ ] identify exact Switch title and demo version;
- [ ] record Title ID / product ID;
- [ ] confirm Artemis Engine using primary/vendor evidence;
- [ ] compare demo vs full version;
- [ ] record Switch 1 vs Switch 2 behavior;
- [ ] identify whether Lua scripts/resources are packaged in the title;
- [ ] identify engine/runtime version if exposed;
- [ ] locate public research from the original researcher.

## Questions that matter

1. Does the Switch build still embed Lua?
2. Which Lua version?
3. Does it load script material from save data or packaged resources?
4. Is script input authenticated/validated differently from PS4/PS5?
5. Can controlled Lua be executed at all?
6. If yes, is it still inside a Lua sandbox?
7. If sandbox escape exists, what process permissions does the game have?
8. Can this route reach a useful HBL² bootstrap primitive?
9. Does it work offline?
10. Does it survive future SmileBASIC delisting/patching as an independent route?

## Success ladder

Do not jump straight to native code.

```text
identify Artemis title
        ↓
prove Lua/runtime presence
        ↓
prove controlled benign script execution
        ↓
understand sandbox
        ↓
reproduce published escape (if/when public)
        ↓
minimal HBL² bootstrap
```

---

# 4. Why multiple entry points are valuable

HBL² should treat entry points as replaceable adapters:

```text
SmileBASIC/ns2jb ─┐
Artemis title ────┼──> HBL² bootstrap contract ──> launcher/runtime
future entry ─────┘
```

This avoids rebuilding the launcher every time Nintendo patches or delists an entry application.

The ideal end state is:

- one common HBL² payload/runtime;
- several independently maintained entry adapters;
- clear capability metadata per adapter.

Example capability record:

```text
entry: smilebasic-ns2jb
native_exec: yes
fs_context: yes
graphics: research
persistent: no

entry: artemis-<title>
lua_exec: unknown
native_exec: unknown
fs_context: unknown
persistent: no/unknown
```

---

# 5. Candidate inventory policy

Do not buy random visual novels because they happen to use Artemis.

A candidate should enter the HBL² list only when at least one of these exists:

- official engine/vendor confirmation;
- executable/runtime fingerprint;
- original researcher confirmation;
- reproducible technical evidence.

For each candidate record:

- title;
- region;
- demo/full/physical;
- product/title ID;
- engine confirmation source;
- exact app version;
- availability;
- exploit status;
- researcher/source;
- local ownership/install status.

