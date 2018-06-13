# GaitMate
## Zach Samalonis, Jess Montelone, Abigail Balster, Sammy Haq
## Developed for the RESNA 2018 Student Design Competition.

This project's goal is to provide a wearable device for patients with
Parkinson's Syndrome that aids the recovery of gait initiation failure,
also known as "freezing of gait." Initially developed in Arduino, the
Gaitmate was further developed on the Raspberry Pi Zero W to develop
more robust code and features.

The purpose of this README is to help aid in navigation of the project
files, and hopefully provide an overview of how the files interface with
each other.

### TODO:

	- create a method of saving and reading from a text file. Need to be able to store step data over time.
	- Author and mark the top of the pi files so far. Add to comment code if necessary.
	- by GOD, just do the TODO already. Don't be such a lazy about it.

### NOTE:
	- In Pinout, the button sensor pin is set to 22 (BCM 25).

### Ideas on how to implement machine learning algorithm:
	- each file should be its own feature set.
		- if only one number is "allowed", perhaps determine how much
		  the numberset varies throughout the file?
			- Like a lot of variance = walking, low = shuffling,
			  none = standing still, etc.
	- features: x, y, z.
	- labels: walking, shuffling, stopped.





# DIRECTIONS FOR ZACH
	- To get all the updated files:
		- git pull origin master
	- To run the test code:
		- Go to the home directory of the project:
			- cd ~/gaitmate/pi/
		- Run the code:
			- python gaitmateTest.py

