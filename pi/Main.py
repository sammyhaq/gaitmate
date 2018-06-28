from Gaitmate import Gaitmate
from JuiceBoxListener import JuiceBoxListener
import resetGPIO

def main():
    controller = Gaitmate(0x68, 17, 27, 6, 5, 25)
    jBoxListener = JuiceBoxListener(16, controller)

    controller.ledAction().breathe(5, 0.10)
    controller.execute()

main()
