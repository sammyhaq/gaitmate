"""
LoadFileHelper.py
Code by Sammy Haq
https://github.com/sammyhaq

Class for loading x,y,z data from a .csv-like file.
The functionality of this program is shown in loadFileTester.py

"""
import math
import numpy as np

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

                self.magnitude.append(math.sqrt(math.pow(float(parsedLine[0]), 2) +
                    math.pow(float(parsedLine[1]), 2) +
                    math.pow(float(parsedLine[2]), 2)))
            except ValueError:
                continue
            except IndexError:
                continue

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

    def getDataVariance(self):
        return np.var(self.getData_Magnitude())

    def getDataVariance_X(self):
        return np.var(self.getData_X())

    def getDataVariance_Y(self):
        return np.var(self.getData_Y())

    def getDataVariance_Z(self):
        return np.var(self.getData_Z())



        
