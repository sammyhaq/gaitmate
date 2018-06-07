/*
 #########################
## GAITMATE ARDUINO CODE ##
##~~~~~~~~~~~~~~~~~~~~~~~##
## Zach Samalonis        ##
## Jess Monteleone       ##
## Abigail Balster       ##
 #########################

 Ver 2 Code by Sammy Haq
 (http://www.github.com/sammyhaq/)

 --

 The following code is organized into "states". The system can only be in one
 state at a time. The states are explained below:

 "Walking": The system is currently checking if the patient's gait is normal
 or not. Current configuration checks to see if the patient makes 13 steps
 within 10 seconds. If the patient is successful, then the system will loop into
 the "walking" state again. If not, the system will go into the "vibration
 prompt" state.

 "Vibration Prompt": The system is prompting the patient for a response: to warn
 them that their gait is suboptimal. If the patient presses the button within
 a certain amount of time, then the system will go into the "paused" state. If
 not , the system will continue to the "FoG Recovery" state. During this state,
 a vibration will be played (via the vibrate() function).

 "FoG Recovery": In this state, the patient is not responsive and can be assumed
 to require gait assistance. In this current state, the previous vibration will
 play in tandem with a metronome at an adjustable frequency. This is to aid the
 patient with walking to a rhythm. This mode will continue for 10 seconds. After
 this, the mode will reset to the "walking" state.

 "Paused": The paused state suspends all functions. Everything turns off --
 lights, lasers, metronome, buzzer, etc. This can be reached from any mode at any
 time by pressing the button. THis mode will continue indefinitely until the
 button is pressed again (this can be thought of as a pseudo-off state).

 It's worth noting that if this was later implemented in Raspberry Pi, one
 could just turn the whole thing off.

*/


////////////////
// LIBRARIES //
//////////////

#include "I2Cdev.h"
#include "MPU6050.h"
#define OUTPUT_READABLE_ACCELGYRO

#if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
    #include "Wire.h"
#endif

///////////////////////////
// VARIABLE DEFINITIONS //
/////////////////////////

/* THINGS THAT WERE REMOVED FROM THE PREVIOUS VERSION:

currReading, prevReading, time, outputState, outPin

*/

// accelerometer definitions:
MPU6050 accelgyro; // chip
int16_t ax, ay, az; // accelerometer data.
int16_t gx, gy, gz;


// pin definitions:
#define buttonPin 5
#define hapticPin 13
#define laserPin 7
#define buzzerPin 3

// state definitions:
bool inState_Walking = true; // first state is walking state
bool inState_VibrationPrompt = false;
bool inState_FogRecovery = false;
bool inState_Paused = false;

// misc.
long timer = 0; // used for many things, primarily to keep track of time.
long debounceTime = 200; // delay used in tandem with debounce.

bool debounce = false; // used to help eliminate noise when registering steps
short stepCounter = 0; // used to count steps.


// CHANGE THESE TO CHANGE THE DURATION OF THE CODE AND STUFF
int stepThreshold = 20000; // threshold required for accelerometer to pass
int stepsRequired = 13; // steps required for person to do per amount of time
int stepInterval = 10000; // length of the step check
int vibrationRate = 375; // rate of vibration for both vibrate() and metronome()
int vibrationInterval = 4000; // length of the vibration prompt phase


////////////////////////
// ARDUINO MAIN CODE //
//////////////////////

