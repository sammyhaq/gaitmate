from abc import ABC, abstractmethod


class State(ABC):

    # Constructor.
    def __init__(self, int time):
        self.time = time;
        self.type = "";

    # Gets the type of the State.
    def getType(self):
        return self.name;

    # Boolean returns for simple comparisions.
    def isWalking(self):
        if (self.name == "walking"):
            return True;
        else:
            return False;

    def isVibrating(self):
        if (self.name == "vibrating"):
            return True;
        else:
            return False;

    def isRecovering(self):
        if (self.name == "recovering"):
            return True;
        else:
            return False;

    def isPaused(self):
        if (self.name == "paused"):
            return True;
        else:
            return False;

    # Execution of the State. Abstract method to define in child classes.
    @abstractmethod
    def doState(self):
        pass

class WalkingState(State):

    def __init__(self, int time):
        self.time = time;
        self.name = "walking";

    def doState(self):


class VibrationState(State):

    def __init(self, int time):
        self.time = time;
        self.name = "vibrating";

    def doState(self):


