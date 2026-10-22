# HBL² Ecosystem Watch

Last updated: **2026-10-23**

This file tracks useful third-party work around ns2jb and Switch 2 homebrew.

Status meanings:
- **USEFUL NOW** — concrete code/behavior we can learn from immediately.
- **REFERENCE** — useful mirror/rework/reference, but not a new primitive by itself.
- **WATCH** — interesting but currently too incomplete to rely on.

---

## mhzsajan/ns2jb

Repository:

https://github.com/mhzsajan/ns2jb

**Status:** REFERENCE

Description:

> Switch 2 FS jailbreak (ns2jb) - captured and reworked

The current README matches the published ns2jb operating flow very closely:
- SmileBASIC 4.4.9
- system software 23.0.1
- Node.js 22+
- Linux/macOS host
- port 39380
- same bootstrap / REMOVE / START flow
- same timing-sensitive FS verification model

Usefulness for HBL²:

- convenient GitHub-visible mirror/rework for code browsing;
- compare packaging and file layout against pepsipu's GitLab upstream;
- useful diff target if the author begins making independent changes.

Do **not** treat it as authoritative over pepsipu/ns2jb without checking the actual diff and provenance.

Primary upstream remains:

https://gitlab.com/pepsipu/ns2jb

---

## Ludi-1225/switch2-ns2jb

Repository:

https://github.com/Ludi-1225/switch2-ns2jb

**Status:** WATCH

Repository description:

> ns2jb — what it means for a console on 22.5.0

At the time checked, GitHub reports the repository size as **0** and no README/file content could be fetched.

Usefulness for HBL²:

- track whether meaningful 22.5.0 analysis appears;
- do not infer 22.5.0 exploit compatibility from the repository title alone.

Until content exists, this is only a watch item.

---

## cpypwn/mac2jb

Repository:

https://github.com/cpypwn/mac2jb

**Status:** USEFUL NOW — workflow research

This project turns an Apple Silicon Mac into a USB HID keyboard and automatically types the ns2jb SmileBASIC bootstrap.

It is **not** directly useful as our Windows/Linux host implementation, but its hardware testing solved several important practical problems that are highly relevant to any future automated bootstrap sender.

### Lessons worth reusing

The project documents real hardware behavior for:

- USB HID enumeration;
- key press + release handling;
- stuck-key failure after disconnect;
- SmileBASIC's observed inverted Shift behavior for letter case;
- transfer pacing;
- editor indentation inheritance;
- full bootstrap transfer;
- staged post-bootstrap command sending.

Most important editor finding:

SmileBASIC carries the previous line's leading indentation forward after Enter. A robust sender should track the inherited indentation and send only the difference (spaces or Backspaces), rather than blindly typing every source-space again.

### HBL² opportunity

We may be able to build a similar bootstrap sender using an **ESP board with native USB HID/device capability**, avoiding manual entry of thousands of characters.

Potential architecture:

```text
PC / phone
   ↓
ESP HID sender
   ↓ USB keyboard
Switch 2 / SmileBASIC
   ↓
ns2jb bootstrap
```

This would be independent of macOS-specific gadget drivers.

Before implementation, verify the exact ESP board and whether it can act as a native USB HID device.

### What not to copy blindly

mac2jb depends on:
- Apple Silicon hardware;
- macOS-specific USB device-controller behavior;
- an experimental kernel extension;
- Mac-specific controller selection.

We only care about the **input protocol / typing lessons**, not the Mac implementation.

---

## Ecosystem rule

For every newly discovered project, record:

- repository/source;
- author;
- exact purpose;
- whether it introduces a **new primitive** or only automates an existing one;
- tested firmware/app version;
- whether it has real hardware evidence;
- whether HBL² should adopt code, copy an idea, or merely watch it.

This prevents the repository from becoming a pile of links with no technical value.
