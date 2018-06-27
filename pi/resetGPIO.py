import RPi.GPIO as GPIO
import State
import MPU6050
import OutputComponent
import Button

def main():

    GPIO.setwarnings(False);
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

    state = State.State()
    gyro = MPU6050.MPU6050(gyroAddress)
    buzzer = OutputComponent.OutputComponent(buzzerPin)
    haptic = OutputComponent.OutputComponent(hapticPin)
    button = Button.Button(buttonPin)
    laser = OutputComponent.OutputComponent(laserPin)
    led = OutputComponent.OutputComponent(ledPin)

    GPIO.cleanup()
    print("\t..done.\n");

main()
