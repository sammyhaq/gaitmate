"""
trainModel_main.py
Code by Sammy Haq

Driver code for the system to just collect data, making a new file every 5 seconds.
Takes 4 data points per second.

"""


import time
import Gaitmate
import RPi.GPIO as GPIO


def main():
    # PINOUT
    # Buzzer:  PIN 11   BCM 17
    # Haptic:  PIN 13   BCM 27
    # LED:     PIN 22   BCM 25
    # Button:  PIN 31   BCM 6
    # Laser:   PIN 29   BCM 5
    ##

    controller = Gaitmate.Gaitmate(0x68, 17, 27, 6, 5, 25)

    try:
        while True:
            controller.ledAction().toggleOn()

            # Collecting new dataset every 5 seconds, 4 points a second,
            # 4 decimal places..
            isCollecting = controller.collectData(5, 4, 4)

            controller.writerAction().closeWriter()

            if (isCollecting):
                continue
            else:
                time.sleep(5)

                while True:
                    if (controller.buttonAction().isPressed()):
                        controller.ledAction().toggleOn()
                        time.sleep(3)
                        isCollecting = True
                        break

    except KeyboardInterrupt:
        if not (controller.writerAction().isClosed()):
            controller.writerAction().closeWriter()

        controller.ledAction().toggleOff()
        GPIO.cleanup()


main()
