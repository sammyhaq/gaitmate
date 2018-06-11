import RPi.GPIO as GPIO

class Button():

    def __init__(self, pin):
       
        self.pin = pin;

        GPIO.setmode(GPIO.BCM);
        GPIO.setup(self.pin, GPIO.IN);


    def isPressed(self):
        pressed = (GPIO.input(self.pin));

        if (pressed):
            return True;
        else:
            return False;
