"""
Buzzer.py
Code by Sammy Haq
https://github.com/sammyhaq

Class for using a buzzer with Raspberry Pi GPIO pins.
Can also be used for a vibrating motor, or haptic feedback
device as well. No resistor needed. Connect positive end to
a BCM pin of your choice and the negative to ground.

"""

import RPi.GPIO as GPIO
from time import sleep
from time import time as timer

class Buzzer:


    # Constructor.
    def __init__(self, pin):

        self.pin = pin;

        GPIO.setmode(GPIO.BCM);
        GPIO.setup(self.pin, GPIO.OUT);


    # Vibrates/Sounds the device for a length of time (seconds).
    def vibrate(self, duration):
        GPIO.output(self.pin, GPIO.HIGH);
        sleep(duration);
        GPIO.output(self.pin, GPIO.LOW);


    # Vibrates/Sounds the device for a certain length of time continuously. Delay
    # between the vibrations/sounds are set via the delay variable.
    def metronome(self, pitch, delay, duration):

        GPIO.setup(self.pin, GPIO.OUT);

        timerEnd = timer() + duration;

        while timer() < timerEnd:
            self.vibrate(delay);
            sleep(delay);

