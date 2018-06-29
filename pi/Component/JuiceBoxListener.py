import RPi.GPIO as GPIO
import os
from HaqPyTools import UI

class JuiceBoxListener:

    # Constructor
    def __init__(self, pin, controller):

        self.pin = pin

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        # adds a listener that keeps watching the battery pin. Triggers
        # lowBattery_callbackFunction if battery is low.
        GPIO.add_event_detect(self.pin, GPIO.RISING, callback=self.lowBattery_callbackFunction)

    # Triggers if the battery is low.
    def lowBattery_callbackFunction(self):
        GPIO.cleanup()

        # if writer isn't closed yet, close it
        if (not controller.writerAction().isClosed()):
            controller.writerAction().closeWriter()

        controller.ledAction().breathe(30, 0.005)
        os.system("sudo shutdown -h now")


