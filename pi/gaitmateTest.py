import Gaitmate

def main():
    controller = Gaitmate.Gaitmate(0x68, 27, 17, 22, 23);

#    controller.testBuzzer();
#    controller.testHaptic();
#    controller.testGyro();
#    controller.testButton();
    controller.testLaser();
    
main();


