import smbus
import math
import time

"""
MPU6050 registers and addresses.
"""
PWR_MGMT_1 = 0x6b;
PWR_MGMT_2 = 0x6c;


ACCEL_XOUT_H = 0x3b;
ACCEL_XOUT_L = 0x3c;

ACCEL_YOUT_H = 0x3d;
ACCEL_YOUT_L = 0x3e;

ACCEL_ZOUT_H = 0x3f;
ACCEL_ZOUT_L = 0x40;


TEMP_OUT_H = 0x41;
TEMP_OUT_L = 0x42;


GYRO_XOUT_H = 0x43;
GYRO_XOUT_L = 0x44;

GYRO_YOUT_H = 0x45;
GYRO_YOUT_L = 0x46;

GYRO_ZOUT_H = 0x47;
GYRO_ZOUT_L = 0x48;


SMPLRT_DIV = 0x19; 
CONFIG = 0x1a;

"""
MISC SETUP
"""
bus = smbus.SMBus(1);
address = 0x68; # from i2cdetect


# initializes a couple of addresses to a default value.
def MPU6050_init():
    bus.write_byte_data(address, pwrMgmt_1, 0); # waking power from sleep
    bus.write_byte_data(address, SMPLRT_DIV, 7); # delays the sample rate as to not be too taxing
    bus.write_byte_data(address, CONFIG, 0); #disables DLPF, make any value besides 0 or 7 to enable


# reads and returns raw data from MPU6050.
def read_raw_data(addr):
    high = bus.read_byte_data(address, addr);
    low = bus.read_byte_data(address, addr+1);

    value = ( (high << 8) | low);

    # getting signed value
    if (value > 32768):
        value = value - (32768 * 2);

    return value;

"""
Getters that take raw data, round it to a specified decimal, and return.
"""
def getAccel_X(decimal):
    return round((read_raw_data(ACCEL_XOUT_H)/16384.0), decimal);

def getAccel_Y(decimal):
    return round((read_raw_data(ACCEL_YOUT_H)/16384.0), decimal);

def getAccel_Z(decimal):
    return round((read_raw_data(ACCEL_ZOUT_H)/16384.0), decimal);

def getGyro_X(decimal):
    return round((read_raw_data(GYRO_XOUT_H)/16384.0), decimal);

def getGyro_Y(decimal):
    return round((read_raw_data(GYRO_YOUT_H)/16384.0), decimal);

def getGyro_Z(decimal):
    return round((read_raw_data(GYRO_ZOUT_H)/16384.0), decimal);

# returns the acceleration data as a formatted, printable string.
def acceleration_toString(decimal):
    
    ax = getAccel_X(decimal);
    ay = getAccel_Y(decimal);
    az = getAccel_Z(decimal);

    toReturn = 'a_x: {0}, a_y: {1}, a_z: {2}'.format(ax, ay, az);

    return toReturn;


