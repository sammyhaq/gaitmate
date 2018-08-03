from Gaitmate import Gaitmate
from HaqPi.Component.JuiceBoxListener import JuiceBoxListener
import resetGPIO
from multiprocessing import Process, Pipe
import time
from InitSettings import InitSettings as settings
import dataCollector

# PINOUT
#
# Buzzer:  PIN 11   BCM 17
# Buzzer2: PIN 36   BCM 16
# Haptic:  PIN 13   BCM 27
# LED:     PIN 22   BCM 25
# Button:  PIN 31   BCM 6
# Laser:   PIN 29   BCM 5
##


def main():
    controller = Gaitmate(0x68, 17, 27, 6, 5, 25)
    jBoxListener = JuiceBoxListener(16, controller)

    recv_end, send_end = Pipe(False)

    p1 = Process(target=controller.ledAction().breathe,
                 args=(settings.startupDuration+1, 0.05))
    p1.start()

    def buttonListener(send_end):
        timerEnd = time.time() + settings.startupDuration
        while (time.time() < timerEnd):

            time.sleep(0.1)
            if (controller.buttonAction().isPressed()):
                send_end.send(True)
                return

        send_end.send(False)

    buttonListener(send_end)

    if (recv_end.recv()):
        p1.terminate()
        controller.buzzerAction().metronome(0.1, 0.3, 0.05)
        dataCollector.execute()
    else:
        controller.execute()


main()
