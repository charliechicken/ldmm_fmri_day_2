/******************** 
 * Decisionlab *
 ********************/


// store info about the experiment session:
let expName = 'DecisionLab';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '1',
    'day': '1',
    'Global clock format': 'None',
};
let PILOTING = util.getUrlParameters().has('__pilotToken');

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: false,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(WelcomeRoutineBegin());
flowScheduler.add(WelcomeRoutineEachFrame());
flowScheduler.add(WelcomeRoutineEnd());
flowScheduler.add(TaskStructureRoutineBegin());
flowScheduler.add(TaskStructureRoutineEachFrame());
flowScheduler.add(TaskStructureRoutineEnd());
flowScheduler.add(yourGoalRoutineBegin());
flowScheduler.add(yourGoalRoutineEachFrame());
flowScheduler.add(yourGoalRoutineEnd());
flowScheduler.add(keyInstructionsRoutineBegin());
flowScheduler.add(keyInstructionsRoutineEachFrame());
flowScheduler.add(keyInstructionsRoutineEnd());
flowScheduler.add(practiceIntroRoutineBegin());
flowScheduler.add(practiceIntroRoutineEachFrame());
flowScheduler.add(practiceIntroRoutineEnd());
const practiceTrialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(practiceTrialsLoopBegin(practiceTrialsLoopScheduler));
flowScheduler.add(practiceTrialsLoopScheduler);
flowScheduler.add(practiceTrialsLoopEnd);





flowScheduler.add(taskStartSoonRoutineBegin());
flowScheduler.add(taskStartSoonRoutineEachFrame());
flowScheduler.add(taskStartSoonRoutineEnd());
flowScheduler.add(scannerSyncRoutineBegin());
flowScheduler.add(scannerSyncRoutineEachFrame());
flowScheduler.add(scannerSyncRoutineEnd());
flowScheduler.add(crosshair3RoutineBegin());
flowScheduler.add(crosshair3RoutineEachFrame());
flowScheduler.add(crosshair3RoutineEnd());
flowScheduler.add(scannerWaitRoutineBegin());
flowScheduler.add(scannerWaitRoutineEachFrame());
flowScheduler.add(scannerWaitRoutineEnd());
flowScheduler.add(startTaskRoutineBegin());
flowScheduler.add(startTaskRoutineEachFrame());
flowScheduler.add(startTaskRoutineEnd());
const learningLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(learningLoopLoopBegin(learningLoopLoopScheduler));
flowScheduler.add(learningLoopLoopScheduler);
flowScheduler.add(learningLoopLoopEnd);












flowScheduler.add(decisionPhaseRoutineBegin());
flowScheduler.add(decisionPhaseRoutineEachFrame());
flowScheduler.add(decisionPhaseRoutineEnd());
flowScheduler.add(decisionInstructionsRoutineBegin());
flowScheduler.add(decisionInstructionsRoutineEachFrame());
flowScheduler.add(decisionInstructionsRoutineEnd());
flowScheduler.add(whichFruitRoutineBegin());
flowScheduler.add(whichFruitRoutineEachFrame());
flowScheduler.add(whichFruitRoutineEnd());
flowScheduler.add(practiceIntro2RoutineBegin());
flowScheduler.add(practiceIntro2RoutineEachFrame());
flowScheduler.add(practiceIntro2RoutineEnd());
const practiceDecisionLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(practiceDecisionLoopLoopBegin(practiceDecisionLoopLoopScheduler));
flowScheduler.add(practiceDecisionLoopLoopScheduler);
flowScheduler.add(practiceDecisionLoopLoopEnd);







flowScheduler.add(taskStartSoonBlock3RoutineBegin());
flowScheduler.add(taskStartSoonBlock3RoutineEachFrame());
flowScheduler.add(taskStartSoonBlock3RoutineEnd());
flowScheduler.add(scannerSyncBlock3RoutineBegin());
flowScheduler.add(scannerSyncBlock3RoutineEachFrame());
flowScheduler.add(scannerSyncBlock3RoutineEnd());
flowScheduler.add(crosshair3Block3RoutineBegin());
flowScheduler.add(crosshair3Block3RoutineEachFrame());
flowScheduler.add(crosshair3Block3RoutineEnd());
flowScheduler.add(scannerWaitBlock3RoutineBegin());
flowScheduler.add(scannerWaitBlock3RoutineEachFrame());
flowScheduler.add(scannerWaitBlock3RoutineEnd());
flowScheduler.add(startTaskBlock3RoutineBegin());
flowScheduler.add(startTaskBlock3RoutineEachFrame());
flowScheduler.add(startTaskBlock3RoutineEnd());
const decisionLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(decisionLoopLoopBegin(decisionLoopLoopScheduler));
flowScheduler.add(decisionLoopLoopScheduler);
flowScheduler.add(decisionLoopLoopEnd);








flowScheduler.add(thankYouRoutineBegin());
flowScheduler.add(thankYouRoutineEachFrame());
flowScheduler.add(thankYouRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'images/apple.png', 'path': 'images/apple.png'},
    {'name': 'images/banana.png', 'path': 'images/banana.png'},
    {'name': 'images/grapes.png', 'path': 'images/grapes.png'},
    {'name': 'images/kiwi.png', 'path': 'images/kiwi.png'},
    {'name': 'images/pear.png', 'path': 'images/pear.png'},
    {'name': 'images/strawberry.png', 'path': 'images/strawberry.png'},
    {'name': 'images/randomImage.jpg', 'path': 'images/randomImage.jpg'},
    {'name': 'images/blank.png', 'path': 'images/blank.png'},
    {'name': 'default.png', 'path': 'https://pavlovia.org/assets/default/default.png'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.INFO);

async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2025.1.1';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}

