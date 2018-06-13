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
    controller = Gaitmate.Gaitmate(0x68, 27, 17, 22, 23, 23);

    while True:
        controller.collectData(60, 4);
        controller.writerAction().closeWriter();


    except KeyboardInterrupt:
        if !(controller.writerAction().isClosed()):
            controller.writerAction.closeWriter();

        GPIO.cleanup();
