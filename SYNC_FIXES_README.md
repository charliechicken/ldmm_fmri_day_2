# Why Day-2 Fixes Don't Apply — and How to Fix It

## The Problem

**PsychoPy Builder stores code INSIDE the .psyexp file** — not in the `experiment/` folder. When you run the experiment:

1. Builder reads code from the .psyexp
2. Builder generates `DecisionLab_lastrun.py` from that embedded code
3. The experiment runs from `DecisionLab_lastrun.py`

**The `day2/experiment/` folder** (e.g. `5decisionMakingEndRoutine.py`, `7decisionITI3BeginRoutine.py`, `1trialBeginRoutine.py`) is a separate copy. Edits there are **never used** when you run from Builder.

## Why Day-1 Works But Day-2 Doesn’t

Day-1 was likely fixed either by:
- Updating the .psyexp directly in Builder, or
- Using a different workflow (e.g. running from a script that loads from files)

Day-2’s .psyexp still has the old embedded code, so the same bugs appear even though the experiment folder files are correct.

## How to Apply the Fixes

Run the sync script **before** running the experiment:

```powershell
cd c:\Users\cn\Desktop\ldmm_fmri-main\day2
python sync_experiment_fixes.py
```

Then run the experiment **from the command line** (so the patched lastrun is used):

```powershell
python DecisionLab_lastrun.py
```

**Important:** If you run from PsychoPy Builder, it will overwrite `DecisionLab_lastrun.py` with the old code. Always run the sync script first, then run via `python DecisionLab_lastrun.py`.

## Quick 3+3 Test (Learning + Decision, With Timeout)

To verify fixes: 3 learning trials, 3 decision trials, skip one response for timeout:

1. Run sync: `python sync_experiment_fixes.py`
2. In `DecisionLab_lastrun.py`, change:
   - `decisionLoop` → `nReps=3.0`
   - `learningLoop` → `nReps=3.0` (or 6 for 3 per block)
3. Run: `python DecisionLab_lastrun.py` (or from PsychoPy)
4. For one decision trial, don’t press 1 or 3 within 2 s → you should see the timeout screen and ITI3 ≈ 1.5 s
5. Check output CSVs for `iti3_base`, varying `iti3_duration`, and non‑zero `fruit_onset_time_s` on trial 2+

## Alternative: Update PsychoPy Builder by Hand

In PsychoPy Builder, manually replace the code in these components:

1. **decisionMaking** routine → End Routine code  
   Replace the ITI3 block with the contents of `experiment/4decisionLoopBlock3/5decisionMakingEndRoutine.py`.

2. **decisionITI3** routine → Begin Routine code  
   Replace with the contents of `experiment/4decisionLoopBlock3/7decisionITI3BeginRoutine.py`.

3. **trial** routine → Begin Routine code  
   Replace the scanner_clock / fruit_onset block with the contents from `experiment/8block1and2learningLoop/1trialBeginRoutine.py` (the relevant section).

Then save the .psyexp. Future runs from Builder will use the updated code.
