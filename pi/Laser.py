import RPi.GPIO as GPIO
from time import sleep
from time import time as timer
from enum import Enum

class Laser:

    def __init__(self, pin):

        self.pin = pin;
        GPIO.setmode(GPIO.BCM);
        GPIO.setup(self.pin, GPIO.OUT);

    def toggle(self, switchVar):
        if (switchVar == GPIO.HIGH):
            GPIO.output(self.pin, GPIO.HIGH);
        else:
            GPIO.output(self.pin, GPIO.LOW);


