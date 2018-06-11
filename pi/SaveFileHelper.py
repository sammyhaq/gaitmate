"""
SaveFileHelper.py
Code by Sammy Haq

Class for saving x,y,z data from a .csv-like file.
The functionality of this program is shown in saveFileTester.py

"""

class SaveFileHelper():

    # Constructor
    def __init__(self, filename):
        self.filename = filename;
        self.file = open(filename, "w");

    # Writes a line to the file.
    def writeToFile(self, line):
        self.file.write(line);

    # Writes given float variables to the line.
    def writeData(self, x, y, z ):
        self.writeToFile("%.3f,%.3f,%.3f\n" %(float(x), float(y), float(z)));

    # Good practice to close the writer after one is done with it.
    def closeHelper(self):
        self.file.close();
