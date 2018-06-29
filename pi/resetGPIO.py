import RPi.GPIO as GPIO
from Automata.State import State
from Component.MPU6050 import MPU6050
from Component.OutputComponent import OutputComponent
from Component.Button import Button


def main():

    GPIO.setwarnings(False)
    print("\nResetting all pins..")

    gyroAddress = 0x68
    buzzerPin = 17
    hapticPin = 27
    buttonPin = 6
    laserPin = 5
    ledPin = 25

    gyroAddress = gyroAddress
    buzzerPin = buzzerPin
    hapticPin = hapticPin
    buttonPin = buttonPin
    laserPin = laserPin
    ledPin = ledPin

    state = State()
    gyro = MPU6050(gyroAddress)
    buzzer = OutputComponent(buzzerPin)
    haptic = OutputComponent(hapticPin)
    button = Button(buttonPin)
    laser = OutputComponent(laserPin)
    led = OutputComponent(ledPin)

    GPIO.cleanup()
    print("\t..done.\n")


main()
