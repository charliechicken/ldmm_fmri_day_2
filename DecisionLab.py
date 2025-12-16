#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2025.1.1),
    on November 10, 2025, at 16:33
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, STOPPING, FINISHED, PRESSED, 
    RELEASED, FOREVER, priority
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2025.1.1'
expName = 'DecisionLab'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'Global clock format': 'None',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'expVersion|hid': expVersion,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = False
_winSize = [1280, 720]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # replace default participant ID
    if prefs.piloting['replaceParticipantID']:
        expInfo['participant'] = 'pilot'

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\charl\\psychoPyDecision\\DecisionLab.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=True, allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    if PILOTING:
        # show a visual indicator if we're in piloting mode
        if prefs.piloting['showPilotingIndicator']:
            win.showPilotingIndicator()
        # always show the mouse in piloting mode
        if prefs.piloting['forceMouseVisible']:
            win.mouseVisible = True
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    if deviceManager.getDevice('key_resp_2') is None:
        # initialise key_resp_2
        key_resp_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_2',
        )
    if deviceManager.getDevice('key_resp_transition') is None:
        # initialise key_resp_transition
        key_resp_transition = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_transition',
        )
    if deviceManager.getDevice('key_resp_4') is None:
        # initialise key_resp_4
        key_resp_4 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_4',
        )
    if deviceManager.getDevice('key_resp_5') is None:
        # initialise key_resp_5
        key_resp_5 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_5',
        )
    if deviceManager.getDevice('key_resp_6') is None:
        # initialise key_resp_6
        key_resp_6 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_6',
        )
    if deviceManager.getDevice('key_resp_8') is None:
        # initialise key_resp_8
        key_resp_8 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_8',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], currentRoutine=None):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    currentRoutine : psychopy.data.Routine
        Current Routine we are in at time of pausing, if any. This object tells PsychoPy what Components to pause/play/dispatch.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # dispatch messages on response components
        if currentRoutine is not None:
            for comp in currentRoutine.getDispatchComponents():
                comp.device.dispatchMessages()
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "Welcome" ---
    button = visual.ButtonStim(win, 
        text='Next', font='Arvo',
        pos=(0.6, -0.4),
        letterHeight=0.05,
        size=(0.2, 0.1), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='button',
        depth=0
    )
    button.buttonClock = core.Clock()
    text = visual.TextStim(win=win, name='text',
        text='Welcome to the Prediction Game!\n\nYour goal in this game is to learn the number of points associated with different fruits.\n\nIn the next couple of slides, instructions for the task will be provided, followed by the task itself.\n\nAt the end of the task, you will be presented with several additional questions.',
        font='Arial',
        pos=(0, .2), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    apple = visual.ImageStim(
        win=win,
        name='apple', 
        image='images/apple.png', mask=None, anchor='center',
        ori=0.0, pos=(-.4, -.2), draggable=False, size=(0.15, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    banana = visual.ImageStim(
        win=win,
        name='banana', 
        image='images/banana.png', mask=None, anchor='center',
        ori=0.0, pos=(-.24, -.2), draggable=False, size=(0.15, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    grape = visual.ImageStim(
        win=win,
        name='grape', 
        image='images/grapes.png', mask=None, anchor='center',
        ori=0.0, pos=(-.08, -.2), draggable=False, size=(0.15, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    kiwi = visual.ImageStim(
        win=win,
        name='kiwi', 
        image='images/kiwi.png', mask=None, anchor='center',
        ori=0.0, pos=(.08, -.2), draggable=False, size=(0.15, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    pear = visual.ImageStim(
        win=win,
        name='pear', 
        image='images/pear.png', mask=None, anchor='center',
        ori=0.0, pos=(.24, -.2), draggable=False, size=(0.15, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-6.0)
    strawberry = visual.ImageStim(
        win=win,
        name='strawberry', 
        image='images/strawberry.png', mask=None, anchor='center',
        ori=0.0, pos=(.4, -.2), draggable=False, size=(0.15, 0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-7.0)
    
    # --- Initialize components for Routine "TaskStructure" ---
    text_2 = visual.TextStim(win=win, name='text_2',
        text="Task Structure\n\nIn this task, you'll see different fruits as you play.\n\nEach fruit can either give you points or take points away.\n\nYou'll earn points when the number is positive (+), and lose points when it's negative (-).",
        font='Arial',
        pos=(0, .2), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    button_2 = visual.ButtonStim(win, 
        text='Next', font='Arvo',
        pos=(0.6, -0.4),
        letterHeight=0.05,
        size=(0.2, 0.1), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='button_2',
        depth=-1
    )
    button_2.buttonClock = core.Clock()
    text_19 = visual.TextStim(win=win, name='text_19',
        text='+50',
        font='Arial',
        pos=(-.2, -.2), draggable=False, height=0.15, wrapWidth=None, ori=0.0, 
        color=[-1.0000, 0.0039, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    text_21 = visual.TextStim(win=win, name='text_21',
        text='-50',
        font='Arial',
        pos=(.2, -.2), draggable=False, height=0.15, wrapWidth=None, ori=0.0, 
        color=[0.5294, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "yourGoal" ---
    text_3 = visual.TextStim(win=win, name='text_3',
        text='Your Goal\n\nRight after a fruit is shown, you will be asked to predict how many points it will provide this time.\n\nDo your best to be as accurate as you can.\n\nImmediately after your prediction, you will be shown how many points it actually provided this time.',
        font='Arial',
        pos=(0, .3), draggable=False, height=0.035, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    button_3 = visual.ButtonStim(win, 
        text='Next', font='Arvo',
        pos=(0.6, -0.4),
        letterHeight=0.05,
        size=(0.2, 0.1), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='button_3',
        depth=-1
    )
    button_3.buttonClock = core.Clock()
    slider_2 = visual.Slider(win=win, name='slider_2',
        startValue=0, size=(1, 0.075), pos=(0, -0.2), units=win.units,
        labels=(-100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100), ticks=(-100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100), granularity=5.0,
        style='slider', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-2, readOnly=False)
    text_22 = visual.TextStim(win=win, name='text_22',
        text='"How many points do you expect to receive from this fruit?"',
        font='Arial',
        pos=(0, -0.08), draggable=False, height=0.055, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "keyInstructions" ---
    text_20 = visual.TextStim(win=win, name='text_20',
        text='Pressing "1" will shift the slider value leftwards by a value of 5. Pressing "3" will shift the slider value rightwards, also by a value of 5. \n\nPressing "2" will confirm your answer.\n',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    button_5 = visual.ButtonStim(win, 
        text='Next', font='Arvo',
        pos=(0.6, -0.4),
        letterHeight=0.05,
        size=(0.4, 0.1), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='button_5',
        depth=-1
    )
    button_5.buttonClock = core.Clock()
    
    # --- Initialize components for Routine "startTask" ---
    text_4 = visual.TextStim(win=win, name='text_4',
        text='Start the Task\n\nWhen you are ready to start the task, press the “Next” button.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    button_4 = visual.ButtonStim(win, 
        text='Start Task', font='Arvo',
        pos=(0.6, -0.4),
        letterHeight=0.05,
        size=(0.4, 0.1), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='button_4',
        depth=-1
    )
    button_4.buttonClock = core.Clock()
    # Run 'Begin Experiment' code from code
    import random
    import sys
    
    # Add current directory to path to import data_logging
    # PsychoPy runs from the experiment directory, so data_logging.py should be in the same directory
    # NO os import - completely avoid it for PsychoPy compatibility (doesn't work online/Pavlovia)
    try:
        # Try to import data_logging from the experiment directory
        # This should work if data_logging.py is in the same directory as the .psyexp file
        from data_logging import initialize_logger
    except ImportError:
        print("WARNING: Could not import data_logging module. Data logging will be disabled.")
        print("Make sure data_logging.py is in the same directory as your .psyexp file.")
        # Create a dummy logger
        class DummyLogger:
            def __init__(self, *args, **kwargs): pass
            def start_trial(self, *args): pass
            def log_keypress(self, *args): pass
            def log_learning_trial(self, *args, **kwargs): pass
            def log_decision_trial(self, *args, **kwargs): pass
            def save_learning_data(self, *args, **kwargs): pass
            def save_decision_data(self, *args, **kwargs): pass
        def initialize_logger(*args, **kwargs):
            return DummyLogger()
    
    # Initialize data logger
    # TODO: Set subject_id and day appropriately (you can make these configurable)
    SUBJECT_ID = 1  # Change this for different subjects
    DAY = 1  # Change this for different days
    data_logger = initialize_logger(subject_id=SUBJECT_ID, day=DAY, experiment_dir="data")
    globals()['data_logger'] = data_logger
    
    # Load timing configuration from text file
    # Use simple defaults, config loading happens in individual routines to avoid os conflicts
    TRIAL_TIMEOUT_SECONDS = 8.0
    CROSSHAIR_RANDOM_VALUES = [2, 3, 4]
    TIMEOUT_SCREEN_DURATION = 1.5
    ACTUAL_POINTS_DURATION = 2.0
    
    # Try to load from config file (will be loaded in routines that need it)
    print(f"Using timing config: timeout={TRIAL_TIMEOUT_SECONDS}s, actualPoints={ACTUAL_POINTS_DURATION}s")
    
    image_dir = "images/"
    all_fruits = ["apple.png", "banana.png", "strawberry.png", "kiwi.png", "pear.png", "grapes.png"]
    
    # Create fruit name mapping (remove .png extension)
    fruit_names = [f.replace('.png', '') for f in all_fruits]
    
    # Create numerical ID mapping (1-6 for each fruit)
    # This will be used for decision making phase
    fruit_to_num = {}
    num_to_fruit = {}
    for i, fruit in enumerate(fruit_names, 1):
        fruit_to_num[fruit] = i
        num_to_fruit[i] = fruit
    
    # Store globally for use in decision making
    globals()['fruit_to_num'] = fruit_to_num
    globals()['num_to_fruit'] = num_to_fruit
    
    # Randomly assign 3 fruits as gain and 3 as loss
    random.shuffle(all_fruits)
    gain_fruits = all_fruits[:3]
    loss_fruits = all_fruits[3:]
    
    # Randomly assign baseline values to each fruit
    gain_baselines = random.sample([20, 50, 80], 3)
    loss_baselines = random.sample([-20, -50, -80], 3)
    
    print(f"Gain fruits: {gain_fruits} with baselines: {gain_baselines}")
    print(f"Loss fruits: {loss_fruits} with baselines: {loss_baselines}")
    
    def make_values(base):
        # Create 10 unique values: [base]*4 + [base+5]*2 + [base-5]*2 + [base+10, base-10]
        values = [base]*4 + [base+5]*2 + [base-5]*2 + [base+10, base-10]
        # Shuffle them once
        random.shuffle(values)
        # Double the list to get 20 presentations per fruit
        return values * 2
    
    gain_block, loss_block = [], []
    
    for fruit, base in zip(gain_fruits, gain_baselines):
        values = make_values(base)  # This gives 20 values per fruit
        for val in values:
            gain_block.append({"block":"gain", "fruit":image_dir+fruit, "baseline":base, "true_value":val})
    
    for fruit, base in zip(loss_fruits, loss_baselines):
        values = make_values(base)  # This gives 20 values per fruit
        for val in values:
            loss_block.append({"block":"loss", "fruit":image_dir+fruit, "baseline":base, "true_value":val})
    
    # Shuffle each block to randomize trial order
    random.shuffle(gain_block)
    random.shuffle(loss_block)
    
    # Trial count is determined by loop nReps in PsychoPy Builder
    # The loop nReps should be set to total number of trials (e.g., 60)
    # We'll use the first nReps/2 trials from each block
    # Full blocks have 60 trials each (3 fruits × 20 presentations)
    # For 60 total trials: use first 30 from gain_block and first 30 from loss_block
    
    # Don't limit here - the loop nReps will control how many trials run
    # We'll use all available trials, and the loop will stop when nReps is reached
    print(f"Full gain block: {len(gain_block)} trials available")
    print(f"Full loss block: {len(loss_block)} trials available")
    print(f"NOTE: Set loop nReps to total trials (e.g., 60 for 30 gain + 30 loss)")
    print(f"      The code will use first nReps/2 from each block")
    
    # Randomly decide which block comes first
    block_order = ["gain", "loss"]
    random.shuffle(block_order)
    first_block = block_order[0]
    second_block = block_order[1]
    
    # Note: Trial count per block will be determined by loop nReps / 2
    # For now, we'll use all available trials and let the loop control it
    # The combined block will be truncated by the loop's nReps
    
    print(f"Block order: {first_block} first, then {second_block}")
    
    # Create combined block list in the random order
    # IMPORTANT: This ensures all trials from first block appear first, then all from second block
    # We'll create the full combined block, but trialBeginRoutine will limit based on nReps
    combined_learning_block = []
    if first_block == "gain":
        # First block: all gain trials, then all loss trials
        combined_learning_block = gain_block.copy() + loss_block.copy()
        print(f"Combined block: {len(gain_block)} gains + {len(loss_block)} losses = {len(combined_learning_block)} total")
    else:
        # First block: all loss trials, then all gain trials
        combined_learning_block = loss_block.copy() + gain_block.copy()
        print(f"Combined block: {len(loss_block)} losses + {len(gain_block)} gains = {len(combined_learning_block)} total")
    
    # Explicitly store in globals to ensure it's accessible in other routines
    globals()['combined_learning_block'] = combined_learning_block
    globals()['gain_block'] = gain_block
    globals()['loss_block'] = loss_block
    
    learning_block_index = -1
    # Store in globals to ensure it persists
    globals()['learning_block_index'] = learning_block_index
    show_block_transition = False  # Flag to trigger transition screen between blocks
    globals()['show_block_transition'] = show_block_transition
    print(f"Combined learning block has {len(combined_learning_block)} trials")
    
    gain_index = -1
    loss_index = -1
    fruitFile = image_dir + "blank.png"
    trueVal = 0
    trueValStr = ""
    blockType = ""
    baselineR = 0
    
    
    print("Gain trials:", len(gain_block), "| Loss trials:", len(loss_block))
    
    # --- Initialize decision placeholders (prevents undefined variable error) ---
    leftFile = "images/blank.png"
    rightFile = "images/blank.png"
    
    # --- Decision pairs setup ---
    # Create fruit values dictionary based on randomized assignments
    fruit_values = {}
    for fruit, baseline in zip(gain_fruits, gain_baselines):
        fruit_values[image_dir + fruit] = baseline
    for fruit, baseline in zip(loss_fruits, loss_baselines):
        fruit_values[image_dir + fruit] = baseline
    
    # Create all unique pairs (15 pairs from 6 fruits: C(6,2) = 15)
    all_fruit_paths = [image_dir + fruit for fruit in all_fruits]
    decision_pairs = []
    for i in range(len(all_fruit_paths)):
        for j in range(i + 1, len(all_fruit_paths)):
            decision_pairs.append((all_fruit_paths[i], all_fruit_paths[j]))
    
    print(f"Created {len(decision_pairs)} unique pairs")
    
    # Build list of decision trials with counterbalancing (4 repetitions per pair)
    # IMPORTANT: First stimulus ALWAYS appears on LEFT, second stimulus ALWAYS appears on RIGHT
    # Counterbalancing ensures all 4 unique configurations appear:
    # 1. fruit1 left, fruit2 right, fruit1 appears first → fruit1 left, fruit2 right
    # 2. fruit1 left, fruit2 right, fruit2 appears first → fruit1 left, fruit2 right (but fruit2 shown first)
    # 3. fruit2 left, fruit1 right, fruit1 appears first → fruit2 left, fruit1 right (but fruit1 shown first)
    # 4. fruit2 left, fruit1 right, fruit2 appears first → fruit2 left, fruit1 right (but fruit2 shown first)
    
    decision_block = []
    for fruit1, fruit2 in decision_pairs:
        left_val = fruit_values[fruit1]
        right_val = fruit_values[fruit2]
        correct_side = "left" if left_val > right_val else "right"
        
        # Trial 1: fruit1 left, fruit2 right, fruit1 appears first
        # Sequence: fruit1 (left) → fruit2 (right) → both: fruit1 left, fruit2 right
        decision_block.append({
            "leftFruit": fruit1,
            "rightFruit": fruit2,
            "firstFruit": fruit1,
            "firstSide": "left",
            "secondFruit": fruit2,
            "secondSide": "right",
            "leftVal": left_val,
            "rightVal": right_val,
            "correct": correct_side
        })
        
        # Trial 2: fruit1 left, fruit2 right, fruit2 appears first
        # Sequence: fruit2 (left) → fruit1 (right) → both: fruit1 left, fruit2 right
        decision_block.append({
            "leftFruit": fruit1,
            "rightFruit": fruit2,
            "firstFruit": fruit2,
            "firstSide": "left",  # fruit2 appears first on left
            "secondFruit": fruit1,
            "secondSide": "right",  # fruit1 appears second on right
            "leftVal": left_val,
            "rightVal": right_val,
            "correct": correct_side
        })
        
        # Trial 3: fruit2 left, fruit1 right, fruit1 appears first
        # Sequence: fruit1 (left) → fruit2 (right) → both: fruit2 left, fruit1 right
        decision_block.append({
            "leftFruit": fruit2,
            "rightFruit": fruit1,
            "firstFruit": fruit1,
            "firstSide": "left",  # fruit1 appears first on left
            "secondFruit": fruit2,
            "secondSide": "right",  # fruit2 appears second on right
            "leftVal": right_val,
            "rightVal": left_val,
            "correct": "right" if correct_side == "left" else "left"
        })
        
        # Trial 4: fruit2 left, fruit1 right, fruit2 appears first
        # Sequence: fruit2 (left) → fruit1 (right) → both: fruit2 left, fruit1 right
        decision_block.append({
            "leftFruit": fruit2,
            "rightFruit": fruit1,
            "firstFruit": fruit2,
            "firstSide": "left",
            "secondFruit": fruit1,
            "secondSide": "right",
            "leftVal": right_val,
            "rightVal": left_val,
            "correct": "right" if correct_side == "left" else "left"
        })
    
    # Shuffle all trials
    random.shuffle(decision_block)
    
    decision_index = 0
    # Store in globals to ensure it persists across routines
    globals()['decision_index'] = decision_index
    globals()['decision_block'] = decision_block
    print(f"Decision trials: {len(decision_block)} (should be 60)")
    
    # Initialize ITI duration variables (will be set during trials)
    iti1_duration = 2.0  # Default
    iti2_duration = 2.0  # Default
    iti3_duration = 2.0  # Default (will be calculated in decisionMakingEndRoutine)
    
    # --- Additional variables for the experiment ---
    # True values display
    trueValuesText = ""
    
    # Decision making variables
    leftFile = "images/blank.png"
    rightFile = "images/blank.png"
    leftVal = 0
    rightVal = 0
    correct_side = ""
    decision_choice = ""
    decision_rt = 0
    decision_start_time = 0
    
    # Block transition variables
    transitionText = ""
    countdown_time = 30
    countdown_text = ""
    
    # Trial counters
    current_trial = 0
    total_trials = 30  # Change this to 30 for full experiment
    
    print(f"Experiment setup complete:")
    print(f"- Gain fruits: {gain_fruits}")
    print(f"- Loss fruits: {loss_fruits}")
    print(f"- Total learning trials: {len(gain_block) + len(loss_block)}")
    print(f"- Decision trials: {len(decision_block)}")
    
    
    # --- Initialize components for Routine "trial" ---
    slider = visual.Slider(win=win, name='slider',
        startValue=0, size=(1, 0.075), pos=(0, -0.2), units=win.units,
        labels=(-100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100), ticks=(-100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100), granularity=5.0,
        style='slider', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=0, readOnly=False)
    image_3 = visual.ImageStim(
        win=win,
        name='image_3', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.2), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    # Run 'Begin Experiment' code from code_2
    trueValStr = ""
    
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    text_slider_value = visual.TextStim(win=win, name='text_slider_value',
        text=None,
        font='Arial',
        pos=(0, -0.1), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "timeout" ---
    text_timeout = visual.TextStim(win=win, name='text_timeout',
        text='Time out',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "crosshair1" ---
    text_13 = visual.TextStim(win=win, name='text_13',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "actualPoints" ---
    text_actual_points = visual.TextStim(win=win, name='text_actual_points',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "crosshair2" ---
    text_14 = visual.TextStim(win=win, name='text_14',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "blockTransition" ---
    text_block_transition = visual.TextStim(win=win, name='text_block_transition',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_transition = keyboard.Keyboard(deviceName='key_resp_transition')
    
    # --- Initialize components for Routine "decisionPhase" ---
    text_5 = visual.TextStim(win=win, name='text_5',
        text='Learning Phase Completed!\n\nGreat job! You have completed the learning phase.\n\nPress 2 to continue with the decision tasks.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_4 = keyboard.Keyboard(deviceName='key_resp_4')
    
    # --- Initialize components for Routine "decisionInstructions" ---
    text_8 = visual.TextStim(win=win, name='text_8',
        text="\n\nYou have completed the learning phase and will now make decisions between pairs of fruits based on what you learned.\n\nPerformance Bonus Opportunity:\nMost people get 70% of their responses correctly.\nIf you'll be correct in more than 80% of your decisions, you will receive a bonus compensation.\n\nTry to recall the points associated with each fruit and make the best choices you can.\n\nClick 2 to continue.",
        font='Arial',
        pos=(0, 0), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    text_9 = visual.TextStim(win=win, name='text_9',
        text='Decision Task Instructions',
        font='Arial',
        pos=(0, 0.3), draggable=False, height=0.06, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_5 = keyboard.Keyboard(deviceName='key_resp_5')
    
    # --- Initialize components for Routine "whichFruit" ---
    text_10 = visual.TextStim(win=win, name='text_10',
        text='Which fruit would you pick?\n\nIn this block, you will choose between pairs of fruits. Choose the fruit you think will give you more points.\n\nUse "1" to choose the fruit on the left side of the screen, and "3" to choose the fruit on the right side of the screen.\n\nClick 2 to continue.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.06, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_6 = keyboard.Keyboard(deviceName='key_resp_6')
    
    # --- Initialize components for Routine "decisionStimulus1" ---
    text_question = visual.TextStim(win=win, name='text_question',
        text='Any text\n\nincluding line breaks',
        font='Arial',
        pos=(0, 0.3), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    image_left1 = visual.ImageStim(
        win=win,
        name='image_left1', 
        image=None, mask=None, anchor='center',
        ori=0.0, pos=(-0.4, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    image_right2 = visual.ImageStim(
        win=win,
        name='image_right2', 
        image=None, mask=None, anchor='center',
        ori=0.0, pos=(0.4, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    
    # --- Initialize components for Routine "decisionITI1" ---
    text_15 = visual.TextStim(win=win, name='text_15',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "decisionStimulus2" ---
    text_question_2 = visual.TextStim(win=win, name='text_question_2',
        text='Any text\n\nincluding line breaks',
        font='Arial',
        pos=(0, 0.3), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    image_left1_2 = visual.ImageStim(
        win=win,
        name='image_left1_2', 
        image=None, mask=None, anchor='center',
        ori=0.0, pos=(-0.4, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    image_right2_2 = visual.ImageStim(
        win=win,
        name='image_right2_2', 
        image=None, mask=None, anchor='center',
        ori=0.0, pos=(.4, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    
    # --- Initialize components for Routine "decisionITI2" ---
    text_16 = visual.TextStim(win=win, name='text_16',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "decisionMaking" ---
    text_question_1 = visual.TextStim(win=win, name='text_question_1',
        text='Which option do you prefer?',
        font='Arial',
        pos=(0, 0.3), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    image_left_left = visual.ImageStim(
        win=win,
        name='image_left_left', 
        image=None, mask=None, anchor='center',
        ori=0.0, pos=(-0.4, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    image_right_right = visual.ImageStim(
        win=win,
        name='image_right_right', 
        image=None, mask=None, anchor='center',
        ori=0.0, pos=(0.4, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    mouse_2 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_2.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "decisionTimeout" ---
    text_decision_timeout = visual.TextStim(win=win, name='text_decision_timeout',
        text='Time out',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "decisionITI3" ---
    text_17 = visual.TextStim(win=win, name='text_17',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "thankYou" ---
    text_11 = visual.TextStim(win=win, name='text_11',
        text='You completed the experiment!\n\nThank you for participating!\n\nPress 2 to end.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_8 = keyboard.Keyboard(deviceName='key_resp_8')
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "Welcome" ---
    # create an object to store info about Routine Welcome
    Welcome = data.Routine(
        name='Welcome',
        components=[button, text, apple, banana, grape, kiwi, pear, strawberry],
    )
    Welcome.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # reset button to account for continued clicks & clear times on/off
    button.reset()
    # store start times for Welcome
    Welcome.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Welcome.tStart = globalClock.getTime(format='float')
    Welcome.status = STARTED
    thisExp.addData('Welcome.started', Welcome.tStart)
    Welcome.maxDuration = None
    # keep track of which components have finished
    WelcomeComponents = Welcome.components
    for thisComponent in Welcome.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Welcome" ---
    Welcome.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *button* updates
        
        # if button is starting this frame...
        if button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            button.frameNStart = frameN  # exact frame index
            button.tStart = t  # local t and not account for scr refresh
            button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'button.started')
            # update status
            button.status = STARTED
            win.callOnFlip(button.buttonClock.reset)
            button.setAutoDraw(True)
        
        # if button is active this frame...
        if button.status == STARTED:
            # update params
            pass
            # check whether button has been pressed
            if button.isClicked:
                if not button.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    button.timesOn.append(button.buttonClock.getTime())
                    button.timesOff.append(button.buttonClock.getTime())
                elif len(button.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    button.timesOff[-1] = button.buttonClock.getTime()
                if not button.wasClicked:
                    # end routine when button is clicked
                    continueRoutine = False
                if not button.wasClicked:
                    # run callback code when button is clicked
                    pass
        # take note of whether button was clicked, so that next frame we know if clicks are new
        button.wasClicked = button.isClicked and button.status == STARTED
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # *apple* updates
        
        # if apple is starting this frame...
        if apple.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            apple.frameNStart = frameN  # exact frame index
            apple.tStart = t  # local t and not account for scr refresh
            apple.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(apple, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'apple.started')
            # update status
            apple.status = STARTED
            apple.setAutoDraw(True)
        
        # if apple is active this frame...
        if apple.status == STARTED:
            # update params
            pass
        
        # *banana* updates
        
        # if banana is starting this frame...
        if banana.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            banana.frameNStart = frameN  # exact frame index
            banana.tStart = t  # local t and not account for scr refresh
            banana.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(banana, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'banana.started')
            # update status
            banana.status = STARTED
            banana.setAutoDraw(True)
        
        # if banana is active this frame...
        if banana.status == STARTED:
            # update params
            pass
        
        # *grape* updates
        
        # if grape is starting this frame...
        if grape.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            grape.frameNStart = frameN  # exact frame index
            grape.tStart = t  # local t and not account for scr refresh
            grape.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(grape, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'grape.started')
            # update status
            grape.status = STARTED
            grape.setAutoDraw(True)
        
        # if grape is active this frame...
        if grape.status == STARTED:
            # update params
            pass
        
        # *kiwi* updates
        
        # if kiwi is starting this frame...
        if kiwi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            kiwi.frameNStart = frameN  # exact frame index
            kiwi.tStart = t  # local t and not account for scr refresh
            kiwi.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(kiwi, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'kiwi.started')
            # update status
            kiwi.status = STARTED
            kiwi.setAutoDraw(True)
        
        # if kiwi is active this frame...
        if kiwi.status == STARTED:
            # update params
            pass
        
        # *pear* updates
        
        # if pear is starting this frame...
        if pear.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pear.frameNStart = frameN  # exact frame index
            pear.tStart = t  # local t and not account for scr refresh
            pear.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pear, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pear.started')
            # update status
            pear.status = STARTED
            pear.setAutoDraw(True)
        
        # if pear is active this frame...
        if pear.status == STARTED:
            # update params
            pass
        
        # *strawberry* updates
        
        # if strawberry is starting this frame...
        if strawberry.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            strawberry.frameNStart = frameN  # exact frame index
            strawberry.tStart = t  # local t and not account for scr refresh
            strawberry.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(strawberry, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'strawberry.started')
            # update status
            strawberry.status = STARTED
            strawberry.setAutoDraw(True)
        
        # if strawberry is active this frame...
        if strawberry.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=Welcome,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Welcome.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Welcome.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Welcome" ---
    for thisComponent in Welcome.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Welcome
    Welcome.tStop = globalClock.getTime(format='float')
    Welcome.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Welcome.stopped', Welcome.tStop)
    thisExp.addData('button.numClicks', button.numClicks)
    if button.numClicks:
       thisExp.addData('button.timesOn', button.timesOn)
       thisExp.addData('button.timesOff', button.timesOff)
    else:
       thisExp.addData('button.timesOn', "")
       thisExp.addData('button.timesOff', "")
    thisExp.nextEntry()
    # the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "TaskStructure" ---
    # create an object to store info about Routine TaskStructure
    TaskStructure = data.Routine(
        name='TaskStructure',
        components=[text_2, button_2, text_19, text_21],
    )
    TaskStructure.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # reset button_2 to account for continued clicks & clear times on/off
    button_2.reset()
    # store start times for TaskStructure
    TaskStructure.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    TaskStructure.tStart = globalClock.getTime(format='float')
    TaskStructure.status = STARTED
    thisExp.addData('TaskStructure.started', TaskStructure.tStart)
    TaskStructure.maxDuration = None
    # keep track of which components have finished
    TaskStructureComponents = TaskStructure.components
    for thisComponent in TaskStructure.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "TaskStructure" ---
    TaskStructure.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        
        # if text_2 is starting this frame...
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_2.started')
            # update status
            text_2.status = STARTED
            text_2.setAutoDraw(True)
        
        # if text_2 is active this frame...
        if text_2.status == STARTED:
            # update params
            pass
        # *button_2* updates
        
        # if button_2 is starting this frame...
        if button_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            button_2.frameNStart = frameN  # exact frame index
            button_2.tStart = t  # local t and not account for scr refresh
            button_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'button_2.started')
            # update status
            button_2.status = STARTED
            win.callOnFlip(button_2.buttonClock.reset)
            button_2.setAutoDraw(True)
        
        # if button_2 is active this frame...
        if button_2.status == STARTED:
            # update params
            pass
            # check whether button_2 has been pressed
            if button_2.isClicked:
                if not button_2.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    button_2.timesOn.append(button_2.buttonClock.getTime())
                    button_2.timesOff.append(button_2.buttonClock.getTime())
                elif len(button_2.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    button_2.timesOff[-1] = button_2.buttonClock.getTime()
                if not button_2.wasClicked:
                    # end routine when button_2 is clicked
                    continueRoutine = False
                if not button_2.wasClicked:
                    # run callback code when button_2 is clicked
                    pass
        # take note of whether button_2 was clicked, so that next frame we know if clicks are new
        button_2.wasClicked = button_2.isClicked and button_2.status == STARTED
        
        # *text_19* updates
        
        # if text_19 is starting this frame...
        if text_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_19.frameNStart = frameN  # exact frame index
            text_19.tStart = t  # local t and not account for scr refresh
            text_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_19, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_19.started')
            # update status
            text_19.status = STARTED
            text_19.setAutoDraw(True)
        
        # if text_19 is active this frame...
        if text_19.status == STARTED:
            # update params
            pass
        
        # *text_21* updates
        
        # if text_21 is starting this frame...
        if text_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_21.frameNStart = frameN  # exact frame index
            text_21.tStart = t  # local t and not account for scr refresh
            text_21.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_21, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_21.started')
            # update status
            text_21.status = STARTED
            text_21.setAutoDraw(True)
        
        # if text_21 is active this frame...
        if text_21.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=TaskStructure,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            TaskStructure.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TaskStructure.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "TaskStructure" ---
    for thisComponent in TaskStructure.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for TaskStructure
    TaskStructure.tStop = globalClock.getTime(format='float')
    TaskStructure.tStopRefresh = tThisFlipGlobal
    thisExp.addData('TaskStructure.stopped', TaskStructure.tStop)
    thisExp.addData('button_2.numClicks', button_2.numClicks)
    if button_2.numClicks:
       thisExp.addData('button_2.timesOn', button_2.timesOn)
       thisExp.addData('button_2.timesOff', button_2.timesOff)
    else:
       thisExp.addData('button_2.timesOn', "")
       thisExp.addData('button_2.timesOff', "")
    thisExp.nextEntry()
    # the Routine "TaskStructure" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "yourGoal" ---
    # create an object to store info about Routine yourGoal
    yourGoal = data.Routine(
        name='yourGoal',
        components=[text_3, button_3, slider_2, text_22],
    )
    yourGoal.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # reset button_3 to account for continued clicks & clear times on/off
    button_3.reset()
    slider_2.reset()
    # store start times for yourGoal
    yourGoal.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    yourGoal.tStart = globalClock.getTime(format='float')
    yourGoal.status = STARTED
    thisExp.addData('yourGoal.started', yourGoal.tStart)
    yourGoal.maxDuration = None
    # keep track of which components have finished
    yourGoalComponents = yourGoal.components
    for thisComponent in yourGoal.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "yourGoal" ---
    yourGoal.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        
        # if text_3 is starting this frame...
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.started')
            # update status
            text_3.status = STARTED
            text_3.setAutoDraw(True)
        
        # if text_3 is active this frame...
        if text_3.status == STARTED:
            # update params
            pass
        # *button_3* updates
        
        # if button_3 is starting this frame...
        if button_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            button_3.frameNStart = frameN  # exact frame index
            button_3.tStart = t  # local t and not account for scr refresh
            button_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'button_3.started')
            # update status
            button_3.status = STARTED
            win.callOnFlip(button_3.buttonClock.reset)
            button_3.setAutoDraw(True)
        
        # if button_3 is active this frame...
        if button_3.status == STARTED:
            # update params
            pass
            # check whether button_3 has been pressed
            if button_3.isClicked:
                if not button_3.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    button_3.timesOn.append(button_3.buttonClock.getTime())
                    button_3.timesOff.append(button_3.buttonClock.getTime())
                elif len(button_3.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    button_3.timesOff[-1] = button_3.buttonClock.getTime()
                if not button_3.wasClicked:
                    # end routine when button_3 is clicked
                    continueRoutine = False
                if not button_3.wasClicked:
                    # run callback code when button_3 is clicked
                    pass
        # take note of whether button_3 was clicked, so that next frame we know if clicks are new
        button_3.wasClicked = button_3.isClicked and button_3.status == STARTED
        
        # *slider_2* updates
        
        # if slider_2 is starting this frame...
        if slider_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            slider_2.frameNStart = frameN  # exact frame index
            slider_2.tStart = t  # local t and not account for scr refresh
            slider_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'slider_2.started')
            # update status
            slider_2.status = STARTED
            slider_2.setAutoDraw(True)
        
        # if slider_2 is active this frame...
        if slider_2.status == STARTED:
            # update params
            pass
        
        # *text_22* updates
        
        # if text_22 is starting this frame...
        if text_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_22.frameNStart = frameN  # exact frame index
            text_22.tStart = t  # local t and not account for scr refresh
            text_22.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_22, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_22.started')
            # update status
            text_22.status = STARTED
            text_22.setAutoDraw(True)
        
        # if text_22 is active this frame...
        if text_22.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=yourGoal,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            yourGoal.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in yourGoal.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "yourGoal" ---
    for thisComponent in yourGoal.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for yourGoal
    yourGoal.tStop = globalClock.getTime(format='float')
    yourGoal.tStopRefresh = tThisFlipGlobal
    thisExp.addData('yourGoal.stopped', yourGoal.tStop)
    thisExp.addData('button_3.numClicks', button_3.numClicks)
    if button_3.numClicks:
       thisExp.addData('button_3.timesOn', button_3.timesOn)
       thisExp.addData('button_3.timesOff', button_3.timesOff)
    else:
       thisExp.addData('button_3.timesOn', "")
       thisExp.addData('button_3.timesOff', "")
    thisExp.addData('slider_2.response', slider_2.getRating())
    thisExp.addData('slider_2.rt', slider_2.getRT())
    thisExp.nextEntry()
    # the Routine "yourGoal" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "keyInstructions" ---
    # create an object to store info about Routine keyInstructions
    keyInstructions = data.Routine(
        name='keyInstructions',
        components=[text_20, button_5],
    )
    keyInstructions.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # reset button_5 to account for continued clicks & clear times on/off
    button_5.reset()
    # store start times for keyInstructions
    keyInstructions.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    keyInstructions.tStart = globalClock.getTime(format='float')
    keyInstructions.status = STARTED
    thisExp.addData('keyInstructions.started', keyInstructions.tStart)
    keyInstructions.maxDuration = None
    # keep track of which components have finished
    keyInstructionsComponents = keyInstructions.components
    for thisComponent in keyInstructions.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "keyInstructions" ---
    keyInstructions.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_20* updates
        
        # if text_20 is starting this frame...
        if text_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_20.frameNStart = frameN  # exact frame index
            text_20.tStart = t  # local t and not account for scr refresh
            text_20.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_20, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_20.started')
            # update status
            text_20.status = STARTED
            text_20.setAutoDraw(True)
        
        # if text_20 is active this frame...
        if text_20.status == STARTED:
            # update params
            pass
        # *button_5* updates
        
        # if button_5 is starting this frame...
        if button_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            button_5.frameNStart = frameN  # exact frame index
            button_5.tStart = t  # local t and not account for scr refresh
            button_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'button_5.started')
            # update status
            button_5.status = STARTED
            win.callOnFlip(button_5.buttonClock.reset)
            button_5.setAutoDraw(True)
        
        # if button_5 is active this frame...
        if button_5.status == STARTED:
            # update params
            pass
            # check whether button_5 has been pressed
            if button_5.isClicked:
                if not button_5.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    button_5.timesOn.append(button_5.buttonClock.getTime())
                    button_5.timesOff.append(button_5.buttonClock.getTime())
                elif len(button_5.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    button_5.timesOff[-1] = button_5.buttonClock.getTime()
                if not button_5.wasClicked:
                    # end routine when button_5 is clicked
                    continueRoutine = False
                if not button_5.wasClicked:
                    # run callback code when button_5 is clicked
                    pass
        # take note of whether button_5 was clicked, so that next frame we know if clicks are new
        button_5.wasClicked = button_5.isClicked and button_5.status == STARTED
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=keyInstructions,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            keyInstructions.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in keyInstructions.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "keyInstructions" ---
    for thisComponent in keyInstructions.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for keyInstructions
    keyInstructions.tStop = globalClock.getTime(format='float')
    keyInstructions.tStopRefresh = tThisFlipGlobal
    thisExp.addData('keyInstructions.stopped', keyInstructions.tStop)
    thisExp.addData('button_5.numClicks', button_5.numClicks)
    if button_5.numClicks:
       thisExp.addData('button_5.timesOn', button_5.timesOn)
       thisExp.addData('button_5.timesOff', button_5.timesOff)
    else:
       thisExp.addData('button_5.timesOn', "")
       thisExp.addData('button_5.timesOff', "")
    thisExp.nextEntry()
    # the Routine "keyInstructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "startTask" ---
    # create an object to store info about Routine startTask
    startTask = data.Routine(
        name='startTask',
        components=[text_4, button_4],
    )
    startTask.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # reset button_4 to account for continued clicks & clear times on/off
    button_4.reset()
    # store start times for startTask
    startTask.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    startTask.tStart = globalClock.getTime(format='float')
    startTask.status = STARTED
    thisExp.addData('startTask.started', startTask.tStart)
    startTask.maxDuration = None
    # keep track of which components have finished
    startTaskComponents = startTask.components
    for thisComponent in startTask.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "startTask" ---
    startTask.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        
        # if text_4 is starting this frame...
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_4.started')
            # update status
            text_4.status = STARTED
            text_4.setAutoDraw(True)
        
        # if text_4 is active this frame...
        if text_4.status == STARTED:
            # update params
            pass
        # *button_4* updates
        
        # if button_4 is starting this frame...
        if button_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            button_4.frameNStart = frameN  # exact frame index
            button_4.tStart = t  # local t and not account for scr refresh
            button_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'button_4.started')
            # update status
            button_4.status = STARTED
            win.callOnFlip(button_4.buttonClock.reset)
            button_4.setAutoDraw(True)
        
        # if button_4 is active this frame...
        if button_4.status == STARTED:
            # update params
            pass
            # check whether button_4 has been pressed
            if button_4.isClicked:
                if not button_4.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    button_4.timesOn.append(button_4.buttonClock.getTime())
                    button_4.timesOff.append(button_4.buttonClock.getTime())
                elif len(button_4.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    button_4.timesOff[-1] = button_4.buttonClock.getTime()
                if not button_4.wasClicked:
                    # end routine when button_4 is clicked
                    continueRoutine = False
                if not button_4.wasClicked:
                    # run callback code when button_4 is clicked
                    pass
        # take note of whether button_4 was clicked, so that next frame we know if clicks are new
        button_4.wasClicked = button_4.isClicked and button_4.status == STARTED
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=startTask,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            startTask.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in startTask.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "startTask" ---
    for thisComponent in startTask.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for startTask
    startTask.tStop = globalClock.getTime(format='float')
    startTask.tStopRefresh = tThisFlipGlobal
    thisExp.addData('startTask.stopped', startTask.tStop)
    thisExp.addData('button_4.numClicks', button_4.numClicks)
    if button_4.numClicks:
       thisExp.addData('button_4.timesOn', button_4.timesOn)
       thisExp.addData('button_4.timesOff', button_4.timesOff)
    else:
       thisExp.addData('button_4.timesOn', "")
       thisExp.addData('button_4.timesOff', "")
    thisExp.nextEntry()
    # the Routine "startTask" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    learningLoop = data.TrialHandler2(
        name='learningLoop',
        nReps=2.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(learningLoop)  # add the loop to the experiment
    thisLearningLoop = learningLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLearningLoop.rgb)
    if thisLearningLoop != None:
        for paramName in thisLearningLoop:
            globals()[paramName] = thisLearningLoop[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisLearningLoop in learningLoop:
        learningLoop.status = STARTED
        if hasattr(thisLearningLoop, 'status'):
            thisLearningLoop.status = STARTED
        currentLoop = learningLoop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisLearningLoop.rgb)
        if thisLearningLoop != None:
            for paramName in thisLearningLoop:
                globals()[paramName] = thisLearningLoop[paramName]
        
        # --- Prepare to start Routine "trial" ---
        # create an object to store info about Routine trial
        trial = data.Routine(
            name='trial',
            components=[slider, image_3, key_resp_2, text_slider_value],
        )
        trial.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        slider.reset()
        image_3.setImage('images/blank.png')
        # Run 'Begin Routine' code from code_2
        # Get the current trial from combined learning block
        # The loop nReps controls total trials - we use first nReps/2 from each block type
        # Get learning_block_index from globals (or initialize if first trial)
        learning_block_index = globals().get('learning_block_index', -1)
        learning_block_index += 1
        # Store in globals to persist across trials
        globals()['learning_block_index'] = learning_block_index
        
        # Calculate how many trials per block based on loop nReps
        # If loop nReps is 60, we want 30 gain + 30 loss
        total_trials = 120  # Default
        trials_per_block = 60  # Default
        
        try:
            # Try to get nReps from current loop
            if 'currentLoop' in locals() and hasattr(currentLoop, 'nReps'):
                if currentLoop.nReps is not None:
                    total_trials = int(currentLoop.nReps)
                    trials_per_block = total_trials // 2
                    print(f"Using loop nReps: {total_trials} total trials ({trials_per_block} per block)")
            elif 'learningLoop' in globals() and hasattr(learningLoop, 'nReps'):
                if learningLoop.nReps is not None:
                    total_trials = int(learningLoop.nReps)
                    trials_per_block = total_trials // 2
                    print(f"Using learningLoop nReps: {total_trials} total trials ({trials_per_block} per block)")
            else:
                # Fallback: use all available or default
                combined_learning_block_check = globals().get('combined_learning_block', [])
                if combined_learning_block_check:
                    total_trials = len(combined_learning_block_check)
                    trials_per_block = total_trials // 2
                    print(f"Using combined block length: {total_trials} total trials ({trials_per_block} per block)")
                else:
                    print(f"WARNING: Using default {total_trials} total trials ({trials_per_block} per block)")
        except Exception as e:
            print(f"Error getting nReps: {e}, using defaults")
            combined_learning_block_check = globals().get('combined_learning_block', [])
            if combined_learning_block_check:
                total_trials = len(combined_learning_block_check)
                trials_per_block = total_trials // 2
        
        # Build a limited combined block on-the-fly based on nReps
        # This ensures we use exactly nReps/2 from each block type
        # Store it globally so it persists across trials
        existing_limited = globals().get('limited_combined_block', [])
        combined_learning_block = globals().get('combined_learning_block', [])
        if 'limited_combined_block' not in globals() or len(existing_limited) != total_trials:
            print(f"DEBUG: Building limited block. learning_block_index={learning_block_index}, total_trials={total_trials}, existing_size={len(existing_limited)}")
            # First trial or not yet built - build the limited combined block
            if combined_learning_block and len(combined_learning_block) > 0:
                # The combined_learning_block is structured as: [first_block_all_trials, second_block_all_trials]
                # So we take first trials_per_block from the beginning (first block type)
                # Then we find where second block starts and take first trials_per_block from there
                
                first_block_type = combined_learning_block[0]["block"]
                second_block_type = "loss" if first_block_type == "gain" else "gain"
                
                # Find where first block ends and second block begins
                first_block_end = 0
                for i, trial_dict in enumerate(combined_learning_block):
                    if trial_dict["block"] != first_block_type:
                        first_block_end = i
                        break
                else:
                    # All trials are of first type (shouldn't happen, but handle it)
                    first_block_end = len(combined_learning_block)
                
                # Get first trials_per_block from first block (they're already at the start)
                first_block_trials = combined_learning_block[:min(trials_per_block, first_block_end)]
                
                # Get first trials_per_block from second block (starting from first_block_end)
                second_block_start = first_block_end
                second_block_trials = combined_learning_block[second_block_start:second_block_start + trials_per_block]
                
                # Create limited combined block and store globally
                limited_block = first_block_trials + second_block_trials
                globals()['limited_combined_block'] = limited_block
                globals()['total_trials'] = total_trials  # Store for reference
                print(f"Built limited block: {len(first_block_trials)} {first_block_type} + {len(second_block_trials)} {second_block_type} = {len(limited_block)} total (expected {total_trials})")
            else:
                # Fallback: use first total_trials from combined block
                if combined_learning_block:
                    globals()['limited_combined_block'] = combined_learning_block[:total_trials]
                    print(f"Built limited block from combined (fallback): {len(globals()['limited_combined_block'])} trials")
                else:
                    globals()['limited_combined_block'] = []
                    print(f"ERROR: No combined_learning_block available! Available globals: {[k for k in globals().keys() if 'block' in k.lower()]}")
        
        # Get the limited block (from globals)
        limited_combined_block = globals().get('limited_combined_block', [])
        
        # Get stored total_trials if available
        stored_total = globals().get('total_trials', total_trials)
        if stored_total != total_trials:
            total_trials = stored_total
            trials_per_block = total_trials // 2
        
        # Safety check - rebuild if empty or wrong size
        if not limited_combined_block or len(limited_combined_block) != total_trials:
            print(f"WARNING: Limited block mismatch. Expected {total_trials}, got {len(limited_combined_block) if limited_combined_block else 0}")
            # Rebuild if needed - get combined_learning_block from globals
            combined_learning_block = globals().get('combined_learning_block', [])
            if combined_learning_block and len(combined_learning_block) > 0:
                first_block_type = combined_learning_block[0]["block"]
                second_block_type = "loss" if first_block_type == "gain" else "gain"
                
                # Find where first block ends
                first_block_end = 0
                for i, trial_dict in enumerate(combined_learning_block):
                    if trial_dict["block"] != first_block_type:
                        first_block_end = i
                        break
                else:
                    first_block_end = len(combined_learning_block)
                
                # Get first trials_per_block from each block
                first_block_trials = combined_learning_block[:min(trials_per_block, first_block_end)]
                second_block_start = first_block_end
                second_block_trials = combined_learning_block[second_block_start:second_block_start + trials_per_block]
                
                limited_combined_block = first_block_trials + second_block_trials
                globals()['limited_combined_block'] = limited_combined_block
                globals()['total_trials'] = total_trials
                print(f"Rebuilt limited block: {len(first_block_trials)} {first_block_type} + {len(second_block_trials)} {second_block_type} = {len(limited_combined_block)} total")
        
        # Get current trial - ensure index is valid
        # learning_block_index starts at -1, increments to 0 for first trial, so we use it directly (not -1)
        if learning_block_index >= 0 and learning_block_index < len(limited_combined_block):
            current = limited_combined_block[learning_block_index]
            idx = learning_block_index + 1  # Display as 1-indexed for user
            block_type_str = current["block"].title()
            print(f"{block_type_str} trial {idx}/{total_trials}: {current['fruit']}")
        elif learning_block_index < total_trials:
            # Fallback to combined_learning_block if limited is empty
            combined_learning_block = globals().get('combined_learning_block', [])
            if learning_block_index >= 0 and learning_block_index < len(combined_learning_block):
                current = combined_learning_block[learning_block_index]
                idx = learning_block_index + 1  # Display as 1-indexed
                block_type_str = current["block"].title()
                print(f"{block_type_str} trial {idx}/{len(combined_learning_block)}: {current['fruit']} (using fallback from combined)")
            else:
                print(f"ERROR: Index {learning_block_index} out of range. Combined block has {len(combined_learning_block)} trials")
                current = {"fruit": "images/blank.png", "true_value": 0, "baseline": 0, "block": "unknown"}
                idx = 0
        else:
            # No more trials
            print(f"ERROR: Learning block exceeded. Index={learning_block_index}, Total={total_trials}, Limited block size={len(limited_combined_block) if limited_combined_block else 0}")
            current = {"fruit": "images/blank.png", "true_value": 0, "baseline": 0, "block": "unknown"}
            idx = 0
        
        # Assign trial values
        fruitFile = current["fruit"]
        trueVal   = current["true_value"]
        baselineR = current["baseline"]
        blockType = current["block"]
        
        print(f"Trial {idx}: {fruitFile}, value={trueVal}")
        
        # Clear any keys that were pressed in previous routines (like space from introScreen)
        try:
            event.clearEvents()
            print("DEBUG: Cleared key buffer at trial start")
        except:
            pass  # If event is not available, that's ok
        
        # Force hide the image initially to prevent ghost fruit, then show real fruit
        if 'image_3' in locals():
            image_3.opacity = 0
            image_3.setImage("images/blank.png")
            # Now set the real fruit image
            image_3.setImage(fruitFile)
            image_3.opacity = 1
            # Reset debug flag for EachFrame
            if hasattr(image_3, '_shown_debug'):
                del image_3._shown_debug
            print(f"DEBUG: BeginRoutine set image to {fruitFile} with opacity {image_3.opacity}")
        
        # Reset slider to 0 and ensure it's visible
        if 'slider' in locals():
            slider.reset()
            slider.setRating(0)  # Ensure it starts at 0
            print(f"Slider reset to 0")
        else:
            print("WARNING: Slider component not found!")
        
        # Initialize timing variables for response tracking
        import time
        trial_start_time = time.time()
        response_time = None
        trial_timed_out = False
        responded_in_time = False
        
        # Store in globals so EachFrame and EndRoutine can access them
        globals()['trial_start_time'] = trial_start_time
        globals()['response_time'] = None
        globals()['trial_timed_out'] = False
        globals()['responded_in_time'] = False
        
        # Log trial start for data logging
        try:
            data_logger = globals().get('data_logger', None)
            if data_logger:
                data_logger.start_trial(trial_start_time)
        except:
            pass
        
        # create starting attributes for key_resp_2
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        # store start times for trial
        trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        trial.tStart = globalClock.getTime(format='float')
        trial.status = STARTED
        thisExp.addData('trial.started', trial.tStart)
        trial.maxDuration = None
        # keep track of which components have finished
        trialComponents = trial.components
        for thisComponent in trial.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial" ---
        trial.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisLearningLoop, 'status') and thisLearningLoop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *slider* updates
            
            # if slider is starting this frame...
            if slider.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                slider.frameNStart = frameN  # exact frame index
                slider.tStart = t  # local t and not account for scr refresh
                slider.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider.started')
                # update status
                slider.status = STARTED
                slider.setAutoDraw(True)
            
            # if slider is active this frame...
            if slider.status == STARTED:
                # update params
                pass
            
            # *image_3* updates
            
            # if image_3 is starting this frame...
            if image_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image_3.frameNStart = frameN  # exact frame index
                image_3.tStart = t  # local t and not account for scr refresh
                image_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_3.started')
                # update status
                image_3.status = STARTED
                image_3.setAutoDraw(True)
            
            # if image_3 is active this frame...
            if image_3.status == STARTED:
                # update params
                pass
            # Run 'Each Frame' code from code_2
            # Show the fruit image - FORCE it to be visible
            if 'image_3' in locals() and fruitFile and fruitFile != 'images/blank.png' and fruitFile != '':
                # Set the image and make it visible every frame
                image_3.setImage(fruitFile)
                image_3.opacity = 1.0  # Force opacity to 1.0
                image_3.setAutoDraw(True)  # Force autodraw to ensure it's drawn
                # Debug: print once per trial that image is being shown
                if not hasattr(image_3, '_shown_debug'):
                    print(f"DEBUG: Showing image {fruitFile} with opacity {image_3.opacity}, autodraw={image_3.status}")
                    image_3._shown_debug = True
            elif 'image_3' in locals():
                image_3.opacity = 0
                image_3.setAutoDraw(False)
            
            # Display current slider value
            if 'slider' in locals():
                current_value = slider.getRating()
                # Update text display if it exists
                if 'text_slider_value' in locals():
                    text_slider_value.text = f"Current rating: {int(current_value)}"
                elif 'text_rating' in locals():
                    text_rating.text = f"Current rating: {int(current_value)}"
            
            # Handle keyboard input for slider controls
            # Using keys 1/2/3: 1 = left (decrease), 2 = continue, 3 = right (increase)
            try:
                keys = event.getKeys(keyList=['1', '2', '3', 'num_1', 'num_2', 'num_3'])
            except (NameError, AttributeError):
                keys = []
                if 'key_resp_2' in locals() and hasattr(key_resp_2, 'keys'):
                    if key_resp_2.keys and len(key_resp_2.keys) > 0:
                        keys = [key_resp_2.keys[0]]
                        key_resp_2.keys = []
            
            for key in keys:
                # Log keypress for data logging
                import time
                current_timestamp = time.time()
                try:
                    data_logger = globals().get('data_logger', None)
                    if data_logger:
                        data_logger.log_keypress(key, current_timestamp)
                except:
                    pass
                
                # Normalize key names (handle both '1' and 'num_1' formats)
                if key == 'num_1' or key == '1':
                    # Key 1: Move slider left by 5 points (allow negatives)
                    if 'slider' in locals():
                        current_rating = slider.getRating()
                        new_rating = current_rating - 5
                        slider.setRating(new_rating)
                        print(f"Slider moved left (key 1): {current_rating} -> {new_rating}")
                        
                elif key == 'num_3' or key == '3':
                    # Key 3: Move slider right by 5 points
                    if 'slider' in locals():
                        current_rating = slider.getRating()
                        new_rating = current_rating + 5
                        slider.setRating(new_rating)
                        print(f"Slider moved right (key 3): {current_rating} -> {new_rating}")
                        
                elif key == 'num_2' or key == '2':
                    # Key 2: Submit answer - calculate response time
                    import time
                    trial_start_time = globals().get('trial_start_time', time.time())
                    response_time = time.time() - trial_start_time
                    
                    # Get timeout threshold (from startTaskBeginExperiment or default)
                    try:
                        if 'TRIAL_TIMEOUT_SECONDS' in globals():
                            pass  # Use existing value
                        else:
                            TRIAL_TIMEOUT_SECONDS = 8.0  # Default
                    except:
                        TRIAL_TIMEOUT_SECONDS = 8.0  # Default
                    
                    if response_time <= TRIAL_TIMEOUT_SECONDS:
                        responded_in_time = True
                        trial_timed_out = False
                        print(f"Answer submitted (key 2) in {response_time:.2f} seconds (within {TRIAL_TIMEOUT_SECONDS}s limit)")
                    else:
                        # Shouldn't happen since we check timeout below, but just in case
                        responded_in_time = False
                        trial_timed_out = True
                        print(f"Answer submitted (key 2) in {response_time:.2f} seconds (over {TRIAL_TIMEOUT_SECONDS}s limit)")
                    
                    # Store in globals for EndRoutine
                    globals()['response_time'] = response_time
                    globals()['responded_in_time'] = responded_in_time
                    globals()['trial_timed_out'] = trial_timed_out
                    
                    continueRoutine = False
                    event.clearEvents()
                    break
            
            # Check for timeout - use config value
            try:
                import time
                
                # Get trial_start_time from globals
                trial_start_time = globals().get('trial_start_time', time.time())
                
                # Get timeout threshold (from startTaskBeginExperiment or default)
                try:
                    if 'TRIAL_TIMEOUT_SECONDS' in globals():
                        pass  # Use existing value
                    else:
                        TRIAL_TIMEOUT_SECONDS = 8.0  # Default
                except:
                    TRIAL_TIMEOUT_SECONDS = 8.0  # Default
                
                # Check if already responded
                responded_in_time = globals().get('responded_in_time', False)
                
                elapsed_time = time.time() - trial_start_time
                
                if elapsed_time >= TRIAL_TIMEOUT_SECONDS and not responded_in_time:
                    # Trial timed out
                    trial_timed_out = True
                    response_time = TRIAL_TIMEOUT_SECONDS
                    responded_in_time = False
                    
                    # Store in globals for EndRoutine
                    globals()['response_time'] = response_time
                    globals()['responded_in_time'] = responded_in_time
                    globals()['trial_timed_out'] = trial_timed_out
                    
                    print(f"Trial timed out at {TRIAL_TIMEOUT_SECONDS} seconds")
                    continueRoutine = False
                    event.clearEvents()
            except:
                pass
            
            # Alternative: Fallback to keyboard component method if event.getKeys() doesn't work
            # if 'key_resp_2' in locals():
            #     keys = getattr(key_resp_2, 'keys', None)
            #     if keys and len(keys) > 0:
            #         key = keys[0]
            #         if key == 'left' and 'slider' in locals():
            #             current_rating = slider.getRating()
            #             slider.setRating(max(0, current_rating - 5))
            #         elif key == 'right' and 'slider' in locals():
            #             current_rating = slider.getRating()
            #             slider.setRating(min(100, current_rating + 5))
            #         elif key == 'return' or key == 'space':
            #             continueRoutine = False
            #         key_resp_2.keys = []
            
            # Check if slider itself is being clicked (alternative submission method)
            if 'slider' in locals() and slider.getMouseResponses():
                # User clicked on slider to submit
                slider_responses = slider.getMouseResponses()
                if slider_responses:
                    print(f"Slider clicked to submit: {slider.getRating()}")
                    continueRoutine = False
            
            
            # *key_resp_2* updates
            waitOnFlip = False
            
            # if key_resp_2 is starting this frame...
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_2.started')
                # update status
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['left','right','return'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                    key_resp_2.duration = _key_resp_2_allKeys[-1].duration
            
            # *text_slider_value* updates
            
            # if text_slider_value is starting this frame...
            if text_slider_value.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_slider_value.frameNStart = frameN  # exact frame index
                text_slider_value.tStart = t  # local t and not account for scr refresh
                text_slider_value.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_slider_value, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_slider_value.started')
                # update status
                text_slider_value.status = STARTED
                text_slider_value.setAutoDraw(True)
            
            # if text_slider_value is active this frame...
            if text_slider_value.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=trial,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                trial.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trial.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for trial
        trial.tStop = globalClock.getTime(format='float')
        trial.tStopRefresh = tThisFlipGlobal
        thisExp.addData('trial.stopped', trial.tStop)
        learningLoop.addData('slider.response', slider.getRating())
        learningLoop.addData('slider.rt', slider.getRT())
        # Run 'End Routine' code from code_2
        rating = slider.getRating()
        rt = slider.getRT()
        
        # Get response_time, responded_in_time, and trial_timed_out from globals (set in EachFrame)
        response_time = globals().get('response_time', None)
        responded_in_time = globals().get('responded_in_time', False)
        trial_timed_out = globals().get('trial_timed_out', False)
        
        # Use response_time if available (from our tracking), otherwise use slider RT
        actual_response_time = response_time if response_time is not None else rt
        
        # Convert to milliseconds for logging
        reaction_time_ms = int(actual_response_time * 1000) if actual_response_time else 0
        
        print(f"Trial EndRoutine: RT={actual_response_time:.3f}s, responded_in_time={responded_in_time}, timed_out={trial_timed_out}")
        
        thisExp.addData("block", blockType)
        thisExp.addData("fruit", fruitFile)
        thisExp.addData("baseline", baselineR)
        thisExp.addData("true_value", trueVal)
        thisExp.addData("predicted", rating)
        thisExp.addData("predicted_rt", actual_response_time)
        thisExp.addData("responded_in_time", responded_in_time)
        thisExp.addData("trial_timed_out", trial_timed_out)
        
        # Log trial data
        try:
            # Extract fruit name from fruitFile (remove path and extension)
            # Use string operations instead of os.path for PsychoPy compatibility
            if fruitFile:
                # Handle both '/' and '\' path separators
                fruit_name = str(fruitFile).replace('\\', '/').split('/')[-1].replace('.png', '')
            else:
                fruit_name = "unknown"
            
            # Determine trial number within block (1-indexed)
            # learning_block_index is 0-indexed, so trial number = learning_block_index + 1
            # But we need trial number WITHIN the current block
            # Get learning_block_index from globals (should be set in BeginRoutine)
            learning_block_index = globals().get('learning_block_index', -1)
            limited_combined_block = globals().get('limited_combined_block', [])
            total_expected = globals().get('total_trials', 120)
            trials_per_block = total_expected // 2
            
            # Determine which block we're in based on learning_block_index
            if learning_block_index < trials_per_block:
                # First block
                trial_num_within_block = learning_block_index + 1
                block_id = 1 if blockType == "gain" else 2
                block_name = "rewards" if blockType == "gain" else "punishment"
            else:
                # Second block
                trial_num_within_block = (learning_block_index - trials_per_block) + 1
                block_id = 1 if blockType == "gain" else 2
                block_name = "rewards" if blockType == "gain" else "punishment"
            
            # Get data logger and log trial
            data_logger = globals().get('data_logger', None)
            if data_logger:
                data_logger.log_learning_trial(
                    trial_num=trial_num_within_block,
                    block_id=block_id,
                    block_name=block_name,
                    stimulus_identity=fruit_name,
                    stimulus_avg_points=baselineR,
                    actual_points=trueVal,
                    prediction_value=int(rating),
                    reaction_time_ms=reaction_time_ms,
                    responded_in_time=responded_in_time,
                    trial_timed_out=trial_timed_out
                )
        except Exception as e:
            print(f"Error logging trial data: {e}")
        
        # Calculate durations for subsequent routines and set text
        import random
        
        # Use timing config values (set in startTaskBeginExperiment or defaults)
        # Avoid os import to prevent conflicts with PsychoPy
        try:
            # Try to use values from startTaskBeginExperiment
            if 'TRIAL_TIMEOUT_SECONDS' in globals():
                pass  # Use existing values
            else:
                TRIAL_TIMEOUT_SECONDS = 8.0
                CROSSHAIR_RANDOM_VALUES = [2, 3, 4]
                TIMEOUT_SCREEN_DURATION = 1.5
                ACTUAL_POINTS_DURATION = 2.0
        except:
            # Fallback defaults
            TRIAL_TIMEOUT_SECONDS = 8.0
            CROSSHAIR_RANDOM_VALUES = [2, 3, 4]
            TIMEOUT_SCREEN_DURATION = 1.5
            ACTUAL_POINTS_DURATION = 2.0
        
        # Set actual_points_text here so it's available before actualPoints routine starts
        # Make sure trueVal exists first
        try:
            actual_points_text = f"Actual points: {trueVal:+d}"
        except:
            actual_points_text = "Actual points: 0"
        
        if responded_in_time and actual_response_time <= TRIAL_TIMEOUT_SECONDS:
            # Case 1: Responded in time (t <= TRIAL_TIMEOUT_SECONDS)
            rand1 = random.choice(CROSSHAIR_RANDOM_VALUES)
            crosshair1_duration = rand1 + (TRIAL_TIMEOUT_SECONDS - actual_response_time)
            actualPoints_duration = ACTUAL_POINTS_DURATION  # From config
            rand2 = random.choice(CROSSHAIR_RANDOM_VALUES)
            crosshair2_duration = rand2
            timeout_duration = 0  # No timeout screen
            
            # Log timing data
            thisExp.addData("crosshair1_rand", rand1)
            thisExp.addData("crosshair1_duration", crosshair1_duration)
            thisExp.addData("actualPoints_duration", actualPoints_duration)
            thisExp.addData("crosshair2_rand", rand2)
            thisExp.addData("crosshair2_duration", crosshair2_duration)
            thisExp.addData("timeout_duration", timeout_duration)
            
            print(f"Case 1: RT={actual_response_time:.2f}s")
            print(f"  rand1={rand1}, crosshair1={rand1} + ({TRIAL_TIMEOUT_SECONDS}-{actual_response_time:.2f}) = {crosshair1_duration:.2f}s")
            print(f"  actualPoints={ACTUAL_POINTS_DURATION}s (from config)")
            print(f"  rand2={rand2}, crosshair2={rand2}s")
        else:
            # Case 2: Timed out (t > TRIAL_TIMEOUT_SECONDS)
            timeout_duration = TIMEOUT_SCREEN_DURATION
            rand1 = random.choice(CROSSHAIR_RANDOM_VALUES)
            crosshair1_duration = max(0, rand1 - TIMEOUT_SCREEN_DURATION)  # Ensure non-negative
            actualPoints_duration = ACTUAL_POINTS_DURATION  # From config
            rand2 = random.choice(CROSSHAIR_RANDOM_VALUES)
            crosshair2_duration = rand2
            
            # Log timing data
            thisExp.addData("timeout_duration", timeout_duration)
            thisExp.addData("crosshair1_rand", rand1)
            thisExp.addData("crosshair1_duration", crosshair1_duration)
            thisExp.addData("actualPoints_duration", actualPoints_duration)
            thisExp.addData("crosshair2_rand", rand2)
            thisExp.addData("crosshair2_duration", crosshair2_duration)
            
            print(f"Case 2: Timeout at {TRIAL_TIMEOUT_SECONDS}s")
            print(f"  timeout={TIMEOUT_SCREEN_DURATION}s")
            print(f"  rand1={rand1}, crosshair1={rand1} - {TIMEOUT_SCREEN_DURATION} = {crosshair1_duration:.2f}s")
            print(f"  actualPoints={ACTUAL_POINTS_DURATION}s (from config)")
            print(f"  rand2={rand2}, crosshair2={rand2}s")
        
        # Check if we've completed the first block (halfway point)
        # This will trigger the transition screen before starting the second block
        # Get learning_block_index from globals (should be set in BeginRoutine)
        learning_block_index = globals().get('learning_block_index', -1)
        limited_combined_block = globals().get('limited_combined_block', [])
        total_expected = globals().get('total_trials', 120)
        trials_per_block = total_expected // 2
        
        # learning_block_index is 0-indexed and incremented at START of each trial
        # After completing the last trial of first block (trial #trials_per_block),
        # learning_block_index = trials_per_block - 1
        # At the end of that trial, we want to show transition screen
        # So we check if we just completed the last trial of the first block
        if learning_block_index == trials_per_block - 1:
            print(f"DEBUG: First block complete check - learning_block_index={learning_block_index}, trials_per_block={trials_per_block}")
            # We've just completed the first block - set flag to show transition screen
            globals()['show_block_transition'] = True
            
            # Save learning data for first block
            try:
                data_logger = globals().get('data_logger', None)
                if data_logger:
                    # Determine block name based on first block type
                    first_block_type = blockType if learning_block_index == 0 else None
                    if not first_block_type and limited_combined_block:
                        first_block_type = limited_combined_block[0]["block"]
                    block_name = "rewards" if first_block_type == "gain" else "punishment"
                    data_logger.save_learning_data(block_num=1, block_name=block_name)
            except Exception as e:
                print(f"Error saving first block data: {e}")
            
            print(f"First block complete! ({trials_per_block} trials) - Transition screen will appear next.")
        
        # Check if we've completed all learning trials
        # learning_block_index is 0-indexed and incremented at START of each trial
        # After completing the last trial (trial N where N = total_expected), 
        # learning_block_index = N - 1 = total_expected - 1
        # So we check if we've just completed the last trial
        print(f"DEBUG: Checking if all trials complete - learning_block_index={learning_block_index}, total_expected={total_expected}, condition={learning_block_index == total_expected - 1}")
        if learning_block_index == total_expected - 1:
            print(f"Learning trials complete. Completed {learning_block_index + 1}/{total_expected} trials.")
            
            # Save learning data for second block
            try:
                data_logger = globals().get('data_logger', None)
                if data_logger:
                    # Determine block name based on second block type
                    if limited_combined_block and len(limited_combined_block) > trials_per_block:
                        second_block_type = limited_combined_block[trials_per_block]["block"]
                        block_name = "rewards" if second_block_type == "gain" else "punishment"
                        print(f"Saving second block data: block_num=2, block_name={block_name}")
                        data_logger.save_learning_data(block_num=2, block_name=block_name)
                    else:
                        # Fallback: determine block name from current blockType
                        # Since we're in the second block, blockType should be the second block type
                        block_name = "rewards" if blockType == "gain" else "punishment"
                        print(f"Saving second block data (fallback): block_num=2, block_name={block_name}")
                        data_logger.save_learning_data(block_num=2, block_name=block_name)
            except Exception as e:
                print(f"Error saving second block data: {e}")
                import traceback
                traceback.print_exc()
            
            # End the loop (assuming loop is named learningLoop or similar)
            if 'learningLoop' in locals():
                learningLoop.finished = True
            elif 'currentLoop' in locals():
                currentLoop.finished = True
        
        
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
        learningLoop.addData('key_resp_2.keys',key_resp_2.keys)
        if key_resp_2.keys != None:  # we had a response
            learningLoop.addData('key_resp_2.rt', key_resp_2.rt)
            learningLoop.addData('key_resp_2.duration', key_resp_2.duration)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "timeout" ---
        # create an object to store info about Routine timeout
        timeout = data.Routine(
            name='timeout',
            components=[text_timeout],
        )
        timeout.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_7
        # Timeout screen - shows "Time out" message
        # Duration is exactly 1.5 seconds (set in Builder or dynamically)
        # Only show if timeout_duration > 0
        
        if 'timeout_duration' in locals() and timeout_duration > 0:
            if 'text_timeout' in locals():
                text_timeout.text = "Time out"
                text_timeout.opacity = 1
                text_timeout.setAutoDraw(True)
                print("Showing timeout screen")
            else:
                print("WARNING: text_timeout component not found!")
        else:
            # No timeout - skip this screen (duration should be 0)
            print("Skipping timeout screen (no timeout occurred)")
            if 'text_timeout' in locals():
                text_timeout.opacity = 0
        
        
        # store start times for timeout
        timeout.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        timeout.tStart = globalClock.getTime(format='float')
        timeout.status = STARTED
        thisExp.addData('timeout.started', timeout.tStart)
        timeout.maxDuration = None
        # keep track of which components have finished
        timeoutComponents = timeout.components
        for thisComponent in timeout.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "timeout" ---
        timeout.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisLearningLoop, 'status') and thisLearningLoop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_timeout* updates
            
            # if text_timeout is starting this frame...
            if text_timeout.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_timeout.frameNStart = frameN  # exact frame index
                text_timeout.tStart = t  # local t and not account for scr refresh
                text_timeout.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_timeout, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_timeout.started')
                # update status
                text_timeout.status = STARTED
                text_timeout.setAutoDraw(True)
            
            # if text_timeout is active this frame...
            if text_timeout.status == STARTED:
                # update params
                pass
            
            # if text_timeout is stopping this frame...
            if text_timeout.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_timeout.tStartRefresh + timeout_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    text_timeout.tStop = t  # not accounting for scr refresh
                    text_timeout.tStopRefresh = tThisFlipGlobal  # on global time
                    text_timeout.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_timeout.stopped')
                    # update status
                    text_timeout.status = FINISHED
                    text_timeout.setAutoDraw(False)
            # Run 'Each Frame' code from code_7
            # Timeout screen - just wait for duration
            pass
            
            
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=timeout,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                timeout.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in timeout.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "timeout" ---
        for thisComponent in timeout.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for timeout
        timeout.tStop = globalClock.getTime(format='float')
        timeout.tStopRefresh = tThisFlipGlobal
        thisExp.addData('timeout.stopped', timeout.tStop)
        # the Routine "timeout" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "crosshair1" ---
        # create an object to store info about Routine crosshair1
        crosshair1 = data.Routine(
            name='crosshair1',
            components=[text_13],
        )
        crosshair1.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_6
        # First crosshair screen - duration set dynamically based on trial response time
        # Duration is set in trialEndRoutine.py as crosshair1_duration
        # This routine will show a crosshair in the center of the screen
        
        # Make sure crosshair is visible (add a crosshair component in Builder)
        if 'crosshair' in locals():
            crosshair.opacity = 1
            crosshair.setAutoDraw(True)
        
        
        # store start times for crosshair1
        crosshair1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        crosshair1.tStart = globalClock.getTime(format='float')
        crosshair1.status = STARTED
        thisExp.addData('crosshair1.started', crosshair1.tStart)
        crosshair1.maxDuration = None
        # keep track of which components have finished
        crosshair1Components = crosshair1.components
        for thisComponent in crosshair1.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "crosshair1" ---
        crosshair1.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisLearningLoop, 'status') and thisLearningLoop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_13* updates
            
            # if text_13 is starting this frame...
            if text_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_13.frameNStart = frameN  # exact frame index
                text_13.tStart = t  # local t and not account for scr refresh
                text_13.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_13.started')
                # update status
                text_13.status = STARTED
                text_13.setAutoDraw(True)
            
            # if text_13 is active this frame...
            if text_13.status == STARTED:
                # update params
                pass
            
            # if text_13 is stopping this frame...
            if text_13.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_13.tStartRefresh + crosshair1_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    text_13.tStop = t  # not accounting for scr refresh
                    text_13.tStopRefresh = tThisFlipGlobal  # on global time
                    text_13.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_13.stopped')
                    # update status
                    text_13.status = FINISHED
                    text_13.setAutoDraw(False)
            # Run 'Each Frame' code from code_6
            # Crosshair screen - just wait for duration
            # Duration is controlled by PsychoPy Builder routine settings
            pass
            
            
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=crosshair1,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                crosshair1.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in crosshair1.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "crosshair1" ---
        for thisComponent in crosshair1.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for crosshair1
        crosshair1.tStop = globalClock.getTime(format='float')
        crosshair1.tStopRefresh = tThisFlipGlobal
        thisExp.addData('crosshair1.stopped', crosshair1.tStop)
        # the Routine "crosshair1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "actualPoints" ---
        # create an object to store info about Routine actualPoints
        actualPoints = data.Routine(
            name='actualPoints',
            components=[text_actual_points],
        )
        actualPoints.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_8
        # Actual points screen - shows the true value
        # Duration is set dynamically based on trial response time
        # IMPORTANT: In Builder, leave the Text component's text field BLANK - code will set it
        
        # Get trueVal and create the text
        actual_points_text = "Actual points: 0"  # Initialize first
        
        # Try to get trueVal from various sources
        if 'trueVal' in locals():
            actual_points_text = f"Actual points: {trueVal:+d}"
        elif 'trueVal' in globals():
            actual_points_text = f"Actual points: {trueVal:+d}"
        else:
            # Fallback: try to get from actual_points_text if it was set in trialEndRoutine
            try:
                if 'actual_points_text' in locals():
                    pass  # Use the value that exists
                else:
                    actual_points_text = "Actual points: 0"
            except:
                actual_points_text = "Actual points: 0"
        
        # Set the text component (DO NOT set text in Builder - leave it blank!)
        if 'text_actual_points' in locals():
            text_actual_points.text = actual_points_text
            text_actual_points.opacity = 1
            text_actual_points.setAutoDraw(True)
            print(f"Showing actual points: {actual_points_text}")
        else:
            print("WARNING: text_actual_points component not found!")
        
        
        # store start times for actualPoints
        actualPoints.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        actualPoints.tStart = globalClock.getTime(format='float')
        actualPoints.status = STARTED
        thisExp.addData('actualPoints.started', actualPoints.tStart)
        actualPoints.maxDuration = None
        # keep track of which components have finished
        actualPointsComponents = actualPoints.components
        for thisComponent in actualPoints.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "actualPoints" ---
        actualPoints.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisLearningLoop, 'status') and thisLearningLoop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_actual_points* updates
            
            # if text_actual_points is starting this frame...
            if text_actual_points.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_actual_points.frameNStart = frameN  # exact frame index
                text_actual_points.tStart = t  # local t and not account for scr refresh
                text_actual_points.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_actual_points, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_actual_points.started')
                # update status
                text_actual_points.status = STARTED
                text_actual_points.setAutoDraw(True)
            
            # if text_actual_points is active this frame...
            if text_actual_points.status == STARTED:
                # update params
                pass
            
            # if text_actual_points is stopping this frame...
            if text_actual_points.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_actual_points.tStartRefresh + actualPoints_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    text_actual_points.tStop = t  # not accounting for scr refresh
                    text_actual_points.tStopRefresh = tThisFlipGlobal  # on global time
                    text_actual_points.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_actual_points.stopped')
                    # update status
                    text_actual_points.status = FINISHED
                    text_actual_points.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=actualPoints,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                actualPoints.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in actualPoints.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "actualPoints" ---
        for thisComponent in actualPoints.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for actualPoints
        actualPoints.tStop = globalClock.getTime(format='float')
        actualPoints.tStopRefresh = tThisFlipGlobal
        thisExp.addData('actualPoints.stopped', actualPoints.tStop)
        # the Routine "actualPoints" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "crosshair2" ---
        # create an object to store info about Routine crosshair2
        crosshair2 = data.Routine(
            name='crosshair2',
            components=[text_14],
        )
        crosshair2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_9
        # Second crosshair screen - duration is random 2-4 seconds
        # Duration is set in trialEndRoutine.py as crosshair2_duration
        
        # Make sure crosshair is visible
        if 'crosshair' in locals():
            crosshair.opacity = 1
            crosshair.setAutoDraw(True)
        
        
        # store start times for crosshair2
        crosshair2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        crosshair2.tStart = globalClock.getTime(format='float')
        crosshair2.status = STARTED
        thisExp.addData('crosshair2.started', crosshair2.tStart)
        crosshair2.maxDuration = None
        # keep track of which components have finished
        crosshair2Components = crosshair2.components
        for thisComponent in crosshair2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "crosshair2" ---
        crosshair2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisLearningLoop, 'status') and thisLearningLoop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_14* updates
            
            # if text_14 is starting this frame...
            if text_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_14.frameNStart = frameN  # exact frame index
                text_14.tStart = t  # local t and not account for scr refresh
                text_14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_14, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_14.started')
                # update status
                text_14.status = STARTED
                text_14.setAutoDraw(True)
            
            # if text_14 is active this frame...
            if text_14.status == STARTED:
                # update params
                pass
            
            # if text_14 is stopping this frame...
            if text_14.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_14.tStartRefresh + crosshair2_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    text_14.tStop = t  # not accounting for scr refresh
                    text_14.tStopRefresh = tThisFlipGlobal  # on global time
                    text_14.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_14.stopped')
                    # update status
                    text_14.status = FINISHED
                    text_14.setAutoDraw(False)
            # Run 'Each Frame' code from code_9
            # Crosshair screen - just wait for duration
            pass
            
            
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=crosshair2,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                crosshair2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in crosshair2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "crosshair2" ---
        for thisComponent in crosshair2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for crosshair2
        crosshair2.tStop = globalClock.getTime(format='float')
        crosshair2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('crosshair2.stopped', crosshair2.tStop)
        # the Routine "crosshair2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "blockTransition" ---
        # create an object to store info about Routine blockTransition
        blockTransition = data.Routine(
            name='blockTransition',
            components=[text_block_transition, key_resp_transition],
        )
        blockTransition.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for key_resp_transition
        key_resp_transition.keys = []
        key_resp_transition.rt = []
        _key_resp_transition_allKeys = []
        # Run 'Begin Routine' code from code_16
        # Block transition screen - shown between first and second block
        # Shows "You completed the first block. Press 2 to move on to next block."
        
        # Check if we should show this screen (only after first block completes)
        show_block_transition = globals().get('show_block_transition', False)
        
        if not show_block_transition:
            # Don't show transition screen - skip this routine
            print("Skipping block transition screen (not needed at this time)")
            continueRoutine = False
        else:
            # Show the transition screen
            transitionText = "You completed the first block.\n\nPress 2 to move on to next block."
            
            # Set the text component (make sure component name matches your Builder setup)
            if 'text_block_transition' in locals():
                text_block_transition.text = transitionText
                text_block_transition.opacity = 1
                text_block_transition.setAutoDraw(True)
                print("Showing block transition screen")
            else:
                print("WARNING: text_block_transition component not found!")
            
            # Clear any previous key presses
            try:
                event.clearEvents()
            except:
                pass
        
        # store start times for blockTransition
        blockTransition.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        blockTransition.tStart = globalClock.getTime(format='float')
        blockTransition.status = STARTED
        thisExp.addData('blockTransition.started', blockTransition.tStart)
        blockTransition.maxDuration = None
        # keep track of which components have finished
        blockTransitionComponents = blockTransition.components
        for thisComponent in blockTransition.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blockTransition" ---
        blockTransition.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisLearningLoop, 'status') and thisLearningLoop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_block_transition* updates
            
            # if text_block_transition is starting this frame...
            if text_block_transition.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_block_transition.frameNStart = frameN  # exact frame index
                text_block_transition.tStart = t  # local t and not account for scr refresh
                text_block_transition.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_block_transition, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_block_transition.started')
                # update status
                text_block_transition.status = STARTED
                text_block_transition.setAutoDraw(True)
            
            # if text_block_transition is active this frame...
            if text_block_transition.status == STARTED:
                # update params
                pass
            
            # *key_resp_transition* updates
            waitOnFlip = False
            
            # if key_resp_transition is starting this frame...
            if key_resp_transition.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_transition.frameNStart = frameN  # exact frame index
                key_resp_transition.tStart = t  # local t and not account for scr refresh
                key_resp_transition.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_transition, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_transition.started')
                # update status
                key_resp_transition.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_transition.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_transition.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_transition.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_transition.getKeys(keyList=['2', 'num_2'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_transition_allKeys.extend(theseKeys)
                if len(_key_resp_transition_allKeys):
                    key_resp_transition.keys = _key_resp_transition_allKeys[-1].name  # just the last key pressed
                    key_resp_transition.rt = _key_resp_transition_allKeys[-1].rt
                    key_resp_transition.duration = _key_resp_transition_allKeys[-1].duration
            # Run 'Each Frame' code from code_16
            # Block transition screen - wait for key press 2 to continue
            
            # Only show if flag is set (double-check)
            show_block_transition = globals().get('show_block_transition', False)
            if not show_block_transition:
                continueRoutine = False
            else:
                # Check for key press 2 (or num_2)
                try:
                    keys = event.getKeys(keyList=['2', 'num_2'])
                    if '2' in keys or 'num_2' in keys:
                        # User pressed 2, continue to next block
                        print("Key 2 pressed - moving to next block")
                        # Reset the flag so it doesn't show again
                        globals()['show_block_transition'] = False
                        continueRoutine = False
                        event.clearEvents()
                except (NameError, AttributeError):
                    # Fallback: check keyboard component if event.getKeys doesn't work
                    if 'key_resp_transition' in locals() and hasattr(key_resp_transition, 'keys'):
                        if key_resp_transition.keys and len(key_resp_transition.keys) > 0:
                            key = key_resp_transition.keys[0]
                            if key == '2' or key == 'num_2':
                                print("Key 2 pressed (via keyboard component) - moving to next block")
                                # Reset the flag so it doesn't show again
                                globals()['show_block_transition'] = False
                                continueRoutine = False
                                key_resp_transition.keys = []
            
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=blockTransition,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                blockTransition.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blockTransition.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blockTransition" ---
        for thisComponent in blockTransition.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for blockTransition
        blockTransition.tStop = globalClock.getTime(format='float')
        blockTransition.tStopRefresh = tThisFlipGlobal
        thisExp.addData('blockTransition.stopped', blockTransition.tStop)
        # check responses
        if key_resp_transition.keys in ['', [], None]:  # No response was made
            key_resp_transition.keys = None
        learningLoop.addData('key_resp_transition.keys',key_resp_transition.keys)
        if key_resp_transition.keys != None:  # we had a response
            learningLoop.addData('key_resp_transition.rt', key_resp_transition.rt)
            learningLoop.addData('key_resp_transition.duration', key_resp_transition.duration)
        # the Routine "blockTransition" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisLearningLoop as finished
        if hasattr(thisLearningLoop, 'status'):
            thisLearningLoop.status = FINISHED
        # if awaiting a pause, pause now
        if learningLoop.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            learningLoop.status = STARTED
        thisExp.nextEntry()
        
    # completed 2.0 repeats of 'learningLoop'
    learningLoop.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "decisionPhase" ---
    # create an object to store info about Routine decisionPhase
    decisionPhase = data.Routine(
        name='decisionPhase',
        components=[text_5, key_resp_4],
    )
    decisionPhase.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_4
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # store start times for decisionPhase
    decisionPhase.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    decisionPhase.tStart = globalClock.getTime(format='float')
    decisionPhase.status = STARTED
    thisExp.addData('decisionPhase.started', decisionPhase.tStart)
    decisionPhase.maxDuration = None
    # keep track of which components have finished
    decisionPhaseComponents = decisionPhase.components
    for thisComponent in decisionPhase.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "decisionPhase" ---
    decisionPhase.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_5* updates
        
        # if text_5 is starting this frame...
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_5.started')
            # update status
            text_5.status = STARTED
            text_5.setAutoDraw(True)
        
        # if text_5 is active this frame...
        if text_5.status == STARTED:
            # update params
            pass
        
        # *key_resp_4* updates
        waitOnFlip = False
        
        # if key_resp_4 is starting this frame...
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_4.started')
            # update status
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['2', 'num2'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                key_resp_4.duration = _key_resp_4_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=decisionPhase,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            decisionPhase.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in decisionPhase.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "decisionPhase" ---
    for thisComponent in decisionPhase.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for decisionPhase
    decisionPhase.tStop = globalClock.getTime(format='float')
    decisionPhase.tStopRefresh = tThisFlipGlobal
    thisExp.addData('decisionPhase.stopped', decisionPhase.tStop)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    thisExp.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        thisExp.addData('key_resp_4.rt', key_resp_4.rt)
        thisExp.addData('key_resp_4.duration', key_resp_4.duration)
    thisExp.nextEntry()
    # the Routine "decisionPhase" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "decisionInstructions" ---
    # create an object to store info about Routine decisionInstructions
    decisionInstructions = data.Routine(
        name='decisionInstructions',
        components=[text_8, text_9, key_resp_5],
    )
    decisionInstructions.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_5
    key_resp_5.keys = []
    key_resp_5.rt = []
    _key_resp_5_allKeys = []
    # store start times for decisionInstructions
    decisionInstructions.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    decisionInstructions.tStart = globalClock.getTime(format='float')
    decisionInstructions.status = STARTED
    thisExp.addData('decisionInstructions.started', decisionInstructions.tStart)
    decisionInstructions.maxDuration = None
    # keep track of which components have finished
    decisionInstructionsComponents = decisionInstructions.components
    for thisComponent in decisionInstructions.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "decisionInstructions" ---
    decisionInstructions.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_8* updates
        
        # if text_8 is starting this frame...
        if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_8.frameNStart = frameN  # exact frame index
            text_8.tStart = t  # local t and not account for scr refresh
            text_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_8.started')
            # update status
            text_8.status = STARTED
            text_8.setAutoDraw(True)
        
        # if text_8 is active this frame...
        if text_8.status == STARTED:
            # update params
            pass
        
        # *text_9* updates
        
        # if text_9 is starting this frame...
        if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_9.frameNStart = frameN  # exact frame index
            text_9.tStart = t  # local t and not account for scr refresh
            text_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_9.started')
            # update status
            text_9.status = STARTED
            text_9.setAutoDraw(True)
        
        # if text_9 is active this frame...
        if text_9.status == STARTED:
            # update params
            pass
        
        # *key_resp_5* updates
        waitOnFlip = False
        
        # if key_resp_5 is starting this frame...
        if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.tStart = t  # local t and not account for scr refresh
            key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_5.started')
            # update status
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_5.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_5.getKeys(keyList=['2', 'num2'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_5_allKeys.extend(theseKeys)
            if len(_key_resp_5_allKeys):
                key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                key_resp_5.duration = _key_resp_5_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=decisionInstructions,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            decisionInstructions.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in decisionInstructions.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "decisionInstructions" ---
    for thisComponent in decisionInstructions.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for decisionInstructions
    decisionInstructions.tStop = globalClock.getTime(format='float')
    decisionInstructions.tStopRefresh = tThisFlipGlobal
    thisExp.addData('decisionInstructions.stopped', decisionInstructions.tStop)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys = None
    thisExp.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        thisExp.addData('key_resp_5.rt', key_resp_5.rt)
        thisExp.addData('key_resp_5.duration', key_resp_5.duration)
    thisExp.nextEntry()
    # the Routine "decisionInstructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "whichFruit" ---
    # create an object to store info about Routine whichFruit
    whichFruit = data.Routine(
        name='whichFruit',
        components=[text_10, key_resp_6],
    )
    whichFruit.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_6
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    # store start times for whichFruit
    whichFruit.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    whichFruit.tStart = globalClock.getTime(format='float')
    whichFruit.status = STARTED
    thisExp.addData('whichFruit.started', whichFruit.tStart)
    whichFruit.maxDuration = None
    # keep track of which components have finished
    whichFruitComponents = whichFruit.components
    for thisComponent in whichFruit.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "whichFruit" ---
    whichFruit.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_10* updates
        
        # if text_10 is starting this frame...
        if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_10.frameNStart = frameN  # exact frame index
            text_10.tStart = t  # local t and not account for scr refresh
            text_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_10.started')
            # update status
            text_10.status = STARTED
            text_10.setAutoDraw(True)
        
        # if text_10 is active this frame...
        if text_10.status == STARTED:
            # update params
            pass
        
        # *key_resp_6* updates
        waitOnFlip = False
        
        # if key_resp_6 is starting this frame...
        if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.tStart = t  # local t and not account for scr refresh
            key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_6.started')
            # update status
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_6.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_6.getKeys(keyList=['2', 'num2'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_6_allKeys.extend(theseKeys)
            if len(_key_resp_6_allKeys):
                key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                key_resp_6.duration = _key_resp_6_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=whichFruit,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            whichFruit.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in whichFruit.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "whichFruit" ---
    for thisComponent in whichFruit.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for whichFruit
    whichFruit.tStop = globalClock.getTime(format='float')
    whichFruit.tStopRefresh = tThisFlipGlobal
    thisExp.addData('whichFruit.stopped', whichFruit.tStop)
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys = None
    thisExp.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        thisExp.addData('key_resp_6.rt', key_resp_6.rt)
        thisExp.addData('key_resp_6.duration', key_resp_6.duration)
    thisExp.nextEntry()
    # the Routine "whichFruit" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    decisionLoop = data.TrialHandler2(
        name='decisionLoop',
        nReps=2.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(decisionLoop)  # add the loop to the experiment
    thisDecisionLoop = decisionLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisDecisionLoop.rgb)
    if thisDecisionLoop != None:
        for paramName in thisDecisionLoop:
            globals()[paramName] = thisDecisionLoop[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisDecisionLoop in decisionLoop:
        decisionLoop.status = STARTED
        if hasattr(thisDecisionLoop, 'status'):
            thisDecisionLoop.status = STARTED
        currentLoop = decisionLoop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisDecisionLoop.rgb)
        if thisDecisionLoop != None:
            for paramName in thisDecisionLoop:
                globals()[paramName] = thisDecisionLoop[paramName]
        
        # --- Prepare to start Routine "decisionStimulus1" ---
        # create an object to store info about Routine decisionStimulus1
        decisionStimulus1 = data.Routine(
            name='decisionStimulus1',
            components=[text_question, image_left1, image_right2],
        )
        decisionStimulus1.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_10
        # First stimulus screen - shows first fruit on its side for 2 seconds
        # Components: text_question, image_left1, image_right2
        
        # Get decision_index and decision_block from globals
        decision_index = globals().get('decision_index', 0)
        decision_block = globals().get('decision_block', [])
        
        if decision_block:
            # Use modulo to cycle through trials if needed
            trial_idx = decision_index % len(decision_block)
            current = decision_block[trial_idx]
            first_fruit = current["firstFruit"]
            first_side = current["firstSide"]
            
            # Show text
            if 'text_question' in locals():
                text_question.text = "Which option do you prefer?"
                text_question.opacity = 1
                text_question.setAutoDraw(True)
            
            # Show first fruit on its designated side
            if first_side == "left":
                if 'image_left1' in locals():
                    image_left1.setImage(first_fruit)
                    image_left1.opacity = 1
                    image_left1.setAutoDraw(True)
                if 'image_right2' in locals():
                    image_right2.opacity = 0
                    image_right2.setAutoDraw(False)
            else:  # right
                if 'image_right2' in locals():
                    image_right2.setImage(first_fruit)
                    image_right2.opacity = 1
                    image_right2.setAutoDraw(True)
                if 'image_left1' in locals():
                    image_left1.opacity = 0
                    image_left1.setAutoDraw(False)
            
            print(f"Decision {decision_index+1}: Showing {first_fruit} on {first_side} (2 seconds)")
        else:
            print("No more decision trials")
        
        
        # store start times for decisionStimulus1
        decisionStimulus1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        decisionStimulus1.tStart = globalClock.getTime(format='float')
        decisionStimulus1.status = STARTED
        thisExp.addData('decisionStimulus1.started', decisionStimulus1.tStart)
        decisionStimulus1.maxDuration = None
        # keep track of which components have finished
        decisionStimulus1Components = decisionStimulus1.components
        for thisComponent in decisionStimulus1.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "decisionStimulus1" ---
        decisionStimulus1.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # if trial has changed, end Routine now
            if hasattr(thisDecisionLoop, 'status') and thisDecisionLoop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_question* updates
            
            # if text_question is starting this frame...
            if text_question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_question.frameNStart = frameN  # exact frame index
                text_question.tStart = t  # local t and not account for scr refresh
                text_question.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_question, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_question.started')
                # update status
                text_question.status = STARTED
                text_question.setAutoDraw(True)
            
            # if text_question is active this frame...
            if text_question.status == STARTED:
                # update params
                pass
            
            # if text_question is stopping this frame...
            if text_question.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_question.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_question.tStop = t  # not accounting for scr refresh
                    text_question.tStopRefresh = tThisFlipGlobal  # on global time
                    text_question.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_question.stopped')
                    # update status
                    text_question.status = FINISHED
                    text_question.setAutoDraw(False)
            
            # *image_left1* updates
            
            # if image_left1 is starting this frame...
            if image_left1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_left1.frameNStart = frameN  # exact frame index
                image_left1.tStart = t  # local t and not account for scr refresh
                image_left1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_left1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_left1.started')
                # update status
                image_left1.status = STARTED
                image_left1.setAutoDraw(True)
            
            # if image_left1 is active this frame...
            if image_left1.status == STARTED:
                # update params
                pass
            
            # if image_left1 is stopping this frame...
            if image_left1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_left1.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    image_left1.tStop = t  # not accounting for scr refresh
                    image_left1.tStopRefresh = tThisFlipGlobal  # on global time
                    image_left1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_left1.stopped')
                    # update status
                    image_left1.status = FINISHED
                    image_left1.setAutoDraw(False)
            
            # *image_right2* updates
            
            # if image_right2 is starting this frame...
            if image_right2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_right2.frameNStart = frameN  # exact frame index
                image_right2.tStart = t  # local t and not account for scr refresh
                image_right2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_right2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_right2.started')
                # update status
                image_right2.status = STARTED
                image_right2.setAutoDraw(True)
            
            # if image_right2 is active this frame...
            if image_right2.status == STARTED:
                # update params
                pass
            
            # if image_right2 is stopping this frame...
            if image_right2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_right2.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    image_right2.tStop = t  # not accounting for scr refresh
                    image_right2.tStopRefresh = tThisFlipGlobal  # on global time
                    image_right2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_right2.stopped')
                    # update status
                    image_right2.status = FINISHED
                    image_right2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=decisionStimulus1,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                decisionStimulus1.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in decisionStimulus1.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "decisionStimulus1" ---
        for thisComponent in decisionStimulus1.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for decisionStimulus1
        decisionStimulus1.tStop = globalClock.getTime(format='float')
        decisionStimulus1.tStopRefresh = tThisFlipGlobal
        thisExp.addData('decisionStimulus1.stopped', decisionStimulus1.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if decisionStimulus1.maxDurationReached:
            routineTimer.addTime(-decisionStimulus1.maxDuration)
        elif decisionStimulus1.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # --- Prepare to start Routine "decisionITI1" ---
        # create an object to store info about Routine decisionITI1
        decisionITI1 = data.Routine(
            name='decisionITI1',
            components=[text_15],
        )
        decisionITI1.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_11
        # ITI 1 - Crosshair screen (random 1-3 seconds)
        # Component: text_15 (crosshair)
        import random
        
        # Hide previous text and fruits
        if 'text_question' in locals():
            text_question.opacity = 0
            text_question.setAutoDraw(False)
        
        if 'image_left1' in locals():
            image_left1.opacity = 0
            image_left1.setAutoDraw(False)
        
        if 'image_right2' in locals():
            image_right2.opacity = 0
            image_right2.setAutoDraw(False)
        
        # Show crosshair
        if 'text_15' in locals():
            text_15.text = "+"  # Crosshair symbol
            text_15.opacity = 1
            text_15.setAutoDraw(True)
        
        # Random duration: 1, 2, or 3 seconds
        iti1_duration = random.choice([1, 2, 3])
        print(f"ITI 1: {iti1_duration} seconds")
        
        
        # store start times for decisionITI1
        decisionITI1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        decisionITI1.tStart = globalClock.getTime(format='float')
        decisionITI1.status = STARTED
        thisExp.addData('decisionITI1.started', decisionITI1.tStart)
        decisionITI1.maxDuration = None
        # keep track of which components have finished
        decisionITI1Components = decisionITI1.components
        for thisComponent in decisionITI1.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "decisionITI1" ---
        decisionITI1.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisDecisionLoop, 'status') and thisDecisionLoop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_15* updates
            
            # if text_15 is starting this frame...
            if text_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_15.frameNStart = frameN  # exact frame index
                text_15.tStart = t  # local t and not account for scr refresh
                text_15.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_15, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_15.started')
                # update status
                text_15.status = STARTED
                text_15.setAutoDraw(True)
            
            # if text_15 is active this frame...
            if text_15.status == STARTED:
                # update params
                pass
            
            # if text_15 is stopping this frame...
            if text_15.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_15.tStartRefresh + iti1_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    text_15.tStop = t  # not accounting for scr refresh
                    text_15.tStopRefresh = tThisFlipGlobal  # on global time
                    text_15.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_15.stopped')
                    # update status
                    text_15.status = FINISHED
                    text_15.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=decisionITI1,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                decisionITI1.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in decisionITI1.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "decisionITI1" ---
        for thisComponent in decisionITI1.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for decisionITI1
        decisionITI1.tStop = globalClock.getTime(format='float')
        decisionITI1.tStopRefresh = tThisFlipGlobal
        thisExp.addData('decisionITI1.stopped', decisionITI1.tStop)
        # the Routine "decisionITI1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "decisionStimulus2" ---
        # create an object to store info about Routine decisionStimulus2
        decisionStimulus2 = data.Routine(
            name='decisionStimulus2',
            components=[text_question_2, image_left1_2, image_right2_2],
        )
        decisionStimulus2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_12
        # Second stimulus screen - shows second fruit on opposite side for 2 seconds
        # Components: text_question_2, image_left1_2, image_right2_2
        
        # Get decision_index and decision_block from globals
        decision_index = globals().get('decision_index', 0)
        decision_block = globals().get('decision_block', [])
        
        if decision_block:
            # Use modulo to cycle through trials if needed
            trial_idx = decision_index % len(decision_block)
            current = decision_block[trial_idx]
            second_fruit = current["secondFruit"]
            second_side = current["secondSide"]
            
            # Show text
            if 'text_question_2' in locals():
                text_question_2.text = "Which option do you prefer?"
                text_question_2.opacity = 1
                text_question_2.setAutoDraw(True)
            
            # Hide previous crosshair
            if 'text_15' in locals():
                text_15.opacity = 0
                text_15.setAutoDraw(False)
            
            # Show second fruit on its designated side
            if second_side == "left":
                if 'image_left1_2' in locals():
                    image_left1_2.setImage(second_fruit)
                    image_left1_2.opacity = 1
                    image_left1_2.setAutoDraw(True)
                if 'image_right2_2' in locals():
                    image_right2_2.opacity = 0
                    image_right2_2.setAutoDraw(False)
            else:  # right
                if 'image_right2_2' in locals():
                    image_right2_2.setImage(second_fruit)
                    image_right2_2.opacity = 1
                    image_right2_2.setAutoDraw(True)
                if 'image_left1_2' in locals():
                    image_left1_2.opacity = 0
                    image_left1_2.setAutoDraw(False)
            
            print(f"Decision {decision_index+1}: Showing {second_fruit} on {second_side} (2 seconds)")
        else:
            print("No more decision trials")
        
        
        # store start times for decisionStimulus2
        decisionStimulus2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        decisionStimulus2.tStart = globalClock.getTime(format='float')
        decisionStimulus2.status = STARTED
        thisExp.addData('decisionStimulus2.started', decisionStimulus2.tStart)
        decisionStimulus2.maxDuration = None
        # keep track of which components have finished
        decisionStimulus2Components = decisionStimulus2.components
        for thisComponent in decisionStimulus2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "decisionStimulus2" ---
        decisionStimulus2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # if trial has changed, end Routine now
            if hasattr(thisDecisionLoop, 'status') and thisDecisionLoop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_question_2* updates
            
            # if text_question_2 is starting this frame...
            if text_question_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_question_2.frameNStart = frameN  # exact frame index
                text_question_2.tStart = t  # local t and not account for scr refresh
                text_question_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_question_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_question_2.started')
                # update status
                text_question_2.status = STARTED
                text_question_2.setAutoDraw(True)
            
            # if text_question_2 is active this frame...
            if text_question_2.status == STARTED:
                # update params
                pass
            
            # if text_question_2 is stopping this frame...
            if text_question_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_question_2.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_question_2.tStop = t  # not accounting for scr refresh
                    text_question_2.tStopRefresh = tThisFlipGlobal  # on global time
                    text_question_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_question_2.stopped')
                    # update status
                    text_question_2.status = FINISHED
                    text_question_2.setAutoDraw(False)
            
            # *image_left1_2* updates
            
            # if image_left1_2 is starting this frame...
            if image_left1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_left1_2.frameNStart = frameN  # exact frame index
                image_left1_2.tStart = t  # local t and not account for scr refresh
                image_left1_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_left1_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_left1_2.started')
                # update status
                image_left1_2.status = STARTED
                image_left1_2.setAutoDraw(True)
            
            # if image_left1_2 is active this frame...
            if image_left1_2.status == STARTED:
                # update params
                pass
            
            # if image_left1_2 is stopping this frame...
            if image_left1_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_left1_2.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    image_left1_2.tStop = t  # not accounting for scr refresh
                    image_left1_2.tStopRefresh = tThisFlipGlobal  # on global time
                    image_left1_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_left1_2.stopped')
                    # update status
                    image_left1_2.status = FINISHED
                    image_left1_2.setAutoDraw(False)
            
            # *image_right2_2* updates
            
            # if image_right2_2 is starting this frame...
            if image_right2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_right2_2.frameNStart = frameN  # exact frame index
                image_right2_2.tStart = t  # local t and not account for scr refresh
                image_right2_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_right2_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_right2_2.started')
                # update status
                image_right2_2.status = STARTED
                image_right2_2.setAutoDraw(True)
            
            # if image_right2_2 is active this frame...
            if image_right2_2.status == STARTED:
                # update params
                pass
            
            # if image_right2_2 is stopping this frame...
            if image_right2_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_right2_2.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    image_right2_2.tStop = t  # not accounting for scr refresh
                    image_right2_2.tStopRefresh = tThisFlipGlobal  # on global time
                    image_right2_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_right2_2.stopped')
                    # update status
                    image_right2_2.status = FINISHED
                    image_right2_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=decisionStimulus2,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                decisionStimulus2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in decisionStimulus2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "decisionStimulus2" ---
        for thisComponent in decisionStimulus2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for decisionStimulus2
        decisionStimulus2.tStop = globalClock.getTime(format='float')
        decisionStimulus2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('decisionStimulus2.stopped', decisionStimulus2.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if decisionStimulus2.maxDurationReached:
            routineTimer.addTime(-decisionStimulus2.maxDuration)
        elif decisionStimulus2.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # --- Prepare to start Routine "decisionITI2" ---
        # create an object to store info about Routine decisionITI2
        decisionITI2 = data.Routine(
            name='decisionITI2',
            components=[text_16],
        )
        decisionITI2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_13
        # ITI 2 - Crosshair screen (random 1-3 seconds)
        # Component: text_16 (crosshair)
        import random
        
        # Hide previous text and fruits
        if 'text_question_2' in locals():
            text_question_2.opacity = 0
            text_question_2.setAutoDraw(False)
        
        if 'image_left1_2' in locals():
            image_left1_2.opacity = 0
            image_left1_2.setAutoDraw(False)
        
        if 'image_right2_2' in locals():
            image_right2_2.opacity = 0
            image_right2_2.setAutoDraw(False)
        
        # Show crosshair
        if 'text_16' in locals():
            text_16.text = "+"  # Crosshair symbol
            text_16.opacity = 1
            text_16.setAutoDraw(True)
        
        # Random duration: 1, 2, or 3 seconds
        iti2_duration = random.choice([1, 2, 3])
        print(f"ITI 2: {iti2_duration} seconds")
        
        
        # store start times for decisionITI2
        decisionITI2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        decisionITI2.tStart = globalClock.getTime(format='float')
        decisionITI2.status = STARTED
        thisExp.addData('decisionITI2.started', decisionITI2.tStart)
        decisionITI2.maxDuration = None
        # keep track of which components have finished
        decisionITI2Components = decisionITI2.components
        for thisComponent in decisionITI2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "decisionITI2" ---
        decisionITI2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisDecisionLoop, 'status') and thisDecisionLoop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_16* updates
            
            # if text_16 is starting this frame...
            if text_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_16.frameNStart = frameN  # exact frame index
                text_16.tStart = t  # local t and not account for scr refresh
                text_16.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_16, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_16.started')
                # update status
                text_16.status = STARTED
                text_16.setAutoDraw(True)
            
            # if text_16 is active this frame...
            if text_16.status == STARTED:
                # update params
                pass
            
            # if text_16 is stopping this frame...
            if text_16.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_16.tStartRefresh + iti2_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    text_16.tStop = t  # not accounting for scr refresh
                    text_16.tStopRefresh = tThisFlipGlobal  # on global time
                    text_16.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_16.stopped')
                    # update status
                    text_16.status = FINISHED
                    text_16.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=decisionITI2,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                decisionITI2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in decisionITI2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "decisionITI2" ---
        for thisComponent in decisionITI2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for decisionITI2
        decisionITI2.tStop = globalClock.getTime(format='float')
        decisionITI2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('decisionITI2.stopped', decisionITI2.tStop)
        # the Routine "decisionITI2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "decisionMaking" ---
        # create an object to store info about Routine decisionMaking
        decisionMaking = data.Routine(
            name='decisionMaking',
            components=[text_question_1, image_left_left, image_right_right, mouse_2],
        )
        decisionMaking.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # setup some python lists for storing info about the mouse_2
        mouse_2.x = []
        mouse_2.y = []
        mouse_2.leftButton = []
        mouse_2.midButton = []
        mouse_2.rightButton = []
        mouse_2.time = []
        gotValidClick = False  # until a click is received
        # Run 'Begin Routine' code from code_14
        # Decision phase - both fruits shown simultaneously (max 4 seconds)
        # Components: text_question_1, image_left_left, image_right_right, mouse_2
        import time
        
        # Get decision_index and decision_block from globals (ensure they persist)
        decision_index = globals().get('decision_index', 0)
        decision_block = globals().get('decision_block', [])
        
        # Use modulo to cycle through decision_block if needed (for when nReps > len(decision_block))
        if decision_block:
            # Use modulo to cycle through trials if we need more than available
            trial_idx = decision_index % len(decision_block)
            current = decision_block[trial_idx]
            leftFile  = current["leftFruit"]
            rightFile = current["rightFruit"]
            correct   = current["correct"]
            
            # Show text
            if 'text_question_1' in locals():
                text_question_1.text = "Which option do you prefer?"
                text_question_1.opacity = 1
                text_question_1.setAutoDraw(True)
            
            # Hide previous crosshair
            if 'text_16' in locals():
                text_16.opacity = 0
                text_16.setAutoDraw(False)
            
            # Set both images
            if 'image_left_left' in locals():
                image_left_left.setImage(leftFile)
                image_left_left.opacity = 1
                image_left_left.setAutoDraw(True)
            if 'image_right_right' in locals():
                image_right_right.setImage(rightFile)
                image_right_right.opacity = 1
                image_right_right.setAutoDraw(True)
            
            # Reset choice and start timer
            choice = ""
            decision_start_time = time.time()
            decision_timed_out = False
            
            # Store in globals for use in EachFrame
            globals()['choice'] = choice
            globals()['decision_start_time'] = decision_start_time
            globals()['decision_timed_out'] = False
            
            # Log decision start for data logging
            try:
                data_logger = globals().get('data_logger', None)
                if data_logger:
                    data_logger.start_decision(decision_start_time)
            except:
                pass
            
            # Clear any key presses from previous routines ONCE at the start
            # This prevents keys pressed during decisionStimulus1/2 or ITIs from being registered here
            try:
                event.clearEvents()
                print(f"Cleared key buffer at decision start")
            except:
                pass
            
            # Set a small ignore window to prevent immediate key registration (0.1 seconds)
            # This ensures keys pressed right before this routine started are ignored
            ignore_keys_until = decision_start_time + 0.1
            globals()['ignore_keys_until'] = ignore_keys_until
            
            if 'mouse_2' in locals():
                mouse_2.clickReset()
            print(f"Decision {decision_index+1}: {leftFile} vs {rightFile}, correct={correct}")
        else:
            # No more decision trials
            leftFile = "images/blank.png"
            rightFile = "images/blank.png"
            choice = ""
            print("No more decision trials available")
        
        # store start times for decisionMaking
        decisionMaking.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        decisionMaking.tStart = globalClock.getTime(format='float')
        decisionMaking.status = STARTED
        thisExp.addData('decisionMaking.started', decisionMaking.tStart)
        decisionMaking.maxDuration = None
        # keep track of which components have finished
        decisionMakingComponents = decisionMaking.components
        for thisComponent in decisionMaking.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "decisionMaking" ---
        decisionMaking.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 4.0:
            # if trial has changed, end Routine now
            if hasattr(thisDecisionLoop, 'status') and thisDecisionLoop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_question_1* updates
            
            # if text_question_1 is starting this frame...
            if text_question_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_question_1.frameNStart = frameN  # exact frame index
                text_question_1.tStart = t  # local t and not account for scr refresh
                text_question_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_question_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_question_1.started')
                # update status
                text_question_1.status = STARTED
                text_question_1.setAutoDraw(True)
            
            # if text_question_1 is active this frame...
            if text_question_1.status == STARTED:
                # update params
                pass
            
            # if text_question_1 is stopping this frame...
            if text_question_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_question_1.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    text_question_1.tStop = t  # not accounting for scr refresh
                    text_question_1.tStopRefresh = tThisFlipGlobal  # on global time
                    text_question_1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_question_1.stopped')
                    # update status
                    text_question_1.status = FINISHED
                    text_question_1.setAutoDraw(False)
            
            # *image_left_left* updates
            
            # if image_left_left is starting this frame...
            if image_left_left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_left_left.frameNStart = frameN  # exact frame index
                image_left_left.tStart = t  # local t and not account for scr refresh
                image_left_left.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_left_left, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_left_left.started')
                # update status
                image_left_left.status = STARTED
                image_left_left.setAutoDraw(True)
            
            # if image_left_left is active this frame...
            if image_left_left.status == STARTED:
                # update params
                pass
            
            # if image_left_left is stopping this frame...
            if image_left_left.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_left_left.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    image_left_left.tStop = t  # not accounting for scr refresh
                    image_left_left.tStopRefresh = tThisFlipGlobal  # on global time
                    image_left_left.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_left_left.stopped')
                    # update status
                    image_left_left.status = FINISHED
                    image_left_left.setAutoDraw(False)
            
            # *image_right_right* updates
            
            # if image_right_right is starting this frame...
            if image_right_right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_right_right.frameNStart = frameN  # exact frame index
                image_right_right.tStart = t  # local t and not account for scr refresh
                image_right_right.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_right_right, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_right_right.started')
                # update status
                image_right_right.status = STARTED
                image_right_right.setAutoDraw(True)
            
            # if image_right_right is active this frame...
            if image_right_right.status == STARTED:
                # update params
                pass
            
            # if image_right_right is stopping this frame...
            if image_right_right.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_right_right.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    image_right_right.tStop = t  # not accounting for scr refresh
                    image_right_right.tStopRefresh = tThisFlipGlobal  # on global time
                    image_right_right.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_right_right.stopped')
                    # update status
                    image_right_right.status = FINISHED
                    image_right_right.setAutoDraw(False)
            # *mouse_2* updates
            
            # if mouse_2 is starting this frame...
            if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_2.frameNStart = frameN  # exact frame index
                mouse_2.tStart = t  # local t and not account for scr refresh
                mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouse_2.started', t)
                # update status
                mouse_2.status = STARTED
                mouse_2.mouseClock.reset()
                prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
            
            # if mouse_2 is stopping this frame...
            if mouse_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > mouse_2.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    mouse_2.tStop = t  # not accounting for scr refresh
                    mouse_2.tStopRefresh = tThisFlipGlobal  # on global time
                    mouse_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.addData('mouse_2.stopped', t)
                    # update status
                    mouse_2.status = FINISHED
            if mouse_2.status == STARTED:  # only update if started and not finished!
                buttons = mouse_2.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        pass
                        x, y = mouse_2.getPos()
                        mouse_2.x.append(x)
                        mouse_2.y.append(y)
                        buttons = mouse_2.getPressed()
                        mouse_2.leftButton.append(buttons[0])
                        mouse_2.midButton.append(buttons[1])
                        mouse_2.rightButton.append(buttons[2])
                        mouse_2.time.append(mouse_2.mouseClock.getTime())
                        
                        continueRoutine = False  # end routine on response
            # Run 'Each Frame' code from code_14
            # Decision phase - check for response (max 4 seconds)
            # Using keys 1/3: 1 = left image, 3 = right image
            import time
            
            # Get decision_start_time and ignore_keys_until from globals (set in BeginRoutine)
            decision_start_time = globals().get('decision_start_time', time.time())
            ignore_keys_until = globals().get('ignore_keys_until', decision_start_time + 0.1)
            
            # Check for timeout (4 seconds max)
            try:
                elapsed_time = time.time() - decision_start_time
                
                if elapsed_time >= 4.0:
                    # Timeout - no response
                    choice = ""
                    decision_rt = 4.0
                    decision_timed_out = True
                    # Store in globals for EndRoutine
                    globals()['decision_timed_out'] = True
                    globals()['decision_rt'] = 4.0
                    print(f"Decision {decision_index+1}: Timeout at 4.0 seconds")
                    continueRoutine = False
            except:
                decision_timed_out = False
            
            # Only check for keys if we're past the ignore window AND not timed out
            if not decision_timed_out:
                current_time = time.time()
                if current_time >= ignore_keys_until:
                    # Check for keyboard input (keys 1 or 3)
                    try:
                        keys = event.getKeys(keyList=['1', '3', 'num_1', 'num_3'])
                        for key in keys:
                            # Normalize key names (handle both '1' and 'num_1' formats)
                            if key == 'num_1' or key == '1':
                                # Key 1: Choose left image
                                choice = "left"
                                decision_rt = time.time() - decision_start_time
                                decision_timed_out = False
                                # Store in globals
                                globals()['choice'] = choice
                                globals()['decision_rt'] = decision_rt
                                globals()['decision_timed_out'] = False
                                print(f"Decision {decision_index+1}: Chose left (key 1, RT={decision_rt:.2f}s)")
                                continueRoutine = False
                                # Clear events after processing
                                try:
                                    event.clearEvents()
                                except:
                                    pass
                                break
                            elif key == 'num_3' or key == '3':
                                # Key 3: Choose right image
                                choice = "right"
                                decision_rt = time.time() - decision_start_time
                                decision_timed_out = False
                                # Store in globals
                                globals()['choice'] = choice
                                globals()['decision_rt'] = decision_rt
                                globals()['decision_timed_out'] = False
                                print(f"Decision {decision_index+1}: Chose right (key 3, RT={decision_rt:.2f}s)")
                                continueRoutine = False
                                # Clear events after processing
                                try:
                                    event.clearEvents()
                                except:
                                    pass
                                break
                    except (NameError, AttributeError):
                        # Fallback: Check for mouse click (using mouse_2 and correct image components)
                        if 'mouse_2' in locals() and 'image_left_left' in locals() and 'image_right_right' in locals():
                            if mouse_2.isPressedIn(image_left_left):
                                choice = "left"
                                decision_rt = time.time() - decision_start_time
                                decision_timed_out = False
                                globals()['choice'] = choice
                                globals()['decision_rt'] = decision_rt
                                globals()['decision_timed_out'] = False
                                print(f"Decision {decision_index+1}: Chose left (mouse, RT={decision_rt:.2f}s)")
                                continueRoutine = False
                            elif mouse_2.isPressedIn(image_right_right):
                                choice = "right"
                                decision_rt = time.time() - decision_start_time
                                decision_timed_out = False
                                globals()['choice'] = choice
                                globals()['decision_rt'] = decision_rt
                                globals()['decision_timed_out'] = False
                                print(f"Decision {decision_index+1}: Chose right (mouse, RT={decision_rt:.2f}s)")
                                continueRoutine = False
            
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=decisionMaking,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                decisionMaking.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in decisionMaking.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "decisionMaking" ---
        for thisComponent in decisionMaking.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for decisionMaking
        decisionMaking.tStop = globalClock.getTime(format='float')
        decisionMaking.tStopRefresh = tThisFlipGlobal
        thisExp.addData('decisionMaking.stopped', decisionMaking.tStop)
        # store data for decisionLoop (TrialHandler)
        decisionLoop.addData('mouse_2.x', mouse_2.x)
        decisionLoop.addData('mouse_2.y', mouse_2.y)
        decisionLoop.addData('mouse_2.leftButton', mouse_2.leftButton)
        decisionLoop.addData('mouse_2.midButton', mouse_2.midButton)
        decisionLoop.addData('mouse_2.rightButton', mouse_2.rightButton)
        decisionLoop.addData('mouse_2.time', mouse_2.time)
        # Run 'End Routine' code from code_14
        # Get decision_index and decision_block from globals
        decision_index = globals().get('decision_index', 0)
        decision_block = globals().get('decision_block', [])
        
        # Get choice, decision_rt, and decision_timed_out from globals (set in EachFrame)
        choice = globals().get('choice', "")
        decision_rt = globals().get('decision_rt', 4.0)
        decision_timed_out = globals().get('decision_timed_out', False)
        
        # Get leftFile and rightFile from current trial
        if decision_block:
            trial_idx = decision_index % len(decision_block)
            current = decision_block[trial_idx]
            leftFile = current.get("leftFruit", "images/blank.png")
            rightFile = current.get("rightFruit", "images/blank.png")
            correct = current.get("correct", "")
        else:
            leftFile = "images/blank.png"
            rightFile = "images/blank.png"
            correct = ""
        
        # Determine correctness
        was_correct = (choice == correct) if choice else False
        
        # Convert reaction time to milliseconds
        decision_rt_value = decision_rt if decision_rt is not None else 4.0
        decision_rt_ms = int(decision_rt_value * 1000)
        
        # Calculate timeout duration for timeout screen (1.5 seconds if timed out, 0 otherwise)
        decision_timeout_duration = 1.5 if decision_timed_out else 0.0
        globals()['decision_timeout_duration'] = decision_timeout_duration
        
        # Log the decision data
        thisExp.addData("decision_trial", decision_index + 1)
        thisExp.addData("leftFruit", leftFile)
        thisExp.addData("rightFruit", rightFile)
        thisExp.addData("choice", choice)
        thisExp.addData("correctSide", correct)
        thisExp.addData("was_correct", was_correct)
        thisExp.addData("decision_rt", decision_rt_value)
        thisExp.addData("decision_timed_out", decision_timed_out)
        thisExp.addData("decision_timeout_duration", decision_timeout_duration)
        
        # Log decision trial to CSV
        try:
            # Extract fruit names from file paths
            # Use string operations instead of os.path for PsychoPy compatibility
            if leftFile:
                left_fruit_name = str(leftFile).replace('\\', '/').split('/')[-1].replace('.png', '')
            else:
                left_fruit_name = "unknown"
            
            if rightFile:
                right_fruit_name = str(rightFile).replace('\\', '/').split('/')[-1].replace('.png', '')
            else:
                right_fruit_name = "unknown"
            
            # Get fruit numerical IDs
            fruit_to_num = globals().get('fruit_to_num', {})
            left_stimulus_num = fruit_to_num.get(left_fruit_name, 0)
            right_stimulus_num = fruit_to_num.get(right_fruit_name, 0)
            
            # Get fruit average points (baselines)
            # We need to get these from the fruit_values or decision_block
            decision_block = globals().get('decision_block', [])
            left_avg = 0
            right_avg = 0
            if decision_block:
                # Use modulo to get the correct trial (cycles if needed)
                trial_idx = decision_index % len(decision_block)
                current = decision_block[trial_idx]
                left_avg = current.get('leftVal', 0)
                right_avg = current.get('rightVal', 0)
            
            # Determine block ID (1=before showing points explicitly, 2=after showing points explicitly)
            # For now, we'll use 1 as default (you can modify this based on your experiment structure)
            block_id = 1  # TODO: Update this based on your experiment structure
            block_name = "implicit"  # TODO: Update this based on your experiment structure
            
            # Determine choice as numerical ID (left_stimulus_num or right_stimulus_num)
            # The choice should be the numerical ID of the chosen fruit
            choice_num = left_stimulus_num if choice == "left" else (right_stimulus_num if choice == "right" else "")
            
            # Get data logger and log decision
            data_logger = globals().get('data_logger', None)
            if data_logger:
                data_logger.log_decision_trial(
                    trial_num=decision_index + 1,
                    block_id=block_id,
                    block_name=block_name,
                    left_stimulus_id=left_fruit_name,
                    right_stimulus_id=right_fruit_name,
                    left_stimulus_num=left_stimulus_num,
                    right_stimulus_num=right_stimulus_num,
                    left_avg_points=left_avg,
                    right_avg_points=right_avg,
                    choice=choice_num if choice_num else "",
                    reaction_time_ms=decision_rt_ms
                )
        except Exception as e:
            print(f"Error logging decision data: {e}")
        
        # Calculate ITI 3 duration: (4 - response_time) + rand(1,2,3)
        # If timed out, subtract timeout duration from ITI
        # Set this BEFORE decisionITI3 routine starts so it's available for Builder duration
        import random
        response_time = decision_rt_value
        rand3 = random.choice([1, 2, 3])
        
        if decision_timed_out:
            # If timed out, subtract timeout duration (1.5s) from ITI
            # Ensure ITI is non-negative
            iti3_duration = max(0, (4.0 - response_time) + rand3 - decision_timeout_duration)
        else:
            # Normal case: (4 - response_time) + rand(1,2,3)
            iti3_duration = (4.0 - response_time) + rand3
        
        # Ensure iti3_duration is in globals so Builder can access it
        if 'iti3_duration' not in globals():
            globals()['iti3_duration'] = iti3_duration
        
        print(f"ITI 3: (4 - {response_time:.2f}) + {rand3} = {iti3_duration:.2f} seconds (timeout: {decision_timed_out})")
        
        # Log ITI durations
        iti1_duration = globals().get('iti1_duration', 0)
        iti2_duration = globals().get('iti2_duration', 0)
        thisExp.addData("iti1_duration", iti1_duration)
        thisExp.addData("iti2_duration", iti2_duration)
        thisExp.addData("iti3_duration", iti3_duration)
        thisExp.addData("decision_response_time", response_time)
        
        print(f"Decision {decision_index + 1}: {choice} (correct: {correct}, accurate: {was_correct}, RT: {response_time:.2f}s)")
        
        # Move to next trial
        decision_index += 1
        # Store in globals to ensure it persists
        globals()['decision_index'] = decision_index
        
        # Check if we're done with decision trials
        # IMPORTANT: Let PsychoPy loop's nReps control when to stop
        # Only end the loop if we've reached the loop's nReps OR run out of decision_block trials
        decision_block = globals().get('decision_block', [])
        total_decision_trials = len(decision_block)
        
        # Get loop nReps to determine when to stop
        loop_nReps = None
        try:
            if 'currentLoop' in locals() and hasattr(currentLoop, 'nReps') and currentLoop.nReps:
                loop_nReps = int(currentLoop.nReps)
            elif 'decisionLoop' in globals() and hasattr(decisionLoop, 'nReps') and decisionLoop.nReps:
                loop_nReps = int(decisionLoop.nReps)
        except:
            pass
        
        # Only end loop if we've reached nReps OR run out of decision_block trials
        # Don't end prematurely - let the loop run for nReps iterations
        should_end = False
        if loop_nReps is not None:
            # End when we've completed the number of trials specified by nReps
            if decision_index >= loop_nReps:
                print(f"Decision loop complete: {decision_index}/{loop_nReps} trials completed (nReps reached)")
                should_end = True
            elif decision_index >= total_decision_trials:
                # Ran out of decision_block trials before reaching nReps
                print(f"WARNING: Ran out of decision_block trials ({total_decision_trials}) before reaching nReps ({loop_nReps})")
                should_end = True
        else:
            # Fallback: check against decision_block length if nReps not available
            if decision_index >= total_decision_trials:
                print(f"All decision_block trials complete ({total_decision_trials} trials)")
                should_end = True
        
        # Only end and save if we should
        if should_end:
            # Save decision data before ending
            try:
                data_logger = globals().get('data_logger', None)
                if data_logger:
                    block_num = 3  # TODO: Update based on your experiment structure
                    block_name = "implicit"  # TODO: Update based on your experiment structure
                    data_logger.save_decision_data(block_num=block_num, block_name=block_name)
            except Exception as e:
                print(f"Error saving decision data: {e}")
            
            # Only end the loop if we should
            if 'decisionLoop' in locals():
                decisionLoop.finished = True
            elif 'currentLoop' in locals():
                currentLoop.finished = True
        
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if decisionMaking.maxDurationReached:
            routineTimer.addTime(-decisionMaking.maxDuration)
        elif decisionMaking.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-4.000000)
        
        # --- Prepare to start Routine "decisionTimeout" ---
        # create an object to store info about Routine decisionTimeout
        decisionTimeout = data.Routine(
            name='decisionTimeout',
            components=[text_decision_timeout],
        )
        decisionTimeout.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_17
        # Decision timeout screen - shows "Time out" message
        # Duration is exactly 1.5 seconds (set in Builder or dynamically)
        # Only show if decision_timeout_duration > 0
        
        decision_timeout_duration = globals().get('decision_timeout_duration', 0)
        
        if decision_timeout_duration > 0:
            if 'text_decision_timeout' in locals():
                text_decision_timeout.text = "Time out"
                text_decision_timeout.opacity = 1
                text_decision_timeout.setAutoDraw(True)
                print("Showing decision timeout screen")
            else:
                print("WARNING: text_decision_timeout component not found!")
        else:
            # No timeout - skip this screen (duration should be 0)
            print("Skipping decision timeout screen (no timeout occurred)")
            if 'text_decision_timeout' in locals():
                text_decision_timeout.opacity = 0
        
        
        # store start times for decisionTimeout
        decisionTimeout.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        decisionTimeout.tStart = globalClock.getTime(format='float')
        decisionTimeout.status = STARTED
        thisExp.addData('decisionTimeout.started', decisionTimeout.tStart)
        decisionTimeout.maxDuration = None
        # keep track of which components have finished
        decisionTimeoutComponents = decisionTimeout.components
        for thisComponent in decisionTimeout.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "decisionTimeout" ---
        decisionTimeout.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.5:
            # if trial has changed, end Routine now
            if hasattr(thisDecisionLoop, 'status') and thisDecisionLoop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_decision_timeout* updates
            
            # if text_decision_timeout is starting this frame...
            if text_decision_timeout.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_decision_timeout.frameNStart = frameN  # exact frame index
                text_decision_timeout.tStart = t  # local t and not account for scr refresh
                text_decision_timeout.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_decision_timeout, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_decision_timeout.started')
                # update status
                text_decision_timeout.status = STARTED
                text_decision_timeout.setAutoDraw(True)
            
            # if text_decision_timeout is active this frame...
            if text_decision_timeout.status == STARTED:
                # update params
                pass
            
            # if text_decision_timeout is stopping this frame...
            if text_decision_timeout.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_decision_timeout.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_decision_timeout.tStop = t  # not accounting for scr refresh
                    text_decision_timeout.tStopRefresh = tThisFlipGlobal  # on global time
                    text_decision_timeout.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_decision_timeout.stopped')
                    # update status
                    text_decision_timeout.status = FINISHED
                    text_decision_timeout.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=decisionTimeout,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                decisionTimeout.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in decisionTimeout.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "decisionTimeout" ---
        for thisComponent in decisionTimeout.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for decisionTimeout
        decisionTimeout.tStop = globalClock.getTime(format='float')
        decisionTimeout.tStopRefresh = tThisFlipGlobal
        thisExp.addData('decisionTimeout.stopped', decisionTimeout.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if decisionTimeout.maxDurationReached:
            routineTimer.addTime(-decisionTimeout.maxDuration)
        elif decisionTimeout.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.500000)
        
        # --- Prepare to start Routine "decisionITI3" ---
        # create an object to store info about Routine decisionITI3
        decisionITI3 = data.Routine(
            name='decisionITI3',
            components=[text_17],
        )
        decisionITI3.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_15
        # ITI 3 - Crosshair screen (duration: (4 - response_time) + rand(1,2,3))
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
            globals()['iti3_duration'] = iti3_duration
        
        # Hide previous text and fruits
        if 'text_question_1' in locals():
            text_question_1.opacity = 0
            text_question_1.setAutoDraw(False)
        
        if 'image_left_left' in locals():
            image_left_left.opacity = 0
            image_left_left.setAutoDraw(False)
        
        if 'image_right_right' in locals():
            image_right_right.opacity = 0
            image_right_right.setAutoDraw(False)
        
        # Show crosshair
        if 'text_17' in locals():
            text_17.text = "+"  # Crosshair symbol
            text_17.opacity = 1
            text_17.setAutoDraw(True)
        
        print(f"Showing ITI 3 crosshair (duration: {iti3_duration if 'iti3_duration' in locals() or 'iti3_duration' in globals() else 'unknown'}s)")
        
        
        # store start times for decisionITI3
        decisionITI3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        decisionITI3.tStart = globalClock.getTime(format='float')
        decisionITI3.status = STARTED
        thisExp.addData('decisionITI3.started', decisionITI3.tStart)
        decisionITI3.maxDuration = None
        # keep track of which components have finished
        decisionITI3Components = decisionITI3.components
        for thisComponent in decisionITI3.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "decisionITI3" ---
        decisionITI3.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisDecisionLoop, 'status') and thisDecisionLoop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_17* updates
            
            # if text_17 is starting this frame...
            if text_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_17.frameNStart = frameN  # exact frame index
                text_17.tStart = t  # local t and not account for scr refresh
                text_17.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_17, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_17.started')
                # update status
                text_17.status = STARTED
                text_17.setAutoDraw(True)
            
            # if text_17 is active this frame...
            if text_17.status == STARTED:
                # update params
                pass
            
            # if text_17 is stopping this frame...
            if text_17.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_17.tStartRefresh + iti3_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    text_17.tStop = t  # not accounting for scr refresh
                    text_17.tStopRefresh = tThisFlipGlobal  # on global time
                    text_17.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_17.stopped')
                    # update status
                    text_17.status = FINISHED
                    text_17.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=decisionITI3,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                decisionITI3.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in decisionITI3.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "decisionITI3" ---
        for thisComponent in decisionITI3.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for decisionITI3
        decisionITI3.tStop = globalClock.getTime(format='float')
        decisionITI3.tStopRefresh = tThisFlipGlobal
        thisExp.addData('decisionITI3.stopped', decisionITI3.tStop)
        # the Routine "decisionITI3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisDecisionLoop as finished
        if hasattr(thisDecisionLoop, 'status'):
            thisDecisionLoop.status = FINISHED
        # if awaiting a pause, pause now
        if decisionLoop.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            decisionLoop.status = STARTED
        thisExp.nextEntry()
        
    # completed 2.0 repeats of 'decisionLoop'
    decisionLoop.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "thankYou" ---
    # create an object to store info about Routine thankYou
    thankYou = data.Routine(
        name='thankYou',
        components=[text_11, key_resp_8],
    )
    thankYou.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_8
    key_resp_8.keys = []
    key_resp_8.rt = []
    _key_resp_8_allKeys = []
    # store start times for thankYou
    thankYou.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    thankYou.tStart = globalClock.getTime(format='float')
    thankYou.status = STARTED
    thisExp.addData('thankYou.started', thankYou.tStart)
    thankYou.maxDuration = None
    # keep track of which components have finished
    thankYouComponents = thankYou.components
    for thisComponent in thankYou.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "thankYou" ---
    thankYou.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_11* updates
        
        # if text_11 is starting this frame...
        if text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_11.frameNStart = frameN  # exact frame index
            text_11.tStart = t  # local t and not account for scr refresh
            text_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_11.started')
            # update status
            text_11.status = STARTED
            text_11.setAutoDraw(True)
        
        # if text_11 is active this frame...
        if text_11.status == STARTED:
            # update params
            pass
        
        # *key_resp_8* updates
        waitOnFlip = False
        
        # if key_resp_8 is starting this frame...
        if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_8.frameNStart = frameN  # exact frame index
            key_resp_8.tStart = t  # local t and not account for scr refresh
            key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_8.started')
            # update status
            key_resp_8.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_8.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_8.getKeys(keyList=['2', 'num2'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_8_allKeys.extend(theseKeys)
            if len(_key_resp_8_allKeys):
                key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
                key_resp_8.rt = _key_resp_8_allKeys[-1].rt
                key_resp_8.duration = _key_resp_8_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=thankYou,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            thankYou.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in thankYou.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "thankYou" ---
    for thisComponent in thankYou.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for thankYou
    thankYou.tStop = globalClock.getTime(format='float')
    thankYou.tStopRefresh = tThisFlipGlobal
    thisExp.addData('thankYou.stopped', thankYou.tStop)
    # check responses
    if key_resp_8.keys in ['', [], None]:  # No response was made
        key_resp_8.keys = None
    thisExp.addData('key_resp_8.keys',key_resp_8.keys)
    if key_resp_8.keys != None:  # we had a response
        thisExp.addData('key_resp_8.rt', key_resp_8.rt)
        thisExp.addData('key_resp_8.duration', key_resp_8.duration)
    thisExp.nextEntry()
    # the Routine "thankYou" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # run any 'at exit' functions
    for fcn in runAtExit:
        fcn()
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
