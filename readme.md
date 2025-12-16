# PsychoPy Learning and Decision-Making Experiment

A PsychoPy experiment for fMRI studies involving learning trials and decision-making tasks with scanner synchronization.

## Quick Start

### Prerequisites
- PsychoPy (version 2020.1 or later)
- Python 3.x

### Setup

1. **Create data directory:**
   ```bash
   mkdir -p data/sub-1
   ```

2. **Configure PsychoPy Builder:**
   - Open experiment in PsychoPy Builder
   - Go to **Experiment Settings > Basic > Experiment info**
   - Add fields:
     - `participant`: `ignore`
     - `session`: Session number (e.g., `1`, `009`)
     - `day`: Day number (`1` or `2`)

3. **Required images** (place in `images/` directory):
   - Learning: `apple.png`, `banana.png`, `strawberry.png`, `kiwi.png`, `pear.png`, `grapes.png`
   - Practice: `ten.png`, `thirty.png`, `fifty.png`
   - Other: `blank.png` and unrelated images for scanner wait screens

4. **Run the experiment** in PsychoPy Builder

## Experiment Structure

### Block 1: Learning (Rewards)
- 3 practice trials
- Scanner sync → Learning trials (default: 60)
- Slider-based prediction task

### Block 2: Learning (Punishments)
- Block transition screen
- Scanner sync → Learning trials (default: 60)
- Same prediction task

### Block 3: Decision-Making
- 3 practice decision trials
- Scanner sync → Decision trials
- Two-alternative forced choice (2s response window)

## Scanner Synchronization

Each block includes a setup sequence:

1. **"Task will start soon"** → Press `2`
2. **Scanner sync** → Wait for scanner trigger `5`
3. **Crosshair** (2s) → **Wait image** (2s) → **Crosshair** (2s)
4. Trials begin

**Note:** Scanner sync routines only appear once per block during the transition period.

## Data Output

### Directory Structure
```
data/
└── sub-1/                          # All data saved here (regardless of session)
    ├── sub-001_day-1_block-1_learning_1_rewards.csv
    ├── sub-001_day-1_block-2_learning_2_punishments.csv
    └── sub-001_day-1_block-3_decisions_3_implicit.csv
```

### File Naming
- **Folder**: `sub-1` (no zero-padding)
- **Files**: `sub-001_day-1_block-X_*.csv` (zero-padded session number)

### User ID
- Generated deterministically from session number
- Same session number → Same user ID (consistent across days)
- Formula: `1000000 + (session_number * 7919) % 8000000`

### CSV Columns

**Learning Trials:**
- `user_id`, `trial_number`, `block_id`, `block_name`
- `stimulus_identity`, `stimulus_average_points`, `actual_points`
- `prediction_value`, `reaction_time_ms`
- `responded_in_time`, `trial_timed_out`, `keypress_sequence`

**Decision Trials:**
- `user_id`, `trial_number`, `block_id`, `block_name`
- `first_stimulus_id`, `first_stimulus_side`
- `left_stimulus_id`, `right_stimulus_id`
- `left_avg_points`, `right_avg_points`
- `choice`, `reaction_time_ms`

## Key Features

### Learning Trials
- **Slider range**: -100 to +100
- **Random starting position** on each trial
- **Controls**: `1` = decrease, `2` = continue, `3` = increase (or mouse)
- **Timeout**: 8 seconds
- **Feedback**: Shows actual points received

### Decision Trials
- **Timing**: First stimulus (2s) → Crosshair (1s) → Second stimulus (2s) → Crosshair (1s) → Both (2s) → Crosshair (1s)
- **Response window**: 2 seconds
- **Controls**: `1` = left, `3` = right (or mouse click)
- **Timeout**: Shows "Time out" screen if no response

## Configuration

### Trial Numbers
Modify in PsychoPy Builder loop settings:
- **Block 1 & 2**: Set learning loop `nReps` (default: 60 per block)
- **Block 3**: Set decision loop `nReps`

### Timing Parameters
Key timings (modify in code if needed):
- Learning trial timeout: 8.0s
- Decision trial timeout: 2.0s
- Actual points display: 2.0s
- Crosshair durations: 2.0s
- Scanner wait image: 2.0s

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Scanner sync appears after trials | Check `block2_setup_complete` flag is set correctly |
| Data not saving | Ensure `data/sub-1/` directory exists |
| Practice trials not showing | Check `practice_decision_block` initialization in console |

## File Structure

```
psychopyStuffs/
├── README.md
├── data_logging.py              # Data logging module
├── images/                      # Image files
├── data/                        # Output directory
│   └── sub-1/                   # Participant data
├── startTask/                   # Experiment initialization
├── trial/                       # Learning trials
├── decisionMaking/              # Decision trials
├── scannerSync*/                # Scanner sync routines
├── taskStartSoon*/              # Task start routines
└── ... (other routine folders)
```

## Notes

- All data saved to `data/sub-1/` regardless of session number
- Session number appears in filenames (zero-padded: `sub-001`)
- User ID consistent across days for same session number
- Scanner sync only shows once per block during transition
