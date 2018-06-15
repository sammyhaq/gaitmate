"""
ledTest.py
Code by Sammy Haq

Simple driver code to make the LED always stay on.

"""

import Gaitmate
import RPi.GPIO as GPIO

def main():
    
    ## PINOUT ##
    # Buzzer:  PIN 11   BCM 17
    # Haptic:  PIN 13   BCM 27
    # LED:     PIN 15   BCM 22
    # Button:  PIN 31   BCM 6
    # Laser:   PIN 29   BCM 5
    ##

    controller = Gaitmate.Gaitmate(0x68, 17, 27, 6, 5, 22);

    print("=======================");
    print("=  LED TEST CODE");
    print("=======================\n");

    print("Type 'OFF' and press enter to turn the LED off.");
    print("Type 'ON' and press enter to turn the LED on.");
    print("Alternatively, press enter by itself and the LED will toggle.");
    print("Press ctrl+c at any time to exit.\n\n");
    
    print("Turning on LED..");
    controller.ledAction().toggle(GPIO.HIGH);
    isLightOn = True;
    print("\t..done.\n\n");

    while True:

        try:

            userIn = str(raw_input("Press ctrl+c at any time to exit.\n\n"));

            if (userIn == "ON"):
                if (isLightOn == True):
                    print("\tLight is already on.\n");
                    userIn = "NULL";
                else:
                    print("Turning on LED..");
                    controller.ledAction().toggle(GPIO.HIGH);
                    isLightOn = True;
                    userIn = "NULL";
                    print("\t..done.\n");
                    continue;

            if (userIn == "OFF"):
                if (isLightOn == False):
                    print("\tLight is already off.\n");
                    userIn = "NULL";
                else:
                    print("Turning off LED..");
                    controller.ledAction().toggle(GPIO.LOW);
                    isLightOn = False;
                    userIn = "NULL";
                    print("\t..done.\n");

            if (userIn == ""):
                print("Toggling LED..");
                
                if (isLightOn):
                    print("\tTurning off LED..");
                    controller.ledAction().toggle(GPIO.LOW);
                    isLightOn = False;
                    userIn = "NULL";
                    print("\t\t..done.\n");

                else:
                    print("\tTurning on LED..");
                    controller.ledAction().toggle(GPIO.HIGH);
                    isLightOn = True;
                    userIn = "NULL";
                    print("\t\t..done.\n");


        except KeyboardInterrupt:
            print("\n=========");
            print("\n\texiting..\n");
            GPIO.cleanup();
            break;
        

    

main();
