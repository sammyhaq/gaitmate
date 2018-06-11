import Gaitmate

def main():
    controller = Gaitmate.Gaitmate(0x68, 27, 17, 0);

#    controller.testBuzzer();
#    controller.testHaptic();
    controller.testGyro();

main();


