# GaitMate
#### Zach Samalonis, Jess Montelone, Abigail Balster, Sammy Haq
#### Developed for the RESNA 2018 Student Design Competition.


### Overview

This project's goal is to provide a wearable device for patients with
Parkinson's Syndrome that aids the recovery of gait initiation failure,
also known as "freezing of gait." Initially developed in Arduino, the
Gaitmate was further developed on the Raspberry Pi Zero W to develop
more robust code and features.

The purpose of this README is to help aid in navigation of the project
files, and hopefully provide an overview of how the files interface with
each other.

### File Breakdown

The following section was created in order to help explain the structure of the
code and give an inkling as to what the purpose of each .py file in this
workspace is.

#### [`arduino/`](arduino/)
This folder contains the older code that ran when the arduino was the core of
the Gaitmate. While this code works, it does not contain the same machine learning
algorithms and datasets that the Raspberry Pi implementation does.  

#### [`pi/`](pi/)
This folder contains the code that is required for the Raspberry Pi
implementation of the Gaitmate.

##### [`Button.py`](pi/Button.py)
This python-defined object represents an input Button component attached via
GPIO pin to the Raspberry Pi, and contains a simple `isPressed()` function. This
function returns true if pressed, and false if not.

The purpose of this button is to "pause" the state of the system, suspending all
functions such as haptics, walk-count, and data collection.

##### [`Gaitmate.py`](pi/Gaitmate.py)
This python class is where all components of the Raspberry Pi come together in
one interface. It contains the initialization for all of the classes, and acts
as the "front-end" for all of the other code. All code is run through this
script.

##### [`gaitmateTest.py`](pi/gaitmateTest.py)
This is a simple driver code for testing all of the components for the Gaitmate.
This ensures that the functions defined in `Gaitmate.py` are working properly.

##### [`ledTest.py`](pi/ledTest.py)
This is a simple standalone driver code for the LED. It is more interactive than
`gaitmateTest.py` and can be used to troubleshoot the LED pin.

##### [`LoadFileHelper.py`](pi/LoadFileHelper.py)
This class is responsible for the loading and parsing of files found in
[`pi/logs`](pi/logs). This is where the data required for machine learning is
saved to to help train the machine to adjust to the person's gait. The
capabilities of this class can be tested by using the driver code found in
[`loadFileTester.py`](pi/loadFileTester.py).

##### [`MPU6050.py`](pi/MPU6050.py)
This class is responsible for all of the accelerometer/gyro/temperature
interpretation code.

##### [`OutputComponent.py`](pi/OutputComponent.py)
This class contains all of the functions every output component has on the GPIO
pins of the Raspberry Pi. This contains (but is not limited to) code for the
Laser, LED, Buzzer, and Haptics.

##### [`resetGPIO.py`](pi/resetGPIO.py)
Simple driver's code to reset all GPIO pins.

##### [`SaveFileHelper.py`](pi/SaveFileHelper.py)
This class is responsible for the saving and writing of files found in
[`pi/logs`](pi/logs). This is where the data required for machine learning is
saved to help train the machine to adjust to the person's gait. The capabilities
of this class can be tested by using the driver code found in
[`saveFileTester.py`](pi/saveFileTester.py).

##### [`State.py`](pi/State.py)

*WIP* 

##### [`trainModel_main.py`](pi/trainModel_main.py)
This driver code contains code for saving data in order to train a machine
learning model. 


### Terminal Instructions (for git and everything)
#### Updating from git
If you're reading this off ABBA (The Raspberry Pi), updating the code is
probably a good idea because I might be updating a couple things from home now
and then. To update the code simply type:
```
git pull origin master
```
**Note that this requires your information -- this means your username and
password for [GitHub](https://www.github.com/).** If you don't have permission to access the files (these files are located in a private respository), email me at sammy.haq1@gmail.com (or just request permission through GitHub).

####
To run any of the python scripts, be sure that you are in the same spot the
files are in.
To view what directory you're currently in when using Terminal, type:
```
pwd
```
If you are not in the right directory, enter in the right directory by typing
the following:
```
cd ~/gaitmate/pi/
```

After this, to view what files are in your current working directory, type:
```
ls
```
These files can be viewed in any text editor. The default one on the Raspberry
Pi is nano -- which you can call directly from terminal. For example, if I
wanted to open MPU6050.py:
```
nano MPU6050.py
```
To run any python script (`ledTest.py`,`trainModel_main.py`, `gaitmateTest.py`), enter in the following:
```
python gaitmateTest.py
```

Let me know if you have any questions via email. If it's immediate, ask Zach for my phone number and just text me (or message me via Facebook).


### SCRATCH NOTES

#### Ideas on how to implement machine learning algorithm:
	- each file should be its own feature set.
		- if only one number is "allowed", perhaps determine how much
		  the numberset varies throughout the file?
			- Like a lot of variance = walking, low = shuffling,
			  none = standing still, etc.
	- features: x, y, z.
	- labels: walking, shuffling, stopped.

