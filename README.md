# GaitMate
By: Zach Samalonis, Jess Montelone, Abigail Balster, Sammy Haq

Developed for the RESNA 2018 Student Design Competition.

## Overview

This project's goal is to provide a wearable device for patients with
Parkinson's Disease that aids the recovery of gait initiation failure,
also known as "freezing of gait." Initially developed in Arduino, the
Gaitmate was further developed on the Raspberry Pi Zero W to develop
more robust code and features.

## State Execution
The overall theoretical execution of this device is akin to that of a finate
deterministic automata with 4 states: "walking", "vibrating", "recovering", and
"paused." Details of each state are shown below:

 - *"Walking":* The system is currently checking if the patient's gait is normal
 or not. If the patient is deemed to be walking successfully, then the system will loop
 into the "walking" state again. If not, the system will go into the "vibrating"
 state.

 - *"Vibrating":* The system is prompting the patient for a response: to
 them that their gait is suboptimal. If the patient presses the button within
 a certain amount of time, then the system will go into the "paused" state. If
 not , the system will continue to the "recovering" state. During this state,
 a vibration will be played to gently alert the patient.

 - *"Recovering":* In this current state, the previous
 vibration will play in tandem with a metronome at a suitable walking pace in
 the attempt to help the patient recover to a normal gait. This will continue
 until the patient is sensed to have returned to a normal walking pace, or until
 the button is pressed. If the button is not pressed, the system will go into
 the "paused" state.

 - *"Paused"*: The paused state suspends all device functions. Everything turns off --
 lights, lasers, metronome, buzzer, etc. This can be reached from any mode at
 any time by pressing the button. This mode will continue indefinitely until
 the button is pressed again (this can be thought of as a pseudo-off state).

