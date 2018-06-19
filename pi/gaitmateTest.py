"""
gaitmateTest.py
Code by Sammy Haq
https://github.com/sammyhaq

Simple driver code for all of the test functions in Gaitmate.py.

"""

import Gaitmate
import RPi.GPIO as GPIO


def main():
    # PINOUT
    #
    # Buzzer:  PIN 11   BCM 17
    # Haptic:  PIN 13   BCM 27
    # LED:     PIN 22   BCM 25
    # Button:  PIN 31   BCM 6
    # Laser:   PIN 29   BCM 5
    ##

    controller = Gaitmate.Gaitmate(0x68, 17, 27, 6, 5, 25)

    controller.testBuzzer()
    controller.testHaptic()
    controller.testGyro()
    controller.testButton()
    controller.testLaser()
    controller.testLED()
    GPIO.cleanup()


main()
