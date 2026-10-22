# HBL² Agent Rules

These rules apply to Codex, local LLM agents, and other coding assistants working in this repository.

## Mission

HBL² is a Switch 2 homebrew-launcher and reverse-engineering research project.

The current goal is **not** to build a complete CFW. Work in small, reproducible steps:

1. reproduce upstream ns2jb unchanged;
2. execute a minimal custom payload;
3. understand available services / process capabilities;
4. establish graphics and storage primitives;
5. build a launcher;
6. investigate a convenient launcher entry flow only after the lower layers are understood.

## Upstream separation

- Treat `pepsipu/ns2jb` as a separate upstream project.
- Do not copy the whole ns2jb repository into HBL².
- Do not silently modify the user's ns2jb clone.
- Record the exact upstream commit used for an experiment.
- Prefer adapters, notes, tiny payloads, and reproducible patches over forks unless a fork becomes necessary.

## Evidence discipline

Every technical claim must be classified as one of:

- **VERIFIED BY US**
- **VERIFIED UPSTREAM**
- **COMMUNITY REPORT**
- **HYPOTHESIS**

Never upgrade a claim to **VERIFIED BY US** without an actual hardware result.

Record:
- firmware version;
- application version;
- exact commit / hash;
- command used;
- expected result;
- observed result;
- logs / error text;
- whether a fresh reboot was required.

## Safety for the research device

- Prefer read-only observation before writes.
- Make one behavioral change per experiment.
- Preserve rollback / reboot paths.
- Do not add persistence unless the user explicitly makes it a research target.
- Do not widen an exploit primitive merely because it is available; prove the smallest useful primitive first.
- Keep payloads small and deterministic during bring-up.

## Repository hygiene

Never commit:
- commercial ROMs or game dumps;
- Nintendo firmware images;
- prod.keys / title.keys or other decryption keys;
- tickets / certificates;
- console-unique secrets;
- credentials;
- private crash dumps containing secrets;
- copyrighted game assets unless clearly redistributable.

Generated binaries may be committed later when they are HBL²-owned and reproducible, but source + build instructions are preferred.

## Coding style for early research

- Favor simple code over abstraction.
- Avoid giant refactors while bring-up is unstable.
- Add assertions and explicit error codes.
- Log exact failure stages.
- Keep hardware-dependent constants documented.
- Do not hide magic values: name them and cite their origin in comments/docs.
- When a change fails on hardware, preserve the failed result in the experiment log before trying the next idea.

## Source priority

Prefer:
1. original author / repository;
2. technical write-up;
3. code;
4. reproducible hardware evidence;
5. community mirror / discussion;
6. speculation.

Reddit/X are useful discovery feeds, not automatic proof.

## Definition of first success

The first HBL² success is intentionally small:

> A custom HBL² payload executes through the reproduced ns2jb path and produces a deterministic observable result on the user's Switch 2.

Do not skip directly to a launcher UI before this is reproducible.
