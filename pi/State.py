
class State():

    # Constructor.
    def __init__(self, int time):
        self.time = time;
        self.currentState = "";

    # Gets the type of the State.
    def getCurrentState(self):
        return self.currentState;

    # Boolean returns for simple comparisions.
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

    # Functions to change the type of the current state.
    def changeToWalkingState(self):
        self.currentState = "walking";

    def changeToVibratingState(self):
        self.currentState = "vibrating";

    def changeToRecoveryState(self):
        self.currentState = "recovering";

    def changeToPausedState(self):
        self.currentState = "paused";

    # Execution of the State. Abstract method to define in child classes.
    def doState(self):
        pass

