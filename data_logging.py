"""
Data Logging Module for PsychoPy Experiment
Handles CSV logging for Learning and Decision Making phases
"""

import csv
import time
from datetime import datetime

# Avoid os import for PsychoPy compatibility (doesn't work online/Pavlovia)
def _join_path(*parts):
    """Join path parts using '/' separator (works on both Windows and Unix)"""
    return '/'.join(str(p).strip('/') for p in parts if p)

def _basename(path):
    """Get basename from path without os.path"""
    if not path:
        return ""
    # Handle both '/' and '\' separators
    path = str(path).replace('\\', '/')
    return path.split('/')[-1]

def _create_directory_if_needed(dir_path):
    """Placeholder - directory creation is handled manually by user"""
    # Directory should be created manually before running experiment
    # This function is kept for compatibility but does nothing
    return True

class DataLogger:
    def __init__(self, session_number=1, day=1, experiment_dir="data"):
        """
        Initialize data logger
        
        Args:
            session_number: Session number (participant serial number, e.g., 9 for participant #9)
            day: Day number (1 or 2)
            experiment_dir: Base directory for data files (default: "data")
        """
        self.session_number = session_number
        self.day = day
        self.experiment_dir = experiment_dir
        
        # Always save to sub-1 folder regardless of session number
        # Folder name: sub-1 (fixed, no zero-padding)
        self.subject_dir = _join_path(experiment_dir, "sub-1")
        # Note: Directory should be created manually before running experiment
        
        # Generate consistent user_id based on session_number
        # This ensures the same session number always gets the same user_id across days
        # Using a deterministic hash-like approach: session_number -> consistent user_id
        # Formula: 1000000 + (session_number * 7919) % 8000000
        # This ensures same session number = same user_id (regardless of day)
        # The user_id is the same for both day 1 and day 2 for the same session number
        self.user_id = 1000000 + (session_number * 7919) % 8000000
        
        # Track current block number
        self.current_block = 0
        
        # Learning phase data storage
        self.learning_data = []
        self.learning_keypresses = []  # Store keypresses with timestamps
        
        # Decision making phase data storage
        self.decision_data = []
        
        # Track trial start time for reaction time calculations
        self.trial_start_time = None
        self.decision_start_time = None
        
        print(f"Data Logger initialized: session_number={session_number}, day={day}")
        print(f"  Folder: sub-1/ (always sub-1, regardless of session number)")
        print(f"  User ID: {self.user_id} (consistent across days for session {session_number})")
    
    def start_trial(self, trial_start_time):
        """Record trial start time"""
        self.trial_start_time = trial_start_time
        self.learning_keypresses = []  # Reset keypress log for this trial
    
    def log_keypress(self, key, timestamp):
        """Log a keypress during learning trial"""
        if self.trial_start_time:
            rt_ms = int((timestamp - self.trial_start_time) * 1000)  # Convert to milliseconds
            direction = "left" if (key == '1' or key == 'num_1') else "right" if (key == '3' or key == 'num_3') else "unknown"
            self.learning_keypresses.append({
                "key": key,
                "direction": direction,
                "reaction_time_ms": rt_ms,
                "timestamp": timestamp
            })
    
    def log_learning_trial(self, trial_num, block_id, block_name, stimulus_identity,
                          stimulus_avg_points, actual_points, prediction_value,
                          reaction_time_ms, responded_in_time, trial_timed_out,
                          slider_starting_value=None,
                          crosshair1_duration=None, crosshair2_duration=None,
                          crosshair1_rand=None, crosshair2_rand=None,
                          timeout_duration=None, actual_points_duration=None,
                          fruit_onset_time=None, first_response_time=None, submit_time=None):
        """
        Log a learning trial

        Args:
            trial_num: Trial number within block (1-30)
            block_id: Block ID (1=Rewards, 2=Punishments)
            block_name: Block name ("gain" or "loss")
            stimulus_identity: Fruit name (e.g., "apple")
            stimulus_avg_points: Average points for this stimulus (baseline)
            actual_points: Actual points in this trial
            prediction_value: User's prediction (slider value)
            reaction_time_ms: Reaction time in milliseconds
            responded_in_time: Whether user responded before timeout
            trial_timed_out: Whether trial timed out
            slider_starting_value: Random starting value of slider for this trial
            fruit_onset_time: Time (s) from scanner sync to fruit image appearing
            first_response_time: Time (s) from scanner sync to first key 1 or 3 press
            submit_time: Time (s) from scanner sync to key 2 (submit) press
        """
        trial_data = {
            "user_id": self.user_id,
            "trial_number": trial_num,
            "block_id": block_id,
            "block_name": block_name,
            "stimulus_identity": stimulus_identity,
            "stimulus_average_points": stimulus_avg_points,
            "actual_points": actual_points,
            "prediction_value": prediction_value,
            "reaction_time_ms": reaction_time_ms,
            "responded_in_time": responded_in_time,
            "trial_timed_out": trial_timed_out,
            "slider_starting_value": slider_starting_value,
            # Timing (so you can reconstruct exact on-screen timing)
            "crosshair1_rand": crosshair1_rand,
            "crosshair1_duration": crosshair1_duration,
            "actual_points_duration": actual_points_duration,
            "crosshair2_rand": crosshair2_rand,
            "crosshair2_duration": crosshair2_duration,
            "timeout_duration": timeout_duration,
            "keypresses": self.learning_keypresses.copy(),  # Copy keypress log
            # Scanner-relative timestamps
            "fruit_onset_time": fruit_onset_time,
            "first_response_time": first_response_time,
            "submit_time": submit_time,
        }
        self.learning_data.append(trial_data)
    
    def start_decision(self, decision_start_time):
        """Record decision start time"""
        self.decision_start_time = decision_start_time
    
    def log_decision_trial(self, trial_num, block_id, block_name, first_stimulus_id,
                          first_stimulus_side, left_stimulus_id, right_stimulus_id,
                          left_stimulus_num, right_stimulus_num, left_avg_points,
                          right_avg_points, choice, reaction_time_ms,
                          iti1_duration=None, iti2_duration=None, iti3_duration=None,
                          decision_timed_out=None, decision_response_limit_s=None,
                          decision_timeout_screen_duration_s=None,
                          stimulus1_onset_time=None, stimulus2_onset_time=None,
                          both_fruits_onset_time=None, choice_time=None):
        """
        Log a decision making trial

        Args:
            trial_num: Trial number
            block_id: Block ID (1=before showing points, 2=after showing points)
            block_name: Block name ("implicit" or "explicit")
            first_stimulus_id: Fruit shown first (e.g., "apple")
            first_stimulus_side: Side where first fruit appeared ("left" or "right")
            left_stimulus_id: Left fruit name (e.g., "apple")
            right_stimulus_id: Right fruit name (e.g., "banana")
            left_stimulus_num: Left fruit numerical ID (1-6)
            right_stimulus_num: Right fruit numerical ID (1-6)
            left_avg_points: Left fruit average points
            right_avg_points: Right fruit average points
            choice: User's choice ("left" or "right")
            reaction_time_ms: Reaction time in milliseconds
        """
        decision_data = {
            "user_id": self.user_id,
            "trial_number": trial_num,
            "block_id": block_id,
            "block_name": block_name,
            "first_stimulus_id": first_stimulus_id,
            "first_stimulus_side": first_stimulus_side,
            "left_stimulus_id": left_stimulus_id,
            "right_stimulus_id": right_stimulus_id,
            "left_stimulus_num": left_stimulus_num,
            "right_stimulus_num": right_stimulus_num,
            "left_avg_points": left_avg_points,
            "right_avg_points": right_avg_points,
            "choice": choice,
            "reaction_time_ms": reaction_time_ms,
            # Timing (so you can reconstruct exact on-screen timing)
            "iti1_duration": iti1_duration,
            "iti2_duration": iti2_duration,
            "iti3_duration": iti3_duration,
            "decision_timed_out": decision_timed_out,
            "decision_response_limit_s": decision_response_limit_s,
            "decision_timeout_screen_duration_s": decision_timeout_screen_duration_s,
            "stimulus1_onset_time": stimulus1_onset_time,
            "stimulus2_onset_time": stimulus2_onset_time,
            "both_fruits_onset_time": both_fruits_onset_time,
            "choice_time": choice_time,
        }
        self.decision_data.append(decision_data)
    
    def _write_csv(self, filepath, fieldnames, rows, fallback_filepath=None):
        """
        Helper to write a CSV file with fallback location support.
        rows: list of lists (already ordered to match fieldnames)
        Returns the path actually written to, or None on failure.
        """
        def _do_write(path, header, data_rows):
            with open(path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(header)
                for row in data_rows:
                    writer.writerow(row)

        try:
            _do_write(filepath, fieldnames, rows)
            return filepath
        except (IOError, OSError, FileNotFoundError) as e:
            print(f"ERROR: Could not save to {filepath}")
            print(f"Error type: {type(e).__name__}, Error message: {str(e)}")
            print(f"\n{'='*60}")
            print(f"DIRECTORY CREATION REQUIRED")
            print(f"{'='*60}")
            print(f"The directory {self.subject_dir} does not exist.")
            print(f"Please create it manually:")
            print(f"  1. Go to your experiment folder")
            print(f"  2. Navigate to the 'data' folder")
            print(f"  3. Create a new folder named: sub-1")
            print(f"  4. Then re-run the experiment")
            print(f"{'='*60}\n")

            if fallback_filepath:
                try:
                    _do_write(fallback_filepath, fieldnames, rows)
                    print(f"Saved to fallback location: {fallback_filepath}")
                    print(f"Please move this file to {self.subject_dir}/ after creating the folder")
                    return fallback_filepath
                except Exception as e2:
                    print(f"ERROR: Could not save file anywhere. Secondary error: {type(e2).__name__}: {str(e2)}")
            return None

    def save_learning_data(self, block_num, block_name):
        """
        Save learning data to two CSV files:
          1. Main learning file (existing behaviour, unchanged)
          2. Timestamps file (new) with fruit_onset_time, first_response_time, submit_time
        
        Args:
            block_num: Block number (1, 2, etc.)
            block_name: "rewards" or "punishment"
        """
        if not self.learning_data:
            print("No learning data to save")
            return
        
        session_str = f"{self.session_number:03d}"  # Zero-padded to 3 digits for filename
        base_name = f"sub-{session_str}_day-{self.day}_block-{block_num}_learning_{block_num}_{block_name}"

        # ── 1. Main learning CSV (existing behaviour, unchanged) ──────────────
        main_filename = f"{base_name}.csv"
        main_filepath = _join_path(self.subject_dir, main_filename)
        main_fallback = _join_path(self.experiment_dir, main_filename)

        print(f"DEBUG save_learning_data:")
        print(f"  session_number: {self.session_number}")
        print(f"  day: {self.day}")
        print(f"  subject_dir: {self.subject_dir} (always sub-1)")
        print(f"  filename: {main_filename} (with zero-padding)")
        print(f"  full filepath: {main_filepath}")

        main_header = [
            "user_id", "trial_number", "block_id", "block_name",
            "stimulus_identity", "stimulus_average_points", "actual_points",
            "prediction_value", "reaction_time_ms", "responded_in_time", "trial_timed_out",
            "slider_starting_value",
            "crosshair1_rand", "crosshair1_duration",
            "actual_points_duration",
            "crosshair2_rand", "crosshair2_duration",
            "timeout_duration",
            "keypress_sequence"
        ]

        main_rows = []
        for trial in self.learning_data:
            keypress_str = "; ".join([
                f"{kp['direction']}:{kp['reaction_time_ms']}ms"
                for kp in trial['keypresses']
            ]) if trial['keypresses'] else ""

            main_rows.append([
                trial['user_id'],
                trial['trial_number'],
                trial['block_id'],
                trial['block_name'],
                trial['stimulus_identity'],
                trial['stimulus_average_points'],
                trial['actual_points'],
                trial['prediction_value'],
                trial['reaction_time_ms'],
                trial['responded_in_time'],
                trial['trial_timed_out'],
                trial.get('slider_starting_value', None),
                trial.get('crosshair1_rand', None),
                trial.get('crosshair1_duration', None),
                trial.get('actual_points_duration', None),
                trial.get('crosshair2_rand', None),
                trial.get('crosshair2_duration', None),
                trial.get('timeout_duration', None),
                keypress_str
            ])

        result = self._write_csv(main_filepath, main_header, main_rows, main_fallback)
        if result:
            print(f"Successfully saved learning data to {result} ({len(self.learning_data)} trials)")

        # ── 2. Timestamps CSV (new file) ──────────────────────────────────────
        ts_filename = f"{base_name}_timestamps.csv"
        ts_filepath = _join_path(self.subject_dir, ts_filename)
        ts_fallback = _join_path(self.experiment_dir, ts_filename)

        print(f"Saving timestamps file: {ts_filepath}")

        ts_header = [
            "user_id",
            "trial_number",
            "block_id",
            "block_name",
            "stimulus_identity",
            "fruit_onset_time_s",      # seconds since scanner sync (key 5)
            "first_response_time_s",   # seconds since scanner sync to first 1 or 3 press
            "submit_time_s",           # seconds since scanner sync to key 2 press
            "time_to_first_move_s",    # first_response_time - fruit_onset_time
            "decision_duration_s",     # submit_time - fruit_onset_time
            "adjustment_duration_s",   # submit_time - first_response_time
            "responded_in_time",
            "trial_timed_out",
        ]

        ts_rows = []
        for trial in self.learning_data:
            fruit_onset    = trial.get('fruit_onset_time', None)
            first_response = trial.get('first_response_time', None)
            submit         = trial.get('submit_time', None)

            # Derived durations (None if any component is missing)
            def _diff(a, b):
                if a is not None and b is not None:
                    return round(a - b, 4)
                return None

            time_to_first_move  = _diff(first_response, fruit_onset)
            decision_duration   = _diff(submit, fruit_onset)
            adjustment_duration = _diff(submit, first_response)

            ts_rows.append([
                trial['user_id'],
                trial['trial_number'],
                trial['block_id'],
                trial['block_name'],
                trial['stimulus_identity'],
                round(fruit_onset, 4)    if fruit_onset    is not None else "",
                round(first_response, 4) if first_response is not None else "",
                round(submit, 4)         if submit         is not None else "",
                time_to_first_move  if time_to_first_move  is not None else "",
                decision_duration   if decision_duration   is not None else "",
                adjustment_duration if adjustment_duration is not None else "",
                trial['responded_in_time'],
                trial['trial_timed_out'],
            ])

        result_ts = self._write_csv(ts_filepath, ts_header, ts_rows, ts_fallback)
        if result_ts:
            print(f"Successfully saved timestamps to {result_ts} ({len(ts_rows)} trials)")

        # Clear data after saving both files
        self.learning_data = []
        self.learning_keypresses = []
    
    def save_decision_data(self, block_num, block_name):
        """
        Save decision making data to CSV file
        
        Args:
            block_num: Block number (3, 4, etc.)
            block_name: "implicit" or "explicit"
        """
        if not self.decision_data:
            print("No decision data to save")
            return
        
        # Create filename: sub-001_day-1_block-3_decisions_1_implicit.csv
        # Filename: WITH zero-padding (sub-001, not sub-1)
        session_str = f"{self.session_number:03d}"  # Zero-padded to 3 digits for filename
        filename = f"sub-{session_str}_day-{self.day}_block-{block_num}_decisions_{block_num}_{block_name}.csv"
        filepath = _join_path(self.subject_dir, filename)
        
        # DEBUG: Print paths for troubleshooting
        print(f"DEBUG save_decision_data:")
        print(f"  session_number: {self.session_number}")
        print(f"  day: {self.day}")
        print(f"  subject_dir: {self.subject_dir} (always sub-1)")
        print(f"  filename: {filename} (with zero-padding)")
        print(f"  full filepath: {filepath}")
        
        # Try to write CSV file
        # Note: Directory should be created manually before running experiment
        # Note: Directory should be created manually before running experiment
        try:
            # Write CSV
            with open(filepath, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                
                # Header row
                writer.writerow([
                    "user_id", "trial_number", "block_id", "block_name",
                    "first_stimulus_id", "first_stimulus_side",
                    "left_stimulus_id", "right_stimulus_id",
                    "left_stimulus_num", "right_stimulus_num",
                    "left_avg_points", "right_avg_points",
                    "choice", "reaction_time_ms",
                    "iti1_duration", "iti2_duration", "iti3_duration",
                    "decision_timed_out", "decision_response_limit_s", "decision_timeout_screen_duration_s",
                    "stimulus1_onset_time_s", "stimulus2_onset_time_s", "both_fruits_onset_time_s",
                    "choice_time_s",
                    "time_to_choice_from_s1_s", "time_to_choice_from_s2_s", "time_to_choice_from_both_s"
                ])
                
                # Data rows
                for trial in self.decision_data:
                    s1 = trial.get('stimulus1_onset_time', None)
                    s2 = trial.get('stimulus2_onset_time', None)
                    sb = trial.get('both_fruits_onset_time', None)
                    ct = trial.get('choice_time', None)

                    def _diff(a, b):
                        if a is not None and b is not None:
                            return round(a - b, 4)
                        return ""

                    writer.writerow([
                        trial['user_id'],
                        trial['trial_number'],
                        trial['block_id'],
                        trial['block_name'],
                        trial.get('first_stimulus_id', ""),
                        trial.get('first_stimulus_side', ""),
                        trial['left_stimulus_id'],
                        trial['right_stimulus_id'],
                        trial['left_stimulus_num'],
                        trial['right_stimulus_num'],
                        trial['left_avg_points'],
                        trial['right_avg_points'],
                        trial['choice'],
                        trial['reaction_time_ms'],
                        trial.get('iti1_duration', None),
                        trial.get('iti2_duration', None),
                        trial.get('iti3_duration', None),
                        trial.get('decision_timed_out', None),
                        trial.get('decision_response_limit_s', None),
                        trial.get('decision_timeout_screen_duration_s', None),
                        round(s1, 4) if s1 is not None else "",
                        round(s2, 4) if s2 is not None else "",
                        round(sb, 4) if sb is not None else "",
                        round(ct, 4) if ct is not None else "",
                        _diff(ct, s1),
                        _diff(ct, s2),
                        _diff(ct, sb),
                    ])
            print(f"Successfully saved decision data to {filepath} ({len(self.decision_data)} trials)")
        except (IOError, OSError, FileNotFoundError) as e:
            print(f"ERROR: Could not save to {filepath}")
            print(f"Error type: {type(e).__name__}, Error message: {str(e)}")
            print(f"Attempted full path: {filepath}")
            print(f"Subject directory: {self.subject_dir}")
            print(f"Experiment directory: {self.experiment_dir}")
            
            print(f"\n{'='*60}")
            print(f"DIRECTORY CREATION REQUIRED")
            print(f"{'='*60}")
            print(f"The directory {self.subject_dir} does not exist.")
            print(f"Please create it manually:")
            print(f"  1. Go to your experiment folder")
            print(f"  2. Navigate to the 'data' folder")
            print(f"  3. Create a new folder named: sub-1")
            print(f"     (always use 'sub-1', regardless of session number)")
            print(f"  4. Then re-run the experiment")
            print(f"{'='*60}\n")
            
            try:
                fallback_path = _join_path(self.experiment_dir, filename)
                print(f"Attempting to save to fallback location: {fallback_path}")
                print(f"NOTE: You should move this file to {self.subject_dir}/ after creating the folder")
                with open(fallback_path, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow([
                        "user_id", "trial_number", "block_id", "block_name",
                        "first_stimulus_id", "first_stimulus_side",
                        "left_stimulus_id", "right_stimulus_id",
                        "left_stimulus_num", "right_stimulus_num",
                        "left_avg_points", "right_avg_points",
                        "choice", "reaction_time_ms",
                        "iti1_duration", "iti2_duration", "iti3_duration",
                        "decision_timed_out", "decision_response_limit_s", "decision_timeout_screen_duration_s",
                        "stimulus1_onset_time_s", "stimulus2_onset_time_s", "both_fruits_onset_time_s",
                        "choice_time_s", "time_to_choice_from_s1_s", "time_to_choice_from_s2_s", "time_to_choice_from_both_s"
                    ])
                    for trial in self.decision_data:
                        s1 = trial.get('stimulus1_onset_time', None)
                        s2 = trial.get('stimulus2_onset_time', None)
                        sb = trial.get('both_fruits_onset_time', None)
                        ct = trial.get('choice_time', None)
                        def _diff(a, b):
                            return round(a - b, 4) if a is not None and b is not None else ""
                        writer.writerow([
                            trial['user_id'], trial['trial_number'], trial['block_id'],
                            trial['block_name'], trial.get('first_stimulus_id', ""),
                            trial.get('first_stimulus_side', ""), trial['left_stimulus_id'],
                            trial['right_stimulus_id'], trial['left_stimulus_num'],
                            trial['right_stimulus_num'], trial['left_avg_points'],
                            trial['right_avg_points'], trial['choice'],
                            trial['reaction_time_ms'],
                            trial.get('iti1_duration', None),
                            trial.get('iti2_duration', None),
                            trial.get('iti3_duration', None),
                            trial.get('decision_timed_out', None),
                            trial.get('decision_response_limit_s', None),
                            trial.get('decision_timeout_screen_duration_s', None),
                            round(s1, 4) if s1 is not None else "",
                            round(s2, 4) if s2 is not None else "",
                            round(sb, 4) if sb is not None else "",
                            round(ct, 4) if ct is not None else "",
                            _diff(ct, s1), _diff(ct, s2), _diff(ct, sb),
                        ])
                print(f"Saved to fallback location: {fallback_path}")
                print(f"Please create {self.subject_dir} and move this file there")
                filepath = fallback_path
            except Exception as e2:
                print(f"ERROR: Could not save file anywhere")
                print(f"Secondary error: {type(e2).__name__}: {str(e2)}")
                print(f"Please create the directory manually: {self.subject_dir}")
                return
        
        # Clear data after saving
        self.decision_data = []


# Global logger instance (will be initialized in startTaskBeginExperiment)
data_logger = None

def get_logger():
    """Get the global data logger instance"""
    global data_logger
    return data_logger

def initialize_logger(session_number=1, day=1, experiment_dir="data"):
    """Initialize the global data logger"""
    global data_logger
    data_logger = DataLogger(session_number, day, experiment_dir)
    return data_logger