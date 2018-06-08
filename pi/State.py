from enum import Enum

class State():

    #
    # Constructor.
    #
    def __init__(self, int time):
        self.time = time;
        self.currentState = StateType.WALKING; # Initial State is Walking.

    # Gets the type of the State.
    def getCurrentState(self):
        return self.currentState;

    #
    # Boolean functions. Returns true if State() is in respective current state.
    #
    def isWalking(self):
        if (self.currentState == StateType.WALKING):
            return True;
        else:
            return False;

    def isVibrating(self):
        if (self.currentState  == StateType.VIBRATING):
            return True;
        else:
            return False;

    def isRecovering(self):
        if (self.currentState == StateType.RECOVERING):
            return True;
        else:
            return False;

    def isPaused(self):
        if (self.currentState == StateType.PAUSED):
            return True;
        else:
            return False;

    #
    # Functions to change the type of the current state.
    #
    def changeToWalkingState(self):
        self.currentState = StateType.WALKING;

    def changeToVibratingState(self):
        self.currentState = StateType.VIBRATING;

    def changeToRecoveryState(self):
        self.currentState = StateType.RECOVERING;

    def changeToPausedState(self):
        self.currentState = StateType.PAUSED;


    # 
    # State Decision and Execution Code.
    #
    def doState(self):

        if (isWalking()):
            doWalkingState();

        if (isVibrating()):
            doVibratingState();

        if (isRecovering()):
            doRecoveringState();

        if (isPaused()):
            doPausedState();

    # Walking State driver code
    def doWalkingState(self):

    # Vibrating State driver code
    def doVibratingState(self):

    # Recovery State driver code
    def doRecoveringState(self);

    # Paused State driver code
    def doPausedState(self):


class StateType(Enum):
    WALKING = 1;
    VIBRATING = 2;
    RECOVERING = 3;
    PAUSED = 4;



