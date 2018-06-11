import State as State
import RPi.GPIO as GPIO
import time
import MPU6050
import Buzzer
import Button

class Gaitmate:

    def __init__(self, gyroAddress, buzzerPin, hapticPin, buttonPin):

        self.gyroAddress = gyroAddress;
        self.buzzerPin = buzzerPin;
        self.hapticPin = hapticPin;
        self.buttonPin = buttonPin;

        self.state = State.State();
        self.gyro = MPU6050.MPU6050(self.gyroAddress);
        self.buzzer = Buzzer.Buzzer(self.buzzerPin);
        self.haptic = Buzzer.Buzzer(self.hapticPin);
        self.button = Button.Button(self.buttonPin); 

    # accessors, just to clean up code..
    def buzzerAction(self):
        return self.buzzer;

    def gyroAction(self):
        return self.gyro;

    def hapticAction(self):
        return self.haptic;
    
    def buttonAction(self):
        return self.button;
    #
    # Assigns/Retrives input integer to the the pin of the corresponding part.
    # Important for successful state operation.
    #
    def getBuzzerPin(self):
        return self.buzzerPin;

    def getHapticPin(self):
        return self.hapticPin;

    def getButtonPin(self):
        return self.buttonPin;

    def getGyroAddress(self):
        return self.gyroAddress;
    
    def getState(self):
        return self.State;

    #
    # Test Code. Previously separate main() files, consolidated here.
    #
    def testBuzzer(self):
        print("Testing buzzer..");
        self.buzzerAction().metronome(1000, 0.375, 5, True);
        print("\t.. done.");

    def testGyro(self):
        print("Testing Gyro..");

        timerEnd = time.timer() + 5;

        while time.timer() < timerEnd:
            print(self.gyroAction().acceleration_toString(2));
            time.sleep(1);

        print("\t.. done.");

    def testHaptic(self):
        print("Testing haptics..");
        self.hapticAction().metronome(1000, 0.375, 5, True);
        print("\t.. done.");
    
    def testButton(self):
        print("Testing Button..");
        print("Will loop continuously. Press ctrl+c to exit.");
        try:

            while True:
                if (self.buttonAction().isPressed()):
                    print("Button is pressed!");
                else:
                    print("Button is not pressed.");
                time.sleep(0.2);

        except KeyboardInterrupt:
            print("\t.. done.");

    # Execution loop of the Gaitmate.
    def execute(self):
        while True:

            time.sleep(0.5);

            if (getState().isWalking()):
                doWalkingState();

            if (getState().isVibrating()):
                doVibratingState();

            if (getState().isRecovering()):
                doRecoveringState();

            if (getState().isPaused()):
                doPausedState();

    # Walking State driver code
    def doWalkingState(self):
        return;

    # Vibrating State driver code
    def doVibratingState(self):
        return;

    # Recovery State driver code
    def doRecoveringState(self):
        return;

    # Paused State driver code
    def State(self):
        return;
<<<<<<< HEAD


=======
>>>>>>> fe7225bdf619915ba8e9303e273de7fd117b498c
