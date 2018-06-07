
class State():

    #
    # Constructor.
    #
    def __init__(self, int time):
        self.time = time;
        self.currentState = "";

    # Gets the type of the State.
    def getCurrentState(self):
        return self.currentState;

    #
    # Boolean functions. Returns true if State() is in respective current state.
    #
    def isWalking(self):
        if (self.currentState == "walking"):
            return True;
        else:
            return False;

    def isVibrating(self):
        if (self.currentState  == "vibrating"):
            return True;
        else:
            return False;

    def isRecovering(self):
        if (self.currentState == "recovering"):
            return True;
        else:
            return False;

    def isPaused(self):
        if (self.currentState == "paused"):
            return True;
        else:
            return False;

    #
    # Functions to change the type of the current state.
    #
    def changeToWalkingState(self):
        self.currentState = "walking";

    def changeToVibratingState(self):
        self.currentState = "vibrating";

    def changeToRecoveryState(self):
        self.currentState = "recovering";

    def changeToPausedState(self):
        self.currentState = "paused";


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