void setup() {

  // Serial Monitor Setup:
  Serial.begin(38400);


  // accelerometer setup:
  #if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
    Wire.begin();
  #elif I2CDEV_IMPLEMENTATION == I2CDEV_BUILTIN_FASTWIRE
    Fastwire::setup(400, true);
  #endif

  Serial.print("Initializing I2C devices...");
  accelgyro.initialize();
  Serial.println(" ..successful.");

  Serial.print("Testing device connections..");
  Serial.println(accelgyro.testConnection() ?
  " ..MPU6050 connection successful." : "MPU60050 connection failed.");

  // pin setup:
  pinMode(buttonPin, INPUT);
  pinMode(hapticPin, OUTPUT);
  pinMode(laserPin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
}

void loop() {

  delay(10);

  if (isWalking()) {
    walkingState(stepInterval);
  }

  if (isVibrating()) {
    vibrationState(vibrationInterval);
  }

  if (isRecovering()) {
    recoveryState(stepInterval);
  }

  if (isPaused()) {
    pausedState();
  }
}


///////////////////////
// HELPER FUNCTIONS //
/////////////////////

/* returns true if the system is in the walking state. */
bool isWalking() {
  if (inState_Walking) {
    return true;
  } else {
    return false;
  }
}


/* returns true if the system is in the vibration prompt state. */
bool isVibrating() {
  if (inState_VibrationPrompt) {
    return true;
  } else {
    return false;
  }
}


/* returns true if the system is in the FoG recovery state. */
bool isRecovering() {
  if (inState_FogRecovery) {
    return true;
  } else {
    return false;
  }
}


/* returns true if the system is in the paused state. */
bool isPaused() {
  if (inState_Paused) {
    return true;
  } else {
    return false;
  }
}


/* returns true if the button has been pressed. */
bool isButtonPressed() {
  if (digitalRead(buttonPin) == 1) {
    return true;
  } else {
    return false;
  }
}


/* returns true if the patient's gait is okay. runs for 't' milliseconds. If
the patient is in the recovery state, the isRecovering boolean should be set
to true. If in the walking state, should be set to false. */
bool isWalkingOk(int t, bool isRecovering) {

  if (isRecovering) {
    Serial.println("Attempting to recover patient.");
    metronome(vibrationRate);
  }

  Serial.print("Checking walking pattern for .");
  Serial.print(t);
  Serial.println(" milliseconds.");

  timer = 0;

  while (timer < t) {

    timer = timer + 10;
    delay(10);

    if (isButtonPressed()) {
      changeToPausedState();
      return true;
    } else {

      accelgyro.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);

      // step check!
      if (tookStep()) {
        stepCounter++;
        debounce = true;

        printStepCount();

        // not looking at accelerometer for 200 ms, takes noise out of data
        delay(debounceTime);
        timer = timer + debounceTime; // offset to avoid delay/timer mismatch
        debounce = false;
      }
    }
  }

  // currently, the recovery mode only lasts for 10 seconds, regardless if the
  // patient's gait is back to normal.
  if (isRecovering) {
    return true;
  }

  if (stepCounter < stepsRequired) {
    stepCounter = 0; // reset
    return false; // patient did not meet amount of steps required
  } else {
    stepCounter = 0; // reset
    return true; // patient is ok
  }
}


/* returns true if the person did a registerable step. Edit the threshold and
other parameters at the top of the script if you want to adjust them. */
bool tookStep() {
  if (ay > stepThreshold && debounce == false) {
    return true;
  } else {
    return false;
  }
}


/* prints the step count so far in the cycle. */
void printStepCount() {
  Serial.print("Step Count: ");
  Serial.println(stepCounter);
}


/* vibrates the haptics for t milliseconds. */
void vibrate(int t) {

  digitalWrite(hapticPin, HIGH); // turns on vibrator

  delay(t);
  timer = timer + t;

  digitalWrite(hapticPin, LOW); // turns off vibrator

  delay(t);
  timer = timer + t;
}


/* vibrates the haptics and buzzes the buzzer for t milliseconds. Please edit
parameters at the top of the script to adjust the vibration pattern frequency.*/
void metronome(int t) {

  digitalWrite(hapticPin, HIGH); // turns on vibrator
  tone(buzzerPin, 1000); // turns on buzzer

  delay(t);
  timer = timer + t;

  digitalWrite(hapticPin, LOW); // turns off vibrator
  noTone(buzzerPin); // turns off buzzer

  delay(t);
  timer = timer + t;
}


/* the following helper functions just change between states. I got tired of
writing the boolean assignments over and over, so.. */
void changeToPausedState() {
  inState_Walking = false;
  inState_VibrationPrompt = false;
  inState_FogRecovery = false;
  inState_Paused = true;
}

void changeToWalkingState() {
  inState_Walking = true;
  inState_VibrationPrompt = false;
  inState_FogRecovery = false;
  inState_Paused = false;
}

void changeToVibrationState() {
  inState_Walking = false;
  inState_VibrationPrompt = true;
  inState_FogRecovery = false;
  inState_Paused = false;
}

void changeToRecoveryState() {
  inState_Walking = false;
  inState_VibrationPrompt = false;
  inState_FogRecovery = true;
  inState_Paused = false;
}


/* the "meat" of the code. These are the functions that dictate what the arduino
should do in each state. */

void walkingState(int t) {

  Serial.println("In Walking State.");
  delay(1000);

  digitalWrite(laserPin, HIGH);
  debounce = false;

  if (isButtonPressed()) {
    changeToPausedState();
  }

  if (!isWalkingOk(t, false)) {
    changeToVibrationState();
  }
}

void vibrationState(int t) {
  digitalWrite(laserPin, HIGH);

  timer = 0;

  while (timer < t) {
    vibrate(vibrationRate);
  }

  if (isVibrating()) {
    changeToRecoveryState();
  }
}

void recoveryState(int t) {

  Serial.println("In FoG Recovery State.");
  digitalWrite(laserPin, HIGH);
  debounce = false;

  if (isWalkingOk(t, true)) {
    changeToWalkingState();
  }
}

void pausedState() {
  Serial.println("In Paused State.");
  digitalWrite(laserPin, LOW);

  delay(3000);

  while (true) {
    if (isButtonPressed()) {
      changeToWalkingState();
      break;
    }
  }
}
