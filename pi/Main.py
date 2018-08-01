from Gaitmate import Gaitmate
from HaqPi.Component.JuiceBoxListener import JuiceBoxListener
import resetGPIO


def main():
    controller = Gaitmate(0x68, 17, 27, 6, 5, 25)
    jBoxListener = JuiceBoxListener(16, controller)

    controller.ledAction().breathe(3, 0.05)
    controller.execute()


main()
