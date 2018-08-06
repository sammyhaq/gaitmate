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
from Automata.State import State
import RPi.GPIO as GPIO
import time
from HaqPi.Component.OutputComponent import OutputComponent
from HaqPi.Component.MPU6050 import MPU6050
from HaqPi.Component.Button import Button
from HaqPi.Component.LED import LED
from HaqPi.Component.Buzzer import Buzzer
from FileHelper.SaveFileHelper import SaveFileHelper
from FileHelper.LoadFileHelper import LoadFileHelper
import numpy as np
from multiprocessing import Process, Pipe
from HaqPyTools import UI
from InitSettings import InitSettings as settings


class Gaitmate:

    def __init__(self,
                 gyroAddress, buzzerPin,
                 hapticPin,
                 buttonPin,
                 laserPin,
                 ledPin):

        self.gyroAddress = gyroAddress
        self.buzzerPin = buzzerPin
        self.hapticPin = hapticPin

        self.hapticPin2 = None
        if (settings.enableSecondHaptic):
            self.hapticPin2 = settings.secondaryHapticPin

        self.buttonPin = buttonPin
        self.laserPin = laserPin
        self.ledPin = ledPin

        self.state = State(State.StateType.PAUSED)
        self.gyro = MPU6050(self.gyroAddress)
        self.buzzer = Buzzer(self.buzzerPin)
        self.haptic = OutputComponent(self.hapticPin)

        self.haptic2 = None
        if (settings.enableSecondHaptic):
            self.haptic2 = OutputComponent(self.hapticPin2)

        self.button = Button(self.buttonPin)
        self.laser = OutputComponent(self.laserPin)
        self.led = LED(self.ledPin)

        self.metronomeDelay = ((float(60)/settings.numberOfSteps) -
        (settings.stepdownDelay))
        
        if (self.metronomeDelay <= 0):
            print("\t**ERROR** Not a valid numberOfSteps defined in" +
                  " InitSettings.py. Exiting..")
            sys.exit(0)

        self.clf = joblib.load(
            '/home/pi/gaitmate/pi/MachineLearn/dTreeExport.pkl')
        self.predictedResult = None
        self.prevPredictedResult = None

    # Component accessors.
    def buzzerAction(self):
        return self.buzzer

    def gyroAction(self):
        return self.gyro

    def hapticAction(self):
        return self.haptic

    def haptic2Action(self):
        return self.haptic2

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

    def getHaptic2Pin(self):
        return self.hapticPin2

    def getButtonPin(self):
        return self.buttonPin

    def getGyroAddress(self):
        return self.gyroAddress

    def getState(self):
        return self.state

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
        # print("Creating " + fileName + "..")

        self.writer = SaveFileHelper(fileName)

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
                self.writerAction().dumpBuffer()
                return False

            time.sleep(delay)

        # print("Saving and creating a new filename..")
        self.writerAction().dumpBuffer()
        return True

    #
    # Test Code. Previously separate main() files, consolidated here.
    #
    def testBuzzer(self):
        print("Testing buzzer..")
        self.buzzerAction().metronome(self.metronomeDelay, 5,
                                      settings.stepdownDelay)
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

        p1 = Process(target=self.hapticAction().metronome,
                     args=(self.metronomeDelay, 5, settings.stepdownDelay))
        p1.start()

        if (settings.enableSecondHaptic):
            p2 = Process(target=self.haptic2Action().metronome,
                         args=(self.metronomeDelay, 5, settings.stepdownDelay))
            p2.start()

            print("secondary haptic enabled. Joining processes..")

            p1.join()
            p2.join()

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
                if (settings.laserToggle):
                    self.laserAction().step(0.2)
                else:
                    print("\tLaserToggle is set to off in InitSettings.py. " +
                          "Exiting..")
                    break
        except KeyboardInterrupt:
            print("\t.. done.\n")

    def testLED(self):
        print("Testing LED..")
        print("Will pulse continuously. Press ctrl+c to exit.")

        try:
            self.ledAction().metronome(self.metronomeDelay, 5)
        except KeyboardInterrupt:
            print("\t.. done.\n")

    #
    # Main Execution loop of the Gaitmate.
    #
    def execute(self):
        while True:

            if (self.getState().isWalking()):
                self.doWalkingState()

            if (self.getState().isVibrating()):
                self.doVibratingState()

            if (self.getState().isRecovering()):
                self.doRecoveringState()

            if (self.getState().isPaused()):
                self.doPausedState()

    #
    # Walking State driver code
    #
    def doWalkingState(self):
        UI.box(["Entering Walking State"])
        time.sleep(settings.walkingState_entryDelay)
        self.state.changeState(self.state.StateType.WALKING)
        self.ledAction().toggleOn()
        self.laserAction().toggleOff()

        recv_end, send_end = Pipe(False)

        isWalkOk = self.checkWalking(send_end)

        if (isWalkOk):
            # If walking okay, do walking state.
            self.doWalkingState()
        else:
            # if walking badly, do vibrating state.
            self.doVibratingState()

    #
    # Vibrating State driver code
    #
    def doVibratingState(self):
        UI.box(["Entering Vibrating State"])
        time.sleep(settings.vibrationState_entryDelay)
        self.state.changeState(self.state.StateType.VIBRATING)
        self.ledAction().toggleOn()

        recv_end, send_end = Pipe(False)

        p1 = Process(target=self.hapticAction().metronome,
                     args=(self.metronomeDelay,
                           settings.vibrationState_Duration
                           )
                     )
        p1.start()

        p2 = Process(target=self.checkWalking,
                     args=(send_end,
                           settings.vibrationState_Duration
                           )
                     )
        p2.start()

        if (settings.enableSecondHaptic):
            p3 = Process(target=self.haptic2Action().metronome,
                         args=(self.metronomeDelay,
                               settings.vibrationState_Duration
                               )
                         )
            p3.start()

            p1.join()
            p2.join()
            p3.join()
        
        else:
            p1.join()
            p2.join()

        if (recv_end.recv()):
            # If walking okay, do walking state.
            self.doWalkingState()
        else:
            # If walking badly, do recovery state.
            self.doRecoveringState()

    #
    # Recovery State driver code
    #
    def doRecoveringState(self):
        UI.box(["Entering Recovering State"])
        self.state.changeState(self.state.StateType.RECOVERING)
        self.ledAction().toggleOn()

        if (settings.laserToggle):
            self.laserAction().toggleOn()
        else:
            self.laserAction().toggleOff()

        recv_end, send_end = Pipe(False)
        p1 = Process(target=self.hapticAndBuzzerMetronome,
                     args=(self.metronomeDelay, settings.stepdownDelay))
        p1.start()

        while True:
            p2 = self.checkWalking(send_end, process=p1)

            if (recv_end.recv()):
                # If walking okay, do walking state.
                p1.terminate()
                self.hapticAction().toggleOff()

                if (settings.enableSecondHaptic):
                    self.haptic2Action().toggleOff()

                self.buzzerAction().toggleOff()
                self.doWalkingState()
            else:
                # If walking badly, do recovery state.
                recv_end, send_end = Pipe(False)

    # Buzzer and haptic driver code as one singular process, to cut down on
    # multiprocessing time.
    def hapticAndBuzzerMetronome(self, delay, stepdownDelay=0.375):
        while True:
            GPIO.output(self.hapticPin, GPIO.HIGH)
            if (settings.enableSecondHaptic):
                GPIO.output(self.hapticPin2, GPIO.HIGH)
            GPIO.output(self.buzzerPin, GPIO.HIGH)
            time.sleep(stepdownDelay)
            GPIO.output(self.hapticPin, GPIO.LOW)
            if (settings.enableSecondHaptic):
                GPIO.output(self.hapticPin2, GPIO.LOW)
            GPIO.output(self.buzzerPin, GPIO.LOW)
            time.sleep(delay)

    #
    # Paused State driver code
    #
    def doPausedState(self):
        UI.box(["Entering Paused State"])
        self.ledAction().toggleOff()
        self.laserAction().toggleOff()
        time.sleep(settings.pausedState_entryDelay)
        self.state.changeState(self.state.StateType.PAUSED)

        # button checking time reduced because data collection is discarded
        # here. Only important thing is button press boolean
        buttonNotPressed = self.collectData(settings.checkDuration, 4, 4)

        while True:
            time.sleep(0.5)
            if (not buttonNotPressed):
                self.doWalkingState()
            else:
                buttonNotPressed = self.collectData(settings.checkDuration,
                                                    4, 4)

    def checkWalking(self, send_end,
                     duration=settings.checkDuration,
                     process=None):
        print("\tChecking gait..")

        # Collect Data for 5 seconds.
        buttonNotPressed = self.collectData(duration, 4, 4)
        filename = self.writerAction().filename
        self.writerAction().closeWriter()

        # button not pressed returns true if the button wasn't pressed during
        # collection.
        if (buttonNotPressed):

            # Checking to see if patient is walking okay.
            loader = LoadFileHelper(filename)
            loader.parseData()
            X = [loader.getDataVariance_X(),
                 loader.getDataVariance_Y(),
                 loader.getDataVariance_Z()]

            self.prevPredictedResult = self.predictedResult
            self.predictedResult = self.clf.predict(
                np.array(X).reshape(1, -1))[0]

            if ((self.predictedResult == "standing" and
                 self.prevPredictedResult == "standing") or
                (self.predictedResult == "shuffling" and
                 self.prevPredictedResult == "shuffling")):
                send_end.send(False)
                return False
            else:
                send_end.send(True)
                return True

        # If button is pressed, change to paused state.
        else:
            if process is not None:
                process.terminate()
                self.hapticAction().toggleOff()
                if (settings.enableSecondHaptic):
                    self.haptic2Action().toggleOff()
                self.buzzerAction().toggleOff()
            self.doPausedState()
