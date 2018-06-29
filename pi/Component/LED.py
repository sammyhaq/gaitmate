"""
LED.py
Code by Sammy Haq
https://github.com/sammyhaq

Child class of OutputComponent that adds exclusive functions to LEDs.

"""

from OutputComponent import OutputComponent
import time


class LED(OutputComponent):
    def __init__(self, pin):
        OutputComponent.__init__(self, pin)

    def breathe(self, duration=5, delay=0.05):
        self.pulse.start(0)

        timerEnd = time.time() + duration

        while (time.time() < timerEnd):
            for dutyCycle in range(0, 101, 5):
                self.pulse.ChangeDutyCycle(dutyCycle)
                time.sleep(delay)
            for dutyCycle in range(100, -1, -5):
                self.pulse.ChangeDutyCycle(dutyCycle)
                time.sleep(delay)
