import RPi.GPIO as GPIO
from time import sleep
from time import time as timer

class Buzzer:

    def __init__(self, pin):

        self.pin = pin
        GPIO.setmode(GPIO.BCM);
        GPIO.setup(self.pin, GPIO.IN);
        GPIO.setup(self.pin, GPIO.OUT);

        sleep(0.5);

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


    def metronome(self, pitch, delay, duration, noPitch):

        GPIO.setup(self.pin, GPIO.OUT);

        timerEnd = timer() + duration;

        if (noPitch == True):
            while timer() < timerEnd:
                self.vibrate(delay);
                sleep(delay);

        else:
            while timer() < timerEnd: 
                print("playing pitch.");
                self.playTone(pitch, delay);
                self.playTone(0, delay);


    # Fun stuff in case want to go more in depth with buzzer, but not necessary
    def prepareSong(self):
        GPIO.setup(self.pin, GPIO.OUT);
        x = 0;

    def playSong(self):
        x = 0;
        pitches = [147, 147, 220, 220, 247, 247, 220, 0, 196, 196, 175, 175, 165, 165, 175, 0];
        duration = 0.2;

        for p in pitches:
            self.playTone(4*p, duration);
            sleep(duration*0.5);
            x+=1;


# Example of Playing Twinkle Twinkle, albeit sounds terrible

#def main():
#    buzzer = Buzzer(17);
#
#    buzzer.prepareSong();
#    buzzer.playSong();
#
#    GPIO.cleanup();
#
#main();


