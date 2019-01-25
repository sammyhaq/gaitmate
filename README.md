# GaitMate
By: Zach Samalonis, Jess Montelone, Abigail Balster, Sammy Haq

Developed for the RESNA 2018 Student Design Competition. Won second place and receiver of the TREAT Award (most likely to market).

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

#### [`observer.py`](pi/observer.py)
Simple driver code that displays the current inferred state from the machine
learning algorithm, and the previous inferred state. Useful for debugging false
negatives, false positives, and other decision-making errors while
not running the entire [Main](pi/Main.py) code.

#### [`resetGPIO.py`](pi/resetGPIO.py)
Simple driver code to reset all GPIO pins.

#### [`componentTest.py`](pi/componentTest.py)
This is a simple driver code for testing all of the components for the Gaitmate.
This ensures that the functions defined in `Gaitmate.py` are working properly.
nano MPU6050.py
```
To run any python script (`ledTest.py`,`trainModel_main.py`, `gaitmateTest.py`), enter in the following:
```
python gaitmateTest.py
```