## Machine Learning Details
This device uses [`scikit-learn`](http://scikit-learn.org)'s implementation of Simple Decision Tree
Learning, which is a supervised machine learning algorithm known for its simple
yet effective classification methods. As machine learning algorithms are
computationally intensive, the learning model is trained on a machine with a
stronger processor than the Pi and saved as [`dTreeExport.pkl`](pi/MachineLearn/dTreeExport.pkl).

The machine learning problem is to determine whether the patient is walking or
standing/shuffling. Training data was recorded via the script shown in
[`trainModel.py`](pi/MachineLearn/trainModel.py), after which a Decision Tree
Model was generated via [`Learner.py`](pi/MachineLearn/Learner.py). After
verifying the model's effectiveness via a confusion-matrix and classification
report, the model was exported and tested for a final time via the real-time
classification code in [`Tester.py`](pi/MachineLearn/Tester.py).

Originally, there were three possible labels/classifications considered:
"walking", "standing", or "shuffling". However, difficulty arose when
differentiating between "shuffling" and "walking", as "shuffling" is such an
intermediary between the two current labels. A potential solution to this problem
would be exploring different machine learning algorithms -- however, increasing
the amount of computation required for this algorithm would be troublesome on
the Raspberry Pi Zero W's limited processor. Another solution would be collecting more data. However, as "shuffling" and "standing" were both considered to be viable
candidates for entering into the recovery phase of the device, they were
inputted into the same model as the same classification to simplify the problem
and increase accuracy.


## File Breakdown (Packages)
The following section was created in order to help explain the structure of the
code and give an inkling as to what the purpose of each .py file in this
workspace is.

### [`arduino/`](arduino/)
This folder contains the older code that ran when the arduino was the core of
the Gaitmate. While this code works, it does not contain the same machine learning
algorithms and datasets that the Raspberry Pi implementation does. It is also
not as robust (class design, etc). 

### [`pi/`](pi/)
This folder contains the code that is required for the Raspberry Pi
implementation of the Gaitmate.

#### [`pi/Automata/`](pi/Automata/)
This package contains the finite deterministic automata-inspired State class,
which is used for much of the decision-making code found in the core code.

#### [`pi/HaqPi/Component/`](pi/HaqPi/Component/)
This package contains all of the object representations of the Raspberry Pi's
onboard components. Although things such as the LEDs, buttons and buzzers can be
implemented by `OutputComponent.py`, the child classes such as `LED.py` contain
expanded functionality exclusive to that component (for example, making the LED
"breathe"). These components are all defined as if they are connected via BCM
pin. Therefore, one should initialize the components pin by their BCM number,
**NOT** by the physical pin number.

Component details (such as function definitions) can be found in their respective files.

#### [`pi/FileHelper/`](pi/FileHelper/)
This package contains both the `SaveFileHelper` and `LoadFileHelper` class,
which are used to save and parse the log files (both for training the
DecisionTree machine learning algorithm and testing it in real-time).

#### [`Gaitmate.py`](pi/Gaitmate.py)
This python class is where all components of the Raspberry Pi come together in
one interface. It contains the initialization for all of the classes, and acts
as the "front-end" for all of the other code. All code is run through this
script. Acting as the controller, `Main.py` calls on this to do most of the
work. It contains the methods for checking walking, state execution, etc.

## File Breakdown (Driver Code)
The files talked about in the previous section are the "foundation" of the code.
If you are unsure as to how to run these, please refer to the 'Terminal
Instructions' in the back of this README.

#### [`Main.py`](pi/Main.py)
This code is the code to execute when running the Gaitmate normally. This script
launches on boot. It links the JuiceBoxListener to the code and assigns pins to
the Gaitmate class controller. After blinking its LED to let the user know it is ready,
it then tells the Gaitmate to start its cycle (in the paused state).

#### [`resetGPIO.py`](pi/resetGPIO.py)
Simple driver code to reset all GPIO pins.

#### [`componentTest.py`](pi/componentTest.py)
This is a simple driver code for testing all of the components for the Gaitmate.
This ensures that the functions defined in `Gaitmate.py` are working properly.


## Terminal Instructions
If you do not know how to navigate a computer using Terminal, don't worry! 
A bunch of resources online exist that can help you out. I recommend the [crash
course by Code Academy](https://www.codeacademy.com/learn/learn-the-command-line/)
to at least get a rudimentary knowledge of everything before you delve deep into
the code here (otherwise, you may get lost).

However, I completely get it if you don't want to spend time learning how to use
a bash shell, I get it. In this section, I'm going to try to give you the bare
minimum Terminal knowledge required to SSH into the Raspberry Pi, navigate to
the project folder, edit files, and run scripts.

### SSHing into the Raspberry Pi
Our Raspberry Pi, 'abba', is reachable through many different avenues -- however,
the most efficient way on her is to SSH into her. This can be easily done
assuming you are on the same wifi network. To begin, type the following into
your Terminal:
```
ssh pi@abba.local
```
'pi' is the username on abba. 'abba.local' refers to the name of the machine.
**Note that this only works if you are on the same wifi network. abba.local is
only understood by your computer if it detects a computer by the name 'abba' on
the wifi network.** If SSH is not successful and you timeout, you can safely 
assume that 1) you and abba are not connected to the same wifi network or 2)
abba is not powered up completely yet.

After this, you will be prompted to enter in a password. The password for abba
is 'gaitmate2018'. If all goes well, you should be greeted with a new Terminal.
You can see if you are in the correct terminal by looking at the user callsign
to the left of your cursor (it should say something along the lines of
'pi@abba', followed by your current working directory).

It's worth noting that as soon as you SSH into abba, you'll find that a script
is automatically running -- this is the main code of the GaitMate. To exit,
simply press 'control + c'. **This is required if you are intending to change
the contents of the code.** 

Now, you might be asking: "Why did you name the Raspberry Pi 'abba', Sammy? Why did
you give the Raspberry Pi a name in the first place?".

To which I just stare blankly back at you, shrug, and take a bite of a bartlett pear I
inexplicably procured from seemingly nowhere. *Mm. __Delicious.__*

### Updating from git
If you're reading this off the Raspberry Pi, updating the code is
probably a good idea because I might be updating a couple things from home now
and then. To update the code simply type:
```
git pull origin master
```
**Note that this requires your information -- this means your username and
password for [GitHub](https://www.github.com/).** If you don't have permission
to access the files (these files are located in a private respository), email me
at sammy.haq1@gmail.com (or just request permission through GitHub).

I currently have auto-pushing to the repository disabled, because I don't want
the master branch to be modified without my knowledge (and proper testing to ensure
it works). If you have an edit to make, please make a merge request so I can
take a look at it before submitting.

### Running a Python Script
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
