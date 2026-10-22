# HBL² Lab Setup

This document describes the reproducible baseline for HBL² experiments.

## Known upstream target

Upstream ns2jb currently documents:

- Nintendo Switch 2 system software **23.0.1**
- SmileBASIC **4.4.9**
- Node.js **22+**
- host OS: **macOS or Linux**
- computer and console on the same reachable network
- TCP port **39380**
- more than **20 MiB** free in the SmileBASIC save
- no npm install or compiler required for the distributed demo

Primary upstream sources:

- https://pepsipu.com/blog/2026-10-switch2-jailbreak-ns2jb/
- https://gitlab.com/pepsipu/ns2jb

## Our initial hardware/software baseline

- Switch 2: system software 23.0.1
- SmileBASIC: 4.4.9
- Windows PC with WSL2 Ubuntu planned as Linux host
- Node.js 22+ must be installed **inside the Linux environment**
- separate local clone of ns2jb
- separate local clone of HBL²

Suggested local layout:

```text
E:\VS\repos\
├── ns2jb\
└── HBL-HOCH2\
```

Inside WSL the Windows drive is normally visible under `/mnt/e/`.

## Important WSL networking note

ns2jb requires the Switch to reach the host over the LAN.

WSL2 networking can differ from native Linux. Do **not** assume that a service listening inside WSL is automatically reachable from the Switch.

Before exploit testing:

1. verify the Linux host IP / networking mode;
2. confirm the intended host address is reachable from the LAN;
3. allow TCP 39380 through the relevant firewall path;
4. if WSL networking becomes the blocker, use native Linux rather than changing exploit code.

Networking problems and exploit failures must not be mixed into one debugging problem.

## One-time SmileBASIC preparation

Follow the exact upstream README in the ns2jb clone.

Current upstream flow says to enter `bootstrap.bas` in SmileBASIC's **Make a Program**, slot 0, then save it as:

```text
NS2
```

A USB keyboard is strongly recommended.

The distributed ZIP/repository is a computer-side package, not a SmileBASIC import package.

## Baseline run procedure

Start from a fresh console boot.

On the Linux host, from the **unmodified upstream ns2jb directory**:

```bash
node run.cjs
```

If required, pass the LAN-reachable host address printed/selected by the setup.

On the Switch in SmileBASIC Direct mode, upstream currently instructs:

```text
LOAD "TXT:NS2"
RUN
REMOVE NSR,&H60000000,&H3FFFFFFF
```

The reported out-of-memory result from `REMOVE` is expected by upstream.

Then enter the exact `V=START(...)` line printed by the host.

### Critical upstream notes

- Enter the `REMOVE` command only once per application process.
- Keep SmileBASIC open and the host awake until FS execution is verified.
- The exploit is timing-sensitive.
- If a run fails, preserve the generated `runs/` directory, reboot the Switch, and retry from a fresh process.
- Rebooting restores the original system state.

## HBL² rule: reproduce before modifying

Before any custom HBL² payload:

- [ ] upstream ns2jb runs unchanged;
- [ ] successful run log preserved locally;
- [ ] exact upstream Git commit recorded;
- [ ] exact Switch firmware recorded;
- [ ] exact SmileBASIC version recorded;
- [ ] Node version recorded;
- [ ] Linux distribution / kernel recorded;
- [ ] host network mode recorded.

Only then begin M1 custom-payload work.

## Useful host commands

Record these in each first-success report:

```bash
node --version
git -C /path/to/ns2jb rev-parse HEAD
uname -a
cat /etc/os-release
ip addr
```

For WSL:

```powershell
wsl --version
wsl --status
wsl -l -v
```

## What *not* to change during baseline testing

Do not simultaneously change:

- ns2jb exploit code;
- network topology;
- SmileBASIC bootstrap;
- console firmware;
- payload behavior.

If baseline fails, first determine whether the failure is host setup, network reachability, SmileBASIC state, or exploit timing.
