"""
LoadFileHelper.py
Code by Sammy Haq
https://github.com/sammyhaq

Class for loading x,y,z data from a .csv-like file.
The functionality of this program is shown in loadFileTester.py

"""
import math
import numpy as np
import os


class LoadFileHelper():

    # Constructor
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, "r")
        self.x = []
        self.y = []
        self.z = []
        self.magnitude = []

    # Returns all the raw data.
    def returnRawFile(self):
        return self.file.read

    # Parses the data and stores all of the corresponding data points in x, y,
    # and z.
    def parseData(self):
        for line in self.file.readlines():
            parsedLine = line.split(",")

            try:

                self.x.append(float(parsedLine[0]))
                self.y.append(float(parsedLine[1]))
                self.z.append(float(parsedLine[2]))

                self.magnitude.append(math.sqrt(
                                      math.pow(float(parsedLine[0]), 2) +
                                      math.pow(float(parsedLine[1]), 2) +
                                      math.pow(float(parsedLine[2]), 2)))
            except ValueError:
                continue
            except IndexError:
                continue

        # snipping rows.. (credit to https://github.com/rollinsjw)
        while (len(self.x) > len(self.z)):
            self.x.pop()
        while (len(self.y) > len(self.z)):
            self.y.pop()

    # returns true if the file is blank. Good for catching files that were
    # touched but not saved.
    def isBlank(self):
        if (os.stat(self.filename).st_size == 0):
            return True
        else:
            return False

    # Returns the x data as a list of floats.
    def getData_X(self):
        return self.x

    # Returns the y data as a list of floats.
    def getData_Y(self):
        return self.y

    # Returns the z data as a list of floats.
    def getData_Z(self):
        return self.z

    # Returns the x, y, z data as a pythagorean magnitude.
    def getData_Magnitude(self):
        return self.magnitude

    # Packages and returns all data as a nested list of floats.
    def getData(self):

        data = []
        data.append(self.x)
        data.append(self.y)
        data.append(self.z)

        return data

    # Returns the pythagorean magnitude's variance.
    def getDataVariance(self):
        return np.var(self.getData_Magnitude())

    # Returns the x variance.
    def getDataVariance_X(self):
        return np.var(self.getData_X())

    # Returns the y data's variance.
    def getDataVariance_Y(self):
        return np.var(self.getData_Y())

    # Returns the z data's variance.
    def getDataVariance_Z(self):
        return np.var(self.getData_Z())
