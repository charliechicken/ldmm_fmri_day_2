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
                          slider_starting_value=None):
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
            "keypresses": self.learning_keypresses.copy()  # Copy keypress log
        }
        self.learning_data.append(trial_data)
    
    def start_decision(self, decision_start_time):
        """Record decision start time"""
        self.decision_start_time = decision_start_time
    
    def log_decision_trial(self, trial_num, block_id, block_name, first_stimulus_id,
                          first_stimulus_side, left_stimulus_id, right_stimulus_id,
                          left_stimulus_num, right_stimulus_num, left_avg_points,
                          right_avg_points, choice, reaction_time_ms):
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
            "reaction_time_ms": reaction_time_ms
        }
        self.decision_data.append(decision_data)
    
    def save_learning_data(self, block_num, block_name):
        """
        Save learning data to CSV file
        
        Args:
            block_num: Block number (1, 2, etc.)
            block_name: "rewards" or "punishment"
        """
        if not self.learning_data:
            print("No learning data to save")
            return
        
        # Create filename: sub-001_day-1_block-1_learning_1_punishment.csv
        # Filename: WITH zero-padding (sub-001, not sub-1)
        session_str = f"{self.session_number:03d}"  # Zero-padded to 3 digits for filename
        filename = f"sub-{session_str}_day-{self.day}_block-{block_num}_learning_{block_num}_{block_name}.csv"
        filepath = _join_path(self.subject_dir, filename)
        
        # DEBUG: Print paths for troubleshooting
        print(f"DEBUG save_learning_data:")
        print(f"  session_number: {self.session_number}")
        print(f"  day: {self.day}")
        print(f"  subject_dir: {self.subject_dir} (always sub-1)")
        print(f"  filename: {filename} (with zero-padding)")
        print(f"  full filepath: {filepath}")
        
        # Try to write CSV file
        # Note: Directory should be created manually before running experiment
        try:
            # Write CSV
            with open(filepath, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                
                # Header row
                writer.writerow([
                    "user_id", "trial_number", "block_id", "block_name",
                    "stimulus_identity", "stimulus_average_points", "actual_points",
                    "prediction_value", "reaction_time_ms", "responded_in_time", "trial_timed_out",
                    "slider_starting_value", "keypress_sequence"  # Will contain all keypresses as JSON-like string
                ])
                
                # Data rows
                for trial in self.learning_data:
                    # Format keypresses as a string
                    keypress_str = "; ".join([
                        f"{kp['direction']}:{kp['reaction_time_ms']}ms"
                        for kp in trial['keypresses']
                    ]) if trial['keypresses'] else ""
                    
                    writer.writerow([
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
                        trial.get('slider_starting_value', None),  # Use .get() for backward compatibility
                        keypress_str
                    ])
            print(f"Successfully saved learning data to {filepath} ({len(self.learning_data)} trials)")
        except (IOError, OSError, FileNotFoundError) as e:
            # Directory might not exist - try creating it
            print(f"ERROR: Could not save to {filepath}")
            print(f"Error type: {type(e).__name__}, Error message: {str(e)}")
            print(f"Attempted full path: {filepath}")
            print(f"Subject directory: {self.subject_dir}")
            print(f"Experiment directory: {self.experiment_dir}")
            
            # Directory doesn't exist - save to data folder with note, or provide instructions
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
            
            # Try saving to data folder as fallback (user can move it later)
            try:
                fallback_path = _join_path(self.experiment_dir, filename)
                print(f"Attempting to save to fallback location: {fallback_path}")
                print(f"NOTE: You should move this file to {self.subject_dir}/ after creating the folder")
                with open(fallback_path, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow([
                        "user_id", "trial_number", "block_id", "block_name",
                        "stimulus_identity", "stimulus_average_points", "actual_points",
                        "prediction_value", "reaction_time_ms", "responded_in_time", "trial_timed_out",
                        "slider_starting_value", "keypress_sequence"
                    ])
                    for trial in self.learning_data:
                        keypress_str = "; ".join([
                            f"{kp['direction']}:{kp['reaction_time_ms']}ms"
                            for kp in trial['keypresses']
                        ]) if trial['keypresses'] else ""
                        writer.writerow([
                            trial['user_id'], trial['trial_number'], trial['block_id'],
                            trial['block_name'], trial['stimulus_identity'],
                            trial['stimulus_average_points'], trial['actual_points'],
                            trial['prediction_value'], trial['reaction_time_ms'],
                            trial['responded_in_time'], trial['trial_timed_out'],
                            trial.get('slider_starting_value', None),  # Use .get() for backward compatibility
                            keypress_str
                        ])
                print(f"Saved to fallback location: {fallback_path}")
                print(f"Please create {self.subject_dir} and move this file there")
                filepath = fallback_path
            except Exception as e2:
                print(f"ERROR: Could not save file anywhere")
                print(f"Secondary error: {type(e2).__name__}: {str(e2)}")
                print(f"Please create the directory manually: {self.subject_dir}")
                return
        
        # File was already saved above, message was printed
        
        # Clear data after saving
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
                    "choice", "reaction_time_ms"
                ])
                
                # Data rows
                for trial in self.decision_data:
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
                        trial['reaction_time_ms']
                    ])
            print(f"Successfully saved decision data to {filepath} ({len(self.decision_data)} trials)")
        except (IOError, OSError, FileNotFoundError) as e:
            # Directory might not exist - try creating it
            print(f"ERROR: Could not save to {filepath}")
            print(f"Error type: {type(e).__name__}, Error message: {str(e)}")
            print(f"Attempted full path: {filepath}")
            print(f"Subject directory: {self.subject_dir}")
            print(f"Experiment directory: {self.experiment_dir}")
            
            # Directory doesn't exist - save to data folder with note, or provide instructions
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
            
            # Try saving to data folder as fallback (user can move it later)
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
                        "choice", "reaction_time_ms"
                    ])
                    for trial in self.decision_data:
                        writer.writerow([
                            trial['user_id'], trial['trial_number'], trial['block_id'],
                            trial['block_name'], trial.get('first_stimulus_id', ""),
                            trial.get('first_stimulus_side', ""), trial['left_stimulus_id'],
                            trial['right_stimulus_id'], trial['left_stimulus_num'],
                            trial['right_stimulus_num'], trial['left_avg_points'],
                            trial['right_avg_points'], trial['choice'],
                            trial['reaction_time_ms']
                        ])
                print(f"Saved to fallback location: {fallback_path}")
                print(f"Please create {self.subject_dir} and move this file there")
                filepath = fallback_path
            except Exception as e2:
                print(f"ERROR: Could not save file anywhere")
                print(f"Secondary error: {type(e2).__name__}: {str(e2)}")
                print(f"Please create the directory manually: {self.subject_dir}")
                return
        
        # File was already saved above, message was printed
        
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

