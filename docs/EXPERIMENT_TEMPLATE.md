# HBL² Experiment Template

Copy this file for every meaningful hardware experiment.

Suggested filename:

```text
experiments/YYYY-MM-DD-short-name.md
```

---

# Experiment: <name>

## Status

- [ ] planned
- [ ] running
- [ ] success
- [ ] failed
- [ ] inconclusive

Evidence class:

- [ ] VERIFIED BY US
- [ ] VERIFIED UPSTREAM
- [ ] COMMUNITY REPORT
- [ ] HYPOTHESIS

## Goal

One sentence. What exact question does this experiment answer?

## Baseline

Console:
- hardware:
- system software:
- region:

Entry application:
- title:
- version:

Host:
- OS:
- kernel:
- Node:
- network mode:
- host IP used:

Upstream:
- repository:
- commit:

HBL²:
- branch:
- commit:

## Preconditions

- fresh console boot:
- app freshly launched:
- network reachable:
- previous experiment state cleared:

## Change under test

Describe **one** change only.

Files changed:

```text
<paths>
```

## Commands

```bash
<exact commands>
```

## Expected result

What should happen if the hypothesis is correct?

## Observed result

What actually happened?

Include exact:
- host output;
- Switch error;
- return values;
- crash stage;
- visible behavior.

## Artifacts

Local-only paths are okay. Do not commit secrets/dumps.

- run directory:
- log:
- screenshot/video:
- hashes:

## Result

### What this proves

-

### What this does **not** prove

-

## Next experiment

One smallest useful follow-up.
