from OutputComponent import OutputComponent
import time
import RPi.GPIO as GPIO

class Buzzer(OutputComponent):
    def __init__(self, pin, dutyCycle=66):
        OutputComponent.__init__(self, pin)

        self.pulse = GPIO.PWM(self.pin, 440)
        self.pulse.stop()
        self.dutyCycle = dutyCycle

    def tone(self, frequency, duration=0.25):
        if (frequency == 0):
            self.pulse.stop()
            time.sleep(duration)
            return

        else:
            self.pulse.start(self.dutyCycle)
            self.pulse.ChangeFrequency(frequency)
            time.sleep(duration)
            self.pulse.stop()

    def test(self):
        pitches = [262, 330, 392, 523, 1047]
        duration = [0.2, 0.2, 0.2, 0.2, 0.5]

        for i in range(len(pitches)):
            self.tone(pitches[i], duration[i])
            time.sleep(duration[i] * 0.5)
