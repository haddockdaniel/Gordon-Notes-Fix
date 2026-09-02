# Synthetic Voice/NLU Coverage Implementation Plan

Implementation Program ID: `smartspeak-pm-e2e-2026-09-02-v1`

## Authority and execution

This disposable plan exists only to test the SmartSpeak PM automation architecture. Modules execute numerically and serially. Implementation work is one PR at a time. A final-state closure audit is required after the last implementation PR in each module.

## Module 1 — Confirmed dispatch expansion

### Objective
Add deterministic `create invoice` dispatch while preserving existing `show balance` and unknown-command behavior.

### Required outcomes
- `create invoice` resolves to `invoice_create`.
- Existing `show balance` behavior does not regress.
- Unknown commands remain unknown.
- Focused/full repository tests pass.

### Closure criteria
Repository behavior and tests prove every Module 1 outcome on merged `main`; closure audit returns GO.

## Module 2 — Normalization regression guard

### Objective
Preserve normalization invariants across whitespace and casing.

### Required outcomes
- Leading/trailing whitespace is ignored.
- Repeated internal whitespace is collapsed.
- Matching remains case-insensitive.
- Existing dispatch behavior remains unchanged.

### Closure criteria
Repository behavior and tests prove every Module 2 outcome on merged `main`; closure audit returns GO.
