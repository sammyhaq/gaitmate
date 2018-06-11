import Gaitmate

def main():
    controller = Gaitmate.Gaitmate(0x68, 27, 17, 22);

<<<<<<< HEAD
    controller.testBuzzer();
    controller.testHaptic();
    controller.testGyro();
=======
#    controller.testBuzzer();
#    controller.testHaptic();
#    controller.testGyro();
>>>>>>> fe7225bdf619915ba8e9303e273de7fd117b498c
    controller.testButton();
main();


