# HBL² Research Risk Notes

Last updated: **2026-10-23**

This document exists because "userland" does **not** mean "cannot brick the console."

## Current safe baseline

The published ns2jb demo is tethered and intentionally non-persistent.

Its documented behavior is:

```text
exploit runs
    ↓
temporary process/sysmodule modification
    ↓
reboot
    ↓
original system state restored
```

That is the baseline HBL² should preserve during early research.

## Why persistence is a different risk class

The current public chain reaches powerful userland contexts, including the filesystem sysmodule.

A process does not need kernel privilege to cause a serious boot failure if it already has authority to modify data that the normal boot/system software depends on.

Therefore these are **high-risk research areas**:

- early-boot system savedata;
- persistent service/configuration state;
- critical filesystem metadata;
- system titles / executable content;
- boot-relevant databases;
- any write whose recovery path has not been demonstrated.

## HBL² policy for now

Until a reliable recovery route is independently demonstrated:

- **NO persistence experiments on the primary console**
- **NO writes to boot-critical/system-critical state**
- keep custom work volatile where possible;
- prefer read-only inspection;
- write only HBL²-owned test data in known noncritical locations;
- reboot between materially different exploit experiments;
- preserve logs from failures;
- never assume "it is only userland" means a write is recoverable.

## Brick reports

There are historical Switch 2 brick/bootloop reports from unrelated 2025 hacking attempts.

As of this note, HBL² has **not independently verified** the current claim that a console was bricked specifically while experimenting with ns2jb persistence.

Do not merge old reports and new claims into one fact.

If a current case becomes verifiable, record:

- exact experiment;
- firmware;
- code/commit;
- modified storage/state;
- symptoms;
- recovery attempts;
- whether the failure was permanent or recoverable.

## Persistence status

Current public discussion indicates that an untethered/persistent route may theoretically involve manipulating early system savedata and dealing with boot-time heap layout.

That is precisely why HBL² treats persistence as a separate, later research track rather than an extension of ordinary launcher work.

For our current goals, **tethered + repeatable + recoverable beats persistent**.
