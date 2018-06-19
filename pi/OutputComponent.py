"""
OutputComponent.py
Code by Sammy Haq
https://github.com/sammyhaq

Class for using any output device with Raspberry Pi GPIO pins.
Contains PWM stuff. Used for buttons, lasers, LEDs, haptics,
you name it.

"""

import RPi.GPIO as GPIO
import time


class OutputComponent:

    # Constructor.
    def __init__(self, pin):

        self.pin = pin

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

#        self.pulse = GPIO.PWM(self.pin, 1000);
#        self.pulse.start(0);

    def toggleOn(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def toggleOff(self):
        GPIO.output(self.pin, GPIO.LOW)

    # Vibrates/Sounds the device for a length of time (sec).
    def step(self, duration):
        GPIO.output(self.pin, GPIO.HIGH)
        time.sleep(duration)
        GPIO.output(self.pin, GPIO.LOW)
        time.sleep(duration)

    # Vibrates/Sounds the device for a certain length of time continuously.
    # Delay between the vibrations/sounds are set via the delay variable.
    def metronome(self, delay, duration):

        timerEnd = time.time() + duration

        while (time.time() < timerEnd):
            self.step(delay)

    def breathe(self):
        while True:
            for dutyCycle in range(0, 101, 4):
                self.pulse.ChangeDutyCycle(dutyCycle)
                sleep(0.05)
            for dutyCycle in reversed(range(0, 101, 4)):
                self.pulse.ChangeDutyCycle(dutyCycle)
                sleep(0.05)
        sleep(1)

    def __destroy__(self):
        self.pulse.stop()
        GPIO.output(self.pin, GPIO.HIGH)
        GPIO.cleanup()
