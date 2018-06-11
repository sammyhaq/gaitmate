import RPi.GPIO as GPIO
from time import sleep
from enum import Enum


class LED:

    def __init__(self, pin):

        self.pin = pin;
        GPIO.setmode(GPIO.BCM);

        GPIO.setup(self.pin, GPIO.OUT);
        GPIO.output(self.pin, GPIO.LOW);

        self.pulse = GPIO.PWM(self.pin, 1000);
        self.pulse.start(0);

    def toggle(self, switchVar):
        if (switchVar == GPIO.HIGH):
            GPIO.output(self.pin, GPIO.HIGH);
        else:
            GPIO.output(self.pin, GPIO.LOW);

    def breathe(self):
        while True:
            for dutyCycle in range(0, 101, 4):
                self.pulse.ChangeDutyCycle(dutyCycle);
                sleep(0.05);
            for dutyCycle in reversed(range(0, 101, 4)):
                self.pulse.ChangeDutyCycle(dutyCycle);
                sleep(0.05);
        sleep(1);


    def destroy(self):
        pulse.stop();
        GPIO.output(self.pin, GPIO.HIGH);
        GPIO.cleanup();
