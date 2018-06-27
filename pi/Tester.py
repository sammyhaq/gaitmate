import Gaitmate
import time
from multiprocessing import Pipe
from HaqPyTools import UI
import resetGPIO

def main():

    UI.box(["Tester.py", "Code by Sammy Haq"])
    
    resetGPIO

    controller = Gaitmate.Gaitmate(0x68, 17, 27, 6, 5, 25)

    while True:
        recv_end, send_end = Pipe(False)
        controller.checkWalking(send_end)

        print("\t\t\t" + controller.predictedResult)

main()
