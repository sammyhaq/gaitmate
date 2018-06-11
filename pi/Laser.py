"""
Laser.py
Code by Sammy Haq

Simple class for using a laser (or light) with Raspberry Pi GPIO pins.
No resistor needed. Connect positive end to a BCM pin of your choice
and the negative to ground.

"""


import RPi.GPIO as GPIO
from time import sleep
from time import time as timer
from enum import Enum

class Laser:

    
    # Constructor
    def __init__(self, pin):

        self.pin = pin;
        GPIO.setmode(GPIO.BCM);
        GPIO.setup(self.pin, GPIO.OUT);


    # Toggles the Laser on/off.
    #   ON: switchVar -> GPIO.HIGH
    #   OFF: switchVar -> GPIO.LOW
    def toggle(self, switchVar):
        if (switchVar == GPIO.HIGH):
            GPIO.output(self.pin, GPIO.HIGH);
        else:
            GPIO.output(self.pin, GPIO.LOW);


