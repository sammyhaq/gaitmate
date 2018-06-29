"""
ledTest.py
Code by Sammy Haq
https://github.com/sammyhaq

Simple driver code to test the LED.

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

    print("=======================")
    print("=  LED TEST CODE")
    print("=======================\n")

    print("Type 'OFF' and press enter to turn the LED off.")
    print("Type 'ON' and press enter to turn the LED on.")
    print("Alternatively, press enter by itself and the LED will toggle.")
    print("Press ctrl+c at any time to exit.\n\n")

    print("Turning on LED..")
    controller.ledAction().toggleOn()
    isLightOn = True
    print("\t..done.\n\n")

    while True:

        try:

            userIn = str(raw_input("Press ctrl+c at any time to exit.\n\n"))

            if (userIn == "ON"):
                if (isLightOn):
                    print("\tLight is already on.\n")
                    userIn = "NULL"
                else:
                    print("Turning on LED..")
                    controller.ledAction().toggleOn()
                    isLightOn = True
                    userIn = "NULL"
                    print("\t..done.\n")
                    continue

            if (userIn == "OFF"):
                if (not isLightOn):
                    print("\tLight is already off.\n")
                    userIn = "NULL"
                else:
                    print("Turning off LED..")
                    controller.ledAction().toggleOff()
                    isLightOn = False
                    userIn = "NULL"
                    print("\t..done.\n")

            if (userIn == ""):
                print("Toggling LED..")

                if (isLightOn):
                    print("\tTurning off LED..")
                    controller.ledAction().toggleOff()
                    isLightOn = False
                    userIn = "NULL"
                    print("\t\t..done.\n")

                else:
                    print("\tTurning on LED..")
                    controller.ledAction().toggleOn()
                    isLightOn = True
                    userIn = "NULL"
                    print("\t\t..done.\n")

        except KeyboardInterrupt:
            print("\n=========")
            print("\n\texiting..\n")
            GPIO.cleanup()
            break


main()
