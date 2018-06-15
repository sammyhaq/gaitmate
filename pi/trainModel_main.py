"""
trainModel_main.py
Code by Sammy Haq

Driver code for the system to just collect data, making a new file every minute.
Takes 4 data points per second.

"""


#!/usr/bin/env python

import Gaitmate
import RPi.GPIO as GPIO

def main():
    ## PINOUT ##
    # Buzzer:  PIN 11   BCM 17
    # Haptic:  PIN 13   BCM 27
    # LED:     PIN 22   BCM 25
    # Button:  PIN 31   BCM 6
    # Laser:   PIN 29   BCM 5
    ##

    controller = Gaitmate.Gaitmate(0x68, 17, 27, 6, 5, 25);

    try:
        while True:
            # Collecting new dataset every 10 seconds, 4 points a second, 3 decimal places
            controller.collectData(10, 4, 3);
            controller.writerAction().closeWriter();


    except KeyboardInterrupt:
        if not (controller.writerAction().isClosed()):
            controller.writerAction().closeWriter();

        GPIO.cleanup();

main();
