"""
State.py
Code by Sammy Haq
https://github.com/sammyhaq

--
PASTED FROM ARDUINO IMPLEMENTATION:

 The following code is organized into "states". The system can only be in one
 state at a time. The states are explained below:

 "Walking": The system is currently checking if the patient's gait is normal
 or not. Current configuration checks to see if the patient makes 13 steps
 within 10 seconds. If the patient is successful, then the system will loop
 into the "walking" state again. If not, the system will go into the "vibration
 prompt" state.

 "Vibration Prompt": The system is prompting the patient for a response: to
 them that their gait is suboptimal. If the patient presses the button within
 a certain amount of time, then the system will go into the "paused" state. If
 not , the system will continue to the "FoG Recovery" state. During this state,
 a vibration will be played (via the vibrate() function).

 "FoG Recovery": In this state, the patient is not responsive and can be
 assumed to require gait assistance. In this current state, the previous
 vibration will play in tandem with a metronome at an adjustable frequency.
 This is to aid the patient with walking to a rhythm. This mode will continue
 for 10 seconds. After this, the mode will reset to the "walking" state.

 "Paused": The paused state suspends all functions. Everything turns off --
 lights, lasers, metronome, buzzer, etc. This can be reached from any mode at
 any time by pressing the button. This mode will continue indefinitely until
 the button is pressed again (this can be thought of as a pseudo-off state).

 It's worth noting that if this was later implemented in Raspberry Pi, one
 could just turn the whole thing off.

 """

from enum import Enum


class State:


    class StateType(Enum):
        WALKING = 1
        VIBRATING = 2
        RECOVERING = 3
        PAUSED = 4

    #
    # Constructor.
    #
    def __init__(self, currentState=StateType.WALKING):
        self.currentState = currentState  # Default State is walking.
        self.prevState = None

    # Gets the type of the State.
    def getCurrentState(self):
        return self.currentState

    def getPreviousState(self):
        return self.prevState

    #
    # Boolean functions. Returns true if State() is in respective state.
    #
    def isWalking(self):
        if (self.currentState == self.StateType.WALKING):
            return True
        else:
            return False

    def isVibrating(self):
        if (self.currentState == self.StateType.VIBRATING):
            return True
        else:
            return False

    def isRecovering(self):
        if (self.currentState == self.StateType.RECOVERING):
            return True
        else:
            return False

    def isPaused(self):
        if (self.currentState == self.StateType.PAUSED):
            return True
        else:
            return False

    #
    # Functions to change the type of the current state.
    #
    def changeState(self, stateType):
        self.previousState = self.currentState
        self.currentState = stateType

    #
    # Prints what state the system is currently in.
    #
    def printState(self):
        if (isWalking()):
            print("Walking State")
        if (isVibrating()):
            print("Vibrating State")
        if (isRecovering()):
            print("Recovery State")
        if (isPaused()):
            print("Paused State")
