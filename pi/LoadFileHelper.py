"""
LoadFileHelper.py
Code by Sammy Haq

Class for loading x,y,z data from a .csv-like file.
The functionality of this program is shown in loadFileTester.py

"""

class LoadFileHelper():

    # Constructor
    def __init__(self, filename):
        self.filename = filename;
        self.file = open(filename, "r"); 
        self.x = [];
        self.y = [];
        self.z = [];

    # Returns all the raw data.
    def returnRawFile(self):
        return self.file.read

    # Parses the data and stores all of the corresponding data points in x, y, and z.
    def parseData(self):
        for line in self.file.readlines():
            parsedLine = line.split(",");

            print(parsedLine[0]);
            
            self.x.append(float(parsedLine[0]));
            self.y.append(float(parsedLine[1]));
            self.z.append(float(parsedLine[2]));

    # Returns the x data as a list of floats.
    def getData_X(self):
        return self.x;

    # Returns the y data as a list of floats.
    def getData_Y(self):
        return self.y;

    # Returns the z data as a list of floats.
    def getData_Z(self):
        return self.z;

    # Packages and returns all data as a nested list of floats.
    def getData(self):
        data = [];
        data.append(self.x);
        data.append(self.y);
        data.append(self.z);

        return data;
