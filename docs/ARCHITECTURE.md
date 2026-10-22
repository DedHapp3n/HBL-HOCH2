# HBL² Architecture

This is a working architecture, not a promise that every layer is already available.

## Layer model

```text
┌──────────────────────────────────────┐
│             HBL² UI                 │
│ app grid • icons • metadata • input │
├──────────────────────────────────────┤
│          Homebrew Runtime            │
│ app loading • lifecycle • logging   │
├──────────────────────────────────────┤
│          Platform Services           │
│ graphics • storage • input • IPC    │
├──────────────────────────────────────┤
│        Native Payload / Bootstrap    │
│ minimal code under proven context   │
├──────────────────────────────────────┤
│        ns2jb / Entry Point           │
│ exploit chain maintained upstream   │
├──────────────────────────────────────┤
│             Horizon OS               │
└──────────────────────────────────────┘
```

## Design principle: exploit ≠ launcher

HBL² should not become an exploit monolith.

The launcher should consume a small set of platform primitives while the exact entry point remains replaceable.

Today that entry point is ns2jb via SmileBASIC. Tomorrow it could be another application, cartridge, browser path, or a more convenient exploit.

The UI should not care.

## Minimum platform primitives

### P0 — Execution

Required:
- execute HBL²-owned native code;
- return a deterministic status;
- log where execution failed.

### P1 — Output

One of:
- framebuffer access;
- a graphics service;
- Vulkan;
- another reliable presentation path.

Goal:
- draw a known screen without modifying a commercial game.

### P2 — Input

Required:
- basic controller input;
- debouncing / repeat policy;
- clean exit path.

### P3 — Storage

Required:
- open an HBL²-owned directory;
- read a small test file;
- enumerate application folders;
- later write logs/config safely.

### P4 — App loading

Required eventually:
- define an HBL² app metadata format;
- allocate/load an HBL²-owned payload;
- transfer control;
- define return / exit behavior.

## Upstream capabilities relevant to research

The public ns2jb write-up demonstrates substantially more than a simple application sandbox escape.

Upstream reports:
- arbitrary native code execution using ordinary sysmodule permissions;
- native execution using the built-in `fs` sysmodule;
- use of `ro` permissions;
- kernel SVC access available to that process context, including `MapProcessMemory`, `MapProcessCodeMemory`, and `SetProcessMemoryPermission`;
- use of process handles and mapped process memory as part of the published chain.

For HBL², this means process-memory research is a technically relevant future branch.

It does **not** mean we should begin by modifying arbitrary processes. First reproduce the chain and understand the exact execution context.

## Graphics branch

Current state:

- Vulkan in userland has been reported publicly by RavensClawX.
- HBL² has not reproduced it yet.

Possible architecture if reproducible:

```text
HBL² UI
  ↓
small renderer abstraction
  ├── Vulkan backend
  └── minimal fallback backend
```

Do not hard-wire the launcher to Vulkan until:
- initialization is understood;
- presentation works reliably;
- required services are known;
- code is reproducible on our target firmware.

## Proposed application format

Early concept only:

```text
/HBL2/apps/example/
├── app.json
├── icon.png
└── payload.bin
```

Possible `app.json`:

```json
{
  "name": "Hello HBL²",
  "author": "DedHapp3n",
  "version": "0.0.1",
  "entry": "payload.bin",
  "icon": "icon.png"
}
```

Do not freeze this format until storage and payload loading are proven.

## Long-term nostalgic UX

Desired eventual experience:

```text
Album / convenient title entry
            ↓
           HBL²
            ↓
      homebrew app grid
```

This is intentionally separated from the first technical milestones. A polished entry route is useless until the launcher runtime itself works.
