"""
State.py
Code by Sammy Haq
https://github.com/sammyhaq

State representation, for pseudo finite-automata execution.

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
