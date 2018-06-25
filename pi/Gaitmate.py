"""
Gaitmate.py
Code by Sammy Haq
https://github.com/sammyhaq

Class for pulling all of the libraries defined in this folder together.
Contains everything, from the primary assignment of pins to creating a save 
buffer to save the data collected. Basically, this .py acts as the front end
for all of the other code. This may be the first thing to try to edit if
something goes wrong.

"""

from sklearn.tree import DecisionTreeClassifier
from sklearn.externals import joblib
from sklearn.metrics import classification_report, confusion_matrix
import sys
import State
import RPi.GPIO as GPIO
import time
import MPU6050
import Button
import SaveFileHelper
import LoadFileHelper
import OutputComponent


class Gaitmate:

    def __init__(self,
                 gyroAddress,
                 buzzerPin,
                 hapticPin,
                 buttonPin,
                 laserPin,
                 ledPin):

        self.gyroAddress = gyroAddress
        self.buzzerPin = buzzerPin
        self.hapticPin = hapticPin
        self.buttonPin = buttonPin
        self.laserPin = laserPin
        self.ledPin = ledPin

        self.state = State.State()
        self.gyro = MPU6050.MPU6050(self.gyroAddress)
        self.buzzer = OutputComponent.OutputComponent(self.buzzerPin)
        self.haptic = OutputComponent.OutputComponent(self.hapticPin)
        self.button = Button.Button(self.buttonPin)
        self.laser = OutputComponent.OutputComponent(self.laserPin)
        self.led = OutputComponent.OutputComponent(self.ledPin)
        
        self.clf = joblib.load('dTreeExport.pkl')

    # accessors, just to clean up code..

    def buzzerAction(self):
        return self.buzzer

    def gyroAction(self):
        return self.gyro

    def hapticAction(self):
        return self.haptic

    def buttonAction(self):
        return self.button

    def laserAction(self):
        return self.laser

    def ledAction(self):
        return self.led

    def writerAction(self):
        return self.writer

    #
    # Assigns/Retrives input integer to the the pin of the corresponding part.
    # Important for successful state operation.
    #
    def getBuzzerPin(self):
        return self.buzzerPin

    def getHapticPin(self):
        return self.hapticPin

    def getButtonPin(self):
        return self.buttonPin

    def getGyroAddress(self):
        return self.gyroAddress

    def getState(self):
        return self.State

    # Collects Data for a certain period of time at a certain frequency.
    # Returns true if the button is not pressed. Returns false if the button is
    # pressed.

    def collectData(self, duration, collectionFrequency, accuracy):

        if (collectionFrequency == 0):
            collectionFrequency = 1  # default to 1 collection per second 

        if (duration == 0):
            return

        # Initializing write file to have the name of the local time and date.
        fileName = time.strftime(
            "/home/pi/gaitmate/pi/logs/%m-%d-%y_%H%M%S", time.localtime())
        print("Creating " + fileName + "..")

        self.writer = SaveFileHelper.SaveFileHelper(fileName)

        timerEnd = time.time() + duration
        delay = 1.0/float(collectionFrequency)

        while (time.time() < timerEnd):
            self.writerAction().appendToBuffer(
                self.gyroAction().getAccel_X(accuracy),
                self.gyroAction().getAccel_Y(accuracy),
                self.gyroAction().getAccel_Z(accuracy))

            # Code that stops script when button is pressed.
            if (self.buttonAction().isPressed()):
                self.ledAction().toggleOff()
                time.sleep(3)
                self.writerAction().dumpBuffer()
                return False

            time.sleep(delay)

        print("Saving and creating a new filename..")
        self.writerAction().dumpBuffer()
        return True

    #
    # Test Code. Previously separate main() files, consolidated here.
    #
    def testBuzzer(self):
        print("Testing buzzer..")
        self.buzzerAction().metronome(0.375, 5)
        print("\t.. done.\n")

    def testGyro(self):
        print("Testing Gyro..")

        timerEnd = time.time() + 5

        while time.time() < timerEnd:
            print(self.gyroAction().acceleration_toString(4))
            time.sleep(1)

        print("\t.. done.\n")

    def testHaptic(self):
        print("Testing haptics..")
        self.hapticAction().metronome(0.375, 5)
        print("\t.. done.\n")

    def testButton(self):
        print("Testing Button..")
        print("Will loop continuously. Press ctrl+c to exit.")
        try:

            while True:
                if (self.buttonAction().isPressed()):
                    print("Button is pressed!")
                else:
                    print("Button is not pressed.")
                time.sleep(0.2)

        except KeyboardInterrupt:
            print("\t.. done.\n")

    def testLaser(self):
        print("Testing Laser..")
        print("Will turn on/off continuously. Press ctrl+c to exit.")

        try:
            while True:
                self.laserAction().step(0.2)
        except KeyboardInterrupt:
            print("\t.. done.\n")

    def testLED(self):
        print("Testing LED..")
        print("Will pulse continuously. Press ctrl+c to exit.")

        try:
            self.ledAction().metronome(0.375, 5)
        except KeyboardInterrupt:
            print("\t.. done.\n")

    # Execution loop of the Gaitmate.
    def execute(self):
        while True:

            time.sleep(0.5)

            if (getState().isWalking()):
                doWalkingState()

            if (getState().isVibrating()):
                doVibratingState()

            if (getState().isRecovering()):
                doRecoveringState()

            if (getState().isPaused()):
                doPausedState()

    #
    # Walking State driver code
    #
    def doWalkingState(self):
        time.sleep(0.5)
        self.state.changeState(State.StateType.PAUSED)
        self.ledAction().toggleOn()

        if (self.checkWalking()):
            # If walking okay, do walking state.
            self.doWalkingState()
        else:
            # if walking badly, do vibrating state.
            self.doVibratingState()

    #
    # Vibrating State driver code
    #
    def doVibratingState(self):
        time.sleep(0.5)
        self.state.changeState(State.StateType.VIBRATING)
        self.ledAction().toggleOn()
        self.hapticAction().metronome(0.375, 5)

        if (self.checkWalking()):
            # If walking okay, do walking state.
            self.doWalkingState()
        else:
            # If walking badly, do recovery state.
            self.doRecoveringState()

    #
    # Recovery State driver code
    #
    def doRecoveringState(self):
        time.sleep(0.5)
        self.state.changeState(State.StateType.RECOVERING)
        self.ledAction().toggleOn()
        self.laserAction().toggleOn()
        self.hapticAction().metronome(0.375, 5)
        self.buzzerAction().metronome(0.375, 5)

        if (self.checkWalking()):
            # If walking okay, do walking state.
            self.doWalkingState()
        else:
            # If walking badly, do recovery state.
            self.doRecoveringState()

    #
    # Paused State driver code
    #
    def doPausedState(self):
        time.sleep(3)
        self.state.changeState(State.StateType.RECOVERING)
        self.ledAction().toggleOff()
        self.laserAction().toggleOff()
        
        while True:
            time.sleep(0.5)
            if (not buttonNotPressed):
                self.doWalkingState()

    def checkWalking(self):
        # Collect Data for 5 seconds.
        buttonNotPressed = self.collectData(5, 4, 4)
        filename = self.writerAction.filename
        self.writerAction.closeWriter()

        # button not pressed returns true if the button wasn't pressed during
        # collection.
        if (buttonNotPressed):

            # Checking to see if patient is walking okay.
            loader = LoadFileHelper.LoadFileHelper(filename)
            X = [loader.getDataVariance_X(),
                 loader.getDataVariance_Y(),
                 laoder.getDataVariance_Z()]

            # If patient is walking correctly, return true.
            if (str(self.clf.predict(np.array(X))) == "walking"):
                return True
            # If patient is not walking okay, return false.
            else:
                return False

        # If button is pressed, change to paused state.
        else:
            self.doPausedState()
