import time #important for delays
import mpu6050

def main():
    
    while True:
        print(mpu6050.acceleration_toString(2));
        time.sleep(1);


main();
