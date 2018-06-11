import Gaitmate

def main():
    controller = Gaitmate.Gaitmate(0x68, 27, 17, 22);

#    controller.testBuzzer();
#    controller.testHaptic();
#    controller.testGyro();
    controller.testButton();
main();


