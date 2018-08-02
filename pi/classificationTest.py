import Gaitmate
import time
from multiprocessing import Pipe
from HaqPyTools import UI
import resetGPIO


def main():

    UI.box(["classificationTest.py", "Code by Sammy Haq"])

    resetGPIO

    controller = Gaitmate.Gaitmate(0x68, 17, 27, 6, 5, 25)

    while True:
        recv_end, send_end = Pipe(False)
        controller.checkWalking(send_end)

        print("\t\t"+time.strftime("[%m/%d/%y | %H:%M:%S]"))
        print("\t\t\tcurrentState: " + controller.predictedResult)

        if (controller.prevPredictedResult is None):
            print("\t\t\tpreviousState: None")
        else:
            print("\t\t\tpreviousState: " + controller.prevPredictedResult)


main()
