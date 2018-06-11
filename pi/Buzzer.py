import RPi.GPIO as GPIO
from time import sleep
from time import time as timer

class Buzzer:

    def __init__(self, pin):

        self.pin = pin;

        GPIO.setmode(GPIO.BCM);
        GPIO.setup(self.pin, GPIO.OUT);


    def vibrate(self, duration):
        GPIO.output(self.pin, GPIO.HIGH);
        sleep(duration);
        GPIO.output(self.pin, GPIO.LOW);

    def playTone(self, pitch, duration):

        if (pitch == 0):
            sleep(duration);

            return;

        else:
            period = 1.0 / pitch # cycles/sec

            delay = period / 2;

            cycles = int (duration * pitch); # number of waves to produce

            # Producing the waves..
            for i in range(cycles):
                GPIO.output(self.pin, GPIO.HIGH);
                sleep(delay);
                
                GPIO.output(self.pin, GPIO.LOW);
                sleep(delay);


    def metronome(self, pitch, delay, duration):

        GPIO.setup(self.pin, GPIO.OUT);

        timerEnd = timer() + duration;

        if (noPitch == True):
            while timer() < timerEnd:
                self.vibrate(delay);
                sleep(delay);