async function experimentInit() {
  // Initialize components for Routine "Welcome"
  WelcomeClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Welcome to the Prediction Game!\n\nYour goal in this game is to learn the number of points associated with different fruits.\n\nIn the next couple of slides, instructions for the task will be provided, followed by the task itself.\n\nAt the end of the task, you will be presented with several additional questions.\n\nPress 2 to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.2], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  apple = new visual.ImageStim({
    win : psychoJS.window,
    name : 'apple', units : undefined, 
    image : 'images/apple.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [(- 0.4), (- 0.2)], 
    draggable: false,
    size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  banana = new visual.ImageStim({
    win : psychoJS.window,
    name : 'banana', units : undefined, 
    image : 'images/banana.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [(- 0.24), (- 0.2)], 
    draggable: false,
    size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  grape = new visual.ImageStim({
    win : psychoJS.window,
    name : 'grape', units : undefined, 
    image : 'images/grapes.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [(- 0.08), (- 0.2)], 
    draggable: false,
    size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  kiwi = new visual.ImageStim({
    win : psychoJS.window,
    name : 'kiwi', units : undefined, 
    image : 'images/kiwi.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0.08, (- 0.2)], 
    draggable: false,
    size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  pear = new visual.ImageStim({
    win : psychoJS.window,
    name : 'pear', units : undefined, 
    image : 'images/pear.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0.24, (- 0.2)], 
    draggable: false,
    size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  strawberry = new visual.ImageStim({
    win : psychoJS.window,
    name : 'strawberry', units : undefined, 
    image : 'images/strawberry.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0.4, (- 0.2)], 
    draggable: false,
    size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -6.0 
  });
  key_resp_17 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "TaskStructure"
  TaskStructureClock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: "Task Structure\n\nIn this task, you'll see different fruits as you play.\n\nEach fruit can either give you points or take points away.\n\nYou'll earn points when the number is positive (+), and lose points when it's negative (-).",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.2], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_19 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_19',
    text: '+50',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.2), (- 0.2)], draggable: false, height: 0.15,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), 0.0039, (- 1.0)]),  opacity: undefined,
    depth: -1.0 
  });
  
  text_21 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_21',
    text: '-50',
    font: 'Arial',
    units: undefined, 
    pos: [0.2, (- 0.2)], draggable: false, height: 0.15,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([0.5294, (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp_16 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_28 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_28',
    text: 'Press 2 to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  // Initialize components for Routine "yourGoal"
  yourGoalClock = new util.Clock();
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: 'Your Goal\n\nRight after a fruit is shown, you will be asked to predict how many points it will provide this time.\n\nDo your best to be as accurate as you can.\n\nImmediately after your prediction, you will be shown how many points it actually provided this time.\n\nPress 2 to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], draggable: false, height: 0.035,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  slider_2 = new visual.Slider({
    win: psychoJS.window, name: 'slider_2',
    startValue: 0,
    size: [1, 0.075], pos: [0, (- 0.2)], ori: 0.0, units: psychoJS.window.units,
    labels: [(- 100), (- 80), (- 60), (- 40), (- 20), 0, 20, 40, 60, 80, 100], fontSize: 0.05, ticks: [(- 100), (- 80), (- 60), (- 40), (- 20), 0, 20, 40, 60, 80, 100],
    granularity: 5.0, style: ["SLIDER"],
    color: new util.Color('LightGray'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Noto Sans', bold: true, italic: false, depth: -1, 
    flip: false,
  });
  
  text_22 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_22',
    text: '"How many points do you expect to receive from this fruit?"',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.08)], draggable: false, height: 0.055,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp_18 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "keyInstructions"
  keyInstructionsClock = new util.Clock();
  text_20 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_20',
    text: 'Pressing "1" will shift the slider value leftwards by a value of 5. Pressing "3" will shift the slider value rightwards, also by a value of 5. \n\nPressing "2" will confirm your answer.\n\nPress 2 to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_19 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "practiceIntro"
  practiceIntroClock = new util.Clock();
  text_practice_intro = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_practice_intro',
    text: 'We will run a short practice test now. Press 2 to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_9 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "practiceTrial"
  practiceTrialClock = new util.Clock();
  image_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_4', units : undefined, 
    image : undefined, mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0.17], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  slider_3 = new visual.Slider({
    win: psychoJS.window, name: 'slider_3',
    startValue: 0,
    size: [1, 0.075], pos: [0, (- 0.2)], ori: 0.0, units: psychoJS.window.units,
    labels: [(- 100), (- 80), (- 60), (- 40), (- 20), 0, 20, 40, 60, 80, 100], fontSize: 0.05, ticks: [(- 100), (- 80), (- 60), (- 40), (- 20), 0, 20, 40, 60, 80, 100],
    granularity: 5.0, style: ["SLIDER"],
    color: new util.Color('LightGray'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Noto Sans', bold: true, italic: false, depth: -2, 
    flip: false,
  });
  
  // Initialize components for Routine "crosshair5"
  crosshair5Clock = new util.Clock();
  // Run 'Begin Experiment' code from code_40
  var _pj;
  function _pj_snippets(container) {
      function in_es6(left, right) {
          if (((right instanceof Array) || ((typeof right) === "string"))) {
              return (right.indexOf(left) > (- 1));
          } else {
              if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                  return right.has(left);
              } else {
                  return (left in right);
              }
          }
      }
      container["in_es6"] = in_es6;
      return container;
  }
  _pj = {};
  _pj_snippets(_pj);
  if (_pj.in_es6("crosshair", locals())) {
      crosshair.opacity = 1;
      crosshair.setAutoDraw(true);
  }
  
  text_27 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_27',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "actualPoints1"
  actualPoints1Clock = new util.Clock();
  text_actual_points = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_actual_points',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "crosshair3"
  crosshair3Clock = new util.Clock();
  text_23 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_23',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "taskStartSoon"
  taskStartSoonClock = new util.Clock();
  text_task_start_soon = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_task_start_soon',
    text: 'The task will start soon.\n\nPress 2 to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_10 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "scannerSync"
  scannerSyncClock = new util.Clock();
  text_scanner_wait = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_scanner_wait',
    text: 'Waiting for the scanner to start...',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_11 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "scannerWait"
  scannerWaitClock = new util.Clock();
  waitImage = new visual.ImageStim({
    win : psychoJS.window,
    name : 'waitImage', units : undefined, 
    image : 'images/randomImage.jpg', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [1, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "startTask"
  startTaskClock = new util.Clock();
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Run 'Begin Experiment' code from code
  /* Syntax Error: Fix Python code */
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  slider = new visual.Slider({
    win: psychoJS.window, name: 'slider',
    startValue: 0,
    size: [1, 0.075], pos: [0, (- 0.2)], ori: 0.0, units: psychoJS.window.units,
    labels: [(- 100), (- 80), (- 60), (- 40), (- 20), 0, 20, 40, 60, 80, 100], fontSize: 0.05, ticks: [(- 100), (- 80), (- 60), (- 40), (- 20), 0, 20, 40, 60, 80, 100],
    granularity: 5.0, style: ["SLIDER"],
    color: new util.Color('LightGray'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Noto Sans', bold: true, italic: false, depth: 0, 
    flip: false,
  });
  
  image_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_3', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0.2], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  // Run 'Begin Experiment' code from code_2
  trueValStr = "";
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_slider_value = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_slider_value',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.1)], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  // Initialize components for Routine "timeout"
  timeoutClock = new util.Clock();
  text_timeout = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_timeout',
    text: 'Time out',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "crosshair1"
  crosshair1Clock = new util.Clock();
  text_13 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_13',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "actualPoints"
  actualPointsClock = new util.Clock();
  image_30 = new visual.TextStim({
    win: psychoJS.window,
    name: 'image_30',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "crosshair2"
  crosshair2Clock = new util.Clock();
  text_14 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_14',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "blockTransition"
  blockTransitionClock = new util.Clock();
  text_block_transition = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_block_transition',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_transition = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "taskStartSoonBlock2"
  taskStartSoonBlock2Clock = new util.Clock();
  key_resp_14 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_24 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_24',
    text: 'The task will start soon.\n\nPress 2 to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  // Initialize components for Routine "scannerSyncBlock2"
  scannerSyncBlock2Clock = new util.Clock();
  text_scanner_wait_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_scanner_wait_2',
    text: 'Waiting for the scanner to start...',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_13 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "crosshairBlock2"
  crosshairBlock2Clock = new util.Clock();
  text_crosshair_block2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_crosshair_block2',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "scannerWaitBlock2"
  scannerWaitBlock2Clock = new util.Clock();
  image_scanner_wait_block2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_scanner_wait_block2', units : undefined, 
    image : 'images/randomImage.jpg', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [1, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "crosshair2Block2"
  crosshair2Block2Clock = new util.Clock();
  text_crosshair2_block2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_crosshair2_block2',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "decisionPhase"
  decisionPhaseClock = new util.Clock();
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: 'Learning Phase Completed!\n\nGreat job! You have completed the learning phase.\n\nPress 2 to continue with the decision tasks.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "decisionInstructions"
  decisionInstructionsClock = new util.Clock();
  text_8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_8',
    text: "\n\nYou have completed the learning phase and will now make decisions between pairs of fruits based on what you learned.\n\nPerformance Bonus Opportunity:\nMost people get 70% of their responses correctly.\nIf you'll be correct in more than 80% of your decisions, you will receive a bonus compensation.\n\nTry to recall the points associated with each fruit and make the best choices you can.\n\nClick 2 to continue.",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_9 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_9',
    text: 'Decision Task Instructions',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], draggable: false, height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "whichFruit"
  whichFruitClock = new util.Clock();
  text_10 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_10',
    text: 'Which fruit would you pick?\n\nIn this block, you will choose between pairs of fruits. Choose the fruit you think will give you more points.\n\nUse "1" to choose the fruit on the left side of the screen, and "3" to choose the fruit on the right side of the screen.\n\nClick 2 to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_6 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "practiceIntro2"
  practiceIntro2Clock = new util.Clock();
  key_resp_15 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "practiceDecisionSimulus1"
  practiceDecisionSimulus1Clock = new util.Clock();
  text_question1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_question1',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  image_left3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_left3', units : undefined, 
    image : undefined, mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [(- 0.4), 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  image_right3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_right3', units : undefined, 
    image : undefined, mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0.4, 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "crosshairPracticeDecision1"
  crosshairPracticeDecision1Clock = new util.Clock();
  // Initialize components for Routine "practiceDecisionSimulus2"
  practiceDecisionSimulus2Clock = new util.Clock();
  text_question_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_question_3',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  image_left1_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_left1_3', units : undefined, 
    image : undefined, mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [(- 0.4), 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  image_right2_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_right2_3', units : undefined, 
    image : undefined, mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0.4, 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  text_25 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_25',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "crosshairPracticeDecision2"
  crosshairPracticeDecision2Clock = new util.Clock();
  // Initialize components for Routine "practiceDecisionMaking"
  practiceDecisionMakingClock = new util.Clock();
  text_question_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_question_4',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  image_left_left1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_left_left1', units : undefined, 
    image : undefined, mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [(- 0.4), 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  image_right_right1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_right_right1', units : undefined, 
    image : undefined, mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0.4, 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "crosshairPracticeDecision3"
  crosshairPracticeDecision3Clock = new util.Clock();
  // Initialize components for Routine "taskStartSoonBlock3"
  taskStartSoonBlock3Clock = new util.Clock();
  text_task_start_soon_block3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_task_start_soon_block3',
    text: 'The task will start soon. Press 2 to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "scannerSyncBlock3"
  scannerSyncBlock3Clock = new util.Clock();
  text_scanner_wait_block3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_scanner_wait_block3',
    text: 'Waiting for the scanner to start...',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "crosshair3Block3"
  crosshair3Block3Clock = new util.Clock();
  text_crosshair3_block3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_crosshair3_block3',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "scannerWaitBlock3"
  scannerWaitBlock3Clock = new util.Clock();
  image_scanner_wait_block3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_scanner_wait_block3', units : undefined, 
    image : 'images/randomImage.jpg', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [1, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "startTaskBlock3"
  startTaskBlock3Clock = new util.Clock();
  text_26 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_26',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "decisionStimulus1"
  decisionStimulus1Clock = new util.Clock();
  text_question = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_question',
    text: 'Any text\n\nincluding line breaks',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  image_left1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_left1', units : undefined, 
    image : undefined, mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [(- 0.4), 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  image_right2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_right2', units : undefined, 
    image : undefined, mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0.4, 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "decisionITI1"
  decisionITI1Clock = new util.Clock();
  text_15 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_15',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "decisionStimulus2"
  decisionStimulus2Clock = new util.Clock();
  text_question_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_question_2',
    text: 'Any text\n\nincluding line breaks',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  image_left1_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_left1_2', units : undefined, 
    image : undefined, mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [(- 0.4), 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  image_right2_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_right2_2', units : undefined, 
    image : undefined, mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0.4, 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "decisionITI2"
  decisionITI2Clock = new util.Clock();
  text_16 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_16',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "decisionMaking"
  decisionMakingClock = new util.Clock();
  text_question_1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_question_1',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  image_left_left = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_left_left', units : undefined, 
    image : undefined, mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [(- 0.4), 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  image_right_right = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_right_right', units : undefined, 
    image : undefined, mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0.4, 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  mouse_2 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_2.mouseClock = new util.Clock();
  // Initialize components for Routine "decisionTimeout"
  decisionTimeoutClock = new util.Clock();
  text_decision_timeout = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_decision_timeout',
    text: 'Time out',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "decisionITI3"
  decisionITI3Clock = new util.Clock();
  text_17 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_17',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "thankYou"
  thankYouClock = new util.Clock();
  text_11 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_11',
    text: 'You completed the experiment!\n\nThank you for participating!\n\nPress 2 to end.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_8 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

function WelcomeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Welcome' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    WelcomeClock.reset();
    routineTimer.reset();
    WelcomeMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_17.keys = undefined;
    key_resp_17.rt = undefined;
    _key_resp_17_allKeys = [];
    psychoJS.experiment.addData('Welcome.started', globalClock.getTime());
    WelcomeMaxDuration = null
    // keep track of which components have finished
    WelcomeComponents = [];
    WelcomeComponents.push(text);
    WelcomeComponents.push(apple);
    WelcomeComponents.push(banana);
    WelcomeComponents.push(grape);
    WelcomeComponents.push(kiwi);
    WelcomeComponents.push(pear);
    WelcomeComponents.push(strawberry);
    WelcomeComponents.push(key_resp_17);
    
    WelcomeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function WelcomeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Welcome' ---
    // get current time
    t = WelcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }
    
    
    // if text is active this frame...
    if (text.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *apple* updates
    if (t >= 0.0 && apple.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      apple.tStart = t;  // (not accounting for frame time here)
      apple.frameNStart = frameN;  // exact frame index
      
      apple.setAutoDraw(true);
    }
    
    
    // if apple is active this frame...
    if (apple.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *banana* updates
    if (t >= 0.0 && banana.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      banana.tStart = t;  // (not accounting for frame time here)
      banana.frameNStart = frameN;  // exact frame index
      
      banana.setAutoDraw(true);
    }
    
    
    // if banana is active this frame...
    if (banana.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *grape* updates
    if (t >= 0.0 && grape.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      grape.tStart = t;  // (not accounting for frame time here)
      grape.frameNStart = frameN;  // exact frame index
      
      grape.setAutoDraw(true);
    }
    
    
    // if grape is active this frame...
    if (grape.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *kiwi* updates
    if (t >= 0.0 && kiwi.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      kiwi.tStart = t;  // (not accounting for frame time here)
      kiwi.frameNStart = frameN;  // exact frame index
      
      kiwi.setAutoDraw(true);
    }
    
    
    // if kiwi is active this frame...
    if (kiwi.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *pear* updates
    if (t >= 0.0 && pear.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pear.tStart = t;  // (not accounting for frame time here)
      pear.frameNStart = frameN;  // exact frame index
      
      pear.setAutoDraw(true);
    }
    
    
    // if pear is active this frame...
    if (pear.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *strawberry* updates
    if (t >= 0.0 && strawberry.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      strawberry.tStart = t;  // (not accounting for frame time here)
      strawberry.frameNStart = frameN;  // exact frame index
      
      strawberry.setAutoDraw(true);
    }
    
    
    // if strawberry is active this frame...
    if (strawberry.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_resp_17* updates
    if (t >= 0.0 && key_resp_17.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_17.tStart = t;  // (not accounting for frame time here)
      key_resp_17.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_17.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_17.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_17.clearEvents(); });
    }
    
    // if key_resp_17 is active this frame...
    if (key_resp_17.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_17.getKeys({keyList: ['2','num_2'], waitRelease: false});
      _key_resp_17_allKeys = _key_resp_17_allKeys.concat(theseKeys);
      if (_key_resp_17_allKeys.length > 0) {
        key_resp_17.keys = _key_resp_17_allKeys[_key_resp_17_allKeys.length - 1].name;  // just the last key pressed
        key_resp_17.rt = _key_resp_17_allKeys[_key_resp_17_allKeys.length - 1].rt;
        key_resp_17.duration = _key_resp_17_allKeys[_key_resp_17_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    WelcomeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function WelcomeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Welcome' ---
    WelcomeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Welcome.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_17.corr, level);
    }
    psychoJS.experiment.addData('key_resp_17.keys', key_resp_17.keys);
    if (typeof key_resp_17.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_17.rt', key_resp_17.rt);
        psychoJS.experiment.addData('key_resp_17.duration', key_resp_17.duration);
        routineTimer.reset();
        }
    
    key_resp_17.stop();
    // the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function TaskStructureRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'TaskStructure' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    TaskStructureClock.reset();
    routineTimer.reset();
    TaskStructureMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_16.keys = undefined;
    key_resp_16.rt = undefined;
    _key_resp_16_allKeys = [];
    psychoJS.experiment.addData('TaskStructure.started', globalClock.getTime());
    TaskStructureMaxDuration = null
    // keep track of which components have finished
    TaskStructureComponents = [];
    TaskStructureComponents.push(text_2);
    TaskStructureComponents.push(text_19);
    TaskStructureComponents.push(text_21);
    TaskStructureComponents.push(key_resp_16);
    TaskStructureComponents.push(text_28);
    
    TaskStructureComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function TaskStructureRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'TaskStructure' ---
    // get current time
    t = TaskStructureClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }
    
    
    // if text_2 is active this frame...
    if (text_2.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *text_19* updates
    if (t >= 0.0 && text_19.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_19.tStart = t;  // (not accounting for frame time here)
      text_19.frameNStart = frameN;  // exact frame index
      
      text_19.setAutoDraw(true);
    }
    
    
    // if text_19 is active this frame...
    if (text_19.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *text_21* updates
    if (t >= 0.0 && text_21.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_21.tStart = t;  // (not accounting for frame time here)
      text_21.frameNStart = frameN;  // exact frame index
      
      text_21.setAutoDraw(true);
    }
    
    
    // if text_21 is active this frame...
    if (text_21.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_resp_16* updates
    if (t >= 0.0 && key_resp_16.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_16.tStart = t;  // (not accounting for frame time here)
      key_resp_16.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_16.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_16.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_16.clearEvents(); });
    }
    
    // if key_resp_16 is active this frame...
    if (key_resp_16.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_16.getKeys({keyList: ['2','num_2'], waitRelease: false});
      _key_resp_16_allKeys = _key_resp_16_allKeys.concat(theseKeys);
      if (_key_resp_16_allKeys.length > 0) {
        key_resp_16.keys = _key_resp_16_allKeys[_key_resp_16_allKeys.length - 1].name;  // just the last key pressed
        key_resp_16.rt = _key_resp_16_allKeys[_key_resp_16_allKeys.length - 1].rt;
        key_resp_16.duration = _key_resp_16_allKeys[_key_resp_16_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_28* updates
    if (t >= 0.0 && text_28.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_28.tStart = t;  // (not accounting for frame time here)
      text_28.frameNStart = frameN;  // exact frame index
      
      text_28.setAutoDraw(true);
    }
    
    
    // if text_28 is active this frame...
    if (text_28.status === PsychoJS.Status.STARTED) {
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    TaskStructureComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function TaskStructureRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'TaskStructure' ---
    TaskStructureComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('TaskStructure.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_16.corr, level);
    }
    psychoJS.experiment.addData('key_resp_16.keys', key_resp_16.keys);
    if (typeof key_resp_16.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_16.rt', key_resp_16.rt);
        psychoJS.experiment.addData('key_resp_16.duration', key_resp_16.duration);
        routineTimer.reset();
        }
    
    key_resp_16.stop();
    // the Routine "TaskStructure" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function yourGoalRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'yourGoal' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    yourGoalClock.reset();
    routineTimer.reset();
    yourGoalMaxDurationReached = false;
    // update component parameters for each repeat
    slider_2.reset()
    key_resp_18.keys = undefined;
    key_resp_18.rt = undefined;
    _key_resp_18_allKeys = [];
    psychoJS.experiment.addData('yourGoal.started', globalClock.getTime());
    yourGoalMaxDuration = null
    // keep track of which components have finished
    yourGoalComponents = [];
    yourGoalComponents.push(text_3);
    yourGoalComponents.push(slider_2);
    yourGoalComponents.push(text_22);
    yourGoalComponents.push(key_resp_18);
    
    yourGoalComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function yourGoalRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'yourGoal' ---
    // get current time
    t = yourGoalClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_3* updates
    if (t >= 0.0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_3.tStart = t;  // (not accounting for frame time here)
      text_3.frameNStart = frameN;  // exact frame index
      
      text_3.setAutoDraw(true);
    }
    
    
    // if text_3 is active this frame...
    if (text_3.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *slider_2* updates
    if (t >= 0 && slider_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider_2.tStart = t;  // (not accounting for frame time here)
      slider_2.frameNStart = frameN;  // exact frame index
      
      slider_2.setAutoDraw(true);
    }
    
    
    // if slider_2 is active this frame...
    if (slider_2.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *text_22* updates
    if (t >= 0.0 && text_22.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_22.tStart = t;  // (not accounting for frame time here)
      text_22.frameNStart = frameN;  // exact frame index
      
      text_22.setAutoDraw(true);
    }
    
    
    // if text_22 is active this frame...
    if (text_22.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_resp_18* updates
    if (t >= 0.0 && key_resp_18.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_18.tStart = t;  // (not accounting for frame time here)
      key_resp_18.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_18.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_18.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_18.clearEvents(); });
    }
    
    // if key_resp_18 is active this frame...
    if (key_resp_18.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_18.getKeys({keyList: ['2','num_2'], waitRelease: false});
      _key_resp_18_allKeys = _key_resp_18_allKeys.concat(theseKeys);
      if (_key_resp_18_allKeys.length > 0) {
        key_resp_18.keys = _key_resp_18_allKeys[_key_resp_18_allKeys.length - 1].name;  // just the last key pressed
        key_resp_18.rt = _key_resp_18_allKeys[_key_resp_18_allKeys.length - 1].rt;
        key_resp_18.duration = _key_resp_18_allKeys[_key_resp_18_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    yourGoalComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function yourGoalRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'yourGoal' ---
    yourGoalComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('yourGoal.stopped', globalClock.getTime());
    psychoJS.experiment.addData('slider_2.response', slider_2.getRating());
    psychoJS.experiment.addData('slider_2.rt', slider_2.getRT());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_18.corr, level);
    }
    psychoJS.experiment.addData('key_resp_18.keys', key_resp_18.keys);
    if (typeof key_resp_18.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_18.rt', key_resp_18.rt);
        psychoJS.experiment.addData('key_resp_18.duration', key_resp_18.duration);
        routineTimer.reset();
        }
    
    key_resp_18.stop();
    // the Routine "yourGoal" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function keyInstructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'keyInstructions' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    keyInstructionsClock.reset();
    routineTimer.reset();
    keyInstructionsMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_19.keys = undefined;
    key_resp_19.rt = undefined;
    _key_resp_19_allKeys = [];
    psychoJS.experiment.addData('keyInstructions.started', globalClock.getTime());
    keyInstructionsMaxDuration = null
    // keep track of which components have finished
    keyInstructionsComponents = [];
    keyInstructionsComponents.push(text_20);
    keyInstructionsComponents.push(key_resp_19);
    
    keyInstructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function keyInstructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'keyInstructions' ---
    // get current time
    t = keyInstructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_20* updates
    if (t >= 0.0 && text_20.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_20.tStart = t;  // (not accounting for frame time here)
      text_20.frameNStart = frameN;  // exact frame index
      
      text_20.setAutoDraw(true);
    }
    
    
    // if text_20 is active this frame...
    if (text_20.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_resp_19* updates
    if (t >= 0.0 && key_resp_19.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_19.tStart = t;  // (not accounting for frame time here)
      key_resp_19.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_19.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_19.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_19.clearEvents(); });
    }
    
    // if key_resp_19 is active this frame...
    if (key_resp_19.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_19.getKeys({keyList: ['2','num_2'], waitRelease: false});
      _key_resp_19_allKeys = _key_resp_19_allKeys.concat(theseKeys);
      if (_key_resp_19_allKeys.length > 0) {
        key_resp_19.keys = _key_resp_19_allKeys[_key_resp_19_allKeys.length - 1].name;  // just the last key pressed
        key_resp_19.rt = _key_resp_19_allKeys[_key_resp_19_allKeys.length - 1].rt;
        key_resp_19.duration = _key_resp_19_allKeys[_key_resp_19_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    keyInstructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function keyInstructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'keyInstructions' ---
    keyInstructionsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('keyInstructions.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_19.corr, level);
    }
    psychoJS.experiment.addData('key_resp_19.keys', key_resp_19.keys);
    if (typeof key_resp_19.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_19.rt', key_resp_19.rt);
        psychoJS.experiment.addData('key_resp_19.duration', key_resp_19.duration);
        routineTimer.reset();
        }
    
    key_resp_19.stop();
    // the Routine "keyInstructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function practiceIntroRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practiceIntro' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    practiceIntroClock.reset();
    routineTimer.reset();
    practiceIntroMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_18
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    try {
        psychoJS.eventManager.clearEvents();
    } catch(e) {
    }
    if (_pj.in_es6("text_practice_intro", locals())) {
        text_practice_intro.text = "We will run a short practice task now. Press 2 to continue";
        text_practice_intro.opacity = 1;
        text_practice_intro.setAutoDraw(true);
        console.log("Practice introduction screen displayed");
    } else {
        console.log("WARNING: text_practice_intro component not found!");
    }
    
    key_resp_9.keys = undefined;
    key_resp_9.rt = undefined;
    _key_resp_9_allKeys = [];
    psychoJS.experiment.addData('practiceIntro.started', globalClock.getTime());
    practiceIntroMaxDuration = null
    // keep track of which components have finished
    practiceIntroComponents = [];
    practiceIntroComponents.push(text_practice_intro);
    practiceIntroComponents.push(key_resp_9);
    
    practiceIntroComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function practiceIntroRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practiceIntro' ---
    // get current time
    t = practiceIntroClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_practice_intro* updates
    if (t >= 0.0 && text_practice_intro.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_practice_intro.tStart = t;  // (not accounting for frame time here)
      text_practice_intro.frameNStart = frameN;  // exact frame index
      
      text_practice_intro.setAutoDraw(true);
    }
    
    
    // if text_practice_intro is active this frame...
    if (text_practice_intro.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_resp_9* updates
    if (t >= 0.0 && key_resp_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_9.tStart = t;  // (not accounting for frame time here)
      key_resp_9.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_9.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_9.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_9.clearEvents(); });
    }
    
    // if key_resp_9 is active this frame...
    if (key_resp_9.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_9.getKeys({keyList: ['2','num_2'], waitRelease: false});
      _key_resp_9_allKeys = _key_resp_9_allKeys.concat(theseKeys);
      if (_key_resp_9_allKeys.length > 0) {
        key_resp_9.keys = _key_resp_9_allKeys[_key_resp_9_allKeys.length - 1].name;  // just the last key pressed
        key_resp_9.rt = _key_resp_9_allKeys[_key_resp_9_allKeys.length - 1].rt;
        key_resp_9.duration = _key_resp_9_allKeys[_key_resp_9_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    practiceIntroComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function practiceIntroRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practiceIntro' ---
    practiceIntroComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('practiceIntro.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_9.corr, level);
    }
    psychoJS.experiment.addData('key_resp_9.keys', key_resp_9.keys);
    if (typeof key_resp_9.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_9.rt', key_resp_9.rt);
        psychoJS.experiment.addData('key_resp_9.duration', key_resp_9.duration);
        routineTimer.reset();
        }
    
    key_resp_9.stop();
    // the Routine "practiceIntro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function practiceTrialsLoopBegin(practiceTrialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    practiceTrials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 3, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'practiceTrials'
    });
    psychoJS.experiment.addLoop(practiceTrials); // add the loop to the experiment
    currentLoop = practiceTrials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    practiceTrials.forEach(function() {
      snapshot = practiceTrials.getSnapshot();
    
      practiceTrialsLoopScheduler.add(importConditions(snapshot));
      practiceTrialsLoopScheduler.add(practiceTrialRoutineBegin(snapshot));
      practiceTrialsLoopScheduler.add(practiceTrialRoutineEachFrame());
      practiceTrialsLoopScheduler.add(practiceTrialRoutineEnd(snapshot));
      practiceTrialsLoopScheduler.add(crosshair5RoutineBegin(snapshot));
      practiceTrialsLoopScheduler.add(crosshair5RoutineEachFrame());
      practiceTrialsLoopScheduler.add(crosshair5RoutineEnd(snapshot));
      practiceTrialsLoopScheduler.add(actualPoints1RoutineBegin(snapshot));
      practiceTrialsLoopScheduler.add(actualPoints1RoutineEachFrame());
      practiceTrialsLoopScheduler.add(actualPoints1RoutineEnd(snapshot));
      practiceTrialsLoopScheduler.add(crosshair3RoutineBegin(snapshot));
      practiceTrialsLoopScheduler.add(crosshair3RoutineEachFrame());
      practiceTrialsLoopScheduler.add(crosshair3RoutineEnd(snapshot));
      practiceTrialsLoopScheduler.add(practiceTrialsLoopEndIteration(practiceTrialsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}

async function practiceTrialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(practiceTrials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function practiceTrialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function learningLoopLoopBegin(learningLoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    learningLoop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 6, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'learningLoop'
    });
    psychoJS.experiment.addLoop(learningLoop); // add the loop to the experiment
    currentLoop = learningLoop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    learningLoop.forEach(function() {
      snapshot = learningLoop.getSnapshot();
    
      learningLoopLoopScheduler.add(importConditions(snapshot));
      learningLoopLoopScheduler.add(trialRoutineBegin(snapshot));
      learningLoopLoopScheduler.add(trialRoutineEachFrame());
      learningLoopLoopScheduler.add(trialRoutineEnd(snapshot));
      learningLoopLoopScheduler.add(timeoutRoutineBegin(snapshot));
      learningLoopLoopScheduler.add(timeoutRoutineEachFrame());
      learningLoopLoopScheduler.add(timeoutRoutineEnd(snapshot));
      learningLoopLoopScheduler.add(crosshair1RoutineBegin(snapshot));
      learningLoopLoopScheduler.add(crosshair1RoutineEachFrame());
      learningLoopLoopScheduler.add(crosshair1RoutineEnd(snapshot));
      learningLoopLoopScheduler.add(actualPointsRoutineBegin(snapshot));
      learningLoopLoopScheduler.add(actualPointsRoutineEachFrame());
      learningLoopLoopScheduler.add(actualPointsRoutineEnd(snapshot));
      learningLoopLoopScheduler.add(crosshair2RoutineBegin(snapshot));
      learningLoopLoopScheduler.add(crosshair2RoutineEachFrame());
      learningLoopLoopScheduler.add(crosshair2RoutineEnd(snapshot));
      learningLoopLoopScheduler.add(blockTransitionRoutineBegin(snapshot));
      learningLoopLoopScheduler.add(blockTransitionRoutineEachFrame());
      learningLoopLoopScheduler.add(blockTransitionRoutineEnd(snapshot));
      learningLoopLoopScheduler.add(taskStartSoonBlock2RoutineBegin(snapshot));
      learningLoopLoopScheduler.add(taskStartSoonBlock2RoutineEachFrame());
      learningLoopLoopScheduler.add(taskStartSoonBlock2RoutineEnd(snapshot));
      learningLoopLoopScheduler.add(scannerSyncBlock2RoutineBegin(snapshot));
      learningLoopLoopScheduler.add(scannerSyncBlock2RoutineEachFrame());
      learningLoopLoopScheduler.add(scannerSyncBlock2RoutineEnd(snapshot));
      learningLoopLoopScheduler.add(crosshairBlock2RoutineBegin(snapshot));
      learningLoopLoopScheduler.add(crosshairBlock2RoutineEachFrame());
      learningLoopLoopScheduler.add(crosshairBlock2RoutineEnd(snapshot));
      learningLoopLoopScheduler.add(scannerWaitBlock2RoutineBegin(snapshot));
      learningLoopLoopScheduler.add(scannerWaitBlock2RoutineEachFrame());
      learningLoopLoopScheduler.add(scannerWaitBlock2RoutineEnd(snapshot));
      learningLoopLoopScheduler.add(crosshair2Block2RoutineBegin(snapshot));
      learningLoopLoopScheduler.add(crosshair2Block2RoutineEachFrame());
      learningLoopLoopScheduler.add(crosshair2Block2RoutineEnd(snapshot));
      learningLoopLoopScheduler.add(learningLoopLoopEndIteration(learningLoopLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}

async function learningLoopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(learningLoop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function learningLoopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function practiceDecisionLoopLoopBegin(practiceDecisionLoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    practiceDecisionLoop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 3, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'practiceDecisionLoop'
    });
    psychoJS.experiment.addLoop(practiceDecisionLoop); // add the loop to the experiment
    currentLoop = practiceDecisionLoop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    practiceDecisionLoop.forEach(function() {
      snapshot = practiceDecisionLoop.getSnapshot();
    
      practiceDecisionLoopLoopScheduler.add(importConditions(snapshot));
      practiceDecisionLoopLoopScheduler.add(practiceDecisionSimulus1RoutineBegin(snapshot));
      practiceDecisionLoopLoopScheduler.add(practiceDecisionSimulus1RoutineEachFrame());
      practiceDecisionLoopLoopScheduler.add(practiceDecisionSimulus1RoutineEnd(snapshot));
      practiceDecisionLoopLoopScheduler.add(crosshairPracticeDecision1RoutineBegin(snapshot));
      practiceDecisionLoopLoopScheduler.add(crosshairPracticeDecision1RoutineEachFrame());
      practiceDecisionLoopLoopScheduler.add(crosshairPracticeDecision1RoutineEnd(snapshot));
      practiceDecisionLoopLoopScheduler.add(practiceDecisionSimulus2RoutineBegin(snapshot));
      practiceDecisionLoopLoopScheduler.add(practiceDecisionSimulus2RoutineEachFrame());
      practiceDecisionLoopLoopScheduler.add(practiceDecisionSimulus2RoutineEnd(snapshot));
      practiceDecisionLoopLoopScheduler.add(crosshairPracticeDecision2RoutineBegin(snapshot));
      practiceDecisionLoopLoopScheduler.add(crosshairPracticeDecision2RoutineEachFrame());
      practiceDecisionLoopLoopScheduler.add(crosshairPracticeDecision2RoutineEnd(snapshot));
      practiceDecisionLoopLoopScheduler.add(practiceDecisionMakingRoutineBegin(snapshot));
      practiceDecisionLoopLoopScheduler.add(practiceDecisionMakingRoutineEachFrame());
      practiceDecisionLoopLoopScheduler.add(practiceDecisionMakingRoutineEnd(snapshot));
      practiceDecisionLoopLoopScheduler.add(crosshairPracticeDecision3RoutineBegin(snapshot));
      practiceDecisionLoopLoopScheduler.add(crosshairPracticeDecision3RoutineEachFrame());
      practiceDecisionLoopLoopScheduler.add(crosshairPracticeDecision3RoutineEnd(snapshot));
      practiceDecisionLoopLoopScheduler.add(practiceDecisionLoopLoopEndIteration(practiceDecisionLoopLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}

async function practiceDecisionLoopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(practiceDecisionLoop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function practiceDecisionLoopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function decisionLoopLoopBegin(decisionLoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    decisionLoop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 4, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'decisionLoop'
    });
    psychoJS.experiment.addLoop(decisionLoop); // add the loop to the experiment
    currentLoop = decisionLoop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    decisionLoop.forEach(function() {
      snapshot = decisionLoop.getSnapshot();
    
      decisionLoopLoopScheduler.add(importConditions(snapshot));
      decisionLoopLoopScheduler.add(decisionStimulus1RoutineBegin(snapshot));
      decisionLoopLoopScheduler.add(decisionStimulus1RoutineEachFrame());
      decisionLoopLoopScheduler.add(decisionStimulus1RoutineEnd(snapshot));
      decisionLoopLoopScheduler.add(decisionITI1RoutineBegin(snapshot));
      decisionLoopLoopScheduler.add(decisionITI1RoutineEachFrame());
      decisionLoopLoopScheduler.add(decisionITI1RoutineEnd(snapshot));
      decisionLoopLoopScheduler.add(decisionStimulus2RoutineBegin(snapshot));
      decisionLoopLoopScheduler.add(decisionStimulus2RoutineEachFrame());
      decisionLoopLoopScheduler.add(decisionStimulus2RoutineEnd(snapshot));
      decisionLoopLoopScheduler.add(decisionITI2RoutineBegin(snapshot));
      decisionLoopLoopScheduler.add(decisionITI2RoutineEachFrame());
      decisionLoopLoopScheduler.add(decisionITI2RoutineEnd(snapshot));
      decisionLoopLoopScheduler.add(decisionMakingRoutineBegin(snapshot));
      decisionLoopLoopScheduler.add(decisionMakingRoutineEachFrame());
      decisionLoopLoopScheduler.add(decisionMakingRoutineEnd(snapshot));
      decisionLoopLoopScheduler.add(decisionTimeoutRoutineBegin(snapshot));
      decisionLoopLoopScheduler.add(decisionTimeoutRoutineEachFrame());
      decisionLoopLoopScheduler.add(decisionTimeoutRoutineEnd(snapshot));
      decisionLoopLoopScheduler.add(decisionITI3RoutineBegin(snapshot));
      decisionLoopLoopScheduler.add(decisionITI3RoutineEachFrame());
      decisionLoopLoopScheduler.add(decisionITI3RoutineEnd(snapshot));
      decisionLoopLoopScheduler.add(decisionLoopLoopEndIteration(decisionLoopLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}

async function decisionLoopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(decisionLoop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function decisionLoopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function practiceTrialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practiceTrial' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    practiceTrialClock.reset();
    routineTimer.reset();
    practiceTrialMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_19
    import * as time from 'time';
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    practice_block_index = globals().get("practice_block_index", (- 1));
    practice_block_index += 1;
    globals()["practice_block_index"] = practice_block_index;
    practice_block = globals().get("practice_block", []);
    if (((practice_block_index >= 0) && (practice_block_index < practice_block.length))) {
        current = practice_block[practice_block_index];
        fruitFile = current["fruit"];
        trueVal = current["true_value"];
        baselineR = current["baseline"];
        blockType = current["block"];
        idx = (practice_block_index + 1);
        console.log(`Practice trial ${idx}/3: ${fruitFile}, value=${trueVal}`);
    } else {
        fruitFile = "images/blank.png";
        trueVal = 0;
        baselineR = 0;
        blockType = "practice";
        idx = 0;
        console.log(`WARNING: Practice trial ${practice_block_index} out of range`);
    }
    try {
        psychoJS.eventManager.clearEvents();
    } catch(e) {
    }
    if (_pj.in_es6("image_3", locals())) {
        image_3.opacity = 0;
        image_3.setImage("images/blank.png");
        image_3.setImage(fruitFile);
        image_3.opacity = 1;
        console.log(`Practice trial: Set image to ${fruitFile}`);
    }
    if (_pj.in_es6("slider", locals())) {
        slider.reset();
        slider.setRating(0);
        console.log("Practice trial: Slider reset to 0");
    }
    trial_start_time = time.time();
    response_time = null;
    trial_timed_out = false;
    responded_in_time = false;
    globals()["trial_start_time"] = trial_start_time;
    globals()["response_time"] = null;
    globals()["trial_timed_out"] = false;
    globals()["responded_in_time"] = false;
    globals()["PRACTICE_TIMEOUT_SECONDS"] = 6.0;
    
    slider_3.reset()
    psychoJS.experiment.addData('practiceTrial.started', globalClock.getTime());
    practiceTrialMaxDuration = null
    // keep track of which components have finished
    practiceTrialComponents = [];
    practiceTrialComponents.push(image_4);
    practiceTrialComponents.push(slider_3);
    
    practiceTrialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function practiceTrialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practiceTrial' ---
    // get current time
    t = practiceTrialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from code_19
    import * as time from 'time';
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    if (((_pj.in_es6("image_3", locals()) && fruitFile) && (fruitFile !== "images/blank.png"))) {
        image_3.setImage(fruitFile);
        image_3.opacity = 1.0;
        image_3.setAutoDraw(true);
    }
    if (_pj.in_es6("slider", locals())) {
        current_value = slider.getRating();
        if (_pj.in_es6("text_slider_value", locals())) {
            text_slider_value.text = `Current rating: ${Number.parseInt(current_value)}`;
        } else {
            if (_pj.in_es6("text_rating", locals())) {
                text_rating.text = `Current rating: ${Number.parseInt(current_value)}`;
            }
        }
    }
    try {
        keys = psychoJS.eventManager.getKeys({"keyList": ["1", "2", "3", "num_1", "num_2", "num_3"]});
    } catch(e) {
        keys = [];
    }
    for (var key, _pj_c = 0, _pj_a = keys, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        key = _pj_a[_pj_c];
        if (((key === "num_1") || (key === "1"))) {
            if (_pj.in_es6("slider", locals())) {
                current_rating = slider.getRating();
                new_rating = (current_rating - 5);
                slider.setRating(new_rating);
                console.log(`Practice: Slider moved left (key 1): ${current_rating} -> ${new_rating}`);
            }
        } else {
            if (((key === "num_3") || (key === "3"))) {
                if (_pj.in_es6("slider", locals())) {
                    current_rating = slider.getRating();
                    new_rating = (current_rating + 5);
                    slider.setRating(new_rating);
                    console.log(`Practice: Slider moved right (key 3): ${current_rating} -> ${new_rating}`);
                }
            } else {
                if (((key === "num_2") || (key === "2"))) {
                    trial_start_time = globals().get("trial_start_time", time.time());
                    response_time = (time.time() - trial_start_time);
                    PRACTICE_TIMEOUT_SECONDS = globals().get("PRACTICE_TIMEOUT_SECONDS", 6.0);
                    if ((response_time <= PRACTICE_TIMEOUT_SECONDS)) {
                        responded_in_time = true;
                        trial_timed_out = false;
                        console.log(`Practice: Answer submitted (key 2) in ${util.pad(Number.parseFloat(response_time).toFixed(2), 1)} seconds`);
                    } else {
                        responded_in_time = false;
                        trial_timed_out = true;
                        console.log(`Practice: Answer submitted (key 2) in ${util.pad(Number.parseFloat(response_time).toFixed(2), 1)} seconds (over limit)`);
                    }
                    globals()["response_time"] = response_time;
                    globals()["responded_in_time"] = responded_in_time;
                    globals()["trial_timed_out"] = trial_timed_out;
                    continueRoutine = false;
                    psychoJS.eventManager.clearEvents();
                    break;
                }
            }
        }
    }
    try {
        trial_start_time = globals().get("trial_start_time", time.time());
        PRACTICE_TIMEOUT_SECONDS = globals().get("PRACTICE_TIMEOUT_SECONDS", 6.0);
        responded_in_time = globals().get("responded_in_time", false);
        elapsed_time = (time.time() - trial_start_time);
        if (((elapsed_time >= PRACTICE_TIMEOUT_SECONDS) && (! responded_in_time))) {
            trial_timed_out = true;
            response_time = PRACTICE_TIMEOUT_SECONDS;
            responded_in_time = false;
            globals()["response_time"] = response_time;
            globals()["responded_in_time"] = responded_in_time;
            globals()["trial_timed_out"] = trial_timed_out;
            console.log(`Practice: Trial timed out at ${PRACTICE_TIMEOUT_SECONDS} seconds`);
            continueRoutine = false;
            psychoJS.eventManager.clearEvents();
        }
    } catch(e) {
    }
    
    
    // *image_4* updates
    if (t >= 0.0 && image_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_4.tStart = t;  // (not accounting for frame time here)
      image_4.frameNStart = frameN;  // exact frame index
      
      image_4.setAutoDraw(true);
    }
    
    
    // if image_4 is active this frame...
    if (image_4.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *slider_3* updates
    if (t >= 0 && slider_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider_3.tStart = t;  // (not accounting for frame time here)
      slider_3.frameNStart = frameN;  // exact frame index
      
      slider_3.setAutoDraw(true);
    }
    
    
    // if slider_3 is active this frame...
    if (slider_3.status === PsychoJS.Status.STARTED) {
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    practiceTrialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function practiceTrialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practiceTrial' ---
    practiceTrialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('practiceTrial.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_19
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    rating = (_pj.in_es6("slider", locals()) ? slider.getRating() : 0);
    rt = (_pj.in_es6("slider", locals()) ? slider.getRT() : null);
    response_time = globals().get("response_time", null);
    responded_in_time = globals().get("responded_in_time", false);
    trial_timed_out = globals().get("trial_timed_out", false);
    actual_response_time = ((response_time !== null) ? response_time : rt);
    rt_str = (actual_response_time ? `${util.pad(Number.parseFloat(actual_response_time).toFixed(3), 1)}s` : "N/A");
    console.log(`Practice trial EndRoutine: RT=${rt_str}, responded_in_time=${responded_in_time}, timed_out=${trial_timed_out}`);
    psychoJS.experiment.addData("practice_trial", true);
    psychoJS.experiment.addData("practice_block", (_pj.in_es6("blockType", locals()) ? blockType : "practice"));
    psychoJS.experiment.addData("practice_fruit", (_pj.in_es6("fruitFile", locals()) ? fruitFile : ""));
    psychoJS.experiment.addData("practice_rating", rating);
    psychoJS.experiment.addData("practice_rt", (actual_response_time ? actual_response_time : null));
    psychoJS.experiment.addData("practice_true_value", (_pj.in_es6("trueVal", locals()) ? trueVal : 0));
    psychoJS.experiment.addData("practice_responded_in_time", responded_in_time);
    psychoJS.experiment.addData("practice_timed_out", trial_timed_out);
    
    psychoJS.experiment.addData('slider_3.response', slider_3.getRating());
    psychoJS.experiment.addData('slider_3.rt', slider_3.getRT());
    // the Routine "practiceTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function crosshair5RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crosshair5' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    crosshair5Clock.reset(routineTimer.getTime());
    routineTimer.add(1.000000);
    crosshair5MaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('crosshair5.started', globalClock.getTime());
    crosshair5MaxDuration = null
    // keep track of which components have finished
    crosshair5Components = [];
    crosshair5Components.push(text_27);
    
    crosshair5Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function crosshair5RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crosshair5' ---
    // get current time
    t = crosshair5Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_27* updates
    if (t >= 0.0 && text_27.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_27.tStart = t;  // (not accounting for frame time here)
      text_27.frameNStart = frameN;  // exact frame index
      
      text_27.setAutoDraw(true);
    }
    
    
    // if text_27 is active this frame...
    if (text_27.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_27.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      text_27.tStop = t;  // not accounting for scr refresh
      text_27.frameNStop = frameN;  // exact frame index
      // update status
      text_27.status = PsychoJS.Status.FINISHED;
      text_27.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    crosshair5Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function crosshair5RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crosshair5' ---
    crosshair5Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('crosshair5.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (crosshair5MaxDurationReached) {
        crosshair5Clock.add(crosshair5MaxDuration);
    } else {
        crosshair5Clock.add(1.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function actualPoints1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'actualPoints1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    actualPoints1Clock.reset(routineTimer.getTime());
    routineTimer.add(2.000000);
    actualPoints1MaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('actualPoints1.started', globalClock.getTime());
    actualPoints1MaxDuration = null
    // keep track of which components have finished
    actualPoints1Components = [];
    actualPoints1Components.push(text_actual_points);
    
    actualPoints1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function actualPoints1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'actualPoints1' ---
    // get current time
    t = actualPoints1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_actual_points* updates
    if (t >= 0.0 && text_actual_points.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_actual_points.tStart = t;  // (not accounting for frame time here)
      text_actual_points.frameNStart = frameN;  // exact frame index
      
      text_actual_points.setAutoDraw(true);
    }
    
    
    // if text_actual_points is active this frame...
    if (text_actual_points.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_actual_points.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      text_actual_points.tStop = t;  // not accounting for scr refresh
      text_actual_points.frameNStop = frameN;  // exact frame index
      // update status
      text_actual_points.status = PsychoJS.Status.FINISHED;
      text_actual_points.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    actualPoints1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function actualPoints1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'actualPoints1' ---
    actualPoints1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('actualPoints1.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (actualPoints1MaxDurationReached) {
        actualPoints1Clock.add(actualPoints1MaxDuration);
    } else {
        actualPoints1Clock.add(2.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function crosshair3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crosshair3' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    crosshair3Clock.reset(routineTimer.getTime());
    routineTimer.add(1.000000);
    crosshair3MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_23
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    if (_pj.in_es6("crosshair", locals())) {
        crosshair.opacity = 1;
        crosshair.setAutoDraw(true);
    }
    
    psychoJS.experiment.addData('crosshair3.started', globalClock.getTime());
    crosshair3MaxDuration = null
    // keep track of which components have finished
    crosshair3Components = [];
    crosshair3Components.push(text_23);
    
    crosshair3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function crosshair3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crosshair3' ---
    // get current time
    t = crosshair3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_23* updates
    if (t >= 0.0 && text_23.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_23.tStart = t;  // (not accounting for frame time here)
      text_23.frameNStart = frameN;  // exact frame index
      
      text_23.setAutoDraw(true);
    }
    
    
    // if text_23 is active this frame...
    if (text_23.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_23.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      text_23.tStop = t;  // not accounting for scr refresh
      text_23.frameNStop = frameN;  // exact frame index
      // update status
      text_23.status = PsychoJS.Status.FINISHED;
      text_23.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    crosshair3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function crosshair3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crosshair3' ---
    crosshair3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('crosshair3.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (crosshair3MaxDurationReached) {
        crosshair3Clock.add(crosshair3MaxDuration);
    } else {
        crosshair3Clock.add(1.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function taskStartSoonRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'taskStartSoon' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    taskStartSoonClock.reset();
    routineTimer.reset();
    taskStartSoonMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_10.keys = undefined;
    key_resp_10.rt = undefined;
    _key_resp_10_allKeys = [];
    // Run 'Begin Routine' code from code_20
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    try {
        psychoJS.eventManager.clearEvents();
    } catch(e) {
    }
    if (_pj.in_es6("text_task_start_soon", locals())) {
        text_task_start_soon.text = "The task will start soon. Press 2 to continue";
        text_task_start_soon.opacity = 1;
        text_task_start_soon.setAutoDraw(true);
        console.log("Task start soon screen displayed");
    } else {
        console.log("WARNING: text_task_start_soon component not found!");
    }
    
    psychoJS.experiment.addData('taskStartSoon.started', globalClock.getTime());
    taskStartSoonMaxDuration = null
    // keep track of which components have finished
    taskStartSoonComponents = [];
    taskStartSoonComponents.push(text_task_start_soon);
    taskStartSoonComponents.push(key_resp_10);
    
    taskStartSoonComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function taskStartSoonRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'taskStartSoon' ---
    // get current time
    t = taskStartSoonClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_task_start_soon* updates
    if (t >= 0.0 && text_task_start_soon.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_task_start_soon.tStart = t;  // (not accounting for frame time here)
      text_task_start_soon.frameNStart = frameN;  // exact frame index
      
      text_task_start_soon.setAutoDraw(true);
    }
    
    
    // if text_task_start_soon is active this frame...
    if (text_task_start_soon.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_resp_10* updates
    if (t >= 0.0 && key_resp_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_10.tStart = t;  // (not accounting for frame time here)
      key_resp_10.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_10.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_10.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_10.clearEvents(); });
    }
    
    // if key_resp_10 is active this frame...
    if (key_resp_10.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_10.getKeys({keyList: ['2','num2'], waitRelease: false});
      _key_resp_10_allKeys = _key_resp_10_allKeys.concat(theseKeys);
      if (_key_resp_10_allKeys.length > 0) {
        key_resp_10.keys = _key_resp_10_allKeys[_key_resp_10_allKeys.length - 1].name;  // just the last key pressed
        key_resp_10.rt = _key_resp_10_allKeys[_key_resp_10_allKeys.length - 1].rt;
        key_resp_10.duration = _key_resp_10_allKeys[_key_resp_10_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    taskStartSoonComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function taskStartSoonRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'taskStartSoon' ---
    taskStartSoonComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('taskStartSoon.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_10.corr, level);
    }
    psychoJS.experiment.addData('key_resp_10.keys', key_resp_10.keys);
    if (typeof key_resp_10.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_10.rt', key_resp_10.rt);
        psychoJS.experiment.addData('key_resp_10.duration', key_resp_10.duration);
        routineTimer.reset();
        }
    
    key_resp_10.stop();
    // the Routine "taskStartSoon" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function scannerSyncRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'scannerSync' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    scannerSyncClock.reset();
    routineTimer.reset();
    scannerSyncMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_11.keys = undefined;
    key_resp_11.rt = undefined;
    _key_resp_11_allKeys = [];
    // Run 'Begin Routine' code from code_21
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    try {
        psychoJS.eventManager.clearEvents();
    } catch(e) {
    }
    if (_pj.in_es6("text_scanner_wait", locals())) {
        text_scanner_wait.text = "Waiting for the scanner to start...";
        text_scanner_wait.opacity = 1;
        text_scanner_wait.setAutoDraw(true);
        console.log("Scanner sync: Waiting for trigger '5' from MRI scanner");
    } else {
        console.log("WARNING: text_scanner_wait component not found!");
    }
    
    psychoJS.experiment.addData('scannerSync.started', globalClock.getTime());
    scannerSyncMaxDuration = null
    // keep track of which components have finished
    scannerSyncComponents = [];
    scannerSyncComponents.push(text_scanner_wait);
    scannerSyncComponents.push(key_resp_11);
    
    scannerSyncComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function scannerSyncRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'scannerSync' ---
    // get current time
    t = scannerSyncClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_scanner_wait* updates
    if (t >= 0.0 && text_scanner_wait.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_scanner_wait.tStart = t;  // (not accounting for frame time here)
      text_scanner_wait.frameNStart = frameN;  // exact frame index
      
      text_scanner_wait.setAutoDraw(true);
    }
    
    
    // if text_scanner_wait is active this frame...
    if (text_scanner_wait.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_resp_11* updates
    if (t >= 0.0 && key_resp_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_11.tStart = t;  // (not accounting for frame time here)
      key_resp_11.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_11.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_11.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_11.clearEvents(); });
    }
    
    // if key_resp_11 is active this frame...
    if (key_resp_11.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_11.getKeys({keyList: ['5','num5'], waitRelease: false});
      _key_resp_11_allKeys = _key_resp_11_allKeys.concat(theseKeys);
      if (_key_resp_11_allKeys.length > 0) {
        key_resp_11.keys = _key_resp_11_allKeys[_key_resp_11_allKeys.length - 1].name;  // just the last key pressed
        key_resp_11.rt = _key_resp_11_allKeys[_key_resp_11_allKeys.length - 1].rt;
        key_resp_11.duration = _key_resp_11_allKeys[_key_resp_11_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    scannerSyncComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function scannerSyncRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'scannerSync' ---
    scannerSyncComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('scannerSync.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_11.corr, level);
    }
    psychoJS.experiment.addData('key_resp_11.keys', key_resp_11.keys);
    if (typeof key_resp_11.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_11.rt', key_resp_11.rt);
        psychoJS.experiment.addData('key_resp_11.duration', key_resp_11.duration);
        routineTimer.reset();
        }
    
    key_resp_11.stop();
    // the Routine "scannerSync" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function scannerWaitRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'scannerWait' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    scannerWaitClock.reset(routineTimer.getTime());
    routineTimer.add(2.000000);
    scannerWaitMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('scannerWait.started', globalClock.getTime());
    scannerWaitMaxDuration = null
    // keep track of which components have finished
    scannerWaitComponents = [];
    scannerWaitComponents.push(waitImage);
    
    scannerWaitComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function scannerWaitRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'scannerWait' ---
    // get current time
    t = scannerWaitClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *waitImage* updates
    if (t >= 0.0 && waitImage.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      waitImage.tStart = t;  // (not accounting for frame time here)
      waitImage.frameNStart = frameN;  // exact frame index
      
      waitImage.setAutoDraw(true);
    }
    
    
    // if waitImage is active this frame...
    if (waitImage.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (waitImage.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      waitImage.tStop = t;  // not accounting for scr refresh
      waitImage.frameNStop = frameN;  // exact frame index
      // update status
      waitImage.status = PsychoJS.Status.FINISHED;
      waitImage.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    scannerWaitComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function scannerWaitRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'scannerWait' ---
    scannerWaitComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('scannerWait.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (scannerWaitMaxDurationReached) {
        scannerWaitClock.add(scannerWaitMaxDuration);
    } else {
        scannerWaitClock.add(2.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function startTaskRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'startTask' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    startTaskClock.reset(routineTimer.getTime());
    routineTimer.add(10.000000);
    startTaskMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('startTask.started', globalClock.getTime());
    startTaskMaxDuration = null
    // keep track of which components have finished
    startTaskComponents = [];
    startTaskComponents.push(text_4);
    
    startTaskComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function startTaskRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'startTask' ---
    // get current time
    t = startTaskClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_4* updates
    if (t >= 0.0 && text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_4.tStart = t;  // (not accounting for frame time here)
      text_4.frameNStart = frameN;  // exact frame index
      
      text_4.setAutoDraw(true);
    }
    
    
    // if text_4 is active this frame...
    if (text_4.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      text_4.tStop = t;  // not accounting for scr refresh
      text_4.frameNStop = frameN;  // exact frame index
      // update status
      text_4.status = PsychoJS.Status.FINISHED;
      text_4.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    startTaskComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function startTaskRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'startTask' ---
    startTaskComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('startTask.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (startTaskMaxDurationReached) {
        startTaskClock.add(startTaskMaxDuration);
    } else {
        startTaskClock.add(10.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    trialClock.reset();
    routineTimer.reset();
    trialMaxDurationReached = false;
    // update component parameters for each repeat
    slider.reset()
    image_3.setImage('images/blank.png');
    // Run 'Begin Routine' code from code_2
    current = trials[trial_index];
    trial_index += 1;
    fruitFile = current["fruit"];
    trueVal = current["true_value"];
    baselineR = current["baseline"];
    blockType = current["block"];
    console.log("Trial", trial_index, fruitFile, trueVal);
    slider.reset();
    
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    psychoJS.experiment.addData('trial.started', globalClock.getTime());
    trialMaxDuration = null
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(slider);
    trialComponents.push(image_3);
    trialComponents.push(key_resp_2);
    trialComponents.push(text_slider_value);
    
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial' ---
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *slider* updates
    if (t >= 0 && slider.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      slider.tStart = t;  // (not accounting for frame time here)
      slider.frameNStart = frameN;  // exact frame index
      
      slider.setAutoDraw(true);
    }
    
    
    // if slider is active this frame...
    if (slider.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *image_3* updates
    if (t >= 0 && image_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_3.tStart = t;  // (not accounting for frame time here)
      image_3.frameNStart = frameN;  // exact frame index
      
      image_3.setAutoDraw(true);
    }
    
    
    // if image_3 is active this frame...
    if (image_3.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }
    
    // if key_resp_2 is active this frame...
    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['left','right','return'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        key_resp_2.duration = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].duration;
      }
    }
    
    
    // *text_slider_value* updates
    if (t >= 0.0 && text_slider_value.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_slider_value.tStart = t;  // (not accounting for frame time here)
      text_slider_value.frameNStart = frameN;  // exact frame index
      
      text_slider_value.setAutoDraw(true);
    }
    
    
    // if text_slider_value is active this frame...
    if (text_slider_value.status === PsychoJS.Status.STARTED) {
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial' ---
    trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('trial.stopped', globalClock.getTime());
    psychoJS.experiment.addData('slider.response', slider.getRating());
    psychoJS.experiment.addData('slider.rt', slider.getRT());
    // Run 'End Routine' code from code_2
    rating = slider.getRating();
    rt = slider.getRT();
    psychoJS.experiment.addData("block", blockType);
    psychoJS.experiment.addData("fruit", fruitFile);
    psychoJS.experiment.addData("baseline", baselineR);
    psychoJS.experiment.addData("true_value", trueVal);
    psychoJS.experiment.addData("predicted", rating);
    psychoJS.experiment.addData("predicted_rt", rt);
    
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_2.corr, level);
    }
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        psychoJS.experiment.addData('key_resp_2.duration', key_resp_2.duration);
        }
    
    key_resp_2.stop();
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function timeoutRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'timeout' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    timeoutClock.reset();
    routineTimer.reset();
    timeoutMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_7
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    if (_pj.in_es6("text_timeout", locals())) {
        text_timeout.text = "Time out";
        text_timeout.opacity = 1;
        text_timeout.setAutoDraw(true);
    }
    console.log("Showing timeout screen");
    
    psychoJS.experiment.addData('timeout.started', globalClock.getTime());
    timeoutMaxDuration = null
    // keep track of which components have finished
    timeoutComponents = [];
    timeoutComponents.push(text_timeout);
    
    timeoutComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function timeoutRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'timeout' ---
    // get current time
    t = timeoutClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_timeout* updates
    if (t >= 0.0 && text_timeout.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_timeout.tStart = t;  // (not accounting for frame time here)
      text_timeout.frameNStart = frameN;  // exact frame index
      
      text_timeout.setAutoDraw(true);
    }
    
    
    // if text_timeout is active this frame...
    if (text_timeout.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + timeout_duration - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_timeout.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      text_timeout.tStop = t;  // not accounting for scr refresh
      text_timeout.frameNStop = frameN;  // exact frame index
      // update status
      text_timeout.status = PsychoJS.Status.FINISHED;
      text_timeout.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    timeoutComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function timeoutRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'timeout' ---
    timeoutComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('timeout.stopped', globalClock.getTime());
    // the Routine "timeout" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function crosshair1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crosshair1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    crosshair1Clock.reset();
    routineTimer.reset();
    crosshair1MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_6
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    if (_pj.in_es6("crosshair", locals())) {
        crosshair.opacity = 1;
        crosshair.setAutoDraw(true);
    }
    
    psychoJS.experiment.addData('crosshair1.started', globalClock.getTime());
    crosshair1MaxDuration = null
    // keep track of which components have finished
    crosshair1Components = [];
    crosshair1Components.push(text_13);
    
    crosshair1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function crosshair1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crosshair1' ---
    // get current time
    t = crosshair1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_13* updates
    if (t >= 0.0 && text_13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_13.tStart = t;  // (not accounting for frame time here)
      text_13.frameNStart = frameN;  // exact frame index
      
      text_13.setAutoDraw(true);
    }
    
    
    // if text_13 is active this frame...
    if (text_13.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + crosshair1_duration - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_13.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      text_13.tStop = t;  // not accounting for scr refresh
      text_13.frameNStop = frameN;  // exact frame index
      // update status
      text_13.status = PsychoJS.Status.FINISHED;
      text_13.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    crosshair1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function crosshair1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crosshair1' ---
    crosshair1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('crosshair1.stopped', globalClock.getTime());
    // the Routine "crosshair1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function actualPointsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'actualPoints' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    actualPointsClock.reset();
    routineTimer.reset();
    actualPointsMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('actualPoints.started', globalClock.getTime());
    actualPointsMaxDuration = null
    // keep track of which components have finished
    actualPointsComponents = [];
    actualPointsComponents.push(image_30);
    
    actualPointsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function actualPointsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'actualPoints' ---
    // get current time
    t = actualPointsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_30* updates
    if (t >= 0.0 && image_30.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_30.tStart = t;  // (not accounting for frame time here)
      image_30.frameNStart = frameN;  // exact frame index
      
      image_30.setAutoDraw(true);
    }
    
    
    // if image_30 is active this frame...
    if (image_30.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + actualPoints_duration - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image_30.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      image_30.tStop = t;  // not accounting for scr refresh
      image_30.frameNStop = frameN;  // exact frame index
      // update status
      image_30.status = PsychoJS.Status.FINISHED;
      image_30.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    actualPointsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function actualPointsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'actualPoints' ---
    actualPointsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('actualPoints.stopped', globalClock.getTime());
    // the Routine "actualPoints" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function crosshair2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crosshair2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    crosshair2Clock.reset();
    routineTimer.reset();
    crosshair2MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_9
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    if (_pj.in_es6("crosshair", locals())) {
        crosshair.opacity = 1;
        crosshair.setAutoDraw(true);
    }
    
    psychoJS.experiment.addData('crosshair2.started', globalClock.getTime());
    crosshair2MaxDuration = null
    // keep track of which components have finished
    crosshair2Components = [];
    crosshair2Components.push(text_14);
    
    crosshair2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function crosshair2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crosshair2' ---
    // get current time
    t = crosshair2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_14* updates
    if (t >= 0.0 && text_14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_14.tStart = t;  // (not accounting for frame time here)
      text_14.frameNStart = frameN;  // exact frame index
      
      text_14.setAutoDraw(true);
    }
    
    
    // if text_14 is active this frame...
    if (text_14.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + crosshair2_duration - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_14.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      text_14.tStop = t;  // not accounting for scr refresh
      text_14.frameNStop = frameN;  // exact frame index
      // update status
      text_14.status = PsychoJS.Status.FINISHED;
      text_14.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    crosshair2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function crosshair2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crosshair2' ---
    crosshair2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('crosshair2.stopped', globalClock.getTime());
    // the Routine "crosshair2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function blockTransitionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'blockTransition' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    blockTransitionClock.reset();
    routineTimer.reset();
    blockTransitionMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_transition.keys = undefined;
    key_resp_transition.rt = undefined;
    _key_resp_transition_allKeys = [];
    psychoJS.experiment.addData('blockTransition.started', globalClock.getTime());
    blockTransitionMaxDuration = null
    // keep track of which components have finished
    blockTransitionComponents = [];
    blockTransitionComponents.push(text_block_transition);
    blockTransitionComponents.push(key_resp_transition);
    
    blockTransitionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function blockTransitionRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'blockTransition' ---
    // get current time
    t = blockTransitionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_block_transition* updates
    if (t >= 0.0 && text_block_transition.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_block_transition.tStart = t;  // (not accounting for frame time here)
      text_block_transition.frameNStart = frameN;  // exact frame index
      
      text_block_transition.setAutoDraw(true);
    }
    
    
    // if text_block_transition is active this frame...
    if (text_block_transition.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_resp_transition* updates
    if (t >= 0.0 && key_resp_transition.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_transition.tStart = t;  // (not accounting for frame time here)
      key_resp_transition.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_transition.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_transition.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_transition.clearEvents(); });
    }
    
    // if key_resp_transition is active this frame...
    if (key_resp_transition.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_transition.getKeys({keyList: ['2','num_2'], waitRelease: false});
      _key_resp_transition_allKeys = _key_resp_transition_allKeys.concat(theseKeys);
      if (_key_resp_transition_allKeys.length > 0) {
        key_resp_transition.keys = _key_resp_transition_allKeys[_key_resp_transition_allKeys.length - 1].name;  // just the last key pressed
        key_resp_transition.rt = _key_resp_transition_allKeys[_key_resp_transition_allKeys.length - 1].rt;
        key_resp_transition.duration = _key_resp_transition_allKeys[_key_resp_transition_allKeys.length - 1].duration;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    blockTransitionComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function blockTransitionRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'blockTransition' ---
    blockTransitionComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('blockTransition.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_transition.corr, level);
    }
    psychoJS.experiment.addData('key_resp_transition.keys', key_resp_transition.keys);
    if (typeof key_resp_transition.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_transition.rt', key_resp_transition.rt);
        psychoJS.experiment.addData('key_resp_transition.duration', key_resp_transition.duration);
        }
    
    key_resp_transition.stop();
    // the Routine "blockTransition" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function taskStartSoonBlock2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'taskStartSoonBlock2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    taskStartSoonBlock2Clock.reset();
    routineTimer.reset();
    taskStartSoonBlock2MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_14.keys = undefined;
    key_resp_14.rt = undefined;
    _key_resp_14_allKeys = [];
    psychoJS.experiment.addData('taskStartSoonBlock2.started', globalClock.getTime());
    taskStartSoonBlock2MaxDuration = null
    // keep track of which components have finished
    taskStartSoonBlock2Components = [];
    taskStartSoonBlock2Components.push(key_resp_14);
    taskStartSoonBlock2Components.push(text_24);
    
    taskStartSoonBlock2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function taskStartSoonBlock2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'taskStartSoonBlock2' ---
    // get current time
    t = taskStartSoonBlock2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_14* updates
    if (t >= 0.0 && key_resp_14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_14.tStart = t;  // (not accounting for frame time here)
      key_resp_14.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_14.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_14.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_14.clearEvents(); });
    }
    
    // if key_resp_14 is active this frame...
    if (key_resp_14.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_14.getKeys({keyList: '2', waitRelease: false});
      _key_resp_14_allKeys = _key_resp_14_allKeys.concat(theseKeys);
      if (_key_resp_14_allKeys.length > 0) {
        key_resp_14.keys = _key_resp_14_allKeys[_key_resp_14_allKeys.length - 1].name;  // just the last key pressed
        key_resp_14.rt = _key_resp_14_allKeys[_key_resp_14_allKeys.length - 1].rt;
        key_resp_14.duration = _key_resp_14_allKeys[_key_resp_14_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_24* updates
    if (t >= 0.0 && text_24.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_24.tStart = t;  // (not accounting for frame time here)
      text_24.frameNStart = frameN;  // exact frame index
      
      text_24.setAutoDraw(true);
    }
    
    
    // if text_24 is active this frame...
    if (text_24.status === PsychoJS.Status.STARTED) {
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    taskStartSoonBlock2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function taskStartSoonBlock2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'taskStartSoonBlock2' ---
    taskStartSoonBlock2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('taskStartSoonBlock2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_14.corr, level);
    }
    psychoJS.experiment.addData('key_resp_14.keys', key_resp_14.keys);
    if (typeof key_resp_14.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_14.rt', key_resp_14.rt);
        psychoJS.experiment.addData('key_resp_14.duration', key_resp_14.duration);
        routineTimer.reset();
        }
    
    key_resp_14.stop();
    // the Routine "taskStartSoonBlock2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function scannerSyncBlock2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'scannerSyncBlock2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    scannerSyncBlock2Clock.reset();
    routineTimer.reset();
    scannerSyncBlock2MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_25
    /* Syntax Error: Fix Python code */
    key_resp_13.keys = undefined;
    key_resp_13.rt = undefined;
    _key_resp_13_allKeys = [];
    psychoJS.experiment.addData('scannerSyncBlock2.started', globalClock.getTime());
    scannerSyncBlock2MaxDuration = null
    // keep track of which components have finished
    scannerSyncBlock2Components = [];
    scannerSyncBlock2Components.push(text_scanner_wait_2);
    scannerSyncBlock2Components.push(key_resp_13);
    
    scannerSyncBlock2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function scannerSyncBlock2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'scannerSyncBlock2' ---
    // get current time
    t = scannerSyncBlock2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_scanner_wait_2* updates
    if (t >= 0.0 && text_scanner_wait_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_scanner_wait_2.tStart = t;  // (not accounting for frame time here)
      text_scanner_wait_2.frameNStart = frameN;  // exact frame index
      
      text_scanner_wait_2.setAutoDraw(true);
    }
    
    
    // if text_scanner_wait_2 is active this frame...
    if (text_scanner_wait_2.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_resp_13* updates
    if (t >= 0.0 && key_resp_13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_13.tStart = t;  // (not accounting for frame time here)
      key_resp_13.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_13.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_13.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_13.clearEvents(); });
    }
    
    // if key_resp_13 is active this frame...
    if (key_resp_13.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_13.getKeys({keyList: '5', waitRelease: false});
      _key_resp_13_allKeys = _key_resp_13_allKeys.concat(theseKeys);
      if (_key_resp_13_allKeys.length > 0) {
        key_resp_13.keys = _key_resp_13_allKeys[_key_resp_13_allKeys.length - 1].name;  // just the last key pressed
        key_resp_13.rt = _key_resp_13_allKeys[_key_resp_13_allKeys.length - 1].rt;
        key_resp_13.duration = _key_resp_13_allKeys[_key_resp_13_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    scannerSyncBlock2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function scannerSyncBlock2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'scannerSyncBlock2' ---
    scannerSyncBlock2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('scannerSyncBlock2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_13.corr, level);
    }
    psychoJS.experiment.addData('key_resp_13.keys', key_resp_13.keys);
    if (typeof key_resp_13.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_13.rt', key_resp_13.rt);
        psychoJS.experiment.addData('key_resp_13.duration', key_resp_13.duration);
        routineTimer.reset();
        }
    
    key_resp_13.stop();
    // the Routine "scannerSyncBlock2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function crosshairBlock2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crosshairBlock2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    crosshairBlock2Clock.reset(routineTimer.getTime());
    routineTimer.add(2.000000);
    crosshairBlock2MaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('crosshairBlock2.started', globalClock.getTime());
    crosshairBlock2MaxDuration = null
    // keep track of which components have finished
    crosshairBlock2Components = [];
    crosshairBlock2Components.push(text_crosshair_block2);
    
    crosshairBlock2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function crosshairBlock2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crosshairBlock2' ---
    // get current time
    t = crosshairBlock2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_crosshair_block2* updates
    if (t >= 0.0 && text_crosshair_block2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_crosshair_block2.tStart = t;  // (not accounting for frame time here)
      text_crosshair_block2.frameNStart = frameN;  // exact frame index
      
      text_crosshair_block2.setAutoDraw(true);
    }
    
    
    // if text_crosshair_block2 is active this frame...
    if (text_crosshair_block2.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_crosshair_block2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      text_crosshair_block2.tStop = t;  // not accounting for scr refresh
      text_crosshair_block2.frameNStop = frameN;  // exact frame index
      // update status
      text_crosshair_block2.status = PsychoJS.Status.FINISHED;
      text_crosshair_block2.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    crosshairBlock2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function crosshairBlock2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crosshairBlock2' ---
    crosshairBlock2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('crosshairBlock2.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (crosshairBlock2MaxDurationReached) {
        crosshairBlock2Clock.add(crosshairBlock2MaxDuration);
    } else {
        crosshairBlock2Clock.add(2.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function scannerWaitBlock2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'scannerWaitBlock2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    scannerWaitBlock2Clock.reset(routineTimer.getTime());
    routineTimer.add(2.000000);
    scannerWaitBlock2MaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('scannerWaitBlock2.started', globalClock.getTime());
    scannerWaitBlock2MaxDuration = null
    // keep track of which components have finished
    scannerWaitBlock2Components = [];
    scannerWaitBlock2Components.push(image_scanner_wait_block2);
    
    scannerWaitBlock2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function scannerWaitBlock2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'scannerWaitBlock2' ---
    // get current time
    t = scannerWaitBlock2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_scanner_wait_block2* updates
    if (t >= 0.0 && image_scanner_wait_block2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_scanner_wait_block2.tStart = t;  // (not accounting for frame time here)
      image_scanner_wait_block2.frameNStart = frameN;  // exact frame index
      
      image_scanner_wait_block2.setAutoDraw(true);
    }
    
    
    // if image_scanner_wait_block2 is active this frame...
    if (image_scanner_wait_block2.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image_scanner_wait_block2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      image_scanner_wait_block2.tStop = t;  // not accounting for scr refresh
      image_scanner_wait_block2.frameNStop = frameN;  // exact frame index
      // update status
      image_scanner_wait_block2.status = PsychoJS.Status.FINISHED;
      image_scanner_wait_block2.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    scannerWaitBlock2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function scannerWaitBlock2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'scannerWaitBlock2' ---
    scannerWaitBlock2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('scannerWaitBlock2.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (scannerWaitBlock2MaxDurationReached) {
        scannerWaitBlock2Clock.add(scannerWaitBlock2MaxDuration);
    } else {
        scannerWaitBlock2Clock.add(2.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function crosshair2Block2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crosshair2Block2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    crosshair2Block2Clock.reset(routineTimer.getTime());
    routineTimer.add(10.000000);
    crosshair2Block2MaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('crosshair2Block2.started', globalClock.getTime());
    crosshair2Block2MaxDuration = null
    // keep track of which components have finished
    crosshair2Block2Components = [];
    crosshair2Block2Components.push(text_crosshair2_block2);
    
    crosshair2Block2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function crosshair2Block2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crosshair2Block2' ---
    // get current time
    t = crosshair2Block2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_crosshair2_block2* updates
    if (t >= 0.0 && text_crosshair2_block2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_crosshair2_block2.tStart = t;  // (not accounting for frame time here)
      text_crosshair2_block2.frameNStart = frameN;  // exact frame index
      
      text_crosshair2_block2.setAutoDraw(true);
    }
    
    
    // if text_crosshair2_block2 is active this frame...
    if (text_crosshair2_block2.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_crosshair2_block2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      text_crosshair2_block2.tStop = t;  // not accounting for scr refresh
      text_crosshair2_block2.frameNStop = frameN;  // exact frame index
      // update status
      text_crosshair2_block2.status = PsychoJS.Status.FINISHED;
      text_crosshair2_block2.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    crosshair2Block2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function crosshair2Block2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crosshair2Block2' ---
    crosshair2Block2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('crosshair2Block2.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (crosshair2Block2MaxDurationReached) {
        crosshair2Block2Clock.add(crosshair2Block2MaxDuration);
    } else {
        crosshair2Block2Clock.add(10.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function decisionPhaseRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'decisionPhase' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    decisionPhaseClock.reset();
    routineTimer.reset();
    decisionPhaseMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_4.keys = undefined;
    key_resp_4.rt = undefined;
    _key_resp_4_allKeys = [];
    psychoJS.experiment.addData('decisionPhase.started', globalClock.getTime());
    decisionPhaseMaxDuration = null
    // keep track of which components have finished
    decisionPhaseComponents = [];
    decisionPhaseComponents.push(text_5);
    decisionPhaseComponents.push(key_resp_4);
    
    decisionPhaseComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function decisionPhaseRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'decisionPhase' ---
    // get current time
    t = decisionPhaseClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_5* updates
    if (t >= 0.0 && text_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_5.tStart = t;  // (not accounting for frame time here)
      text_5.frameNStart = frameN;  // exact frame index
      
      text_5.setAutoDraw(true);
    }
    
    
    // if text_5 is active this frame...
    if (text_5.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_resp_4* updates
    if (t >= 0.0 && key_resp_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_4.tStart = t;  // (not accounting for frame time here)
      key_resp_4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.clearEvents(); });
    }
    
    // if key_resp_4 is active this frame...
    if (key_resp_4.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_4.getKeys({keyList: ['2','num_2'], waitRelease: false});
      _key_resp_4_allKeys = _key_resp_4_allKeys.concat(theseKeys);
      if (_key_resp_4_allKeys.length > 0) {
        key_resp_4.keys = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].name;  // just the last key pressed
        key_resp_4.rt = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].rt;
        key_resp_4.duration = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    decisionPhaseComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function decisionPhaseRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'decisionPhase' ---
    decisionPhaseComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('decisionPhase.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_4.corr, level);
    }
    psychoJS.experiment.addData('key_resp_4.keys', key_resp_4.keys);
    if (typeof key_resp_4.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_4.rt', key_resp_4.rt);
        psychoJS.experiment.addData('key_resp_4.duration', key_resp_4.duration);
        routineTimer.reset();
        }
    
    key_resp_4.stop();
    // the Routine "decisionPhase" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function decisionInstructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'decisionInstructions' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    decisionInstructionsClock.reset();
    routineTimer.reset();
    decisionInstructionsMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_5.keys = undefined;
    key_resp_5.rt = undefined;
    _key_resp_5_allKeys = [];
    psychoJS.experiment.addData('decisionInstructions.started', globalClock.getTime());
    decisionInstructionsMaxDuration = null
    // keep track of which components have finished
    decisionInstructionsComponents = [];
    decisionInstructionsComponents.push(text_8);
    decisionInstructionsComponents.push(text_9);
    decisionInstructionsComponents.push(key_resp_5);
    
    decisionInstructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function decisionInstructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'decisionInstructions' ---
    // get current time
    t = decisionInstructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_8* updates
    if (t >= 0.0 && text_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_8.tStart = t;  // (not accounting for frame time here)
      text_8.frameNStart = frameN;  // exact frame index
      
      text_8.setAutoDraw(true);
    }
    
    
    // if text_8 is active this frame...
    if (text_8.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *text_9* updates
    if (t >= 0.0 && text_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_9.tStart = t;  // (not accounting for frame time here)
      text_9.frameNStart = frameN;  // exact frame index
      
      text_9.setAutoDraw(true);
    }
    
    
    // if text_9 is active this frame...
    if (text_9.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_resp_5* updates
    if (t >= 0.0 && key_resp_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_5.tStart = t;  // (not accounting for frame time here)
      key_resp_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.clearEvents(); });
    }
    
    // if key_resp_5 is active this frame...
    if (key_resp_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_5.getKeys({keyList: ['2','num_2'], waitRelease: false});
      _key_resp_5_allKeys = _key_resp_5_allKeys.concat(theseKeys);
      if (_key_resp_5_allKeys.length > 0) {
        key_resp_5.keys = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].name;  // just the last key pressed
        key_resp_5.rt = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].rt;
        key_resp_5.duration = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    decisionInstructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function decisionInstructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'decisionInstructions' ---
    decisionInstructionsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('decisionInstructions.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_5.corr, level);
    }
    psychoJS.experiment.addData('key_resp_5.keys', key_resp_5.keys);
    if (typeof key_resp_5.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_5.rt', key_resp_5.rt);
        psychoJS.experiment.addData('key_resp_5.duration', key_resp_5.duration);
        routineTimer.reset();
        }
    
    key_resp_5.stop();
    // the Routine "decisionInstructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function whichFruitRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'whichFruit' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    whichFruitClock.reset();
    routineTimer.reset();
    whichFruitMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_6.keys = undefined;
    key_resp_6.rt = undefined;
    _key_resp_6_allKeys = [];
    psychoJS.experiment.addData('whichFruit.started', globalClock.getTime());
    whichFruitMaxDuration = null
    // keep track of which components have finished
    whichFruitComponents = [];
    whichFruitComponents.push(text_10);
    whichFruitComponents.push(key_resp_6);
    
    whichFruitComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function whichFruitRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'whichFruit' ---
    // get current time
    t = whichFruitClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_10* updates
    if (t >= 0.0 && text_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_10.tStart = t;  // (not accounting for frame time here)
      text_10.frameNStart = frameN;  // exact frame index
      
      text_10.setAutoDraw(true);
    }
    
    
    // if text_10 is active this frame...
    if (text_10.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_resp_6* updates
    if (t >= 0.0 && key_resp_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_6.tStart = t;  // (not accounting for frame time here)
      key_resp_6.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_6.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.clearEvents(); });
    }
    
    // if key_resp_6 is active this frame...
    if (key_resp_6.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_6.getKeys({keyList: ['2','num_2'], waitRelease: false});
      _key_resp_6_allKeys = _key_resp_6_allKeys.concat(theseKeys);
      if (_key_resp_6_allKeys.length > 0) {
        key_resp_6.keys = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].name;  // just the last key pressed
        key_resp_6.rt = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].rt;
        key_resp_6.duration = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    whichFruitComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function whichFruitRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'whichFruit' ---
    whichFruitComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('whichFruit.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_6.corr, level);
    }
    psychoJS.experiment.addData('key_resp_6.keys', key_resp_6.keys);
    if (typeof key_resp_6.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_6.rt', key_resp_6.rt);
        psychoJS.experiment.addData('key_resp_6.duration', key_resp_6.duration);
        routineTimer.reset();
        }
    
    key_resp_6.stop();
    // the Routine "whichFruit" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function practiceIntro2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practiceIntro2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    practiceIntro2Clock.reset();
    routineTimer.reset();
    practiceIntro2MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_28
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    try {
        psychoJS.eventManager.clearEvents();
    } catch(e) {
    }
    if (_pj.in_es6("text_practice_intro", locals())) {
        text_practice_intro.text = "We will run a short practice task now. Press 2 to continue";
        text_practice_intro.opacity = 1;
        text_practice_intro.setAutoDraw(true);
        console.log("Practice introduction screen displayed");
    } else {
        console.log("WARNING: text_practice_intro component not found!");
    }
    
    key_resp_15.keys = undefined;
    key_resp_15.rt = undefined;
    _key_resp_15_allKeys = [];
    psychoJS.experiment.addData('practiceIntro2.started', globalClock.getTime());
    practiceIntro2MaxDuration = null
    // keep track of which components have finished
    practiceIntro2Components = [];
    practiceIntro2Components.push(key_resp_15);
    
    practiceIntro2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function practiceIntro2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practiceIntro2' ---
    // get current time
    t = practiceIntro2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_15* updates
    if (t >= 0.0 && key_resp_15.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_15.tStart = t;  // (not accounting for frame time here)
      key_resp_15.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_15.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_15.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_15.clearEvents(); });
    }
    
    // if key_resp_15 is active this frame...
    if (key_resp_15.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_15.getKeys({keyList: ['2','num_2'], waitRelease: false});
      _key_resp_15_allKeys = _key_resp_15_allKeys.concat(theseKeys);
      if (_key_resp_15_allKeys.length > 0) {
        key_resp_15.keys = _key_resp_15_allKeys[_key_resp_15_allKeys.length - 1].name;  // just the last key pressed
        key_resp_15.rt = _key_resp_15_allKeys[_key_resp_15_allKeys.length - 1].rt;
        key_resp_15.duration = _key_resp_15_allKeys[_key_resp_15_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    practiceIntro2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function practiceIntro2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practiceIntro2' ---
    practiceIntro2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('practiceIntro2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_15.corr, level);
    }
    psychoJS.experiment.addData('key_resp_15.keys', key_resp_15.keys);
    if (typeof key_resp_15.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_15.rt', key_resp_15.rt);
        psychoJS.experiment.addData('key_resp_15.duration', key_resp_15.duration);
        routineTimer.reset();
        }
    
    key_resp_15.stop();
    // the Routine "practiceIntro2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function practiceDecisionSimulus1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practiceDecisionSimulus1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    practiceDecisionSimulus1Clock.reset();
    routineTimer.reset();
    practiceDecisionSimulus1MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_29
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    practice_decision_index = globals().get("practice_decision_index", (- 1));
    practice_decision_index += 1;
    globals()["practice_decision_index"] = practice_decision_index;
    practice_decision_block = globals().get("practice_decision_block", []);
    if (((practice_decision_block && (practice_decision_index >= 0)) && (practice_decision_index < practice_decision_block.length))) {
        current = practice_decision_block[practice_decision_index];
        first_fruit = current["firstFruit"];
        first_side = current["firstSide"];
        if (_pj.in_es6("text_question1", locals())) {
            text_question1.text = "+";
            try {
                text_question1.setPos([0, 0]);
            } catch(e) {
                if ((e instanceof AttributeError)) {
                    text_question1.pos = [0, 0];
                } else {
                    throw e;
                }
            }
            text_question1.opacity = 1;
            text_question1.setAutoDraw(true);
        }
        if ((first_side === "left")) {
            if (_pj.in_es6("image_left3", locals())) {
                image_left3.setImage(first_fruit);
                image_left3.opacity = 1;
                image_left3.setAutoDraw(true);
            }
            if (_pj.in_es6("image_right3", locals())) {
                image_right3.opacity = 0;
                image_right3.setAutoDraw(false);
            }
        } else {
            if (_pj.in_es6("image_right3", locals())) {
                image_right3.setImage(first_fruit);
                image_right3.opacity = 1;
                image_right3.setAutoDraw(true);
            }
            if (_pj.in_es6("image_left3", locals())) {
                image_left3.opacity = 0;
                image_left3.setAutoDraw(false);
            }
        }
        console.log(`Practice decision ${(practice_decision_index + 1)}/3: Showing ${first_fruit} on ${first_side} (2 seconds)`);
    } else {
        console.log(`WARNING: Practice decision trial ${practice_decision_index} out of range`);
    }
    
    psychoJS.experiment.addData('practiceDecisionSimulus1.started', globalClock.getTime());
    practiceDecisionSimulus1MaxDuration = 2
    // keep track of which components have finished
    practiceDecisionSimulus1Components = [];
    practiceDecisionSimulus1Components.push(text_question1);
    practiceDecisionSimulus1Components.push(image_left3);
    practiceDecisionSimulus1Components.push(image_right3);
    
    practiceDecisionSimulus1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function practiceDecisionSimulus1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practiceDecisionSimulus1' ---
    // get current time
    t = practiceDecisionSimulus1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // is it time to end the Routine? (based on local clock)
    if (t > practiceDecisionSimulus1MaxDuration) {
        practiceDecisionSimulus1MaxDurationReached = true
        continueRoutine = false
    }
    
    // *text_question1* updates
    if (t >= 0.0 && text_question1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_question1.tStart = t;  // (not accounting for frame time here)
      text_question1.frameNStart = frameN;  // exact frame index
      
      text_question1.setAutoDraw(true);
    }
    
    
    // if text_question1 is active this frame...
    if (text_question1.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *image_left3* updates
    if (t >= 0.0 && image_left3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_left3.tStart = t;  // (not accounting for frame time here)
      image_left3.frameNStart = frameN;  // exact frame index
      
      image_left3.setAutoDraw(true);
    }
    
    
    // if image_left3 is active this frame...
    if (image_left3.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *image_right3* updates
    if (t >= 0.0 && image_right3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_right3.tStart = t;  // (not accounting for frame time here)
      image_right3.frameNStart = frameN;  // exact frame index
      
      image_right3.setAutoDraw(true);
    }
    
    
    // if image_right3 is active this frame...
    if (image_right3.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image_right3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      image_right3.tStop = t;  // not accounting for scr refresh
      image_right3.frameNStop = frameN;  // exact frame index
      // update status
      image_right3.status = PsychoJS.Status.FINISHED;
      image_right3.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    practiceDecisionSimulus1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function practiceDecisionSimulus1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practiceDecisionSimulus1' ---
    practiceDecisionSimulus1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('practiceDecisionSimulus1.stopped', globalClock.getTime());
    // the Routine "practiceDecisionSimulus1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function crosshairPracticeDecision1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crosshairPracticeDecision1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    crosshairPracticeDecision1Clock.reset();
    routineTimer.reset();
    crosshairPracticeDecision1MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_41
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    if (_pj.in_es6("text_crosshair_practice_decision1", locals())) {
        text_crosshair_practice_decision1.text = "+";
        try {
            text_crosshair_practice_decision1.setPos([0, 0]);
        } catch(e) {
            if ((e instanceof AttributeError)) {
                text_crosshair_practice_decision1.pos = [0, 0];
            } else {
                throw e;
            }
        }
        text_crosshair_practice_decision1.opacity = 1;
        text_crosshair_practice_decision1.setAutoDraw(true);
        console.log("Crosshair Practice Decision 1: Showing fixation cross (1 second)");
    } else {
        console.log("WARNING: text_crosshair_practice_decision1 component not found!");
    }
    if (_pj.in_es6("image_left3", locals())) {
        image_left3.setAutoDraw(false);
        image_left3.opacity = 0;
    }
    if (_pj.in_es6("image_right3", locals())) {
        image_right3.setAutoDraw(false);
        image_right3.opacity = 0;
    }
    
    psychoJS.experiment.addData('crosshairPracticeDecision1.started', globalClock.getTime());
    crosshairPracticeDecision1MaxDuration = null
    // keep track of which components have finished
    crosshairPracticeDecision1Components = [];
    
    crosshairPracticeDecision1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function crosshairPracticeDecision1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crosshairPracticeDecision1' ---
    // get current time
    t = crosshairPracticeDecision1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    crosshairPracticeDecision1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function crosshairPracticeDecision1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crosshairPracticeDecision1' ---
    crosshairPracticeDecision1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('crosshairPracticeDecision1.stopped', globalClock.getTime());
    // the Routine "crosshairPracticeDecision1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function practiceDecisionSimulus2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practiceDecisionSimulus2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    practiceDecisionSimulus2Clock.reset();
    routineTimer.reset();
    practiceDecisionSimulus2MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_30
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    practice_decision_index = globals().get("practice_decision_index", (- 1));
    practice_decision_block = globals().get("practice_decision_block", []);
    if (((practice_decision_block && (practice_decision_index >= 0)) && (practice_decision_index < practice_decision_block.length))) {
        current = practice_decision_block[practice_decision_index];
        second_fruit = current["secondFruit"];
        second_side = current["secondSide"];
        if (_pj.in_es6("text_question_3", locals())) {
            text_question_3.text = "+";
            try {
                text_question_3.setPos([0, 0]);
            } catch(e) {
                if ((e instanceof AttributeError)) {
                    text_question_3.pos = [0, 0];
                } else {
                    throw e;
                }
            }
            text_question_3.opacity = 1;
            text_question_3.setAutoDraw(true);
        }
        if (_pj.in_es6("text_25", locals())) {
            text_25.opacity = 0;
            text_25.setAutoDraw(false);
        }
        if ((second_side === "left")) {
            if (_pj.in_es6("image_left1_3", locals())) {
                image_left1_3.setImage(second_fruit);
                image_left1_3.opacity = 1;
                image_left1_3.setAutoDraw(true);
            }
            if (_pj.in_es6("image_right2_3", locals())) {
                image_right2_3.opacity = 0;
                image_right2_3.setAutoDraw(false);
            }
        } else {
            if (_pj.in_es6("image_right2_3", locals())) {
                image_right2_3.setImage(second_fruit);
                image_right2_3.opacity = 1;
                image_right2_3.setAutoDraw(true);
            }
            if (_pj.in_es6("image_left1_3", locals())) {
                image_left1_3.opacity = 0;
                image_left1_3.setAutoDraw(false);
            }
        }
        console.log(`Practice decision ${(practice_decision_index + 1)}/3: Showing ${second_fruit} on ${second_side} (2 seconds)`);
    } else {
        console.log(`WARNING: Practice decision trial ${practice_decision_index} out of range`);
    }
    
    psychoJS.experiment.addData('practiceDecisionSimulus2.started', globalClock.getTime());
    practiceDecisionSimulus2MaxDuration = 2
    // keep track of which components have finished
    practiceDecisionSimulus2Components = [];
    practiceDecisionSimulus2Components.push(text_question_3);
    practiceDecisionSimulus2Components.push(image_left1_3);
    practiceDecisionSimulus2Components.push(image_right2_3);
    practiceDecisionSimulus2Components.push(text_25);
    
    practiceDecisionSimulus2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function practiceDecisionSimulus2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practiceDecisionSimulus2' ---
    // get current time
    t = practiceDecisionSimulus2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // is it time to end the Routine? (based on local clock)
    if (t > practiceDecisionSimulus2MaxDuration) {
        practiceDecisionSimulus2MaxDurationReached = true
        continueRoutine = false
    }
    
    // *text_question_3* updates
    if (t >= 0.0 && text_question_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_question_3.tStart = t;  // (not accounting for frame time here)
      text_question_3.frameNStart = frameN;  // exact frame index
      
      text_question_3.setAutoDraw(true);
    }
    
    
    // if text_question_3 is active this frame...
    if (text_question_3.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_question_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      text_question_3.tStop = t;  // not accounting for scr refresh
      text_question_3.frameNStop = frameN;  // exact frame index
      // update status
      text_question_3.status = PsychoJS.Status.FINISHED;
      text_question_3.setAutoDraw(false);
    }
    
    
    // *image_left1_3* updates
    if (t >= 0.0 && image_left1_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_left1_3.tStart = t;  // (not accounting for frame time here)
      image_left1_3.frameNStart = frameN;  // exact frame index
      
      image_left1_3.setAutoDraw(true);
    }
    
    
    // if image_left1_3 is active this frame...
    if (image_left1_3.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *image_right2_3* updates
    if (t >= 0.0 && image_right2_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_right2_3.tStart = t;  // (not accounting for frame time here)
      image_right2_3.frameNStart = frameN;  // exact frame index
      
      image_right2_3.setAutoDraw(true);
    }
    
    
    // if image_right2_3 is active this frame...
    if (image_right2_3.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image_right2_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      image_right2_3.tStop = t;  // not accounting for scr refresh
      image_right2_3.frameNStop = frameN;  // exact frame index
      // update status
      image_right2_3.status = PsychoJS.Status.FINISHED;
      image_right2_3.setAutoDraw(false);
    }
    
    
    // *text_25* updates
    if (t >= 0.0 && text_25.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_25.tStart = t;  // (not accounting for frame time here)
      text_25.frameNStart = frameN;  // exact frame index
      
      text_25.setAutoDraw(true);
    }
    
    
    // if text_25 is active this frame...
    if (text_25.status === PsychoJS.Status.STARTED) {
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    practiceDecisionSimulus2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function practiceDecisionSimulus2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practiceDecisionSimulus2' ---
    practiceDecisionSimulus2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('practiceDecisionSimulus2.stopped', globalClock.getTime());
    // the Routine "practiceDecisionSimulus2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function crosshairPracticeDecision2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crosshairPracticeDecision2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    crosshairPracticeDecision2Clock.reset();
    routineTimer.reset();
    crosshairPracticeDecision2MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_42
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    if (_pj.in_es6("text_crosshair_practice_decision2", locals())) {
        text_crosshair_practice_decision2.text = "+";
        try {
            text_crosshair_practice_decision2.setPos([0, 0]);
        } catch(e) {
            if ((e instanceof AttributeError)) {
                text_crosshair_practice_decision2.pos = [0, 0];
            } else {
                throw e;
            }
        }
        text_crosshair_practice_decision2.opacity = 1;
        text_crosshair_practice_decision2.setAutoDraw(true);
        console.log("Crosshair Practice Decision 2: Showing fixation cross (1 second)");
    } else {
        console.log("WARNING: text_crosshair_practice_decision2 component not found!");
    }
    if (_pj.in_es6("image_left1_3", locals())) {
        image_left1_3.setAutoDraw(false);
        image_left1_3.opacity = 0;
    }
    if (_pj.in_es6("image_right2_3", locals())) {
        image_right2_3.setAutoDraw(false);
        image_right2_3.opacity = 0;
    }
    
    psychoJS.experiment.addData('crosshairPracticeDecision2.started', globalClock.getTime());
    crosshairPracticeDecision2MaxDuration = null
    // keep track of which components have finished
    crosshairPracticeDecision2Components = [];
    
    crosshairPracticeDecision2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function crosshairPracticeDecision2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crosshairPracticeDecision2' ---
    // get current time
    t = crosshairPracticeDecision2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    crosshairPracticeDecision2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function crosshairPracticeDecision2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crosshairPracticeDecision2' ---
    crosshairPracticeDecision2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('crosshairPracticeDecision2.stopped', globalClock.getTime());
    // the Routine "crosshairPracticeDecision2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function practiceDecisionMakingRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practiceDecisionMaking' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    practiceDecisionMakingClock.reset();
    routineTimer.reset();
    practiceDecisionMakingMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_31
    import * as time from 'time';
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    practice_decision_index = globals().get("practice_decision_index", (- 1));
    practice_decision_block = globals().get("practice_decision_block", []);
    if (((practice_decision_block && (practice_decision_index >= 0)) && (practice_decision_index < practice_decision_block.length))) {
        current = practice_decision_block[practice_decision_index];
        leftFile = current["leftFruit"];
        rightFile = current["rightFruit"];
        correct = current["correct"];
        if (_pj.in_es6("text_question_4", locals())) {
            text_question_4.text = "+";
            try {
                text_question_4.setPos([0, 0]);
            } catch(e) {
                if ((e instanceof AttributeError)) {
                    text_question_4.pos = [0, 0];
                } else {
                    throw e;
                }
            }
            text_question_4.opacity = 1;
            text_question_4.setAutoDraw(true);
        }
        if (_pj.in_es6("text_25", locals())) {
            text_25.opacity = 0;
            text_25.setAutoDraw(false);
        }
        if (_pj.in_es6("image_left_left1", locals())) {
            image_left_left1.setImage(leftFile);
            image_left_left1.opacity = 1;
            image_left_left1.setAutoDraw(true);
        }
        if (_pj.in_es6("image_right_right1", locals())) {
            image_right_right1.setImage(rightFile);
            image_right_right1.opacity = 1;
            image_right_right1.setAutoDraw(true);
        }
        choice = "";
        decision_start_time = time.time();
        decision_timed_out = false;
        globals()["choice"] = choice;
        globals()["decision_start_time"] = decision_start_time;
        globals()["decision_timed_out"] = false;
        try {
            psychoJS.eventManager.clearEvents();
            console.log(`Cleared key buffer at practice decision start`);
        } catch(e) {
        }
        ignore_keys_until = (decision_start_time + 0.1);
        globals()["ignore_keys_until"] = ignore_keys_until;
        if (_pj.in_es6("mouse_2", locals())) {
            mouse_2.clickReset();
        }
        console.log(`Practice decision ${(practice_decision_index + 1)}/3: ${leftFile} vs ${rightFile}, correct=${correct}`);
    } else {
        leftFile = "images/blank.png";
        rightFile = "images/blank.png";
        choice = "";
        console.log("No more practice decision trials available");
    }
    
    psychoJS.experiment.addData('practiceDecisionMaking.started', globalClock.getTime());
    practiceDecisionMakingMaxDuration = 4
    // keep track of which components have finished
    practiceDecisionMakingComponents = [];
    practiceDecisionMakingComponents.push(text_question_4);
    practiceDecisionMakingComponents.push(image_left_left1);
    practiceDecisionMakingComponents.push(image_right_right1);
    
    practiceDecisionMakingComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function practiceDecisionMakingRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practiceDecisionMaking' ---
    // get current time
    t = practiceDecisionMakingClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // is it time to end the Routine? (based on local clock)
    if (t > practiceDecisionMakingMaxDuration) {
        practiceDecisionMakingMaxDurationReached = true
        continueRoutine = false
    }
    
    // *text_question_4* updates
    if (t >= 0.0 && text_question_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_question_4.tStart = t;  // (not accounting for frame time here)
      text_question_4.frameNStart = frameN;  // exact frame index
      
      text_question_4.setAutoDraw(true);
    }
    
    
    // if text_question_4 is active this frame...
    if (text_question_4.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *image_left_left1* updates
    if (t >= 0.0 && image_left_left1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_left_left1.tStart = t;  // (not accounting for frame time here)
      image_left_left1.frameNStart = frameN;  // exact frame index
      
      image_left_left1.setAutoDraw(true);
    }
    
    
    // if image_left_left1 is active this frame...
    if (image_left_left1.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image_left_left1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      image_left_left1.tStop = t;  // not accounting for scr refresh
      image_left_left1.frameNStop = frameN;  // exact frame index
      // update status
      image_left_left1.status = PsychoJS.Status.FINISHED;
      image_left_left1.setAutoDraw(false);
    }
    
    
    // *image_right_right1* updates
    if (t >= 0.0 && image_right_right1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_right_right1.tStart = t;  // (not accounting for frame time here)
      image_right_right1.frameNStart = frameN;  // exact frame index
      
      image_right_right1.setAutoDraw(true);
    }
    
    
    // if image_right_right1 is active this frame...
    if (image_right_right1.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image_right_right1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      image_right_right1.tStop = t;  // not accounting for scr refresh
      image_right_right1.frameNStop = frameN;  // exact frame index
      // update status
      image_right_right1.status = PsychoJS.Status.FINISHED;
      image_right_right1.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    practiceDecisionMakingComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function practiceDecisionMakingRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practiceDecisionMaking' ---
    practiceDecisionMakingComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('practiceDecisionMaking.stopped', globalClock.getTime());
    // the Routine "practiceDecisionMaking" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function crosshairPracticeDecision3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crosshairPracticeDecision3' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    crosshairPracticeDecision3Clock.reset();
    routineTimer.reset();
    crosshairPracticeDecision3MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_43
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    if (_pj.in_es6("text_crosshair_practice_decision3", locals())) {
        text_crosshair_practice_decision3.text = "+";
        try {
            text_crosshair_practice_decision3.setPos([0, 0]);
        } catch(e) {
            if ((e instanceof AttributeError)) {
                text_crosshair_practice_decision3.pos = [0, 0];
            } else {
                throw e;
            }
        }
        text_crosshair_practice_decision3.opacity = 1;
        text_crosshair_practice_decision3.setAutoDraw(true);
        console.log("Crosshair Practice Decision 3: Showing fixation cross (1 second)");
    } else {
        console.log("WARNING: text_crosshair_practice_decision3 component not found!");
    }
    if (_pj.in_es6("image_left_left1", locals())) {
        image_left_left1.setAutoDraw(false);
        image_left_left1.opacity = 0;
    }
    if (_pj.in_es6("image_right_right1", locals())) {
        image_right_right1.setAutoDraw(false);
        image_right_right1.opacity = 0;
    }
    
    psychoJS.experiment.addData('crosshairPracticeDecision3.started', globalClock.getTime());
    crosshairPracticeDecision3MaxDuration = null
    // keep track of which components have finished
    crosshairPracticeDecision3Components = [];
    
    crosshairPracticeDecision3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function crosshairPracticeDecision3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crosshairPracticeDecision3' ---
    // get current time
    t = crosshairPracticeDecision3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    crosshairPracticeDecision3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function crosshairPracticeDecision3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crosshairPracticeDecision3' ---
    crosshairPracticeDecision3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('crosshairPracticeDecision3.stopped', globalClock.getTime());
    // the Routine "crosshairPracticeDecision3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function taskStartSoonBlock3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'taskStartSoonBlock3' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    taskStartSoonBlock3Clock.reset();
    routineTimer.reset();
    taskStartSoonBlock3MaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('taskStartSoonBlock3.started', globalClock.getTime());
    taskStartSoonBlock3MaxDuration = null
    // keep track of which components have finished
    taskStartSoonBlock3Components = [];
    taskStartSoonBlock3Components.push(text_task_start_soon_block3);
    
    taskStartSoonBlock3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function taskStartSoonBlock3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'taskStartSoonBlock3' ---
    // get current time
    t = taskStartSoonBlock3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_task_start_soon_block3* updates
    if (t >= 0.0 && text_task_start_soon_block3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_task_start_soon_block3.tStart = t;  // (not accounting for frame time here)
      text_task_start_soon_block3.frameNStart = frameN;  // exact frame index
      
      text_task_start_soon_block3.setAutoDraw(true);
    }
    
    
    // if text_task_start_soon_block3 is active this frame...
    if (text_task_start_soon_block3.status === PsychoJS.Status.STARTED) {
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    taskStartSoonBlock3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function taskStartSoonBlock3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'taskStartSoonBlock3' ---
    taskStartSoonBlock3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('taskStartSoonBlock3.stopped', globalClock.getTime());
    // the Routine "taskStartSoonBlock3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function scannerSyncBlock3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'scannerSyncBlock3' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    scannerSyncBlock3Clock.reset();
    routineTimer.reset();
    scannerSyncBlock3MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_33
    import * as time from 'time';
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    try {
        psychoJS.eventManager.clearEvents();
    } catch(e) {
    }
    globals()["scannerSyncBlock3_start_time"] = time.time();
    if (_pj.in_es6("text_scanner_wait_block3", locals())) {
        text_scanner_wait_block3.text = "Waiting for the scanner to start...";
        text_scanner_wait_block3.opacity = 1;
        text_scanner_wait_block3.setAutoDraw(true);
        console.log("Scanner sync Block 3: Waiting for trigger '5' from MRI scanner");
    } else {
        console.log("WARNING: text_scanner_wait_block3 component not found!");
    }
    
    psychoJS.experiment.addData('scannerSyncBlock3.started', globalClock.getTime());
    scannerSyncBlock3MaxDuration = null
    // keep track of which components have finished
    scannerSyncBlock3Components = [];
    scannerSyncBlock3Components.push(text_scanner_wait_block3);
    
    scannerSyncBlock3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function scannerSyncBlock3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'scannerSyncBlock3' ---
    // get current time
    t = scannerSyncBlock3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_scanner_wait_block3* updates
    if (t >= 0.0 && text_scanner_wait_block3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_scanner_wait_block3.tStart = t;  // (not accounting for frame time here)
      text_scanner_wait_block3.frameNStart = frameN;  // exact frame index
      
      text_scanner_wait_block3.setAutoDraw(true);
    }
    
    
    // if text_scanner_wait_block3 is active this frame...
    if (text_scanner_wait_block3.status === PsychoJS.Status.STARTED) {
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    scannerSyncBlock3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function scannerSyncBlock3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'scannerSyncBlock3' ---
    scannerSyncBlock3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('scannerSyncBlock3.stopped', globalClock.getTime());
    // the Routine "scannerSyncBlock3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function crosshair3Block3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crosshair3Block3' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    crosshair3Block3Clock.reset(routineTimer.getTime());
    routineTimer.add(2.000000);
    crosshair3Block3MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_34
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    if (_pj.in_es6("text_crosshair3_block3", locals())) {
        text_crosshair3_block3.text = "+";
        try {
            text_crosshair3_block3.setPos([0, 0]);
        } catch(e) {
            if ((e instanceof AttributeError)) {
                text_crosshair3_block3.pos = [0, 0];
            } else {
                throw e;
            }
        }
        text_crosshair3_block3.opacity = 1;
        text_crosshair3_block3.setAutoDraw(true);
        console.log("Crosshair 3 Block 3: Showing fixation cross (2 seconds)");
    } else {
        console.log("WARNING: text_crosshair3_block3 component not found!");
    }
    
    psychoJS.experiment.addData('crosshair3Block3.started', globalClock.getTime());
    crosshair3Block3MaxDuration = null
    // keep track of which components have finished
    crosshair3Block3Components = [];
    crosshair3Block3Components.push(text_crosshair3_block3);
    
    crosshair3Block3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function crosshair3Block3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crosshair3Block3' ---
    // get current time
    t = crosshair3Block3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_crosshair3_block3* updates
    if (t >= 0.0 && text_crosshair3_block3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_crosshair3_block3.tStart = t;  // (not accounting for frame time here)
      text_crosshair3_block3.frameNStart = frameN;  // exact frame index
      
      text_crosshair3_block3.setAutoDraw(true);
    }
    
    
    // if text_crosshair3_block3 is active this frame...
    if (text_crosshair3_block3.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_crosshair3_block3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      text_crosshair3_block3.tStop = t;  // not accounting for scr refresh
      text_crosshair3_block3.frameNStop = frameN;  // exact frame index
      // update status
      text_crosshair3_block3.status = PsychoJS.Status.FINISHED;
      text_crosshair3_block3.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    crosshair3Block3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function crosshair3Block3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crosshair3Block3' ---
    crosshair3Block3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('crosshair3Block3.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (crosshair3Block3MaxDurationReached) {
        crosshair3Block3Clock.add(crosshair3Block3MaxDuration);
    } else {
        crosshair3Block3Clock.add(2.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function scannerWaitBlock3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'scannerWaitBlock3' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    scannerWaitBlock3Clock.reset(routineTimer.getTime());
    routineTimer.add(2.000000);
    scannerWaitBlock3MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_35
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    if (_pj.in_es6("image_scanner_wait_block3", locals())) {
        image_scanner_wait_block3.opacity = 1;
        image_scanner_wait_block3.setAutoDraw(true);
        console.log("Scanner wait Block 3: Showing wait image (2 seconds)");
    } else {
        console.log("WARNING: image_scanner_wait_block3 component not found!");
    }
    
    psychoJS.experiment.addData('scannerWaitBlock3.started', globalClock.getTime());
    scannerWaitBlock3MaxDuration = null
    // keep track of which components have finished
    scannerWaitBlock3Components = [];
    scannerWaitBlock3Components.push(image_scanner_wait_block3);
    
    scannerWaitBlock3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function scannerWaitBlock3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'scannerWaitBlock3' ---
    // get current time
    t = scannerWaitBlock3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_scanner_wait_block3* updates
    if (t >= 0.0 && image_scanner_wait_block3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_scanner_wait_block3.tStart = t;  // (not accounting for frame time here)
      image_scanner_wait_block3.frameNStart = frameN;  // exact frame index
      
      image_scanner_wait_block3.setAutoDraw(true);
    }
    
    
    // if image_scanner_wait_block3 is active this frame...
    if (image_scanner_wait_block3.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image_scanner_wait_block3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      image_scanner_wait_block3.tStop = t;  // not accounting for scr refresh
      image_scanner_wait_block3.frameNStop = frameN;  // exact frame index
      // update status
      image_scanner_wait_block3.status = PsychoJS.Status.FINISHED;
      image_scanner_wait_block3.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    scannerWaitBlock3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function scannerWaitBlock3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'scannerWaitBlock3' ---
    scannerWaitBlock3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('scannerWaitBlock3.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (scannerWaitBlock3MaxDurationReached) {
        scannerWaitBlock3Clock.add(scannerWaitBlock3MaxDuration);
    } else {
        scannerWaitBlock3Clock.add(2.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function startTaskBlock3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'startTaskBlock3' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    startTaskBlock3Clock.reset(routineTimer.getTime());
    routineTimer.add(10.000000);
    startTaskBlock3MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_36
    console.log("Start task Block 3: Brief pause before decision trials (1 second)");
    
    psychoJS.experiment.addData('startTaskBlock3.started', globalClock.getTime());
    startTaskBlock3MaxDuration = null
    // keep track of which components have finished
    startTaskBlock3Components = [];
    startTaskBlock3Components.push(text_26);
    
    startTaskBlock3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function startTaskBlock3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'startTaskBlock3' ---
    // get current time
    t = startTaskBlock3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_26* updates
    if (t >= 0.0 && text_26.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_26.tStart = t;  // (not accounting for frame time here)
      text_26.frameNStart = frameN;  // exact frame index
      
      text_26.setAutoDraw(true);
    }
    
    
    // if text_26 is active this frame...
    if (text_26.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_26.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      text_26.tStop = t;  // not accounting for scr refresh
      text_26.frameNStop = frameN;  // exact frame index
      // update status
      text_26.status = PsychoJS.Status.FINISHED;
      text_26.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    startTaskBlock3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function startTaskBlock3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'startTaskBlock3' ---
    startTaskBlock3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('startTaskBlock3.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (startTaskBlock3MaxDurationReached) {
        startTaskBlock3Clock.add(startTaskBlock3MaxDuration);
    } else {
        startTaskBlock3Clock.add(10.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function decisionStimulus1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'decisionStimulus1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    decisionStimulus1Clock.reset(routineTimer.getTime());
    routineTimer.add(2.000000);
    decisionStimulus1MaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('decisionStimulus1.started', globalClock.getTime());
    decisionStimulus1MaxDuration = null
    // keep track of which components have finished
    decisionStimulus1Components = [];
    decisionStimulus1Components.push(text_question);
    decisionStimulus1Components.push(image_left1);
    decisionStimulus1Components.push(image_right2);
    
    decisionStimulus1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function decisionStimulus1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'decisionStimulus1' ---
    // get current time
    t = decisionStimulus1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_question* updates
    if (t >= 0.0 && text_question.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_question.tStart = t;  // (not accounting for frame time here)
      text_question.frameNStart = frameN;  // exact frame index
      
      text_question.setAutoDraw(true);
    }
    
    
    // if text_question is active this frame...
    if (text_question.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_question.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      text_question.tStop = t;  // not accounting for scr refresh
      text_question.frameNStop = frameN;  // exact frame index
      // update status
      text_question.status = PsychoJS.Status.FINISHED;
      text_question.setAutoDraw(false);
    }
    
    
    // *image_left1* updates
    if (t >= 0.0 && image_left1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_left1.tStart = t;  // (not accounting for frame time here)
      image_left1.frameNStart = frameN;  // exact frame index
      
      image_left1.setAutoDraw(true);
    }
    
    
    // if image_left1 is active this frame...
    if (image_left1.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image_left1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      image_left1.tStop = t;  // not accounting for scr refresh
      image_left1.frameNStop = frameN;  // exact frame index
      // update status
      image_left1.status = PsychoJS.Status.FINISHED;
      image_left1.setAutoDraw(false);
    }
    
    
    // *image_right2* updates
    if (t >= 0.0 && image_right2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_right2.tStart = t;  // (not accounting for frame time here)
      image_right2.frameNStart = frameN;  // exact frame index
      
      image_right2.setAutoDraw(true);
    }
    
    
    // if image_right2 is active this frame...
    if (image_right2.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image_right2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      image_right2.tStop = t;  // not accounting for scr refresh
      image_right2.frameNStop = frameN;  // exact frame index
      // update status
      image_right2.status = PsychoJS.Status.FINISHED;
      image_right2.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    decisionStimulus1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function decisionStimulus1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'decisionStimulus1' ---
    decisionStimulus1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('decisionStimulus1.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (decisionStimulus1MaxDurationReached) {
        decisionStimulus1Clock.add(decisionStimulus1MaxDuration);
    } else {
        decisionStimulus1Clock.add(2.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function decisionITI1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'decisionITI1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    decisionITI1Clock.reset();
    routineTimer.reset();
    decisionITI1MaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('decisionITI1.started', globalClock.getTime());
    decisionITI1MaxDuration = null
    // keep track of which components have finished
    decisionITI1Components = [];
    decisionITI1Components.push(text_15);
    
    decisionITI1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function decisionITI1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'decisionITI1' ---
    // get current time
    t = decisionITI1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_15* updates
    if (t >= 0.0 && text_15.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_15.tStart = t;  // (not accounting for frame time here)
      text_15.frameNStart = frameN;  // exact frame index
      
      text_15.setAutoDraw(true);
    }
    
    
    // if text_15 is active this frame...
    if (text_15.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + iti1_duration - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_15.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      text_15.tStop = t;  // not accounting for scr refresh
      text_15.frameNStop = frameN;  // exact frame index
      // update status
      text_15.status = PsychoJS.Status.FINISHED;
      text_15.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    decisionITI1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function decisionITI1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'decisionITI1' ---
    decisionITI1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('decisionITI1.stopped', globalClock.getTime());
    // the Routine "decisionITI1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function decisionStimulus2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'decisionStimulus2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    decisionStimulus2Clock.reset(routineTimer.getTime());
    routineTimer.add(2.000000);
    decisionStimulus2MaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('decisionStimulus2.started', globalClock.getTime());
    decisionStimulus2MaxDuration = null
    // keep track of which components have finished
    decisionStimulus2Components = [];
    decisionStimulus2Components.push(text_question_2);
    decisionStimulus2Components.push(image_left1_2);
    decisionStimulus2Components.push(image_right2_2);
    
    decisionStimulus2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function decisionStimulus2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'decisionStimulus2' ---
    // get current time
    t = decisionStimulus2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_question_2* updates
    if (t >= 0.0 && text_question_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_question_2.tStart = t;  // (not accounting for frame time here)
      text_question_2.frameNStart = frameN;  // exact frame index
      
      text_question_2.setAutoDraw(true);
    }
    
    
    // if text_question_2 is active this frame...
    if (text_question_2.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_question_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      text_question_2.tStop = t;  // not accounting for scr refresh
      text_question_2.frameNStop = frameN;  // exact frame index
      // update status
      text_question_2.status = PsychoJS.Status.FINISHED;
      text_question_2.setAutoDraw(false);
    }
    
    
    // *image_left1_2* updates
    if (t >= 0.0 && image_left1_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_left1_2.tStart = t;  // (not accounting for frame time here)
      image_left1_2.frameNStart = frameN;  // exact frame index
      
      image_left1_2.setAutoDraw(true);
    }
    
    
    // if image_left1_2 is active this frame...
    if (image_left1_2.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image_left1_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      image_left1_2.tStop = t;  // not accounting for scr refresh
      image_left1_2.frameNStop = frameN;  // exact frame index
      // update status
      image_left1_2.status = PsychoJS.Status.FINISHED;
      image_left1_2.setAutoDraw(false);
    }
    
    
    // *image_right2_2* updates
    if (t >= 0.0 && image_right2_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_right2_2.tStart = t;  // (not accounting for frame time here)
      image_right2_2.frameNStart = frameN;  // exact frame index
      
      image_right2_2.setAutoDraw(true);
    }
    
    
    // if image_right2_2 is active this frame...
    if (image_right2_2.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image_right2_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      image_right2_2.tStop = t;  // not accounting for scr refresh
      image_right2_2.frameNStop = frameN;  // exact frame index
      // update status
      image_right2_2.status = PsychoJS.Status.FINISHED;
      image_right2_2.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    decisionStimulus2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function decisionStimulus2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'decisionStimulus2' ---
    decisionStimulus2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('decisionStimulus2.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (decisionStimulus2MaxDurationReached) {
        decisionStimulus2Clock.add(decisionStimulus2MaxDuration);
    } else {
        decisionStimulus2Clock.add(2.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function decisionITI2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'decisionITI2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    decisionITI2Clock.reset();
    routineTimer.reset();
    decisionITI2MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_13
    import * as random from 'random';
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    if (_pj.in_es6("text_question_2", locals())) {
        text_question_2.opacity = 0;
        text_question_2.setAutoDraw(false);
    }
    if (_pj.in_es6("image_left1_2", locals())) {
        image_left1_2.opacity = 0;
        image_left1_2.setAutoDraw(false);
    }
    if (_pj.in_es6("image_right2_2", locals())) {
        image_right2_2.opacity = 0;
        image_right2_2.setAutoDraw(false);
    }
    if (_pj.in_es6("text_16", locals())) {
        text_16.text = "+";
        text_16.opacity = 1;
        text_16.setAutoDraw(true);
    }
    iti2_duration = Math.random.choice([1, 2, 3]);
    console.log(`ITI 2: ${iti2_duration} seconds`);
    
    psychoJS.experiment.addData('decisionITI2.started', globalClock.getTime());
    decisionITI2MaxDuration = null
    // keep track of which components have finished
    decisionITI2Components = [];
    decisionITI2Components.push(text_16);
    
    decisionITI2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function decisionITI2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'decisionITI2' ---
    // get current time
    t = decisionITI2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_16* updates
    if (t >= 0.0 && text_16.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_16.tStart = t;  // (not accounting for frame time here)
      text_16.frameNStart = frameN;  // exact frame index
      
      text_16.setAutoDraw(true);
    }
    
    
    // if text_16 is active this frame...
    if (text_16.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + iti2_duration - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_16.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      text_16.tStop = t;  // not accounting for scr refresh
      text_16.frameNStop = frameN;  // exact frame index
      // update status
      text_16.status = PsychoJS.Status.FINISHED;
      text_16.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    decisionITI2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function decisionITI2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'decisionITI2' ---
    decisionITI2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('decisionITI2.stopped', globalClock.getTime());
    // the Routine "decisionITI2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function decisionMakingRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'decisionMaking' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    decisionMakingClock.reset(routineTimer.getTime());
    routineTimer.add(4.000000);
    decisionMakingMaxDurationReached = false;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_2
    // current position of the mouse:
    mouse_2.x = [];
    mouse_2.y = [];
    mouse_2.leftButton = [];
    mouse_2.midButton = [];
    mouse_2.rightButton = [];
    mouse_2.time = [];
    gotValidClick = false; // until a click is received
    psychoJS.experiment.addData('decisionMaking.started', globalClock.getTime());
    decisionMakingMaxDuration = null
    // keep track of which components have finished
    decisionMakingComponents = [];
    decisionMakingComponents.push(text_question_1);
    decisionMakingComponents.push(image_left_left);
    decisionMakingComponents.push(image_right_right);
    decisionMakingComponents.push(mouse_2);
    
    decisionMakingComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function decisionMakingRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'decisionMaking' ---
    // get current time
    t = decisionMakingClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_question_1* updates
    if (t >= 0.0 && text_question_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_question_1.tStart = t;  // (not accounting for frame time here)
      text_question_1.frameNStart = frameN;  // exact frame index
      
      text_question_1.setAutoDraw(true);
    }
    
    
    // if text_question_1 is active this frame...
    if (text_question_1.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_question_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      text_question_1.tStop = t;  // not accounting for scr refresh
      text_question_1.frameNStop = frameN;  // exact frame index
      // update status
      text_question_1.status = PsychoJS.Status.FINISHED;
      text_question_1.setAutoDraw(false);
    }
    
    
    // *image_left_left* updates
    if (t >= 0.0 && image_left_left.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_left_left.tStart = t;  // (not accounting for frame time here)
      image_left_left.frameNStart = frameN;  // exact frame index
      
      image_left_left.setAutoDraw(true);
    }
    
    
    // if image_left_left is active this frame...
    if (image_left_left.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image_left_left.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      image_left_left.tStop = t;  // not accounting for scr refresh
      image_left_left.frameNStop = frameN;  // exact frame index
      // update status
      image_left_left.status = PsychoJS.Status.FINISHED;
      image_left_left.setAutoDraw(false);
    }
    
    
    // *image_right_right* updates
    if (t >= 0.0 && image_right_right.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_right_right.tStart = t;  // (not accounting for frame time here)
      image_right_right.frameNStart = frameN;  // exact frame index
      
      image_right_right.setAutoDraw(true);
    }
    
    
    // if image_right_right is active this frame...
    if (image_right_right.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image_right_right.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      image_right_right.tStop = t;  // not accounting for scr refresh
      image_right_right.frameNStop = frameN;  // exact frame index
      // update status
      image_right_right.status = PsychoJS.Status.FINISHED;
      image_right_right.setAutoDraw(false);
    }
    
    // *mouse_2* updates
    if (t >= 0.0 && mouse_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_2.tStart = t;  // (not accounting for frame time here)
      mouse_2.frameNStart = frameN;  // exact frame index
      
      mouse_2.status = PsychoJS.Status.STARTED;
      mouse_2.mouseClock.reset();
      prevButtonState = mouse_2.getPressed();  // if button is down already this ISN'T a new click
    }
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (mouse_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      mouse_2.tStop = t;  // not accounting for scr refresh
      mouse_2.frameNStop = frameN;  // exact frame index
      // update status
      mouse_2.status = PsychoJS.Status.FINISHED;
      mouse_2.status = PsychoJS.Status.FINISHED;
    }
    
    // if mouse_2 is active this frame...
    if (mouse_2.status === PsychoJS.Status.STARTED) {
      _mouseButtons = mouse_2.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          _mouseXYs = mouse_2.getPos();
          mouse_2.x.push(_mouseXYs[0]);
          mouse_2.y.push(_mouseXYs[1]);
          mouse_2.leftButton.push(_mouseButtons[0]);
          mouse_2.midButton.push(_mouseButtons[1]);
          mouse_2.rightButton.push(_mouseButtons[2]);
          mouse_2.time.push(mouse_2.mouseClock.getTime());
          // end routine on response
          continueRoutine = false;
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    decisionMakingComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function decisionMakingRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'decisionMaking' ---
    decisionMakingComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('decisionMaking.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('mouse_2.x', mouse_2.x);
    psychoJS.experiment.addData('mouse_2.y', mouse_2.y);
    psychoJS.experiment.addData('mouse_2.leftButton', mouse_2.leftButton);
    psychoJS.experiment.addData('mouse_2.midButton', mouse_2.midButton);
    psychoJS.experiment.addData('mouse_2.rightButton', mouse_2.rightButton);
    psychoJS.experiment.addData('mouse_2.time', mouse_2.time);
    
    if (routineForceEnded) {
        routineTimer.reset();} else if (decisionMakingMaxDurationReached) {
        decisionMakingClock.add(decisionMakingMaxDuration);
    } else {
        decisionMakingClock.add(4.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function decisionTimeoutRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'decisionTimeout' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    decisionTimeoutClock.reset();
    routineTimer.reset();
    decisionTimeoutMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('decisionTimeout.started', globalClock.getTime());
    decisionTimeoutMaxDuration = decision_timeout_duration
    // keep track of which components have finished
    decisionTimeoutComponents = [];
    decisionTimeoutComponents.push(text_decision_timeout);
    
    decisionTimeoutComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function decisionTimeoutRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'decisionTimeout' ---
    // get current time
    t = decisionTimeoutClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // is it time to end the Routine? (based on local clock)
    if (t > decisionTimeoutMaxDuration) {
        decisionTimeoutMaxDurationReached = true
        continueRoutine = false
    }
    
    // *text_decision_timeout* updates
    if (t >= 0.0 && text_decision_timeout.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_decision_timeout.tStart = t;  // (not accounting for frame time here)
      text_decision_timeout.frameNStart = frameN;  // exact frame index
      
      text_decision_timeout.setAutoDraw(true);
    }
    
    
    // if text_decision_timeout is active this frame...
    if (text_decision_timeout.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + decision_timeout_duration - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_decision_timeout.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      text_decision_timeout.tStop = t;  // not accounting for scr refresh
      text_decision_timeout.frameNStop = frameN;  // exact frame index
      // update status
      text_decision_timeout.status = PsychoJS.Status.FINISHED;
      text_decision_timeout.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    decisionTimeoutComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function decisionTimeoutRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'decisionTimeout' ---
    decisionTimeoutComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('decisionTimeout.stopped', globalClock.getTime());
    // the Routine "decisionTimeout" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function decisionITI3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'decisionITI3' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    decisionITI3Clock.reset();
    routineTimer.reset();
    decisionITI3MaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('decisionITI3.started', globalClock.getTime());
    decisionITI3MaxDuration = null
    // keep track of which components have finished
    decisionITI3Components = [];
    decisionITI3Components.push(text_17);
    
    decisionITI3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function decisionITI3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'decisionITI3' ---
    // get current time
    t = decisionITI3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_17* updates
    if (t >= 0.0 && text_17.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_17.tStart = t;  // (not accounting for frame time here)
      text_17.frameNStart = frameN;  // exact frame index
      
      text_17.setAutoDraw(true);
    }
    
    
    // if text_17 is active this frame...
    if (text_17.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + iti3_duration - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_17.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      text_17.tStop = t;  // not accounting for scr refresh
      text_17.frameNStop = frameN;  // exact frame index
      // update status
      text_17.status = PsychoJS.Status.FINISHED;
      text_17.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    decisionITI3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function decisionITI3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'decisionITI3' ---
    decisionITI3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('decisionITI3.stopped', globalClock.getTime());
    // the Routine "decisionITI3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function thankYouRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'thankYou' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    thankYouClock.reset();
    routineTimer.reset();
    thankYouMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_8.keys = undefined;
    key_resp_8.rt = undefined;
    _key_resp_8_allKeys = [];
    psychoJS.experiment.addData('thankYou.started', globalClock.getTime());
    thankYouMaxDuration = null
    // keep track of which components have finished
    thankYouComponents = [];
    thankYouComponents.push(text_11);
    thankYouComponents.push(key_resp_8);
    
    thankYouComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function thankYouRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'thankYou' ---
    // get current time
    t = thankYouClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_11* updates
    if (t >= 0.0 && text_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_11.tStart = t;  // (not accounting for frame time here)
      text_11.frameNStart = frameN;  // exact frame index
      
      text_11.setAutoDraw(true);
    }
    
    
    // if text_11 is active this frame...
    if (text_11.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_resp_8* updates
    if (t >= 0.0 && key_resp_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_8.tStart = t;  // (not accounting for frame time here)
      key_resp_8.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_8.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_8.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_8.clearEvents(); });
    }
    
    // if key_resp_8 is active this frame...
    if (key_resp_8.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_8.getKeys({keyList: ['2','num2'], waitRelease: false});
      _key_resp_8_allKeys = _key_resp_8_allKeys.concat(theseKeys);
      if (_key_resp_8_allKeys.length > 0) {
        key_resp_8.keys = _key_resp_8_allKeys[_key_resp_8_allKeys.length - 1].name;  // just the last key pressed
        key_resp_8.rt = _key_resp_8_allKeys[_key_resp_8_allKeys.length - 1].rt;
        key_resp_8.duration = _key_resp_8_allKeys[_key_resp_8_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    thankYouComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function thankYouRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'thankYou' ---
    thankYouComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('thankYou.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_8.corr, level);
    }
    psychoJS.experiment.addData('key_resp_8.keys', key_resp_8.keys);
    if (typeof key_resp_8.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_8.rt', key_resp_8.rt);
        psychoJS.experiment.addData('key_resp_8.duration', key_resp_8.duration);
        routineTimer.reset();
        }
    
    key_resp_8.stop();
    // the Routine "thankYou" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}

async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
