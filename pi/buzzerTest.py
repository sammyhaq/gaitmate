# NOTE: KEEP BUZZER AT 3.3 V OTHERWISE YOU'LL FRY IT OKAY

import RPi.GPIO as GPIO
from time import sleep
import buzzer as Buzzer

def main():
    
    buzzer = Buzzer.Buzzer(27);
    buzzer.metronome(1000, 0.375, 5, True);

    GPIO.cleanup();

main();
