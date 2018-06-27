from Gaitmate import Gaitmate
from JuiceBoxListener import JuiceBoxListener
import gpioReset


def main():
    controller = Gaitmate(0x68, 17, 27, 6, 5, 25)
    jBoxListener = JuiceBoxListener(16, controller)
    
    controller.execute()

main()
