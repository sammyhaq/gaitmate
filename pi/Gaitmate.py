import State as State
import time
import mpu6050
import Buzzer

class Gaitmate:

    def __init__(self, buzzerPin, hapticPin, buttonPin):
        self.state = State();

        setBuzzerPin(buzzerPin);
        setHapticPin(hapticPin);
        setButtonPin(buttonPin);

        self.State = State();
        self.MPU6050 = MPU6050.MPU6050();
        self.buzzer = Buzzer.Buzzer(getBuzzerPin());
        self.haptic = Buzzer.Buzzer(getHapticPin());
    #
    # Assigns/Retrives input integer to the the pin of the corresponding part.
    # Important for successful state operation.
    #
    def setBuzzerPin(self, int pin):
        self.buzzerPin = pin;

    def setHapticPin(self, int pin):
        self.hapticPin = pin;

    def setButtonPin(self, int pin):
        self.buttonPin = pin;

    def getBuzzerPin(self):
        return self.buzzerPin;

    def getHapticPin(self):
        return self.hapticPin;

    def getButtonPin(self):
        return self.buttonPin;
    
    def getState(self):
        return self.State;


    def execute(self):
        while True:

            time.sleep(0.5);

            if (getState().isWalking()):
                doWalkingState();

            else if (getState().isVibrating()):
                doVibratingState();

            else if (getState().isRecovering()):
                doRecoveringState();

            else if (getState().isPaused()):
                doPausedState();

    # Walking State driver code
    def doWalkingState(self):

    # Vibrating State driver code
    def doVibratingState(self):

    # Recovery State driver code
    def doRecoveringState(self);

    # Paused State driver code
    def State(self):
