"""
ComponentTester.py
Code by Sammy Haq
https://github.com/sammyhaq

Driver Code to test the connections of the pins in a microcontroller setup.

"""

import Gaitmate
import sys
from HaqPyTools import UI

class ComponentTester:

    def __init__(self):
        buzzerPin = 17 # BCM 17 == PIN 11
        HapticPin = 27 # BCM 27 == PIN 27
        ledPin = 25 # BCM 25 == PIN 22
        buttonPin = 6 # BCM 6 == PIN 31
        laserPin = 5 # BCM 5 == PIN 29
        gyroAddress = 0x68 # get from i2cdetect -y 1
        
        self.pins = {}

        print("\n")
        UI.box([
                "testComponents.py",
                "Code by Sammy Haq",
                "https://github.com/sammyhaq",
                "\n",
                "Simple driver code to test the connections of the pins in a microcontroller setup."
                ])


    def displayCommandLineArgs(self):
        print("\n")
        UI.box(["COMMAND LINE ARGUMENTS:"], indent=1, wrapper="*")
        for k, v in self.pins.items():
            UI.box(["'"+k+"':\t--\tPIN "+str(v)],
                   wrapper = "",
                   indent = 2)

    def parseCommandLineArgs(self):
        if ("--help" in sys.argv):
            self.printHelpMenu()
        else:
            for i in range(0, len(sys.argv)-1, 2):
                try:
                    self.pins[sys.argv[i]] = int(sys.argv[i+1])
                except ValueError:
                        raise InvalidArgumentException("'" + sys.argv[i] + " " + sys.argv[i+1] + "'", "Pin assignment not parseable as 'int'. Type '--help' for options.")


class InvalidArgumentException(Exception):

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

def main():

    tester = ComponentTester()
    tester.parseCommandLineArgs()
    tester.displayCommandLineArgs()

main()

#def testBuzzer(controller):
#    print("Testing buzzer..")
#    controller.buzzerAction().metronome(0.375, 5)
#    print("\t.. done.\n")
#
#
#def testGyro(controller):
#    print("Testing Gyro..")
#
#    timerEnd = time.time() + 5
#
#    while time.time() < timerEnd:
#        print(controller.gyroAction().acceleration_toString(4))
#        time.sleep(1)
#
#    print("\t.. done.\n")
#
#
#def testHaptic(controller):
#    print("Testing haptics..")
#    controller.hapticAction().metronome(0.375, 5)
#    print("\t.. done.\n")
#
#
#def testButton(controller):
#    print("Testing Button..")
#    print("Will loop continuously. Press ctrl+c to exit.")
#    try:
#
#        while True:
#            if (controller.buttonAction().isPressed()):
#                print("Button is pressed!")
#            else:
#                print("Button is not pressed.")
#            time.sleep(0.2)
#
#    except KeyboardInterrupt:
#        print("\t.. done.\n")
#
#
#def testLaser(controller):
#    print("Testing Laser..")
#    print("Will turn on/off continuously. Press ctrl+c to exit.")
#
#    try:
#        while True:
#            controller.laserAction().step(0.2)
#    except KeyboardInterrupt:
#        print("\t.. done.\n")
#
#
#def testLED(controller):
#    print("Testing LED..")
#    print("Will pulse continuously. Press ctrl+c to exit.")
#
#    try:
#        controller.ledAction().metronome(0.375, 5)
#    except KeyboardInterrupt:
#        print("\t.. done.\n")
