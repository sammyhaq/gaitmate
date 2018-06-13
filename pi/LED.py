"""
LED.py
Code by Sammy Haq
https://github.com/sammyhaq

Simple class for using a LED with Raspberry Pi GPIO pins.
LEDs are unidirectional, meaning it matters which way the pins
go in the breadboard/whatever you're circuiting to. No resistor needed.

"""

import RPi.GPIO as GPIO
from time import sleep
from enum import Enum


class LED:

    # Constructor
    def __init__(self, pin):

        self.pin = pin;
        GPIO.setmode(GPIO.BCM);

        GPIO.setup(self.pin, GPIO.OUT);
        GPIO.output(self.pin, GPIO.LOW);

        self.pulse = GPIO.PWM(self.pin, 1000);
        self.pulse.start(0);


    # Turns the LED on or off.
    #  ON: switchVar -> GPIO.HIGH
    #  OFF: switchVar -> GPIO.LOW
    def toggle(self, switchVar):
        if (switchVar == GPIO.HIGH):
            GPIO.output(self.pin, GPIO.HIGH);
        else:
            GPIO.output(self.pin, GPIO.LOW);


    # Slowly pulses the LED. Displays how PWM can be used in essentially
    # any BCM pin.
    def breathe(self):
        while True:
            for dutyCycle in range(0, 101, 4):
                self.pulse.ChangeDutyCycle(dutyCycle);
                sleep(0.05);
            for dutyCycle in reversed(range(0, 101, 4)):
                self.pulse.ChangeDutyCycle(dutyCycle);
                sleep(0.05);
        sleep(1);


    # Use this to nicely clean up this entire class after you're done.
    def destroy(self):
        pulse.stop();
        GPIO.output(self.pin, GPIO.HIGH);
        GPIO.cleanup();
