"""
Button.py
Code by Sammy Haq
https://github.com/sammyhaq

Simple class for using a button with Raspberry Pi GPIO pins.
Button should be in series with a resistor before touching ground.

"""

import RPi.GPIO as GPIO


class Button:

    # Constructor
    def __init__(self, pin):

        self.pin = pin

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN)

    # Returns true if the button is being pressed or not.
    def isPressed(self):
        pressed = (GPIO.input(self.pin))

        if (pressed):
            print("\t\t** Button pressed! **")
            return True
        else:
            return False
