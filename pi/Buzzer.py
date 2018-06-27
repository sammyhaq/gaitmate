from OutputComponent import OutputComponent
import time
import RPi.GPIO as GPIO

class Buzzer(OutputComponent):
    def __init__(self, pin):
        OutputComponent.__init__(self, pin)

    def tone(self, pitch, duration=0.25):
        if (pitch == 0):
            time.sleep(duration)
            return

        else:
            period = 1.0 / pitch
            delay = period / 2
            cycles = int(duration * pitch)

            for i in range(cycles):
                GPIO.output(self.pin, GPIO.HIGH)
                time.sleep(delay)
                GPIO.output(self.pin, GPIO.LOW)
                time.sleep(delay)

    def test(self):
        pitches = [262, 330, 392, 523, 1047]
        duration = [0.2, 0.2, 0.2, 0.2, 0.5]

        for i in range(len(pitches)):
            self.tone(pitches[i], duration[i])
            time.sleep(duration[i] * 0.5)
