"""
Gaitmate.py
Code by Sammy Haq
https://github.com/sammyhaq

Class for pulling all of the libraries defined in this folder together.
Contains everything, from the primary assignment of pins to creating a save buffer
to save the data collected. Basically, this .py acts as the front end for all of
the other code. This may be the first thing to try to edit if something goes wrong.

"""


import State as State
import RPi.GPIO as GPIO
import time
import MPU6050
import Buzzer
import Button
import Laser
import LED
import SaveFileHelper
import LoadFileHelper

class Gaitmate:

    def __init__(self, gyroAddress, buzzerPin, hapticPin, buttonPin, laserPin, ledPin):

        self.gyroAddress = gyroAddress;
        self.buzzerPin = buzzerPin;
        self.hapticPin = hapticPin;
        self.buttonPin = buttonPin;
        self.laserPin = laserPin;
        self.ledPin = ledPin;

        self.state = State.State();
        self.gyro = MPU6050.MPU6050(self.gyroAddress);
        self.buzzer = Buzzer.Buzzer(self.buzzerPin
        self.haptic = Buzzer.Buzzer(self.hapticPin);
        self.button = Button.Button(self.buttonPin); 
        self.laser = Laser.Laser(self.laserPin);
        self.led = LED.LED(self.ledPin);
       

    # accessors, just to clean up code..
    def buzzerAction(self):
        return self.buzzer;

    def gyroAction(self):
        return self.gyro;

    def hapticAction(self):
        return self.haptic;
    
    def buttonAction(self):
        return self.button;

    def laserAction(self):
        return self.laser;

    def ledAction(self):
        return self.led;

    def writerAction(self):
        return self.writer;

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

        
    # Collects Data for a certain period of time at a certain frequency.
    def collectData(self, duration, collectionFrequency):
        
        
        # Initializing write file to have the name of the local time and date.
        self.writer = SaveFileHelper.SaveFileHelper(time.strftime("%m-%d-%y_%H_%M_%S", localtime()));

        timerEnd = time.time() + duration;
        delay = 1.0/collectionFrequency;

        while (time() < timerEnd()):
             writerAction().appendToBuffer(
                     gyroAction().getAccel_X(2),
                     gyroAction().getAccel_Y(2),
                     gyroAction().getAccel_Z(2));

             time.sleep(delay);

        writerAction().dumpBuffer();
    #
    # Test Code. Previously separate main() files, consolidated here.
    #
    def testBuzzer(self):
        print("Testing buzzer..");
        self.buzzerAction().metronome(1000, 0.375, 5);
        print("\t.. done.");

    def testGyro(self):
        print("Testing Gyro..");

        timerEnd = time.time() + 5;

        while time.time() < timerEnd:
            print(self.gyroAction().acceleration_toString(2));
            time.sleep(1);

        print("\t.. done.");

    def testHaptic(self):
        print("Testing haptics..");
        self.hapticAction().metronome(1000, 0.375, 5);
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

    def testLaser(self):
        print("Testing Laser..");
        print("Will turn on/off continuously. Press ctrl+c to exit.");

        try:
            while True:
                self.laserAction().toggle(GPIO.HIGH);
                time.sleep(0.2);
                self.laserAction().toggle(GPIO.LOW);
                time.sleep(0.2);
        except KeyboardInterrupt:
            print("\t.. done.");

    def testLED(self):
        print("Testing LED..");
        print("Will pulse continuously. Press ctrl+c to exit.");

        try:
            self.ledAction().breathe();
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
