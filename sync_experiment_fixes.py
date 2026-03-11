#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Sync fixes from experiment/ folder into DecisionLab_lastrun.py.

PsychoPy Builder stores code in the .psyexp and generates lastrun from it.
The experiment/ folder has the corrected code but is NOT used by Builder.
This script patches lastrun so you get the fixes when running:
    python DecisionLab_lastrun.py

Run this script AFTER Builder has generated lastrun, and run via command line
(not Builder's Run button) to use the patched version.
"""
from __future__ import print_function
import os
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LASTRUN = os.path.join(SCRIPT_DIR, 'DecisionLab_lastrun.py')
EXP_DIR = os.path.join(SCRIPT_DIR, 'experiment')

# --- Patch 1: ITI3 calculation in decisionMaking End Routine ---
OLD_ITI3_BLOCK = r'''        # Calculate ITI 3 duration \(crosshair after decision\)
        # Requirement:
        # - ITI_3 should be 2/3/4 seconds on normal trials \(do NOT subtract RT\)
        # - On timed-out trials, show timeout screen for 1\.5s, then crosshair for \(2/3/4 - 1\.5\)s
        import random
        timeout_screen_duration = globals\(\)\.get\('TIMEOUT_SCREEN_DURATION', 1\.5\)
        iti3_total_values = globals\(\)\.get\('DECISION_ITI3_VALUES', \[2, 3, 4\]\)
        iti3_total = random\.choice\(iti3_total_values\)
        
        if decision_timed_out:
            iti3_duration = max\(0\.0, iti3_total - timeout_screen_duration\)
            print\(f"ITI 3 \(timeout\): total=\{iti3_total\}s, timeout_screen=\{timeout_screen_duration\}s, crosshair=\{iti3_duration:.2f\}s"\)
        else:
            iti3_duration = float\(iti3_total\)
            print\(f"ITI 3 \(normal\): crosshair=\{iti3_duration:.2f\}s \(no RT subtraction\)"\)
        
        globals\(\)\['iti3_duration'\] = iti3_duration'''

NEW_ITI3_BLOCK = '''        # Calculate ITI 3 duration (crosshair after decision)
        # Per stimulus diagram (same as day 1):
        # - Response < 2s: crosshair = (2 - RT) + ITI_base  [remaining response window + base ITI 2/3/4]
        # - No response: Time out screen, then crosshair = ITI_base - timeout_screen
        import random
        timeout_screen_duration = globals().get('TIMEOUT_SCREEN_DURATION', 1.5)
        decision_response_limit = globals().get('DECISION_TIMEOUT_DURATION', 2.0)
        iti3_total_values = globals().get('DECISION_ITI3_VALUES', [2, 3, 4])
        iti3_total = random.choice(iti3_total_values)
        iti3_base = iti3_total  # Base ITI (2/3/4 s) chosen for this trial

        if decision_timed_out:
            iti3_duration = max(0.0, float(iti3_total) - timeout_screen_duration)
            iti3_remaining_response = 0.0
            print(f"ITI 3 (timeout): crosshair={iti3_duration:.2f}s (ITI_base={iti3_base}s - timeout={timeout_screen_duration}s)")
        else:
            # Crosshair = (2 - RT) + ITI_base  [fill remaining 2s window + base]
            iti3_remaining_response = max(0.0, decision_response_limit - decision_rt_value)
            iti3_duration = iti3_remaining_response + iti3_total
            print(f"ITI 3 (responded): RT={decision_rt_value:.3f}s, (2-RT)={iti3_remaining_response:.3f}s + ITI_base={iti3_base}s = crosshair={iti3_duration:.3f}s")

        globals()['iti3_duration'] = iti3_duration'''

# Add iti3_base to addData and log_decision_trial
OLD_ADD_DATA = "        thisExp.addData(\"iti3_duration\", iti3_duration)\n        thisExp.addData(\"decision_response_time\", decision_rt_value)"
NEW_ADD_DATA = "        thisExp.addData(\"iti3_duration\", iti3_duration)\n        thisExp.addData(\"iti3_base\", iti3_base)\n        thisExp.addData(\"decision_response_time\", decision_rt_value)"

OLD_LOG_CALL = "                    iti2_duration=iti2_duration,\n                    iti3_duration=iti3_duration,"
NEW_LOG_CALL = "                    iti2_duration=iti2_duration,\n                    iti3_base=iti3_base,\n                    iti3_duration=iti3_duration,"

# --- Patch 2: ITI3 Begin Routine - read from globals ---
OLD_ITI3_BEGIN = '''        # ITI 3 - Crosshair screen (duration: (2 - response_time) + rand(1,2,3))
        # Component: text_17 (crosshair)
        # Duration is calculated in decisionMakingEndRoutine as iti3_duration
        
        # Make sure iti3_duration exists (should be set in decisionMakingEndRoutine)
        # If for some reason it doesn't exist, use a default
        if 'iti3_duration' not in locals() and 'iti3_duration' not in globals():
            import random
            iti3_duration = random.choice([1, 2, 3]) + 1.0  # Default fallback
            print("WARNING: iti3_duration not found, using default")
        
        # Ensure it's available in globals for Builder
        if 'iti3_duration' in locals():
            globals()['iti3_duration'] = iti3_duration'''

NEW_ITI3_BEGIN = '''        # ITI 3 - Crosshair screen (duration: (2-RT)+ITI when responded, full ITI when timed out)
        # Duration is set in decisionMaking End Routine as iti3_duration
        # NOTE: iti3_duration is in globals() - must read explicitly so Builder's $iti3_duration uses correct value each trial
        iti3_duration = globals().get('iti3_duration', 2.0)
        decision_timed_out = globals().get('decision_timed_out', False)'''

OLD_ITI3_PRINT = '        print(f"Showing ITI 3 crosshair (duration: {iti3_duration if \'iti3_duration\' in locals() or \'iti3_duration\' in globals() else \'unknown\'}s)")'
NEW_ITI3_PRINT = '        print(f"ITI3 Begin: showing crosshair for iti3_duration={iti3_duration:.3f}s (timed_out={decision_timed_out})")'

# --- Patch 3: Learning trial fruit_onset - prefer globals for scanner_clock ---
OLD_SCANNER = "scanner_clock = getattr(thisExp, 'scanner_clock', None) or globals().get('scanner_clock', None)"
NEW_SCANNER = "scanner_clock = globals().get('scanner_clock', None) or getattr(thisExp, 'scanner_clock', None)"


def main():
    if not os.path.isfile(LASTRUN):
        print("ERROR: DecisionLab_lastrun.py not found. Run the experiment from Builder first to generate it.")
        return 1

    with open(LASTRUN, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    n = 0

    # Patch 1a: ITI3 calculation block (use simple string replace - more reliable than regex for multiline)
    old1 = """        # Calculate ITI 3 duration (crosshair after decision)
        # Requirement:
        # - ITI_3 should be 2/3/4 seconds on normal trials (do NOT subtract RT)
        # - On timed-out trials, show timeout screen for 1.5s, then crosshair for (2/3/4 - 1.5)s
        import random
        timeout_screen_duration = globals().get('TIMEOUT_SCREEN_DURATION', 1.5)
        iti3_total_values = globals().get('DECISION_ITI3_VALUES', [2, 3, 4])
        iti3_total = random.choice(iti3_total_values)
        
        if decision_timed_out:
            iti3_duration = max(0.0, iti3_total - timeout_screen_duration)
            print(f"ITI 3 (timeout): total={iti3_total}s, timeout_screen={timeout_screen_duration}s, crosshair={iti3_duration:.2f}s")
        else:
            iti3_duration = float(iti3_total)
            print(f"ITI 3 (normal): crosshair={iti3_duration:.2f}s (no RT subtraction)")
        
        globals()['iti3_duration'] = iti3_duration"""
    if old1 in content:
        content = content.replace(old1, NEW_ITI3_BLOCK)
        n += 1
    else:
        print("WARNING: ITI3 calculation block not found (maybe already patched or structure changed)")

    # Patch 1b: add iti3_base to addData
    if OLD_ADD_DATA in content:
        content = content.replace(OLD_ADD_DATA, NEW_ADD_DATA)
        n += 1

    # Patch 1c: add iti3_base to log_decision_trial
    if OLD_LOG_CALL in content and 'iti3_base=iti3_base' not in content:
        content = content.replace(OLD_LOG_CALL, NEW_LOG_CALL)
        n += 1

    # Patch 2a: ITI3 Begin Routine
    if OLD_ITI3_BEGIN in content:
        content = content.replace(OLD_ITI3_BEGIN, NEW_ITI3_BEGIN)
        n += 1

    # Patch 2b: ITI3 print
    if OLD_ITI3_PRINT in content:
        content = content.replace(OLD_ITI3_PRINT, NEW_ITI3_PRINT)
        n += 1

    # Patch 3: scanner_clock preference
    if OLD_SCANNER in content:
        content = content.replace(OLD_SCANNER, NEW_SCANNER)
        n += 1

    if content == original:
        print("No patches applied. Either already patched or lastrun structure differs.")
        return 0

    with open(LASTRUN, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Applied {n} patch(es) to DecisionLab_lastrun.py")
    print("Run with: python DecisionLab_lastrun.py")
    return 0


if __name__ == '__main__':
    exit(main())
