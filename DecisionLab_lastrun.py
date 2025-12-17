#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2025.1.1),
    on December 17, 2025, at 00:23
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
    'session': '1',
    'day': '1',
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
        originPath='C:\\Users\\cmo53\\Downloads\\day2\\DecisionLab_lastrun.py',
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
    if deviceManager.getDevice('key_resp_15') is None:
        # initialise key_resp_15
        key_resp_15 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_15',
        )
    if deviceManager.getDevice('key_resp_14') is None:
        # initialise key_resp_14
        key_resp_14 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_14',
        )
    if deviceManager.getDevice('key_resp_16') is None:
        # initialise key_resp_16
        key_resp_16 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_16',
        )
    if deviceManager.getDevice('key_resp_18') is None:
        # initialise key_resp_18
        key_resp_18 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_18',
        )
    if deviceManager.getDevice('key_resp_19') is None:
        # initialise key_resp_19
        key_resp_19 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_19',
        )
    if deviceManager.getDevice('key_resp_9') is None:
        # initialise key_resp_9
        key_resp_9 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_9',
        )
    if deviceManager.getDevice('key_resp_10') is None:
        # initialise key_resp_10
        key_resp_10 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_10',
        )
    if deviceManager.getDevice('key_resp_11') is None:
        # initialise key_resp_11
        key_resp_11 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_11',
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
    if deviceManager.getDevice('key_resp_task_start_block2') is None:
        # initialise key_resp_task_start_block2
        key_resp_task_start_block2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_task_start_block2',
        )
    if deviceManager.getDevice('key_resp_13') is None:
        # initialise key_resp_13
        key_resp_13 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_13',
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
    
    # --- Initialize components for Routine "decisionPhase" ---
    text_5 = visual.TextStim(win=win, name='text_5',
        text='Press C to continue with the first block.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_4 = keyboard.Keyboard(deviceName='key_resp_4')
    
    # --- Initialize components for Routine "decisionInstructions" ---
    text_8 = visual.TextStim(win=win, name='text_8',
        text="\n\nYou have completed the learning phase and will now make decisions between pairs of fruits based on what you learned.\n\nPerformance Bonus Opportunity:\nMost people get 70% of their responses correctly.\nIf you'll be correct in more than 80% of your decisions, you will receive a bonus compensation.\n\nTry to recall the points associated with each fruit and make the best choices you can.\n\nClick C to continue.",
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
        text='Which fruit would you pick?\n\nIn this block, you will choose between pairs of fruits. Choose the fruit you think will give you more points.\n\nUse "1" to choose the fruit on the left side of the screen, and "3" to choose the fruit on the right side of the screen.\n\nClick C to continue.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.06, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_6 = keyboard.Keyboard(deviceName='key_resp_6')
    
    # --- Initialize components for Routine "practiceIntro2" ---
    key_resp_15 = keyboard.Keyboard(deviceName='key_resp_15')
    
    # --- Initialize components for Routine "practiceDecisionSimulus1" ---
    text_question1 = visual.TextStim(win=win, name='text_question1',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    text_dollar_left_practice = visual.TextStim(win=win, name='text_dollar_left_practice',
        text=None,
        font='Arial',
        pos=(-0.4, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    text_dollar_right_practice = visual.TextStim(win=win, name='text_dollar_right_practice',
        text=None,
        font='Arial',
        pos=(0.4, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "crosshairPracticeDecision1" ---
    text_crosshair_practice_decision1 = visual.TextStim(win=win, name='text_crosshair_practice_decision1',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "practiceDecisionSimulus2" ---
    text_question_3 = visual.TextStim(win=win, name='text_question_3',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    text_25 = visual.TextStim(win=win, name='text_25',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    text_dollar_left_practice_2 = visual.TextStim(win=win, name='text_dollar_left_practice_2',
        text=None,
        font='Arial',
        pos=(-0.4, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    text_dollar_right_practice_2 = visual.TextStim(win=win, name='text_dollar_right_practice_2',
        text=None,
        font='Arial',
        pos=(0.4, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "crosshairPracticeDecision2" ---
    text_crosshair_practice_decision2 = visual.TextStim(win=win, name='text_crosshair_practice_decision2',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "practiceDecisionMaking" ---
    text_question_4 = visual.TextStim(win=win, name='text_question_4',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    text_dollar_right_practice_3 = visual.TextStim(win=win, name='text_dollar_right_practice_3',
        text=None,
        font='Arial',
        pos=(0.4, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    text_dollar_left_practice_3 = visual.TextStim(win=win, name='text_dollar_left_practice_3',
        text=None,
        font='Arial',
        pos=(-0.4, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "crosshairPracticeDecision3" ---
    text_crosshair_practice_decision3 = visual.TextStim(win=win, name='text_crosshair_practice_decision3',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "taskStartSoonBlock3" ---
    text_task_start_soon_block3 = visual.TextStim(win=win, name='text_task_start_soon_block3',
        text='The task will start soon. Press C to continue.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "scannerSyncBlock3" ---
    text_scanner_wait_block3 = visual.TextStim(win=win, name='text_scanner_wait_block3',
        text='Waiting for the scanner to start...',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "crosshair3Block3" ---
    text_crosshair3_block3 = visual.TextStim(win=win, name='text_crosshair3_block3',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "scannerWaitBlock3" ---
    image_scanner_wait_block3 = visual.ImageStim(
        win=win,
        name='image_scanner_wait_block3', 
        image='images/randomImage.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(1, 1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    
    # --- Initialize components for Routine "startTaskBlock3" ---
    text_26 = visual.TextStim(win=win, name='text_26',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
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
        text=None,
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
    
    # --- Initialize components for Routine "inBetween" ---
    text_24 = visual.TextStim(win=win, name='text_24',
        text='You have completed the first block.\n\nPress C to continue.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_14 = keyboard.Keyboard(deviceName='key_resp_14')
    
    # --- Initialize components for Routine "TaskStructure" ---
    text_2 = visual.TextStim(win=win, name='text_2',
        text="Task Structure\n\nIn this task, you'll see different fruits as you play.\n\nEach fruit can either give you points or take points away.\n\nYou'll earn points when the number is positive (+), and lose points when it's negative (-).",
        font='Arial',
        pos=(0, .2), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    text_19 = visual.TextStim(win=win, name='text_19',
        text='+50',
        font='Arial',
        pos=(-.2, -.2), draggable=False, height=0.15, wrapWidth=None, ori=0.0, 
        color=[-1.0000, 0.0039, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    text_21 = visual.TextStim(win=win, name='text_21',
        text='-50',
        font='Arial',
        pos=(.2, -.2), draggable=False, height=0.15, wrapWidth=None, ori=0.0, 
        color=[0.5294, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    key_resp_16 = keyboard.Keyboard(deviceName='key_resp_16')
    text_28 = visual.TextStim(win=win, name='text_28',
        text='Press C to continue.',
        font='Arial',
        pos=(0, -0.4), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "yourGoal" ---
    text_3 = visual.TextStim(win=win, name='text_3',
        text='Your Goal\n\nRight after a fruit is shown, you will be asked to predict how many points it will provide this time.\n\nDo your best to be as accurate as you can.\n\nImmediately after your prediction, you will be shown how many points it actually provided this time.\n\nPress C to continue.',
        font='Arial',
        pos=(0, .3), draggable=False, height=0.035, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    slider_2 = visual.Slider(win=win, name='slider_2',
        startValue=0, size=(1, 0.075), pos=(0, -0.2), units=win.units,
        labels=(-100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100), ticks=(-100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100), granularity=5.0,
        style='slider', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-1, readOnly=False)
    text_22 = visual.TextStim(win=win, name='text_22',
        text='"How many points do you expect to receive from this fruit?"',
        font='Arial',
        pos=(0, -0.08), draggable=False, height=0.055, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    key_resp_18 = keyboard.Keyboard(deviceName='key_resp_18')
    
    # --- Initialize components for Routine "keyInstructions" ---
    text_20 = visual.TextStim(win=win, name='text_20',
        text='Pressing "1" will shift the slider value leftwards by a value of 5. Pressing "3" will shift the slider value rightwards, also by a value of 5. \n\nPressing "2" will confirm your answer.\n\nPress C to continue.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_19 = keyboard.Keyboard(deviceName='key_resp_19')
    
    # --- Initialize components for Routine "practiceIntro" ---
    text_practice_intro = visual.TextStim(win=win, name='text_practice_intro',
        text='We will run a short practice test now. Press C to continue.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_9 = keyboard.Keyboard(deviceName='key_resp_9')
    
    # --- Initialize components for Routine "practiceTrial" ---
    image_4 = visual.ImageStim(
        win=win,
        name='image_4', 
        image=None, mask=None, anchor='center',
        ori=0.0, pos=(0, 0.17), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    slider_3 = visual.Slider(win=win, name='slider_3',
        startValue=0, size=(1, 0.075), pos=(0, -0.2), units=win.units,
        labels=(-100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100), ticks=(-100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100), granularity=5.0,
        style='slider', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Noto Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-2, readOnly=False)
    
    # --- Initialize components for Routine "crosshair5" ---
    # Run 'Begin Experiment' code from code_40
    # First crosshair screen - duration set dynamically based on trial response time
    # Duration is set in trialEndRoutine.py as crosshair1_duration
    # This routine will show a crosshair in the center of the screen
    
    # Make sure crosshair is visible (add a crosshair component in Builder)
    if 'crosshair' in locals():
        crosshair.opacity = 1
        crosshair.setAutoDraw(True)
    
    
    text_27 = visual.TextStim(win=win, name='text_27',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "actualPoints1" ---
    text_actual_points = visual.TextStim(win=win, name='text_actual_points',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "crosshair3" ---
    text_23 = visual.TextStim(win=win, name='text_23',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "taskStartSoon" ---
    text_task_start_soon = visual.TextStim(win=win, name='text_task_start_soon',
        text='The task will start soon.\n\nPress C to continue.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_10 = keyboard.Keyboard(deviceName='key_resp_10')
    
    # --- Initialize components for Routine "scannerSync" ---
    text_scanner_wait = visual.TextStim(win=win, name='text_scanner_wait',
        text='Waiting for the scanner to start...',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_11 = keyboard.Keyboard(deviceName='key_resp_11')
    
    # --- Initialize components for Routine "crosshair3" ---
    text_23 = visual.TextStim(win=win, name='text_23',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "scannerWait" ---
    waitImage = visual.ImageStim(
        win=win,
        name='waitImage', 
        image='images/randomImage.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(1, 1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    
    # --- Initialize components for Routine "startTask" ---
    text_4 = visual.TextStim(win=win, name='text_4',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    # Run 'Begin Experiment' code from code
    import random
    import sys
    import csv
    
    # Path joining function (avoid os import for PsychoPy compatibility)
    def _join_path(*parts):
        """Join path parts using '/' separator (works on both Windows and Unix)"""
        return '/'.join(str(p).strip('/') for p in parts if p)
    
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
    # Get session_number and day from PsychoPy's expInfo dialog
    # PsychoPy Builder requires 'participant' field - we'll use that as session_number
    # Also need 'day' field (1 or 2)
    
    # Try to get from expInfo (set in PsychoPy Builder dialog)
    try:
        # PsychoPy stores dialog info in thisExp.info or expInfo
        exp_info_dict = None
        if 'thisExp' in locals() and hasattr(thisExp, 'info'):
            exp_info_dict = thisExp.info
        elif 'expInfo' in locals():
            exp_info_dict = expInfo
        
        if exp_info_dict:
            # Get session_number from 'session' field (user's actual field name)
            # Fallback to 'session_number' or 'participant' if 'session' not found
            if 'session' in exp_info_dict:
                session_str = str(exp_info_dict['session']).strip()
                # Remove any 'sub-' prefix if present
                if session_str.startswith('sub-'):
                    session_str = session_str[4:]
                # Try to convert to integer
                try:
                    SESSION_NUMBER = int(session_str)
                except ValueError:
                    # If not a number, use hash of string to get consistent number
                    SESSION_NUMBER = abs(hash(session_str)) % 10000
                    print(f"WARNING: session '{exp_info_dict['session']}' is not a number, using hash: {SESSION_NUMBER}")
            elif 'session_number' in exp_info_dict:
                SESSION_NUMBER = int(exp_info_dict['session_number'])
            elif 'participant' in exp_info_dict:
                # Use participant field as fallback (but user said to ignore it)
                participant_str = str(exp_info_dict['participant']).strip()
                if participant_str.lower() != 'ignore':
                    # Only use if not set to 'ignore'
                    if participant_str.startswith('sub-'):
                        participant_str = participant_str[4:]
                    try:
                        SESSION_NUMBER = int(participant_str)
                    except ValueError:
                        SESSION_NUMBER = abs(hash(participant_str)) % 10000
                        print(f"WARNING: participant '{exp_info_dict['participant']}' is not a number, using hash: {SESSION_NUMBER}")
                else:
                    SESSION_NUMBER = 1
                    print(f"WARNING: 'session' field not found and 'participant' is set to 'ignore', using default: {SESSION_NUMBER}")
            else:
                SESSION_NUMBER = 1
                print(f"WARNING: 'session' field not found in dialog, using default: {SESSION_NUMBER}")
            
            # Get day
            if 'day' in exp_info_dict:
                DAY = int(exp_info_dict['day'])
            else:
                DAY = 1
                print(f"WARNING: 'day' not found in dialog, using default: {DAY}")
            
            print(f"Got session_number={SESSION_NUMBER} (from 'session' field) and day={DAY} from PsychoPy dialog")
        else:
            # No dialog info available - use defaults
            SESSION_NUMBER = 1
            DAY = 1
            print(f"WARNING: Could not get session_number/day from dialog, using defaults: session_number={SESSION_NUMBER}, day={DAY}")
            print(f"  Make sure to set 'participant' (or 'session_number') and 'day' fields in PsychoPy Builder > Experiment Settings > Basic > Experiment info")
    except Exception as e:
        # Fallback to defaults if anything goes wrong
        SESSION_NUMBER = 1
        DAY = 1
        print(f"WARNING: Error getting session_number/day from dialog: {e}")
        print(f"  Using defaults: session_number={SESSION_NUMBER}, day={DAY}")
        print(f"  Make sure to set 'participant' (or 'session_number') and 'day' fields in PsychoPy Builder > Experiment Settings > Basic > Experiment info")
    
    # Initialize data logger with session_number and day
    data_logger = initialize_logger(session_number=SESSION_NUMBER, day=DAY, experiment_dir="data")
    globals()['data_logger'] = data_logger
    print(f"Data logger initialized: session_number={SESSION_NUMBER}, day={DAY}")
    
    # Load timing configuration from text file
    # Use simple defaults, config loading happens in individual routines to avoid os conflicts
    TRIAL_TIMEOUT_SECONDS = 8.0
    CROSSHAIR_RANDOM_VALUES = [2, 3, 4]
    TIMEOUT_SCREEN_DURATION = 1.5  # Timeout screen duration (same across all blocks)
    ACTUAL_POINTS_DURATION = 2.0
    DECISION_TIMEOUT_DURATION = 2.0  # Maximum time for decision making (seconds)
    
    # Store decision timeout in globals for use in decision making routines
    globals()['DECISION_TIMEOUT_DURATION'] = DECISION_TIMEOUT_DURATION
    globals()['TIMEOUT_SCREEN_DURATION'] = TIMEOUT_SCREEN_DURATION
    
    # Try to load from config file (will be loaded in routines that need it)
    print(f"Using timing config: timeout={TRIAL_TIMEOUT_SECONDS}s, actualPoints={ACTUAL_POINTS_DURATION}s, decisionTimeout={DECISION_TIMEOUT_DURATION}s")
    
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
    
    # Day 2 counterbalancing: Load Day 1 data if day == 2
    if DAY == 2:
        print(f"\n{'='*60}")
        print(f"DAY 2: Loading Day 1 data for counterbalancing")
        print(f"{'='*60}")
        
        # Load Day 1 CSV files to get fruit assignments and block order
        # File pattern: sub-{session:03d}_day-1_block-{1,2}_learning_{1,2}_{block_name}.csv
        session_str = f"{SESSION_NUMBER:03d}"
        day1_gain_fruits = []
        day1_loss_fruits = []
        day1_gain_baselines = {}
        day1_loss_baselines = {}
        day1_first_block = None
        
        # Try to load both block files from Day 1
        # Search in multiple locations since Day 1 and Day 2 might be in different folders
        # Priority order:
        # 1. Current experiment folder: data/sub-1/ (relative to Day 2 experiment)
        # 2. Parent folder: ../data/sub-1/ (if Day 1 and Day 2 are siblings)
        # 3. Common Downloads location: ../../data/sub-1/ (if both in Downloads)
        # 4. Absolute path from expInfo if provided (day1_data_path field)
        
        # Get optional Day 1 data path from expInfo (if user specified it)
        day1_data_path = None
        try:
            exp_info_dict = None
            if 'thisExp' in locals() and hasattr(thisExp, 'info'):
                exp_info_dict = thisExp.info
            elif 'expInfo' in locals():
                exp_info_dict = expInfo
            if exp_info_dict and 'day1_data_path' in exp_info_dict:
                day1_data_path = str(exp_info_dict['day1_data_path']).strip()
                if day1_data_path:
                    print(f"Using custom Day 1 data path from dialog: {day1_data_path}")
        except:
            pass
        
        # List of paths to search (in priority order)
        search_paths = []
        if day1_data_path:
            # User-specified path takes highest priority
            search_paths.append(day1_data_path)
        # Add relative paths
        search_paths.extend([
            _join_path("data", "sub-1"),  # Current folder
            _join_path("..", "data", "sub-1"),  # Parent folder (sibling experiments)
            _join_path("../..", "data", "sub-1"),  # Two levels up (common Downloads folder)
            _join_path("..", "..", "data", "sub-1"),  # Alternative two levels up
        ])
        
        print(f"Searching for Day 1 data files in {len(search_paths)} locations:")
        for i, path in enumerate(search_paths, 1):
            print(f"  {i}. {path}")
        
        # Try to load both block files from Day 1
        for block_num in [1, 2]:
            file_found = False
            for block_name in ["rewards", "gain", "punishment", "loss"]:
                filename = f"sub-{session_str}_day-1_block-{block_num}_learning_{block_num}_{block_name}.csv"
                
                # Try each search path
                for search_path in search_paths:
                    filepath = _join_path(search_path, filename)
                    
                    try:
                        # Try to read the CSV file
                        with open(filepath, 'r', encoding='utf-8') as f:
                            reader = csv.DictReader(f)
                            rows = list(reader)
                            
                            if rows:
                                # Determine block type from block_name or first row
                                first_row = rows[0]
                                block_type = first_row.get('block_name', block_name).lower()
                                
                                # Track which block came first
                                if block_num == 1:
                                    if block_type in ["rewards", "gain"]:
                                        day1_first_block = "gain"
                                    elif block_type in ["punishment", "loss"]:
                                        day1_first_block = "loss"
                                
                                # Extract fruits and baselines from this block
                                # Collect all unique fruits and their baselines (use first occurrence for baseline)
                                for row in rows:
                                    fruit_name = row.get('stimulus_identity', '').strip()
                                    if not fruit_name:
                                        continue
                                    
                                    # Add .png extension if not present
                                    if not fruit_name.endswith('.png'):
                                        fruit_name = fruit_name + '.png'
                                    
                                    baseline = float(row.get('stimulus_average_points', 0))
                                    
                                    if block_type in ["rewards", "gain"]:
                                        if fruit_name not in day1_gain_fruits:
                                            day1_gain_fruits.append(fruit_name)
                                            day1_gain_baselines[fruit_name] = baseline
                                    elif block_type in ["punishment", "loss"]:
                                        if fruit_name not in day1_loss_fruits:
                                            day1_loss_fruits.append(fruit_name)
                                            day1_loss_baselines[fruit_name] = baseline
                                
                                print(f"✓ Loaded Day 1 Block {block_num} ({block_type}): {len(rows)} trials from {filepath}")
                                file_found = True
                                break  # Found the file, move to next block
                    except (FileNotFoundError, IOError, OSError) as e:
                        # File doesn't exist at this path - try next path
                        continue
                
                if file_found:
                    break  # Found the file for this block, move to next block
        
        # Verify we got complete data (need 3 gain fruits and 3 loss fruits)
        gain_count = len(day1_gain_fruits) if day1_gain_fruits else 0
        loss_count = len(day1_loss_fruits) if day1_loss_fruits else 0
        print(f"DEBUG: Validation check - gain_fruits count: {gain_count}, loss_fruits count: {loss_count}")
        
        # Check if we have complete data (exactly 3 fruits in each category)
        has_complete_data = (gain_count == 3 and loss_count == 3)
        
        if not has_complete_data:
            print(f"\n{'='*60}")
            print(f"ERROR: Could not load complete Day 1 data for session {SESSION_NUMBER}")
            print(f"{'='*60}")
            print(f"  Found {len(day1_gain_fruits)} gain fruits: {day1_gain_fruits}")
            print(f"  Found {len(day1_loss_fruits)} loss fruits: {day1_loss_fruits}")
            print(f"  Expected 3 of each (need complete Day 1 data)")
            print(f"  Expected files: sub-{session_str}_day-1_block-1_learning_*.csv and block-2_learning_*.csv")
            print(f"  Searched in {len(search_paths)} locations:")
            for i, path in enumerate(search_paths, 1):
                print(f"    {i}. {path}")
            print(f"\n  Day 2 REQUIRES Day 1 data to run.")
            print(f"  Please ensure:")
            print(f"    1. Day 1 experiment completed successfully")
            print(f"    2. Day 1 CSV files are in data/sub-1/ folder")
            print(f"    3. Session number matches Day 1 (session={SESSION_NUMBER})")
            print(f"{'='*60}\n")
            
            # Exit the experiment - Day 2 cannot run without Day 1 data
            print("EXITING EXPERIMENT: Day 2 requires Day 1 data.")
            if 'thisExp' in locals():
                thisExp.abort()  # Abort the experiment
            # Also try to close the window if possible
            try:
                if 'win' in locals():
                    win.close()
            except:
                pass
            # Exit Python
            import sys
            sys.exit(1)
        else:
            print(f"Day 1 data loaded successfully:")
            print(f"  Gain fruits: {day1_gain_fruits} with baselines: {[day1_gain_baselines[f] for f in day1_gain_fruits]}")
            print(f"  Loss fruits: {day1_loss_fruits} with baselines: {[day1_loss_baselines[f] for f in day1_loss_fruits]}")
            print(f"  First block: {day1_first_block}")
            
            # Counterbalance Day 2 based on session ID (participant assignment):
            # Row 1 (session 1, 5, 9, 13, ...): Day 1 = gain/loss, Day 2 = gain/loss
            # Row 2 (session 2, 6, 10, 14, ...): Day 1 = gain/loss, Day 2 = loss/gain
            # Row 3 (session 3, 7, 11, 15, ...): Day 1 = loss/gain, Day 2 = gain/loss
            # Row 4 (session 4, 8, 12, 16, ...): Day 1 = loss/gain, Day 2 = loss/gain
            # Determine row: row = ((session_id - 1) % 4) + 1
            row = ((SESSION_NUMBER - 1) % 4) + 1
            print(f"  Participant row assignment: Row {row} (session {SESSION_NUMBER})")
            
            # Day 2 first block determined directly by row:
            # Row 1 or 3: gain first
            # Row 2 or 4: loss first
            if row == 1 or row == 3:
                # Row 1 or 3: gain first
                day2_first_block = "gain"
                print(f"  Row {row}: Day 2 first block = gain")
            else:  # row == 2 or row == 4
                # Row 2 or 4: loss first
                day2_first_block = "loss"
                print(f"  Row {row}: Day 2 first block = loss")
            
            # Fruits stay in the same category (gains stay gains, losses stay losses)
            # Only shift values: 20→50, 50→80, 80→20 (and -20→-50, -50→-80, -80→-20)
            # This is a mapping, not a circular shift
            
            # Get Day 1 baselines in order
            day1_gain_vals = [day1_gain_baselines[f] for f in day1_gain_fruits]
            day1_loss_vals = [day1_loss_baselines[f] for f in day1_loss_fruits]
            
            # Value mapping function: shifts magnitude only (20→50, 50→80, 80→20)
            # Fruits stay in the same category (gains stay gains, losses stay losses)
            # Only the values shift within each category
            def shift_value(val):
                """Shift value: 20→50, 50→80, 80→20 (preserves sign)"""
                abs_val = abs(val)
                if abs_val == 20:
                    shifted = 50
                elif abs_val == 50:
                    shifted = 80
                elif abs_val == 80:
                    shifted = 20
                else:
                    # Fallback: return original value if not in expected set
                    print(f"WARNING: Unexpected value {val} in Day 2 shift, returning original")
                    return val
                
                # Preserve the sign (positive stays positive, negative stays negative)
                return shifted if val > 0 else -shifted
            
            # Apply value shift to Day 1 values
            # Day 1 gains stay gains, just shift values: apple: 20→50, banana: 50→80, strawberry: 80→20
            day2_gain_vals = [shift_value(val) for val in day1_gain_vals]
            # Day 1 losses stay losses, just shift values: kiwi: -20→-50, pear: -50→-80, grapes: -80→-20
            day2_loss_vals = [shift_value(val) for val in day1_loss_vals]
            
            print(f"DEBUG: Day 1 gain values {day1_gain_vals} → Day 2 gain values {day2_gain_vals}")
            print(f"DEBUG: Day 1 loss values {day1_loss_vals} → Day 2 loss values {day2_loss_vals}")
            
            # Assign fruits: Day 1 gains stay gains, Day 1 losses stay losses (same fruits, shifted values)
            gain_fruits = day1_gain_fruits.copy()
            loss_fruits = day1_loss_fruits.copy()
            
            # Create baseline lists with shifted values (matching fruit order)
            gain_baselines = day2_gain_vals
            loss_baselines = day2_loss_vals
            
            print(f"Day 2 assignments (same fruits, shifted values):")
            print(f"  Gain fruits: {gain_fruits} with baselines: {gain_baselines}")
            print(f"  Loss fruits: {loss_fruits} with baselines: {loss_baselines}")
            print(f"{'='*60}\n")
            
            # Store day2_first_block for use in block order determination
            globals()['day2_first_block'] = day2_first_block
            print(f"DEBUG: Stored day2_first_block = '{day2_first_block}' in globals")
    else:
        # Day 1: Random assignment
        random.shuffle(all_fruits)
        gain_fruits = all_fruits[:3]
        loss_fruits = all_fruits[3:]
        
        # Randomly assign baseline values to each fruit
        gain_baselines = random.sample([20, 50, 80], 3)
        loss_baselines = random.sample([-20, -50, -80], 3)
        
        print(f"Day 1: Random assignment")
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
    
    # Decide which block comes first
    if DAY == 2:
        # Use the counterbalanced block order from Day 2 setup
        day2_first_block = globals().get('day2_first_block', None)
        print(f"DEBUG: Retrieved day2_first_block from globals = '{day2_first_block}'")
        print(f"DEBUG: SESSION_NUMBER = {SESSION_NUMBER}, DAY = {DAY}")
        
        if day2_first_block:
            first_block = day2_first_block
            second_block = "loss" if day2_first_block == "gain" else "gain"
            print(f"Day 2 block order: {first_block} first, then {second_block} (counterbalanced by session ID)")
            print(f"DEBUG: first_block = '{first_block}', second_block = '{second_block}'")
        else:
            # Fallback if day2_first_block wasn't set - this should not happen!
            print(f"ERROR: day2_first_block is None! This should not happen for Day 2.")
            print(f"ERROR: Falling back to random assignment (this is wrong!)")
            # Recalculate based on session ID as fallback
            row = ((SESSION_NUMBER - 1) % 4) + 1
            if row == 1 or row == 3:
                first_block = "gain"
                second_block = "loss"
            else:
                first_block = "loss"
                second_block = "gain"
            print(f"ERROR FALLBACK: Row {row}, Day 2 block order: {first_block} first, then {second_block}")
    else:
        # Day 1: Counterbalance block order based on session ID (participant assignment):
        # Row 1 (session 1, 5, 9, 13, ...): Day 1 = gain/loss
        # Row 2 (session 2, 6, 10, 14, ...): Day 1 = gain/loss
        # Row 3 (session 3, 7, 11, 15, ...): Day 1 = loss/gain
        # Row 4 (session 4, 8, 12, 16, ...): Day 1 = loss/gain
        # Determine row: row = ((session_id - 1) % 4) + 1
        row = ((SESSION_NUMBER - 1) % 4) + 1
        print(f"  Participant row assignment: Row {row} (session {SESSION_NUMBER})")
        
        if row == 1 or row == 2:
            # Row 1 or 2: gain first
            first_block = "gain"
            second_block = "loss"
            print(f"  Row {row}: Day 1 block order = gain/loss")
        else:  # row == 3 or row == 4
            # Row 3 or 4: loss first
            first_block = "loss"
            second_block = "gain"
            print(f"  Row {row}: Day 1 block order = loss/gain")
        
        print(f"Day 1 block order: {first_block} first, then {second_block} (counterbalanced by session ID)")
    
    # Note: Trial count per block will be determined by loop nReps / 2
    # For now, we'll use all available trials and let the loop control it
    # The combined block will be truncated by the loop's nReps
    
    print(f"Block order: {first_block} first, then {second_block}")
    print(f"DEBUG: Creating combined block with first_block='{first_block}', second_block='{second_block}'")
    print(f"DEBUG: gain_block has {len(gain_block)} trials, loss_block has {len(loss_block)} trials")
    if len(gain_block) > 0:
        print(f"DEBUG: First gain trial: {gain_block[0].get('fruit', 'unknown')}, block type: {gain_block[0].get('block', 'unknown')}")
    if len(loss_block) > 0:
        print(f"DEBUG: First loss trial: {loss_block[0].get('fruit', 'unknown')}, block type: {loss_block[0].get('block', 'unknown')}")
    
    # Create combined block list in the correct order
    # IMPORTANT: This ensures all trials from first block appear first, then all from second block
    # We'll create the full combined block, but trialBeginRoutine will limit based on nReps
    combined_learning_block = []
    if first_block == "gain":
        # First block: all gain trials, then all loss trials
        combined_learning_block = gain_block.copy() + loss_block.copy()
        print(f"Combined block: {len(gain_block)} gains + {len(loss_block)} losses = {len(combined_learning_block)} total")
        print(f"DEBUG: First {len(gain_block)} trials are GAIN, next {len(loss_block)} trials are LOSS")
        if len(combined_learning_block) > 0:
            first_trial = combined_learning_block[0]
            print(f"DEBUG: First trial - fruit: {first_trial.get('fruit', 'unknown')}, block type: {first_trial.get('block', 'unknown')}, expected: 'gain'")
            if first_trial.get('block', 'unknown') != 'gain':
                print(f"ERROR: First trial block type is '{first_trial.get('block', 'unknown')}' but should be 'gain'!")
    else:
        # First block: all loss trials, then all gain trials
        combined_learning_block = loss_block.copy() + gain_block.copy()
        print(f"Combined block: {len(loss_block)} losses + {len(gain_block)} gains = {len(combined_learning_block)} total")
        print(f"DEBUG: First {len(loss_block)} trials are LOSS, next {len(gain_block)} trials are GAIN")
        if len(combined_learning_block) > 0:
            first_trial = combined_learning_block[0]
            print(f"DEBUG: First trial - fruit: {first_trial.get('fruit', 'unknown')}, block type: {first_trial.get('block', 'unknown')}, expected: 'loss'")
            if first_trial.get('block', 'unknown') != 'loss':
                print(f"ERROR: First trial block type is '{first_trial.get('block', 'unknown')}' but should be 'loss'!")
    
    # Explicitly store in globals to ensure it's accessible in other routines
    globals()['combined_learning_block'] = combined_learning_block
    globals()['first_block'] = first_block  # Store for debugging
    globals()['second_block'] = second_block  # Store for debugging
    
    # Final verification
    print(f"DEBUG FINAL: Stored first_block='{first_block}', second_block='{second_block}' in globals")
    print(f"DEBUG FINAL: Combined block has {len(combined_learning_block)} trials")
    if len(combined_learning_block) > 0:
        actual_first = combined_learning_block[0].get('block', 'unknown')
        print(f"DEBUG FINAL: Actual first trial block type = '{actual_first}', expected = '{first_block}'")
        if actual_first != first_block:
            print(f"ERROR: MISMATCH! First trial is '{actual_first}' but should be '{first_block}'!")
    globals()['gain_block'] = gain_block
    globals()['loss_block'] = loss_block
    
    learning_block_index = -1
    # Store in globals to ensure it persists
    globals()['learning_block_index'] = learning_block_index
    show_block_transition = False  # Flag to trigger transition screen between blocks
    globals()['show_block_transition'] = show_block_transition
    ready_for_block2_setup = False  # Flag to indicate block transition completed, ready for block 2 setup
    globals()['ready_for_block2_setup'] = ready_for_block2_setup
    ready_for_scanner_sync_block2 = False  # Flag to indicate taskStartSoonBlock2 completed, ready for scanner sync
    globals()['ready_for_scanner_sync_block2'] = ready_for_scanner_sync_block2
    block2_setup_complete = False  # Flag to indicate block 2 setup (taskStartSoon + scannerSync) has already been done
    globals()['block2_setup_complete'] = block2_setup_complete
    crosshair2Block2_actually_ran = False  # Flag to track if crosshair2Block2 actually ran (not skipped)
    globals()['crosshair2Block2_actually_ran'] = crosshair2Block2_actually_ran
    block1_scanner_sync_complete = False  # Flag to indicate Block 1 scanner sync has already been completed
    globals()['block1_scanner_sync_complete'] = block1_scanner_sync_complete
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
    
    # Build list of decision trials with counterbalancing (4 repetitions per pair = 60 total)
    # For each pair (A,B), create 4 reps so that:
    # - Each fruit appears 2x on left and 2x on right (final choice display)
    # - Each fruit appears 2x as the first stimulus and 2x as the second stimulus
    # Rep template:
    # rep 1: left=A right=B, first=A (left)
    # rep 2: left=A right=B, first=B (right)
    # rep 3: left=B right=A, first=A (right)
    # rep 4: left=B right=A, first=B (left)
    
    decision_block = []
    for fruit1, fruit2 in decision_pairs:
        val1 = fruit_values[fruit1]
        val2 = fruit_values[fruit2]
    
        # rep 1
        decision_block.append({
            "leftFruit": fruit1,
            "rightFruit": fruit2,
            "firstFruit": fruit1,
            "firstSide": "left",
            "secondFruit": fruit2,
            "secondSide": "right",
            "leftVal": val1,
            "rightVal": val2,
            "correct": "left" if val1 > val2 else "right",
        })
    
        # rep 2
        decision_block.append({
            "leftFruit": fruit1,
            "rightFruit": fruit2,
            "firstFruit": fruit2,
            "firstSide": "right",
            "secondFruit": fruit1,
            "secondSide": "left",
            "leftVal": val1,
            "rightVal": val2,
            "correct": "left" if val1 > val2 else "right",
        })
    
        # rep 3
        decision_block.append({
            "leftFruit": fruit2,
            "rightFruit": fruit1,
            "firstFruit": fruit1,
            "firstSide": "right",
            "secondFruit": fruit2,
            "secondSide": "left",
            "leftVal": val2,
            "rightVal": val1,
            "correct": "left" if val2 > val1 else "right",
        })
    
        # rep 4
        decision_block.append({
            "leftFruit": fruit2,
            "rightFruit": fruit1,
            "firstFruit": fruit2,
            "firstSide": "left",
            "secondFruit": fruit1,
            "secondSide": "right",
            "leftVal": val2,
            "rightVal": val1,
            "correct": "left" if val2 > val1 else "right",
        })
    
    # Verify counterbalancing: should have 30 left-first and 30 right-first
    left_first_count = sum(1 for trial in decision_block if trial["firstSide"] == "left")
    right_first_count = sum(1 for trial in decision_block if trial["firstSide"] == "right")
    print(f"Counterbalancing check (before shuffle): {left_first_count} left-first, {right_first_count} right-first (should be 30 each)")
    
    # Shuffle all trials to randomize order
    random.shuffle(decision_block)
    
    # Verify randomization: show first 10 trials to confirm pattern
    print("Randomization check (first 10 trials after shuffle):")
    for i in range(min(10, len(decision_block))):
        trial = decision_block[i]
        first_side = trial["firstSide"]
        first_fruit = trial["firstFruit"].replace("images/", "").replace(".png", "")
        second_fruit = trial["secondFruit"].replace("images/", "").replace(".png", "")
        left_fruit = trial["leftFruit"].replace("images/", "").replace(".png", "")
        right_fruit = trial["rightFruit"].replace("images/", "").replace(".png", "")
        print(f"  Trial {i+1}: First {first_fruit} on {first_side}, then {second_fruit} on {trial['secondSide']}, final: {left_fruit} left, {right_fruit} right")
    
    # Final verification after shuffle
    left_first_count_after = sum(1 for trial in decision_block if trial["firstSide"] == "left")
    right_first_count_after = sum(1 for trial in decision_block if trial["firstSide"] == "right")
    print(f"Counterbalancing check (after shuffle): {left_first_count_after} left-first, {right_first_count_after} right-first (should still be 30 each)")
    
    decision_index = 0
    # Store in globals to ensure it persists across routines
    globals()['decision_index'] = decision_index
    globals()['decision_block'] = decision_block
    print(f"Decision trials: {len(decision_block)} (should be 60)")
    
    # --- Create practice block for Block 1 (3 practice trials) ---
    # Practice trials use static images: dog, cat, rabbit (always in this order)
    # These are shorter trials to familiarize participants with the task
    # Practice trials should match the first block type (gain or loss)
    practice_block = []
    # Static practice images (always the same)
    practice_fruit_names = ["dog.png", "cat.png", "rabbit.png"]
    
    # Determine practice values based on first_block type
    # If first_block is "gain", all values should be positive
    # If first_block is "loss", all values should be negative
    if first_block == "gain":
        # Positive values for reward block: 30, 50, 10
        practice_values = [30, 50, 10]  # All positive
        practice_baselines = [50, 50, 50]  # All positive baselines
        practice_block_type = "gain"
    else:
        # Negative values for punishment block: -30, -50, -10
        practice_values = [-30, -50, -10]  # All negative
        practice_baselines = [-50, -50, -50]  # All negative baselines
        practice_block_type = "loss"
    
    for i, image_name in enumerate(practice_fruit_names):
        baseline = practice_baselines[i]
        practice_value = practice_values[i]
        
        # Create practice trial with static value matching first block type
        practice_block.append({
            "block": practice_block_type,
            "fruit": image_dir + image_name,
            "baseline": baseline,
            "true_value": practice_value
        })
        print(f"Practice trial {i+1} (Block 1, {first_block}): {image_name} with value {practice_value:+d} (baseline: {baseline:+d})")
    
    # Do NOT shuffle practice trials - keep them in order: dog, cat, rabbit
    
    practice_block_index = -1
    # Store in globals
    globals()['practice_block'] = practice_block
    globals()['practice_block_index'] = practice_block_index
    print(f"Practice learning trials for Block 1 ({first_block}): {len(practice_block)} (3 trials)")
    
    # --- Create practice decision block (3 practice trials) ---
    # Practice decision trials with dollar amounts: $5/$1, $10/$1, $10/$5
    # Structure matches decision-making practice run:
    # Trial 1: $5 left (2s), crosshair (1s), $1 right (2s), crosshair (1s), both (2s), crosshair (2s)
    # Trial 2: $10 right (2s), crosshair (1s), $1 left (2s), crosshair (1s), both (2s), crosshair (2s)
    # Trial 3: $10 left (2s), crosshair (1s), $5 right (2s), crosshair (1s), both (2s), crosshair (2s)
    practice_decision_block = []
    
    # Practice dollar values
    practice_dollar_values = {
        "$5": 5,
        "$1": 1,
        "$10": 10
    }
    
    # Practice decision trials (3 trials with specific structure):
    # Trial 1: $5 left, $1 right (correct: left, $5 > $1)
    # Trial 2: $1 left, $10 right (correct: right, $10 > $1)
    # Trial 3: $10 left, $5 right (correct: left, $10 > $5)
    practice_decision_trials = [
        {
            "leftDollar": "$5",
            "rightDollar": "$1",
            "firstDollar": "$5",
            "firstSide": "left",      # $5 appears first on left
            "secondDollar": "$1",
            "secondSide": "right",   # $1 appears second on right
            "leftVal": 5,
            "rightVal": 1,
            "correct": "left"
        },
        {
            "leftDollar": "$1",
            "rightDollar": "$10",
            "firstDollar": "$10",
            "firstSide": "right",    # $10 appears first on right
            "secondDollar": "$1",
            "secondSide": "left",    # $1 appears second on left
            "leftVal": 1,
            "rightVal": 10,
            "correct": "right"
        },
        {
            "leftDollar": "$10",
            "rightDollar": "$5",
            "firstDollar": "$10",
            "firstSide": "left",     # $10 appears first on left
            "secondDollar": "$5",
            "secondSide": "right",   # $5 appears second on right
            "leftVal": 10,
            "rightVal": 5,
            "correct": "left"
        }
    ]
    
    for trial in practice_decision_trials:
        practice_decision_block.append(trial)
        print(f"Practice decision trial: {trial['leftDollar']} vs {trial['rightDollar']} (left={trial['leftVal']}, right={trial['rightVal']}, correct={trial['correct']}, first={trial['firstDollar']} on {trial['firstSide']})")
    
    # Do NOT shuffle practice decision trials - keep them in order: rabbit/dog, dog/cat, rabbit/cat
    
    practice_decision_index = -1
    # Store in globals
    globals()['practice_decision_block'] = practice_decision_block
    globals()['practice_decision_index'] = practice_decision_index
    print(f"Practice decision trials: {len(practice_decision_block)} (3 trials)")
    print(f"DEBUG: Stored practice_decision_block in globals with {len(practice_decision_block)} trials")
    print(f"DEBUG: First trial: {practice_decision_block[0] if practice_decision_block else 'EMPTY'}")
    
    # Initialize ITI duration variables (will be set during trials)
    iti1_duration = 2.0  # Default
    iti2_duration = 2.0  # Default
    iti3_duration = 2.0  # Default (will be calculated in decisionMakingEndRoutine)
    
    # Initialize duration variables for learning phase (will be set in trialEndRoutine)
    # Initialize them here so Builder can access them even before first trial
    globals()['crosshair1_duration'] = 2.0  # Default
    globals()['actualPoints_duration'] = ACTUAL_POINTS_DURATION  # Default (2.0)
    globals()['crosshair2_duration'] = 2.0  # Default
    globals()['timeout_duration'] = 0  # Default
    
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
    image_30 = visual.TextStim(win=win, name='image_30',
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
    
    # --- Initialize components for Routine "taskStartSoonBlock2" ---
    key_resp_task_start_block2 = keyboard.Keyboard(deviceName='key_resp_task_start_block2')
    text_task_start_soon_block2 = visual.TextStim(win=win, name='text_task_start_soon_block2',
        text='The task will start soon.\n\nPress C to continue.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "scannerSyncBlock2" ---
    text_scanner_wait_2 = visual.TextStim(win=win, name='text_scanner_wait_2',
        text='Waiting for the scanner to start...',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_13 = keyboard.Keyboard(deviceName='key_resp_13')
    
    # --- Initialize components for Routine "crosshairBlock2" ---
    text_crosshair_block2 = visual.TextStim(win=win, name='text_crosshair_block2',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "scannerWaitBlock2" ---
    image_scanner_wait_block2 = visual.ImageStim(
        win=win,
        name='image_scanner_wait_block2', 
        image='images/randomImage.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(1, 1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    
    # --- Initialize components for Routine "crosshair2Block2" ---
    text_crosshair2_block2 = visual.TextStim(win=win, name='text_crosshair2_block2',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "thankYou" ---
    text_11 = visual.TextStim(win=win, name='text_11',
        text='You completed the experiment!\n\nThank you for participating!\n\nPress C to end.',
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
            theseKeys = key_resp_4.getKeys(keyList=['c', 'C'], ignoreKeys=["escape"], waitRelease=False)
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
            theseKeys = key_resp_5.getKeys(keyList=['c', 'C'], ignoreKeys=["escape"], waitRelease=False)
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
            theseKeys = key_resp_6.getKeys(keyList=['c', 'C'], ignoreKeys=["escape"], waitRelease=False)
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
    
    # --- Prepare to start Routine "practiceIntro2" ---
    # create an object to store info about Routine practiceIntro2
    practiceIntro2 = data.Routine(
        name='practiceIntro2',
        components=[key_resp_15],
    )
    practiceIntro2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_28
    # Practice introduction screen 2 (before practice decision trials)
    # Shows "We will run a short practice task now. Press 2 to continue"
    # Component: text_practice_intro (or similar text component)
    
    # IMPORTANT: Hide all leftover components from previous routines (especially fixation crosses)
    # Hide practice decision components
    if 'text_question1' in locals():
        text_question1.setAutoDraw(False)
        text_question1.opacity = 0
    if 'text_question_3' in locals():
        text_question_3.setAutoDraw(False)
        text_question_3.opacity = 0
    if 'text_question_4' in locals():
        text_question_4.setAutoDraw(False)
        text_question_4.opacity = 0
    if 'text_25' in locals():
        text_25.setAutoDraw(False)
        text_25.opacity = 0
    
    # Hide practice decision images
    if 'image_left3' in locals():
        image_left3.setAutoDraw(False)
        image_left3.opacity = 0
    if 'image_right3' in locals():
        image_right3.setAutoDraw(False)
        image_right3.opacity = 0
    if 'image_left1_3' in locals():
        image_left1_3.setAutoDraw(False)
        image_left1_3.opacity = 0
    if 'image_right2_3' in locals():
        image_right2_3.setAutoDraw(False)
        image_right2_3.opacity = 0
    if 'image_left_left1' in locals():
        image_left_left1.setAutoDraw(False)
        image_left_left1.opacity = 0
    if 'image_right_right1' in locals():
        image_right_right1.setAutoDraw(False)
        image_right_right1.opacity = 0
    
    # Clear any previous key presses
    try:
        event.clearEvents()
    except:
        pass
    
    # Check if practice_decision_block exists, if not, re-initialize it
    practice_decision_block = globals().get('practice_decision_block', [])
    if not practice_decision_block or len(practice_decision_block) == 0:
        print("WARNING: practice_decision_block is empty! Re-initializing...")
        import random
        image_dir = "images/"
        
        # Practice fruit values (baselines from learning practice)
        practice_fruit_values = {
            image_dir + "ten.png": 10,      # ten = 10
            image_dir + "thirty.png": 30,   # thirty = 30
            image_dir + "fifty.png": 50     # fifty = 50
        }
        
        # Practice decision pairs with counterbalancing (same structure as main decision trials)
        practice_decision_pairs = [
            (image_dir + "ten.png", image_dir + "thirty.png"),    # ten/thirty
            (image_dir + "thirty.png", image_dir + "fifty.png"),  # thirty/fifty
            (image_dir + "ten.png", image_dir + "fifty.png")       # ten/fifty
        ]
        
        practice_decision_block = []
        for fruit1, fruit2 in practice_decision_pairs:
            left_val = practice_fruit_values[fruit1]
            right_val = practice_fruit_values[fruit2]
            correct_side = "left" if left_val > right_val else "right"
            
            # ALWAYS left appears first, then right
            practice_decision_block.append({
                "leftFruit": fruit1,
                "rightFruit": fruit2,
                "firstFruit": fruit1,     # Left fruit appears first
                "firstSide": "left",      # ALWAYS left first
                "secondFruit": fruit2,    # Right fruit appears second
                "secondSide": "right",   # ALWAYS right second
                "leftVal": left_val,
                "rightVal": right_val,
                "correct": correct_side
            })
            print(f"Re-initialized practice decision trial: {fruit1.split('/')[-1]} vs {fruit2.split('/')[-1]} (left={left_val}, right={right_val}, correct={correct_side}, first=left)")
        
        globals()['practice_decision_block'] = practice_decision_block
        print(f"Re-initialized practice_decision_block with {len(practice_decision_block)} trials")
    else:
        print(f"DEBUG practiceIntro2: practice_decision_block exists with {len(practice_decision_block)} trials")
    
    # Reset practice_decision_index to -1 before practice decision loop starts
    # This ensures it starts fresh at 0 for the first practice trial
    practice_decision_index = -1
    globals()['practice_decision_index'] = practice_decision_index
    print(f"DEBUG practiceIntro2: Reset practice_decision_index to -1 (will be 0 for first practice trial)")
    
    # Display practice introduction text
    if 'text_practice_intro' in locals():
        text_practice_intro.text = "We will run a short practice task now. Press C to continue"
        text_practice_intro.opacity = 1
        text_practice_intro.setAutoDraw(True)
        print("Practice introduction screen displayed")
    else:
        print("WARNING: text_practice_intro component not found!")
    
    
    # create starting attributes for key_resp_15
    key_resp_15.keys = []
    key_resp_15.rt = []
    _key_resp_15_allKeys = []
    # store start times for practiceIntro2
    practiceIntro2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    practiceIntro2.tStart = globalClock.getTime(format='float')
    practiceIntro2.status = STARTED
    thisExp.addData('practiceIntro2.started', practiceIntro2.tStart)
    practiceIntro2.maxDuration = None
    # keep track of which components have finished
    practiceIntro2Components = practiceIntro2.components
    for thisComponent in practiceIntro2.components:
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
    
    # --- Run Routine "practiceIntro2" ---
    practiceIntro2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_28
        # Practice introduction screen 2 - wait for key press '2' to continue
        # Check for key press '2' to continue to practice decision trials
        
        try:
            keys = event.getKeys(keyList=['2', 'num_2'])
            if keys:
                # Key 2 pressed - continue to practice decision trials
                print("Practice intro 2: Key 2 pressed, continuing to practice decision trials")
                continueRoutine = False
                event.clearEvents()
        except:
            pass
        
        
        
        # *key_resp_15* updates
        waitOnFlip = False
        
        # if key_resp_15 is starting this frame...
        if key_resp_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_15.frameNStart = frameN  # exact frame index
            key_resp_15.tStart = t  # local t and not account for scr refresh
            key_resp_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_15.started')
            # update status
            key_resp_15.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_15.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_15.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_15.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_15.getKeys(keyList=['c', 'C'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_15_allKeys.extend(theseKeys)
            if len(_key_resp_15_allKeys):
                key_resp_15.keys = _key_resp_15_allKeys[-1].name  # just the last key pressed
                key_resp_15.rt = _key_resp_15_allKeys[-1].rt
                key_resp_15.duration = _key_resp_15_allKeys[-1].duration
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
                currentRoutine=practiceIntro2,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            practiceIntro2.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceIntro2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "practiceIntro2" ---
    for thisComponent in practiceIntro2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for practiceIntro2
    practiceIntro2.tStop = globalClock.getTime(format='float')
    practiceIntro2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('practiceIntro2.stopped', practiceIntro2.tStop)
    # Run 'End Routine' code from code_28
    # Hide practice introduction text
    if 'text_practice_intro' in locals():
        text_practice_intro.setAutoDraw(False)
        text_practice_intro.opacity = 0
    
    
    # check responses
    if key_resp_15.keys in ['', [], None]:  # No response was made
        key_resp_15.keys = None
    thisExp.addData('key_resp_15.keys',key_resp_15.keys)
    if key_resp_15.keys != None:  # we had a response
        thisExp.addData('key_resp_15.rt', key_resp_15.rt)
        thisExp.addData('key_resp_15.duration', key_resp_15.duration)
    thisExp.nextEntry()
    # the Routine "practiceIntro2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    practiceDecisionLoop = data.TrialHandler2(
        name='practiceDecisionLoop',
        nReps=3.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(practiceDecisionLoop)  # add the loop to the experiment
    thisPracticeDecisionLoop = practiceDecisionLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeDecisionLoop.rgb)
    if thisPracticeDecisionLoop != None:
        for paramName in thisPracticeDecisionLoop:
            globals()[paramName] = thisPracticeDecisionLoop[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisPracticeDecisionLoop in practiceDecisionLoop:
        practiceDecisionLoop.status = STARTED
        if hasattr(thisPracticeDecisionLoop, 'status'):
            thisPracticeDecisionLoop.status = STARTED
        currentLoop = practiceDecisionLoop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisPracticeDecisionLoop.rgb)
        if thisPracticeDecisionLoop != None:
            for paramName in thisPracticeDecisionLoop:
                globals()[paramName] = thisPracticeDecisionLoop[paramName]
        
        # --- Prepare to start Routine "practiceDecisionSimulus1" ---
        # create an object to store info about Routine practiceDecisionSimulus1
        practiceDecisionSimulus1 = data.Routine(
            name='practiceDecisionSimulus1',
            components=[text_question1, text_dollar_left_practice, text_dollar_right_practice],
        )
        practiceDecisionSimulus1.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_29
        # Practice decision - First stimulus screen - shows first dollar amount on its side for 2 seconds
        # Components: text_question1, text_dollar_left_practice, text_dollar_right_practice
        # Shows dollar amount ($5, $1, or $10) on left or right side for 2 seconds
        
        # Get practice_decision_index and practice_decision_block from globals
        practice_decision_index = globals().get('practice_decision_index', -1)
        practice_decision_index += 1
        globals()['practice_decision_index'] = practice_decision_index
        
        practice_decision_block = globals().get('practice_decision_block', [])
        
        # DEBUG: Print block info
        print(f"DEBUG practiceDecisionStimulus1: practice_decision_index={practice_decision_index}, block_length={len(practice_decision_block) if practice_decision_block else 0}")
        
        if practice_decision_block and practice_decision_index >= 0 and practice_decision_index < len(practice_decision_block):
            current = practice_decision_block[practice_decision_index]
            first_dollar = current["firstDollar"]  # Dollar amount (e.g., "$5", "$1", "$10")
            first_side = current["firstSide"]
            
            # Show central fixation cross
            if 'text_question1' in locals():
                text_question1.text = "+"
                try:
                    text_question1.setPos((0, 0))
                except AttributeError:
                    text_question1.pos = (0, 0)
                text_question1.opacity = 1
                text_question1.setAutoDraw(True)
            
            # Show first dollar amount on its designated side
            # Hide both text components first, then show the correct one
            if 'text_dollar_left_practice' in locals():
                text_dollar_left_practice.opacity = 0
                text_dollar_left_practice.setAutoDraw(False)
            if 'text_dollar_right_practice' in locals():
                text_dollar_right_practice.opacity = 0
                text_dollar_right_practice.setAutoDraw(False)
            
            if first_side == "left":
                if 'text_dollar_left_practice' in locals():
                    text_dollar_left_practice.text = first_dollar
                    text_dollar_left_practice.opacity = 1
                    # Set larger font size for currency numbers
                    try:
                        text_dollar_left_practice.height = 0.1  # Larger font size (default is typically 0.05)
                    except AttributeError:
                        pass  # If height can't be set, continue anyway
                    text_dollar_left_practice.setAutoDraw(True)
            else:  # right
                if 'text_dollar_right_practice' in locals():
                    text_dollar_right_practice.text = first_dollar
                    text_dollar_right_practice.opacity = 1
                    # Set larger font size for currency numbers
                    try:
                        text_dollar_right_practice.height = 0.1  # Larger font size (default is typically 0.05)
                    except AttributeError:
                        pass  # If height can't be set, continue anyway
                    text_dollar_right_practice.setAutoDraw(True)
            
            print(f"Practice decision {practice_decision_index+1}/3: Showing {first_dollar} on {first_side} (2 seconds)")
        else:
            print(f"WARNING: Practice decision trial {practice_decision_index} out of range")
        
        
        # store start times for practiceDecisionSimulus1
        practiceDecisionSimulus1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        practiceDecisionSimulus1.tStart = globalClock.getTime(format='float')
        practiceDecisionSimulus1.status = STARTED
        thisExp.addData('practiceDecisionSimulus1.started', practiceDecisionSimulus1.tStart)
        practiceDecisionSimulus1.maxDuration = 2
        # keep track of which components have finished
        practiceDecisionSimulus1Components = practiceDecisionSimulus1.components
        for thisComponent in practiceDecisionSimulus1.components:
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
        
        # --- Run Routine "practiceDecisionSimulus1" ---
        practiceDecisionSimulus1.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisPracticeDecisionLoop, 'status') and thisPracticeDecisionLoop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > practiceDecisionSimulus1.maxDuration-frameTolerance:
                practiceDecisionSimulus1.maxDurationReached = True
                continueRoutine = False
            
            # *text_question1* updates
            
            # if text_question1 is starting this frame...
            if text_question1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_question1.frameNStart = frameN  # exact frame index
                text_question1.tStart = t  # local t and not account for scr refresh
                text_question1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_question1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_question1.started')
                # update status
                text_question1.status = STARTED
                text_question1.setAutoDraw(True)
            
            # if text_question1 is active this frame...
            if text_question1.status == STARTED:
                # update params
                pass
            
            # *text_dollar_left_practice* updates
            
            # if text_dollar_left_practice is starting this frame...
            if text_dollar_left_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_dollar_left_practice.frameNStart = frameN  # exact frame index
                text_dollar_left_practice.tStart = t  # local t and not account for scr refresh
                text_dollar_left_practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_dollar_left_practice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_dollar_left_practice.started')
                # update status
                text_dollar_left_practice.status = STARTED
                text_dollar_left_practice.setAutoDraw(True)
            
            # if text_dollar_left_practice is active this frame...
            if text_dollar_left_practice.status == STARTED:
                # update params
                pass
            
            # *text_dollar_right_practice* updates
            
            # if text_dollar_right_practice is starting this frame...
            if text_dollar_right_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_dollar_right_practice.frameNStart = frameN  # exact frame index
                text_dollar_right_practice.tStart = t  # local t and not account for scr refresh
                text_dollar_right_practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_dollar_right_practice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_dollar_right_practice.started')
                # update status
                text_dollar_right_practice.status = STARTED
                text_dollar_right_practice.setAutoDraw(True)
            
            # if text_dollar_right_practice is active this frame...
            if text_dollar_right_practice.status == STARTED:
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
                    currentRoutine=practiceDecisionSimulus1,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                practiceDecisionSimulus1.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practiceDecisionSimulus1.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "practiceDecisionSimulus1" ---
        for thisComponent in practiceDecisionSimulus1.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for practiceDecisionSimulus1
        practiceDecisionSimulus1.tStop = globalClock.getTime(format='float')
        practiceDecisionSimulus1.tStopRefresh = tThisFlipGlobal
        thisExp.addData('practiceDecisionSimulus1.stopped', practiceDecisionSimulus1.tStop)
        # Run 'End Routine' code from code_29
        # Hide dollar amount text components when practiceDecisionStimulus1 ends
        # This ensures clean transition to crosshair ITI
        if 'text_dollar_left_practice' in locals():
            text_dollar_left_practice.setAutoDraw(False)
            text_dollar_left_practice.opacity = 0
        if 'text_dollar_right_practice' in locals():
            text_dollar_right_practice.setAutoDraw(False)
            text_dollar_right_practice.opacity = 0
        if 'text_question1' in locals():
            text_question1.setAutoDraw(False)
            text_question1.opacity = 0
        
        # Clear any key presses
        try:
            event.clearEvents()
        except:
            pass
        
        
        # the Routine "practiceDecisionSimulus1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "crosshairPracticeDecision1" ---
        # create an object to store info about Routine crosshairPracticeDecision1
        crosshairPracticeDecision1 = data.Routine(
            name='crosshairPracticeDecision1',
            components=[text_crosshair_practice_decision1],
        )
        crosshairPracticeDecision1.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_41
        # Crosshair ITI 1 for practice decision trials - 1 second fixed duration
        # Shows crosshair between practiceDecisionStimulus1 and practiceDecisionStimulus2
        # Component: text_crosshair_practice_decision1 (or similar crosshair component)
        
        # IMPORTANT: Hide ALL previous dollar amount text components from practiceDecisionStimulus1
        # Force hide to ensure clean transition
        if 'text_dollar_left_practice' in locals():
            text_dollar_left_practice.setAutoDraw(False)
            text_dollar_left_practice.opacity = 0
            text_dollar_left_practice.text = ""  # Clear text
        if 'text_dollar_right_practice' in locals():
            text_dollar_right_practice.setAutoDraw(False)
            text_dollar_right_practice.opacity = 0
            text_dollar_right_practice.text = ""  # Clear text
        if 'text_question1' in locals():
            text_question1.setAutoDraw(False)
            text_question1.opacity = 0
        
        # Show crosshair - make sure it's visible
        if 'text_crosshair_practice_decision1' in locals():
            text_crosshair_practice_decision1.text = "+"
            try:
                text_crosshair_practice_decision1.setPos((0, 0))
            except AttributeError:
                text_crosshair_practice_decision1.pos = (0, 0)
            text_crosshair_practice_decision1.opacity = 1
            text_crosshair_practice_decision1.setAutoDraw(True)
            print("Showing crosshair ITI 1 for practice decision (1 second)")
        elif 'text_25' in locals():
            # Fallback component name
            text_25.text = "+"
            try:
                text_25.setPos((0, 0))
            except AttributeError:
                text_25.pos = (0, 0)
            text_25.opacity = 1
            text_25.setAutoDraw(True)
            print("Showing crosshair ITI 1 for practice decision (using text_25, 1 second)")
        else:
            print("WARNING: text_crosshair_practice_decision1 or text_25 component not found!")
            print("  Make sure crosshairPracticeDecision1 routine has a text component named 'text_crosshair_practice_decision1'")
        
        # Duration is fixed at 1 second for practice trials
        # IMPORTANT: In PsychoPy Builder, set the routine duration to 1.0 seconds
        # The routine should have a duration of 1.0 seconds (not infinite or 0)
        globals()['crosshair_practice_decision1_duration'] = 1.0
        print(f"Crosshair ITI 1 duration: 1.0 seconds (fixed for practice)")
        print(f"  NOTE: Make sure crosshairPracticeDecision1 routine duration is set to 1.0 seconds in Builder")
        
        
        # store start times for crosshairPracticeDecision1
        crosshairPracticeDecision1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        crosshairPracticeDecision1.tStart = globalClock.getTime(format='float')
        crosshairPracticeDecision1.status = STARTED
        thisExp.addData('crosshairPracticeDecision1.started', crosshairPracticeDecision1.tStart)
        crosshairPracticeDecision1.maxDuration = None
        # keep track of which components have finished
        crosshairPracticeDecision1Components = crosshairPracticeDecision1.components
        for thisComponent in crosshairPracticeDecision1.components:
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
        
        # --- Run Routine "crosshairPracticeDecision1" ---
        crosshairPracticeDecision1.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # if trial has changed, end Routine now
            if hasattr(thisPracticeDecisionLoop, 'status') and thisPracticeDecisionLoop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_crosshair_practice_decision1* updates
            
            # if text_crosshair_practice_decision1 is starting this frame...
            if text_crosshair_practice_decision1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_crosshair_practice_decision1.frameNStart = frameN  # exact frame index
                text_crosshair_practice_decision1.tStart = t  # local t and not account for scr refresh
                text_crosshair_practice_decision1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_crosshair_practice_decision1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_crosshair_practice_decision1.started')
                # update status
                text_crosshair_practice_decision1.status = STARTED
                text_crosshair_practice_decision1.setAutoDraw(True)
            
            # if text_crosshair_practice_decision1 is active this frame...
            if text_crosshair_practice_decision1.status == STARTED:
                # update params
                pass
            
            # if text_crosshair_practice_decision1 is stopping this frame...
            if text_crosshair_practice_decision1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_crosshair_practice_decision1.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_crosshair_practice_decision1.tStop = t  # not accounting for scr refresh
                    text_crosshair_practice_decision1.tStopRefresh = tThisFlipGlobal  # on global time
                    text_crosshair_practice_decision1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_crosshair_practice_decision1.stopped')
                    # update status
                    text_crosshair_practice_decision1.status = FINISHED
                    text_crosshair_practice_decision1.setAutoDraw(False)
            
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
                    currentRoutine=crosshairPracticeDecision1,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                crosshairPracticeDecision1.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in crosshairPracticeDecision1.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "crosshairPracticeDecision1" ---
        for thisComponent in crosshairPracticeDecision1.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for crosshairPracticeDecision1
        crosshairPracticeDecision1.tStop = globalClock.getTime(format='float')
        crosshairPracticeDecision1.tStopRefresh = tThisFlipGlobal
        thisExp.addData('crosshairPracticeDecision1.stopped', crosshairPracticeDecision1.tStop)
        # Run 'End Routine' code from code_41
        # Hide crosshair when routine ends
        if 'text_crosshair_practice_decision1' in locals():
            text_crosshair_practice_decision1.setAutoDraw(False)
            text_crosshair_practice_decision1.opacity = 0
        elif 'text_25' in locals():
            text_25.setAutoDraw(False)
            text_25.opacity = 0
        
        # Clear any key presses
        try:
            event.clearEvents()
        except:
            pass
        
        
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if crosshairPracticeDecision1.maxDurationReached:
            routineTimer.addTime(-crosshairPracticeDecision1.maxDuration)
        elif crosshairPracticeDecision1.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "practiceDecisionSimulus2" ---
        # create an object to store info about Routine practiceDecisionSimulus2
        practiceDecisionSimulus2 = data.Routine(
            name='practiceDecisionSimulus2',
            components=[text_question_3, text_25, text_dollar_left_practice_2, text_dollar_right_practice_2],
        )
        practiceDecisionSimulus2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_30
        # Practice decision - Second stimulus screen - shows second dollar amount on its side for 2 seconds
        # Components: text_question_3, text_dollar_left_practice, text_dollar_right_practice
        # Shows second dollar amount on left or right side for 2 seconds
        
        # Get practice_decision_index and practice_decision_block from globals
        practice_decision_index = globals().get('practice_decision_index', 0)
        practice_decision_block = globals().get('practice_decision_block', [])
        
        # DEBUG: Print block info
        print(f"DEBUG practiceDecisionStimulus2: practice_decision_index={practice_decision_index}, block_length={len(practice_decision_block) if practice_decision_block else 0}")
        
        if practice_decision_block and practice_decision_index >= 0 and practice_decision_index < len(practice_decision_block):
            current = practice_decision_block[practice_decision_index]
            second_dollar = current["secondDollar"]  # Dollar amount (e.g., "$5", "$1", "$10")
            second_side = current["secondSide"]
            
            # Show central fixation cross
            if 'text_question_3' in locals():
                text_question_3.text = "+"
                try:
                    text_question_3.setPos((0, 0))
                except AttributeError:
                    text_question_3.pos = (0, 0)
                text_question_3.opacity = 1
                text_question_3.setAutoDraw(True)
            
            # Hide previous crosshair
            if 'text_crosshair_practice_decision1' in locals():
                text_crosshair_practice_decision1.opacity = 0
                text_crosshair_practice_decision1.setAutoDraw(False)
            elif 'text_25' in locals():
                text_25.opacity = 0
                text_25.setAutoDraw(False)
            
            # Hide first dollar amount (from practiceDecisionStimulus1)
            if 'text_dollar_left_practice' in locals():
                text_dollar_left_practice.opacity = 0
                text_dollar_left_practice.setAutoDraw(False)
            if 'text_dollar_right_practice' in locals():
                text_dollar_right_practice.opacity = 0
                text_dollar_right_practice.setAutoDraw(False)
            
            # Show second dollar amount on its designated side (using _2 components)
            if second_side == "left":
                if 'text_dollar_left_practice_2' in locals():
                    text_dollar_left_practice_2.text = second_dollar
                    text_dollar_left_practice_2.opacity = 1
                    # Set larger font size for currency numbers
                    try:
                        text_dollar_left_practice_2.height = 0.1  # Larger font size (default is typically 0.05)
                    except AttributeError:
                        pass  # If height can't be set, continue anyway
                    text_dollar_left_practice_2.setAutoDraw(True)
            else:  # right
                if 'text_dollar_right_practice_2' in locals():
                    text_dollar_right_practice_2.text = second_dollar
                    text_dollar_right_practice_2.opacity = 1
                    # Set larger font size for currency numbers
                    try:
                        text_dollar_right_practice_2.height = 0.1  # Larger font size (default is typically 0.05)
                    except AttributeError:
                        pass  # If height can't be set, continue anyway
                    text_dollar_right_practice_2.setAutoDraw(True)
            
            print(f"Practice decision {practice_decision_index+1}/3: Showing {second_dollar} on {second_side} (2 seconds)")
        else:
            print(f"WARNING: Practice decision trial {practice_decision_index} out of range")
        
        
        # store start times for practiceDecisionSimulus2
        practiceDecisionSimulus2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        practiceDecisionSimulus2.tStart = globalClock.getTime(format='float')
        practiceDecisionSimulus2.status = STARTED
        thisExp.addData('practiceDecisionSimulus2.started', practiceDecisionSimulus2.tStart)
        practiceDecisionSimulus2.maxDuration = 2
        # keep track of which components have finished
        practiceDecisionSimulus2Components = practiceDecisionSimulus2.components
        for thisComponent in practiceDecisionSimulus2.components:
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
        
        # --- Run Routine "practiceDecisionSimulus2" ---
        practiceDecisionSimulus2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisPracticeDecisionLoop, 'status') and thisPracticeDecisionLoop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > practiceDecisionSimulus2.maxDuration-frameTolerance:
                practiceDecisionSimulus2.maxDurationReached = True
                continueRoutine = False
            
            # *text_question_3* updates
            
            # if text_question_3 is starting this frame...
            if text_question_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_question_3.frameNStart = frameN  # exact frame index
                text_question_3.tStart = t  # local t and not account for scr refresh
                text_question_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_question_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_question_3.started')
                # update status
                text_question_3.status = STARTED
                text_question_3.setAutoDraw(True)
            
            # if text_question_3 is active this frame...
            if text_question_3.status == STARTED:
                # update params
                pass
            
            # if text_question_3 is stopping this frame...
            if text_question_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_question_3.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_question_3.tStop = t  # not accounting for scr refresh
                    text_question_3.tStopRefresh = tThisFlipGlobal  # on global time
                    text_question_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_question_3.stopped')
                    # update status
                    text_question_3.status = FINISHED
                    text_question_3.setAutoDraw(False)
            
            # *text_25* updates
            
            # if text_25 is starting this frame...
            if text_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_25.frameNStart = frameN  # exact frame index
                text_25.tStart = t  # local t and not account for scr refresh
                text_25.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_25, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_25.started')
                # update status
                text_25.status = STARTED
                text_25.setAutoDraw(True)
            
            # if text_25 is active this frame...
            if text_25.status == STARTED:
                # update params
                pass
            
            # *text_dollar_left_practice_2* updates
            
            # if text_dollar_left_practice_2 is starting this frame...
            if text_dollar_left_practice_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_dollar_left_practice_2.frameNStart = frameN  # exact frame index
                text_dollar_left_practice_2.tStart = t  # local t and not account for scr refresh
                text_dollar_left_practice_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_dollar_left_practice_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_dollar_left_practice_2.started')
                # update status
                text_dollar_left_practice_2.status = STARTED
                text_dollar_left_practice_2.setAutoDraw(True)
            
            # if text_dollar_left_practice_2 is active this frame...
            if text_dollar_left_practice_2.status == STARTED:
                # update params
                pass
            
            # *text_dollar_right_practice_2* updates
            
            # if text_dollar_right_practice_2 is starting this frame...
            if text_dollar_right_practice_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_dollar_right_practice_2.frameNStart = frameN  # exact frame index
                text_dollar_right_practice_2.tStart = t  # local t and not account for scr refresh
                text_dollar_right_practice_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_dollar_right_practice_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_dollar_right_practice_2.started')
                # update status
                text_dollar_right_practice_2.status = STARTED
                text_dollar_right_practice_2.setAutoDraw(True)
            
            # if text_dollar_right_practice_2 is active this frame...
            if text_dollar_right_practice_2.status == STARTED:
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
                    currentRoutine=practiceDecisionSimulus2,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                practiceDecisionSimulus2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practiceDecisionSimulus2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "practiceDecisionSimulus2" ---
        for thisComponent in practiceDecisionSimulus2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for practiceDecisionSimulus2
        practiceDecisionSimulus2.tStop = globalClock.getTime(format='float')
        practiceDecisionSimulus2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('practiceDecisionSimulus2.stopped', practiceDecisionSimulus2.tStop)
        # Run 'End Routine' code from code_30
        # Hide dollar amount text components when practiceDecisionStimulus2 ends
        # This ensures clean transition to crosshair ITI
        if 'text_dollar_left_practice_2' in locals():
            text_dollar_left_practice_2.setAutoDraw(False)
            text_dollar_left_practice_2.opacity = 0
            text_dollar_left_practice_2.text = ""  # Clear text
        if 'text_dollar_right_practice_2' in locals():
            text_dollar_right_practice_2.setAutoDraw(False)
            text_dollar_right_practice_2.opacity = 0
            text_dollar_right_practice_2.text = ""  # Clear text
        if 'text_question_3' in locals():
            text_question_3.setAutoDraw(False)
            text_question_3.opacity = 0
        
        # Clear any key presses
        try:
            event.clearEvents()
        except:
            pass
        
        
        # the Routine "practiceDecisionSimulus2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "crosshairPracticeDecision2" ---
        # create an object to store info about Routine crosshairPracticeDecision2
        crosshairPracticeDecision2 = data.Routine(
            name='crosshairPracticeDecision2',
            components=[text_crosshair_practice_decision2],
        )
        crosshairPracticeDecision2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_42
        # Crosshair ITI 2 for practice decision trials - 1 second fixed duration
        # Shows crosshair between practiceDecisionStimulus2 and practiceDecisionMaking
        # Component: text_crosshair_practice_decision2 (or similar crosshair component)
        
        # IMPORTANT: Hide ALL previous dollar amount text components from practiceDecisionStimulus2
        # Force hide to ensure clean transition
        if 'text_dollar_left_practice_2' in locals():
            text_dollar_left_practice_2.setAutoDraw(False)
            text_dollar_left_practice_2.opacity = 0
            text_dollar_left_practice_2.text = ""  # Clear text
        if 'text_dollar_right_practice_2' in locals():
            text_dollar_right_practice_2.setAutoDraw(False)
            text_dollar_right_practice_2.opacity = 0
            text_dollar_right_practice_2.text = ""  # Clear text
        if 'text_question_3' in locals():
            text_question_3.setAutoDraw(False)
            text_question_3.opacity = 0
        if 'text_crosshair_practice_decision1' in locals():
            text_crosshair_practice_decision1.setAutoDraw(False)
            text_crosshair_practice_decision1.opacity = 0
        
        # Show crosshair - make sure it's visible
        if 'text_crosshair_practice_decision2' in locals():
            text_crosshair_practice_decision2.text = "+"
            try:
                text_crosshair_practice_decision2.setPos((0, 0))
            except AttributeError:
                text_crosshair_practice_decision2.pos = (0, 0)
            text_crosshair_practice_decision2.opacity = 1
            text_crosshair_practice_decision2.setAutoDraw(True)
            print("Showing crosshair ITI 2 for practice decision (1 second)")
        else:
            print("WARNING: text_crosshair_practice_decision2 component not found!")
            print("  Make sure crosshairPracticeDecision2 routine has a text component named 'text_crosshair_practice_decision2'")
        
        # Duration is fixed at 1 second for practice trials
        # IMPORTANT: In PsychoPy Builder, set the routine duration to 1.0 seconds
        # The routine should have a duration of 1.0 seconds (not infinite or 0)
        globals()['crosshair_practice_decision2_duration'] = 1.0
        print(f"Crosshair ITI 2 duration: 1.0 seconds (fixed for practice)")
        print(f"  NOTE: Make sure crosshairPracticeDecision2 routine duration is set to 1.0 seconds in Builder")
        
        
        # store start times for crosshairPracticeDecision2
        crosshairPracticeDecision2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        crosshairPracticeDecision2.tStart = globalClock.getTime(format='float')
        crosshairPracticeDecision2.status = STARTED
        thisExp.addData('crosshairPracticeDecision2.started', crosshairPracticeDecision2.tStart)
        crosshairPracticeDecision2.maxDuration = None
        # keep track of which components have finished
        crosshairPracticeDecision2Components = crosshairPracticeDecision2.components
        for thisComponent in crosshairPracticeDecision2.components:
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
        
        # --- Run Routine "crosshairPracticeDecision2" ---
        crosshairPracticeDecision2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # if trial has changed, end Routine now
            if hasattr(thisPracticeDecisionLoop, 'status') and thisPracticeDecisionLoop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_crosshair_practice_decision2* updates
            
            # if text_crosshair_practice_decision2 is starting this frame...
            if text_crosshair_practice_decision2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_crosshair_practice_decision2.frameNStart = frameN  # exact frame index
                text_crosshair_practice_decision2.tStart = t  # local t and not account for scr refresh
                text_crosshair_practice_decision2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_crosshair_practice_decision2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_crosshair_practice_decision2.started')
                # update status
                text_crosshair_practice_decision2.status = STARTED
                text_crosshair_practice_decision2.setAutoDraw(True)
            
            # if text_crosshair_practice_decision2 is active this frame...
            if text_crosshair_practice_decision2.status == STARTED:
                # update params
                pass
            
            # if text_crosshair_practice_decision2 is stopping this frame...
            if text_crosshair_practice_decision2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_crosshair_practice_decision2.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_crosshair_practice_decision2.tStop = t  # not accounting for scr refresh
                    text_crosshair_practice_decision2.tStopRefresh = tThisFlipGlobal  # on global time
                    text_crosshair_practice_decision2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_crosshair_practice_decision2.stopped')
                    # update status
                    text_crosshair_practice_decision2.status = FINISHED
                    text_crosshair_practice_decision2.setAutoDraw(False)
            
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
                    currentRoutine=crosshairPracticeDecision2,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                crosshairPracticeDecision2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in crosshairPracticeDecision2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "crosshairPracticeDecision2" ---
        for thisComponent in crosshairPracticeDecision2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for crosshairPracticeDecision2
        crosshairPracticeDecision2.tStop = globalClock.getTime(format='float')
        crosshairPracticeDecision2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('crosshairPracticeDecision2.stopped', crosshairPracticeDecision2.tStop)
        # Run 'End Routine' code from code_42
        # Hide crosshair when routine ends
        if 'text_crosshair_practice_decision2' in locals():
            text_crosshair_practice_decision2.setAutoDraw(False)
            text_crosshair_practice_decision2.opacity = 0
        
        # Clear any key presses
        try:
            event.clearEvents()
        except:
            pass
        
        
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if crosshairPracticeDecision2.maxDurationReached:
            routineTimer.addTime(-crosshairPracticeDecision2.maxDuration)
        elif crosshairPracticeDecision2.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "practiceDecisionMaking" ---
        # create an object to store info about Routine practiceDecisionMaking
        practiceDecisionMaking = data.Routine(
            name='practiceDecisionMaking',
            components=[text_question_4, text_dollar_right_practice_3, text_dollar_left_practice_3],
        )
        practiceDecisionMaking.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_31
        # Practice decision phase - both dollar amounts shown simultaneously (2 seconds fixed)
        # Components: text_question_4, text_dollar_left_practice, text_dollar_right_practice, mouse_2
        # Shows both dollar amounts together for decision
        import time
        
        # Get practice_decision_index and practice_decision_block from globals
        practice_decision_index = globals().get('practice_decision_index', 0)
        practice_decision_block = globals().get('practice_decision_block', [])
        
        if practice_decision_block and practice_decision_index >= 0 and practice_decision_index < len(practice_decision_block):
            current = practice_decision_block[practice_decision_index]
            leftDollar  = current["leftDollar"]   # Dollar amount for left (e.g., "$5")
            rightDollar = current["rightDollar"]  # Dollar amount for right (e.g., "$1")
            correct     = current["correct"]
            
            # Show central fixation cross
            if 'text_question_4' in locals():
                text_question_4.text = "+"
                try:
                    text_question_4.setPos((0, 0))
                except AttributeError:
                    text_question_4.pos = (0, 0)
                text_question_4.opacity = 1
                text_question_4.setAutoDraw(True)
            
            # Hide previous crosshair
            if 'text_crosshair_practice_decision2' in locals():
                text_crosshair_practice_decision2.opacity = 0
                text_crosshair_practice_decision2.setAutoDraw(False)
            
            # Hide dollar amounts from previous routines
            if 'text_dollar_left_practice' in locals():
                text_dollar_left_practice.opacity = 0
                text_dollar_left_practice.setAutoDraw(False)
            if 'text_dollar_right_practice' in locals():
                text_dollar_right_practice.opacity = 0
                text_dollar_right_practice.setAutoDraw(False)
            if 'text_dollar_left_practice_2' in locals():
                text_dollar_left_practice_2.opacity = 0
                text_dollar_left_practice_2.setAutoDraw(False)
            if 'text_dollar_right_practice_2' in locals():
                text_dollar_right_practice_2.opacity = 0
                text_dollar_right_practice_2.setAutoDraw(False)
            
            # Show both dollar amounts simultaneously (using _3 components)
            if 'text_dollar_left_practice_3' in locals():
                text_dollar_left_practice_3.text = leftDollar
                text_dollar_left_practice_3.opacity = 1
                # Set larger font size for currency numbers
                try:
                    text_dollar_left_practice_3.height = 0.1  # Larger font size (default is typically 0.05)
                except AttributeError:
                    pass  # If height can't be set, continue anyway
                text_dollar_left_practice_3.setAutoDraw(True)
            if 'text_dollar_right_practice_3' in locals():
                text_dollar_right_practice_3.text = rightDollar
                text_dollar_right_practice_3.opacity = 1
                # Set larger font size for currency numbers
                try:
                    text_dollar_right_practice_3.height = 0.1  # Larger font size (default is typically 0.05)
                except AttributeError:
                    pass  # If height can't be set, continue anyway
                text_dollar_right_practice_3.setAutoDraw(True)
            
            # Reset choice and start timer (for practice, allow responses during 2 second display)
            choice = ""
            decision_start_time = time.time()
            decision_timed_out = False
            
            # Store in globals for use in EachFrame
            globals()['choice'] = choice
            globals()['decision_start_time'] = decision_start_time
            globals()['decision_timed_out'] = False
            
            # Clear any key presses from previous routines ONCE at the start
            try:
                event.clearEvents()
                print(f"Cleared key buffer at practice decision start")
            except:
                pass
            
            # Set a small ignore window to prevent immediate key registration (0.1 seconds)
            ignore_keys_until = decision_start_time + 0.1
            globals()['ignore_keys_until'] = ignore_keys_until
            
            if 'mouse_2' in locals():
                mouse_2.clickReset()
            print(f"Practice decision {practice_decision_index+1}/3: {leftDollar} vs {rightDollar}, correct={correct} (2 seconds fixed)")
        else:
            # No more practice decision trials
            leftDollar = ""
            rightDollar = ""
            choice = ""
            print("No more practice decision trials available")
        
        
        # store start times for practiceDecisionMaking
        practiceDecisionMaking.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        practiceDecisionMaking.tStart = globalClock.getTime(format='float')
        practiceDecisionMaking.status = STARTED
        thisExp.addData('practiceDecisionMaking.started', practiceDecisionMaking.tStart)
        practiceDecisionMaking.maxDuration = 4
        # keep track of which components have finished
        practiceDecisionMakingComponents = practiceDecisionMaking.components
        for thisComponent in practiceDecisionMaking.components:
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
        
        # --- Run Routine "practiceDecisionMaking" ---
        practiceDecisionMaking.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisPracticeDecisionLoop, 'status') and thisPracticeDecisionLoop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > practiceDecisionMaking.maxDuration-frameTolerance:
                practiceDecisionMaking.maxDurationReached = True
                continueRoutine = False
            
            # *text_question_4* updates
            
            # if text_question_4 is starting this frame...
            if text_question_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_question_4.frameNStart = frameN  # exact frame index
                text_question_4.tStart = t  # local t and not account for scr refresh
                text_question_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_question_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_question_4.started')
                # update status
                text_question_4.status = STARTED
                text_question_4.setAutoDraw(True)
            
            # if text_question_4 is active this frame...
            if text_question_4.status == STARTED:
                # update params
                pass
            # Run 'Each Frame' code from code_31
            # Practice decision phase - check for response (2 seconds fixed duration)
            # Using keys 1/3: 1 = left image, 3 = right image
            import time
            
            # Get practice_decision_index from globals (needed for logging)
            practice_decision_index = globals().get('practice_decision_index', -1)
            
            # Get decision_start_time and ignore_keys_until from globals (set in BeginRoutine)
            decision_start_time = globals().get('decision_start_time', time.time())
            ignore_keys_until = globals().get('ignore_keys_until', decision_start_time + 0.1)
            
            # Initialize decision_timed_out if not already set
            decision_timed_out = globals().get('decision_timed_out', False)
            
            # Check for timeout (2 seconds max for practice)
            try:
                elapsed_time = time.time() - decision_start_time
                
                if elapsed_time >= 2.0:
                    # Timeout - no response (routine will end at 2 seconds fixed duration)
                    if not globals().get('choice', ""):
                        choice = ""
                        decision_rt = 2.0
                        decision_timed_out = True
                        # Store in globals for EndRoutine
                        globals()['decision_timed_out'] = True
                        globals()['decision_rt'] = 2.0
                        print(f"Practice decision {practice_decision_index+1}/3: No response within 2.0 seconds")
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
                                print(f"Practice decision {practice_decision_index+1}/3: Chose left (key 1, RT={decision_rt:.2f}s)")
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
                                print(f"Practice decision {practice_decision_index+1}/3: Chose right (key 3, RT={decision_rt:.2f}s)")
                                continueRoutine = False
                                # Clear events after processing
                                try:
                                    event.clearEvents()
                                except:
                                    pass
                                break
                    except (NameError, AttributeError):
                        # Fallback: Check for mouse click (using mouse_2 and correct image components)
                        if 'mouse_2' in locals() and 'image_left_left1' in locals() and 'image_right_right1' in locals():
                            if mouse_2.isPressedIn(image_left_left1):
                                choice = "left"
                                decision_rt = time.time() - decision_start_time
                                decision_timed_out = False
                                globals()['choice'] = choice
                                globals()['decision_rt'] = decision_rt
                                globals()['decision_timed_out'] = False
                                print(f"Practice decision {practice_decision_index+1}/3: Chose left (mouse, RT={decision_rt:.2f}s)")
                                continueRoutine = False
                            elif mouse_2.isPressedIn(image_right_right1):
                                choice = "right"
                                decision_rt = time.time() - decision_start_time
                                decision_timed_out = False
                                globals()['choice'] = choice
                                globals()['decision_rt'] = decision_rt
                                globals()['decision_timed_out'] = False
                                print(f"Practice decision {practice_decision_index+1}/3: Chose right (mouse, RT={decision_rt:.2f}s)")
                                continueRoutine = False
            
            
            
            # *text_dollar_right_practice_3* updates
            
            # if text_dollar_right_practice_3 is starting this frame...
            if text_dollar_right_practice_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_dollar_right_practice_3.frameNStart = frameN  # exact frame index
                text_dollar_right_practice_3.tStart = t  # local t and not account for scr refresh
                text_dollar_right_practice_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_dollar_right_practice_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_dollar_right_practice_3.started')
                # update status
                text_dollar_right_practice_3.status = STARTED
                text_dollar_right_practice_3.setAutoDraw(True)
            
            # if text_dollar_right_practice_3 is active this frame...
            if text_dollar_right_practice_3.status == STARTED:
                # update params
                pass
            
            # *text_dollar_left_practice_3* updates
            
            # if text_dollar_left_practice_3 is starting this frame...
            if text_dollar_left_practice_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_dollar_left_practice_3.frameNStart = frameN  # exact frame index
                text_dollar_left_practice_3.tStart = t  # local t and not account for scr refresh
                text_dollar_left_practice_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_dollar_left_practice_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_dollar_left_practice_3.started')
                # update status
                text_dollar_left_practice_3.status = STARTED
                text_dollar_left_practice_3.setAutoDraw(True)
            
            # if text_dollar_left_practice_3 is active this frame...
            if text_dollar_left_practice_3.status == STARTED:
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
                    currentRoutine=practiceDecisionMaking,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                practiceDecisionMaking.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practiceDecisionMaking.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "practiceDecisionMaking" ---
        for thisComponent in practiceDecisionMaking.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for practiceDecisionMaking
        practiceDecisionMaking.tStop = globalClock.getTime(format='float')
        practiceDecisionMaking.tStopRefresh = tThisFlipGlobal
        thisExp.addData('practiceDecisionMaking.stopped', practiceDecisionMaking.tStop)
        # Run 'End Routine' code from code_31
        # Get practice_decision_index and practice_decision_block from globals
        practice_decision_index = globals().get('practice_decision_index', -1)
        practice_decision_block = globals().get('practice_decision_block', [])
        
        # Get choice, decision_rt, and decision_timed_out from globals (set in EachFrame)
        choice = globals().get('choice', "")
        decision_rt = globals().get('decision_rt', 4.0)
        decision_timed_out = globals().get('decision_timed_out', False)
        
        # Get leftDollar and rightDollar from current trial
        if practice_decision_block and practice_decision_index >= 0 and practice_decision_index < len(practice_decision_block):
            current = practice_decision_block[practice_decision_index]
            leftDollar = current.get("leftDollar", "")
            rightDollar = current.get("rightDollar", "")
            correct = current.get("correct", "")
        else:
            leftDollar = ""
            rightDollar = ""
            correct = ""
        
        # Determine correctness
        was_correct = (choice == correct) if choice else False
        
        # Convert reaction time to milliseconds
        decision_rt_value = decision_rt if decision_rt is not None else 4.0
        decision_rt_ms = int(decision_rt_value * 1000)
        
        # Calculate timeout duration for timeout screen (1.5 seconds if timed out, 0 otherwise)
        decision_timeout_duration = 1.5 if decision_timed_out else 0.0
        globals()['decision_timeout_duration'] = decision_timeout_duration
        
        # Log the practice decision data (for debugging/monitoring, not saved to CSV)
        print(f"Practice decision {practice_decision_index+1}/3: {choice} (correct: {correct}, accurate: {was_correct}, RT: {decision_rt_value:.2f}s, timed_out: {decision_timed_out})")
        print(f"Practice decision EndRoutine: RT={decision_rt_value:.3f}s={decision_rt_ms}ms, responded_in_time={not decision_timed_out}, timed_out={decision_timed_out}")
        
        # Hide dollar amount text components (from practiceDecisionMaking - _3 components)
        if 'text_dollar_left_practice_3' in locals():
            text_dollar_left_practice_3.setAutoDraw(False)
            text_dollar_left_practice_3.opacity = 0
        if 'text_dollar_right_practice_3' in locals():
            text_dollar_right_practice_3.setAutoDraw(False)
            text_dollar_right_practice_3.opacity = 0
        if 'text_question_4' in locals():
            text_question_4.setAutoDraw(False)
            text_question_4.opacity = 0
        
        # Practice decision trials don't increment the regular decision_index
        # They're separate and just for practice
        
        
        # the Routine "practiceDecisionMaking" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "crosshairPracticeDecision3" ---
        # create an object to store info about Routine crosshairPracticeDecision3
        crosshairPracticeDecision3 = data.Routine(
            name='crosshairPracticeDecision3',
            components=[text_crosshair_practice_decision3],
        )
        crosshairPracticeDecision3.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_43
        # Crosshair ITI 3 for practice decision trials - 2 seconds fixed duration
        # Shows crosshair after practiceDecisionMaking (before next trial or end)
        # Component: text_crosshair_practice_decision3 (or similar crosshair component)
        
        # IMPORTANT: Hide ALL previous dollar amount text components from practiceDecisionMaking
        # Force hide to ensure clean transition
        if 'text_dollar_left_practice_3' in locals():
            text_dollar_left_practice_3.setAutoDraw(False)
            text_dollar_left_practice_3.opacity = 0
            text_dollar_left_practice_3.text = ""  # Clear text
        if 'text_dollar_right_practice_3' in locals():
            text_dollar_right_practice_3.setAutoDraw(False)
            text_dollar_right_practice_3.opacity = 0
            text_dollar_right_practice_3.text = ""  # Clear text
        if 'text_question_4' in locals():
            text_question_4.setAutoDraw(False)
            text_question_4.opacity = 0
        if 'text_crosshair_practice_decision2' in locals():
            text_crosshair_practice_decision2.setAutoDraw(False)
            text_crosshair_practice_decision2.opacity = 0
        
        # Show crosshair - make sure it's visible
        if 'text_crosshair_practice_decision3' in locals():
            text_crosshair_practice_decision3.text = "+"
            try:
                text_crosshair_practice_decision3.setPos((0, 0))
            except AttributeError:
                text_crosshair_practice_decision3.pos = (0, 0)
            text_crosshair_practice_decision3.opacity = 1
            text_crosshair_practice_decision3.setAutoDraw(True)
            print("Showing crosshair ITI 3 for practice decision (2 seconds)")
        else:
            print("WARNING: text_crosshair_practice_decision3 component not found!")
            print("  Make sure crosshairPracticeDecision3 routine has a text component named 'text_crosshair_practice_decision3'")
        
        # Duration is fixed at 2 seconds for practice trials (ITI between trials)
        # IMPORTANT: In PsychoPy Builder, set the routine duration to 2.0 seconds
        # The routine should have a duration of 2.0 seconds (not infinite or 0)
        globals()['crosshair_practice_decision3_duration'] = 2.0
        print(f"Crosshair ITI 3 duration: 2.0 seconds (fixed for practice)")
        print(f"  NOTE: Make sure crosshairPracticeDecision3 routine duration is set to 2.0 seconds in Builder")
        
        
        # store start times for crosshairPracticeDecision3
        crosshairPracticeDecision3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        crosshairPracticeDecision3.tStart = globalClock.getTime(format='float')
        crosshairPracticeDecision3.status = STARTED
        thisExp.addData('crosshairPracticeDecision3.started', crosshairPracticeDecision3.tStart)
        crosshairPracticeDecision3.maxDuration = None
        # keep track of which components have finished
        crosshairPracticeDecision3Components = crosshairPracticeDecision3.components
        for thisComponent in crosshairPracticeDecision3.components:
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
        
        # --- Run Routine "crosshairPracticeDecision3" ---
        crosshairPracticeDecision3.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # if trial has changed, end Routine now
            if hasattr(thisPracticeDecisionLoop, 'status') and thisPracticeDecisionLoop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_crosshair_practice_decision3* updates
            
            # if text_crosshair_practice_decision3 is starting this frame...
            if text_crosshair_practice_decision3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_crosshair_practice_decision3.frameNStart = frameN  # exact frame index
                text_crosshair_practice_decision3.tStart = t  # local t and not account for scr refresh
                text_crosshair_practice_decision3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_crosshair_practice_decision3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_crosshair_practice_decision3.started')
                # update status
                text_crosshair_practice_decision3.status = STARTED
                text_crosshair_practice_decision3.setAutoDraw(True)
            
            # if text_crosshair_practice_decision3 is active this frame...
            if text_crosshair_practice_decision3.status == STARTED:
                # update params
                pass
            
            # if text_crosshair_practice_decision3 is stopping this frame...
            if text_crosshair_practice_decision3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_crosshair_practice_decision3.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_crosshair_practice_decision3.tStop = t  # not accounting for scr refresh
                    text_crosshair_practice_decision3.tStopRefresh = tThisFlipGlobal  # on global time
                    text_crosshair_practice_decision3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_crosshair_practice_decision3.stopped')
                    # update status
                    text_crosshair_practice_decision3.status = FINISHED
                    text_crosshair_practice_decision3.setAutoDraw(False)
            
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
                    currentRoutine=crosshairPracticeDecision3,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                crosshairPracticeDecision3.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in crosshairPracticeDecision3.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "crosshairPracticeDecision3" ---
        for thisComponent in crosshairPracticeDecision3.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for crosshairPracticeDecision3
        crosshairPracticeDecision3.tStop = globalClock.getTime(format='float')
        crosshairPracticeDecision3.tStopRefresh = tThisFlipGlobal
        thisExp.addData('crosshairPracticeDecision3.stopped', crosshairPracticeDecision3.tStop)
        # Run 'End Routine' code from code_43
        # Hide crosshair when routine ends
        if 'text_crosshair_practice_decision3' in locals():
            text_crosshair_practice_decision3.setAutoDraw(False)
            text_crosshair_practice_decision3.opacity = 0
        
        # Clear any key presses
        try:
            event.clearEvents()
        except:
            pass
        
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if crosshairPracticeDecision3.maxDurationReached:
            routineTimer.addTime(-crosshairPracticeDecision3.maxDuration)
        elif crosshairPracticeDecision3.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        # mark thisPracticeDecisionLoop as finished
        if hasattr(thisPracticeDecisionLoop, 'status'):
            thisPracticeDecisionLoop.status = FINISHED
        # if awaiting a pause, pause now
        if practiceDecisionLoop.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            practiceDecisionLoop.status = STARTED
        thisExp.nextEntry()
        
    # completed 3.0 repeats of 'practiceDecisionLoop'
    practiceDecisionLoop.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "taskStartSoonBlock3" ---
    # create an object to store info about Routine taskStartSoonBlock3
    taskStartSoonBlock3 = data.Routine(
        name='taskStartSoonBlock3',
        components=[text_task_start_soon_block3],
    )
    taskStartSoonBlock3.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_32
    # "Task will start soon. Press 2 to continue" screen - for third block (decision phase)
    # Shows after practice decision trials complete
    # Component: text_task_start_soon_block3 (or similar text component)
    
    # Clear any previous key presses IMMEDIATELY to prevent carryover
    try:
        event.clearEvents()
    except:
        pass
    
    # Set a timestamp to ignore any keys pressed before this routine started
    import time
    globals()['taskStartSoonBlock3_start_time'] = time.time()
    
    # Display task start message
    if 'text_task_start_soon_block3' in locals():
        text_task_start_soon_block3.text = "The task will start soon. Press C to continue"
        text_task_start_soon_block3.opacity = 1
        text_task_start_soon_block3.setAutoDraw(True)
        print("Task start soon screen displayed (for Block 3 - decision phase)")
    else:
        print("WARNING: text_task_start_soon_block3 component not found!")
    
    
    
    
    
    
    # store start times for taskStartSoonBlock3
    taskStartSoonBlock3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    taskStartSoonBlock3.tStart = globalClock.getTime(format='float')
    taskStartSoonBlock3.status = STARTED
    thisExp.addData('taskStartSoonBlock3.started', taskStartSoonBlock3.tStart)
    taskStartSoonBlock3.maxDuration = None
    # keep track of which components have finished
    taskStartSoonBlock3Components = taskStartSoonBlock3.components
    for thisComponent in taskStartSoonBlock3.components:
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
    
    # --- Run Routine "taskStartSoonBlock3" ---
    taskStartSoonBlock3.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_32
        # Task start soon Block 3 - wait for key press '2' to continue
        # Check for key press '2' to continue to scanner sync
        import time
        
        # Only accept keys pressed AFTER this routine started (ignore carryover)
        routine_start_time = globals().get('taskStartSoonBlock3_start_time', time.time())
        current_time = time.time()
        
        # Only process keys if at least 0.1 seconds have passed since routine started
        if current_time - routine_start_time >= 0.1:
            try:
                keys = event.getKeys(keyList=['c', 'C'])
                if keys:
                    # Key 2 pressed - continue to scanner sync
                    print("Task start soon Block 3: Key C pressed, continuing to scanner sync")
                    continueRoutine = False
                    event.clearEvents()
            except:
                pass
        
        
        
        
        
        
        
        # *text_task_start_soon_block3* updates
        
        # if text_task_start_soon_block3 is starting this frame...
        if text_task_start_soon_block3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_task_start_soon_block3.frameNStart = frameN  # exact frame index
            text_task_start_soon_block3.tStart = t  # local t and not account for scr refresh
            text_task_start_soon_block3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_task_start_soon_block3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_task_start_soon_block3.started')
            # update status
            text_task_start_soon_block3.status = STARTED
            text_task_start_soon_block3.setAutoDraw(True)
        
        # if text_task_start_soon_block3 is active this frame...
        if text_task_start_soon_block3.status == STARTED:
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
                currentRoutine=taskStartSoonBlock3,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            taskStartSoonBlock3.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in taskStartSoonBlock3.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "taskStartSoonBlock3" ---
    for thisComponent in taskStartSoonBlock3.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for taskStartSoonBlock3
    taskStartSoonBlock3.tStop = globalClock.getTime(format='float')
    taskStartSoonBlock3.tStopRefresh = tThisFlipGlobal
    thisExp.addData('taskStartSoonBlock3.stopped', taskStartSoonBlock3.tStop)
    thisExp.nextEntry()
    # the Routine "taskStartSoonBlock3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "scannerSyncBlock3" ---
    # create an object to store info about Routine scannerSyncBlock3
    scannerSyncBlock3 = data.Routine(
        name='scannerSyncBlock3',
        components=[text_scanner_wait_block3],
    )
    scannerSyncBlock3.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_33
    # MRI Scanner sync Block 3 - wait for scanner trigger (key '5')
    # Shows after taskStartSoonBlock3 completes
    # Component: text_scanner_wait_block3 (or similar text component)
    
    # Clear any previous key presses IMMEDIATELY to prevent carryover
    try:
        event.clearEvents()
    except:
        pass
    
    # Set a timestamp to ignore any keys pressed before this routine started
    import time
    globals()['scannerSyncBlock3_start_time'] = time.time()
    
    # Display waiting message
    if 'text_scanner_wait_block3' in locals():
        text_scanner_wait_block3.text = "Waiting for the scanner to start..."
        text_scanner_wait_block3.opacity = 1
        text_scanner_wait_block3.setAutoDraw(True)
        print("Scanner sync Block 3: Waiting for trigger '5' from MRI scanner")
    else:
        print("WARNING: text_scanner_wait_block3 component not found!")
    
    
    
    
    
    
    # store start times for scannerSyncBlock3
    scannerSyncBlock3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    scannerSyncBlock3.tStart = globalClock.getTime(format='float')
    scannerSyncBlock3.status = STARTED
    thisExp.addData('scannerSyncBlock3.started', scannerSyncBlock3.tStart)
    scannerSyncBlock3.maxDuration = None
    # keep track of which components have finished
    scannerSyncBlock3Components = scannerSyncBlock3.components
    for thisComponent in scannerSyncBlock3.components:
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
    
    # --- Run Routine "scannerSyncBlock3" ---
    scannerSyncBlock3.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_33
        # Scanner sync Block 3 - wait for MRI scanner trigger (key '5')
        # The MRI sends '5' when it's ready
        # Only accept keys pressed AFTER this routine started (ignore carryover)
        import time
        
        routine_start_time = globals().get('scannerSyncBlock3_start_time', time.time())
        current_time = time.time()
        
        # Only process keys if at least 0.1 seconds have passed since routine started
        if current_time - routine_start_time >= 0.1:
            try:
                keys = event.getKeys(keyList=['5', 'num_5'])
                if keys:
                    # Scanner trigger received - continue to next screen
                    print("Scanner sync Block 3: Trigger '5' received from MRI scanner, continuing")
                    continueRoutine = False
                    event.clearEvents()
            except:
                pass
        
        
        
        
        
        
        
        # *text_scanner_wait_block3* updates
        
        # if text_scanner_wait_block3 is starting this frame...
        if text_scanner_wait_block3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_scanner_wait_block3.frameNStart = frameN  # exact frame index
            text_scanner_wait_block3.tStart = t  # local t and not account for scr refresh
            text_scanner_wait_block3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_scanner_wait_block3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_scanner_wait_block3.started')
            # update status
            text_scanner_wait_block3.status = STARTED
            text_scanner_wait_block3.setAutoDraw(True)
        
        # if text_scanner_wait_block3 is active this frame...
        if text_scanner_wait_block3.status == STARTED:
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
                currentRoutine=scannerSyncBlock3,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            scannerSyncBlock3.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in scannerSyncBlock3.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "scannerSyncBlock3" ---
    for thisComponent in scannerSyncBlock3.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for scannerSyncBlock3
    scannerSyncBlock3.tStop = globalClock.getTime(format='float')
    scannerSyncBlock3.tStopRefresh = tThisFlipGlobal
    thisExp.addData('scannerSyncBlock3.stopped', scannerSyncBlock3.tStop)
    thisExp.nextEntry()
    # the Routine "scannerSyncBlock3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "crosshair3Block3" ---
    # create an object to store info about Routine crosshair3Block3
    crosshair3Block3 = data.Routine(
        name='crosshair3Block3',
        components=[text_crosshair3_block3],
    )
    crosshair3Block3.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_34
    # Crosshair 3 Block 3 - 2 second fixation cross before Block 3 (decision phase)
    # Component: text_crosshair3_block3 (or similar text component)
    
    # Show fixation cross
    if 'text_crosshair3_block3' in locals():
        text_crosshair3_block3.text = "+"
        try:
            text_crosshair3_block3.setPos((0, 0))
        except AttributeError:
            text_crosshair3_block3.pos = (0, 0)
        text_crosshair3_block3.opacity = 1
        text_crosshair3_block3.setAutoDraw(True)
        print("Crosshair 3 Block 3: Showing fixation cross (2 seconds)")
    else:
        print("WARNING: text_crosshair3_block3 component not found!")
    
    
    # store start times for crosshair3Block3
    crosshair3Block3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    crosshair3Block3.tStart = globalClock.getTime(format='float')
    crosshair3Block3.status = STARTED
    thisExp.addData('crosshair3Block3.started', crosshair3Block3.tStart)
    crosshair3Block3.maxDuration = None
    # keep track of which components have finished
    crosshair3Block3Components = crosshair3Block3.components
    for thisComponent in crosshair3Block3.components:
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
    
    # --- Run Routine "crosshair3Block3" ---
    crosshair3Block3.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_crosshair3_block3* updates
        
        # if text_crosshair3_block3 is starting this frame...
        if text_crosshair3_block3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_crosshair3_block3.frameNStart = frameN  # exact frame index
            text_crosshair3_block3.tStart = t  # local t and not account for scr refresh
            text_crosshair3_block3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_crosshair3_block3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_crosshair3_block3.started')
            # update status
            text_crosshair3_block3.status = STARTED
            text_crosshair3_block3.setAutoDraw(True)
        
        # if text_crosshair3_block3 is active this frame...
        if text_crosshair3_block3.status == STARTED:
            # update params
            pass
        
        # if text_crosshair3_block3 is stopping this frame...
        if text_crosshair3_block3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_crosshair3_block3.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text_crosshair3_block3.tStop = t  # not accounting for scr refresh
                text_crosshair3_block3.tStopRefresh = tThisFlipGlobal  # on global time
                text_crosshair3_block3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_crosshair3_block3.stopped')
                # update status
                text_crosshair3_block3.status = FINISHED
                text_crosshair3_block3.setAutoDraw(False)
        
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
                currentRoutine=crosshair3Block3,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            crosshair3Block3.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in crosshair3Block3.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "crosshair3Block3" ---
    for thisComponent in crosshair3Block3.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for crosshair3Block3
    crosshair3Block3.tStop = globalClock.getTime(format='float')
    crosshair3Block3.tStopRefresh = tThisFlipGlobal
    thisExp.addData('crosshair3Block3.stopped', crosshair3Block3.tStop)
    # Run 'End Routine' code from code_34
    # Hide crosshair
    if 'text_crosshair3_block3' in locals():
        text_crosshair3_block3.setAutoDraw(False)
        text_crosshair3_block3.opacity = 0
    
    
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if crosshair3Block3.maxDurationReached:
        routineTimer.addTime(-crosshair3Block3.maxDuration)
    elif crosshair3Block3.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "scannerWaitBlock3" ---
    # create an object to store info about Routine scannerWaitBlock3
    scannerWaitBlock3 = data.Routine(
        name='scannerWaitBlock3',
        components=[image_scanner_wait_block3],
    )
    scannerWaitBlock3.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_35
    # Scanner wait Block 3 - shows wait image for 2 seconds before Block 3 (decision phase)
    # Component: image_scanner_wait_block3 (or similar image component)
    
    # Show wait image
    if 'image_scanner_wait_block3' in locals():
        image_scanner_wait_block3.opacity = 1
        image_scanner_wait_block3.setAutoDraw(True)
        print("Scanner wait Block 3: Showing wait image (2 seconds)")
    else:
        print("WARNING: image_scanner_wait_block3 component not found!")
    
    
    # store start times for scannerWaitBlock3
    scannerWaitBlock3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    scannerWaitBlock3.tStart = globalClock.getTime(format='float')
    scannerWaitBlock3.status = STARTED
    thisExp.addData('scannerWaitBlock3.started', scannerWaitBlock3.tStart)
    scannerWaitBlock3.maxDuration = None
    # keep track of which components have finished
    scannerWaitBlock3Components = scannerWaitBlock3.components
    for thisComponent in scannerWaitBlock3.components:
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
    
    # --- Run Routine "scannerWaitBlock3" ---
    scannerWaitBlock3.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_scanner_wait_block3* updates
        
        # if image_scanner_wait_block3 is starting this frame...
        if image_scanner_wait_block3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_scanner_wait_block3.frameNStart = frameN  # exact frame index
            image_scanner_wait_block3.tStart = t  # local t and not account for scr refresh
            image_scanner_wait_block3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_scanner_wait_block3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_scanner_wait_block3.started')
            # update status
            image_scanner_wait_block3.status = STARTED
            image_scanner_wait_block3.setAutoDraw(True)
        
        # if image_scanner_wait_block3 is active this frame...
        if image_scanner_wait_block3.status == STARTED:
            # update params
            pass
        
        # if image_scanner_wait_block3 is stopping this frame...
        if image_scanner_wait_block3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_scanner_wait_block3.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                image_scanner_wait_block3.tStop = t  # not accounting for scr refresh
                image_scanner_wait_block3.tStopRefresh = tThisFlipGlobal  # on global time
                image_scanner_wait_block3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_scanner_wait_block3.stopped')
                # update status
                image_scanner_wait_block3.status = FINISHED
                image_scanner_wait_block3.setAutoDraw(False)
        
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
                currentRoutine=scannerWaitBlock3,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            scannerWaitBlock3.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in scannerWaitBlock3.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "scannerWaitBlock3" ---
    for thisComponent in scannerWaitBlock3.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for scannerWaitBlock3
    scannerWaitBlock3.tStop = globalClock.getTime(format='float')
    scannerWaitBlock3.tStopRefresh = tThisFlipGlobal
    thisExp.addData('scannerWaitBlock3.stopped', scannerWaitBlock3.tStop)
    # Run 'End Routine' code from code_35
    # Hide wait image
    if 'image_scanner_wait_block3' in locals():
        image_scanner_wait_block3.setAutoDraw(False)
        image_scanner_wait_block3.opacity = 0
    
    
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if scannerWaitBlock3.maxDurationReached:
        routineTimer.addTime(-scannerWaitBlock3.maxDuration)
    elif scannerWaitBlock3.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "startTaskBlock3" ---
    # create an object to store info about Routine startTaskBlock3
    startTaskBlock3 = data.Routine(
        name='startTaskBlock3',
        components=[text_26],
    )
    startTaskBlock3.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_36
    # Start task Block 3 - 1 second before Block 3 (decision phase) begins
    # Component: text_start_task_block3 (or similar text component, optional)
    
    # This is just a brief pause before Block 3 decision trials start
    # You can add text here if needed, or leave it empty
    print("Start task Block 3: Brief pause before decision trials (1 second)")
    
    
    # store start times for startTaskBlock3
    startTaskBlock3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    startTaskBlock3.tStart = globalClock.getTime(format='float')
    startTaskBlock3.status = STARTED
    thisExp.addData('startTaskBlock3.started', startTaskBlock3.tStart)
    startTaskBlock3.maxDuration = None
    # keep track of which components have finished
    startTaskBlock3Components = startTaskBlock3.components
    for thisComponent in startTaskBlock3.components:
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
    
    # --- Run Routine "startTaskBlock3" ---
    startTaskBlock3.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 10.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_26* updates
        
        # if text_26 is starting this frame...
        if text_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_26.frameNStart = frameN  # exact frame index
            text_26.tStart = t  # local t and not account for scr refresh
            text_26.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_26, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_26.started')
            # update status
            text_26.status = STARTED
            text_26.setAutoDraw(True)
        
        # if text_26 is active this frame...
        if text_26.status == STARTED:
            # update params
            pass
        
        # if text_26 is stopping this frame...
        if text_26.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_26.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                text_26.tStop = t  # not accounting for scr refresh
                text_26.tStopRefresh = tThisFlipGlobal  # on global time
                text_26.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_26.stopped')
                # update status
                text_26.status = FINISHED
                text_26.setAutoDraw(False)
        
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
                currentRoutine=startTaskBlock3,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            startTaskBlock3.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in startTaskBlock3.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "startTaskBlock3" ---
    for thisComponent in startTaskBlock3.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for startTaskBlock3
    startTaskBlock3.tStop = globalClock.getTime(format='float')
    startTaskBlock3.tStopRefresh = tThisFlipGlobal
    thisExp.addData('startTaskBlock3.stopped', startTaskBlock3.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if startTaskBlock3.maxDurationReached:
        routineTimer.addTime(-startTaskBlock3.maxDuration)
    elif startTaskBlock3.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-10.000000)
    thisExp.nextEntry()
    
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
            
            # Show central fixation cross
            if 'text_question' in locals():
                text_question.text = "+"
                try:
                    text_question.setPos((0, 0))
                except AttributeError:
                    text_question.pos = (0, 0)
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
            
            # Show central fixation cross
            if 'text_question_2' in locals():
                text_question_2.text = "+"
                try:
                    text_question_2.setPos((0, 0))
                except AttributeError:
                    text_question_2.pos = (0, 0)
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
        # Decision phase - both fruits shown simultaneously (2 seconds fixed)
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
            
            # IMPORTANT: Maintain the sides where each fruit appeared individually
            # firstFruit appeared on firstSide, secondFruit appeared on secondSide (opposite side)
            # They should maintain these positions when shown together
            first_fruit = current["firstFruit"]
            first_side = current["firstSide"]
            second_fruit = current["secondFruit"]
            
            # Determine which fruit goes on left and which on right based on where they appeared individually
            # Since firstFruit and secondFruit appear on opposite sides:
            # - If firstFruit was on left, it stays on left; secondFruit (on right) stays on right
            # - If firstFruit was on right, it stays on right; secondFruit (on left) stays on left
            if first_side == "left":
                leftFile = first_fruit   # firstFruit was on left, stays on left
                rightFile = second_fruit  # secondFruit was on right, stays on right
            else:  # first_side == "right"
                leftFile = second_fruit   # secondFruit was on left, stays on left
                rightFile = first_fruit   # firstFruit was on right, stays on right
            
            # Recalculate correct side based on actual positions
            # Get fruit values to determine which side is correct
            left_val = current.get("leftVal", 0)  # Value of fruit originally on left
            right_val = current.get("rightVal", 0)  # Value of fruit originally on right
            
            # But we need the values of the fruits in their actual positions
            # Get fruit_values dictionary to look up actual values
            fruit_values = globals().get('fruit_values', {})
            actual_left_val = fruit_values.get(leftFile, 0)
            actual_right_val = fruit_values.get(rightFile, 0)
            
            # Correct side is the side with the higher value fruit
            correct = "left" if actual_left_val > actual_right_val else "right"
            
            # Store correct value in globals for use in EndRoutine
            globals()['decision_correct_side'] = correct
            
            # Show central fixation cross
            if 'text_question_1' in locals():
                text_question_1.text = "+"
                try:
                    text_question_1.setPos((0, 0))
                except AttributeError:
                    text_question_1.pos = (0, 0)
                text_question_1.opacity = 1
                text_question_1.setAutoDraw(True)
            
            # Hide previous crosshair
            if 'text_16' in locals():
                text_16.opacity = 0
                text_16.setAutoDraw(False)
            
            # Set both images - maintain positions from individual presentations
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
            # Clear prior RT so timeouts can't accidentally inherit a previous trial's RT
            globals()['decision_rt'] = None
            
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
            
            # Debug: Show which fruits appeared where individually
            print(f"Decision {decision_index+1}: {first_fruit} (was on {first_side}) vs {second_fruit} (was on {second_side})")
            print(f"  Final positions: {leftFile} (left) vs {rightFile} (right), correct={correct}")
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
        decisionMaking.maxDuration = 2
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
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > decisionMaking.maxDuration-frameTolerance:
                decisionMaking.maxDurationReached = True
                continueRoutine = False
            
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
                if tThisFlipGlobal > mouse_2.tStartRefresh + 2-frameTolerance:
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
            # Decision phase - check for response
            # Using keys 1/3: 1 = left image, 3 = right image
            import time
            
            # Get decision_index from globals (needed for logging)
            decision_index = globals().get('decision_index', 0)
            
            # Get decision_start_time and ignore_keys_until from globals (set in BeginRoutine)
            decision_start_time = globals().get('decision_start_time', time.time())
            ignore_keys_until = globals().get('ignore_keys_until', decision_start_time + 0.1)
            
            # Initialize decision_timed_out if not already set
            decision_timed_out = globals().get('decision_timed_out', False)
            
            # Get the actual timeout duration from configuration (set in startTaskBeginExperiment.py)
            # This is configurable via DECISION_TIMEOUT_DURATION global variable
            decision_timeout_duration = globals().get('DECISION_TIMEOUT_DURATION', 4.0)
            try:
                # Also try to get from routine duration if available (for Builder compatibility)
                if 'decisionMaking' in locals():
                    if hasattr(decisionMaking, 'duration'):
                        routine_duration = float(decisionMaking.duration)
                        if routine_duration > 0:
                            decision_timeout_duration = routine_duration
                    elif hasattr(decisionMaking, 'stopVal'):
                        routine_duration = float(decisionMaking.stopVal)
                        if routine_duration > 0:
                            decision_timeout_duration = routine_duration
            except:
                # Use configured default
                pass
            
            # Store in globals for use in EndRoutine
            globals()['decision_timeout_duration'] = decision_timeout_duration
            
            # Check for timeout (use actual duration from Builder, not hardcoded 2.0)
            try:
                elapsed_time = time.time() - decision_start_time
                
                if elapsed_time >= decision_timeout_duration:
                    # Timeout - no response (routine will end at the actual timeout duration)
                    if not globals().get('choice', ""):
                        choice = ""
                        decision_rt = decision_timeout_duration  # Use actual timeout duration, not hardcoded 2.0
                        decision_timed_out = True
                        # Store in globals for EndRoutine
                        globals()['decision_timed_out'] = True
                        globals()['decision_rt'] = decision_timeout_duration
                        print(f"Decision {decision_index+1}: No response within {decision_timeout_duration:.1f} seconds")
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
        # Response limit (seconds): global default
        decision_response_limit = globals().get('DECISION_TIMEOUT_DURATION', 2.0)
        decision_rt = globals().get('decision_rt', None)
        decision_timed_out = globals().get('decision_timed_out', False)
        
        # Get leftFile and rightFile from current trial
        if decision_block:
            trial_idx = decision_index % len(decision_block)
            current = decision_block[trial_idx]
            # Get actual left/right files from BeginRoutine (which maintains positions from individual presentations)
            # But we need to recalculate them here too, or get from globals
            firstFile = current.get("firstFruit", "")
            firstSide = current.get("firstSide", "")
            secondFruit = current.get("secondFruit", "")
            
            # Recalculate leftFile and rightFile based on where fruits appeared individually
            if firstSide == "left":
                leftFile = firstFile
                rightFile = secondFruit
            else:  # firstSide == "right"
                leftFile = secondFruit
                rightFile = firstFile
            
            # Get correct side from globals (recalculated in BeginRoutine based on actual positions)
            correct = globals().get('decision_correct_side', current.get("correct", ""))
        else:
            leftFile = "images/blank.png"
            rightFile = "images/blank.png"
            firstFile = ""
            firstSide = ""
            correct = ""
        
        # Determine correctness
        was_correct = (choice == correct) if choice else False
        
        # Decision RT value (seconds)
        if decision_timed_out:
            decision_rt_value = decision_response_limit
        else:
            decision_rt_value = decision_rt if decision_rt is not None else 0.0
        decision_rt_ms = int(decision_rt_value * 1000)
        
        # Timeout screen duration (seconds): 1.5 if timed out, else 0
        timeout_screen_duration = globals().get('TIMEOUT_SCREEN_DURATION', 1.5)
        decision_timeout_screen_duration = timeout_screen_duration if decision_timed_out else 0.0
        globals()['decision_timeout_duration'] = decision_timeout_screen_duration
        print(f"DEBUG decisionMakingEndRoutine: decision_timed_out={decision_timed_out}, decision_timeout_screen_duration={decision_timeout_screen_duration}")
        
        # Log the decision data
        thisExp.addData("decision_trial", decision_index + 1)
        thisExp.addData("leftFruit", leftFile)
        thisExp.addData("rightFruit", rightFile)
        thisExp.addData("firstFruit", firstFile if firstFile else "")
        thisExp.addData("firstSide", firstSide if firstSide else "")
        thisExp.addData("choice", choice)
        thisExp.addData("correctSide", correct)
        thisExp.addData("was_correct", was_correct)
        thisExp.addData("decision_rt", decision_rt_value)
        thisExp.addData("decision_timed_out", decision_timed_out)
        thisExp.addData("decision_timeout_duration", decision_timeout_screen_duration)
        
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
            
            # Extract first fruit information
            if firstFile:
                first_fruit_name = str(firstFile).replace('\\', '/').split('/')[-1].replace('.png', '')
            else:
                first_fruit_name = "unknown"
            first_side_value = firstSide if firstSide else ""
            
            # Determine block ID (1=before showing points explicitly, 2=after showing points explicitly)
            # For now, we'll use 1 as default (you can modify this based on your experiment structure)
            block_id = 1  # TODO: Update this based on your experiment structure
            block_name = "implicit"  # TODO: Update this based on your experiment structure
            
            # Determine choice as numerical ID (left_stimulus_num or right_stimulus_num)
            # The choice should be the numerical ID of the chosen fruit
            choice_num = left_stimulus_num if choice == "left" else (right_stimulus_num if choice == "right" else "")
            
            # Defer CSV logging until after ITI durations are computed (so we can log ITI_1/2/3)
        except Exception as e:
            print(f"Error logging decision data: {e}")
        
        # Calculate ITI 3 duration (crosshair after decision)
        # Requirement:
        # - ITI_3 should be 2/3/4 seconds on normal trials (do NOT subtract RT)
        # - On timed-out trials, show timeout screen for 1.5s, then crosshair for (2/3/4 - 1.5)s
        import random
        timeout_screen_duration = globals().get('TIMEOUT_SCREEN_DURATION', 1.5)
        iti3_total_values = [2, 3, 4]
        iti3_total = random.choice(iti3_total_values)
        
        if decision_timed_out:
            iti3_duration = max(0.0, iti3_total - timeout_screen_duration)
            print(f"ITI 3 (timeout): total={iti3_total}s, timeout_screen={timeout_screen_duration}s, crosshair={iti3_duration:.2f}s")
        else:
            iti3_duration = float(iti3_total)
            print(f"ITI 3 (normal): crosshair={iti3_duration:.2f}s (no RT subtraction)")
        
        globals()['iti3_duration'] = iti3_duration
        
        # Log ITI durations
        iti1_duration = globals().get('iti1_duration', 0)
        iti2_duration = globals().get('iti2_duration', 0)
        thisExp.addData("iti1_duration", iti1_duration)
        thisExp.addData("iti2_duration", iti2_duration)
        thisExp.addData("iti3_duration", iti3_duration)
        thisExp.addData("decision_response_time", decision_rt_value)
        
        # Log decision trial to CSV (includes ITIs and timeout metadata)
        try:
            data_logger = globals().get('data_logger', None)
            if data_logger:
                decision_response_limit_s = globals().get('DECISION_TIMEOUT_DURATION', 2.0)
                timeout_screen_duration_s = globals().get('decision_timeout_duration', 0.0)
                data_logger.log_decision_trial(
                    trial_num=decision_index + 1,
                    block_id=block_id,
                    block_name=block_name,
                    first_stimulus_id=first_fruit_name,
                    first_stimulus_side=first_side_value,
                    left_stimulus_id=left_fruit_name,
                    right_stimulus_id=right_fruit_name,
                    left_stimulus_num=left_stimulus_num,
                    right_stimulus_num=right_stimulus_num,
                    left_avg_points=left_avg,
                    right_avg_points=right_avg,
                    choice=choice_num if choice_num else "",
                    reaction_time_ms=decision_rt_ms,
                    iti1_duration=iti1_duration,
                    iti2_duration=iti2_duration,
                    iti3_duration=iti3_duration,
                    decision_timed_out=decision_timed_out,
                    decision_response_limit_s=decision_response_limit_s,
                    decision_timeout_screen_duration_s=timeout_screen_duration_s,
                )
        except Exception as e:
            print(f"Error logging decision data (with ITIs): {e}")
        
        print(f"Decision {decision_index + 1}: {choice} (correct: {correct}, accurate: {was_correct}, RT: {decision_rt_value:.2f}s, timed_out: {decision_timed_out})")
        print(f"Decision EndRoutine: RT={decision_rt_value:.3f}s={decision_rt_ms}ms, responded_in_time={not decision_timed_out}, timed_out={decision_timed_out}")
        
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
            routineTimer.addTime(-2.000000)
        
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
        decision_timed_out = globals().get('decision_timed_out', False)
        
        # DEBUG: Print timeout status
        print(f"DEBUG decisionTimeout: decision_timeout_duration={decision_timeout_duration}, decision_timed_out={decision_timed_out}")
        
        if decision_timeout_duration > 0:
            if 'text_decision_timeout' in locals():
                text_decision_timeout.text = "Time out"
                text_decision_timeout.opacity = 1
                text_decision_timeout.setAutoDraw(True)
                print("Showing decision timeout screen (1.5 seconds)")
            else:
                print("WARNING: text_decision_timeout component not found!")
        else:
            # No timeout - skip this screen (duration should be 0)
            print("Skipping decision timeout screen (no timeout occurred, decision_timeout_duration=0)")
            if 'text_decision_timeout' in locals():
                text_decision_timeout.opacity = 0
                text_decision_timeout.setAutoDraw(False)
        
        
        
        # store start times for decisionTimeout
        decisionTimeout.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        decisionTimeout.tStart = globalClock.getTime(format='float')
        decisionTimeout.status = STARTED
        thisExp.addData('decisionTimeout.started', decisionTimeout.tStart)
        decisionTimeout.maxDuration = decision_timeout_duration
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
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > decisionTimeout.maxDuration-frameTolerance:
                decisionTimeout.maxDurationReached = True
                continueRoutine = False
            
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
                if tThisFlipGlobal > text_decision_timeout.tStartRefresh + decision_timeout_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    text_decision_timeout.tStop = t  # not accounting for scr refresh
                    text_decision_timeout.tStopRefresh = tThisFlipGlobal  # on global time
                    text_decision_timeout.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_decision_timeout.stopped')
                    # update status
                    text_decision_timeout.status = FINISHED
                    text_decision_timeout.setAutoDraw(False)
            # Run 'Each Frame' code from code_17
            # Decision timeout screen - just displays "Time out" message, no interaction needed
            # The duration is controlled by decision_timeout_duration (1.5 seconds if timeout occurred, 0 otherwise)
            
            # Double-check that we should be showing this (safety check)
            decision_timeout_duration = globals().get('decision_timeout_duration', 0)
            if decision_timeout_duration <= 0:
                # Shouldn't be showing - skip
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
        # Run 'End Routine' code from code_17
        # Hide timeout text
        if 'text_decision_timeout' in locals():
            text_decision_timeout.setAutoDraw(False)
            text_decision_timeout.opacity = 0
        
        
        # the Routine "decisionTimeout" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
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
        # ITI 3 - Crosshair screen (duration: (2 - response_time) + rand(1,2,3))
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
    
    # --- Prepare to start Routine "inBetween" ---
    # create an object to store info about Routine inBetween
    inBetween = data.Routine(
        name='inBetween',
        components=[text_24, key_resp_14],
    )
    inBetween.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_14
    key_resp_14.keys = []
    key_resp_14.rt = []
    _key_resp_14_allKeys = []
    # store start times for inBetween
    inBetween.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    inBetween.tStart = globalClock.getTime(format='float')
    inBetween.status = STARTED
    thisExp.addData('inBetween.started', inBetween.tStart)
    inBetween.maxDuration = None
    # keep track of which components have finished
    inBetweenComponents = inBetween.components
    for thisComponent in inBetween.components:
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
    
    # --- Run Routine "inBetween" ---
    inBetween.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_24* updates
        
        # if text_24 is starting this frame...
        if text_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_24.frameNStart = frameN  # exact frame index
            text_24.tStart = t  # local t and not account for scr refresh
            text_24.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_24, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_24.started')
            # update status
            text_24.status = STARTED
            text_24.setAutoDraw(True)
        
        # if text_24 is active this frame...
        if text_24.status == STARTED:
            # update params
            pass
        
        # *key_resp_14* updates
        waitOnFlip = False
        
        # if key_resp_14 is starting this frame...
        if key_resp_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_14.frameNStart = frameN  # exact frame index
            key_resp_14.tStart = t  # local t and not account for scr refresh
            key_resp_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_14, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_14.started')
            # update status
            key_resp_14.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_14.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_14.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_14.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_14.getKeys(keyList=['c', 'C'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_14_allKeys.extend(theseKeys)
            if len(_key_resp_14_allKeys):
                key_resp_14.keys = _key_resp_14_allKeys[-1].name  # just the last key pressed
                key_resp_14.rt = _key_resp_14_allKeys[-1].rt
                key_resp_14.duration = _key_resp_14_allKeys[-1].duration
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
                currentRoutine=inBetween,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            inBetween.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in inBetween.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "inBetween" ---
    for thisComponent in inBetween.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for inBetween
    inBetween.tStop = globalClock.getTime(format='float')
    inBetween.tStopRefresh = tThisFlipGlobal
    thisExp.addData('inBetween.stopped', inBetween.tStop)
    # check responses
    if key_resp_14.keys in ['', [], None]:  # No response was made
        key_resp_14.keys = None
    thisExp.addData('key_resp_14.keys',key_resp_14.keys)
    if key_resp_14.keys != None:  # we had a response
        thisExp.addData('key_resp_14.rt', key_resp_14.rt)
        thisExp.addData('key_resp_14.duration', key_resp_14.duration)
    thisExp.nextEntry()
    # the Routine "inBetween" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "TaskStructure" ---
    # create an object to store info about Routine TaskStructure
    TaskStructure = data.Routine(
        name='TaskStructure',
        components=[text_2, text_19, text_21, key_resp_16, text_28],
    )
    TaskStructure.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_16
    key_resp_16.keys = []
    key_resp_16.rt = []
    _key_resp_16_allKeys = []
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
        
        # *key_resp_16* updates
        waitOnFlip = False
        
        # if key_resp_16 is starting this frame...
        if key_resp_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_16.frameNStart = frameN  # exact frame index
            key_resp_16.tStart = t  # local t and not account for scr refresh
            key_resp_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_16, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_16.started')
            # update status
            key_resp_16.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_16.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_16.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_16.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_16.getKeys(keyList=['c', 'C'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_16_allKeys.extend(theseKeys)
            if len(_key_resp_16_allKeys):
                key_resp_16.keys = _key_resp_16_allKeys[-1].name  # just the last key pressed
                key_resp_16.rt = _key_resp_16_allKeys[-1].rt
                key_resp_16.duration = _key_resp_16_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *text_28* updates
        
        # if text_28 is starting this frame...
        if text_28.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_28.frameNStart = frameN  # exact frame index
            text_28.tStart = t  # local t and not account for scr refresh
            text_28.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_28, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_28.started')
            # update status
            text_28.status = STARTED
            text_28.setAutoDraw(True)
        
        # if text_28 is active this frame...
        if text_28.status == STARTED:
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
    # check responses
    if key_resp_16.keys in ['', [], None]:  # No response was made
        key_resp_16.keys = None
    thisExp.addData('key_resp_16.keys',key_resp_16.keys)
    if key_resp_16.keys != None:  # we had a response
        thisExp.addData('key_resp_16.rt', key_resp_16.rt)
        thisExp.addData('key_resp_16.duration', key_resp_16.duration)
    thisExp.nextEntry()
    # the Routine "TaskStructure" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "yourGoal" ---
    # create an object to store info about Routine yourGoal
    yourGoal = data.Routine(
        name='yourGoal',
        components=[text_3, slider_2, text_22, key_resp_18],
    )
    yourGoal.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    slider_2.reset()
    # create starting attributes for key_resp_18
    key_resp_18.keys = []
    key_resp_18.rt = []
    _key_resp_18_allKeys = []
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
        
        # *key_resp_18* updates
        waitOnFlip = False
        
        # if key_resp_18 is starting this frame...
        if key_resp_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_18.frameNStart = frameN  # exact frame index
            key_resp_18.tStart = t  # local t and not account for scr refresh
            key_resp_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_18, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_18.started')
            # update status
            key_resp_18.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_18.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_18.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_18.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_18.getKeys(keyList=['c', 'C'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_18_allKeys.extend(theseKeys)
            if len(_key_resp_18_allKeys):
                key_resp_18.keys = _key_resp_18_allKeys[-1].name  # just the last key pressed
                key_resp_18.rt = _key_resp_18_allKeys[-1].rt
                key_resp_18.duration = _key_resp_18_allKeys[-1].duration
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
    thisExp.addData('slider_2.response', slider_2.getRating())
    thisExp.addData('slider_2.rt', slider_2.getRT())
    # check responses
    if key_resp_18.keys in ['', [], None]:  # No response was made
        key_resp_18.keys = None
    thisExp.addData('key_resp_18.keys',key_resp_18.keys)
    if key_resp_18.keys != None:  # we had a response
        thisExp.addData('key_resp_18.rt', key_resp_18.rt)
        thisExp.addData('key_resp_18.duration', key_resp_18.duration)
    thisExp.nextEntry()
    # the Routine "yourGoal" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "keyInstructions" ---
    # create an object to store info about Routine keyInstructions
    keyInstructions = data.Routine(
        name='keyInstructions',
        components=[text_20, key_resp_19],
    )
    keyInstructions.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_19
    key_resp_19.keys = []
    key_resp_19.rt = []
    _key_resp_19_allKeys = []
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
        
        # *key_resp_19* updates
        waitOnFlip = False
        
        # if key_resp_19 is starting this frame...
        if key_resp_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_19.frameNStart = frameN  # exact frame index
            key_resp_19.tStart = t  # local t and not account for scr refresh
            key_resp_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_19, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_19.started')
            # update status
            key_resp_19.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_19.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_19.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_19.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_19.getKeys(keyList=['c', 'C'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_19_allKeys.extend(theseKeys)
            if len(_key_resp_19_allKeys):
                key_resp_19.keys = _key_resp_19_allKeys[-1].name  # just the last key pressed
                key_resp_19.rt = _key_resp_19_allKeys[-1].rt
                key_resp_19.duration = _key_resp_19_allKeys[-1].duration
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
    # check responses
    if key_resp_19.keys in ['', [], None]:  # No response was made
        key_resp_19.keys = None
    thisExp.addData('key_resp_19.keys',key_resp_19.keys)
    if key_resp_19.keys != None:  # we had a response
        thisExp.addData('key_resp_19.rt', key_resp_19.rt)
        thisExp.addData('key_resp_19.duration', key_resp_19.duration)
    thisExp.nextEntry()
    # the Routine "keyInstructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "practiceIntro" ---
    # create an object to store info about Routine practiceIntro
    practiceIntro = data.Routine(
        name='practiceIntro',
        components=[text_practice_intro, key_resp_9],
    )
    practiceIntro.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_18
    # Practice introduction screen
    # Shows "We will run a short practice task now. Press 2 to continue"
    # Component: text_practice_intro (or similar text component)
    
    # Clear any previous key presses
    try:
        event.clearEvents()
    except:
        pass
    
    # Display practice introduction text
    if 'text_practice_intro' in locals():
        text_practice_intro.text = "We will run a short practice task now. Press C to continue"
        text_practice_intro.opacity = 1
        text_practice_intro.setAutoDraw(True)
        print("Practice introduction screen displayed")
    else:
        print("WARNING: text_practice_intro component not found!")
    
    
    # create starting attributes for key_resp_9
    key_resp_9.keys = []
    key_resp_9.rt = []
    _key_resp_9_allKeys = []
    # store start times for practiceIntro
    practiceIntro.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    practiceIntro.tStart = globalClock.getTime(format='float')
    practiceIntro.status = STARTED
    thisExp.addData('practiceIntro.started', practiceIntro.tStart)
    practiceIntro.maxDuration = None
    # keep track of which components have finished
    practiceIntroComponents = practiceIntro.components
    for thisComponent in practiceIntro.components:
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
    
    # --- Run Routine "practiceIntro" ---
    practiceIntro.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_18
        # Practice introduction - wait for key press '2' to continue
        try:
            keys = event.getKeys(keyList=['2', 'num_2'])
            if keys:
                # Key 2 pressed - continue to practice trials
                print("Practice introduction: Key 2 pressed, continuing to practice trials")
                continueRoutine = False
                event.clearEvents()
        except:
            pass
        
        
        
        # *text_practice_intro* updates
        
        # if text_practice_intro is starting this frame...
        if text_practice_intro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_practice_intro.frameNStart = frameN  # exact frame index
            text_practice_intro.tStart = t  # local t and not account for scr refresh
            text_practice_intro.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_practice_intro, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_practice_intro.started')
            # update status
            text_practice_intro.status = STARTED
            text_practice_intro.setAutoDraw(True)
        
        # if text_practice_intro is active this frame...
        if text_practice_intro.status == STARTED:
            # update params
            pass
        
        # *key_resp_9* updates
        waitOnFlip = False
        
        # if key_resp_9 is starting this frame...
        if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_9.frameNStart = frameN  # exact frame index
            key_resp_9.tStart = t  # local t and not account for scr refresh
            key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_9.started')
            # update status
            key_resp_9.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_9.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_9.getKeys(keyList=['c', 'C'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_9_allKeys.extend(theseKeys)
            if len(_key_resp_9_allKeys):
                key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
                key_resp_9.rt = _key_resp_9_allKeys[-1].rt
                key_resp_9.duration = _key_resp_9_allKeys[-1].duration
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
                currentRoutine=practiceIntro,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            practiceIntro.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceIntro.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "practiceIntro" ---
    for thisComponent in practiceIntro.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for practiceIntro
    practiceIntro.tStop = globalClock.getTime(format='float')
    practiceIntro.tStopRefresh = tThisFlipGlobal
    thisExp.addData('practiceIntro.stopped', practiceIntro.tStop)
    # Run 'End Routine' code from code_18
    # Hide practice introduction text
    if 'text_practice_intro' in locals():
        text_practice_intro.setAutoDraw(False)
        text_practice_intro.opacity = 0
    
    # Clear any remaining key presses
    try:
        event.clearEvents()
    except:
        pass
    
    
    # check responses
    if key_resp_9.keys in ['', [], None]:  # No response was made
        key_resp_9.keys = None
    thisExp.addData('key_resp_9.keys',key_resp_9.keys)
    if key_resp_9.keys != None:  # we had a response
        thisExp.addData('key_resp_9.rt', key_resp_9.rt)
        thisExp.addData('key_resp_9.duration', key_resp_9.duration)
    thisExp.nextEntry()
    # the Routine "practiceIntro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    practiceTrials = data.TrialHandler2(
        name='practiceTrials',
        nReps=3.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(practiceTrials)  # add the loop to the experiment
    thisPracticeTrial = practiceTrials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeTrial.rgb)
    if thisPracticeTrial != None:
        for paramName in thisPracticeTrial:
            globals()[paramName] = thisPracticeTrial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisPracticeTrial in practiceTrials:
        practiceTrials.status = STARTED
        if hasattr(thisPracticeTrial, 'status'):
            thisPracticeTrial.status = STARTED
        currentLoop = practiceTrials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisPracticeTrial.rgb)
        if thisPracticeTrial != None:
            for paramName in thisPracticeTrial:
                globals()[paramName] = thisPracticeTrial[paramName]
        
        # --- Prepare to start Routine "practiceTrial" ---
        # create an object to store info about Routine practiceTrial
        practiceTrial = data.Routine(
            name='practiceTrial',
            components=[image_4, slider_3],
        )
        practiceTrial.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_19
        # Practice trial - similar to regular trial but with shorter durations
        # Get practice_block_index from globals (or initialize if first practice trial)
        practice_block_index = globals().get('practice_block_index', -1)
        practice_block_index += 1
        globals()['practice_block_index'] = practice_block_index
        
        # Get practice_block from globals
        practice_block = globals().get('practice_block', [])
        
        # Debug: Print practice block info
        print(f"DEBUG: practice_block_index={practice_block_index}, practice_block length={len(practice_block)}")
        if practice_block:
            print(f"DEBUG: practice_block contents: {[t['fruit'] for t in practice_block]}")
        else:
            print("ERROR: practice_block is empty! Creating fallback practice block.")
            # Fallback: Create a simple practice block if it doesn't exist
            image_dir = "images/"
            practice_block = [
                {"block": "gain", "fruit": image_dir + "dog.png", "baseline": 50, "true_value": 30},
                {"block": "loss", "fruit": image_dir + "cat.png", "baseline": -50, "true_value": -30},
                {"block": "gain", "fruit": image_dir + "rabbit.png", "baseline": 50, "true_value": 50}
            ]
            globals()['practice_block'] = practice_block
            print(f"Created fallback practice block with {len(practice_block)} trials")
        
        # Get current practice trial
        if practice_block and len(practice_block) > 0 and practice_block_index >= 0 and practice_block_index < len(practice_block):
            current = practice_block[practice_block_index]
            fruitFile = current["fruit"]
            trueVal = current["true_value"]
            baselineR = current["baseline"]
            blockType = current["block"]
            idx = practice_block_index + 1
            print(f"Practice trial {idx}/3: {fruitFile}, value={trueVal}")
        else:
            # Fallback - use blank
            fruitFile = "images/blank.png"
            trueVal = 0
            baselineR = 0
            blockType = "practice"
            idx = 0
            print(f"WARNING: Practice trial {practice_block_index} out of range")
        
        # Clear any keys from previous routines
        try:
            event.clearEvents()
        except:
            pass
        
        # Set the fruit image - initialize it properly to avoid tStartRefresh None error
        # This matches the regular trial approach
        if 'image_4' in locals():
            # Set the image first
            image_4.setImage(fruitFile)
            image_4.opacity = 1
            # Initialize by setting autodraw - this ensures tStartRefresh gets set
            image_4.setAutoDraw(True)
            # Reset debug flag for EachFrame
            if hasattr(image_4, '_shown_debug'):
                del image_4._shown_debug
            print(f"Practice trial: Set image to {fruitFile} with opacity {image_4.opacity}")
        
        # Reset slider to 0
        if 'slider_3' in locals():
            slider_3.reset()
            slider_3.setRating(0)
            print("Practice trial: Slider reset to 0")
        
        # Initialize timing variables (shorter timeout for practice - 6 seconds)
        import time
        trial_start_time = time.time()
        response_time = None
        trial_timed_out = False
        responded_in_time = False
        
        # Store in globals
        globals()['trial_start_time'] = trial_start_time
        globals()['response_time'] = None
        globals()['trial_timed_out'] = False
        globals()['responded_in_time'] = False
        
        # Store trial variables in globals for use in other routines (like actualPoints)
        globals()['trueVal'] = trueVal
        globals()['fruitFile'] = fruitFile
        globals()['blockType'] = blockType
        globals()['baselineR'] = baselineR
        
        # Practice trials use shorter timeout (6 seconds instead of 8)
        globals()['PRACTICE_TIMEOUT_SECONDS'] = 6.0
        
        
        slider_3.reset()
        # store start times for practiceTrial
        practiceTrial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        practiceTrial.tStart = globalClock.getTime(format='float')
        practiceTrial.status = STARTED
        thisExp.addData('practiceTrial.started', practiceTrial.tStart)
        practiceTrial.maxDuration = None
        # keep track of which components have finished
        practiceTrialComponents = practiceTrial.components
        for thisComponent in practiceTrial.components:
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
        
        # --- Run Routine "practiceTrial" ---
        practiceTrial.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisPracticeTrial, 'status') and thisPracticeTrial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_19
            # Practice trial - check for response (shorter timeout: 6 seconds)
            # Using keys 1/3: 1 = left (decrease), 2 = continue, 3 = right (increase)
            import time
            
            # Get fruitFile from locals or globals
            if 'fruitFile' not in locals():
                fruitFile = globals().get('fruitFile', 'images/blank.png')
            
            # Show the fruit image - FORCE it to be visible (match regular trial approach)
            if 'image_4' in locals() and fruitFile and fruitFile != 'images/blank.png' and fruitFile != '':
                # Set the image and make it visible every frame
                image_4.setImage(fruitFile)
                image_4.opacity = 1.0  # Force opacity to 1.0
                image_4.setAutoDraw(True)  # Force autodraw to ensure it's drawn
                # Debug: print once per trial that image is being shown
                if not hasattr(image_4, '_shown_debug'):
                    print(f"DEBUG: Practice showing image {fruitFile} with opacity {image_4.opacity}, autodraw={image_4.status}")
                    image_4._shown_debug = True
            elif 'image_4' in locals():
                image_4.opacity = 0
                image_4.setAutoDraw(False)
            
            # Display current slider value
            if 'slider_3' in locals():
                current_value = slider_3.getRating()
                # Handle None values - slider might return None initially
                if current_value is not None:
                    try:
                        current_value_int = int(current_value)
                        if 'text_slider_value' in locals():
                            text_slider_value.text = f"Current rating: {current_value_int}"
                        elif 'text_rating' in locals():
                            text_rating.text = f"Current rating: {current_value_int}"
                    except (ValueError, TypeError):
                        # If conversion fails, just skip updating the text
                        pass
            
            # Handle keyboard input for slider controls
            try:
                keys = event.getKeys(keyList=['1', '2', '3', 'num_1', 'num_2', 'num_3'])
            except:
                keys = []
            
            for key in keys:
                # Normalize key names
                if key == 'num_1' or key == '1':
                    # Key 1: Move slider left by 5 points
                    if 'slider_3' in locals():
                        current_rating = slider_3.getRating()
                        if current_rating is None:
                            current_rating = 0
                        new_rating = current_rating - 5
                        slider_3.setRating(new_rating)
                        print(f"Practice: Slider moved left (key 1): {current_rating} -> {new_rating}")
                        
                elif key == 'num_3' or key == '3':
                    # Key 3: Move slider right by 5 points
                    if 'slider_3' in locals():
                        current_rating = slider_3.getRating()
                        if current_rating is None:
                            current_rating = 0
                        new_rating = current_rating + 5
                        slider_3.setRating(new_rating)
                        print(f"Practice: Slider moved right (key 3): {current_rating} -> {new_rating}")
                        
                elif key == 'num_2' or key == '2':
                    # Key 2: Submit answer
                    trial_start_time = globals().get('trial_start_time', time.time())
                    response_time = time.time() - trial_start_time
                    
                    PRACTICE_TIMEOUT_SECONDS = globals().get('PRACTICE_TIMEOUT_SECONDS', 6.0)
                    
                    if response_time <= PRACTICE_TIMEOUT_SECONDS:
                        responded_in_time = True
                        trial_timed_out = False
                        print(f"Practice: Answer submitted (key 2) in {response_time:.2f} seconds")
                    else:
                        responded_in_time = False
                        trial_timed_out = True
                        print(f"Practice: Answer submitted (key 2) in {response_time:.2f} seconds (over limit)")
                    
                    globals()['response_time'] = response_time
                    globals()['responded_in_time'] = responded_in_time
                    globals()['trial_timed_out'] = trial_timed_out
                    
                    continueRoutine = False
                    event.clearEvents()
                    break
            
            # Check for timeout (6 seconds for practice)
            try:
                trial_start_time = globals().get('trial_start_time', time.time())
                PRACTICE_TIMEOUT_SECONDS = globals().get('PRACTICE_TIMEOUT_SECONDS', 6.0)
                responded_in_time = globals().get('responded_in_time', False)
                
                elapsed_time = time.time() - trial_start_time
                
                if elapsed_time >= PRACTICE_TIMEOUT_SECONDS and not responded_in_time:
                    trial_timed_out = True
                    response_time = PRACTICE_TIMEOUT_SECONDS
                    responded_in_time = False
                    
                    globals()['response_time'] = response_time
                    globals()['responded_in_time'] = responded_in_time
                    globals()['trial_timed_out'] = trial_timed_out
                    
                    print(f"Practice: Trial timed out at {PRACTICE_TIMEOUT_SECONDS} seconds")
                    continueRoutine = False
                    event.clearEvents()
            except:
                pass
            
            
            
            # *image_4* updates
            
            # if image_4 is starting this frame...
            if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_4.frameNStart = frameN  # exact frame index
                image_4.tStart = t  # local t and not account for scr refresh
                image_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_4.started')
                # update status
                image_4.status = STARTED
                image_4.setAutoDraw(True)
            
            # if image_4 is active this frame...
            if image_4.status == STARTED:
                # update params
                pass
            
            # *slider_3* updates
            
            # if slider_3 is starting this frame...
            if slider_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                slider_3.frameNStart = frameN  # exact frame index
                slider_3.tStart = t  # local t and not account for scr refresh
                slider_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_3.started')
                # update status
                slider_3.status = STARTED
                slider_3.setAutoDraw(True)
            
            # if slider_3 is active this frame...
            if slider_3.status == STARTED:
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
                    currentRoutine=practiceTrial,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                practiceTrial.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practiceTrial.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "practiceTrial" ---
        for thisComponent in practiceTrial.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for practiceTrial
        practiceTrial.tStop = globalClock.getTime(format='float')
        practiceTrial.tStopRefresh = tThisFlipGlobal
        thisExp.addData('practiceTrial.stopped', practiceTrial.tStop)
        # Run 'End Routine' code from code_19
        # Get response data from practice trial
        if 'slider_3' in locals():
            rating = slider_3.getRating()
            if rating is None:
                rating = 0
            rt = slider_3.getRT()
        else:
            rating = 0
            rt = None
        
        # Get response_time, responded_in_time, and trial_timed_out from globals
        response_time = globals().get('response_time', None)
        responded_in_time = globals().get('responded_in_time', False)
        trial_timed_out = globals().get('trial_timed_out', False)
        
        # Use response_time if available, otherwise use slider RT
        actual_response_time = response_time if response_time is not None else rt
        
        rt_str = f"{actual_response_time:.3f}s" if actual_response_time else "N/A"
        print(f"Practice trial EndRoutine: RT={rt_str}, responded_in_time={responded_in_time}, timed_out={trial_timed_out}")
        
        # Log practice trial data (optional - you may want to log this separately)
        thisExp.addData("practice_trial", True)
        thisExp.addData("practice_block", blockType if 'blockType' in locals() else "practice")
        thisExp.addData("practice_fruit", fruitFile if 'fruitFile' in locals() else "")
        thisExp.addData("practice_rating", rating)
        thisExp.addData("practice_rt", actual_response_time if actual_response_time else None)
        thisExp.addData("practice_true_value", trueVal if 'trueVal' in locals() else 0)
        thisExp.addData("practice_responded_in_time", responded_in_time)
        thisExp.addData("practice_timed_out", trial_timed_out)
        
        
        practiceTrials.addData('slider_3.response', slider_3.getRating())
        practiceTrials.addData('slider_3.rt', slider_3.getRT())
        # the Routine "practiceTrial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "crosshair5" ---
        # create an object to store info about Routine crosshair5
        crosshair5 = data.Routine(
            name='crosshair5',
            components=[text_27],
        )
        crosshair5.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for crosshair5
        crosshair5.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        crosshair5.tStart = globalClock.getTime(format='float')
        crosshair5.status = STARTED
        thisExp.addData('crosshair5.started', crosshair5.tStart)
        crosshair5.maxDuration = None
        # keep track of which components have finished
        crosshair5Components = crosshair5.components
        for thisComponent in crosshair5.components:
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
        
        # --- Run Routine "crosshair5" ---
        crosshair5.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # if trial has changed, end Routine now
            if hasattr(thisPracticeTrial, 'status') and thisPracticeTrial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_27* updates
            
            # if text_27 is starting this frame...
            if text_27.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_27.frameNStart = frameN  # exact frame index
                text_27.tStart = t  # local t and not account for scr refresh
                text_27.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_27, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_27.started')
                # update status
                text_27.status = STARTED
                text_27.setAutoDraw(True)
            
            # if text_27 is active this frame...
            if text_27.status == STARTED:
                # update params
                pass
            
            # if text_27 is stopping this frame...
            if text_27.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_27.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_27.tStop = t  # not accounting for scr refresh
                    text_27.tStopRefresh = tThisFlipGlobal  # on global time
                    text_27.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_27.stopped')
                    # update status
                    text_27.status = FINISHED
                    text_27.setAutoDraw(False)
            
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
                    currentRoutine=crosshair5,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                crosshair5.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in crosshair5.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "crosshair5" ---
        for thisComponent in crosshair5.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for crosshair5
        crosshair5.tStop = globalClock.getTime(format='float')
        crosshair5.tStopRefresh = tThisFlipGlobal
        thisExp.addData('crosshair5.stopped', crosshair5.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if crosshair5.maxDurationReached:
            routineTimer.addTime(-crosshair5.maxDuration)
        elif crosshair5.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "actualPoints1" ---
        # create an object to store info about Routine actualPoints1
        actualPoints1 = data.Routine(
            name='actualPoints1',
            components=[text_actual_points],
        )
        actualPoints1.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_22
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
        
        
        
        # store start times for actualPoints1
        actualPoints1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        actualPoints1.tStart = globalClock.getTime(format='float')
        actualPoints1.status = STARTED
        thisExp.addData('actualPoints1.started', actualPoints1.tStart)
        actualPoints1.maxDuration = None
        # keep track of which components have finished
        actualPoints1Components = actualPoints1.components
        for thisComponent in actualPoints1.components:
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
        
        # --- Run Routine "actualPoints1" ---
        actualPoints1.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # if trial has changed, end Routine now
            if hasattr(thisPracticeTrial, 'status') and thisPracticeTrial.status == STOPPING:
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
                if tThisFlipGlobal > text_actual_points.tStartRefresh + 2-frameTolerance:
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
                    currentRoutine=actualPoints1,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                actualPoints1.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in actualPoints1.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "actualPoints1" ---
        for thisComponent in actualPoints1.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for actualPoints1
        actualPoints1.tStop = globalClock.getTime(format='float')
        actualPoints1.tStopRefresh = tThisFlipGlobal
        thisExp.addData('actualPoints1.stopped', actualPoints1.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if actualPoints1.maxDurationReached:
            routineTimer.addTime(-actualPoints1.maxDuration)
        elif actualPoints1.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # --- Prepare to start Routine "crosshair3" ---
        # create an object to store info about Routine crosshair3
        crosshair3 = data.Routine(
            name='crosshair3',
            components=[text_23],
        )
        crosshair3.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_23
        # First crosshair screen - duration set dynamically based on trial response time
        # Duration is set in trialEndRoutine.py as crosshair1_duration
        # This routine will show a crosshair in the center of the screen
        
        # Make sure crosshair is visible (add a crosshair component in Builder)
        if 'crosshair' in locals():
            crosshair.opacity = 1
            crosshair.setAutoDraw(True)
        
        
        # store start times for crosshair3
        crosshair3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        crosshair3.tStart = globalClock.getTime(format='float')
        crosshair3.status = STARTED
        thisExp.addData('crosshair3.started', crosshair3.tStart)
        crosshair3.maxDuration = None
        # keep track of which components have finished
        crosshair3Components = crosshair3.components
        for thisComponent in crosshair3.components:
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
        
        # --- Run Routine "crosshair3" ---
        crosshair3.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # if trial has changed, end Routine now
            if hasattr(thisPracticeTrial, 'status') and thisPracticeTrial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_23* updates
            
            # if text_23 is starting this frame...
            if text_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_23.frameNStart = frameN  # exact frame index
                text_23.tStart = t  # local t and not account for scr refresh
                text_23.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_23, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_23.started')
                # update status
                text_23.status = STARTED
                text_23.setAutoDraw(True)
            
            # if text_23 is active this frame...
            if text_23.status == STARTED:
                # update params
                pass
            
            # if text_23 is stopping this frame...
            if text_23.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_23.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    text_23.tStop = t  # not accounting for scr refresh
                    text_23.tStopRefresh = tThisFlipGlobal  # on global time
                    text_23.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_23.stopped')
                    # update status
                    text_23.status = FINISHED
                    text_23.setAutoDraw(False)
            # Run 'Each Frame' code from code_23
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
                    currentRoutine=crosshair3,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                crosshair3.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in crosshair3.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "crosshair3" ---
        for thisComponent in crosshair3.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for crosshair3
        crosshair3.tStop = globalClock.getTime(format='float')
        crosshair3.tStopRefresh = tThisFlipGlobal
        thisExp.addData('crosshair3.stopped', crosshair3.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if crosshair3.maxDurationReached:
            routineTimer.addTime(-crosshair3.maxDuration)
        elif crosshair3.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        # mark thisPracticeTrial as finished
        if hasattr(thisPracticeTrial, 'status'):
            thisPracticeTrial.status = FINISHED
        # if awaiting a pause, pause now
        if practiceTrials.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            practiceTrials.status = STARTED
        thisExp.nextEntry()
        
    # completed 3.0 repeats of 'practiceTrials'
    practiceTrials.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "taskStartSoon" ---
    # create an object to store info about Routine taskStartSoon
    taskStartSoon = data.Routine(
        name='taskStartSoon',
        components=[text_task_start_soon, key_resp_10],
    )
    taskStartSoon.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_10
    key_resp_10.keys = []
    key_resp_10.rt = []
    _key_resp_10_allKeys = []
    # Run 'Begin Routine' code from code_20
    # "Task will start soon. Press 2 to continue" screen
    # Component: text_task_start_soon (or similar text component)
    # This should ONLY show ONCE at the start of Block 1, NOT after every trial
    
    # Check if Block 1 setup has already been completed
    block1_scanner_sync_complete = globals().get('block1_scanner_sync_complete', False)
    block2_setup_complete = globals().get('block2_setup_complete', False)
    learning_block_index = globals().get('learning_block_index', -1)
    
    # Only show taskStartSoon ONCE at the start of Block 1
    # Skip if: Block 1 scanner sync already done, OR block 2 setup is complete, OR we've already started trials (learning_block_index >= 0 means at least one trial has started)
    print(f"DEBUG taskStartSoon: block1_scanner_sync_complete={block1_scanner_sync_complete}, block2_setup_complete={block2_setup_complete}, learning_block_index={learning_block_index}")
    
    if block1_scanner_sync_complete or block2_setup_complete or learning_block_index >= 0:
        print(f"Skipping taskStartSoon (block1_scanner_sync_complete={block1_scanner_sync_complete}, block2_setup_complete={block2_setup_complete}, learning_block_index={learning_block_index})")
        continueRoutine = False
    else:
        # Clear any previous key presses
        try:
            event.clearEvents()
        except:
            pass
    
        # Display task start message
        if 'text_task_start_soon' in locals():
            text_task_start_soon.text = "The task will start soon. Press C to continue"
            text_task_start_soon.opacity = 1
            text_task_start_soon.setAutoDraw(True)
            print("Task start soon screen displayed")
        else:
            print("WARNING: text_task_start_soon component not found!")
    
    
    
    
    
    # store start times for taskStartSoon
    taskStartSoon.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    taskStartSoon.tStart = globalClock.getTime(format='float')
    taskStartSoon.status = STARTED
    thisExp.addData('taskStartSoon.started', taskStartSoon.tStart)
    taskStartSoon.maxDuration = None
    # keep track of which components have finished
    taskStartSoonComponents = taskStartSoon.components
    for thisComponent in taskStartSoon.components:
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
    
    # --- Run Routine "taskStartSoon" ---
    taskStartSoon.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_task_start_soon* updates
        
        # if text_task_start_soon is starting this frame...
        if text_task_start_soon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_task_start_soon.frameNStart = frameN  # exact frame index
            text_task_start_soon.tStart = t  # local t and not account for scr refresh
            text_task_start_soon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_task_start_soon, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_task_start_soon.started')
            # update status
            text_task_start_soon.status = STARTED
            text_task_start_soon.setAutoDraw(True)
        
        # if text_task_start_soon is active this frame...
        if text_task_start_soon.status == STARTED:
            # update params
            pass
        
        # *key_resp_10* updates
        waitOnFlip = False
        
        # if key_resp_10 is starting this frame...
        if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_10.frameNStart = frameN  # exact frame index
            key_resp_10.tStart = t  # local t and not account for scr refresh
            key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_10.started')
            # update status
            key_resp_10.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_10.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_10.getKeys(keyList=['c', 'C'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_10_allKeys.extend(theseKeys)
            if len(_key_resp_10_allKeys):
                key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
                key_resp_10.rt = _key_resp_10_allKeys[-1].rt
                key_resp_10.duration = _key_resp_10_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        # Run 'Each Frame' code from code_20
        # Task start soon - wait for key press '2' to continue
        # Check if Block 1 setup has already been completed (shouldn't happen, but safety check)
        block1_scanner_sync_complete = globals().get('block1_scanner_sync_complete', False)
        if block1_scanner_sync_complete:
            continueRoutine = False
        else:
            try:
                keys = event.getKeys(keyList=['2', 'num_2'])
                if keys:
                    # Key 2 pressed - continue to scanner sync
                    print("Task start soon: Key 2 pressed, continuing to scanner sync")
                    continueRoutine = False
                    event.clearEvents()
            except:
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
                currentRoutine=taskStartSoon,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            taskStartSoon.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in taskStartSoon.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "taskStartSoon" ---
    for thisComponent in taskStartSoon.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for taskStartSoon
    taskStartSoon.tStop = globalClock.getTime(format='float')
    taskStartSoon.tStopRefresh = tThisFlipGlobal
    thisExp.addData('taskStartSoon.stopped', taskStartSoon.tStop)
    # check responses
    if key_resp_10.keys in ['', [], None]:  # No response was made
        key_resp_10.keys = None
    thisExp.addData('key_resp_10.keys',key_resp_10.keys)
    if key_resp_10.keys != None:  # we had a response
        thisExp.addData('key_resp_10.rt', key_resp_10.rt)
        thisExp.addData('key_resp_10.duration', key_resp_10.duration)
    # Run 'End Routine' code from code_20
    # Hide task start soon text
    if 'text_task_start_soon' in locals():
        text_task_start_soon.setAutoDraw(False)
        text_task_start_soon.opacity = 0
    
    # Clear any remaining key presses
    try:
        event.clearEvents()
    except:
        pass
    
    
    thisExp.nextEntry()
    # the Routine "taskStartSoon" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "scannerSync" ---
    # create an object to store info about Routine scannerSync
    scannerSync = data.Routine(
        name='scannerSync',
        components=[text_scanner_wait, key_resp_11],
    )
    scannerSync.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_11
    key_resp_11.keys = []
    key_resp_11.rt = []
    _key_resp_11_allKeys = []
    # Run 'Begin Routine' code from code_21
    # MRI Scanner sync - wait for scanner trigger (key '5')
    # Component: text_scanner_wait (or similar text component)
    # This should ONLY show ONCE at the start of Block 1, NOT after every trial
    
    # Check if Block 1 scanner sync has already been completed
    block1_scanner_sync_complete = globals().get('block1_scanner_sync_complete', False)
    block2_setup_complete = globals().get('block2_setup_complete', False)
    learning_block_index = globals().get('learning_block_index', -1)
    
    # Only show scannerSync ONCE at the start of Block 1
    # Skip if: Block 1 scanner sync already done, OR block 2 setup is complete, OR we've already started trials (learning_block_index >= 0 means at least one trial has started)
    print(f"DEBUG scannerSync: block1_scanner_sync_complete={block1_scanner_sync_complete}, block2_setup_complete={block2_setup_complete}, learning_block_index={learning_block_index}")
    
    if block1_scanner_sync_complete or block2_setup_complete or learning_block_index >= 0:
        print(f"Skipping scannerSync (block1_scanner_sync_complete={block1_scanner_sync_complete}, block2_setup_complete={block2_setup_complete}, learning_block_index={learning_block_index})")
        continueRoutine = False
    else:
        # Clear any previous key presses
        try:
            event.clearEvents()
        except:
            pass
    
        # Display waiting message
        if 'text_scanner_wait' in locals():
            text_scanner_wait.text = "Waiting for the scanner to start..."
            text_scanner_wait.opacity = 1
            text_scanner_wait.setAutoDraw(True)
            print("Scanner sync: Waiting for trigger '5' from MRI scanner (Block 1)")
        else:
            print("WARNING: text_scanner_wait component not found!")
    
    
    
    
    # store start times for scannerSync
    scannerSync.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    scannerSync.tStart = globalClock.getTime(format='float')
    scannerSync.status = STARTED
    thisExp.addData('scannerSync.started', scannerSync.tStart)
    scannerSync.maxDuration = None
    # keep track of which components have finished
    scannerSyncComponents = scannerSync.components
    for thisComponent in scannerSync.components:
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
    
    # --- Run Routine "scannerSync" ---
    scannerSync.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_scanner_wait* updates
        
        # if text_scanner_wait is starting this frame...
        if text_scanner_wait.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_scanner_wait.frameNStart = frameN  # exact frame index
            text_scanner_wait.tStart = t  # local t and not account for scr refresh
            text_scanner_wait.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_scanner_wait, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_scanner_wait.started')
            # update status
            text_scanner_wait.status = STARTED
            text_scanner_wait.setAutoDraw(True)
        
        # if text_scanner_wait is active this frame...
        if text_scanner_wait.status == STARTED:
            # update params
            pass
        
        # *key_resp_11* updates
        waitOnFlip = False
        
        # if key_resp_11 is starting this frame...
        if key_resp_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_11.frameNStart = frameN  # exact frame index
            key_resp_11.tStart = t  # local t and not account for scr refresh
            key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_11.started')
            # update status
            key_resp_11.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_11.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_11.getKeys(keyList=['5', 'num_5', 'num5'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_11_allKeys.extend(theseKeys)
            if len(_key_resp_11_allKeys):
                key_resp_11.keys = _key_resp_11_allKeys[-1].name  # just the last key pressed
                key_resp_11.rt = _key_resp_11_allKeys[-1].rt
                key_resp_11.duration = _key_resp_11_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        # Run 'Each Frame' code from code_21
        # Scanner sync - wait for MRI scanner trigger (key '5')
        # The MRI sends '5' when it's ready
        # Check if Block 1 scanner sync has already been completed (shouldn't happen, but safety check)
        block1_scanner_sync_complete = globals().get('block1_scanner_sync_complete', False)
        if block1_scanner_sync_complete:
            continueRoutine = False
        else:
            try:
                keys = event.getKeys(keyList=['5', 'num_5'])
                if keys:
                    # Scanner trigger received - continue to next screen
                    print("Scanner sync: Trigger '5' received from MRI scanner, continuing")
                    continueRoutine = False
                    event.clearEvents()
            except:
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
                currentRoutine=scannerSync,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            scannerSync.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in scannerSync.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "scannerSync" ---
    for thisComponent in scannerSync.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for scannerSync
    scannerSync.tStop = globalClock.getTime(format='float')
    scannerSync.tStopRefresh = tThisFlipGlobal
    thisExp.addData('scannerSync.stopped', scannerSync.tStop)
    # check responses
    if key_resp_11.keys in ['', [], None]:  # No response was made
        key_resp_11.keys = None
    thisExp.addData('key_resp_11.keys',key_resp_11.keys)
    if key_resp_11.keys != None:  # we had a response
        thisExp.addData('key_resp_11.rt', key_resp_11.rt)
        thisExp.addData('key_resp_11.duration', key_resp_11.duration)
    # Run 'End Routine' code from code_21
    # Hide scanner wait text
    if 'text_scanner_wait' in locals():
        text_scanner_wait.setAutoDraw(False)
        text_scanner_wait.opacity = 0
    
    # Clear any remaining key presses
    try:
        event.clearEvents()
    except:
        pass
    
    # Log scanner sync time (optional)
    import time
    scanner_sync_time = time.time()
    globals()['scanner_sync_time'] = scanner_sync_time
    print(f"Scanner sync completed at {scanner_sync_time}")
    
    # Mark Block 1 scanner sync as complete - it should not show again
    globals()['block1_scanner_sync_complete'] = True
    print("Block 1 scanner sync complete - will not show again")
    
    
    
    
    
    thisExp.nextEntry()
    # the Routine "scannerSync" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "crosshair3" ---
    # create an object to store info about Routine crosshair3
    crosshair3 = data.Routine(
        name='crosshair3',
        components=[text_23],
    )
    crosshair3.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_23
    # First crosshair screen - duration set dynamically based on trial response time
    # Duration is set in trialEndRoutine.py as crosshair1_duration
    # This routine will show a crosshair in the center of the screen
    
    # Make sure crosshair is visible (add a crosshair component in Builder)
    if 'crosshair' in locals():
        crosshair.opacity = 1
        crosshair.setAutoDraw(True)
    
    
    # store start times for crosshair3
    crosshair3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    crosshair3.tStart = globalClock.getTime(format='float')
    crosshair3.status = STARTED
    thisExp.addData('crosshair3.started', crosshair3.tStart)
    crosshair3.maxDuration = None
    # keep track of which components have finished
    crosshair3Components = crosshair3.components
    for thisComponent in crosshair3.components:
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
    
    # --- Run Routine "crosshair3" ---
    crosshair3.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_23* updates
        
        # if text_23 is starting this frame...
        if text_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_23.frameNStart = frameN  # exact frame index
            text_23.tStart = t  # local t and not account for scr refresh
            text_23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_23, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_23.started')
            # update status
            text_23.status = STARTED
            text_23.setAutoDraw(True)
        
        # if text_23 is active this frame...
        if text_23.status == STARTED:
            # update params
            pass
        
        # if text_23 is stopping this frame...
        if text_23.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_23.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                text_23.tStop = t  # not accounting for scr refresh
                text_23.tStopRefresh = tThisFlipGlobal  # on global time
                text_23.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_23.stopped')
                # update status
                text_23.status = FINISHED
                text_23.setAutoDraw(False)
        # Run 'Each Frame' code from code_23
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
                currentRoutine=crosshair3,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            crosshair3.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in crosshair3.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "crosshair3" ---
    for thisComponent in crosshair3.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for crosshair3
    crosshair3.tStop = globalClock.getTime(format='float')
    crosshair3.tStopRefresh = tThisFlipGlobal
    thisExp.addData('crosshair3.stopped', crosshair3.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if crosshair3.maxDurationReached:
        routineTimer.addTime(-crosshair3.maxDuration)
    elif crosshair3.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "scannerWait" ---
    # create an object to store info about Routine scannerWait
    scannerWait = data.Routine(
        name='scannerWait',
        components=[waitImage],
    )
    scannerWait.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for scannerWait
    scannerWait.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    scannerWait.tStart = globalClock.getTime(format='float')
    scannerWait.status = STARTED
    thisExp.addData('scannerWait.started', scannerWait.tStart)
    scannerWait.maxDuration = None
    # keep track of which components have finished
    scannerWaitComponents = scannerWait.components
    for thisComponent in scannerWait.components:
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
    
    # --- Run Routine "scannerWait" ---
    scannerWait.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *waitImage* updates
        
        # if waitImage is starting this frame...
        if waitImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            waitImage.frameNStart = frameN  # exact frame index
            waitImage.tStart = t  # local t and not account for scr refresh
            waitImage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(waitImage, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'waitImage.started')
            # update status
            waitImage.status = STARTED
            waitImage.setAutoDraw(True)
        
        # if waitImage is active this frame...
        if waitImage.status == STARTED:
            # update params
            pass
        
        # if waitImage is stopping this frame...
        if waitImage.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > waitImage.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                waitImage.tStop = t  # not accounting for scr refresh
                waitImage.tStopRefresh = tThisFlipGlobal  # on global time
                waitImage.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'waitImage.stopped')
                # update status
                waitImage.status = FINISHED
                waitImage.setAutoDraw(False)
        
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
                currentRoutine=scannerWait,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            scannerWait.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in scannerWait.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "scannerWait" ---
    for thisComponent in scannerWait.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for scannerWait
    scannerWait.tStop = globalClock.getTime(format='float')
    scannerWait.tStopRefresh = tThisFlipGlobal
    thisExp.addData('scannerWait.stopped', scannerWait.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if scannerWait.maxDurationReached:
        routineTimer.addTime(-scannerWait.maxDuration)
    elif scannerWait.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "startTask" ---
    # create an object to store info about Routine startTask
    startTask = data.Routine(
        name='startTask',
        components=[text_4],
    )
    startTask.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
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
    while continueRoutine and routineTimer.getTime() < 10.0:
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
        
        # if text_4 is stopping this frame...
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.tStopRefresh = tThisFlipGlobal  # on global time
                text_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_4.stopped')
                # update status
                text_4.status = FINISHED
                text_4.setAutoDraw(False)
        
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
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if startTask.maxDurationReached:
        routineTimer.addTime(-startTask.maxDuration)
    elif startTask.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-10.000000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    learningLoop = data.TrialHandler2(
        name='learningLoop',
        nReps=4.0, 
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
                if len(limited_block) > 0:
                    print(f"DEBUG LIMITED BLOCK: First trial block type = '{limited_block[0].get('block', 'unknown')}', should be '{first_block_type}'")
                    if len(limited_block) > trials_per_block:
                        print(f"DEBUG LIMITED BLOCK: Trial at index {trials_per_block} block type = '{limited_block[trials_per_block].get('block', 'unknown')}', should be '{second_block_type}'")
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
        
        # Reset slider to random starting value and ensure it's visible
        if 'slider' in locals():
            import random
            # Get slider min/max if available, otherwise use reasonable defaults
            slider_min = -100  # Default minimum
            slider_max = 100   # Default maximum
            try:
                if hasattr(slider, 'min'):
                    slider_min = slider.min
                if hasattr(slider, 'max'):
                    slider_max = slider.max
            except:
                pass
            
            # Generate random starting value within slider range
            random_start_value = random.randint(int(slider_min), int(slider_max))
            
            # Round to nearest 5 to match slider granularity (what's displayed)
            # Slider has granularity=5, so values are rounded to nearest 5 for display
            # Examples: 64 → 65, 32 → 30, -69 → -70
            rounded_start_value = round(random_start_value / 5) * 5
            
            slider.reset()
            slider.setRating(rounded_start_value)  # Start at rounded value (matches display)
            print(f"Slider reset to random starting value: {random_start_value} → {rounded_start_value} (rounded to nearest 5, range: {slider_min} to {slider_max})")
            
            # Store rounded slider starting value in globals for logging (matches what's displayed)
            globals()['slider_starting_value'] = rounded_start_value
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
            
            # Defer CSV logging until after timing durations are computed (so we can log crosshair durations)
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
            # Convert to int for display (trueVal can be float)
            actual_points_text = f"Actual points: {int(trueVal):+d}"
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
            
            # Store in globals so Builder can access them via $variableName
            globals()['crosshair1_duration'] = crosshair1_duration
            globals()['actualPoints_duration'] = actualPoints_duration
            globals()['crosshair2_duration'] = crosshair2_duration
            globals()['timeout_duration'] = timeout_duration
            
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
            
            # Store in globals so Builder can access them via $variableName
            globals()['timeout_duration'] = timeout_duration
            globals()['crosshair1_duration'] = crosshair1_duration
            globals()['actualPoints_duration'] = actualPoints_duration
            globals()['crosshair2_duration'] = crosshair2_duration
            
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
        
        # Log trial to CSV (includes crosshair durations)
        try:
            data_logger = globals().get('data_logger', None)
            if data_logger:
                slider_starting_value = globals().get('slider_starting_value', None)
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
                    trial_timed_out=trial_timed_out,
                    slider_starting_value=slider_starting_value,
                    crosshair1_duration=globals().get('crosshair1_duration', None),
                    crosshair2_duration=globals().get('crosshair2_duration', None),
                    crosshair1_rand=globals().get('crosshair1_rand', None),
                    crosshair2_rand=globals().get('crosshair2_rand', None),
                    timeout_duration=globals().get('timeout_duration', None),
                    actual_points_duration=globals().get('actualPoints_duration', None),
                )
        except Exception as e:
            print(f"Error logging trial data (with crosshair durations): {e}")
        
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
            components=[image_30],
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
            # Convert to int for display (trueVal can be float)
            actual_points_text = f"Actual points: {int(trueVal):+d}"
        elif 'trueVal' in globals():
            # Convert to int for display (trueVal can be float)
            actual_points_text = f"Actual points: {int(trueVal):+d}"
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
        # Try multiple possible component names
        if 'text_actual_points' in locals():
            text_actual_points.text = actual_points_text
            text_actual_points.opacity = 1
            text_actual_points.setAutoDraw(True)
            print(f"Showing actual points: {actual_points_text}")
        elif 'image_30' in locals():
            # Handle case where component was accidentally renamed to image_30
            image_30.text = actual_points_text
            image_30.opacity = 1
            image_30.setAutoDraw(True)
            print(f"Showing actual points (via image_30): {actual_points_text}")
        else:
            print("WARNING: text_actual_points or image_30 component not found!")
        
        # Ensure actualPoints_duration is available from globals
        # This helps Builder access it for the routine duration
        if 'actualPoints_duration' not in globals():
            # Fallback to default if not set yet
            globals()['actualPoints_duration'] = 2.0
            print("WARNING: actualPoints_duration not found in globals, using default 2.0")
        else:
            print(f"actualPoints_duration is {globals()['actualPoints_duration']} seconds")
        
        
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
            
            # *image_30* updates
            
            # if image_30 is starting this frame...
            if image_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_30.frameNStart = frameN  # exact frame index
                image_30.tStart = t  # local t and not account for scr refresh
                image_30.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_30, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_30.started')
                # update status
                image_30.status = STARTED
                image_30.setAutoDraw(True)
            
            # if image_30 is active this frame...
            if image_30.status == STARTED:
                # update params
                pass
            
            # if image_30 is stopping this frame...
            if image_30.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_30.tStartRefresh + actualPoints_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    image_30.tStop = t  # not accounting for scr refresh
                    image_30.tStopRefresh = tThisFlipGlobal  # on global time
                    image_30.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_30.stopped')
                    # update status
                    image_30.status = FINISHED
                    image_30.setAutoDraw(False)
            
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
        # Run 'End Routine' code from code_8
        # Hide actual points text
        if 'text_actual_points' in locals():
            text_actual_points.setAutoDraw(False)
            text_actual_points.opacity = 0
        elif 'image_30' in locals():
            image_30.setAutoDraw(False)
            image_30.opacity = 0
        
        # Clear any key presses
        try:
            event.clearEvents()
        except:
            pass
        
        print("Actual points routine ended")
        
        
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
        # Shows "You completed the first block. Press C to move on to next block."
        
        # Check if we should show this screen (only after first block completes, and only once)
        show_block_transition = globals().get('show_block_transition', False)
        ready_for_block2_setup = globals().get('ready_for_block2_setup', False)
        learning_block_index = globals().get('learning_block_index', -1)
        total_expected = globals().get('total_trials', 120)
        trials_per_block = total_expected // 2
        
        # Only show if:
        # 1. Flag is set to True
        # 2. Block 2 setup hasn't been completed yet (ready_for_block2_setup = False)
        # 3. We're still in or just finished the first block (learning_block_index < trials_per_block)
        if not show_block_transition or ready_for_block2_setup or learning_block_index >= trials_per_block:
            # Don't show transition screen - skip this routine
            if not show_block_transition:
                print("Skipping block transition screen (flag not set)")
            elif ready_for_block2_setup:
                print("Skipping block transition screen (block 2 setup already completed)")
            elif learning_block_index >= trials_per_block:
                print(f"Skipping block transition screen (already past first block: index={learning_block_index}, trials_per_block={trials_per_block})")
            continueRoutine = False
        else:
            # Show the transition screen
            transitionText = "You completed the first block.\n\nPress C to move on to next block."
            
            # Set the text component (make sure component name matches your Builder setup)
            if 'text_block_transition' in locals():
                text_block_transition.text = transitionText
                text_block_transition.opacity = 1
                text_block_transition.setAutoDraw(True)
                print("Showing block transition screen")
            else:
                print("WARNING: text_block_transition component not found!")
            
            # Clear any previous key presses IMMEDIATELY to prevent carryover
            try:
                event.clearEvents()
                # Also clear any keyboard component buffers
                if 'key_resp_transition' in locals() and hasattr(key_resp_transition, 'keys'):
                    key_resp_transition.keys = []
            except:
                pass
            
            # Set a timestamp to ignore any keys pressed before this routine started
            import time
            globals()['block_transition_start_time'] = time.time()
            print(f"Block transition: Routine started at {globals()['block_transition_start_time']}, cleared key buffer")
        
        
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
                theseKeys = key_resp_transition.getKeys(keyList=['c', 'C'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_transition_allKeys.extend(theseKeys)
                if len(_key_resp_transition_allKeys):
                    key_resp_transition.keys = _key_resp_transition_allKeys[-1].name  # just the last key pressed
                    key_resp_transition.rt = _key_resp_transition_allKeys[-1].rt
                    key_resp_transition.duration = _key_resp_transition_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            # Run 'Each Frame' code from code_16
            # Block transition screen - wait for key press 2 to continue
            
            # Only show if flag is set (double-check)
            show_block_transition = globals().get('show_block_transition', False)
            if not show_block_transition:
                continueRoutine = False
            else:
                # Check for key press 2 (or num_2)
                # Only accept keys pressed AFTER this routine started (ignore carryover)
                import time
                routine_start_time = globals().get('block_transition_start_time', time.time())
                current_time = time.time()
                
                # Only process keys if at least 0.1 seconds have passed since routine started
                # This prevents using keys that were pressed before the routine started
                if current_time - routine_start_time >= 0.1:
                    try:
                        keys = event.getKeys(keyList=['2', 'num_2'])
                        if '2' in keys or 'num_2' in keys:
                            # User pressed 2, continue to next block
                            print("Key 2 pressed - moving to next block")
                            # Reset the flag so it doesn't show again
                            globals()['show_block_transition'] = False
                            # Set flag to indicate we're ready for block 2 setup
                            globals()['ready_for_block2_setup'] = True
                            print(f"DEBUG: Set ready_for_block2_setup = True")
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
                                    # Set flag to indicate we're ready for block 2 setup
                                    globals()['ready_for_block2_setup'] = True
                                    print(f"DEBUG: Set ready_for_block2_setup = True (keyboard component)")
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
        # Run 'End Routine' code from code_16
        # Hide block transition text when routine ends
        if 'text_block_transition' in locals():
            text_block_transition.setAutoDraw(False)
            text_block_transition.opacity = 0
            print("Block transition text hidden")
        
        # Clear any remaining key presses
        try:
            event.clearEvents()
        except:
            pass
        
        # IMPORTANT: Reset the show_block_transition flag to False so it doesn't show again
        # This ensures it only shows once after the first block
        globals()['show_block_transition'] = False
        
        # Ensure the flag is set correctly
        globals()['ready_for_block2_setup'] = True
        print("Block transition ended, ready for block 2 setup")
        print("  - show_block_transition set to False (will not show again)")
        print("  - ready_for_block2_setup set to True")
        
        
        
        # the Routine "blockTransition" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "taskStartSoonBlock2" ---
        # create an object to store info about Routine taskStartSoonBlock2
        taskStartSoonBlock2 = data.Routine(
            name='taskStartSoonBlock2',
            components=[key_resp_task_start_block2, text_task_start_soon_block2],
        )
        taskStartSoonBlock2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_26
        # "Task will start soon. Press C to continue" screen - for second block
        # Only shows after first block completes (after blockTransition)
        # Component: text_task_start_soon_block2 (or similar text component)
        
        # Check if we should show this (only after block transition completes, and only once)
        # The blockTransition sets ready_for_block2_setup = True when user presses 2
        ready_for_block2_setup = globals().get('ready_for_block2_setup', False)
        block2_setup_complete = globals().get('block2_setup_complete', False)
        
        # Also check if we've already started Block 2 trials (once Block 2 has started, never show this again)
        learning_block_index = globals().get('learning_block_index', -1)
        total_expected = globals().get('total_trials', 120)
        trials_per_block = total_expected // 2
        
        # DEBUG: Print flag states
        print(f"DEBUG taskStartSoonBlock2: ready_for_block2_setup={ready_for_block2_setup}, block2_setup_complete={block2_setup_complete}, learning_block_index={learning_block_index}, trials_per_block={trials_per_block}")
        
        # Skip if:
        # 1. Block transition hasn't completed yet (ready_for_block2_setup = False)
        # 2. Block 2 setup already done (block2_setup_complete = True)
        # 3. Still in Block 1 (learning_block_index < trials_per_block - 1)
        # 4. Already well into Block 2 (learning_block_index > trials_per_block)
        # Show during transition: learning_block_index >= trials_per_block - 1 AND learning_block_index <= trials_per_block
        if not ready_for_block2_setup or block2_setup_complete or learning_block_index < trials_per_block - 1 or learning_block_index > trials_per_block:
            # Skip this routine
            if block2_setup_complete:
                print("Skipping taskStartSoonBlock2 (block 2 setup already completed)")
            elif learning_block_index < trials_per_block - 1:
                print(f"Skipping taskStartSoonBlock2 (still in Block 1, learning_block_index={learning_block_index} < trials_per_block-1={trials_per_block-1})")
            elif learning_block_index > trials_per_block:
                print(f"Skipping taskStartSoonBlock2 (already in Block 2, learning_block_index={learning_block_index} > trials_per_block={trials_per_block})")
            else:
                print(f"Skipping taskStartSoonBlock2 (block transition not completed yet, ready_for_block2_setup={ready_for_block2_setup})")
            continueRoutine = False
        else:
            # We're past the first block - show the screen
            # IMPORTANT: Hide any previous text components first to prevent overlap
            if 'text_block_transition' in locals():
                text_block_transition.setAutoDraw(False)
                text_block_transition.opacity = 0
                print("Hidden block transition text")
            
            # Clear any previous key presses IMMEDIATELY to prevent carryover
            try:
                event.clearEvents()
                # Also clear any keyboard component buffers
                if 'key_resp_task_start_block2' in locals() and hasattr(key_resp_task_start_block2, 'keys'):
                    key_resp_task_start_block2.keys = []
            except:
                pass
        
            # Set a timestamp to ignore any keys pressed before this routine started
            import time
            globals()['taskStartSoonBlock2_start_time'] = time.time()
            print(f"Task start soon Block 2: Routine started at {globals()['taskStartSoonBlock2_start_time']}, cleared key buffer")
        
            # Display task start message
            if 'text_task_start_soon_block2' in locals():
                text_task_start_soon_block2.text = "The task will start soon. Press C to continue"
                text_task_start_soon_block2.opacity = 1
                text_task_start_soon_block2.setAutoDraw(True)
                print("Task start soon screen displayed (for second block)")
            else:
                print("WARNING: text_task_start_soon_block2 component not found!")
        
        
        # create starting attributes for key_resp_task_start_block2
        key_resp_task_start_block2.keys = []
        key_resp_task_start_block2.rt = []
        _key_resp_task_start_block2_allKeys = []
        # store start times for taskStartSoonBlock2
        taskStartSoonBlock2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        taskStartSoonBlock2.tStart = globalClock.getTime(format='float')
        taskStartSoonBlock2.status = STARTED
        thisExp.addData('taskStartSoonBlock2.started', taskStartSoonBlock2.tStart)
        taskStartSoonBlock2.maxDuration = None
        # keep track of which components have finished
        taskStartSoonBlock2Components = taskStartSoonBlock2.components
        for thisComponent in taskStartSoonBlock2.components:
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
        
        # --- Run Routine "taskStartSoonBlock2" ---
        taskStartSoonBlock2.forceEnded = routineForceEnded = not continueRoutine
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
            # Run 'Each Frame' code from code_26
            # Task start soon Block 2 - wait for key press 'C' to continue
            # Only runs if block transition has completed
            
            # Check if we should still be showing this
            ready_for_block2_setup = globals().get('ready_for_block2_setup', False)
            block2_setup_complete = globals().get('block2_setup_complete', False)
            
            # Also check if we've already started Block 2 trials
            learning_block_index = globals().get('learning_block_index', -1)
            total_expected = globals().get('total_trials', 120)
            trials_per_block = total_expected // 2
            
            # Skip if any of these conditions are true
            # Skip if: still in Block 1, OR block 2 setup already done, OR block transition hasn't completed, OR already in Block 2
            if not ready_for_block2_setup or block2_setup_complete or learning_block_index < trials_per_block - 1 or learning_block_index > trials_per_block:
                # Block transition hasn't completed yet OR block 2 setup already done OR still in Block 1 OR already in Block 2 - skip
                continueRoutine = False
            else:
                # Check for key press 'C' to continue
                # Only accept keys pressed AFTER this routine started (ignore carryover)
                import time
                routine_start_time = globals().get('taskStartSoonBlock2_start_time', time.time())
                current_time = time.time()
                
                # Only process keys if at least 0.1 seconds have passed since routine started
                # This prevents using keys that were pressed before the routine started
                if current_time - routine_start_time >= 0.1:
                    try:
                        keys = event.getKeys(keyList=['c', 'C'])
                        if keys:
                            # Key C pressed - continue to scanner sync
                            print("Task start soon Block 2: Key C pressed, continuing to scanner sync")
                            continueRoutine = False
                            event.clearEvents()
                            # Set flag for scanner sync
                            globals()['ready_for_scanner_sync_block2'] = True
                    except:
                        pass
            
            
            
            # *key_resp_task_start_block2* updates
            waitOnFlip = False
            
            # if key_resp_task_start_block2 is starting this frame...
            if key_resp_task_start_block2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_task_start_block2.frameNStart = frameN  # exact frame index
                key_resp_task_start_block2.tStart = t  # local t and not account for scr refresh
                key_resp_task_start_block2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_task_start_block2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_task_start_block2.started')
                # update status
                key_resp_task_start_block2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_task_start_block2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_task_start_block2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_task_start_block2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_task_start_block2.getKeys(keyList=['c', 'C'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_task_start_block2_allKeys.extend(theseKeys)
                if len(_key_resp_task_start_block2_allKeys):
                    key_resp_task_start_block2.keys = _key_resp_task_start_block2_allKeys[-1].name  # just the last key pressed
                    key_resp_task_start_block2.rt = _key_resp_task_start_block2_allKeys[-1].rt
                    key_resp_task_start_block2.duration = _key_resp_task_start_block2_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *text_task_start_soon_block2* updates
            
            # if text_task_start_soon_block2 is starting this frame...
            if text_task_start_soon_block2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_task_start_soon_block2.frameNStart = frameN  # exact frame index
                text_task_start_soon_block2.tStart = t  # local t and not account for scr refresh
                text_task_start_soon_block2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_task_start_soon_block2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_task_start_soon_block2.started')
                # update status
                text_task_start_soon_block2.status = STARTED
                text_task_start_soon_block2.setAutoDraw(True)
            
            # if text_task_start_soon_block2 is active this frame...
            if text_task_start_soon_block2.status == STARTED:
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
                    currentRoutine=taskStartSoonBlock2,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                taskStartSoonBlock2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in taskStartSoonBlock2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "taskStartSoonBlock2" ---
        for thisComponent in taskStartSoonBlock2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for taskStartSoonBlock2
        taskStartSoonBlock2.tStop = globalClock.getTime(format='float')
        taskStartSoonBlock2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('taskStartSoonBlock2.stopped', taskStartSoonBlock2.tStop)
        # Run 'End Routine' code from code_26
        # Hide task start soon Block 2 text when routine ends
        if 'text_task_start_soon_block2' in locals():
            text_task_start_soon_block2.setAutoDraw(False)
            text_task_start_soon_block2.opacity = 0
            print("Task start soon Block 2 text hidden")
        
        # Clear any remaining key presses
        try:
            event.clearEvents()
        except:
            pass
        
        # IMPORTANT: Set flag to indicate taskStartSoonBlock2 completed, ready for scanner sync
        globals()['ready_for_scanner_sync_block2'] = True
        print("Task start soon Block 2 ended, ready for scanner sync (ready_for_scanner_sync_block2 = True)")
        
        
        
        # check responses
        if key_resp_task_start_block2.keys in ['', [], None]:  # No response was made
            key_resp_task_start_block2.keys = None
        learningLoop.addData('key_resp_task_start_block2.keys',key_resp_task_start_block2.keys)
        if key_resp_task_start_block2.keys != None:  # we had a response
            learningLoop.addData('key_resp_task_start_block2.rt', key_resp_task_start_block2.rt)
            learningLoop.addData('key_resp_task_start_block2.duration', key_resp_task_start_block2.duration)
        # the Routine "taskStartSoonBlock2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "scannerSyncBlock2" ---
        # create an object to store info about Routine scannerSyncBlock2
        scannerSyncBlock2 = data.Routine(
            name='scannerSyncBlock2',
            components=[text_scanner_wait_2, key_resp_13],
        )
        scannerSyncBlock2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_25
        # MRI Scanner sync Block 2 - wait for scanner trigger (key '5')
        # Only shows after first block completes (after blockTransition and taskStartSoonBlock2)
        # Component: text_scanner_wait_block2 (or similar text component)
        
        # Check if we should show this (only after taskStartSoonBlock2 completes, and only once)
        # taskStartSoonBlock2 sets ready_for_scanner_sync_block2 = True when user presses C
        ready_for_scanner_sync_block2 = globals().get('ready_for_scanner_sync_block2', False)
        block2_setup_complete = globals().get('block2_setup_complete', False)
        
        # Also check if we've already started Block 2 trials (once Block 2 has started, never show this again)
        learning_block_index = globals().get('learning_block_index', -1)
        total_expected = globals().get('total_trials', 120)
        trials_per_block = total_expected // 2
        
        # DEBUG: Print flag states
        print(f"DEBUG scannerSyncBlock2: ready_for_scanner_sync_block2={ready_for_scanner_sync_block2}, block2_setup_complete={block2_setup_complete}, learning_block_index={learning_block_index}, trials_per_block={trials_per_block}")
        print(f"DEBUG scannerSyncBlock2: Condition check - block2_setup_complete={block2_setup_complete}, not ready={not ready_for_scanner_sync_block2}, index too low={learning_block_index < trials_per_block - 1}, index too high={learning_block_index > trials_per_block}")
        
        # Skip if:
        # 1. Block 2 setup already done (block2_setup_complete = True) - NEVER show again once setup is complete
        # 2. taskStartSoonBlock2 hasn't completed yet (ready_for_scanner_sync_block2 = False)
        # 3. Still in Block 1 (learning_block_index < trials_per_block - 1)
        # 4. Already well into Block 2 trials (learning_block_index > trials_per_block) - once Block 2 trials start, never show again
        # Show during transition: learning_block_index >= trials_per_block - 1 AND learning_block_index <= trials_per_block AND ready_for_scanner_sync_block2 = True
        # NOTE: learning_block_index is 0-indexed, so after last trial of block 1, it equals trials_per_block - 1
        should_skip = block2_setup_complete or not ready_for_scanner_sync_block2 or learning_block_index < trials_per_block - 1 or learning_block_index > trials_per_block
        print(f"DEBUG scannerSyncBlock2: should_skip = {should_skip}")
        if should_skip:
            # Skip this routine
            if block2_setup_complete:
                print("Skipping scannerSyncBlock2 (block 2 setup already completed)")
            elif learning_block_index < trials_per_block - 1:
                print(f"Skipping scannerSyncBlock2 (still in Block 1, learning_block_index={learning_block_index} < trials_per_block-1={trials_per_block-1})")
            elif learning_block_index > trials_per_block:
                print(f"Skipping scannerSyncBlock2 (already in Block 2 trials, learning_block_index={learning_block_index} > trials_per_block={trials_per_block})")
            else:
                print(f"Skipping scannerSyncBlock2 (taskStartSoonBlock2 not completed yet, ready_for_scanner_sync_block2={ready_for_scanner_sync_block2})")
            continueRoutine = False
        else:
            # We're past the first block - show the scanner sync
            # Clear any previous key presses IMMEDIATELY to prevent carryover
            try:
                event.clearEvents()
                # Also clear any keyboard component buffers
                if 'key_resp_scanner_block2' in locals() and hasattr(key_resp_scanner_block2, 'keys'):
                    key_resp_scanner_block2.keys = []
            except:
                pass
        
            # Set a timestamp to ignore any keys pressed before this routine started
            import time
            globals()['scannerSyncBlock2_start_time'] = time.time()
            print(f"Scanner sync Block 2: Routine started at {globals()['scannerSyncBlock2_start_time']}, cleared key buffer")
        
            # Display waiting message
            if 'text_scanner_wait_block2' in locals():
                text_scanner_wait_block2.text = "Waiting for the scanner to start..."
                text_scanner_wait_block2.opacity = 1
                text_scanner_wait_block2.setAutoDraw(True)
                print("Scanner sync Block 2: Waiting for trigger '5' from MRI scanner")
            else:
                print("WARNING: text_scanner_wait_block2 component not found!")
        
        
        # create starting attributes for key_resp_13
        key_resp_13.keys = []
        key_resp_13.rt = []
        _key_resp_13_allKeys = []
        # store start times for scannerSyncBlock2
        scannerSyncBlock2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        scannerSyncBlock2.tStart = globalClock.getTime(format='float')
        scannerSyncBlock2.status = STARTED
        thisExp.addData('scannerSyncBlock2.started', scannerSyncBlock2.tStart)
        scannerSyncBlock2.maxDuration = None
        # keep track of which components have finished
        scannerSyncBlock2Components = scannerSyncBlock2.components
        for thisComponent in scannerSyncBlock2.components:
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
        
        # --- Run Routine "scannerSyncBlock2" ---
        scannerSyncBlock2.forceEnded = routineForceEnded = not continueRoutine
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
            # Run 'Each Frame' code from code_25
            # Scanner sync Block 2 - wait for MRI scanner trigger (key '5')
            # Only runs if taskStartSoonBlock2 has completed
            
            # Check if we should still be showing this
            ready_for_scanner_sync_block2 = globals().get('ready_for_scanner_sync_block2', False)
            block2_setup_complete = globals().get('block2_setup_complete', False)
            
            # Also check if we've already started Block 2 trials
            learning_block_index = globals().get('learning_block_index', -1)
            total_expected = globals().get('total_trials', 120)
            trials_per_block = total_expected // 2
            
            # Skip if any of these conditions are true
            # Skip if: block 2 setup already done (NEVER show again), OR still in Block 1, OR taskStartSoonBlock2 hasn't completed, OR already well into Block 2 trials
            # Allow during transition: learning_block_index >= trials_per_block - 1 AND learning_block_index <= trials_per_block
            if block2_setup_complete or not ready_for_scanner_sync_block2 or learning_block_index < trials_per_block - 1 or learning_block_index > trials_per_block:
                # taskStartSoonBlock2 hasn't completed yet OR block 2 setup already done OR still in Block 1 OR already in Block 2 - skip
                continueRoutine = False
            else:
                # The MRI sends '5' when it's ready
                # Only accept keys pressed AFTER this routine started (ignore carryover)
                import time
                routine_start_time = globals().get('scannerSyncBlock2_start_time', time.time())
                current_time = time.time()
                
                # Only process keys if at least 0.1 seconds have passed since routine started
                # This prevents using keys that were pressed before the routine started
                if current_time - routine_start_time >= 0.1:
                    try:
                        keys = event.getKeys(keyList=['5', 'num_5'])
                        if keys:
                            # Scanner trigger received - continue to next screen
                            print("Scanner sync Block 2: Trigger '5' received from MRI scanner, continuing")
                            continueRoutine = False
                            event.clearEvents()
                    except:
                        pass
            
            
            
            # *text_scanner_wait_2* updates
            
            # if text_scanner_wait_2 is starting this frame...
            if text_scanner_wait_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_scanner_wait_2.frameNStart = frameN  # exact frame index
                text_scanner_wait_2.tStart = t  # local t and not account for scr refresh
                text_scanner_wait_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_scanner_wait_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_scanner_wait_2.started')
                # update status
                text_scanner_wait_2.status = STARTED
                text_scanner_wait_2.setAutoDraw(True)
            
            # if text_scanner_wait_2 is active this frame...
            if text_scanner_wait_2.status == STARTED:
                # update params
                pass
            
            # *key_resp_13* updates
            waitOnFlip = False
            
            # if key_resp_13 is starting this frame...
            if key_resp_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_13.frameNStart = frameN  # exact frame index
                key_resp_13.tStart = t  # local t and not account for scr refresh
                key_resp_13.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_13, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_13.started')
                # update status
                key_resp_13.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_13.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_13.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_13.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_13.getKeys(keyList=['5', 'num_5', 'num5'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_13_allKeys.extend(theseKeys)
                if len(_key_resp_13_allKeys):
                    key_resp_13.keys = _key_resp_13_allKeys[-1].name  # just the last key pressed
                    key_resp_13.rt = _key_resp_13_allKeys[-1].rt
                    key_resp_13.duration = _key_resp_13_allKeys[-1].duration
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
                    currentRoutine=scannerSyncBlock2,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                scannerSyncBlock2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in scannerSyncBlock2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "scannerSyncBlock2" ---
        for thisComponent in scannerSyncBlock2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for scannerSyncBlock2
        scannerSyncBlock2.tStop = globalClock.getTime(format='float')
        scannerSyncBlock2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('scannerSyncBlock2.stopped', scannerSyncBlock2.tStop)
        # Run 'End Routine' code from code_25
        # Hide scanner wait Block 2 text
        if 'text_scanner_wait_block2' in locals():
            text_scanner_wait_block2.setAutoDraw(False)
            text_scanner_wait_block2.opacity = 0
        
        # Clear any remaining key presses
        try:
            event.clearEvents()
        except:
            pass
        
        # Log scanner sync time (optional)
        import time
        scanner_sync_time = time.time()
        globals()['scanner_sync_time_block2'] = scanner_sync_time
        print(f"Scanner sync Block 2 completed at {scanner_sync_time}")
        
        # IMPORTANT: Do NOT set block2_setup_complete = True here
        # It should only be set after ALL scanner sync routines complete (crosshairBlock2 → scannerWaitBlock2 → crosshair2Block2)
        # Just clear the scanner sync flag
        globals()['ready_for_scanner_sync_block2'] = False
        print("Scanner sync Block 2 ended, proceeding to crosshairBlock2")
        
        
        # check responses
        if key_resp_13.keys in ['', [], None]:  # No response was made
            key_resp_13.keys = None
        learningLoop.addData('key_resp_13.keys',key_resp_13.keys)
        if key_resp_13.keys != None:  # we had a response
            learningLoop.addData('key_resp_13.rt', key_resp_13.rt)
            learningLoop.addData('key_resp_13.duration', key_resp_13.duration)
        # the Routine "scannerSyncBlock2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "crosshairBlock2" ---
        # create an object to store info about Routine crosshairBlock2
        crosshairBlock2 = data.Routine(
            name='crosshairBlock2',
            components=[text_crosshair_block2],
        )
        crosshairBlock2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_37
        # Crosshair Block 2 - 2 second fixation cross before Block 2 begins
        # Component: text_crosshair_block2 (or similar text component)
        
        # Check if Block 2 has already started - if so, skip this routine
        block2_setup_complete = globals().get('block2_setup_complete', False)
        learning_block_index = globals().get('learning_block_index', -1)
        total_expected = globals().get('total_trials', 120)
        trials_per_block = total_expected // 2
        
        # Skip if:
        # 1. Block 2 setup is complete (block2_setup_complete = True) - NEVER show again once setup is complete
        # 2. Still in Block 1 (learning_block_index < trials_per_block - 1)
        # 3. Already well into Block 2 trials (learning_block_index > trials_per_block) - once Block 2 trials start, never show again
        # Show during transition: learning_block_index >= trials_per_block - 1 AND learning_block_index <= trials_per_block
        if block2_setup_complete or learning_block_index < trials_per_block - 1 or learning_block_index > trials_per_block:
            print(f"Skipping crosshairBlock2 (learning_block_index={learning_block_index}, trials_per_block={trials_per_block}, block2_setup_complete={block2_setup_complete})")
            continueRoutine = False
        else:
            # Show fixation cross
            if 'text_crosshair_block2' in locals():
                text_crosshair_block2.text = "+"
                try:
                    text_crosshair_block2.setPos((0, 0))
                except AttributeError:
                    text_crosshair_block2.pos = (0, 0)
                text_crosshair_block2.opacity = 1
                text_crosshair_block2.setAutoDraw(True)
                print("Crosshair Block 2: Showing fixation cross (2 seconds)")
            else:
                print("WARNING: text_crosshair_block2 component not found!")
        
        
        
        # store start times for crosshairBlock2
        crosshairBlock2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        crosshairBlock2.tStart = globalClock.getTime(format='float')
        crosshairBlock2.status = STARTED
        thisExp.addData('crosshairBlock2.started', crosshairBlock2.tStart)
        crosshairBlock2.maxDuration = None
        # keep track of which components have finished
        crosshairBlock2Components = crosshairBlock2.components
        for thisComponent in crosshairBlock2.components:
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
        
        # --- Run Routine "crosshairBlock2" ---
        crosshairBlock2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # if trial has changed, end Routine now
            if hasattr(thisLearningLoop, 'status') and thisLearningLoop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_crosshair_block2* updates
            
            # if text_crosshair_block2 is starting this frame...
            if text_crosshair_block2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_crosshair_block2.frameNStart = frameN  # exact frame index
                text_crosshair_block2.tStart = t  # local t and not account for scr refresh
                text_crosshair_block2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_crosshair_block2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_crosshair_block2.started')
                # update status
                text_crosshair_block2.status = STARTED
                text_crosshair_block2.setAutoDraw(True)
            
            # if text_crosshair_block2 is active this frame...
            if text_crosshair_block2.status == STARTED:
                # update params
                pass
            
            # if text_crosshair_block2 is stopping this frame...
            if text_crosshair_block2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_crosshair_block2.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_crosshair_block2.tStop = t  # not accounting for scr refresh
                    text_crosshair_block2.tStopRefresh = tThisFlipGlobal  # on global time
                    text_crosshair_block2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_crosshair_block2.stopped')
                    # update status
                    text_crosshair_block2.status = FINISHED
                    text_crosshair_block2.setAutoDraw(False)
            # Run 'Each Frame' code from code_37
            # Crosshair Block 2 - just displays fixation cross, no interaction needed
            # Check if Block 2 has already started - if so, skip this routine
            block2_setup_complete = globals().get('block2_setup_complete', False)
            learning_block_index = globals().get('learning_block_index', -1)
            total_expected = globals().get('total_trials', 120)
            trials_per_block = total_expected // 2
            
            # Skip if Block 2 setup is complete OR Block 2 has already started (well into Block 2)
            # Allow during transition: learning_block_index >= trials_per_block - 1 AND learning_block_index <= trials_per_block
            if block2_setup_complete or learning_block_index > trials_per_block:
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
                    currentRoutine=crosshairBlock2,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                crosshairBlock2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in crosshairBlock2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "crosshairBlock2" ---
        for thisComponent in crosshairBlock2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for crosshairBlock2
        crosshairBlock2.tStop = globalClock.getTime(format='float')
        crosshairBlock2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('crosshairBlock2.stopped', crosshairBlock2.tStop)
        # Run 'End Routine' code from code_37
        # Hide crosshair when routine ends
        if 'text_crosshair_block2' in locals():
            text_crosshair_block2.setAutoDraw(False)
            text_crosshair_block2.opacity = 0
        
        
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if crosshairBlock2.maxDurationReached:
            routineTimer.addTime(-crosshairBlock2.maxDuration)
        elif crosshairBlock2.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # --- Prepare to start Routine "scannerWaitBlock2" ---
        # create an object to store info about Routine scannerWaitBlock2
        scannerWaitBlock2 = data.Routine(
            name='scannerWaitBlock2',
            components=[image_scanner_wait_block2],
        )
        scannerWaitBlock2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_38
        # Scanner wait Block 2 - 2 second display of unrelated image before Block 2 begins
        # Component: image_scanner_wait_block2 (or similar image component)
        
        # Check if Block 2 has already started - if so, skip this routine
        block2_setup_complete = globals().get('block2_setup_complete', False)
        learning_block_index = globals().get('learning_block_index', -1)
        total_expected = globals().get('total_trials', 120)
        trials_per_block = total_expected // 2
        
        # Skip if:
        # 1. Block 2 setup is complete (block2_setup_complete = True) - NEVER show again once setup is complete
        # 2. Still in Block 1 (learning_block_index < trials_per_block - 1)
        # 3. Already well into Block 2 trials (learning_block_index > trials_per_block) - once Block 2 trials start, never show again
        # Show during transition: learning_block_index >= trials_per_block - 1 AND learning_block_index <= trials_per_block
        if block2_setup_complete or learning_block_index < trials_per_block - 1 or learning_block_index > trials_per_block:
            print(f"Skipping scannerWaitBlock2 (learning_block_index={learning_block_index}, trials_per_block={trials_per_block}, block2_setup_complete={block2_setup_complete})")
            continueRoutine = False
        else:
            # Show unrelated image (2 seconds)
            if 'image_scanner_wait_block2' in locals():
                # Set image to some unrelated image (e.g., "images/unrelated.png" or similar)
                # You may need to adjust the image path based on your setup
                image_scanner_wait_block2.opacity = 1
                image_scanner_wait_block2.setAutoDraw(True)
                print("Scanner wait Block 2: Showing unrelated image (2 seconds)")
            else:
                print("WARNING: image_scanner_wait_block2 component not found!")
        
        
        
        # store start times for scannerWaitBlock2
        scannerWaitBlock2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        scannerWaitBlock2.tStart = globalClock.getTime(format='float')
        scannerWaitBlock2.status = STARTED
        thisExp.addData('scannerWaitBlock2.started', scannerWaitBlock2.tStart)
        scannerWaitBlock2.maxDuration = None
        # keep track of which components have finished
        scannerWaitBlock2Components = scannerWaitBlock2.components
        for thisComponent in scannerWaitBlock2.components:
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
        
        # --- Run Routine "scannerWaitBlock2" ---
        scannerWaitBlock2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # if trial has changed, end Routine now
            if hasattr(thisLearningLoop, 'status') and thisLearningLoop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_scanner_wait_block2* updates
            
            # if image_scanner_wait_block2 is starting this frame...
            if image_scanner_wait_block2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_scanner_wait_block2.frameNStart = frameN  # exact frame index
                image_scanner_wait_block2.tStart = t  # local t and not account for scr refresh
                image_scanner_wait_block2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_scanner_wait_block2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_scanner_wait_block2.started')
                # update status
                image_scanner_wait_block2.status = STARTED
                image_scanner_wait_block2.setAutoDraw(True)
            
            # if image_scanner_wait_block2 is active this frame...
            if image_scanner_wait_block2.status == STARTED:
                # update params
                pass
            
            # if image_scanner_wait_block2 is stopping this frame...
            if image_scanner_wait_block2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_scanner_wait_block2.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    image_scanner_wait_block2.tStop = t  # not accounting for scr refresh
                    image_scanner_wait_block2.tStopRefresh = tThisFlipGlobal  # on global time
                    image_scanner_wait_block2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_scanner_wait_block2.stopped')
                    # update status
                    image_scanner_wait_block2.status = FINISHED
                    image_scanner_wait_block2.setAutoDraw(False)
            # Run 'Each Frame' code from code_38
            # Scanner wait Block 2 - just displays unrelated image, no interaction needed
            # Check if Block 2 has already started - if so, skip this routine
            block2_setup_complete = globals().get('block2_setup_complete', False)
            learning_block_index = globals().get('learning_block_index', -1)
            total_expected = globals().get('total_trials', 120)
            trials_per_block = total_expected // 2
            
            # Skip if Block 2 setup is complete OR Block 2 has already started (well into Block 2)
            # Allow during transition: learning_block_index >= trials_per_block - 1 AND learning_block_index <= trials_per_block
            if block2_setup_complete or learning_block_index > trials_per_block:
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
                    currentRoutine=scannerWaitBlock2,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                scannerWaitBlock2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in scannerWaitBlock2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "scannerWaitBlock2" ---
        for thisComponent in scannerWaitBlock2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for scannerWaitBlock2
        scannerWaitBlock2.tStop = globalClock.getTime(format='float')
        scannerWaitBlock2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('scannerWaitBlock2.stopped', scannerWaitBlock2.tStop)
        # Run 'End Routine' code from code_38
        # Hide scanner wait image when routine ends
        if 'image_scanner_wait_block2' in locals():
            image_scanner_wait_block2.setAutoDraw(False)
            image_scanner_wait_block2.opacity = 0
        # Do NOT set block2_setup_complete here - wait until after final crosshair (crosshair2Block2)
        
        
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if scannerWaitBlock2.maxDurationReached:
            routineTimer.addTime(-scannerWaitBlock2.maxDuration)
        elif scannerWaitBlock2.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # --- Prepare to start Routine "crosshair2Block2" ---
        # create an object to store info about Routine crosshair2Block2
        crosshair2Block2 = data.Routine(
            name='crosshair2Block2',
            components=[text_crosshair2_block2],
        )
        crosshair2Block2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_39
        # Crosshair2 Block 2 - 10 second fixation cross before Block 2 begins (final crosshair)
        # Component: text_crosshair2_block2 (or similar text component)
        
        # Check if Block 2 has already started - if so, skip this routine
        block2_setup_complete = globals().get('block2_setup_complete', False)
        learning_block_index = globals().get('learning_block_index', -1)
        total_expected = globals().get('total_trials', 120)
        trials_per_block = total_expected // 2
        
        # Skip if:
        # 1. Block 2 setup is complete (block2_setup_complete = True) - NEVER show again once setup is complete
        # 2. Still in Block 1 (learning_block_index < trials_per_block - 1)
        # 3. Already well into Block 2 trials (learning_block_index > trials_per_block) - once Block 2 trials start, never show again
        # Show during transition: learning_block_index >= trials_per_block - 1 AND learning_block_index <= trials_per_block
        if block2_setup_complete or learning_block_index < trials_per_block - 1 or learning_block_index > trials_per_block:
            print(f"Skipping crosshair2Block2 (learning_block_index={learning_block_index}, trials_per_block={trials_per_block}, block2_setup_complete={block2_setup_complete})")
            continueRoutine = False
        else:
            # Show fixation cross
            if 'text_crosshair2_block2' in locals():
                text_crosshair2_block2.text = "+"
                try:
                    text_crosshair2_block2.setPos((0, 0))
                except AttributeError:
                    text_crosshair2_block2.pos = (0, 0)
                text_crosshair2_block2.opacity = 1
                text_crosshair2_block2.setAutoDraw(True)
                print("Crosshair2 Block 2: Showing fixation cross (10 seconds)")
                # Set flag to indicate this routine actually ran
                globals()['crosshair2Block2_actually_ran'] = True
            else:
                print("WARNING: text_crosshair2_block2 component not found!")
        
        
        # store start times for crosshair2Block2
        crosshair2Block2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        crosshair2Block2.tStart = globalClock.getTime(format='float')
        crosshair2Block2.status = STARTED
        thisExp.addData('crosshair2Block2.started', crosshair2Block2.tStart)
        crosshair2Block2.maxDuration = None
        # keep track of which components have finished
        crosshair2Block2Components = crosshair2Block2.components
        for thisComponent in crosshair2Block2.components:
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
        
        # --- Run Routine "crosshair2Block2" ---
        crosshair2Block2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 10.0:
            # if trial has changed, end Routine now
            if hasattr(thisLearningLoop, 'status') and thisLearningLoop.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_crosshair2_block2* updates
            
            # if text_crosshair2_block2 is starting this frame...
            if text_crosshair2_block2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_crosshair2_block2.frameNStart = frameN  # exact frame index
                text_crosshair2_block2.tStart = t  # local t and not account for scr refresh
                text_crosshair2_block2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_crosshair2_block2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_crosshair2_block2.started')
                # update status
                text_crosshair2_block2.status = STARTED
                text_crosshair2_block2.setAutoDraw(True)
            
            # if text_crosshair2_block2 is active this frame...
            if text_crosshair2_block2.status == STARTED:
                # update params
                pass
            
            # if text_crosshair2_block2 is stopping this frame...
            if text_crosshair2_block2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_crosshair2_block2.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    text_crosshair2_block2.tStop = t  # not accounting for scr refresh
                    text_crosshair2_block2.tStopRefresh = tThisFlipGlobal  # on global time
                    text_crosshair2_block2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_crosshair2_block2.stopped')
                    # update status
                    text_crosshair2_block2.status = FINISHED
                    text_crosshair2_block2.setAutoDraw(False)
            # Run 'Each Frame' code from code_39
            # Crosshair2 Block 2 - just displays fixation cross, no interaction needed
            # Check if Block 2 has already started - if so, skip this routine
            block2_setup_complete = globals().get('block2_setup_complete', False)
            learning_block_index = globals().get('learning_block_index', -1)
            total_expected = globals().get('total_trials', 120)
            trials_per_block = total_expected // 2
            
            # Skip if Block 2 setup is complete OR Block 2 has already started (well into Block 2)
            # Allow during transition: learning_block_index >= trials_per_block - 1 AND learning_block_index <= trials_per_block
            if block2_setup_complete or learning_block_index > trials_per_block:
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
                    currentRoutine=crosshair2Block2,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                crosshair2Block2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in crosshair2Block2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "crosshair2Block2" ---
        for thisComponent in crosshair2Block2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for crosshair2Block2
        crosshair2Block2.tStop = globalClock.getTime(format='float')
        crosshair2Block2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('crosshair2Block2.stopped', crosshair2Block2.tStop)
        # Run 'End Routine' code from code_39
        # IMPORTANT: Only set block2_setup_complete if this routine actually ran (wasn't skipped)
        # Check if the routine was actually shown by checking the flag set in BeginRoutine
        routine_actually_ran = globals().get('crosshair2Block2_actually_ran', False)
        
        if 'text_crosshair2_block2' in locals():
            # Hide crosshair2 Block 2 text when routine ends
            text_crosshair2_block2.setAutoDraw(False)
            text_crosshair2_block2.opacity = 0
            print("Crosshair2 Block 2 text hidden")
        
        # Clear any remaining key presses
        try:
            event.clearEvents()
        except:
            pass
        
        # IMPORTANT: ONLY mark block 2 setup as complete if this routine actually ran
        # This prevents the flag from being set when the routine is skipped
        # Sequence: scannerSyncBlock2 → crosshairBlock2 → scannerWaitBlock2 → crosshair2Block2 (this routine)
        if routine_actually_ran:
            globals()['ready_for_block2_setup'] = False
            globals()['ready_for_scanner_sync_block2'] = False
            globals()['block2_setup_complete'] = True
            print("Block 2 setup complete - all scanner sync routines finished (scannerSyncBlock2 → crosshairBlock2 → scannerWaitBlock2 → crosshair2Block2), ready for Block 2 trials")
        else:
            print("DEBUG: crosshair2Block2EndRoutine called but routine was skipped - NOT setting block2_setup_complete")
        
        
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if crosshair2Block2.maxDurationReached:
            routineTimer.addTime(-crosshair2Block2.maxDuration)
        elif crosshair2Block2.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-10.000000)
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
        
    # completed 4.0 repeats of 'learningLoop'
    learningLoop.status = FINISHED
    
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
            theseKeys = key_resp_8.getKeys(keyList=['c', 'C'], ignoreKeys=["escape"], waitRelease=False)
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
